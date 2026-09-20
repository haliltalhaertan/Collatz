#!/usr/bin/env python3
"""Scan global target margins M-L and singleton charging margins."""
from fractions import Fraction
from math import comb
import sys
sys.path.insert(0, "/home/mdp/muse-work/cp22-scout")
from gate import per_stratum

def scan_margins(mmax=12):
    rows = []
    for m in range(2, mmax+1):
        for s in range(1, m):
            ps = per_stratum(m, s)
            L = sum(ps["Lk"].values(), Fraction(0,1))
            M = sum(ps["Mj"].values(), Fraction(0,1))
            rows.append((m, s, L, M, M-L))
    return rows

if __name__ == "__main__":
    rows = scan_margins(10)
    # smallest positive defect
    pos = [(m,s,d) for (m,s,L,M,d) in rows if d > 0]
    pos_sorted = sorted(pos, key=lambda e: e[2])
    print("smallest positive defects:")
    for e in pos_sorted[:10]:
        print(f"m={e[0]} s={e[1]} M-L={e[2]}")
    neg = [(m,s,d) for (m,s,L,M,d) in rows if d < 0]
    print("negative defects (target violations):", neg)
    # singleton radius-2 margins: dem vs full supply
    print("=== singleton margins ===")
    for m in range(2, 11):
        for s in range(1, m):
            ps = per_stratum(m, s)
            Lk = ps["Lk"]; Mj = ps["Mj"]
            for k in range(1, m+1):
                dem = max(Lk[k], Fraction(0,1))
                if dem <= 0:
                    continue
                lo = max(k-1,2); hi = min(k+2, m)
                sup = sum(Mj[j] for j in range(lo, hi+1))
                # narrow radius-1 singleton supply [k,k+1]
                lo1 = max(k,2); hi1 = min(k+1, m)
                sup1 = sum(Mj[j] for j in range(lo1, hi1+1))
                if dem > sup1:
                    print(f"SINGLETON-R1-FAIL m={m} s={s} k={k} dem={dem} sup1={sup1} full={sup}")
    print("done singleton check")
    # Lk negativity witness + Mj zero witness details
    ps = per_stratum(4, 3)
    print("m=4 s=3 Lk", {k: str(v) for k,v in ps["Lk"].items()}, "Lsum", sum(ps["Lk"].values(), Fraction(0,1)))
    ps = per_stratum(6, 1)
    print("m=6 s=1 Mj", {k: str(v) for k,v in ps["Mj"].items()})
    print("m=6 s=1 Lk", {k: str(v) for k,v in ps["Lk"].items()})
