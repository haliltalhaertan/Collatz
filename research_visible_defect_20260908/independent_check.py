"""Independent exact dyadic source and convolution audit, frozen four panels."""
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

def H(x):return (3*x+1)//2 if x&1 else x//2
def weight(x,t):
    k=0
    for _ in range(t):k+=x&1;x=H(x)
    return k

def panel(r):
    A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m;q=1<<t
    P=Counter()
    for h in range(1,1<<m,2):
        x=h;k=0
        for _ in range(m):k+=x&1;x=H(x)
        P[k,x%q]+=1
    rows=[]; G=[0]*q;sumV=F(0);D2=F(0);Dsrc=F(0)
    tails=[weight(z,t) for z in range(q)]
    for k in range(max(1,r-t),min(m,r)+1):
        N=comb(m-1,k-1);j=r-k;c=comb(t,j);p=F(c,q)
        full=[P[k,z] for z in range(q)]
        assert sum(full)==N
        resolutions=[];previous=F(0);Rlist=[]
        for s in range(t+1):
            mod=1<<s;counts=[sum(full[z::mod]) for z in range(mod)]
            e=F(sum(v*v for v in counts))-F(N*N,mod)
            if s:
                R=sum((counts[z]-counts[z+(mod//2)])**2 for z in range(mod//2))
                assert e==previous/2+F(R,2)
                Rlist.append(R)
            resolutions.append(dict(s=s,e=str(e)))
            previous=e
        e=previous
        assert e==sum((F(R,1<<(t-s)) for s,R in enumerate(Rlist)),F(0))
        # Direct cyclic correlation; no Fourier transforms or conductor formulas.
        conv=[sum(full[z] for z in range(q) if tails[(z+a)%q]==j) for a in range(q)]
        mean=N*p
        assert sum(conv)==N*c
        Vk=sum(((F(v)-mean)**2 for v in conv),F(0))/q
        # Independent pair-autocorrelation expansion of the same variance.
        tail=[int(v==j) for v in tails]
        pairsecond=F(0)
        for d in range(q):
            Csource=sum(full[z]*full[(z+d)%q] for z in range(q))
            Ctail=sum(tail[z]*tail[(z+d)%q] for z in range(q))
            pairsecond+=F(Csource*Ctail,q)
        assert pairsecond-mean*mean==Vk
        bound=q*e*p*p
        assert Vk<=bound
        # Actual translation of initial starts has the weight-dependent slope.
        for a in range(q):G[a]+=conv[(pow(3,k,q)*a)%q]
        sumV+=Vk;D2+=e*p*p;Dsrc+=e*p*(1-p)
        rows.append(dict(k=k,j=j,N=N,p=str(p),e=str(e),R_by_s=Rlist,
            resolutions=resolutions,Vk=str(Vk),generic_bound=str(bound),
            visible_fraction_of_generic=str(Vk/bound) if bound else None))
    B=F(comb(A-1,r-1),q)
    assert sum(G)==q*B
    V=sum(((F(g)-B)**2 for g in G),F(0))/q
    assert V<=len(rows)*sumV
    return dict(r=r,A=A,m=m,t=t,q=q,B=str(B),D2=str(D2),Dsrc=str(Dsrc),
        sumVk=str(sumV),qD2=str(q*D2),V=str(V),G=G,rows=rows)

if __name__=='__main__':
    panels=[panel(r) for r in [5,10,12,14]]
    out=dict(scope='Frozen r=5,10,12,14; exact integer/rational arithmetic; no Fourier',panels=panels)
    Path(__file__).with_name('INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:p[k] for k in ['r','D2','Dsrc','sumVk','qD2','V']} for p in panels],indent=2))
