#!/usr/bin/env python3
"""Cheap kills K1, K2 with exact arithmetic (Fractions only)."""
from fractions import Fraction
import sys
sys.path.insert(0, "/home/mdp/muse-work/cp22-scout")
from gate import transfer_quantities, per_stratum

# K1: identical-lift conjecture F=I always. Witness (4,2): L=8/3 != 0.
tq = transfer_quantities(4, 2)
print("K1 (4,2) I=", tq["I"], "F=", tq["F"], "L=F-I=", tq["L"])
assert tq["I"] == Fraction(40, 3)
assert tq["F"] == Fraction(16, 1)
assert tq["L"] == Fraction(8, 3)
assert tq["L"] != 0
print("K1 KILLED: L_lift=8/3 != 0")

# K2: per-stratum non-negativity L_k>=0. Witness (4,3,k=3): L_3=-8/3.
ps = per_stratum(4, 3)
print("K2 (4,3) Lk=", {k: str(v) for k, v in ps["Lk"].items()})
assert ps["Lk"][3] == Fraction(-8, 3)
assert ps["Lk"][3] < 0
# cross-check: sum Lk == F - I
Lsum = sum(ps["Lk"].values(), Fraction(0, 1))
LI = ps["tq"]["F"] - ps["tq"]["I"]
print("K2 Lsum=", Lsum, "F-I=", LI)
assert Lsum == LI == Fraction(-8, 3)
print("K2 KILLED: L_3=-8/3 < 0")
