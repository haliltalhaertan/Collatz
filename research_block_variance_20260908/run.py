from collections import defaultdict
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import json

def block(m,t,a,r):
 A=m+t;states={(1,(3*a*2**(m-1)+2)%(2**(A-1))):1}
 for i in range(1,m):
  mod=2**(A-i-1);new=defaultdict(int)
  for (k,b),v in states.items():
   for h in (0,1):
    c=b+3**k*h;p=c%2
    new[k+p,((3*c+1)//2 if p else c//2)%mod]+=v
  states=new
 total=0
 for (k,b),v in states.items():
  for i in range(t):k+=b%2;b=(3*b+1)//2 if b%2 else b//2
  if k==r:total+=v
 return total

rows=[]
for r in (10,12,14):
 A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m;Q=2**t
 G=[block(m,t,a,r) for a in range(Q)]
 S=sum(G);assert S==comb(A-1,r-1)
 B=F(S,Q);V=sum((F(g)-B)**2 for g in G)/Q
 num=(Q-1)*(Q*sum(g*g for g in G)-S*S)
 root=isqrt(num);root+=root*root<num
 bound=(S+root+Q-1)//Q
 assert max(G)<=bound
 # Independent old direct-iteration controls.
 if r in (10,12):
  old=json.loads((Path(__file__).resolve().parents[1]/'research_joint_panel_20260908/BLOCK_RESULT.json').read_text())
  assert G==next(x['block_totals'] for x in old['rows'] if x['r']==r)
 means=[F(sum(G[::2**s]),len(G[::2**s])) for s in range(t+1)]
 assert means[0]==B and means[-1]==G[0]
 rows.append(dict(r=r,A=A,m=m,t=t,blocks=Q,G=G,mean=str(B),variance=str(V),relative_variance=str(V/B**2),fano=str(V/B),origin=G[0],minimum=min(G),maximum=max(G),uniform_integer_bound=bound,origin_nested_means=list(map(str,means))))
out=dict(status='PASS',design='fixed all-block panels r10,12,14; no extrapolation',rows=rows)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
