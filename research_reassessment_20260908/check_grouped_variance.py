"""Bounded structural diagnostic; exact integers, no stochastic assumptions."""
from collections import Counter
from math import comb, floor, ceil, log2
from fractions import Fraction
from pathlib import Path
import json

def H(x):
    return (3*x+1)//2 if x & 1 else x//2

def panel(r):
    A=floor(log2(3)*r); m=ceil(1.2*r); t=A-m; q=2**t
    P=Counter()
    for h in range(1,2**m,2):
        x=h; k=0
        for _ in range(m):
            k+=x&1; x=H(x)
        P[k,x%q]+=1
    G=[0]*q; signatures=[]; individual=0; grouped=0
    for (k,z),w in P.items():
        j=r-k
        if not 0<=j<=t: continue
        v=[]
        for a in range(q):
            x=(pow(3,k,q)*a+z)%q; count=0
            for _ in range(t):
                count+=x&1; x=H(x)
            v.append(int(count==j))
        c=comb(t,j)
        assert sum(v)==c
        individual+=w*c*(q-c)
        grouped+=w*w*c*(q-c)
        for a in range(q): G[a]+=w*v[a]
        signatures.append((w,c,v))
    total=comb(A-1,r-1)
    assert sum(G)==total
    variance_num=q*sum(x*x for x in G)-total*total
    positive=negative=0
    for i,(w,c,v) in enumerate(signatures):
        for w2,c2,v2 in signatures[i+1:]:
            cov=2*w*w2*(q*sum(x*y for x,y in zip(v,v2))-c*c2)
            if cov>=0: positive+=cov
            else: negative+=cov
    assert grouped+positive+negative==variance_num
    return dict(r=r,A=A,m=m,t=t,q=q,active_signatures=len(signatures),
        mean=str(Fraction(total,q)),variance=str(Fraction(variance_num,q*q)),
        individual_diagonal=str(Fraction(individual,q*q)),
        grouped_diagonal=str(Fraction(grouped,q*q)),
        positive_cross=str(Fraction(positive,q*q)),
        negative_cross=str(Fraction(negative,q*q)),
        G=G)

if __name__=='__main__':
    out={'scope':'fixed r=5,10,12,14; exact signature-group covariance, finite only',
         'panels':[panel(r) for r in [5,10,12,14]]}
    Path(__file__).with_name('GROUPED_VARIANCE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
