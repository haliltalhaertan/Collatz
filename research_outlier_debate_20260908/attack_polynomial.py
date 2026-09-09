from collections import Counter
from functools import lru_cache
from pathlib import Path
import json

@lru_cache(None)
def progression(a,b,N,m,t):
 if not N:return ()
 if m+t==0:return (((0,0),N),)
 out=Counter();stage=0 if m else 1
 nm,nt=(m-1,t) if m else (0,t-1)
 if a%2==0:
  e=b%2
  branches=[(a//2,b//2,N,e)] if not e else [(3*a//2,(3*b+1)//2,N,e)]
 else:
  branches=[]
  for j in (0,1):
   C=b+a*j;e=C%2;count=(N+1-j)//2
   branches.append((a,C//2,count,e) if not e else (3*a,(3*C+1)//2,count,e))
 for aa,bb,nn,e in branches:
  for (k,l),count in progression(aa,bb,nn,nm,nt):
   out[(k+e*(stage==0),l+e*(stage==1))]+=count
 return tuple(sorted(out.items()))

def direct(m,t):
 out=Counter();examples=[]
 for x in range(1,2**m,2):
  y=x;k=l=0
  for i in range(m+t):
   e=y%2
   if i<m:k+=e
   else:l+=e
   y=(3*y+1)//2 if e else y//2
  out[k,l]+=1
  examples.append(dict(x=x,k=k,l=l))
 return out,examples

rows=[]
for m in range(1,10):
 for t in range(1,6):
  p=dict(progression(2,1,2**(m-1),m,t));d,examples=direct(m,t)
  assert p==d
  row=dict(m=m,t=t,coefficients=[dict(k=k,l=l,count=c) for (k,l),c in sorted(p.items())])
  if m<=4 and t<=2:row['examples']=examples
  rows.append(row)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(status='PASS',rows=rows),indent=2))
print(json.dumps(dict(status='PASS',cases=len(rows),cache=str(progression.cache_info()))))
