"""FINAL: the forced common index and the gauge variants on it.

WHY THE INDEX IS FORCED.
  The lift law indexes by xi odd mod N = 2^(s+1).
  The merge side is J_s of an array on Z/q, q = 2^s.  Its Fourier frequencies
  are odd residues mod q; equivalently Ehat_k(xi) and Ohat_k(xi) are INVARIANT
  under xi -> xi+q.  So the merge side literally cannot distinguish the two
  lifts xi, xi+q of an odd a mod q -- any per-lift split of M is an arbitrary
  choice, not a canonical decomposition.
  The lift side, by contrast, ANTI-symmetric: cos(2 pi c_k (xi+q)/N)
  = -cos(2 pi c_k xi/N).
  Hence the unique common index on which BOTH sides are well defined is
        a  odd  mod q = 2^s,
  with the lift contributions of xi and xi+q summed.  On that index the lift
  part becomes RATIONAL (the cos's combine into differences of squares), which
  is a strong canonicity signal and is verified below.

VARIANTS TESTED on that forced index (all exact, all identity-checked):
   D : a = xi        mod q        (raw input frequency)
   E : a = 3^k xi    mod q        (the Round-7 gauge, reduced mod q)
   F : a = 3^(k-1)xi mod q        (merge-parent gauge)
"""
import sys, os, json, time
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, sign_of_real, to_rational, approx_str
from source import row, run_gate
from freq import dft


def decompose_q(m, s, variant):
    N = 1 << (s + 1)
    q = 1 << s
    d = N // 2
    r = row(m, s)
    hist = r["hist_hi"]
    inv3 = pow(3, -1, N)
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

    def base(a, k):
        """the mod-N lift pair whose mod-q class maps to label a, for stratum k"""
        if variant == "D":
            b = a
        elif variant == "E":
            b = (pow(inv3, k, N) * a) % N
        elif variant == "F":
            b = (pow(inv3, k - 1, N) * a) % N
        else:
            raise ValueError(variant)
        b %= q
        if b % 2 == 0:
            b += q
        return [b, b + q] if b < q else [b - q, b]

    odd_q = list(range(1, q, 2))
    Lp, Mp, D = {}, {}, {}
    for a in odd_q:
        L = Cyc(d)
        M = Cyc(d)
        for k in range(1, m + 1):
            nk = comb(m - 1, k - 1)
            for xi in base(a, k):
                ckx = (pow(3, k, N) * xi) % N
                cosv = (Cyc.zpow(d, ckx) + Cyc.zpow(d, -ckx)).scale(Fraction(1, 2))
                L = L + (cosv * norm2(Ph[k][xi])).scale(Fraction(1, nk))
        for k in range(2, m + 1):
            nk = comb(m - 1, k - 1)
            nkm = comb(m - 1, k - 2)
            for xi in base(a, k):
                Dv = Eh[k][xi].scale(nkm) - Oh[k - 1][xi].scale(nk)
                M = M + norm2(Dv).scale(Fraction(1, 2 * nk * nkm * (nk + nkm)))
        Lp[a], Mp[a], D[a] = L, M, M - L
    sL, sM = Cyc(d), Cyc(d)
    for a in odd_q:
        sL = sL + Lp[a]
        sM = sM + Mp[a]
    rL, rM = to_rational(sL), to_rational(sM)
    ok = (rL is not None and rM is not None and rL == r["L"] and rM == r["M"]
          and rM - rL == r["defect"])
    rat = all(to_rational(D[a]) is not None for a in odd_q)
    signs = {a: sign_of_real(D[a]) for a in odd_q}
    return ok, signs, D, r, rat


if __name__ == "__main__":
    assert run_gate(verbose=False)
    print("GATE OK\n")
    pairs = ([(m, s) for s in (2, 3, 4) for m in range(4, 13) if s <= m - 1]
             + [(m, 5) for m in range(6, 15)] + [(m, 2) for m in (13, 14)]
             + [(m, 3) for m in (13, 14)] + [(m, 4) for m in (13, 14)])
    here = os.path.dirname(os.path.abspath(__file__))
    allout = {}
    for v in ("D", "E", "F"):
        t0 = time.time()
        table = []
        negrows = 0
        allrat = True
        gmin = None
        for (m, s) in pairs:
            ok, signs, D, r, rat = decompose_q(m, s, v)
            assert ok, ("IDENTITY FAILED", v, m, s)
            allrat &= rat
            neg = [a for a in signs if signs[a] < 0]
            if neg:
                negrows += 1
            ds = {a: to_rational(D[a]) for a in D}
            for a in ds:
                if ds[a] is not None and (gmin is None or ds[a] < gmin[0]):
                    gmin = (ds[a], m, s, a)
            table.append(dict(m=m, s=s, q=1 << s, defect=str(r["defect"]),
                              L=str(r["L"]), M=str(r["M"]),
                              deltas={str(a): str(ds[a]) for a in sorted(ds)},
                              signs={str(a): signs[a] for a in sorted(signs)},
                              negative_a=neg))
        allout[v] = dict(table=table, rows=len(table), rows_with_negative=negrows,
                         all_rational=allrat,
                         min_delta=str(gmin[0]), min_row="(m=%d,s=%d)" % (gmin[1], gmin[2]),
                         min_a=gmin[3], secs=round(time.time() - t0, 2))
        print("VARIANT %s: %d rows, identity OK on all, all Delta rational=%s, "
              "rows with a negative Delta^(a)=%d, min=%s at (m=%d,s=%d) a=%d  [%.1fs]"
              % (v, len(table), allrat, negrows, gmin[0], gmin[1], gmin[2], gmin[3],
                 allout[v]["secs"]))
    json.dump(allout, open(os.path.join(here, "final.json"), "w"), indent=1)
    print()
    T = allout["E"]["table"]
    print("FULL SIGN TABLE, variant E (Round-7 gauge on the forced mod-q index)")
    print("%-9s %-4s %-16s %-15s %s" % ("row", "q", "defect", "L_lift", "Delta^(a) for a=1,3,..,q-1 (exact rationals)"))
    for t in sorted(T, key=lambda x: (x["s"], x["m"])):
        ds = " | ".join(t["deltas"][k] for k in sorted(t["deltas"], key=int))
        print("(%2d,%d)    %-4d %-16s %-15s %s" % (t["m"], t["s"], t["q"], t["defect"], t["L"], ds))
    print()
    print("-> final.json")
