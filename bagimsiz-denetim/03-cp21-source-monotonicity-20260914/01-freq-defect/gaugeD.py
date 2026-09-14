"""GAUGE D: index by odd residue mod q = 2^s  (group xi and xi+q).

This is the convention that reproduces the prior session's published numbers:
at (m,s)=(4,2) it gives Delta^(a) = 3/2 for BOTH a=1 and a=3, total 3.
It is also the *natural* one: E_k and O_k live on Z/q, so their Fourier
frequencies are odd residues mod q; the two lifts xi, xi+q of a given odd
a mod q are summed together.

Also fixes the cross-field comparison bug: all Delta values are embedded into
a common cyclotomic field before taking minima.
"""
import sys, os, json, time
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, sign_of_real, to_rational, approx_str
from source import row, run_gate
from freq import dft, embed


def gauge_D(m, s):
    """Delta^(a) for a odd mod q = 2^s.  Exact.  Returns (ok, signs, D, r)."""
    N = 1 << (s + 1)
    q = 1 << s
    d = N // 2
    r = row(m, s)
    hist = r["hist_hi"]
    Ph, Ah, Bh, Eh, Oh = {}, {}, {}, {}, {}
    for k in range(1, m + 1):
        P = hist[k]
        Ph[k] = dft(P, s + 1)
        Ah[k] = dft([P[z] if z % 2 == 0 else 0 for z in range(N)], s + 1)
        Bh[k] = dft([P[z] if z % 2 == 1 else 0 for z in range(N)], s + 1)
    for k in range(1, m + 1):
        ck = pow(3, k, N)
        Eh[k], Oh[k] = {}, {}
        for xi in range(1, N, 2):
            Eh[k][xi] = Ah[k][xi] + Cyc.zpow(d, xi * ck) * Bh[k][xi]
            x3 = (3 * xi) % N
            Oh[k][xi] = Cyc.zpow(d, xi) * (Bh[k][x3] + Cyc.zpow(d, 3 * xi * ck) * Ah[k][x3])

    odd_q = list(range(1, q, 2)) if q > 1 else [1]
    Lp, Mp, D = {}, {}, {}
    for a in odd_q:
        lifts = [a, a + q]          # the two lifts of a mod q into mod N
        L = Cyc(d)
        M = Cyc(d)
        for xi in lifts:
            for k in range(1, m + 1):
                nk = comb(m - 1, k - 1)
                ckx = (pow(3, k, N) * xi) % N
                cosv = (Cyc.zpow(d, ckx) + Cyc.zpow(d, -ckx)).scale(Fraction(1, 2))
                L = L + (cosv * norm2(Ph[k][xi])).scale(Fraction(1, nk))
            for k in range(2, m + 1):
                nk = comb(m - 1, k - 1)
                nkm = comb(m - 1, k - 2)
                Dv = Eh[k][xi].scale(nkm) - Oh[k - 1][xi].scale(nk)
                M = M + norm2(Dv).scale(Fraction(1, 2 * nk * nkm * (nk + nkm)))
        Lp[a], Mp[a], D[a] = L, M, M - L
    sL, sM = Cyc(d), Cyc(d)
    for a in odd_q:
        sL = sL + Lp[a]
        sM = sM + Mp[a]
    rL, rM = to_rational(sL), to_rational(sM)
    ok = (rL == r["L"] and rM == r["M"] and rM is not None and rL is not None
          and rM - rL == r["defect"])
    signs = {a: sign_of_real(D[a]) for a in odd_q}
    return ok, signs, D, r


if __name__ == "__main__":
    assert run_gate(verbose=False)
    print("GATE OK")
    print()
    # sanity: reproduce the prior session's (4,2) = 3/2 per frequency
    ok, signs, D, r = gauge_D(4, 2)
    print("(4,2) GAUGE D reproduction of prior session's claim:")
    for a in sorted(D):
        print("   a=%d  Delta^(a) = %s  (rational: %s)  sign=%+d"
              % (a, D[a].c, to_rational(D[a]), signs[a]))
    print("   identity_ok =", ok, " defect =", r["defect"])
    print()

    pairs = [(m, s) for s in (2, 3, 4) for m in range(4, 13) if s <= m - 1]
    t0 = time.time()
    DBIG = 16          # Z[zeta_32] contains Z[zeta_8], Z[zeta_16]
    best = None
    table = []
    negrows = 0
    for (m, s) in pairs:
        ok, signs, D, r = gauge_D(m, s)
        assert ok, ("IDENTITY FAILED", m, s)
        q = 1 << s
        neg = [a for a in signs if signs[a] < 0]
        if neg:
            negrows += 1
        table.append(dict(m=m, s=s, q=q, defect=str(r["defect"]), L=str(r["L"]),
                          M=str(r["M"]), signs={str(a): signs[a] for a in sorted(signs)},
                          negative_a=neg, identity_ok=ok,
                          deltas={str(a): (str(to_rational(D[a])) if to_rational(D[a]) is not None
                                           else approx_str(D[a], 20)) for a in sorted(D)}))
        for a in D:
            e = embed(D[a], DBIG)
            if best is None or sign_of_real(best[0] - e) > 0:
                best = (e, m, s, a)
    print("%-9s %-4s %-15s %-14s %s" % ("row", "q", "defect", "L_lift", "sign Delta^(a), a=1,3,..,q-1"))
    for t in table:
        sg = " ".join("%+d" % t["signs"][k] for k in sorted(t["signs"], key=int))
        print("(%2d,%d)    %-4d %-15s %-14s %s" % (t["m"], t["s"], t["q"], t["defect"], t["L"], sg))
    print()
    print("rows with some Delta^(a) < 0 : %d / %d" % (negrows, len(table)))
    bD, bm, bs, ba = best
    print("MIN Delta^(a) over the grid: (m=%d,s=%d), a=%d" % (bm, bs, ba))
    rv = to_rational(bD)
    print("   exact = %s" % (rv if rv is not None else bD.c))
    print("   enclosure ~ %s" % approx_str(bD, 24))
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(dict(table=table, min_row="(m=%d,s=%d)" % (bm, bs), min_a=ba,
                   min_exact=(str(rv) if rv is not None else [str(x) for x in bD.c]),
                   min_approx=approx_str(bD, 24), rows_with_negative=negrows,
                   total=len(table)),
              open(os.path.join(here, "gaugeD.json"), "w"), indent=1)
    print("elapsed %.1fs -> gaugeD.json" % (time.time() - t0))
