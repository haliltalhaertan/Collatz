from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time
import numpy as np
ROOT=Path(__file__).parent
C=lambda n,k:comb(n,k) if 0<=k<=n else 0
def budget(t,j,s):
 return sum(C(s-1,h)*(C(t-s,j-h)-C(t-s,j-h-1))**2 for h in range(s))
def panel(r):
 started=time.perf_counter();A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m;q=2**t
 hist=np.zeros((m+1,q),dtype=np.int64)
 for start in range(1,2**m,2**17):
  x=np.arange(start,min(start+2**17,2**m),2,dtype=np.int64)
  k=np.zeros(len(x),dtype=np.int64)
  for _ in range(m):
   b=x&1;k+=b;x=np.where(b,(3*x+1)//2,x//2)
  hist+=np.bincount(k*q+x%q,minlength=(m+1)*q).reshape(m+1,q)
 assert int(hist.sum())==2**(m-1)
 assert all(int(hist[k].sum())==C(m-1,k-1) for k in range(m+1))
 x=np.arange(q,dtype=np.int64);tw=np.zeros(q,dtype=np.int64)
 for _ in range(t):
  b=x&1;tw+=b;x=np.where(b,(3*x+1)//2,x//2)
 rows=[];W=F(0);flat_total=F(0)
 removed={str(L):0.0 for L in [1,2,4]};oracle={str(L):0.0 for L in [1,2,4]}
 for k in range(max(1,r-t),min(m,r)+1):
  j=r-k;P=hist[k];T=(tw==j).astype(np.int64)
  G=[int(P@np.roll(T,-a)) for a in range(q)]
  direct=F(q*sum(g*g for g in G)-sum(G)**2,q*q)
  exact_sum=F(0)
  for s in range(1,t+1):
   n=2**s;H=n//2
   pp=np.array([sum(map(int,P[u::n])) for u in range(n)],dtype=np.int64)
   tt=np.array([sum(map(int,T[u::n])) for u in range(n)],dtype=np.int64)
   R=sum(int(pp[u]-pp[u+H])**2 for u in range(H));D=budget(t,j,s)
   cp=[sum(int(pp[u])*int(pp[(u+d)%n]) for u in range(n)) for d in range(n)]
   ct=[sum(int(tt[u])*int(tt[(u+d)%n]) for u in range(n)) for d in range(n)]
   V=F(H*sum(cp[d]*(ct[d]-ct[(d+H)%n]) for d in range(n)),q*q)
   flat=F(H*R*D,q*q);assert V>=0
   if s<=2:assert V==flat
   assert V<=(1 if s==1 else H//2)*flat
   X=np.abs(np.fft.fft(pp))**2;Y=np.abs(np.fft.fft(tt))**2
   pairs=[]
   for a in ([1] if s==1 else range(1,H,2)):
    factor=1 if s==1 else 2
    pairs.append({'a':a,'conjugate':(-a)%n,'tail':float(Y[a]),'source':float(X[a]),'contribution':float(factor*X[a]*Y[a]/(q*q))})
   fft_total=sum(p['contribution'] for p in pairs)
   assert abs(fft_total-float(V))<=1e-7*max(1,float(V))
   # Exact equality classes in Z[zeta_(2^s)]: Phi_(2^s)=X^H+1.
   # FFT noise must not choose a different member of an exactly tied class.
   groups={}
   for pair in pairs:
    poly=[0]*H
    for d,c in enumerate(ct):
     exponent=(pair['a']*d)%n
     poly[exponent%H]+=(1 if exponent<H else -1)*c
    groups.setdefault(tuple(poly),[]).append(pair)
   ranked=sorted(groups.values(),key=lambda group:-sum(p['tail'] for p in group)/len(group))
   for left,right in zip(ranked,ranked[1:]):
    assert min(p['tail'] for p in left)-max(p['tail'] for p in right)>1e-9*max(1,max(Y))
   bytail=[pair for group in ranked for pair in sorted(group,key=lambda p:p['a'])]
   byjoint=sorted(pairs,key=lambda p:(-p['contribution'],p['a']))
   for L in [1,2,4]:
    removed[str(L)]+=sum(p['contribution'] for p in bytail[:L])
    oracle[str(L)]+=sum(p['contribution'] for p in byjoint[:L])
   rows.append({'k':k,'j':j,'s':s,'R':R,'D':D,'V':str(V),'flat':str(flat),'alignment':str(V/flat) if flat else None,'pairs_by_tail':bytail})
   exact_sum+=V;flat_total+=flat
  assert exact_sum==direct
  W+=direct
 return {'r':r,'A':A,'m':m,'t':t,'starts':2**(m-1),'W':str(W),'W_flat':str(flat_total),'ratio':str(W/flat_total),'tail_top_shares':{L:v/float(W) for L,v in removed.items()},'joint_oracle_shares':{L:v/float(W) for L,v in oracle.items()},'tail_residual_over_original_flat':{L:(float(W)-v)/float(flat_total) for L,v in removed.items()},'rows':rows,'seconds':time.perf_counter()-started}
if __name__=='__main__':
 plan=json.loads((ROOT/'PLAN.json').read_text())
 results=[]
 for r in plan['panels_r']:
  p=panel(r);results.append(p);print(json.dumps({k:v for k,v in p.items() if k!='rows'}),flush=True)
 (ROOT/'RESULTS.json').write_text(json.dumps({'plan':plan,'panels':results},indent=2)+'\n',encoding='utf-8',newline='\n')
