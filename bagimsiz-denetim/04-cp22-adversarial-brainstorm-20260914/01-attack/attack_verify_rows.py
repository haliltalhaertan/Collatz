"""Final cross-checks on saved hot rows (no recompute): full-interval violation scan,
exact min-ratio bounds vs 21/20 and 1051/1000, (24,2) all-nonpositive confirmation.
Run: python3 attack_verify_rows.py
"""
import sys, json
sys.path.insert(0, "/home/mdp/muse-work/cp22-attack")
from fractions import Fraction

D = json.load(open("/home/mdp/muse-work/cp22-attack/attack_hot_results.json"))
n_viol = 0
for row in D["rows"]:
    m, s = row["m"], row["s"]
    L = {int(k): Fraction(v) for k, v in row["Lterms"].items()}
    M = {int(j): Fraction(v) for j, v in row["Mterms"].items()}
    M1 = {1: Fraction(0), m + 1: Fraction(0)}
    M1.update(M)
    bad = 0
    for a in range(1, m + 1):
        for b in range(a, m + 1):
            dem = sum((v for k, v in L.items() if a <= k <= b and v > 0), Fraction(0))
            lo = max(a - 1, 2)
            hi = min(b + 2, m)
            sup = sum((M1[j] for j in range(lo, hi + 1)), Fraction(0)) if lo <= hi else Fraction(0)
            if dem > sup:
                bad += 1
    print(f"(m={m},s={s}) violating intervals (ALL [a,b]): {bad}")
    n_viol += bad
    if m == 24 and s == 2:
        npos = sum(1 for v in L.values() if v > 0)
        print(f"  (24,2) #positive L_k = {npos}; L = {sorted([(k, str(v)) for k, v in L.items() if v != 0])[:6]}...")
print(f"TOTAL real-row violations: {n_viol}")

g = D["global_min"]
r = Fraction(g["ratio"])
print(f"global min ratio = {r} at (m={g['m']},s={g['s']})[{g['a']},{g['b']}]")
print(f"  vs 21/20: diff = {r - Fraction(21, 20)}  (sign>0: {(r - Fraction(21,20)) > 0})")
print(f"  vs 1051/1000: diff = {Fraction(1051,1000) - r}  (sign>0: {(Fraction(1051,1000)-r) > 0})")
print(f"  cross: 20*num={20*r.numerator} vs 21*den={21*r.denominator}")
