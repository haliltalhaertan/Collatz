"""Exact conditional-projection energies equal cyclic Fourier conductor energies."""
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

def H(x):return (3*x+1)//2 if x&1 else x//2
def choose(n,k):return comb(n,k) if 0<=k<=n else 0
def conductor_energies(v):
    q=len(v);t=q.bit_length()-1;mean=sum(v)/q
    previous=F(0);out=[]
    for s in range(1,t+1):
        n=1<<s
        means=[sum(v[a] for a in range(b,q,n))*F(n,q)-mean for b in range(n)]
        energy=sum(x*x for x in means)/n
        assert energy>=previous
        out.append(energy-previous);previous=energy
    return out

def panel(r):
    A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m;q=1<<t
    P=Counter()
    for h in range(1,1<<m,2):
        x=h;k=0
        for _ in range(m):k+=x&1;x=H(x)
        P[k,x%q]+=1
    tails=[]
    for z in range(q):
        x=z;j=0
        for _ in range(t):j+=x&1;x=H(x)
        tails.append(j)
    total=[F(0)]*q;rows=[]
    sum_source=[F(0)]*t;sum_visible=[F(0)]*t
    for k in range(max(1,r-t),min(m,r)+1):
        j=r-k;Nk=comb(m-1,k-1);p=F(comb(t,j),q)
        pk=[F(P[k,z]) for z in range(q)]
        assert sum(pk)==Nk
        es=[q*x for x in conductor_energies(pk)]
        # Independent sibling-count identity for source conductor energy.
        for s,e in enumerate(es,1):
            n=1<<s;aggregated=[sum(pk[z] for z in range(b,q,n)) for b in range(n)]
            R=sum((aggregated[b]-aggregated[b+n//2])**2 for b in range(n//2))
            assert e==F(1<<(s-1),q)*R
        g=[sum(pk[z] for z in range(q) if tails[(z+pow(3,k,q)*a)%q]==j) for a in range(q)]
        vs=conductor_energies(g)
        for s in range(t):
            cap=q*p*p*es[s]
            assert vs[s]<=cap
            sum_source[s]+=cap;sum_visible[s]+=vs[s]
        # Exact parity-conductor transmission factor.
        assert vs[0]==q*p*p*es[0]*F(t-2*j,t)**2
        for a in range(q):total[a]+=g[a]
        rows.append(dict(k=k,j=j,N=Nk,p=str(p),source_energies=list(map(str,es)),
            visible_variances=list(map(str,vs))))
    B=F(comb(A-1,r-1),q);assert sum(total)==q*B
    actual=conductor_energies(total)
    assert sum(actual)==sum((x-B)**2 for x in total)/q
    return dict(r=r,A=A,m=m,t=t,B=str(B),G=list(map(int,total)),layers=rows,
        source_caps_by_conductor=list(map(str,sum_source)),
        sum_layer_variances_by_conductor=list(map(str,sum_visible)),
        total_variances_by_conductor=list(map(str,actual)))

if __name__=='__main__':
    out=[panel(r) for r in [5,10,12,14]]
    Path(__file__).with_name('DIAGNOSTIC.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in p.items() if k not in ('layers','G')} for p in out],indent=2))
