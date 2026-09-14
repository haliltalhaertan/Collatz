"""
STEP 3 -- exact-collision multiplicity M(m,k) = max_e #{w in W_{m,k} : e_w = e},
and the bounds.

BOUND B1  (stabilisation):  if 2^r >= 3^k - 1  then cap(m,k,r) = M(m,k).
BOUND B2  (closeness):      M(m,k) <= ceil(2^{m-k+1}/3).
BOUND B3  (window):         cap(m,k,r) <= min( n_k,
                               (2*floor((3^k-2)/2^r)+1) * ceil(2^{m-k+2}/6) ).
"""
import sys, json
from math import comb
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\cap-proof")
from collatz_cap_core import *

MMAX = 20
Mtab = {}
print("=== M(m,k) = max exact-e multiplicity, and bound B2 = ceil(2^(m-k+1)/3) ===")
for m in range(2, MMAX + 1):
    row = []
    for k in range(1, m + 1):
        cnts = {}
        for (w, B, h, e) in layer(m, k):
            cnts[e] = cnts.get(e, 0) + 1
        M = max(cnts.values())
        Mtab[f"{m},{k}"] = M
        b2 = -((-(1 << (m - k + 1))) // 3)      # ceil
        row.append((k, M, min(b2, comb(m - 1, k - 1))))
    print(f"m={m:2d}: " + "  ".join(f"k{k}:M={M},B2={b}" for k, M, b in row))

# ---- B2 verification + tightness
viol2 = []
tight2 = []
for key, M in Mtab.items():
    m, k = map(int, key.split(","))
    b2 = min(-((-(1 << (m - k + 1))) // 3), comb(m - 1, k - 1))
    if M > b2:
        viol2.append((m, k, M, b2))
    tight2.append((b2 / M, m, k, M, b2))
print()
print("B2 cases checked:", len(Mtab), " violations:", len(viol2))
tight2.sort()
print("B2 tightness (bound/actual): best", tight2[0][:1], tight2[0][1:],
      " worst", tight2[-1][:1], tight2[-1][1:])
worst = max(tight2)[0]
best = min(tight2)[0]
print(f"B2 ratio range: {best:.3f} .. {worst:.1f}")
# ratio restricted to m-k <= 8 (the regime where B2 is not swamped)
sub = [t for t in tight2 if t[1] - t[2] <= 8]
print("B2 ratio for m-k<=8: min %.3f max %.3f  (n=%d)" % (min(s[0] for s in sub), max(s[0] for s in sub), len(sub)))

# ---- B1 verification: cap(m,k,r) == M(m,k) once 2^r >= 3^k - 1
b1_checked = 0
b1_fail = 0
for m in range(2, 15):
    for k in range(1, m + 1):
        rmin = (3 ** k - 1).bit_length()          # smallest r with 2^r >= 3^k-1
        for r in range(rmin, rmin + 3):
            c = cap(m, k, r)
            b1_checked += 1
            if c != Mtab[f"{m},{k}"]:
                b1_fail += 1
print()
print("B1 (stabilisation) cases:", b1_checked, "failures:", b1_fail)

# ---- B3 verification + tightness
captab = json.load(open(r"C:\Users\MDP\collatz-analysis\cap-proof\cap_table.json"))
rows = []
viol3 = 0
for key, c in captab.items():
    m, k, r = map(int, key.split(","))
    nk = comb(m - 1, k - 1)
    ns = 2 * ((3 ** k - 2) // (1 << r)) + 1
    win = -((-(1 << (m - k + 2))) // 6)           # ceil(2^{m-k+2}/6)
    b3 = min(nk, ns * win)
    if c > b3:
        viol3 += 1
        print("  B3 VIOLATION", m, k, r, c, b3)
    rows.append((m, k, r, c, nk, b3, b3 / c if c else None, b3 < nk))
print("B3 cases:", len(rows), "violations:", viol3)
nontriv = [x for x in rows if x[5] < x[4]]
print("B3 strictly beats the trivial bound n_k in", len(nontriv), "of", len(rows), "cells")
if nontriv:
    rr = sorted(nontriv, key=lambda x: x[6])
    print("  best ratio bound/actual: %.2f at (m,k,r)=%s" % (rr[0][6], rr[0][:3]))
    print("  worst ratio bound/actual: %.2f at (m,k,r)=%s" % (rr[-1][6], rr[-1][:3]))
    import statistics
    print("  median ratio: %.2f" % statistics.median(x[6] for x in nontriv))

json.dump(Mtab, open(r"C:\Users\MDP\collatz-analysis\cap-proof\M_table.json", "w"))
print()
print("=== growth check: is M(m,k) ~ c * 2^{m-k}? ===")
for d in range(1, 11):
    vals = [(m, Mtab.get(f"{m},{m-d}")) for m in range(d + 2, MMAX + 1)]
    vals = [(m, v) for m, v in vals if v]
    print(f"  m-k={d:2d}: 2^(m-k)/3={2**d/3:8.2f}  M values over m: {[v for _, v in vals]}")
