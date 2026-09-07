#!/usr/bin/env python3
"""theta_profile.py -- exact-DP extension of the prefix probe to large r, for the
question "does r*|G_r| have a limiting profile Phi(theta_r), and is inf Phi > 0?".

[NUM] evidence only.  Nothing here proves any bound or the Collatz conjecture.

Objects (identical to A2_numeric_probe/prefix_probe.py, re-derived independently here):

  alpha = log2(3), beta = alpha - 1, theta_r = frac(beta r), n_r = floor(beta r) - 8
  z uniform on weak compositions of n into r parts, a_i = z_i + 1, A_j = j + S_j,
  B_r(a) = sum_{s=1}^r 3^(r-s) 2^(A_(s-1)),  G_(r,n) = E[e_(16 3^r)(B_r) | sum z = n]
  H_(m,k)(j) = E[ e_(3^(m+4))( 2^j B_m(y+1) ) | Y_m = k ];   we need j = 0, m = r-4, k = n_r.

Row factorisation (exact rational identity, no congruence):
  3^(m-s) 2^t / (c 3^m) = (2^t mod c 3^s) / (c 3^s),   c = 16 for G, c = 81 for H,
so both objects are the SAME transfer-matrix DP over (position s, cumulative excess S)
whose transition is a prefix sum, with different phase caches.

The only change relative to prefix_probe.py is a per-step scalar rescaling of the DP
vector with a running log accumulator, which removes the C(n+r-1,r-1) < 1e308 ceiling
(that ceiling caps prefix_probe.py at r ~ 620).  Residues stay exact Python integers;
each residue becomes one correctly-rounded double, accumulation is complex128.
An mpmath 30-digit scalar re-implementation (no rescaling at all -- mpf has unbounded
exponent, so it independently validates the rescaling) bounds the rounding error.

Usage:
  python theta_profile.py selftest            -> SELFTEST.json   (vs PROBE_RESULTS.csv)
  python theta_profile.py run RMAX            -> PROFILE_DATA.csv, RUN_LOG.txt
  python theta_profile.py mpcheck             -> MPMATH_CROSSCHECK.json
"""
import csv
import json
import math
import os
import platform
import sys
import time

import numpy as np
import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
A2 = os.path.join(os.path.dirname(HERE), "..", "lead_parallel_20260907", "A2_numeric_probe")
LOG10 = math.log(10.0)
TWO_PI = 2.0 * math.pi

# ------------------------------------------------------------------ constants (verified once)
with mp.workdps(60):
    ALPHA_MP = mp.log(3) / mp.log(2)
    BETA_MP = ALPHA_MP - 1
ALPHA = float(ALPHA_MP)
BETA = float(BETA_MP)


def n_crit(r):
    """n_r = floor(beta r) - 8, floor cross-checked at 60 digits against the double."""
    with mp.workdps(60):
        nb = int(mp.floor(BETA_MP * r))
    nf = math.floor(BETA * r)
    if nb != nf:
        raise ArithmeticError(f"floor(beta r) ambiguous at r={r}: {nb} vs {nf}")
    return nb - 8


def theta_of(r):
    """theta_r = frac(beta r), at 60 digits then rounded to double."""
    with mp.workdps(60):
        return float(BETA_MP * r - mp.floor(BETA_MP * r))


# ------------------------------------------------------------------ exact residue phase cache
class PhaseCache:
    """phi_s(t) = exp(2 pi i (2^t mod c 3^s) / (c 3^s)) for t = s-1, s, s+1, ...

    Residues by exact integer doubling with a conditional subtract (no big-int division
    in the loop).  Each residue -> one correctly-rounded double via int/int true division.
    Tables are r-independent, so they are shared across all r."""

    def __init__(self, c):
        self.c = c
        self.store = {}  # s -> [M, x, list_of_float_fractions, np_array_or_None]

    def get(self, s, count):
        ent = self.store.get(s)
        if ent is None:
            M = self.c * 3 ** s
            ent = [M, pow(2, s - 1, M), [], None]
            self.store[s] = ent
        M, x, fr, arr = ent
        if len(fr) < count:
            new = []
            for _ in range(count - len(fr)):
                new.append(x / M)         # exact-rounded double of the exact ratio
                x <<= 1
                if x >= M:
                    x -= M
            fr.extend(new)
            ent[1] = x
            tail = np.exp(1j * TWO_PI * np.asarray(new, dtype=np.float64))
            ent[3] = tail if arr is None else np.concatenate([arr, tail])
        return ent[3][:count]

    def residue_mp(self, s, t, dps):
        """High-precision phi_s(t) from the exact integer residue."""
        M = self.c * 3 ** s
        x = pow(2, t, M)
        with mp.workdps(dps):
            return mp.expjpi(2 * mp.mpf(x) / mp.mpf(M))


PHASE16 = PhaseCache(16)
PHASE81 = PhaseCache(81)

# small tiny-entry flush threshold: entries this far below the row max cannot affect the
# answer at double precision but do force denormal arithmetic.
FLUSH = 1e-280


def dp_value(cache, m, n):
    """Return (complex unit direction, log|.|) of

        V[n] = sum over weak compositions y of n into m parts of
               prod_{s=1}^m phi_s( (s-1) + Y_(s-1) ),      Y_0 = 0.

    V[n] = C(n+m-1,m-1) * G_(m,n)          for cache = PHASE16
    V[n] = C(n+m-1,m-1) * H_(m,n)(0)       for cache = PHASE81
    """
    V = np.zeros(n + 1, dtype=np.complex128)
    V[0] = 1.0
    logscale = 0.0
    for s in range(1, m + 1):
        V *= cache.get(s, n + 1)
        np.cumsum(V, out=V)
        mx = float(np.max(np.abs(V)))
        if mx == 0.0:
            return 0.0 + 0.0j, -math.inf
        V /= mx
        logscale += math.log(mx)
        np.putmask(V, np.abs(V) < FLUSH, 0.0)
    a = abs(V[n])
    if a == 0.0:
        return 0.0 + 0.0j, -math.inf
    return complex(V[n]) / a, math.log(a) + logscale


def log_comb(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def G_r(r, n):
    """(|G_(r,n)|, arg) via the rescaled DP."""
    u, lg = dp_value(PHASE16, r, n)
    return math.exp(lg - log_comb(n + r - 1, r - 1)), u


def H0_r(r, n):
    """(|H_(r-4,n)(0)|, arg)."""
    m = r - 4
    u, lg = dp_value(PHASE81, m, n)
    return math.exp(lg - log_comb(n + m - 1, m - 1)), u


# ------------------------------------------------------------------ mpmath reference (no rescaling)
def dp_value_mp(cache, m, n, dps=30):
    """Scalar mpmath DP, arbitrary exponent range -> no rescaling at all.
    Returns mpc V[n] (unnormalised)."""
    with mp.workdps(dps + 10):
        V = [mp.mpc(0)] * (n + 1)
        V[0] = mp.mpc(1)
        for s in range(1, m + 1):
            M = cache.c * 3 ** s
            x = pow(2, s - 1, M)
            acc = mp.mpc(0)
            for S in range(n + 1):
                if V[S] != 0:
                    acc += V[S] * mp.expjpi(2 * mp.mpf(x) / mp.mpf(M))
                V[S] = acc
                x <<= 1
                if x >= M:
                    x -= M
        return V[n]


def G_r_mp(r, n, dps=30):
    with mp.workdps(dps + 10):
        V = dp_value_mp(PHASE16, r, n, dps)
        C = mp.binomial(n + r - 1, r - 1)
        return mp.fabs(V / C)


def H0_r_mp(r, n, dps=30):
    m = r - 4
    with mp.workdps(dps + 10):
        V = dp_value_mp(PHASE81, m, n, dps)
        C = mp.binomial(n + m - 1, m - 1)
        return mp.fabs(V / C)


# ------------------------------------------------------------------ brute force (independent path)
def compositions(n, parts):
    if parts == 1:
        yield (n,)
        return
    for k in range(n + 1):
        for rest in compositions(n - k, parts - 1):
            yield (k,) + rest


def G_brute(r, n):
    """Direct definition: G = E[e_(16 3^r)(B_r)] over weak compositions."""
    M = 16 * 3 ** r
    tot = mp.mpc(0)
    cnt = 0
    with mp.workdps(40):
        for z in compositions(n, r):
            a = [x + 1 for x in z]
            A = 0
            B = 0
            for s in range(1, r + 1):
                B += 3 ** (r - s) * 2 ** A
                A += a[s - 1]
            tot += mp.expjpi(2 * mp.mpf(B % M) / mp.mpf(M))
            cnt += 1
        return mp.fabs(tot / cnt)


def H0_brute(m, k):
    """Direct definition of H_(m,k)(0)."""
    M = 3 ** (m + 4)
    tot = mp.mpc(0)
    cnt = 0
    with mp.workdps(40):
        for y in compositions(k, m):
            a = [x + 1 for x in y]
            A = 0
            B = 0
            for s in range(1, m + 1):
                B += 3 ** (m - s) * 2 ** A
                A += a[s - 1]
            tot += mp.expjpi(2 * mp.mpf(B % M) / mp.mpf(M))
            cnt += 1
        return mp.fabs(tot / cnt)


# ------------------------------------------------------------------ commands
def cmd_selftest():
    out = {"python": sys.version, "platform": platform.platform(),
           "numpy": np.__version__, "mpmath": mpmath.__version__,
           "alpha": ALPHA, "beta": BETA}
    # (a) constants
    out["beta_check"] = abs(BETA - (math.log(3) / math.log(2) - 1.0))
    # (b) brute force vs DP on small cases
    bf = []
    worst = 0.0
    for r in range(5, 9):
        for n in range(0, 5):
            g, _ = G_r(r, n)
            gb = float(G_brute(r, n))
            worst = max(worst, abs(g - gb))
            bf.append({"r": r, "n": n, "dp": g, "brute": gb, "err": abs(g - gb)})
    for m in range(3, 7):
        for k in range(0, 5):
            h, _ = H0_r(m + 4, k)
            hb = float(H0_brute(m, k))
            worst = max(worst, abs(h - hb))
            bf.append({"m": m, "k": k, "dp_H0": h, "brute_H0": hb, "err": abs(h - hb)})
    out["bruteforce_cases"] = len(bf)
    out["bruteforce_max_err"] = worst
    # (c) reproduce PROBE_RESULTS.csv abs_G for r = 14..600
    path = os.path.join(A2, "PROBE_RESULTS.csv")
    diffs = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            r = int(row["r"])
            n = int(row["n_r"])
            assert n == n_crit(r), (r, n, n_crit(r))
            g, _ = G_r(r, n)
            ref = float(row["abs_G"])
            diffs.append((r, abs(g - ref), abs(g - ref) / max(ref, 1e-300)))
    out["probe_rows_compared"] = len(diffs)
    out["probe_max_abs_diff"] = max(d[1] for d in diffs)
    out["probe_max_rel_diff"] = max(d[2] for d in diffs)
    out["probe_argmax_r"] = max(diffs, key=lambda d: d[2])[0]
    with open(os.path.join(HERE, "SELFTEST.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k != "bruteforce_cases"}, indent=2))


def cmd_run(rmax):
    rows = []
    log = open(os.path.join(HERE, "RUN_LOG.txt"), "w", encoding="utf-8")
    log.write(f"platform {platform.platform()} python {sys.version.split()[0]} "
              f"numpy {np.__version__} mpmath {mpmath.__version__}\n")
    log.write(f"alpha {ALPHA!r} beta {BETA!r} rmax {rmax}\n")
    t0 = time.perf_counter()
    for r in range(14, rmax + 1):
        n = n_crit(r)
        if n < 0:
            continue
        th = theta_of(r)
        t1 = time.perf_counter()
        g, gu = G_r(r, n)
        t2 = time.perf_counter()
        h, hu = H0_r(r, n)
        t3 = time.perf_counter()
        rows.append({
            "r": r, "n_r": n, "theta_r": repr(th),
            "abs_G": repr(g), "r_abs_G": repr(r * g),
            "arg_G": repr(math.atan2(gu.imag, gu.real)),
            "abs_H0": repr(h), "r_abs_H0": repr(r * h),
            "arg_H0": repr(math.atan2(hu.imag, hu.real)),
            "sec_G": round(t2 - t1, 4), "sec_H0": round(t3 - t2, 4),
        })
        log.write(f"r={r} n={n} theta={th:.9f} absG={g:.12e} r|G|={r*g:.9f} "
                  f"absH0={h:.12e} r|H0|={r*h:.9f} secG={t2-t1:.3f} secH={t3-t2:.3f}\n")
        if r % 50 == 0:
            log.flush()
            print(f"r={r} theta={th:.4f} r|G|={r*g:.4f} r|H0|={r*h:.4f} "
                  f"[{time.perf_counter()-t0:.0f}s]", flush=True)
    total = time.perf_counter() - t0
    log.write(f"TOTAL_SECONDS {total:.2f}\n")
    log.close()
    with open(os.path.join(HERE, "PROFILE_DATA.csv"), "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        for row in rows:
            wr.writerow(row)
    print(f"wrote {len(rows)} rows in {total:.1f}s")


def cmd_mpcheck(sample=None):
    sample = sample or [14, 20, 30, 50, 80, 120, 200, 300, 400, 600, 900, 1200, 1500]
    out = []
    for r in sample:
        n = n_crit(r)
        t0 = time.perf_counter()
        g, _ = G_r(r, n)
        h, _ = H0_r(r, n)
        t1 = time.perf_counter()
        gm = float(G_r_mp(r, n, 30))
        hm = float(H0_r_mp(r, n, 30))
        t2 = time.perf_counter()
        rec = {"r": r, "n_r": n,
               "abs_G_f64": g, "abs_G_mp30": gm,
               "abs_err_G": abs(g - gm), "rel_err_G": abs(g - gm) / gm,
               "abs_H0_f64": h, "abs_H0_mp30": hm,
               "abs_err_H0": abs(h - hm), "rel_err_H0": abs(h - hm) / hm,
               "sec_f64": round(t1 - t0, 3), "sec_mp": round(t2 - t1, 1)}
        out.append(rec)
        print(f"r={r} relG={rec['rel_err_G']:.2e} relH0={rec['rel_err_H0']:.2e} "
              f"mp {rec['sec_mp']}s", flush=True)
        with open(os.path.join(HERE, "MPMATH_CROSSCHECK.json"), "w", encoding="utf-8") as f:
            json.dump({"dps": 30, "records": out,
                       "max_rel_err_G": max(x["rel_err_G"] for x in out),
                       "max_rel_err_H0": max(x["rel_err_H0"] for x in out),
                       "max_abs_err_G": max(x["abs_err_G"] for x in out),
                       "max_abs_err_H0": max(x["abs_err_H0"] for x in out)}, f, indent=2)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "selftest":
        cmd_selftest()
    elif cmd == "run":
        cmd_run(int(sys.argv[2]))
    elif cmd == "mpcheck":
        arg = sys.argv[2:] and [int(x) for x in sys.argv[2:]] or None
        cmd_mpcheck(arg)
    else:
        raise SystemExit("unknown command")
