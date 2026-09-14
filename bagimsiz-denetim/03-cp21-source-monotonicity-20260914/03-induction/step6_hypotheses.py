"""
Step 6: (a) reproduce the documented radius-1 counterexample at (18,2) [14,14]
        (b) test candidate EXTRA HYPOTHESES that would rescue the induction
        (c) check whether the witnesses' parents are themselves "real-like"
"""
import sys, json
from fractions import Fraction
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import masses, L_terms, M_terms, charging_violations, source, E_op, O_op
from step1_wform import L_from_w, M_from_w
from step3_obstruction import child_from_parent

print("=== (a) DOCUMENTED RADIUS-1 COUNTEREXAMPLE (18,2) interval [14,14] ===")
m, s = 18, 2
L = L_from_w(m, s); M = M_from_w(m, s)
d = max(L[14], Fraction(0))
sup1 = sum(M[j] for j in range(max(14-1, 2), min(14+1, m)+1))
sup2 = sum(M[j] for j in range(max(14-1, 2), min(14+2, m)+1))
print(f"  L_14 = {L[14]}  (documented demand 3/35: {L[14]==Fraction(3,35)})")
print(f"  radius-1 supply = {sup1}  (documented 4033/69615: {sup1==Fraction(4033,69615)})")
print(f"  gap = {d - sup1}  (documented 1934/69615: {d-sup1==Fraction(1934,69615)})")
print(f"  radius-2 supply = {sup2}  -> radius-2 holds here: {d <= sup2}")
r1 = charging_violations(L, M, m, radius=1)
r2 = charging_violations(L, M, m, radius=2)
print(f"  (18,2): radius-1 violations = {len(r1)}, radius-2 violations = {len(r2)}")

print("\n=== (b) CANDIDATE EXTRA HYPOTHESES ===")
# H1: per-stratum max entry cap.  Real source: what is max_k max_u P_k[u]?
print("  H1  per-stratum cap  cap_k(m,s) := max_u P_{m,k,s+1}[u]  on real source:")
caps = {}
for m2 in range(2, 15):
    for s2 in range(1, m2):
        P = source(m2, s2+1)
        caps[(m2,s2)] = [max(P[k]) for k in range(1, m2+1)]
for key in [(4,2),(5,2),(6,2),(8,2),(10,2),(12,2),(6,5),(10,9)]:
    print(f"    ({key[0]},{key[1]}): {caps[key]}")

# Does the per-stratum cap exclude the two witnesses?
W42P = [[0,0,0,0,0,0,0,1],[0,0,1,2,0,0,0,0],[0,0,1,0,0,0,0,2],[0,0,0,0,0,0,0,1]]
W62P = [[0,0,1,0,0,0,0,0],[2,1,1,0,0,0,0,1],[1,2,0,2,1,0,2,2],
        [0,1,2,1,1,3,2,0],[0,2,0,2,0,1,0,0],[0,0,0,0,0,1,0,0]]
print(f"    W(4,2) per-k caps {[max(r) for r in W42P]} vs real {caps[(4,2)]} "
      f"-> excluded by H1: {[max(r) for r in W42P] != caps[(4,2)] and any(max(r)>c for r,c in zip(W42P,caps[(4,2)]))}")
print(f"    W(6,2) per-k caps {[max(r) for r in W62P]} vs real {caps[(6,2)]} "
      f"-> excluded by H1: {any(max(r)>c for r,c in zip(W62P,caps[(6,2)]))}")

# H2: support hypothesis -- real support of P_k mod 2^(s+1)
print("\n  H2  support: supp(P_{m,k,s+1}) on real source vs witnesses")
for (m2,s2,Wp) in [(4,2,W42P),(6,2,W62P)]:
    P = source(m2, s2+1)
    for k in range(1, m2+1):
        rs = {u for u in range(1<<(s2+1)) if P[k][u]}
        ws = {u for u in range(1<<(s2+1)) if Wp[k-1][u]}
        if not ws <= rs:
            print(f"    ({m2},{s2}) k={k}: witness support {sorted(ws)} NOT inside "
                  f"real support {sorted(rs)}  -> excluded by H2")
            break

# H3: "parent demand zero => child demand zero"?  Already refuted (20 levels).
print("\n  H3  'parent demand 0 => child demand 0': REFUTED on 20 real levels (step3 A)")

# H4: monotone total ineq M_total >= L_total, transported?
print("\n  H4  does S_child >= D_child follow from S_parent >= D_parent? check ratios")
bad4 = []
for m2 in range(3, 14):
    for s2 in range(1, m2):
        Dc = sum(v for v in L_from_w(m2,s2).values() if v>0)
        Dp = sum(v for v in L_from_w(m2-1,s2+1).values() if v>0)
        Sc = sum(M_from_w(m2,s2).values())
        Sp = sum(M_from_w(m2-1,s2+1).values())
        # a transport argument needs Sc >= alpha*Sp and Dc <= alpha*Dp for a common alpha
        if Dp == 0 and Dc > 0:
            bad4.append((m2,s2,"no alpha: Dp=0<Dc"))
        elif Dp > 0 and Sp > 0:
            need = Fraction(Dc,Dp); have = Fraction(Sc,Sp)
            if need > have:
                bad4.append((m2,s2,f"Dc/Dp={need} > Sc/Sp={have}"))
print(f"    levels where NO common transfer factor alpha exists: {len(bad4)}")
for x in bad4[:12]:
    print("     ", x)

print("\n=== (c) ARE THE WITNESS PARENTS 'REAL-LIKE'? ===")
W42Q = [[0]*14+[1,0],[0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]]
realQ = source(3, 4)
print("  W(4,2) parent Q per-k caps:", [max(r) for r in W42Q],
      " real (3,3) per-k caps:", [max(realQ[k]) for k in range(1,4)])
print("  -> witness parent already violates the real per-stratum cap at k=2 (2 vs 1):",
      max(W42Q[1]) > max(realQ[2]))
