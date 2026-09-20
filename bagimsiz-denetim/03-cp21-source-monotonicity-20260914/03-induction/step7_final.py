"""
Step 7: FINAL CONVENTION CONFIRMATION + consolidated verdict data.
The task defines RADIUS-1 as supply window j in [a, b+1] (lower end a, NOT a-1).
core.charging_violations only varied the upper end -> re-do radius-1 properly.
"""
import sys, json
from fractions import Fraction
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import masses, L_terms, M_terms, source
from step1_wform import L_from_w, M_from_w


def viol(L, M, m, lo_off, hi_off):
    """lo_off=-1,hi_off=+2 -> radius-2 (task);  lo_off=0,hi_off=+1 -> radius-1 (task)."""
    bad = []
    for a in range(1, m + 1):
        for b in range(a, m + 1):
            d = sum(x for x in (L[k] for k in range(a, b + 1)) if x > 0)
            lo = max(a + lo_off, 2); hi = min(b + hi_off, m)
            su = sum(M[j] for j in range(lo, hi + 1)) if lo <= hi else Fraction(0)
            if d > su:
                bad.append((a, b, d, su))
    return bad


print("=== RADIUS-1 AS DEFINED IN THE TASK: j in [a, b+1] ===")
m, s = 18, 2
L = L_from_w(m, s); M = M_from_w(m, s)
d = L[14]
sup = sum(M[j] for j in range(max(14, 2), min(15, m) + 1))
print(f"  (18,2) [14,14]: demand L_14 = {d}   radius-1 supply M_14+M_15 = {sup}")
print(f"  gap = {d - sup}   (documented: demand 3/35, supply 4033/69615, gap 1934/69615)")
print(f"  MATCH: demand {d==Fraction(3,35)}, supply {sup==Fraction(4033,69615)}, "
      f"gap {d-sup==Fraction(1934,69615)}")

print("\n=== GRID: radius-1 vs radius-2 on the real source ===")
r1t = r2t = rows = 0
r1rows = []
for mm in range(2, 19):
    for ss in range(1, mm):
        Lx = L_from_w(mm, ss); Mx = M_from_w(mm, ss)
        v1 = viol(Lx, Mx, mm, 0, 1)
        v2 = viol(Lx, Mx, mm, -1, 2)
        rows += 1; r1t += len(v1); r2t += len(v2)
        if v1:
            r1rows.append((mm, ss, len(v1)))
print(f"  rows m=2..18: {rows}")
print(f"  RADIUS-1 violations: {r1t}  (rows with violations: {r1rows})")
print(f"  RADIUS-2 violations: {r2t}")

print("\n=== CONSOLIDATED: the 20 vacuous-parent levels (obstruction A) ===")
vac = []
for mm in range(3, 15):
    for ss in range(1, mm):
        Dc = sum(v for v in L_from_w(mm, ss).values() if v > 0)
        Dp = sum(v for v in L_from_w(mm - 1, ss + 1).values() if v > 0)
        if Dp == 0 and Dc > 0:
            Mx = M_from_w(mm, ss)
            vac.append((mm, ss, str(Dc), str(sum(Mx.values()))))
print(f"  count = {len(vac)}")
for x in vac:
    print("   child (m,s)=(%d,%d): parent demand 0, child demand %s, child supply %s" % x)
json.dump({"vacuous_levels": vac, "r1": r1t, "r2": r2t, "rows": rows},
          open(r"C:\Users\MDP\collatz-analysis\induction\final_report.json", "w"), indent=1)
