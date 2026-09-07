#!/usr/bin/env python3
"""barrier_probe.py -- exploratory numerical test ([NUM] evidence only) of the
BARRIER / SURVIVAL hypothesis for the exponential sum G_(r,n).

Objects (identical to A2_numeric_probe/prefix_probe.py, re-implemented independently):
  z = (z_1..z_r) uniform on weak compositions of n into r parts, a_i = z_i + 1,
  S_j = sum_{i<=j} z_i, A_j = j + S_j,
  B_r(a) = sum_{s=1}^r 3^(r-s) 2^(A_(s-1)),  F_r = e_(16 3^r)(B_r),  G_(r,n) = E[F_r | sum z = n].
  n_r = floor(beta r) - 8, beta = log2(3) - 1, r >= 14, theta_r = frac(beta r).

EXACT IDENTITY (Task 1).  16 3^s = 2^(4 + alpha s), alpha = log2(3), so
  B_r / (16 3^r) = sum_{s=1}^r 2^(A_(s-1) - 4 - alpha s) = sum_{s=1}^r 2^(delta_s),
  delta_s = S_(s-1) - beta s - 5,
and therefore  F_r = prod_{s=1}^r exp(2 pi i 2^(delta_s))  EXACTLY (no congruence needed).

HYPOTHESIS.  |G_r| ~= P(max_s delta_s <= T) for an effective O(1) barrier level T.

Everything below is a deterministic transfer-matrix DP over the conditioned measure.
NO Monte Carlo anywhere.  The counting DP (the measure) uses exact Python ints /
Fractions; the phase DP uses complex128 and is cross-checked against a scalar mpmath
re-implementation at 30 digits.

Nothing here proves any bound or the Collatz conjecture.

Usage:  python barrier_probe.py            (writes every artifact next to this file)
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
from itertools import accumulate

import numpy as np
import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
PROBE_DIR = os.path.abspath(os.path.join(
    HERE, "..", "..", "lead_parallel_20260907", "A2_numeric_probe"))

mp.dps = 50
ALPHA_MP = mp.log(3) / mp.log(2)
BETA_MP = ALPHA_MP - 1
BETA = float(BETA_MP)
TWO_PI = 2.0 * math.pi

RMIN, RMAX = 14, 600
T_GRID = [-5.4, -5.2, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0,
          -1.5, -1.0, -0.5, -0.25, 0.0, 0.25, 0.5, 1.0, 1.5, 2.0]
T_REQUIRED = [-4.0, -3.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]

LOG = []


def log(msg):
    print(msg, flush=True)
    LOG.append(msg)


# --------------------------------------------------------------------------- parameters
def n_crit(r):
    with mp.workdps(50):
        v = BETA_MP * r
        fl = mp.floor(v)
        if abs(v - fl) < mp.mpf('1e-30'):
            raise ArithmeticError("floor(beta r) ambiguous")
        return int(fl) - 8


def theta(r):
    with mp.workdps(50):
        return float(BETA_MP * r - mp.floor(BETA_MP * r))


def caps_for(r, T):
    """delta_s <= T  <=>  S_(s-1) <= floor(beta s + 5 + T) =: c_s   (S integer).
    Returns [c_1,...,c_r]; floors are taken at 50 digits with an ambiguity guard."""
    out = []
    with mp.workdps(50):
        Tm = mp.mpf(repr(T))
        for s in range(1, r + 1):
            v = BETA_MP * s + 5 + Tm
            fl = mp.floor(v)
            d = v - fl
            if d < mp.mpf('1e-25') or d > 1 - mp.mpf('1e-25'):
                raise ArithmeticError(f"ambiguous floor at r={r} s={s} T={T}")
            out.append(int(fl))
    return out


# --------------------------------------------------------------------------- phase tables
NMAX = 0
_TAB = {}


def tab(s, count):
    """phi_s(t) = exp(2 pi i (2^t mod 16 3^s)/(16 3^s)) for t = s-1 .. s-1+NMAX-1.
    Exact integer residues -> one correctly rounded double each -> one complex128 phase."""
    e = _TAB.get(s)
    if e is None:
        M = 16 * 3 ** s
        x = pow(2, s - 1, M)
        fr = []
        for _ in range(NMAX):
            fr.append(x / M)
            x = (x << 1) % M
        e = np.exp(1j * TWO_PI * np.asarray(fr, dtype=np.float64))
        _TAB[s] = e
    return e[:count]


# --------------------------------------------------------------------------- DPs
def phase_dp(r, n, caps=None):
    """Unnormalised-then-normalised  E[ prod_s exp(2 pi i 2^(delta_s)) * 1{delta_s <= T for all s} ].
    caps=None  ->  the unconstrained G_(r,n).
    State V[S] after s-1 steps carries S = S_(s-1); the level condition is S <= c_s."""
    V = np.zeros(n + 1, dtype=np.complex128)
    V[0] = 1.0
    for s in range(1, r + 1):
        c = n if caps is None else min(caps[s - 1], n)
        if c < 0:
            return 0j
        if c < n:
            V[c + 1:] = 0.0
        V[:c + 1] *= tab(s, c + 1)
        np.cumsum(V[:c + 1], out=V[:c + 1])
        if c < n:
            V[c + 1:] = V[c]
    return complex(V[n]) / math.comb(n + r - 1, r - 1)


def surv_count(r, n, caps):
    """EXACT integer count of weak compositions of n into r parts with S_(s-1) <= c_s for all s."""
    f = [0] * (n + 1)
    f[0] = 1
    for s in range(1, r + 1):
        c = caps[s - 1]
        if c < 0:
            return 0
        if c >= n:
            f = list(accumulate(f))
        else:
            g = list(accumulate(f[:c + 1]))
            f = g + [g[-1]] * (n - c)
    return f[n]


def phase_dp_mp(r, n, caps=None, dps=30):
    """Scalar mpmath re-implementation of phase_dp (independent arithmetic path)."""
    with mp.workdps(dps):
        V = [mp.mpc(0)] * (n + 1)
        V[0] = mp.mpc(1)
        for s in range(1, r + 1):
            c = n if caps is None else min(caps[s - 1], n)
            if c < 0:
                return mp.mpc(0)
            M = 16 * 3 ** s
            x = pow(2, s - 1, M)
            for S in range(c + 1):
                V[S] = V[S] * mp.expjpi(2 * mp.mpf(x) / M)
                x = (x << 1) % M
            acc = mp.mpc(0)
            for S in range(c + 1):
                acc = acc + V[S]
                V[S] = acc
            for S in range(c + 1, n + 1):
                V[S] = acc
        return V[n] / mp.mpf(math.comb(n + r - 1, r - 1))


# --------------------------------------------------------------------------- brute force
def compositions(n, parts):
    if parts == 1:
        yield (n,)
        return
    for k in range(n + 1):
        for rest in compositions(n - k, parts - 1):
            yield (k,) + rest


# --------------------------------------------------------------------------- Task 1
def task1_verify():
    res = {}
    with mp.workdps(60):
        res["alpha_50dps"] = mpmath.nstr(ALPHA_MP, 50)
        res["beta_50dps"] = mpmath.nstr(BETA_MP, 50)
        res["beta_float"] = repr(BETA)
        res["beta_float_matches_given"] = (repr(BETA) == repr(0.5849625007211562))

    # (a) the delta identity, 50-digit, on explicit compositions (deterministic sweep)
    worst = mp.mpf(0)
    worst_case = None
    cases = 0
    with mp.workdps(60):
        for r in range(3, 9):
            for n in range(0, 7):
                for z in compositions(n, r):
                    cases += 1
                    A = 0
                    B = 0
                    for s in range(1, r + 1):
                        B += 3 ** (r - s) * 2 ** A
                        A += z[s - 1] + 1
                    X1 = mp.mpf(B) / (16 * mp.mpf(3) ** r)   # exact rational -> 60 dps
                    S = 0
                    X2 = mp.mpf(0)
                    for s in range(1, r + 1):
                        X2 += mp.mpf(2) ** (mp.mpf(S) - BETA_MP * s - 5)
                        S += z[s - 1]
                    d = abs(X1 - X2) / X1
                    if d > worst:
                        worst, worst_case = d, (r, n, z)
    res["identity_cases"] = cases
    res["identity_max_rel_dev"] = mpmath.nstr(worst, 8)
    res["identity_worst_case"] = str(worst_case)

    # (b) brute-force product form vs the DP, small r
    bf = []
    for (r, n) in [(5, 3), (6, 4), (7, 3), (8, 2)]:
        acc = 0j
        cnt = 0
        for z in compositions(n, r):
            A = 0
            B = 0
            for s in range(1, r + 1):
                B += 3 ** (r - s) * 2 ** A
                A += z[s - 1] + 1
            M = 16 * 3 ** r
            acc += complex(np.exp(1j * TWO_PI * ((B % M) / M)))
            cnt += 1
        g = acc / cnt
        gd = phase_dp(r, n)
        bf.append({"r": r, "n": n, "abs_brute": abs(g), "abs_dp": abs(gd),
                   "dev": abs(g - gd)})
    res["bruteforce_vs_dp"] = bf
    res["bruteforce_max_dev"] = max(x["dev"] for x in bf)
    return res


def task1_reproduce(absG):
    """Product-form DP vs PROBE_RESULTS.csv abs_G."""
    sample = [14, 15, 20, 31, 47, 64, 89, 121, 150, 199, 251, 300, 377, 421, 500, 555, 599, 600]
    devs = []
    for r in sample:
        n = n_crit(r)
        g = abs(phase_dp(r, n))
        devs.append({"r": r, "abs_G_dp": g, "abs_G_csv": absG[r],
                     "dev": abs(g - absG[r])})
    return devs, max(d["dev"] for d in devs)


def task1_mpcheck():
    out = []
    for r in [14, 30, 60, 100]:
        n = n_crit(r)
        for T in [None, -4.0, 0.0]:
            caps = None if T is None else caps_for(r, T)
            a = phase_dp(r, n, caps)
            b = phase_dp_mp(r, n, caps, dps=30)
            out.append({"r": r, "n": n, "T": T,
                        "abs_c128": abs(a),
                        "abs_mp30": float(abs(b)),
                        "dev": float(abs(mp.mpc(a) - b))})
    return out, max(x["dev"] for x in out)


# --------------------------------------------------------------------------- Task 5 moments
def moments(r, n):
    """Exact first two moments of z_1 and the exchangeable covariance, under the
    uniform measure on weak compositions of n into r parts."""
    if n == 0:
        return 0.0, 0.0, 0.0
    tot = math.comb(n + r - 1, r - 1)
    e1 = Fraction(0)
    e2 = Fraction(0)
    for k in range(n + 1):
        w = Fraction(math.comb(n - k + r - 2, r - 2), tot)
        e1 += w * k
        e2 += w * k * k
    v = e2 - e1 * e1
    # exchangeable + fixed sum  =>  Cov = -v/(r-1),  Var(S_k) = v k (r-k)/(r-1)
    sigma2_eff = float(v) * r / (r - 1)     # Var(S_k) = sigma2_eff k(r-k)/r
    return float(e1), float(v), sigma2_eff


# --------------------------------------------------------------------------- main sweep
def main():
    global NMAX
    t_start = time.time()
    rs = list(range(RMIN, RMAX + 1))
    ns = {r: n_crit(r) for r in rs}
    NMAX = max(ns.values()) + 2

    # ---- read existing probe data (do not recompute)
    absG = {}
    with open(os.path.join(PROBE_DIR, "PROBE_RESULTS.csv"), newline="") as fh:
        for row in csv.DictReader(fh):
            absG[int(row["r"])] = float(row["abs_G"])
    log(f"[read] PROBE_RESULTS.csv: {len(absG)} rows, r in "
        f"{min(absG)}..{max(absG)}")

    # ================= TASK 1
    log("== TASK 1: identity + reproduction ==")
    v1 = task1_verify()
    log(f"   alpha = {v1['alpha_50dps']}")
    log(f"   beta  = {v1['beta_50dps']}   float matches given: {v1['beta_float_matches_given']}")
    log(f"   delta-identity: {v1['identity_cases']} exhaustive cases, "
        f"max relative deviation at 60 dps = {v1['identity_max_rel_dev']}")
    log(f"   brute force vs DP: max |dev| = {v1['bruteforce_max_dev']:.3e}")
    rep, maxrep = task1_reproduce(absG)
    log(f"   product-form DP vs PROBE_RESULTS abs_G on {len(rep)} values of r: "
        f"max |dev| = {maxrep:.3e}")
    mpc, maxmpc = task1_mpcheck()
    log(f"   complex128 vs mpmath(30 dps): max |dev| = {maxmpc:.3e}")
    json.dump({"verify": v1, "reproduce": rep, "reproduce_max_dev": maxrep,
               "mpcheck": mpc, "mpcheck_max_dev": maxmpc,
               "python": sys.version, "platform": platform.platform(),
               "numpy": np.__version__, "mpmath": mpmath.__version__},
              open(os.path.join(HERE, "VERIFICATION.json"), "w"), indent=1)

    # ================= TASK 2 + 6 sweep
    log("== TASK 2/6: exact survival DP + constrained phase DP ==")
    caps_cache = {}
    qrows = []
    drows = []
    Gabs = {}
    for r in rs:
        n = ns[r]
        tot = math.comb(n + r - 1, r - 1)
        G = phase_dp(r, n)
        Gabs[r] = abs(G)
        th = theta(r)
        m1, var1, s2 = moments(r, n)
        row = {"r": r, "n_r": n, "theta_r": th, "abs_G": abs(G), "r_abs_G": r * abs(G),
               "abs_G_csv": absG[r], "Ez": m1, "var_z": var1, "sigma2_eff": s2}
        for T in T_GRID:
            caps = caps_for(r, T)
            c = surv_count(r, n, caps)
            Q = float(Fraction(c, tot))
            row[f"Q_{T}"] = Q
            row[f"rQ_{T}"] = r * Q
            if T in T_REQUIRED:
                Gin = phase_dp(r, n, caps)
                Gout = G - Gin
                drows.append({"r": r, "n_r": n, "T": T, "abs_G": abs(G),
                              "Q": Q, "abs_in": abs(Gin), "abs_out": abs(Gout),
                              "r_abs_G": r * abs(G), "r_abs_in": r * abs(Gin),
                              "r_abs_out": r * abs(Gout),
                              "in_over_G": abs(Gin) / abs(G),
                              "out_over_G": abs(Gout) / abs(G)})
        qrows.append(row)
        if r % 100 == 0:
            log(f"   ... r={r} done ({time.time()-t_start:.1f}s)")

    qfields = ["r", "n_r", "theta_r", "abs_G", "r_abs_G", "abs_G_csv",
               "Ez", "var_z", "sigma2_eff"] + \
              [f"{p}_{T}" for T in T_GRID for p in ("Q", "rQ")]
    with open(os.path.join(HERE, "Q_RESULTS.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=qfields)
        w.writeheader()
        for row in qrows:
            w.writerow({k: row[k] for k in qfields})
    with open(os.path.join(HERE, "DECOMPOSITION.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(drows[0].keys()))
        w.writeheader()
        w.writerows(drows)
    log(f"   wrote Q_RESULTS.csv ({len(qrows)} rows) and DECOMPOSITION.csv ({len(drows)} rows)")
    log(f"   max |abs_G(dp) - abs_G(csv)| over all r = "
        f"{max(abs(row['abs_G']-row['abs_G_csv']) for row in qrows):.3e}")

    # ================= TASK 3 : per-T comparison
    def pearson(x, y):
        n_ = len(x)
        mx = sum(x) / n_
        my = sum(y) / n_
        sx = math.sqrt(sum((a - mx) ** 2 for a in x))
        sy = math.sqrt(sum((b - my) ** 2 for b in y))
        if sx == 0 or sy == 0:
            return float('nan')
        return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)

    def slope(x, y):
        n_ = len(x)
        mx = sum(x) / n_
        my = sum(y) / n_
        den = sum((a - mx) ** 2 for a in x)
        return sum((a - mx) * (b - my) for a, b in zip(x, y)) / den

    sel = [row for row in qrows if row["r"] >= 50]
    hi = [row for row in qrows if row["r"] >= 300]
    lo = [row for row in qrows if 50 <= row["r"] < 150]
    fit = []
    for T in T_GRID:
        rQ = [row[f"rQ_{T}"] for row in sel]
        rG = [row["r_abs_G"] for row in sel]
        ratio = [g / q if q > 0 else float('nan') for g, q in zip(rG, rQ)]
        ok = [x for x in ratio if x == x]
        mean = sum(ok) / len(ok)
        sd = math.sqrt(sum((x - mean) ** 2 for x in ok) / len(ok))
        rl = sum(row["r_abs_G"] / row[f"rQ_{T}"] for row in lo) / len(lo)
        rh = sum(row["r_abs_G"] / row[f"rQ_{T}"] for row in hi) / len(hi)
        lr = [math.log(row["r"]) for row in sel]
        lrat = [math.log(x) for x in ratio]
        fit.append({"T": T,
                    "corr_rQ_rabsG": pearson(rQ, rG),
                    "mean_rQ": sum(rQ) / len(rQ),
                    "mean_ratio_absG_over_Q": mean,
                    "cv_ratio": sd / mean,
                    "ratio_r50_149": rl, "ratio_r300_600": rh,
                    "drift_hi_over_lo": rh / rl,
                    "dlogratio_dlogr": slope(lr, lrat),
                    "corr_theta_rQ": pearson([row["theta_r"] for row in sel], rQ)})

    corr_theta_G = pearson([row["theta_r"] for row in sel], [row["r_abs_G"] for row in sel])
    log("== TASK 3/4: per-T comparison (r >= 50) ==")
    log(f"   measured corr(theta_r, r|G_r|) = {corr_theta_G:.4f}   "
        f"mean r|G_r| = {sum(row['r_abs_G'] for row in sel)/len(sel):.4f}")
    log("   T      mean r*Q   corr(rQ,r|G|)  mean |G|/Q   cv    ratio(50-149) ratio(300-600) drift  corr(theta,rQ)")
    for f in fit:
        log(f"  {f['T']:>5}  {f['mean_rQ']:9.3f}  {f['corr_rQ_rabsG']:12.4f}  "
            f"{f['mean_ratio_absG_over_Q']:10.4f} {f['cv_ratio']:6.3f} "
            f"{f['ratio_r50_149']:11.4f} {f['ratio_r300_600']:13.4f} "
            f"{f['drift_hi_over_lo']:6.3f} {f['corr_theta_rQ']:8.4f}")
    with open(os.path.join(HERE, "FIT_BY_T.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(fit[0].keys()))
        w.writeheader()
        w.writerows(fit)

    # ---- best-fit T per r by bisection on the (monotone) step function Q_r(.)
    log("== TASK 3b: per-r effective barrier level T*(r) with Q_r(T*) = |G_r| ==")
    tstar = []
    for r in rs:
        if r < 30:
            continue
        n = ns[r]
        tot = math.comb(n + r - 1, r - 1)
        target = Gabs[r]
        lo_t, hi_t = -5.5849, 3.0
        for _ in range(28):
            mid = 0.5 * (lo_t + hi_t)
            try:
                q = surv_count(r, n, caps_for(r, mid)) / tot
            except ArithmeticError:
                mid += 1e-9
                q = surv_count(r, n, caps_for(r, mid)) / tot
            if q < target:
                lo_t = mid
            else:
                hi_t = mid
        tstar.append({"r": r, "T_star": 0.5 * (lo_t + hi_t), "abs_G": target})
    with open(os.path.join(HERE, "TSTAR.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["r", "T_star", "abs_G"])
        w.writeheader()
        w.writerows(tstar)
    for lo_r, hi_r in [(30, 99), (100, 199), (200, 299), (300, 399), (400, 499), (500, 600)]:
        blk = [x["T_star"] for x in tstar if lo_r <= x["r"] <= hi_r]
        log(f"   r in [{lo_r},{hi_r}]: mean T* = {sum(blk)/len(blk):.4f}  "
            f"min {min(blk):.4f} max {max(blk):.4f}")

    # ================= TASK 5 : classical bridge constant
    log("== TASK 5: classical 2ab/(sigma^2 m) against the measured constant ==")
    brows = []
    for row in qrows:
        r = row["r"]
        n = row["n_r"]
        if n == 0:
            continue
        a = 5.0 + BETA                      # -delta_1, deterministic
        b = 13.0 + row["theta_r"] + row["Ez"]   # -E[delta_r]
        s2 = row["sigma2_eff"]
        m = r - 1
        pred = 2 * a * b / (s2 * m)
        brows.append({"r": r, "a": a, "b": b, "sigma2_eff": s2,
                      "pred_P": pred, "r_pred_P": r * pred,
                      "pred_P_exact": 1 - math.exp(-2 * a * b / (s2 * m)),
                      "r_pred_exact": r * (1 - math.exp(-2 * a * b / (s2 * m))),
                      "rQ_0": row["rQ_0.0"], "r_abs_G": row["r_abs_G"]})
    with open(os.path.join(HERE, "BRIDGE_PREDICTION.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(brows[0].keys()))
        w.writeheader()
        w.writerows(brows)
    tail = [x for x in brows if x["r"] >= 400]
    log(f"   r>=400:  a={tail[0]['a']:.4f}  mean b={sum(x['b'] for x in tail)/len(tail):.4f}  "
        f"mean sigma^2_eff={sum(x['sigma2_eff'] for x in tail)/len(tail):.4f}")
    log(f"   r>=400:  mean r*2ab/(sigma^2 m) = {sum(x['r_pred_P'] for x in tail)/len(tail):.3f}"
        f"   mean r*(1-exp(-2ab/(sigma^2 m))) = {sum(x['r_pred_exact'] for x in tail)/len(tail):.3f}")
    log(f"   r>=400:  mean r*Q_r(0)          = {sum(x['rQ_0'] for x in tail)/len(tail):.3f}")
    log(f"   r>=400:  mean r*|G_r|           = {sum(x['r_abs_G'] for x in tail)/len(tail):.3f}")
    log(f"   gap factor (r*Q(0) / r|G|)      = "
        f"{(sum(x['rQ_0'] for x in tail)/len(tail))/(sum(x['r_abs_G'] for x in tail)/len(tail)):.3f}")

    # ================= TASK 6 summary
    log("== TASK 6: decomposition E[prod 1{max<=T}] vs E[prod 1{max>T}] ==")
    log("    T    r      r|G|     r|E_in|   r|E_out|   |E_in|/|G|   |E_out|/|G|")
    for T in T_REQUIRED:
        for r in (100, 200, 300, 400, 500, 600):
            d = next(x for x in drows if x["r"] == r and x["T"] == T)
            log(f"  {T:>5} {r:>4} {d['r_abs_G']:9.4f} {d['r_abs_in']:9.4f} "
                f"{d['r_abs_out']:10.6f} {d['in_over_G']:11.6f} {d['out_over_G']:12.3e}")

    # out-term scaling summary
    log("   sup over r>=50 of r*|E_out| per T:")
    for T in T_REQUIRED:
        sub = [x for x in drows if x["T"] == T and x["r"] >= 50]
        log(f"     T={T:>5}  max r|E_out| = {max(x['r_abs_out'] for x in sub):.6e}   "
            f"at r=600: {next(x for x in sub if x['r']==600)['r_abs_out']:.6e}")

    log(f"total seconds: {time.time()-t_start:.1f}")
    open(os.path.join(HERE, "RUN_LOG.txt"), "w").write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
