import json
from pathlib import Path
out=[]
for t in range(1,40,2):
 y=2**t-1;k=0
 while 3**k<=y:k+=1
 x=y;rev=[]
 for _ in range(k):
  a=1 if x%3==2 else 2
  if ((2**a*x-1)//3)%3==0:a+=2
  assert (2**a*x-1)%3==0
  x=(2**a*x-1)//3
  assert x>0 and x%2==1 and x%3!=0
  rev.append(a)
 m=sum(rev);z=x;bits=[]
 for _ in range(m+t):
  b=z%2;bits.append(b);z=(3*z+1)//2 if b else z//2
 assert x<2**m and sum(bits[:m])==k and all(bits[m:])
 out.append(dict(t=t,k=k,m=m,x=x,tail_start=y,valuations=list(reversed(rev)),critical_defect=m+t-(3**(k+t)).bit_length()+1))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
