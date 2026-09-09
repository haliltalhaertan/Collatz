from math import comb,log2
from pathlib import Path
import json

rows=[]
for r in (10,12,16):
 A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m
 cs=[0]*(t+1)
 for x in range(1,2**m,2):
  y=x;k=0
  for _ in range(m):
   k+=y%2;y=(3*y+1)//2 if y%2 else y//2
  for h in range(t+1):
   cs[h]+=int(r-(t-h)<=k<=r)
   if h<t:k+=y%2;y=(3*y+1)//2 if y%2 else y//2
 lows=[]
 for h in range(t+1):
  lo=max(1,r-t+h);hi=min(m,r-h)
  lower=sum(comb(m-1,k-1) for k in range(lo,hi+1))
  assert lower<=cs[h]
  lows.append(lower)
 assert all(cs[i+1]<=cs[i] for i in range(t))
 rows.append(dict(r=r,A=A,m=m,t=t,certificates=cs,forced_acceptance_lower_bounds=lows,exact=cs[-1]))
a=log2(3);b=1.2;kappa=1.053
def H(p):return -p*log2(p)-(1-p)*log2(1-p)
lo=.5;hi=1-1e-15
for _ in range(80):
 p=(lo+hi)/2
 if H(p)>1/kappa:lo=p
 else:hi=p
p=(lo+hi)/2;h=b*p-(1-a+b)
out=dict(status='PASS',rows=rows,necessary_lookahead=dict(b=b,kappa=kappa,p=p,h_over_r=h,h_over_tail=h/(a-b),scope='necessary only for the specified full-dyadic exact-lookahead/worst-rest certificate'))
Path(__file__).with_name('LOOKAHEAD_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
