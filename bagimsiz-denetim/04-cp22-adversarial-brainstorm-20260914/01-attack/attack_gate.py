"""Mandatory calibration gate -- from-scratch checks. Run: python3 attack_gate.py"""
import sys
sys.path.insert(0, "/home/mdp/muse-work/cp22-attack")
from fractions import Fraction
from attack_engine import (
    row_of, prefix_hist, L_terms_of, M_terms_of,
    demand_of, supply_radius1, adversary_L_M,
)

FAIL = []


def check(name, got, want):
    ok = (got == want)
    print(("OK   " if ok else "FAIL ") + f"{name}: got {got} want {want}")
    if not ok:
        FAIL.append(name)


def main():
    # (m,s)=(4,2)
    r = row_of(4, 2, method="small")
    check("(4,2) I", r["I"], Fraction(40, 3))
    check("(4,2) F", r["F"], Fraction(16))
    check("(4,2) Out", r["Out"], Fraction(31, 3))
    check("(4,2) L_lift", r["L"], Fraction(8, 3))
    check("(4,2) M_merge", r["M"], Fraction(17, 3))
    check("(4,2) defect", r["defect"], Fraction(3))
    # per-stratum M sum identity
    L4 = L_terms_of(r["hist_hi"], 4, 2)
    M4 = M_terms_of(r["hist_hi"], 4, 2)
    check("(4,2) sumM==M", sum((M4[j] for j in range(2, 5)), Fraction(0)), r["M"])
    check("(4,2) sumL==L", sum(L4.values(), Fraction(0)), r["L"])

    # (m,s)=(3,2)
    r = row_of(3, 2, method="small")
    check("(3,2) I", r["I"], Fraction(12))
    check("(3,2) F", r["F"], Fraction(12))
    check("(3,2) Out", r["Out"], Fraction(8))
    check("(3,2) L_lift", r["L"], Fraction(0))
    check("(3,2) M_merge", r["M"], Fraction(4))
    check("(3,2) defect", r["defect"], Fraction(4))

    # (m,s)=(2,1)
    r = row_of(2, 1, method="small")
    check("(2,1) I", r["I"], Fraction(4))
    check("(2,1) F", r["F"], Fraction(4))
    check("(2,1) Out", r["Out"], Fraction(4))
    check("(2,1) L", r["L"], Fraction(0))
    check("(2,1) M", r["M"], Fraction(0))

    # ADVERSARY 1 (3,2) on Z/8
    P1 = {1: [0, 0, 1, 0, 0, 0, 0, 0],
          2: [1, 0, 0, 0, 0, 0, 0, 1],
          3: [0, 0, 0, 0, 1, 0, 0, 0]}
    L, Mm, I, F, Mall = adversary_L_M(P1, 3, 2)
    check("ADV1 L_lift", L, Fraction(2))
    check("ADV1 M_merge", Mm, Fraction(2, 3))

    # ADVERSARY 2 (5,2) on Z/8
    P2 = {1: [0, 0, 1, 0, 0, 0, 0, 0],
          2: [0, 3, 1, 0, 0, 0, 0, 0],
          3: [0, 3, 0, 0, 2, 0, 1, 0],
          4: [1, 0, 0, 0, 3, 0, 0, 0],
          5: [0, 0, 1, 0, 0, 0, 0, 0]}
    L, Mm, I, F, Mall = adversary_L_M(P2, 5, 2)
    check("ADV2 L_lift", L, Fraction(9))
    check("ADV2 M_merge", Mm, Fraction(101, 15))

    # radius-1 counterexample (18,2) interval [14,14]
    hist18 = prefix_hist(18, 3, method="numpy")
    L18 = L_terms_of(hist18, 18, 2)
    M18 = M_terms_of(hist18, 18, 2)
    dem = demand_of(L18, 14, 14)
    sup = supply_radius1(M18, 18, 14, 14)
    check("(18,2)[14,14] demand", dem, Fraction(3, 35))
    check("(18,2)[14,14] supply", sup, Fraction(4033, 69615))
    check("(18,2)[14,14] gap", dem - sup, Fraction(1934, 69615))
    # numpy vs small consistency on a small row
    h_small = prefix_hist(6, 3, method="small")
    h_np = prefix_hist(6, 3, method="numpy")
    same = all(h_small[k] == h_np[k] for k in range(1, 7))
    print(("OK   " if same else "FAIL ") + f"numpy==small consistency (6,3): {same}")
    if not same:
        FAIL.append("numpy==small")

    print()
    if FAIL:
        print(f"GATE FAILED: {len(FAIL)} mismatches: {FAIL}")
    else:
        print("GATE_OK = True (all reproduced)")
    return not FAIL


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
