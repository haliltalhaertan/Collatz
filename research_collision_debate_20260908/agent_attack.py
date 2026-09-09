from itertools import combinations
import json
from pathlib import Path
def words(r,A):
 for cuts in combinations(range(1,A),r-1):
  c=(0,)+cuts+(A,)
  yield tuple(c[i+1]-c[i] for i in range(r))
def B(w):
 b=0;s=0
 for a in w:b=3*b+2**s;s+=a
 return b
out=[]
for r in range(5,15):
 A=(3**r).bit_length()-1;q=3**r;inv=pow(2,-A,q);seen={};best=None;late=None;collisions=0
 for w in words(r,A):
  m=B(w)*inv%q
  if m in seen:
   z=seen[m];collisions+=1;last=max(i+1 for i in range(r) if w[i]!=z[i])
   item=dict(m=m,w=w,z=z,last=last)
   if best is None or m<best['m']:best=item
   if late is None or last>late['last']:late=item
  else:seen[m]=w
 out.append(dict(r=r,A=A,collisions=collisions,best=best,late=late))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
