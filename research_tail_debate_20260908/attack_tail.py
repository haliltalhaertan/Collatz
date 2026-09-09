import json
from pathlib import Path
out=[]
for r in range(8,17):
 A=(3**r).bit_length()-1;m=(6*r)//5;t=A-m;K=r-t
 counts={}; examples={}
 for x in range(1,2**m,2):
  y=x;k=0
  for _ in range(m):
   bit=y&1;k+=bit;y=(3*y+1)//2 if bit else y//2
  z=y;l=0
  for _ in range(t):
   bit=z&1;l+=bit;z=(3*z+1)//2 if bit else z//2
  if l==t:
   counts[k]=counts.get(k,0)+1
   examples.setdefault(k,dict(x=x,y=y,end=z))
 out.append(dict(r=r,A=A,m=m,t=t,K=K,allodd_by_prefix_weight=counts,critical_allodd=examples.get(K),allodd_total=sum(counts.values())))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
