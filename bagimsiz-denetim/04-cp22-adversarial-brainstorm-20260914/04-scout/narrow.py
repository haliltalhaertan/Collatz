#!/usr/bin/env python3
"""Test whether narrowed radius windows suffice; find witnesses where +2 / -1 extension is load-bearing."""
from fractions import Fraction
from math import comb
import sys
sys.path.insert(0, "/home/mdp/muse-work/cp22-scout")
from gate import per_stratum

def demand_supply(m, s, a, b, lo_off, hi_off):
    ps = per_stratum(m, s)
    Lk = ps["Lk"]; Mj = ps["Mj"]
    dem = sum(max(Lk[k], Fraction(0,1)) for k in range(a, b+1))
    lo = max(a+lo_off, 2)  # lo_off=-1 for full, 0 for no lower ext
    hi = min(b+hi_off, m)
    sup = sum(Mj[j] for j in range(lo, hi+1)) if hi >= lo else Fraction(0,1)
    return dem, sup, Lk, Mj

def find_narrow_kills(mmax=22):
    kills_11 = []  # symmetric radius-1.5? [a-1,b+1] fails but [a-1,b+2] holds
    kills_no_lo = []  # [a,b+2] fails but [a-1,b+2] holds (lower ext needed)
    kills_no_hi2 = []  # [a-1,b+1] fails (upper +2 needed)
    for m in range(2, mmax+1):
        for s in range(1, m):
            ps = per_stratum(m, s)
            Lk = ps["Lk"]; Mj = ps["Mj"]
            for a in range(1, m+1):
                for b in range(a, m+1):
                    dem = sum(max(Lk[k], Fraction(0,1)) for k in range(a, b+1))
                    if dem <= 0:
                        continue
                    full = sum(Mj[j] for j in range(max(a-1,2), min(b+2,m)+1))
                    narrow11 = sum(Mj[j] for j in range(max(a-1,2), min(b+1,m)+1))
                    nolo = sum(Mj[j] for j in range(max(a,2), min(b+2,m)+1))
                    if dem > narrow11 and dem <= full:
                        kills_11.append((m, s, a, b, dem, narrow11, full))
                    if dem > nolo and dem <= full:
                        kills_no_lo.append((m, s, a, b, dem, nolo, full))
    return kills_11, kills_no_lo

if __name__ == "__main__":
    k11, knolo = find_narrow_kills(14)
    print("kills_11 (need +2 beyond +1) count:", len(k11))
    for e in k11[:10]:
        print(f"m={e[0]} s={e[1]} [{e[2]},{e[3]}] dem={e[4]} narrow11={e[5]} full={e[6]} gap={(e[4]-e[5])}")
    print("kills_nolo (need -1) count:", len(knolo))
    for e in knolo[:10]:
        print(f"m={e[0]} s={e[1]} [{e[2]},{e[3]}] dem={e[4]} nolo={e[5]} full={e[6]} gap={(e[4]-e[5])}")
