from collections import defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

checks=0;cells=0
for m in range(1,12):
 groups=defaultdict(list)
 for x in range(1,2**m,2):
  y=x;k=0
  for _ in range(m):
   k+=y%2;y=(3*y+1)//2 if y%2 else y//2
  E=F(2**m*y-3**k*x,2**m)
  groups[k].append(E);checks+=1
 for k,es in groups.items():
  p=F(k,m);v=1+2*p
  bound=F(m,k)*sum((F(1,2**j)*v**(j-1) for j in range(1,m+1)),F(0))
  assert len(es)==comb(m-1,k-1)
  actual=sum(es,F(0))/len(es)
  assert actual<=bound
  for R in (1,2,4,8):
   assert F(sum(e>R for e in es),len(es))<=bound/R
  cells+=1
out=dict(status='PASS',start_checks=checks,weight_cells=cells,scope='theta=1 exact rational verification of conditional moment and Markov bound')
Path(__file__).with_name('MOMENT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
