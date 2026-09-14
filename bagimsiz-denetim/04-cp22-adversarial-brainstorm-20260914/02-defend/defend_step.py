"""Can cap-bounds (triangle or support-refined) close the radius-2 step on REAL levels?
Strongest case for the defender: REAL parent caps + REAL parent supports.
Failure here kills the bound-family a fortiori (propagated bounds are weaker).
Exact arithmetic. DB_k bounds max(L_k,0); interval test sums them vs real supply.
"""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist, transfer, J, L_terms, M_terms
from defend_R import w_of, Tpow, dot
from defend_R3fix import corrected_parent_diffs
from defend_LXbound import real_cap

def step_bounds(m, s):
    N = 1 << (s+1); q = 1 << s; N2 = 1 << (s+2)
    hist = prefix_hist(m, s+1)
    Q = prefix_hist(m-1, s+2)
    L = L_terms(hist, m, s)
    EO = {k: transfer(hist[k], k, s) for k in range(1, m+1)}
    M = M_terms(EO, m, s)
    out = {}
    for k in range(1, m+1):
        Qk = list(Q[k]) if (1 <= k <= m-1) else [0]*N2
        Qk1 = list(Q[k-1]) if (1 <= k-1 <= m-1) else [0]*N2
        dA, dB, _, _, _, _, _ = corrected_parent_diffs(Qk, Qk1, k, s)
        CE = real_cap(m-1, k, s+2) if (1 <= k <= m-1) else 0
        CO = real_cap(m-1, k-1, s+2) if (1 <= k-1 <= m-1) else 0
        nk = comb(m-1, k-1)
        # sanity: entries respect 2C
        assert all(abs(x) <= 2*CE for x in dA) and all(abs(x) <= 2*CO for x in dB)
        # triangle bounds on inner products
        tLE = 4*q*CE*CE; tLO = 4*q*CO*CO; tLX = 8*q*CE*CO
        DBtri = Fraction(q*(tLE+tLO+tLX), nk)
        # support-refined
        sA = sum(1 for x in dA if x != 0); sO = sum(1 for x in dB if x != 0)
        TdB = Tpow(dB, pow(3, k, N), s); TdA = Tpow(dA, pow(3, k, N), s)
        j1 = sum(1 for a, b in zip(dA, TdB) if a != 0 and b != 0)
        j2 = sum(1 for a, b in zip(dB, TdA) if a != 0 and b != 0)
        # |<dA,TdA>| <= sA*(2CE)^2 etc; cross <= j*4CECO
        rLE = sA*4*CE*CE; rLO = sO*4*CO*CO; rLX = (j1+j2)*4*CE*CO
        DBsup = Fraction(q*(rLE+rLO+rLX), nk)
        out[k] = dict(L=L[k], DBtri=DBtri, DBsup=DBsup,
                      CE=CE, CO=CO, sA=sA, sO=sO, j1=j1, j2=j2)
    return out, L, M

def interval_failures(m, s, key):
    data, L, M = step_bounds(m, s)
    fails = []
    for a in range(1, m+1):
        for b in range(a, m+1):
            dem = sum(data[k][key] for k in range(a, b+1))
            lo = max(a-1, 2); hi = min(b+2, m)
            sup = sum(M[j] for j in range(lo, hi+1)) if lo <= hi else Fraction(0)
            if dem > sup:
                fails.append((a, b, dem, sup))
    return fails, data, L, M

if __name__ == "__main__":
    import sys
    levels = [(m, s) for m in range(3, 11) for s in range(1, m)]
    levels += [(13, 12), (18, 2)]
    T = S = 0
    for (m, s) in levels:
        ft, data, L, M = interval_failures(m, s, "DBtri")
        fs, _, _, _ = interval_failures(m, s, "DBsup")
        nint = m*(m+1)//2
        T += len(ft); S += len(fs)
        # tightest interval margin for support bounds
        print("(m=%d,s=%d) intervals=%d tri-fails=%d sup-fails=%d" % (m, s, nint, len(ft), len(fs)))
        if len(fs) <= 3 and len(fs) > 0:
            for (a, b, d, sp) in fs:
                print("   sup-fail [%d,%d] bound=%s supply=%s" % (a, b, d, sp))
    print("TOTAL tri-fails=%d sup-fails=%d" % (T, S))
    # show a concrete tight/loose example
    data, L, M = step_bounds(9, 2)
    print("--- (9,2) L vs DBtri vs DBsup ---")
    for k in sorted(data):
        d = data[k]
        print("  k=%d L=%s DBtri=%s DBsup=%s" % (k, d["L"], d["DBtri"], d["DBsup"]))
