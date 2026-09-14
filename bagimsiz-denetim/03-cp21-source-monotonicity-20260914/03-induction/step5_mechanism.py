"""
Step 5: mechanism + adversary consistency + real-source cap/support facts.

(1) Which part of the decomposition L_k = LE_k + LO_k + LX_k creates demand
    out of nothing?  (levels where parent demand = 0 but child demand > 0)
(2) Real-source max-entry caps, compared with the witness arrays.
(3) Is ADV2 in the image of the transfer?
(4) Re-verify radius-2 charging with 0 violations on the real source grid
    (my own independent reproduction of the 221-row claim).
"""
import sys, json
from fractions import Fraction
from math import comb
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import masses, L_terms, M_terms, charging_violations, source, E_op, O_op
from step1_wform import L_from_w, M_from_w
from step2_induction import decompose_L
from step3_obstruction import child_from_parent

print("=== (1) WHERE DOES THE NEW DEMAND COME FROM? ===")
print("levels with parentDemand=0, childDemand>0; per positive k: LE / LO / LX")
lvls = [(4,2),(5,3),(5,4),(7,3),(7,5),(7,6),(8,3),(8,6),(10,2),(10,3),
        (10,6),(10,8),(10,9),(11,4),(12,4),(12,5)]
cross_dominant = 0; tot = 0
for (m, s) in lvls:
    dec = decompose_L(m, s)
    L = L_from_w(m, s)
    pos = [k for k in range(1, m+1) if L[k] > 0]
    for k in pos:
        d = dec[k]; tot += 1
        tag = ""
        if d["LX"] > 0 and d["LE"] + d["LO"] <= 0:
            tag = "  <-- ENTIRELY from the cross term"; cross_dominant += 1
        elif d["LX"] > 0 and d["LX"] >= d["LE"] + d["LO"]:
            tag = "  <-- cross term dominant"; cross_dominant += 1
        print(f"  (m,s)=({m},{s}) k={k}: L={str(d['L']):>10}  LE={str(d['LE']):>10} "
              f"LO={str(d['LO']):>10} LX={str(d['LX']):>10}{tag}")
print(f"  positive strata where cross term is the driver: {cross_dominant}/{tot}")

print("\n=== (2) REAL-SOURCE MAX ENTRY vs WITNESS MAX ENTRY ===")
for (m, s) in [(4,2),(6,2)]:
    P = source(m, s+1)
    mx = max(max(P[k]) for k in range(1, m+1))
    print(f"  real source ({m},{s}): max entry over strata = {mx}; "
          f"per-k = {[max(P[k]) for k in range(1,m+1)]}")
# witnesses
W42P = [[0,0,0,0,0,0,0,1],[0,0,1,2,0,0,0,0],[0,0,1,0,0,0,0,2],[0,0,0,0,0,0,0,1]]
W62P = [[0,0,1,0,0,0,0,0],[2,1,1,0,0,0,0,1],[1,2,0,2,1,0,2,2],
        [0,1,2,1,1,3,2,0],[0,2,0,2,0,1,0,0],[0,0,0,0,0,1,0,0]]
print(f"  witness W(4,2) child max entry = {max(max(r) for r in W42P)} "
      f"(per-k {[max(r) for r in W42P]})")
print(f"  witness W(6,2) child max entry = {max(max(r) for r in W62P)} "
      f"(per-k {[max(r) for r in W62P]})")
# also parent max entries vs real parent
for (m, s) in [(4,2),(6,2)]:
    Q = source(m-1, s+2)
    print(f"  real parent ({m-1},{s+1}): per-k max = {[max(Q[k]) for k in range(1,m)]}")

print("\n=== (3) IS ADV2 IN THE IMAGE OF THE TRANSFER? ===")
# child (5,2): parent (4,3), masses 1,3,3,1 on Z/16 -> too big to brute force fully.
# Instead: the transfer image is characterised by a linear constraint.  Check a
# necessary condition: every child P_k must equal E'(Q_k)+O'(Q_{k-1}); in
# particular P_1 = E'(Q_1) since Q_0 = 0, and E'(x)[z] = Q_1[2z]+Q_1[2z-3].
# Solve the small linear system for k=1 only (mass 1 -> point mass).
adv2 = {1:(0,0,1,0,0,0,0,0), 2:(0,3,1,0,0,0,0,0), 3:(0,3,0,0,2,0,1,0),
        4:(1,0,0,0,3,0,0,0), 5:(0,0,1,0,0,0,0,0)}
Np = 16
k1_pre = []
for p in range(Np):
    Q1 = [0]*Np; Q1[p] = 1
    if tuple(E_op(Q1, 2+1, pow(3,1))) == adv2[1]:
        k1_pre.append(p)
print("  candidate parent point masses giving ADV2's P_1:", k1_pre)
ok_any = False
if k1_pre:
    # for each, see whether ADV2's P_5 (mass 1) is reachable: P_5 = E'(Q_5)+O'(Q_4),
    # but parent has strata 1..4 only, so Q_5 = 0 -> P_5 = O'(Q_4), mass(Q_4)=1.
    hits = []
    for p in range(Np):
        Q4 = [0]*Np; Q4[p] = 1
        if tuple(O_op(Q4, 3, pow(3,4))) == adv2[5]:
            hits.append(p)
    print("  parent point masses Q_4 giving ADV2's P_5:", hits)
    ok_any = bool(hits)
print("  -> ADV2 consistency:", "no obstruction found at k=1,5 level" if ok_any
      else "ADV2 already fails a necessary transfer-image condition")

print("\n=== (4) RADIUS-2 ON THE REAL SOURCE (independent reproduction) ===")
rows = 0; viol = 0; binding = 0; empty = 0
for m in range(2, 15):
    for s in range(1, m):
        L = L_from_w(m, s); M = M_from_w(m, s)
        v = charging_violations(L, M, m)
        rows += 1; viol += len(v)
        for a in range(1, m+1):
            for b in range(a, m+1):
                d = sum(x for x in (L[k] for k in range(a, b+1)) if x > 0)
                if d == 0: empty += 1
                else: binding += 1
print(f"  rows (m=2..14, s=1..m-1): {rows};  radius-2 violations: {viol}")
print(f"  intervals: binding {binding}, vacuous {empty}")
# radius-1 counterexample reproduction
r1v = 0
for m in range(2, 15):
    for s in range(1, m):
        L = L_from_w(m, s); M = M_from_w(m, s)
        r1v += len(charging_violations(L, M, m, radius=1))
print(f"  radius-1 violations on the same grid: {r1v}  (confirms width 2 is needed)")
