from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json, sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research_exact_join_20260908'))
from run import numerators

out={'sidon':[], 'actual':[]}
for n in (4,8,16,32):
    S=[3*(i+2*n*i*i)+1 for i in range(n)]
    m=3
    while m<=2*max(S):m*=3
    c=Counter((x-y)%m for x in S for y in S)
    energy=sum(v*v for v in c.values())
    assert energy==2*n*n-n
    assert c[0]==n and all(v==1 for z,v in c.items() if z)
    out['sidon'].append(dict(n=n,m=m,overlap=str(F(1,n)),uniform=str(F(1,m)),
        convolution_norm_ratio_squared=str(F(energy,n**3))))
for r,A,L in ((10,15,256),(10,15,4096)):
    k=1
    while 3**k<L:k+=1
    j=r-k;m=3**j; terms=[]; sums=[F(0)]*(j+1)
    for R in range(k,A-j+1):
        a=A-R
        P=Counter(B*pow(2,-a,m)%m for B in numerators(j,a));D=Counter()
        for B in numerators(k,R):
            z=B*pow(2,-R,3**k)%(3**k)
            if z<L:D[((2**R*z-B)//3**k)%m]+=1
        levels=[]
        for s in range(j+1):
            ps=Counter();ds=Counter();q=3**s
            for t,v in P.items():ps[t%q]+=v
            for t,v in D.items():ds[t%q]+=v
            levels.append(F(sum(v*ds[t] for t,v in ps.items()),m//q))
        exact=sum(v*D[t] for t,v in P.items())
        increments=[levels[0]]+[levels[s]-levels[s-1] for s in range(1,j+1)]
        assert levels[-1]==exact and sum(increments)==exact
        sums=[x+y for x,y in zip(sums,increments)]
        terms.append(dict(R=R,baseline_and_increments=list(map(str,increments)),Q=exact))
    direct=sum(B*pow(2,-A,3**r)%(3**r)<L for B in numerators(r,A))
    assert sum(sums)==direct
    out['actual'].append(dict(r=r,A=A,L=L,Q=direct,baseline_and_increments=list(map(str,sums)),terms=terms))
out['status']='PASS'
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
