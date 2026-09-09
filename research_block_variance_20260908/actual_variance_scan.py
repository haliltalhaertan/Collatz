from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from math import comb
import json
violations=[];cases=0;critical=[]
for A in range(2,15):
 weights=[]
 for x in range(1,2**A,2):
  y=x;k=0
  for _ in range(A):
   e=y%2;k+=e;y=(3*y+1)//2 if e else y//2
  weights.append(k)
 for m in range(1,A):
  B=2**(A-m);width=2**(m-1);blocks=[Counter(weights[j*width:(j+1)*width]) for j in range(B)]
  for r in range(1,A+1):
   G=[c[r] for c in blocks];T=sum(G)
   assert T==comb(A-1,r-1)
   ss=sum(g*g for g in G);ratio=F(B*ss-T*T,B*T);cases+=1
   row=dict(A=A,m=m,t=A-m,r=r,mean=str(F(T,B)),variance_over_mean=str(ratio),critical_mass=A==(3**r).bit_length()-1,intended_m=m==(6*r+4)//5)
   if ratio>1:
    row['histogram']=dict(sorted(Counter(G).items()));violations.append(row)
   if row['critical_mass'] and row['intended_m']:critical.append(row)
violations.sort(key=lambda z:F(z['variance_over_mean']),reverse=True)
out=dict(status='PASS',cases=cases,violation_count=len(violations),critical_mass_violation_count=sum(v['critical_mass'] for v in violations),top_violations=violations[:12],first_by_A=min(violations,key=lambda z:(z['A'],z['m'],z['r'])) if violations else None,critical_mass_violations=[v for v in violations if v['critical_mass']][:10],intended_critical_rows=critical)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
