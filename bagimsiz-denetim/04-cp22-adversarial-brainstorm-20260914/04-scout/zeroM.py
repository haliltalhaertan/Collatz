#!/usr/bin/env python3
"""Find M_j=0 with positive neighbouring demand; verify kill witnesses exactly."""
from fractions import Fraction
import sys
sys.path.insert(0, "/home/mdp/muse-work/cp22-scout")
from gate import per_stratum

if __name__ == "__main__":
    for m in range(2, 17):
        for s in (1, 2):
            if s >= m:
                continue
            ps = per_stratum(m, s)
            Lk = ps["Lk"]; Mj = ps["Mj"]
            for j in range(2, m+1):
                if Mj[j] == 0:
                    # neighbour demand: k in [j-2, j+1] (those whose window includes j)
                    neigh = [k for k in range(max(1,j-2), min(m,j+1)+1)]
                    dem_neigh = sum(max(Lk[k], Fraction(0,1)) for k in neigh)
                    print(f"m={m} s={s} M_{j}=0 neigh_demand(k in {neigh})={dem_neigh} Lk={ {k: str(Lk[k]) for k in neigh} }")
    print("done")
