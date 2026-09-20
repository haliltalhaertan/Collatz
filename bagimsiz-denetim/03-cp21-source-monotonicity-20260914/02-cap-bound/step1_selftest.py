"""
STEP 1 -- self-test of the engine + reproduction of the cap table.

Checks, all exact integer arithmetic:
  (S1) B_of == B_closed                                        (recursion vs closed form)
  (S2) every B_w is odd
  (S3) h_of(w) is odd, 0<h<2^m, and parity_word(h_of(w),m) == w   (bijection)
  (S4) the odd h in (0,2^m) are exactly {h_of(w)} over all k      (bijection, counting)
  (S5) e_of(w) == H^m(h_of(w))  computed by direct iteration      (affine identity)
  (S6) 1 <= e_w <= 3^k - 1                                        (range lemma)
  (S7) |W_{m,k}| == C(m-1,k-1)
"""
import sys, json
from math import comb
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\cap-proof")
from collatz_cap_core import *

MMAX = 14
checks = 0
fails = []

for m in range(1, MMAX + 1):
    seen_h = set()
    for k in range(1, m + 1):
        L = layer(m, k)
        if len(L) != comb(m - 1, k - 1):
            fails.append(("S7", m, k, len(L), comb(m - 1, k - 1)))
        checks += 1
        for (w, B, h, e) in L:
            if B_closed(w) != B:
                fails.append(("S1", m, k, w))
            if B % 2 != 1:
                fails.append(("S2", m, k, w, B))
            if not (0 < h < (1 << m)) or h % 2 != 1:
                fails.append(("S3a", m, k, w, h))
            if parity_word(h, m) != w:
                fails.append(("S3b", m, k, w, h))
            x = h
            for _ in range(m):
                x = H(x)
            if x != e:
                fails.append(("S5", m, k, w, e, x))
            if not (1 <= e <= 3 ** k - 1):
                fails.append(("S6", m, k, w, e, 3 ** k - 1))
            seen_h.add(h)
            checks += 6
    if seen_h != set(range(1, 1 << m, 2)):
        fails.append(("S4", m))
    checks += 1

print("self-test checks performed:", checks)
print("failures:", len(fails))
for f in fails[:20]:
    print("  FAIL", f)

# ---------------- cap table ----------------
table = {}
print()
print("=== CAP TABLE  cap(m,k,r) = max_z P_{m,k,r}(z) ===")
for m in range(2, MMAX + 1):
    for k in range(1, m + 1):
        row = []
        for r in range(2, 10):
            c = cap(m, k, r)
            table[f"{m},{k},{r}"] = c
            row.append(c)
        print(f"m={m:2d} k={k:2d} n_k={comb(m-1,k-1):5d}  r=2..9: {row}")
    print()

with open(r"C:\Users\MDP\collatz-analysis\cap-proof\cap_table.json", "w") as f:
    json.dump(table, f)
print("cap table entries:", len(table))
