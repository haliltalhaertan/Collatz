"""ATTACK engine -- implemented from scratch from the task spec. Exact arithmetic only.

Shortcut map H, prefix histogram P_{m,k,r}, energies J/Ecal, transfer E_k/O_k,
row quantities I/F/Out/L/M/defect, per-stratum L_k/M_j, charging windows.
NO floating point in any claimed number (int / Fraction only).
Numpy is used ONLY for exact integer bulk iteration (int64), never floats.
"""
from fractions import Fraction
from math import comb


def H(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2


def prefix_hist_small(m, r):
    """Direct definitional histogram for small m (pure Python)."""
    R = 1 << r
    res = {k: [0] * R for k in range(1, m + 1)}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                x = (3 * x + 1) >> 1
                k += 1
            else:
                x >>= 1
        res[k][x % R] += 1
    return res


def prefix_hist_numpy(m, r):
    """Vectorized exact histogram (numpy int64 bulk iteration). Same result as small."""
    import numpy as np
    R = 1 << r
    mask_mod = R - 1
    N = 1 << (m - 1)  # number of odd h < 2^m
    x = np.arange(1, 1 << m, 2, dtype=np.int64)
    assert len(x) == N
    k = np.zeros(N, dtype=np.int64)
    for _ in range(m):
        odd = (x & 1).astype(np.int64)
        k += odd
        # H step, exact integer arithmetic
        x = np.where(odd.astype(bool), (3 * x + 1) // 2, x // 2)
    z = (x & mask_mod).astype(np.int64)
    res = {}
    for kk in range(1, m + 1):
        sel = z[k == kk]
        bc = np.bincount(sel, minlength=R)
        assert len(bc) == R
        # mass check
        assert int(bc.sum()) == comb(m - 1, kk - 1), (m, kk, int(bc.sum()))
        res[kk] = [int(v) for v in bc]
    # total mass check
    assert sum(sum(v) for v in res.values()) == (1 << (m - 1))
    return res


def prefix_hist(m, r, method="auto"):
    if method == "numpy":
        return prefix_hist_numpy(m, r)
    if method == "small":
        return prefix_hist_small(m, r)
    # auto: small for m<=12 else numpy
    if m <= 12:
        return prefix_hist_small(m, r)
    return prefix_hist_numpy(m, r)


def J_of(X, r):
    half = 1 << (r - 1)
    tot = 0
    for u in range(half):
        dd = X[u] - X[u + half]
        tot += dd * dd
    return Fraction(half * tot)


def Ecal_of(hist, m, r):
    tot = Fraction(0)
    for k in range(1, m + 1):
        nk = comb(m - 1, k - 1)
        tot += J_of(hist[k], r) / nk
    return tot


def transfer_of(P, k, s):
    N = 1 << (s + 1)
    q = 1 << s
    ck = pow(3, k, N)
    rinv = pow(3, -1, N)
    E = [0] * q
    O = [0] * q
    for zz in range(q):
        E[zz] = P[(2 * zz) % N] + P[(2 * zz - ck) % N]
        w = (rinv * (2 * zz - 1)) % N
        O[zz] = P[w] + P[(w - ck) % N]
    return E, O


def row_of(m, s, hist_hi=None, hist_out=None, method="auto"):
    if hist_hi is None:
        hist_hi = prefix_hist(m, s + 1, method=method)
    if hist_out is None:
        hist_out = prefix_hist(m + 1, s, method=method)
    I = Ecal_of(hist_hi, m, s + 1)
    Out = Ecal_of(hist_out, m + 1, s)
    F = Fraction(0)
    EO = {}
    for k in range(1, m + 1):
        nk = comb(m - 1, k - 1)
        E, O = transfer_of(hist_hi[k], k, s)
        EO[k] = (E, O)
        F += (J_of(E, s) + J_of(O, s)) / nk
    L = F - I
    M = F - Out
    return dict(m=m, s=s, I=I, F=F, Out=Out, L=L, M=M, defect=I - Out,
                hist_hi=hist_hi, hist_out=hist_out, EO=EO)


def autocorr(P, d):
    N = len(P)
    return sum(P[u] * P[(u + d) % N] for u in range(N))


def L_terms_of(hist_hi, m, s):
    N = 1 << (s + 1)
    q = 1 << s
    out = {}
    for k in range(1, m + 1):
        nk = comb(m - 1, k - 1)
        d = pow(3, k, N)
        val = autocorr(hist_hi[k], d) - autocorr(hist_hi[k], (d + q) % N)
        out[k] = Fraction(q * val, nk)
    return out


def M_terms_of(hist_hi, m, s):
    n = {k: comb(m - 1, k - 1) for k in range(1, m + 1)}
    out = {1: Fraction(0), m + 1: Fraction(0)}
    for j in range(2, m + 1):
        Ej, _ = transfer_of(hist_hi[j], j, s)
        _, Oj1 = transfer_of(hist_hi[j - 1], j - 1, s)
        X = [n[j - 1] * a - n[j] * b for a, b in zip(Ej, Oj1)]
        num = J_of(X, s)
        den = n[j] * n[j - 1] * (n[j] + n[j - 1])
        out[j] = Fraction(num, den)
    return out


def supply_radius2(M, m, a, b):
    lo = max(a - 1, 2)
    hi = min(b + 2, m)
    if lo > hi:
        return Fraction(0)
    return sum((M[j] for j in range(lo, hi + 1)), Fraction(0))


def supply_radius1(M, m, a, b):
    # CONVENTION TRAP: lower end a (NOT a-1), upper b+1.
    lo = a
    hi = min(b + 1, m + 1)
    if lo > hi:
        return Fraction(0)
    return sum((M.get(j, Fraction(0)) for j in range(lo, hi + 1)), Fraction(0))


def demand_of(L, a, b):
    return sum((v for v in (L[k] for k in range(a, b + 1)) if v > 0), Fraction(0))


def charging_violations_r2(L, M, m):
    bad = []
    for a in range(1, m + 1):
        for b in range(a, m + 1):
            dem = demand_of(L, a, b)
            sup = supply_radius2(M, m, a, b)
            if dem > sup:
                bad.append((a, b, dem, sup))
    return bad


def charging_violations_r1(L, M, m):
    bad = []
    for a in range(1, m + 1):
        for b in range(a, m + 1):
            dem = demand_of(L, a, b)
            sup = supply_radius1(M, m, a, b)
            if dem > sup:
                bad.append((a, b, dem, sup))
    return bad


def adversary_L_M(Pdict, m, s):
    """L_lift = F - I and M_merge = sum M_j from hypothetical P_k on Z/2^(s+1)."""
    N = 1 << (s + 1)
    n = {k: comb(m - 1, k - 1) for k in range(1, m + 1)}
    I = Fraction(0)
    F = Fraction(0)
    EO = {}
    for k in range(1, m + 1):
        P = list(Pdict[k])
        assert len(P) == N
        assert sum(P) == n[k], (k, sum(P), n[k])
        I += J_of(P, s + 1) / n[k]
        E, O = transfer_of(P, k, s)
        EO[k] = (E, O)
        F += (J_of(E, s) + J_of(O, s)) / n[k]
    L = F - I
    # M via identity
    Mall = {1: Fraction(0), m + 1: Fraction(0)}
    for j in range(2, m + 1):
        Ej = EO[j][0]
        Oj1 = EO[j - 1][1]
        X = [n[j - 1] * a - n[j] * b for a, b in zip(Ej, Oj1)]
        Mall[j] = Fraction(J_of(X, s), n[j] * n[j - 1] * (n[j] + n[j - 1]))
    Mall[1] = Fraction(0)
    Mall[m + 1] = Fraction(0)
    Mm = sum((Mall[j] for j in range(2, m + 1)), Fraction(0))
    return L, Mm, I, F, Mall
