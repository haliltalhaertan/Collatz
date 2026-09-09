from collections import Counter
from pathlib import Path
import json
def word(x,t):
 p=[]
 for _ in range(t):
  e=x%2;p.append(e);x=(3*x+1)//2 if e else x//2
 return tuple(p)
checks=0
for t in range(1,8):
 q=2**t
 assert len({word(x,t) for x in range(q)})==q
 for a in (1,3,9,27):
  for N in sorted(set((1,2,q-1,q,q+1,2*q,2*q+3))):
   hist=[]
   for b in range(q):
    c=Counter((a*j+b)%q for j in range(N))
    hist.append(tuple(c[x] for x in range(q)))
   assert len(set(hist))==(1 if N%q==0 else q)
   checks+=1
for N,t in ((1,1),(2,2)):
 polys=[]
 for b in(1,2):
  polys.append(dict(Counter(sum(word(9*j+b,t)) for j in range(N))))
 assert polys[0]!=polys[1]
for j in range(100):
 for x,expected in ((1+16*j,1+9*j),(3+16*j,2+9*j)):
  assert sum(word(x,4))==2
  for _ in range(4):x=(3*x+1)//2 if x%2 else x//2
  assert x==expected
out=dict(status='PASS',equivalence_parameter_cases=checks,actual_prefix_identity_cases=200,scope='Full-word continuation laws; not all scalar-weight algorithms')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
