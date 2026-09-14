"""Collatz prefix source, energies, transfer, lift/merge -- exact arithmetic.

Everything is integers / fractions.Fraction.  NO FLOATING POINT.

Definitions (as handed down, re-implemented from scratch):
  H(x) = (3x+1)//2 if x odd else x//2
  P_{m,k,r}(z) = #{odd h < 2^m : #odd steps in m shortcut steps = k, H^m(h) = z mod 2^r}
  n_k = C(m-1,k-1)
  J_r(X) = 2^(r-1) * sum_{u<2^(r-1)} (X(u) - X(u+2^(r-1)))^2
  Ecal(m,r) = sum_k J_r(P_{m,k,r}) / n_k
  N = 2^(s+1), q = 2^s, c_k = 3^k mod N, rinv = 3^-1 mod N
  E_k[z] = P_k[2z mod N] + P_k[(2z-c_k) mod N]
  O_k[z] = P_k[rinv(2z-1) mod N] + P_k[(rinv(2z-1)-c_k) mod N]
  I = Ecal(m,s+1); F = sum_k (J_s(E_k)+J_s(O_k))/n_k; Out = Ecal(m+1,s)
  L = F - I; M = F - Out; defect = I - Out = M - L
"""
from fractions import Fraction
from math import comb


def prefix_hist(m, r):
    """P_{m,k,r} as {k: [counts over z mod 2^r]}."""
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


def J(X, r):
    """odd-character energy, sibling-difference form."""
    half = 1 << (r - 1)
    tot = 0
    for u in range(half):
        dd = X[u] - X[u + half]
        tot += dd * dd
    return Fraction(half * tot)


def Ecal(m, r, hist=None):
    if hist is None:
        hist = prefix_hist(m, r)
    tot = Fraction(0)
    for k in range(1, m + 1):
        nk = comb(m - 1, k - 1)
        if nk == 0:
            continue
        tot += J(hist[k], r) / nk
    return tot


def transfer(P, k, s):
    """E_k, O_k arrays of length q = 2^s from P (length N = 2^(s+1))."""
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


def row(m, s, hist_hi=None, hist_out=None):
    """Return dict with exact I, F, Out, L, M, defect, plus arrays for reuse."""
    if hist_hi is None:
        hist_hi = prefix_hist(m, s + 1)
    if hist_out is None:
        hist_out = prefix_hist(m + 1, s)
    I = Ecal(m, s + 1, hist_hi)
    Out = Ecal(m + 1, s, hist_out)
    F = Fraction(0)
    EO = {}
    for k in range(1, m + 1):
        nk = comb(m - 1, k - 1)
        E, O = transfer(hist_hi[k], k, s)
        EO[k] = (E, O)
        F += (J(E, s) + J(O, s)) / nk
    L = F - I
    M = F - Out
    return dict(m=m, s=s, I=I, F=F, Out=Out, L=L, M=M, defect=I - Out,
                hist_hi=hist_hi, EO=EO)


def merge_identity(r):
    """M_merge = sum_{k=2..m} J_s(n_{k-1}E_k - n_k O_{k-1}) / (n_k n_{k-1}(n_k+n_{k-1}))."""
    m, s = r["m"], r["s"]
    q = 1 << s
    tot = Fraction(0)
    per_k = {}
    for k in range(2, m + 1):
        nk = comb(m - 1, k - 1)
        nkm = comb(m - 1, k - 2)
        E = r["EO"][k][0]
        O = r["EO"][k - 1][1]
        D = [nkm * E[z] - nk * O[z] for z in range(q)]
        w = nk * nkm * (nk + nkm)
        val = J(D, s) / w
        per_k[k] = val
        tot += val
    return tot, per_k


# ----------------------------------------------------------------- gate -----

GATE = [
    ((4, 2), dict(I=Fraction(40, 3), F=Fraction(16), Out=Fraction(31, 3),
                  L=Fraction(8, 3), M=Fraction(17, 3), defect=Fraction(3))),
    ((2, 1), dict(I=Fraction(4), F=Fraction(4), Out=Fraction(4),
                  L=Fraction(0), M=Fraction(0), defect=Fraction(0))),
    ((3, 2), dict(I=Fraction(12), F=Fraction(12), Out=Fraction(8),
                  L=Fraction(0), M=Fraction(4), defect=Fraction(4))),
]


def run_gate(verbose=True):
    ok = True
    lines = []
    for (m, s), exp in GATE:
        r = row(m, s)
        mm, per_k = merge_identity(r)
        for key, want in exp.items():
            got = r[key]
            good = got == want
            ok &= good
            lines.append("  (m=%d,s=%d) %-6s got %-10s want %-10s %s"
                         % (m, s, key, got, want, "OK" if good else "MISMATCH"))
        good = (mm == r["M"])
        ok &= good
        lines.append("  (m=%d,s=%d) %-6s got %-10s want %-10s %s"
                     % (m, s, "M_sum", mm, r["M"], "OK" if good else "MISMATCH"))
    if verbose:
        print("GATE (published values, reproduced from scratch):")
        print("\n".join(lines))
        print("GATE_OK =", ok)
    return ok


if __name__ == "__main__":
    run_gate()
