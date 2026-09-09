"""Independent exact check of affine-offset tail bound; bounded numeric calibration."""
from math import comb, log2
from pathlib import Path
import json

def step(x):
    return (3*x+1)//2 if x%2 else x//2

checks=0
for m in range(1,13):
    for t in range(1,7):
        counts={}
        for x in range(1,2**m,2):
            y=x;k=0;C=0
            for i in range(m):
                p=y%2;k+=p
                C=(3*C+2**i) if p else C
                y=step(y)
            assert 2**m*y==3**k*x+C
            assert 0<=C<=2**(m-k)*(3**k-2**k)
            assert 0<y<3**k
            z=y;j=0
            for _ in range(t):
                j+=z%2;z=step(z)
            counts[k,j]=counts.get((k,j),0)+1
        for (k,j),actual in counts.items():
            cap1=comb(m-1,k-1)
            cap2=comb(t,j)*((3**k+2**t-1)//2**t)*(2**(m-k)+1)
            assert actual<=min(cap1,cap2),(m,t,k,j,actual,cap1,cap2)
            checks+=1

alpha=log2(3)
def H(p):
    return 0.0 if p<=0 or p>=1 else -p*log2(p)-(1-p)*log2(1-p)

def envelope(b):
    t=alpha-b;lo=max(0,1-t);hi=min(b,1)
    def g(s):
        return min(b*H(s/b),b-s+max(alpha*s-t,0)+t*H((1-s)/t))
    splits=sorted(set([lo,hi,max(lo,min(hi,t/alpha))]))
    candidates=[(g(s),s) for s in splits]
    # Each part is concave: min of two concave functions; split max-affine kink.
    for ll,hh in zip(splits,splits[1:]):
        for _ in range(120):
            a=(2*ll+hh)/3;c=(ll+2*hh)/3
            if g(a)<g(c):ll=a
            else:hh=c
        s=(ll+hh)/2;candidates.append((g(s),s))
    gamma,s=max(candidates)
    return dict(b=b,gamma=gamma,s=s,bridge_ceiling=b/gamma)

out=dict(status='PASS',exact_count_cells=checks,m_max=12,t_max=6,
         numerical_calibration=[envelope(b) for b in [1.1,1.169925001442312,1.2,1.21,1.22,1.3,1.4,1.55]])
Path(__file__).with_name('audit_tail_result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
