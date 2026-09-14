"""Exact global minimum of Delta^(a) (cross-field safe) + lift carrier analysis.

Fixes the naive-min bug: Delta^(a) for different s live in different cyclotomic
fields, so they are embedded into a common Z[zeta_{2^T}] before comparison, and
compared by certified rational enclosures (sign_of_real).
"""
import sys, os, json, time
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, sign_of_real, to_rational, approx_str
from source import row, run_gate
from freq import dft, embed


def parts(m, s):
    """L^(a), M^(a), Delta^(a) on the forced index a odd mod q, gauge E."""
    N = 1 << (s + 1); q = 1 << s; d = N // 2
    r = row(m, s); hist = r["hist_hi"]; inv3 = pow(3, -1, N)
    Ph, Ah, Bh, Eh, Oh = {}, {}, {}, {}, {}
    for k in range(1, m + 1):
        P = hist[k]
        Ph[k] = dft(P, s + 1)
        Ah[k] = dft([P[z] if z % 2 == 0 else 0 for z in range(N)], s + 1)
        Bh[k] = dft([P[z] if z % 2 == 1 else 0 for z in range(N)], s + 1)
    for k in range(1, m + 1):
        ck = pow(3, k, N); Eh[k], Oh[k] = {}, {}
        for xi in range(1, N, 2):
            Eh[k][xi] = Ah[k][xi] + Cyc.zpow(d, xi * ck) * Bh[k][xi]
            x3 = (3 * xi) % N
            Oh[k][xi] = Cyc.zpow(d, xi) * (Bh[k][x3] + Cyc.zpow(d, 3 * xi * ck) * Ah[k][x3])
    def base(a, k):
        b = (pow(inv3, k, N) * a) % N % q
        if b % 2 == 0: b += q
        return [b, b + q] if b < q else [b - q, b]
    odd_q = list(range(1, q, 2))
    Lp, Mp, D = {}, {}, {}
    for a in odd_q:
        L = Cyc(d); M = Cyc(d)
        for k in range(1, m + 1):
            nk = comb(m - 1, k - 1)
            for xi in base(a, k):
                ckx = (pow(3, k, N) * xi) % N
                cosv = (Cyc.zpow(d, ckx) + Cyc.zpow(d, -ckx)).scale(Fraction(1, 2))
                L = L + (cosv * norm2(Ph[k][xi])).scale(Fraction(1, nk))
        for k in range(2, m + 1):
            nk = comb(m - 1, k - 1); nkm = comb(m - 1, k - 2)
            for xi in base(a, k):
                Dv = Eh[k][xi].scale(nkm) - Oh[k - 1][xi].scale(nk)
                M = M + norm2(Dv).scale(Fraction(1, 2 * nk * nkm * (nk + nkm)))
        Lp[a], Mp[a], D[a] = L, M, M - L
    sL, sM = Cyc(d), Cyc(d)
    for a in odd_q:
        sL = sL + Lp[a]; sM = sM + Mp[a]
    rL, rM = to_rational(sL), to_rational(sM)
    ok = (rL == r["L"] and rM == r["M"] and rM - rL == r["defect"])
    return ok, Lp, Mp, D, r


if __name__ == "__main__":
    assert run_gate(verbose=False); print("GATE OK\n")
    pairs = [(m, s) for s in (2, 3, 4) for m in range(4, 13) if s <= m - 1]
    extra = [(m, 5) for m in range(6, 15)] + [(m, s) for s in (2, 3, 4) for m in (13, 14)]
    T = 6; DB = 1 << (T - 1)     # common field Z[zeta_64]
    t0 = time.time()
    best = None; bestL = None
    out = []
    negtotal = 0
    for (m, s) in pairs + extra:
        ok, Lp, Mp, D, r = parts(m, s)
        assert ok, ("IDENTITY FAILED", m, s)
        q = 1 << s
        sg = {a: sign_of_real(D[a]) for a in D}
        lsg = {a: sign_of_real(Lp[a]) for a in D}
        neg = [a for a in sg if sg[a] < 0]
        negtotal += len(neg)
        carriers = [a for a in lsg if lsg[a] > 0]
        for a in D:
            e = embed(D[a], DB)
            if best is None or sign_of_real(best[0] - e) > 0:
                best = (e, m, s, a, D[a])
        out.append(dict(m=m, s=s, q=q, defect=str(r["defect"]), L=str(r["L"]),
                        M=str(r["M"]), identity_ok=ok,
                        signs={str(a): sg[a] for a in sorted(sg)},
                        lift_signs={str(a): lsg[a] for a in sorted(lsg)},
                        negative_a=neg, lift_carriers=carriers,
                        deltas={str(a): (str(to_rational(D[a])) if to_rational(D[a]) is not None
                                         else "~" + approx_str(D[a], 18)) for a in sorted(D)}))
    be, bm, bs, ba, braw = best
    print("GRID: %d rows (s=2,3,4 x m=4..12  PLUS s=5 m=6..14 and m=13,14 for s=2,3,4)" % len(out))
    print("identity sum_a Delta^(a) == defect: holds EXACTLY on all %d rows" % len(out))
    print("total (row,frequency) pairs with Delta^(a) < 0 : %d" % negtotal)
    print()
    rv = to_rational(braw)
    print("EXACT MINIMUM of Delta^(a) over the whole grid:")
    print("   value  = %s" % (rv if rv is not None else braw.c))
    print("   at     = (m=%d, s=%d), frequency a=%d (odd mod q=2^%d)" % (bm, bs, ba, bs))
    print("   enclosure ~ %s" % approx_str(be, 24))
    print()
    print("LIFT CARRIER (which a has L^(a) > 0):")
    for t in sorted(out, key=lambda x: (x["s"], x["m"])):
        print("  (%2d,%d) q=%-3d L_lift=%-15s carriers a=%s   min-ish Delta: %s"
              % (t["m"], t["s"], t["q"], t["L"], t["lift_carriers"],
                 min(t["deltas"].values(), key=lambda z: (z.startswith("~"), z))))
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(dict(rows=out, min_delta=(str(rv) if rv is not None else [str(x) for x in braw.c]),
                   min_row="(m=%d,s=%d)" % (bm, bs), min_a=ba,
                   min_approx=approx_str(be, 24), negatives=negtotal,
                   secs=round(time.time() - t0, 1)),
              open(os.path.join(here, "minmax.json"), "w"), indent=1)
    print("\nelapsed %.1fs -> minmax.json" % (time.time() - t0))
