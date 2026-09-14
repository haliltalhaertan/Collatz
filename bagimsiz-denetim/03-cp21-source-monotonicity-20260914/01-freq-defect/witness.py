"""MINIMAL REPRODUCTION of the kill + exact witness values + robustness.

Run:  python witness.py
Pure integers / Fraction / Z[zeta_N] power-basis vectors.  No floats.
"""
import sys, os, json
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, sign_of_real, to_rational, approx_str
from source import prefix_hist, J, row, merge_identity, run_gate
from freq import dft, decompose, fmt


def basis_str(el, N):
    """exact closed form in the power basis of Z[zeta_N]."""
    ts = []
    for j, v in enumerate(el.c):
        if v == 0:
            continue
        ts.append("(%s)*z^%d" % (v, j) if j else "(%s)" % v)
    return " + ".join(ts) if ts else "0"


def sqrt2_form(el):
    """For N=8: express in the real subfield basis {1, sqrt2}. z^1+z^7=sqrt2."""
    # real element: c0 + c1 z + c2 z^2 + c3 z^3 with conj symmetry
    # z^2 = i (imaginary) -> must vanish for real; z+z^3... use z^3 = -z^{-1}
    c = el.c
    # real => c2 == 0 and c3 == -c1  (since conj: z->z^-1=-z^3, z^3->-z)
    assert c[2] == 0 and c[3] == -c[1], ("not of expected real shape", c)
    return "%s + (%s)*sqrt(2)" % (c[0], c[1])


def main():
    assert run_gate(verbose=True), "GATE FAILED"
    print()

    print("=" * 78)
    print("WITNESS ROWS (exact, in Z[zeta_N] power basis; N = 2^(s+1))")
    print("=" * 78)
    for (m, s) in [(3, 2), (4, 2), (5, 2), (10, 2), (12, 2), (5, 3), (12, 3), (5, 4), (12, 4)]:
        R = decompose(m, s)
        N = R["N"]
        assert R["id_L"] and R["id_M"] and R["id_D"] and R["parseval_ok"] and R["eo_ok"]
        a = 1
        L, M, D = R["Lpart"][a], R["Mpart"][a], R["Dpart"][a]
        print("\n(m=%d,s=%d) N=%d  L_lift=%s  M_merge=%s  defect=%s" %
              (m, s, N, R["L"], R["M"], R["defect"]))
        print("   sum_a Delta^(a) = %s  == defect : %s" % (R["sum_D"], R["id_D"]))
        print("   a=1:  L^(1) = %s" % basis_str(L, N))
        print("         M^(1) = %s" % basis_str(M, N))
        print("         D^(1) = %s   sign = %+d" % (basis_str(D, N), R["signs"][a]))
        if N == 8:
            print("         closed form: L^(1) = %s ; D^(1) = %s"
                  % (sqrt2_form(L), sqrt2_form(D)))
        print("         numeric enclosure D^(1) ~ %s" % approx_str(D, 20))

    print()
    print("=" * 78)
    print("ROBUSTNESS: does the kill survive changing the MERGE-side convention?")
    print("=" * 78)
    print("Any decomposition M_merge = sum_a M^(a) with M^(a) >= 0 obeys M^(a) <= M_merge.")
    print("So L^(a) > M_merge  ==>  Delta^(a) < 0 for EVERY nonneg. decomposition.")
    print()
    rows = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "grid.json")))
    print("%-10s %-14s %-26s %-26s %s" % ("row", "defect", "L^(1) (enclosure)", "M_merge", "L^(1) > M_merge?"))
    worst = None
    for r in rows:
        f1 = [f for f in r["freqs"] if f["a"] == 1][0]
        print("%-10s %-14s %-26s %-26s %s"
              % ("(%d,%d)" % (r["m"], r["s"]), r["defect"], f1["L"], r["M"], f1["L_gt_Mtotal"]))
    print()
    print("=> the negativity of Delta^(1) is a property of THIS (canonically gauged)")
    print("   decomposition, not of every conceivable nonnegative splitting of M_merge.")


if __name__ == "__main__":
    main()
