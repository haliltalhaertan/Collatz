from pathlib import Path
from fractions import Fraction as F
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research_exact_join_20260908'))
from run import numerators

rows=[]
for r,A,L in ((7,11,337),(10,15,256),(10,15,4096)):
 q=3**r;p=2**A;c=F(p,q);D=2**(A-r)-c;X=c*L
 pairs=[]
 for b in numerators(r,A):
  n=b*pow(2,-A,q)%q;x=(p*n-b)//q
  assert p*n-b==q*x and 0<x<p and x%2==1
  assert F(b,q)<=D
  pairs.append((x,n))
 assert len(set(x for x,n in pairs))==len(pairs)
 # Independent ordinary iteration membership: exact first r-1 valuations,
 # and remaining division amount between 1 and actual next valuation.
 direct=[]
 for x in range(1,p,2):
  y=x;s=0
  for i in range(r-1):
   y=3*y+1;a=(y&-y).bit_length()-1;y>>=a;s+=a
  z=3*y+1;a=(z&-z).bit_length()-1
  if 1<=A-s<=a:
   n=z//2**(A-s)
   if n<q:direct.append((x,n))
 assert sorted(direct)==sorted(pairs)
 Q=sum(n<L for x,n in pairs);Qodd=sum(n<L and n%2 for x,n in pairs)
 lo=sum(x<X-D for x,n in pairs);hi=sum(x<X for x,n in pairs)
 assert lo<=Q<=hi
 rows.append(dict(r=r,A=A,L=L,Q=Q,Qodd=Qodd,F_lower=lo,F_upper=hi,X=str(X),D=str(D),actual_gap=hi-Q))
out=dict(status='PASS',rows=rows)
Path(__file__).with_name('DUAL_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
