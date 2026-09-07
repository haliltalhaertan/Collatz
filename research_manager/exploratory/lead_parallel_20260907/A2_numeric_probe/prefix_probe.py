#!/usr/bin/env python3
"""prefix_probe.py -- exploratory numerical probe ([NUM] evidence only).

Implements, independently of every other checker in the repository, the objects of
research_manager/exploratory/prefix_bridge_20260906/derivation/EXACT_PREFIX_REDUCTION.md:

  e_M(x) = exp(2 pi i x / M);  r >= 5, n >= 0;  z uniform on weak compositions of n
  into r parts, a_i = z_i + 1, A_0 = 0, A_j = sum_{i<=j} a_i,
  B_r(a) = sum_{s=1}^r 3^(r-s) 2^(A_(s-1)),   F_r = e_(16 3^r)(B_r),  G_(r,n) = E[F_r | sum z = n].
  m = r-4, j = z_1+..+z_4,
  D_j       = (1/C(j+3,3))       sum_{x_1+..+x_4=j} e_1296(B_4(x+1)),
  H_(m,k)(j)= (1/C(k+m-1,m-1))   sum_{y_1+..+y_m=k} e_(3^(m+4))(2^j B_m(y+1)),
  w_(r,n)(j)= C(j+3,3) C(n-j+m-1,m-1) / C(n+r-1,r-1),
  (M)  G_(r,n) = sum_{j=0}^n w(j) D_j H_(r-4,n-j)(j).
  Critical target n_r = floor(beta r) - 8, beta = log2(3) - 1, r >= 14.
  rho = beta/(1+beta), L_r = ceil(4 (1+delta) ln r / |ln rho|), truncation error <= 4 r^(-1-delta).
  OPEN target  S_r = sum_{j<=min(n_r,L_r)} w(j) |D_j| |H_(r-4,n_r-j)(j)|.

Algorithm.  Every phase factorises over positions:
  3^(m-s) 2^t / (c 3^m) = (2^t mod c 3^s) / (c 3^s),   t = j + (s-1) + Y_(s-1),
(c = 16 for the direct observable, c = 81 for the tail factor whose modulus is 3^(m+4) = 81 3^m),
so the sum over weak compositions is a transfer-matrix DP over (position, cumulative excess)
whose transition is a prefix sum.  Residues are exact Python integers; each residue is turned into
one complex128 phase; accumulation is complex128.  A high-precision (mpmath, 30 digits) scalar
re-implementation of the same DP is used to bound rounding error.

Nothing in this file proves any bound or the Collatz conjecture.

Usage (all outputs are written next to this file):
  python prefix_probe.py verify              -> VERIFICATION.json
  python prefix_probe.py probe RMAX          -> PROBE_RESULTS.csv, PROBE_RESULTS.json, WINDOW_TABLE.csv, RUN_LOG.txt
  python prefix_probe.py mpcheck             -> MPMATH_CROSSCHECK.json
  python prefix_probe.py sha                 -> SHA256SUMS.txt
"""
import csv
import hashlib
import json
import math
import os
import platform
import sys
import time
from fractions import Fraction

import numpy as np
import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
BETA = math.log2(3.0) - 1.0
RHO = BETA / (1.0 + BETA)
TWO_PI = 2.0 * math.pi
DELTAS = (0.5, 1.0)


# ----------------------------------------------------------------------------- parameters
def n_crit(r):
    """n_r = floor(beta r) - 8, with the floor cross-checked at 50 digits."""
    with mp.workdps(50):
        nb = int(mp.floor(mp.log(3) / mp.log(2) * r - r))
    nf = math.floor(BETA * r)
    if nb != nf:
        raise ArithmeticError(f"floor(beta r) ambiguous at r={r}: {nb} vs {nf}")
    return nb - 8


def L_cut(r, delta):
    return math.ceil(4.0 * (1.0 + delta) * math.log(r) / abs(math.log(RHO)))


def trunc_bound(r, delta):
    return 4.0 * r ** (-1.0 - delta)


# ----------------------------------------------------------------------------- phases
class PhaseCache:
    """phi_s(t) = exp(2 pi i (2^t mod c 3^s) / (c 3^s)) for t >= s-1, cached per (c, s).

    The residues are computed by exact integer doubling; each residue is converted once to a
    correctly rounded double in [0,1) (Python int/int true division) and then to a phase.
    The tables do not depend on r, so they are shared across all r."""

    def __init__(self, c):
        self.c = c
        self.store = {}  # s -> [M, next_t, next_x, list_of_fractions]

    def get(self, s, count):
        """Return complex128 array of phi_s(t) for t = s-1, ..., s-1+count-1."""
        if s not in self.store:
            M = self.c * 3 ** s
            self.store[s] = [M, s - 1, pow(2, s - 1, M), []]
        ent = self.store[s]
        M, t, x, fr = ent
        while len(fr) < count:
            fr.append(x / M)      # exact-rounded double of the exact residue ratio
            x = (x << 1) % M
            t += 1
        ent[1], ent[2] = t, x
        return np.exp(1j * TWO_PI * np.asarray(fr[:count], dtype=np.float64))


PHASE16 = PhaseCache(16)
PHASE81 = PhaseCache(81)


# ----------------------------------------------------------------------------- transfer-matrix DP
def comp_dp(cache, m, nmax, jmax):
    """Unnormalised composition sums (complex128 matrix of shape (jmax+1, nmax+1)):

      V[j, S] = sum over weak compositions y of S into m parts of
                prod_{s=1}^m phi_s(j + (s-1) + Y_(s-1)),   Y_(s-1) = y_1 + ... + y_(s-1).

    cache = PHASE16 : V[0, n] = C(n+m-1, m-1) * G_(m,n)          (direct observable, modulus 16 3^m)
    cache = PHASE81 : V[j, k] = C(k+m-1, m-1) * H_(m,k)(j)       (tail average, modulus 3^(m+4))
    """
    lg10 = (math.lgamma(nmax + m) - math.lgamma(m) - math.lgamma(nmax + 1)) / math.log(10.0)
    if lg10 > 300.0:
        raise OverflowError(f"C({nmax + m - 1},{m - 1}) ~ 1e{lg10:.0f} exceeds the double range")
    V = np.zeros((jmax + 1, nmax + 1), dtype=np.complex128)
    V[:, 0] = 1.0
    idx = np.arange(jmax + 1)[:, None] + np.arange(nmax + 1)[None, :]
    for s in range(1, m + 1):
        tab = cache.get(s, jmax + nmax + 1)
        V *= tab[idx]
        np.cumsum(V, axis=1, out=V)
    return V


def G_direct(r, n):
    V = comp_dp(PHASE16, r, n, 0)
    return complex(V[0, n]) / math.comb(n + r - 1, r - 1)


def D_all(jmax):
    """D_j for j = 0..jmax (D_j equals G_(4,j) by definition)."""
    V = comp_dp(PHASE16, 4, jmax, 0)
    return np.array([complex(V[0, j]) / math.comb(j + 3, 3) for j in range(jmax + 1)])


def H_all(m, n):
    """Matrix H[j, k] = H_(m,k)(j) for 0 <= j, k <= n."""
    V = comp_dp(PHASE81, m, n, n)
    den = np.array([float(math.comb(k + m - 1, m - 1)) for k in range(n + 1)])
    return V / den[None, :]


def weights(r, n):
    m = r - 4
    N = math.comb(n + r - 1, r - 1)
    return np.array([(math.comb(j + 3, 3) * math.comb(n - j + m - 1, m - 1)) / N for j in range(n + 1)])


def mixture_terms(r, n):
    """Returns (w, D, Hdiag, terms) with Hdiag[j] = H_(r-4, n-j)(j) and terms = w D Hdiag."""
    m = r - 4
    w = weights(r, n)
    D = D_all(n)
    H = H_all(m, n)
    Hd = np.array([H[j, n - j] for j in range(n + 1)])
    return w, D, Hd, w * D * Hd


# ----------------------------------------------------------------------------- brute force (independent path)
def compositions(n, parts):
    if parts == 1:
        yield (n,)
        return
    for k in range(n + 1):
        for rest in compositions(n - k, parts - 1):
            yield (k,) + rest


def B_exact(a):
    """B_r(a) = sum_{s=1}^r 3^(r-s) 2^(A_(s-1)) by the literal formula (no Horner)."""
    r = len(a)
    total = 0
    A = 0
    for s in range(1, r + 1):
        total += 3 ** (r - s) * 2 ** A
        A += a[s - 1]
    return total


def e_frac(num, M):
    """e_M(num) computed from the exact reduced residue."""
    return complex(np.exp(1j * TWO_PI * ((num % M) / M)))


def brute_G(r, n):
    M = 16 * 3 ** r
    acc = 0j
    cnt = 0
    for z in compositions(n, r):
        acc += e_frac(B_exact(tuple(x + 1 for x in z)), M)
        cnt += 1
    assert cnt == math.comb(n + r - 1, r - 1)
    return acc / cnt


def brute_D(j):
    acc = 0j
    cnt = 0
    for x in compositions(j, 4):
        acc += e_frac(B_exact(tuple(v + 1 for v in x)), 1296)
        cnt += 1
    return acc / cnt


def brute_H(m, k, j):
    M = 3 ** (m + 4)
    acc = 0j
    cnt = 0
    for y in compositions(k, m):
        acc += e_frac(2 ** j * B_exact(tuple(v + 1 for v in y)), M)
        cnt += 1
    return acc / cnt


def brute_mixture(r, n):
    m = r - 4
    N = math.comb(n + r - 1, r - 1)
    acc = 0j
    wsum = Fraction(0)
    for j in range(n + 1):
        wj = Fraction(math.comb(j + 3, 3) * math.comb(n - j + m - 1, m - 1), N)
        wsum += wj
        acc += float(wj) * brute_D(j) * brute_H(m, n - j, j)
    assert wsum == 1
    return acc


# ----------------------------------------------------------------------------- mpmath re-implementation
def comp_dp_mp(c, m, n, j, dps=30):
    """Scalar mpmath version of comp_dp restricted to one frequency j and endpoint n.
    Returns the normalised average (mpc)."""
    with mp.workdps(dps):
        V = [mp.mpc(0)] * (n + 1)
        V[0] = mp.mpc(1)
        for s in range(1, m + 1):
            M = c * 3 ** s
            x = pow(2, j + s - 1, M)
            for S in range(n + 1):
                V[S] = V[S] * mp.expjpi(2 * mp.mpf(x) / M)
                x = (x << 1) % M
            acc = mp.mpc(0)
            for S in range(n + 1):
                acc = acc + V[S]
                V[S] = acc
        return V[n] / mp.mpf(math.comb(n + m - 1, m - 1))


def G_direct_mp(r, n, dps=30):
    return comp_dp_mp(16, r, n, 0, dps)


def D_mp(j, dps=30):
    return comp_dp_mp(16, 4, j, 0, dps)


def H_mp(m, k, j, dps=30):
    return comp_dp_mp(81, m, k, j, dps)


def mpc_to_complex(z):
    return complex(float(z.real), float(z.imag))


# ----------------------------------------------------------------------------- tasks
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def env_info():
    return {
        "python": sys.version,
        "numpy": np.__version__,
        "mpmath": mpmath.__version__,
        "platform": platform.platform(),
        "beta": BETA,
        "rho": RHO,
        "abs_ln_rho": abs(math.log(RHO)),
    }


def task_verify():
    t0 = time.perf_counter()
    out = {"classification": "[NUM] finite mechanical verification of the implementation; not a theorem",
           "environment": env_info()}

    # (A) mixture identity (M) vs direct DP, r in [5,30], n in [0,12]
    worst = 0.0
    worst_at = None
    cnt = 0
    for r in range(5, 31):
        for n in range(0, 13):
            g = G_direct(r, n)
            _, _, _, terms = mixture_terms(r, n)
            d = abs(g - terms.sum())
            cnt += 1
            if d > worst:
                worst, worst_at = d, (r, n)
    out["A_mixture_vs_direct"] = {"r_range": [5, 30], "n_range": [0, 12], "cases": cnt,
                                  "max_abs_discrepancy": float(worst), "worst_case_rn": worst_at,
                                  "pass_1e-12": bool(worst <= 1e-12)}

    # (B) brute-force enumeration vs DP and vs mixture, r in [5,8], n in [0,4]
    worst_dir = worst_mix = worst_bm = 0.0
    cnt = 0
    paths = 0
    for r in range(5, 9):
        for n in range(0, 5):
            gb = brute_G(r, n)
            gd = G_direct(r, n)
            _, _, _, terms = mixture_terms(r, n)
            gm = terms.sum()
            gbm = brute_mixture(r, n)
            worst_dir = max(worst_dir, abs(gb - gd))
            worst_mix = max(worst_mix, abs(gb - gm))
            worst_bm = max(worst_bm, abs(gb - gbm))
            cnt += 1
            paths += math.comb(n + r - 1, r - 1)
    out["B_bruteforce"] = {"r_range": [5, 8], "n_range": [0, 4], "cases": cnt, "paths_enumerated": paths,
                           "max_abs_brute_minus_directDP": float(worst_dir),
                           "max_abs_brute_minus_mixtureDP": float(worst_mix),
                           "max_abs_brute_minus_bruteMixture": float(worst_bm),
                           "pass_1e-12": bool(max(worst_dir, worst_mix, worst_bm) <= 1e-12)}

    # (C) brute-force H and D vs DP for small parameters
    worstH = 0.0
    cntH = 0
    for m in range(1, 5):
        for k in range(0, 5):
            for j in range(0, 9):
                hb = brute_H(m, k, j)
                hd = complex(H_all(m, max(k, j))[j, k])
                worstH = max(worstH, abs(hb - hd))
                cntH += 1
    worstD = 0.0
    Dd = D_all(10)
    for j in range(0, 11):
        worstD = max(worstD, abs(brute_D(j) - complex(Dd[j])))
    out["C_bruteforce_H_D"] = {"H_cases": cntH, "H_m_range": [1, 4], "H_k_range": [0, 4], "H_j_range": [0, 8],
                               "max_abs_H_discrepancy": float(worstH), "D_j_range": [0, 10],
                               "max_abs_D_discrepancy": float(worstD),
                               "pass_1e-12": bool(max(worstH, worstD) <= 1e-12)}

    # (D) exact weight normalisation and float-weight accuracy on the verification grid
    wmax = 0.0
    for r in range(5, 31):
        for n in range(0, 13):
            m = r - 4
            N = math.comb(n + r - 1, r - 1)
            exact = [Fraction(math.comb(j + 3, 3) * math.comb(n - j + m - 1, m - 1), N) for j in range(n + 1)]
            assert sum(exact) == 1
            w = weights(r, n)
            wmax = max(wmax, max(abs(float(e) - wf) for e, wf in zip(exact, w)))
    out["D_weights"] = {"exact_sum_is_one": True, "max_abs_float_weight_error": float(wmax)}

    # (E) critical-target parameters
    nr = {r: n_crit(r) for r in range(14, 601)}
    out["E_targets"] = {"n_r_floor_checked_50_digits_for_r_in": [14, 600],
                        "n_14": nr[14], "n_15": nr[15], "n_16": nr[16], "n_100": nr[100], "n_300": nr[300], "n_600": nr[600],
                        "L_r_delta_0.5": {str(r): L_cut(r, 0.5) for r in (14, 30, 100, 300, 600)},
                        "L_r_delta_1.0": {str(r): L_cut(r, 1.0) for r in (14, 30, 100, 300, 600)}}
    out["elapsed_seconds"] = time.perf_counter() - t0
    out["overall_pass"] = all(out[k]["pass_1e-12"] for k in ("A_mixture_vs_direct", "B_bruteforce", "C_bruteforce_H_D"))
    path = os.path.join(HERE, "VERIFICATION.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k != "environment"}, indent=1))


def task_probe(rmax):
    t_all = time.perf_counter()
    rows = []
    window_rows = []
    log = open(os.path.join(HERE, "RUN_LOG.txt"), "w", encoding="utf-8")
    log.write(f"prefix_probe.py probe {rmax}\n{json.dumps(env_info())}\n")
    for r in range(14, rmax + 1):
        t0 = time.perf_counter()
        n = n_crit(r)
        m = r - 4
        G = G_direct(r, n)
        w, D, Hd, terms = mixture_terms(r, n)
        absD = np.abs(D)
        absH = np.abs(Hd)
        absterms = w * absD * absH
        Gmix = complex(terms.sum())
        row = {
            "r": r, "n_r": n, "m": m, "N_paths_log10": (math.lgamma(n + r) - math.lgamma(r) - math.lgamma(n + 1)) / math.log(10),
            "G_re": G.real, "G_im": G.imag, "abs_G": abs(G), "r_abs_G": r * abs(G),
            "abs_Gmix_minus_G": abs(Gmix - G),
            "tri_full": float(absterms.sum()),
            "r_tri_full": r * float(absterms.sum()),
            "abs_D_at_0": float(absD[0]),
            "max_absH_all_j": float(absH.max()), "argmax_absH_all_j": int(absH.argmax()),
            "argmax_absterm_all_j": int(absterms.argmax()),
        }
        for delta in DELTAS:
            L = L_cut(r, delta)
            jm = min(n, L)
            tag = f"d{delta:g}"
            S = float(absterms[: jm + 1].sum())
            signed = complex(terms[: jm + 1].sum())
            row[f"L_{tag}"] = L
            row[f"jmax_{tag}"] = jm
            row[f"S_{tag}"] = S
            row[f"r_S_{tag}"] = r * S
            row[f"max_absH_window_{tag}"] = float(absH[: jm + 1].max())
            row[f"min_absH_window_{tag}"] = float(absH[: jm + 1].min())
            row[f"trunc_bound_{tag}"] = trunc_bound(r, delta)
            row[f"abs_signed_trunc_{tag}"] = abs(signed)
            row[f"abs_signed_trunc_minus_G_{tag}"] = abs(signed - G)
            row[f"weight_in_window_{tag}"] = float(w[: jm + 1].sum())
            row[f"ratio_S_over_absG_{tag}"] = S / abs(G) if abs(G) > 0 else float("inf")
            row[f"ratio_full_over_S_{tag}"] = float(absterms.sum()) / S if S > 0 else float("inf")
        row["seconds"] = time.perf_counter() - t0
        rows.append(row)
        jm1 = min(n, L_cut(r, 1.0))
        jm05 = min(n, L_cut(r, 0.5))
        for j in range(jm1 + 1):
            window_rows.append({
                "r": r, "n_r": n, "j": j, "k": n - j, "in_window_d0.5": int(j <= jm05), "in_window_d1": 1,
                "w": float(w[j]), "abs_D": float(absD[j]), "arg_D": float(np.angle(D[j])),
                "abs_H": float(absH[j]), "arg_H": float(np.angle(Hd[j])),
                "arg_DH": float(np.angle(D[j] * Hd[j])),
                "abs_term": float(absterms[j]), "term_re": float(terms[j].real), "term_im": float(terms[j].imag),
            })
        msg = (f"r={r} n={n} |G|={abs(G):.6e} r|G|={r*abs(G):.4f} S(0.5)={row['S_d0.5']:.6e} rS(0.5)={row['r_S_d0.5']:.4f} "
               f"S(1)={row['S_d1']:.6e} rS(1)={row['r_S_d1']:.4f} full={row['tri_full']:.6e} "
               f"|Gmix-G|={row['abs_Gmix_minus_G']:.2e} t={row['seconds']:.2f}s")
        log.write(msg + "\n")
        log.flush()
        if r % 25 == 0 or r == 14:
            print(msg, flush=True)
    total = time.perf_counter() - t_all
    log.write(f"TOTAL_SECONDS {total:.2f}\n")
    log.close()
    keys = list(rows[0].keys())
    with open(os.path.join(HERE, "PROBE_RESULTS.csv"), "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=keys)
        wr.writeheader()
        for row in rows:
            wr.writerow(row)
    with open(os.path.join(HERE, "PROBE_RESULTS.json"), "w", encoding="utf-8") as f:
        json.dump({"classification": "[NUM] exploratory numbers; not a theorem", "environment": env_info(),
                   "rmax": rmax, "deltas": list(DELTAS), "total_seconds": total, "rows": rows}, f, indent=1)
    wkeys = list(window_rows[0].keys())
    with open(os.path.join(HERE, "WINDOW_TABLE.csv"), "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=wkeys)
        wr.writeheader()
        for row in window_rows:
            wr.writerow(row)
    print(f"TOTAL_SECONDS {total:.2f}")


def task_mpcheck():
    t0 = time.perf_counter()
    res = {"classification": "[NUM] rounding-error cross-check, mpmath 30 digits vs complex128", "dps": 30, "items": []}
    worst = 0.0

    def rec(kind, params, dbl, mpv, secs):
        nonlocal worst
        d = abs(dbl - mpc_to_complex(mpv))
        worst = max(worst, d)
        res["items"].append({"kind": kind, **params, "double_re": dbl.real, "double_im": dbl.imag,
                             "mp_re": mp.nstr(mpv.real, 25), "mp_im": mp.nstr(mpv.imag, 25),
                             "abs_discrepancy": d, "seconds": secs})

    for r in (14, 30, 60, 100, 200, 300, 450, 600):
        n = n_crit(r)
        t1 = time.perf_counter()
        gm = G_direct_mp(r, n)
        rec("G_direct", {"r": r, "n": n}, G_direct(r, n), gm, time.perf_counter() - t1)
    for r in (100, 300, 600):
        n = n_crit(r)
        m = r - 4
        H = H_all(m, n)
        for j in sorted({0, 3, 10, 20, min(n, L_cut(r, 0.5)), min(n, L_cut(r, 1.0))}):
            if j > n:
                continue
            t1 = time.perf_counter()
            hm = H_mp(m, n - j, j)
            rec("H_tail", {"r": r, "m": m, "k": n - j, "j": j}, complex(H[j, n - j]), hm, time.perf_counter() - t1)
    for j in (0, 5, 50, n_crit(600)):
        t1 = time.perf_counter()
        rec("D_prefix", {"j": j}, complex(D_all(j)[j]), D_mp(j), time.perf_counter() - t1)
    # full mixture and triangle sums at 30 digits for two r
    for r in (60, 100):
        n = n_crit(r)
        m = r - 4
        t1 = time.perf_counter()
        w, D, Hd, terms = mixture_terms(r, n)
        with mp.workdps(30):
            N = math.comb(n + r - 1, r - 1)
            gsum = mp.mpc(0)
            tri = mp.mpf(0)
            Svals = {}
            for j in range(n + 1):
                wj = mp.mpf(math.comb(j + 3, 3) * math.comb(n - j + m - 1, m - 1)) / N
                dj = D_mp(j)
                hj = H_mp(m, n - j, j)
                gsum += wj * dj * hj
                tri += wj * abs(dj) * abs(hj)
                for delta in DELTAS:
                    if j <= min(n, L_cut(r, delta)):
                        Svals[delta] = Svals.get(delta, mp.mpf(0)) + wj * abs(dj) * abs(hj)
            gm = G_direct_mp(r, n)
        secs = time.perf_counter() - t1
        rec("mixture_sum", {"r": r, "n": n}, complex(terms.sum()), gsum, secs)
        absterms = w * np.abs(D) * np.abs(Hd)
        d_tri = abs(float(absterms.sum()) - float(tri))
        worst = max(worst, d_tri)
        item = {"kind": "triangle_full", "r": r, "n": n, "double": float(absterms.sum()), "mp": mp.nstr(tri, 25),
                "abs_discrepancy": d_tri, "mp_mixture_minus_mp_direct": float(abs(gsum - gm))}
        for delta in DELTAS:
            jm = min(n, L_cut(r, delta))
            Sd = float(absterms[: jm + 1].sum())
            dd = abs(Sd - float(Svals[delta]))
            worst = max(worst, dd)
            item[f"S_double_d{delta:g}"] = Sd
            item[f"S_mp_d{delta:g}"] = mp.nstr(Svals[delta], 25)
            item[f"abs_discrepancy_S_d{delta:g}"] = dd
        res["items"].append(item)
    res["max_abs_discrepancy"] = float(worst)
    res["pass_1e-9"] = bool(worst <= 1e-9)
    res["elapsed_seconds"] = time.perf_counter() - t0
    res["environment"] = env_info()
    with open(os.path.join(HERE, "MPMATH_CROSSCHECK.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({"max_abs_discrepancy": worst, "pass_1e-9": res["pass_1e-9"], "items": len(res["items"]),
                      "elapsed_seconds": res["elapsed_seconds"]}, indent=1))


def task_sha():
    names = sorted(f for f in os.listdir(HERE) if f != "SHA256SUMS.txt" and os.path.isfile(os.path.join(HERE, f)))
    lines = [f"{sha256_file(os.path.join(HERE, f))}  {f}" for f in names]
    with open(os.path.join(HERE, "SHA256SUMS.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "verify":
        task_verify()
    elif cmd == "probe":
        task_probe(int(sys.argv[2]) if len(sys.argv) > 2 else 300)
    elif cmd == "mpcheck":
        task_mpcheck()
    elif cmd == "sha":
        task_sha()
    else:
        print(__doc__)
