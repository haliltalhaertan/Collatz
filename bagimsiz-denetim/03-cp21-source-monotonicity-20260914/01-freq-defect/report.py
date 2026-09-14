"""Final report: exact minima, carrier frequency, full sign table."""
import sys, os, json, time
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, to_rational, approx_str, sign_of_real
from gauges import gauged
from source import run_gate


def lt(x, y):
    """exact: is real cyclotomic x < y ?"""
    return sign_of_real(y - x) > 0


def main():
    assert run_gate(verbose=False)
    pairs = [(m, s) for s in (2, 3, 4) for m in range(4, 13) if s <= m - 1]
    t0 = time.time()
    out = {}
    for g in ("A", "B"):
        best = None
        table = []
        for (m, s) in pairs:
            ok, signs, D, r = gauged(m, s, g)
            assert ok, ("identity failed", g, m, s)
            N = 1 << (s + 1)
            # conjugate classes: a and N-a give equal Delta
            reps = [a for a in range(1, N // 2 + 1, 2)]
            neg = [a for a in range(1, N, 2) if signs[a] < 0]
            pos_carrier = [a for a in reps if signs[a] > 0]
            table.append(dict(m=m, s=s, N=N, defect=str(r["defect"]),
                              L=str(r["L"]), M=str(r["M"]),
                              signs={a: signs[a] for a in reps},
                              negative_a=neg,
                              identity_ok=ok))
            for a in range(1, N, 2):
                if best is None or lt(D[a], best[0]):
                    best = (D[a], m, s, a, N)
        bD, bm, bs, ba, bN = best
        out[g] = dict(table=table,
                      min_delta_basis=[str(x) for x in bD.c],
                      min_delta_approx=approx_str(bD, 24),
                      min_row="(m=%d,s=%d)" % (bm, bs), min_a=ba, min_N=bN,
                      rows_with_negative=sum(1 for t in table if t["negative_a"]),
                      total_rows=len(table))
        print("=" * 76)
        print("GAUGE %s  grid s in {2,3,4}, m in 4..12 (s<=m-1) -> %d rows" % (g, len(table)))
        print("=" * 76)
        print("%-9s %-4s %-14s %-13s %s" % ("row", "N", "defect", "L_lift", "sign of Delta^(a), a=1,3,..,N/2 (conj. reps)"))
        for t in table:
            reps = sorted(t["signs"])
            sg = " ".join("%+d" % t["signs"][a] for a in reps)
            print("(%2d,%d)    %-4d %-14s %-13s %s" % (t["m"], t["s"], t["N"], t["defect"], t["L"], sg))
        print("rows with some Delta^(a) < 0: %d/%d" % (out[g]["rows_with_negative"], len(table)))
        print("MIN Delta^(a) at (m=%d,s=%d), a=%d, N=%d" % (bm, bs, ba, bN))
        print("   exact (power basis of Z[zeta_%d]): %s" % (bN, bD.c))
        print("   enclosure: ~%s" % out[g]["min_delta_approx"])
        print()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "report.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("elapsed %.1fs -> report.json" % (time.time() - t0))


if __name__ == "__main__":
    main()
