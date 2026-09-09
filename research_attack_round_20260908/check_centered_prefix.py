from collections import Counter
from fractions import Fraction as F
from math import comb, floor, ceil, log2
from pathlib import Path
import json

def H(x): return (3*x+1)//2 if x&1 else x//2

def panel(r):
    A=floor(log2(3)*r);m=ceil(1.2*r);t=A-m;q=1<<t
    P=Counter()
    for h in range(1,1<<m,2):
        k=0;x=h
        for _ in range(m): k+=x&1;x=H(x)
        P[k,x%q]+=1
    vectors=[]; raw_diag=F(0); centered_diag=F(0); G=[0]*q
    for k in range(max(1,r-t),min(m,r)+1):
        j=r-k;N=comb(m-1,k-1);c=comb(t,j);p=F(c,q)
        assert sum(P[k,z] for z in range(q))==N
        v=[F(0)]*q; cv=[F(0)]*q
        for z in range(q):
            w=P[k,z];dw=F(w)-F(N,q)
            raw_diag+=w*w*p*(1-p)
            centered_diag+=dw*dw*p*(1-p)
            for a in range(q):
                x=(z+pow(3,k,q)*a)%q;weight=0
                for _ in range(t): weight+=x&1;x=H(x)
                if weight==j: v[a]+=w;cv[a]+=dw
        assert cv==[x-N*p for x in v]
        for a in range(q):G[a]+=v[a]
        vectors.append(cv)
    B=F(comb(A-1,r-1),q)
    assert sum(G)==q*B
    V=sum((g-B)**2 for g in G)/q
    E=sum(sum(x*x for x in v)/q for v in vectors)
    assert V<=len(vectors)*E
    return dict(r=r,m=m,t=t,strata=len(vectors),V=str(V),
        raw_signature_diagonal=str(raw_diag),centered_signature_diagonal=str(centered_diag),
        sum_stratum_variances=str(E),cross_strata=str(V-E),
        cauchy_strata_bound=str(len(vectors)*E))

if __name__=='__main__':
    out=[panel(r) for r in [5,10,12,14]]
    Path(__file__).with_name('CENTERED_PREFIX.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
