"""Task 3: T6 propagation law + W(4,2) composite-membership test + support-refined LX bound.
All exact. No ref/ imports.
"""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist, transfer, J
from defend_R import w_of, Tpow, dot
from defend_LXsplit import split_level
from defend_R3fix import corrected_parent_diffs
from defend_LXbound import real_cap

def Epar(Q, k, sp):
    Np = 1 << (sp+1)
    c = pow(3, k, Np)
    return [Q[(2*z) % Np]+Q[(2*z-c) % Np] for z in range(1 << sp)]

def Opar(Q, k, sp):
    Np = 1 << (sp+1)
    c = pow(3, k, Np); rinv = pow(3, -1, Np)
    out = []
    for z in range(1 << sp):
        t = (rinv*(2*z-1)) % Np
        out.append(Q[t]+Q[(t-c) % Np])
    return out

def autoc(P, d):
    N = len(P)
    return sum(P[u]*P[(u+d) % N] for u in range(N))

def LM_of_Plist(Plist, m, s):
    """L_k, M_j from arbitrary P lists (length N). Masses binomial (must match totals)."""
    N = 1 << (s+1); q = 1 << s
    L = {}
    for k in range(1, m+1):
        d = pow(3, k, N)
        L[k] = Fraction(q*(autoc(Plist[k], d)-autoc(Plist[k], (d+q) % N)), comb(m-1, k-1))
    EO = {k: (Epar(Plist[k], k, s) if False else None) for k in range(1, m+1)}
    # child E/O at modulus s (transfer at N): reuse defend_gate.transfer
    from defend_gate import transfer as tr
    EO = {k: tr(Plist[k], k, s) for k in range(1, m+1)}
    M = {1: Fraction(0), m+1: Fraction(0)}
    for j in range(2, m+1):
        nj = comb(m-1, j-1); njm = comb(m-1, j-2)
        D = [njm*EO[j][0][z]-nj*EO[j-1][1][z] for z in range(q)]
        M[j] = Fraction(J(D, s), nj*njm*(nj+njm))
    return L, M

def charging_ok(L, M, m, radius=2):
    bad = []
    for a in range(1, m+1):
        for b in range(a, m+1):
            dem = sum(x for x in (L[k] for k in range(a, b+1)) if x > 0)
            lo = max(a-1, 2); hi = min(b+radius, m)
            sup = sum(M[j] for j in range(lo, hi+1)) if lo <= hi else Fraction(0)
            if dem > sup:
                bad.append((a, b, dem, sup))
    return bad

def t6_rhs(m, k, r):
    """2*cap(m-1,k,r+1)+2*cap(m-1,k-1,r+1), real caps; edge strata use 0 for k out of range."""
    a = real_cap(m-1, k, r+1) if (1 <= k <= m-1) else 0
    b = real_cap(m-1, k-1, r+1) if (1 <= k-1 <= m-1) else 0
    return 2*a+2*b

if __name__ == "__main__":
    print("== T6 law on grid (propagated bound >= real cap?) ==")
    nT = nOk = 0
    worst = None
    for m in range(3, 11):
        for r in range(1, 4):
            for k in range(1, m+1):
                nT += 1
                lhs = real_cap(m, k, r); rhs = t6_rhs(m, k, r)
                if lhs <= rhs:
                    nOk += 1
                else:
                    print("T6 VIOLATION (m=%d,k=%d,r=%d) cap=%d prop=%d" % (m, k, r, lhs, rhs))
                if worst is None or Fraction(rhs, max(lhs, 1)) < worst[0]:
                    worst = (Fraction(rhs, max(lhs, 1)), m, k, r, lhs, rhs)
    print("T6 holds %d/%d; loosest propagation ratio=%s at (m=%d,k=%d,r=%d) cap=%d prop=%d" % (
        nOk, nT, worst[0], worst[1], worst[2], worst[3], worst[4], worst[5]))
    print("== W(4,2) ==")
    # parent (3,3) on Z/16
    Q = {0: [0]*16, 1: [0]*16, 2: [0]*16, 3: [0]*16, 4: [0]*16}
    Q[1][14] = 1; Q[2][6] = 2; Q[3][4] = 1
    Lp, Mp = LM_of_Plist(Q, 3, 3)
    badp = charging_ok(Lp, Mp, 3)
    print("parent L'=%s M'=%s" % ({k: str(v) for k, v in Lp.items()}, {k: str(v) for k, v in Mp.items()}))
    print("parent radius-2 violations: %s (hypothesis holds: %s)" % (badp, len(badp) == 0))
    # real caps at parent: does Q satisfy them?
    for k in range(1, 4):
        print("  parent stratum %d: maxpile=%d realcap(3,%d,4)=%d %s" % (
            k, max(Q[k]), k, real_cap(3, k, 4),
            "OK" if max(Q[k]) <= real_cap(3, k, 4) else "EXCEEDS REAL CAP"))
    # child via parent map at sp=3 (N=16 -> 8)
    P = {}
    Z = [0]*16
    for k in range(1, 5):
        Qk = Q[k] if k <= 3 else Z
        Qk1 = Q[k-1] if k-1 >= 1 else Z
        A = Epar(Qk, k, 3); B = Opar(Qk1, k-1, 3)
        P[k] = [a+b for a, b in zip(A, B)]
    print("child masses:", {k: sum(P[k]) for k in P}, " want n:", {k: comb(3, k-1) for k in range(1, 5)})
    Lc, Mc = LM_of_Plist(P, 4, 2)
    dem = sum(x for x in Lc.values() if x > 0); sup = sum(Mc[j] for j in range(2, 5))
    print("child L=%s M=%s" % ({k: str(v) for k, v in Lc.items()}, {k: str(v) for k, v in Mc.items()}))
    print("child demand=%s (want 16/3) supply=%s (want 14/3)" % (dem, sup))
    badc = charging_ok(Lc, Mc, 4)
    print("child radius-2 violations: %s" % [(a, b, str(d), str(s)) for (a, b, d, s) in badc])
    # T6-propagated caps from REAL parent caps: does W-child satisfy them?
    print("T6-cap membership of W-child (propagated from REAL parent caps):")
    t6ok = True
    for k in range(1, 5):
        prop = 2*(real_cap(3, k, 4) if 1 <= k <= 3 else 0)+2*(real_cap(3, k-1, 4) if 1 <= k-1 <= 3 else 0)
        mp = max(P[k])
        good = mp <= prop
        t6ok = t6ok and good
        print("  child stratum %d: maxpile=%d T6prop=%d %s" % (k, mp, prop, "OK" if good else "EXCEEDS"))
    print("W-child satisfies {parent-Hyp + T6-cap}:", (len(badp) == 0) and t6ok,
          " but violates child Hyp:", len(badc) > 0)
