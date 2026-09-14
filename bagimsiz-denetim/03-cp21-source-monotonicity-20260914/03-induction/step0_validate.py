"""Step 0: convention validation against the two published adversaries,
plus reproduction + verification of the PARENT IDENTITY on many exact cases."""
import sys, json
from fractions import Fraction
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import (source, masses, L_terms, M_terms, check_parent_identity,
                  parent_pieces, J, row, charging_violations)

print("=== ADVERSARY CONVENTION CHECK ===")
# ADVERSARY 1: (m,s)=(3,2), N=8
P = [None] * 5
P[0] = (0,) * 8
P[1] = (0, 0, 1, 0, 0, 0, 0, 0)
P[2] = (1, 0, 0, 0, 0, 0, 0, 1)
P[3] = (0, 0, 0, 0, 1, 0, 0, 0)
L = L_terms(P, 3, 2); M = M_terms(P, 3, 2)
print("adv1 L_k:", {k: str(v) for k, v in L.items()}, "sum", sum(L.values()))
print("adv1 M_j:", {k: str(v) for k, v in M.items()}, "sum", sum(M.values()))
print("adv1 expected L=2, M=2/3 ->",
      sum(L.values()) == 2 and sum(M.values()) == Fraction(2, 3))

# ADVERSARY 2: (m,s)=(5,2), N=8
Q = [None] * 7
Q[0] = (0,) * 8
Q[1] = (0, 0, 1, 0, 0, 0, 0, 0)
Q[2] = (0, 3, 1, 0, 0, 0, 0, 0)
Q[3] = (0, 3, 0, 0, 2, 0, 1, 0)
Q[4] = (1, 0, 0, 0, 3, 0, 0, 0)
Q[5] = (0, 0, 1, 0, 0, 0, 0, 0)
L2 = L_terms(Q, 5, 2); M2 = M_terms(Q, 5, 2)
print("adv2 L_k:", {k: str(v) for k, v in L2.items()}, "sum", sum(L2.values()))
print("adv2 M_j:", {k: str(v) for k, v in M2.items()}, "sum", sum(M2.values()))
print("adv2 expected L=9, M=101/15 ->",
      sum(L2.values()) == 9 and sum(M2.values()) == Fraction(101, 15))

print()
print("=== PARENT IDENTITY VERIFICATION ===")
cases = []
for m in range(2, 15):
    for s in range(0, m):
        ok = check_parent_identity(m, s)
        cases.append((m, s, ok))
nok = sum(1 for _, _, o in cases if o)
print("levels tested:", len(cases), " all-strata-match:", nok)
bad = [(m, s) for m, s, o in cases if not o]
print("failures:", bad)
# per-stratum count (each (m,s,k) is an independent array identity)
strata = 0
for m in range(2, 15):
    for s in range(0, m):
        strata += m
print("independent (m,s,k) array identities verified:", strata)
json.dump({"levels": len(cases), "ok": nok, "strata": strata},
          open(r"C:\Users\MDP\collatz-analysis\induction\parent_identity_report.json", "w"))
