"""FLANK calibration gate -- independent from-scratch implementation.

[EXACT COMPUTATION] Everything here is int / fractions.Fraction.
Shortcut H, prefix histograms P_{m,k,r}, energy J_r, Ecal, transfer E_k/O_k,
per-stratum L_k/M_j, adversaries, radius-1 witness.
"""
from fractions import Fraction
from math import comb


def H(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2


def prefix_hist(m, r):
    """Return {k: list length 2^r} with P_{m,k,r} counts. [EXACT COMPUTATION]"""
    R = 1 << r
    hist = {k: [0] * R for k in range(1, m + 1)}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
                x = (3 * x + 1) >> 1
            else:
                x >>= 1
        hist[k][x % R] += 1
    return hist


def J_energy(X, r):
    half = 1 << (r - 1)
    s = 0
    for u in range(half):
        d = X[u] - X[u + half]
        s += d * d
    return Fraction(half * s)


def Ecal_of(m, r, hist=None):
    if hist is None:
        hist = prefix_hist(m, r)
    tot = Fraction(0)
    for k in range(1, m + 1):
        tot += Fraction(J_energy(hist[k], r), comb(m - 1, k - 1))
    return tot


def transfer_EO(P, k, s):
    N = 1 << (s + 1)
    q = 1 << s
    ck = pow(3, k, N)
    rinv = pow(3, -1, N)
    E = [0] * q
    O = [0] * q
    for z in range(q):
        E[z] = P[(2 * z) % N] + P[(2 * z - ck) % N]
        w = (rinv * (2 * z - 1)) % N
        O[z] = P[w] + P[(w - ck) % N]
    return E, O


def full_row(m, s):
    hist_hi = prefix_hist(m, s + 1)
    hist_out = prefix_hist(m + 1, s)
    I = Ecal_of(m, s + 1, hist_hi)
    Out = Ecal_of(m + 1, s, hist_out)
    F = Fraction(0)
    EO = {}
    for k in range(1, m + 1):
        E, O = transfer_EO(hist_hi[k], k, s)
        EO[k] = (E, O)
        F += Fraction(J_energy(E, s) + J_energy(O, s), comb(m - 1, k - 1))
    L = F - I
    M = F - Out
    return dict(m=m, s=s, I=I, F=F, Out=Out, L=L, M=M,
                defect=I - Out, hist_hi=hist_hi, EO=EO)


def autocorr_cyclic(P, d):
    N = len(P)
    return sum(P[u] * P[(u + d) % N] for u in range(N))


def stratum_L(Pk, k, m, s):
    N = 1 << (s + 1)
    q = 1 << s
    ck = pow(3, k, N)
    val = autocorr_cyclic(Pk, ck) - autocorr_cyclic(Pk, (ck + q) % N)
    return Fraction(q * val, comb(m - 1, k - 1))


def stratum_M(Ej, Ojm1, j, m, s):
    nj = comb(m - 1, j - 1)
    njm = comb(m - 1, j - 2)
    D = [njm * a - nj * b for a, b in zip(Ej, Ojm1)]
    num = J_energy(D, s)
    den = nj * njm * (nj + njm)
    return Fraction(num, den)


def adversary_row(m, s, Pdict):
    """Pdict: {k: list length N=2^(s+1)}. Returns (L_lift, M_merge) via stratum formulas."""
    N = 1 << (s + 1)
    L = Fraction(0)
    Lk = {}
    for k, Pk in Pdict.items():
        assert len(Pk) == N
        assert sum(Pk) == comb(m - 1, k - 1), (k, sum(Pk))
        Lk[k] = stratum_L(Pk, k, m, s)
        L += Lk[k]
    EO = {}
    for k, Pk in Pdict.items():
        EO[k] = transfer_EO(Pk, k, s)
    M = Fraction(0)
    Mj = {1: Fraction(0), m + 1: Fraction(0)}
    for j in range(2, m + 1):
        Mj[j] = stratum_M(EO[j][0], EO[j - 1][1], j, m, s)
        M += Mj[j]
    return L, M, Lk, Mj


def radius_supply_demand(m, s, a, b, radius, Lk, Mj):
    demand = sum(v for k, v in Lk.items() if a <= k <= b and v > 0)
    lo = max(a - 1, 2) if radius == 2 else max(a, 2)
    # radius-1 convention trap: lower end a (NOT a-1); upper b+1
    # radius-2: lower max(a-1,2), upper min(b+2,m)
    if radius == 2:
        lo = max(a - 1, 2)
        hi = min(b + 2, m)
    else:
        lo = max(a, 2)
        hi = min(b + 1, m)
    supply = sum(Mj[j] for j in range(lo, hi + 1)) if lo <= hi else Fraction(0)
    return demand, supply


if __name__ == "__main__":
    ok = True

    def check(name, got, want):
        global ok
        good = (got == want)
        ok = ok and good
        print(f"  {name}: got {got} want {want} {'OK' if good else 'MISMATCH'}")

    print("GATE rows:")
    r = full_row(4, 2)
    check("(4,2) I", r["I"], Fraction(40, 3))
    check("(4,2) F", r["F"], Fraction(16))
    check("(4,2) Out", r["Out"], Fraction(31, 3))
    check("(4,2) L", r["L"], Fraction(8, 3))
    check("(4,2) M", r["M"], Fraction(17, 3))
    check("(4,2) defect", r["defect"], Fraction(3))

    r = full_row(3, 2)
    check("(3,2) I", r["I"], Fraction(12))
    check("(3,2) F", r["F"], Fraction(12))
    check("(3,2) Out", r["Out"], Fraction(8))
    check("(3,2) L", r["L"], Fraction(0))
    check("(3,2) M", r["M"], Fraction(4))

    r = full_row(2, 1)
    check("(2,1) I", r["I"], Fraction(4))
    check("(2,1) F", r["F"], Fraction(4))
    check("(2,1) Out", r["Out"], Fraction(4))
    check("(2,1) L", r["L"], Fraction(0))
    check("(2,1) M", r["M"], Fraction(0))

    print("ADVERSARY 1 (3,2) on Z/8:")
    P1 = {1: [0, 0, 1, 0, 0, 0, 0, 0],
          2: [1, 0, 0, 0, 0, 0, 0, 1],
          3: [0, 0, 0, 0, 1, 0, 0, 0]}
    L, M, _, _ = adversary_row(3, 2, P1)
    check("ADV1 L", L, Fraction(2))
    check("ADV1 M", M, Fraction(2, 3))

    print("ADVERSARY 2 (5,2) on Z/8:")
    P2 = {1: [0, 0, 1, 0, 0, 0, 0, 0],
          2: [0, 3, 1, 0, 0, 0, 0, 0],
          3: [0, 3, 0, 0, 2, 0, 1, 0],
          4: [1, 0, 0, 0, 3, 0, 0, 0],
          5: [0, 0, 1, 0, 0, 0, 0, 0]}
    L, M, _, _ = adversary_row(5, 2, P2)
    check("ADV2 L", L, Fraction(9))
    check("ADV2 M", M, Fraction(101, 15))

    print("RADIUS-1 witness (18,2) interval [14,14]:")
    m, s = 18, 2
    hist = prefix_hist(m, s + 1)
    Lk = {k: stratum_L(hist[k], k, m, s) for k in range(1, m + 1)}
    EO = {k: transfer_EO(hist[k], k, s) for k in range(1, m + 1)}
    Mj = {1: Fraction(0), m + 1: Fraction(0)}
    for j in range(2, m + 1):
        Mj[j] = stratum_M(EO[j][0], EO[j - 1][1], j, m, s)
    dem, sup = radius_supply_demand(m, s, 14, 14, 1, Lk, Mj)
    check("(18,2)[14,14] demand", dem, Fraction(3, 35))
    check("(18,2)[14,14] supply", sup, Fraction(4033, 69615))
    check("(18,2)[14,14] gap", dem - sup, Fraction(1934, 69615))

    print("GATE_OK =", ok)
