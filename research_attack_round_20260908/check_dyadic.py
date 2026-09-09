"""Persist the previously fixed m1..6,t1..4 direct dyadic-identity check."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json

def H(x):
    return (3*x+1)//2 if x&1 else x//2

def polynomial(m,t,a):
    counts=Counter()
    for h in range(1,2**m,2):
        x=h+2**m*a;k=0
        for _ in range(m+t):
            k+=x&1;x=H(x)
        counts[k]+=1
    return counts

def main():
    pair_checks=variance_checks=0
    for m in range(1,7):
        for t in range(1,5):
            q=2**t
            rows=[polynomial(m,t,a) for a in range(q)]
            prev=[polynomial(m,t-1,a) for a in range(q//2)]
            for a in range(q//2):
                for r in range(m+t+1):
                    assert rows[a][r]+rows[a+q//2][r]==prev[a][r]+prev[a][r-1]
                    pair_checks+=1
            for r in range(m+t+1):
                B=Fraction(sum(row[r] for row in rows),q)
                V=sum((row[r]-B)**2 for row in rows)/q
                M=[Fraction(rows[a][r]+rows[a+q//2][r],2)-B for a in range(q//2)]
                D=[Fraction(rows[a][r]-rows[a+q//2][r],2) for a in range(q//2)]
                assert V==sum(x*x+y*y for x,y in zip(M,D))/(q//2)
                variance_checks+=1
    assert pair_checks==699
    out=dict(status='PASS',design='Previously fixed grid, persisted without expansion',
             m_min=1,m_max=6,t_min=1,t_max=4,
             coefficient_pair_checks=pair_checks,exact_variance_checks=variance_checks)
    Path(__file__).with_name('DYADIC_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
