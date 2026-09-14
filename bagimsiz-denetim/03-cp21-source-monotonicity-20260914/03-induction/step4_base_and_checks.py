"""
Step 4: (i) independent re-verification of the witnesses,
        (ii) are the published adversaries themselves in the image of the transfer?
        (iii) the DIAGONAL BASE CASE: what does it actually require?
        (iv) directionality of the transfer on each side (contract / inflate).
"""
import sys, json
from fractions import Fraction
from math import comb
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import (masses, L_terms, M_terms, E_op, O_op, charging_violations,
                  source, J)
from step1_wform import L_from_w, M_from_w
from step3_obstruction import child_from_parent


# ---------------------------------------------------------- (i) re-verification
def recheck(Q, m, s):
    mp = m - 1
    Lp = L_terms(Q, mp, s + 1); Mp = M_terms(Q, mp, s + 1)
    P = child_from_parent(Q, m, s)
    Lc = L_terms(P, m, s); Mc = M_terms(P, m, s)
    return (Lp, Mp, charging_violations(Lp, Mp, mp),
            P, Lc, Mc, charging_violations(Lc, Mc, m))


def pad(rows, L):
    return [list(r) + [0] * (L - len(r)) for r in rows]


W42 = [[0]*14+[1,0],
       [0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]]
W62 = [[0,1]+[0]*14,
       [2,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0],
       [0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0],
       [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]]

print("=== (i) INDEPENDENT RE-VERIFICATION OF WITNESSES ===")
for tag, Qrows, m, s in [("W(4,2)", W42, 4, 2), ("W(6,2)", W62, 6, 2)]:
    Np = 1 << (s + 2)
    Q = [[0]*Np] + pad(Qrows, Np) + [[0]*Np, [0]*Np]
    Lp, Mp, pv, P, Lc, Mc, cv = recheck(Q, m, s)
    mp = m - 1
    print(f"\n{tag}: parent (m,s)=({mp},{s+1}), child ({m},{s})")
    print("  parent masses ok:", [sum(Q[k]) for k in range(1, mp+1)],
          "expected", [comb(mp-1, k-1) for k in range(1, mp+1)])
    print("  child  masses ok:", [sum(P[k]) for k in range(1, m+1)],
          "expected", [comb(m-1, k-1) for k in range(1, m+1)])
    print("  parent L:", {k: str(v) for k, v in sorted(Lp.items())})
    print("  parent M:", {k: str(v) for k, v in sorted(Mp.items())})
    print("  parent radius-2 violations:", pv, "  -> IH HOLDS" if not pv else "")
    print("  child  L:", {k: str(v) for k, v in sorted(Lc.items())})
    print("  child  M:", {k: str(v) for k, v in sorted(Mc.items())})
    print("  child radius-2 violations (a,b,demand,supply):",
          [(a, b, str(d), str(su)) for a, b, d, su in cv])
    print("  child max entry:", max(max(r) for r in P[1:m+1]))

# ------------------------------- (ii) are the adversaries in the transfer image?
print("\n=== (ii) ARE ADV1 / ADV2 IMAGES OF THE TRANSFER? ===")
def adv1():
    return [ (0,)*8, (0,0,1,0,0,0,0,0), (1,0,0,0,0,0,0,1), (0,0,0,0,1,0,0,0) ]
# child (3,2): parent (2,3), masses n'_1=n'_2=1 -> two point masses on Z/16
m, s = 3, 2; Np = 16
target = adv1()
found = []
for p in range(Np):
    for r in range(Np):
        Q = [[0]*Np for _ in range(5)]
        Q[1][p] = 1; Q[2][r] = 1
        P = child_from_parent(Q, m, s)
        if [list(P[k]) for k in range(1, 4)] == [list(target[k]) for k in range(1, 4)]:
            found.append((p, r))
print("  ADV1 preimages under the transfer:", found,
      "-> ADV1 is NOT in the image" if not found else "")

# --------------------------------------------- (iii) DIAGONAL BASE CASE analysis
print("\n=== (iii) DIAGONAL BASE CASE s = m-1 ===")
print(" m | maxentry | #k with L_k>0 | totalDemand | totalSupply | worst (demand-supply) over intervals")
base_rows = []
for m in range(2, 13):
    s = m - 1
    P = source(m, s + 1)
    L = L_from_w(m, s); M = M_from_w(m, s)
    mx = max(max(P[k]) for k in range(1, m + 1))
    pos = [k for k in range(1, m + 1) if L[k] > 0]
    D = sum(v for v in L.values() if v > 0)
    S = sum(M.values())
    v = charging_violations(L, M, m)
    worst = None
    for a in range(1, m + 1):
        for b in range(a, m + 1):
            d = sum(x for x in (L[k] for k in range(a, b+1)) if x > 0)
            lo, hi = max(a-1, 2), min(b+2, m)
            su = sum(M[j] for j in range(lo, hi+1)) if lo <= hi else Fraction(0)
            g = d - su
            if worst is None or g > worst[0]:
                worst = (g, a, b)
    base_rows.append(dict(m=m, mx=mx, pos=pos, D=str(D), S=str(S),
                          worst=str(worst[0]), ab=(worst[1], worst[2]), viol=len(v)))
    print(f"{m:2d} | {mx:8d} | {len(pos):13d} | {str(D):>11} | {str(S):>16} | "
          f"{str(worst[0]):>14} at [{worst[1]},{worst[2]}]  viol={len(v)}")

# ------------------------------------------ (iv) directionality of the transfer
print("\n=== (iv) TRANSFER DIRECTIONALITY ON REAL SOURCE ===")
inf_d = 0; tot_d = 0; contract_s = 0; tot_s = 0
worst_d = None; worst_s = None
for m in range(3, 13):
    for s in range(1, m):
        Lc = L_from_w(m, s); Lp = L_from_w(m-1, s+1)
        Mc = M_from_w(m, s); Mp = M_from_w(m-1, s+1)
        Dc = sum(v for v in Lc.values() if v > 0); Dp = sum(v for v in Lp.values() if v > 0)
        Sc = sum(Mc.values()); Sp = sum(Mp.values())
        tot_d += 1; tot_s += 1
        if Dc > Dp: inf_d += 1
        if Sc < Sp: contract_s += 1
        if Dp > 0:
            rd = Fraction(Dc, Dp)
            if worst_d is None or rd > worst_d[0]: worst_d = (rd, m, s)
        if Sp > 0:
            rs = Fraction(Sc, Sp)
            if worst_s is None or rs < worst_s[0]: worst_s = (rs, m, s)
print(f"  demand INFLATES (D_child > D_parent) on {inf_d}/{tot_d} levels; "
      f"max finite ratio {worst_d[0]} at (m,s)={worst_d[1:]}")
print(f"  supply CONTRACTS (S_child < S_parent) on {contract_s}/{tot_s} levels; "
      f"min ratio {worst_s[0]} at (m,s)={worst_s[1:]}")

json.dump(base_rows, open(r"C:\Users\MDP\collatz-analysis\induction\diagonal_base.json", "w"), indent=1)
