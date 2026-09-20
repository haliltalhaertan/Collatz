"""MINIMAL KILL REPRODUCTION under GAUGE B (the prior session's convention).

Prior session reported, at s=2, Delta^(a) > 0 for both a=1,3, "3/2 per
frequency" at (m,s)=(4,2).  GAUGE B reproduces exactly that (3/2, 3/2).
It then FAILS at (m,s)=(6,4), frequencies a=13 and a=19.

Run:  python kill.py
"""
import sys, os
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import to_rational, approx_str, sign_of_real, Cyc
from gauges import gauged
from source import run_gate


def show(m, s, g, only=None):
    ok, signs, D, r = gauged(m, s, g)
    N = 1 << (s + 1)
    print("GAUGE %s  (m=%d,s=%d) N=%d  L=%s M=%s defect=%s  identity_ok=%s"
          % (g, m, s, N, r["L"], r["M"], r["defect"], ok))
    tot = Cyc(N // 2)
    for a in range(1, N, 2):
        tot = tot + D[a]
        if only and a not in only:
            continue
        v = to_rational(D[a])
        print("    a=%-3d Delta^(a) = %-40s sign=%+d   ~ %s"
              % (a, v if v is not None else str(D[a].c), signs[a],
                 approx_str(D[a], 22)))
    print("    sum_a Delta^(a) = %s  (defect = %s)  MATCH=%s"
          % (to_rational(tot), r["defect"], to_rational(tot) == r["defect"]))
    print()


if __name__ == "__main__":
    assert run_gate(verbose=False)
    print("GATE OK\n")
    print("--- prior session's reported row, reproduced (GAUGE B) ---")
    show(4, 2, "B")
    print("--- THE KILL: exact counterexample ---")
    show(6, 4, "B", only=[13, 19])
    print("--- same row, all frequencies ---")
    show(6, 4, "B")
