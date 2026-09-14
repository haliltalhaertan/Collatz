"""Correct symmetric LE/LO/LX split + recheck of handed-down LX witness claims."""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist, L_terms
from defend_R import w_of, Tpow, dot
from defend_R3fix import corrected_parent_diffs

def split_level(m, s):
    N = 1 << (s+1); q = 1 << s; N2 = 1 << (s+2)
    hist = prefix_hist(m, s+1)
    Q = prefix_hist(m-1, s+2)
    L = L_terms(hist, m, s)
    ok = True; rows = {}
    for k in range(1, m+1):
        w = w_of(hist[k], s)
        Qk = list(Q[k]) if (1 <= k <= m-1) else [0]*N2
        Qk1 = list(Q[k-1]) if (1 <= k-1 <= m-1) else [0]*N2
        dA, dB, fA, fB, _, _, _ = corrected_parent_diffs(Qk, Qk1, k, s)
        assert dA == fA and dB == fB
        assert [a+b for a, b in zip(dA, dB)] == w
        T = Tpow([0]*q, 0, s)  # placeholder
        def Tp(v):
            return Tpow(v, pow(3, k, N), s)
        LE = dot(dA, Tp(dA)); LO = dot(dB, Tp(dB))
        LXa = dot(dA, Tp(dB)); LXb = dot(dB, Tp(dA))
        LX = LXa+LXb
        nk = comb(m-1, k-1)
        good = Fraction(q*(LE+LO+LX), nk) == L[k]
        ok = ok and good
        rows[k] = dict(L=L[k], LE=Fraction(q*LE, nk), LO=Fraction(q*LO, nk),
                       LXa=Fraction(q*LXa, nk), LXb=Fraction(q*LXb, nk),
                       LX=Fraction(q*LX, nk), sym=(LXa == LXb))
    return ok, rows

if __name__ == "__main__":
    import sys
    # specific witness claims from the brief
    for (m, s, k) in [(7, 6, 5), (13, 12, None)]:
        ok, rows = split_level(m, s)
        print("(m=%d,s=%d) split_ok=%s" % (m, s, ok))
        ks = [k] if k else sorted(rows)
        for kk in ks:
            d = rows[kk]
            print("  k=%d %s" % (kk, {t: str(v) for t, v in d.items()}))
    # parent-demand-0 -> child-positive scan on (13,12): parent level is (12,13)?
    # child (m,s)=(13,12): parents Q=P_{12,*,14}. parent demand at level (12,13)? s+1=13 > m-1=12: degenerate.
    # Instead replicate brief's "25 real levels parent demand 0, child positive" on small grid.
    print("--- scan: child L_k>0 with parent-side LE+LO<=0 (LX-created) ---")
    count = 0
    for m in range(3, 11):
        for s in range(1, m):
            ok, rows = split_level(m, s)
            assert ok
            for k, d in rows.items():
                if d["L"] > 0 and d["LE"]+d["LO"] <= 0:
                    count += 1
                    if count <= 15:
                        print("  (m=%d,s=%d,k=%d) L=%s LE=%s LO=%s LX=%s (LXa=%s LXb=%s sym=%s)" % (
                            m, s, k, d["L"], d["LE"], d["LO"], d["LX"], d["LXa"], d["LXb"], d["sym"]))
    print("total LX-created positive strata on grid m=3..10: %d" % count)
