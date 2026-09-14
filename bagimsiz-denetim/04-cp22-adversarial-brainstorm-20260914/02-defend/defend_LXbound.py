"""Task 2: bound |LX_k| by cap+masses; exact tightness on real levels.
Bound [PROOF]: |A_u|<=2C_E, |B_u|<=2C_O with C_E=cap(m-1,k,s+2), C_O=cap(m-1,k-1,s+2)
  (each parent-diff entry is a difference of two Q-piles; A=E'-image sums two such).
  |<A,TB>|<=q*4*C_E*C_O; |LX_inner|=|<A,TB>+<B,TA>|<=8*q*C_E*C_O.
  |LX_k| <= 8*q^2*C_E*C_O/n_k =: B_k.  (Triangle + orthogonality of T.)
Also CS form: same value (||A||<=2*sqrt(q)*C_E etc. give identical product).
Tightness ratio R_k = B_k/|LX_k| (|LX_k|=0 -> +inf, reported separately).
"""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist
from defend_R import w_of, Tpow, dot
from defend_R3fix import corrected_parent_diffs
from defend_LXsplit import split_level

def real_cap(m, k, r):
    hist = prefix_hist(m, r)
    return max(hist[k])

def lx_rows(m, s):
    N = 1 << (s+1); q = 1 << s; N2 = 1 << (s+2)
    hist = prefix_hist(m, s+1)
    Q = prefix_hist(m-1, s+2)
    ok, rows = split_level(m, s)
    assert ok
    out = []
    for k in range(1, m+1):
        CE = real_cap(m-1, k, s+2) if (1 <= k <= m-1) else 0
        CO = real_cap(m-1, k-1, s+2) if (1 <= k-1 <= m-1) else 0
        nk = comb(m-1, k-1)
        Bk = Fraction(8*q*q*CE*CO, nk)
        out.append((k, rows[k]["LX"], Bk, CE, CO))
    return out

if __name__ == "__main__":
    import sys
    worst = None  # tightest (smallest ratio with LX!=0)
    ntested = nok = nzero = 0
    loosest_shown = []
    for m in range(3, 12):
        for s in range(1, m):
            for (k, LX, Bk, CE, CO) in lx_rows(m, s):
                ntested += 1
                if Bk < abs(LX):
                    print("BOUND VIOLATION (m=%d,s=%d,k=%d) |LX|=%s B=%s" % (m, s, k, LX, Bk))
                else:
                    nok += 1
                if LX == 0:
                    nzero += 1
                else:
                    r = Bk/abs(LX)
                    if worst is None or r < worst[0]:
                        worst = (r, m, s, k, LX, Bk)
    print("tested=%d ok=%d zero-LX=%d nonzero=%d" % (ntested, nok, nzero, ntested-nzero))
    print("TIGHTEST nonzero ratio: R=%s at (m=%d,s=%d,k=%d) |LX|=%s B=%s" % (worst[0], worst[1], worst[2], worst[3], worst[4], worst[5]))
    # distribution snapshot: ratios at a mid level
    print("--- (m=9,s=2) per-stratum ---")
    for (k, LX, Bk, CE, CO) in lx_rows(9, 2):
        print("  k=%d LX=%s B=%s CE=%d CO=%d ratio=%s" % (k, LX, Bk, CE, CO, (Bk/abs(LX) if LX != 0 else "inf")))
