"""Minimum restricted to the MANDATED grid (s=2,3,4; m=4..12), cross-field safe,
plus the smallest few values and the lift-carrier summary."""
import sys, os, json
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, sign_of_real, to_rational, approx_str
from freq import embed
from minmax import parts
from source import run_gate

assert run_gate(verbose=False); print("GATE OK\n")
DB = 32   # Z[zeta_64]
vals = []
for s in (2, 3, 4):
    for m in range(4, 13):
        if s > m - 1:
            continue
        ok, Lp, Mp, D, r = parts(m, s)
        assert ok
        for a in D:
            vals.append((embed(D[a], DB), m, s, a, D[a], sign_of_real(D[a])))
neg = [v for v in vals if v[5] < 0]
print("MANDATED GRID s in {2,3,4}, m in 4..12 (s<=m-1): %d rows, %d (row,freq) pairs"
      % (26, len(vals)))
print("pairs with Delta^(a) < 0 : %d" % len(neg))
# exact selection sort for the 5 smallest
rem = list(vals); small = []
for _ in range(5):
    b = rem[0]
    for v in rem[1:]:
        if sign_of_real(b[0] - v[0]) > 0:
            b = v
    small.append(b); rem.remove(b)
print("\nfive smallest Delta^(a) on the mandated grid (exact, certified order):")
for e, m, s, a, raw, sg in small:
    rv = to_rational(raw)
    print("   (m=%2d,s=%d) a=%-3d  Delta = %s   ~ %s  sign=%+d"
          % (m, s, a, rv if rv is not None else "cyclotomic", approx_str(e, 22), sg))
e, m, s, a, raw, sg = small[0]
print("\nMIN over mandated grid = ~%s   at (m=%d,s=%d), a=%d" % (approx_str(e, 24), m, s, a))
print("   exact power-basis coeffs in Z[zeta_%d]: %s" % (2 * raw.d, [str(x) for x in raw.c]))
json.dump(dict(min_approx=approx_str(e, 24), min_row="(m=%d,s=%d)" % (m, s), min_a=a,
               min_coeffs=[str(x) for x in raw.c], field="Z[zeta_%d]" % (2 * raw.d),
               negatives=len(neg), pairs=len(vals)),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mandated_min.json"), "w"), indent=1)
print("-> mandated_min.json")
