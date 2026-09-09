from collections import Counter
from math import comb
from fractions import Fraction as F
from pathlib import Path
import json

rows=[]
for r in (10,12):
 A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m;blocks=[];allcells=Counter()
 for a in range(2**t):
  cells=Counter()
  for x in range(a*2**m+1,(a+1)*2**m,2):
   y=x;k=j=0
   for i in range(A):
    p=y%2
    if i<m:k+=p
    else:j+=p
    y=(3*y+1)//2 if p else y//2
   cells[k,j]+=1
  allcells.update(cells)
  blocks.append(sum(v for (k,j),v in cells.items() if k+j==r))
 for k in range(1,m+1):
  for j in range(t+1):
   assert allcells[k,j]==comb(m-1,k-1)*comb(t,j)
 assert sum(blocks)==comb(A-1,r-1)
 rows.append(dict(r=r,A=A,m=m,t=t,block_totals=blocks,mean=str(F(sum(blocks),len(blocks))),min=min(blocks),max=max(blocks)))
out=dict(status='PASS',rows=rows)
Path(__file__).with_name('BLOCK_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
