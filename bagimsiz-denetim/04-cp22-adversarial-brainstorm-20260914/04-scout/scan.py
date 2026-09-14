#!/usr/bin/env python3
"""Scan for cheap-kill witnesses with exact arithmetic."""
from fractions import Fraction
from math import comb
import sys
sys.path.insert(0, "/home/mdp/muse-work/cp22-scout")
from gate import histograms, J_r, per_stratum, transfer_quantities

def scan_signs(mmax=12):
    negs_Lk = []
    zero_Mj = []
    neg_Llift = []
    pos_Llift = []
    for m in range(2, mmax+1):
        for s in range(1, m):
            ps = per_stratum(m, s)
            Lk = ps["Lk"]; Mj = ps["Mj"]
            L = sum(Lk.values(), Fraction(0,1))
            M = sum(Mj.values(), Fraction(0,1))
            if L < 0:
                neg_Llift.append((m, s, L))
            if L > 0:
                pos_Llift.append((m, s, L))
            for k, v in Lk.items():
                if v < 0:
                    negs_Lk.append((m, s, k, v))
            for j in range(2, m+1):
                if Mj[j] == 0:
                    zero_Mj.append((m, s, j))
    return negs_Lk, zero_Mj, neg_Llift, pos_Llift

if __name__ == "__main__":
    negs_Lk, zero_Mj, neg_Llift, pos_Llift = scan_signs(10)
    print("NEG Lk examples (first 10):")
    for e in negs_Lk[:10]:
        print(e[0], e[1], e[2], str(e[3]))
    print("count neg Lk:", len(negs_Lk))
    print("ZERO Mj interior examples (first 10):")
    for e in zero_Mj[:10]:
        print(e)
    print("count zero Mj:", len(zero_Mj))
    print("NEG L_lift examples (first 10):")
    for e in neg_Llift[:10]:
        print(e[0], e[1], str(e[2]))
    print("count neg L:", len(neg_Llift))
    print("POS L examples (first 10):")
    for e in pos_Llift[:10]:
        print(e[0], e[1], str(e[2]))
    # Check specific candidate kills
    print("=== specific ===")
    ps = per_stratum(6, 2)
    print("m=6 s=2 Lk", {k: str(v) for k,v in ps["Lk"].items()})
    print("m=6 s=2 Mj", {k: str(v) for k,v in ps["Mj"].items()})
    ps = per_stratum(7, 6)
    print("m=7 s=6 Lk", {k: str(v) for k,v in ps["Lk"].items()})
    ps = per_stratum(10, 9)
    print("m=10 s=9 Lk", {k: str(v) for k,v in ps["Lk"].items()})
    print("m=10 s=9 Lsum", sum(ps["Lk"].values(), Fraction(0,1)))
