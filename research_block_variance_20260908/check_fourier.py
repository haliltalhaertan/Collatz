from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import cmath,json

r=10;m=12;t=3;Q=2**t
def H(x):return (3*x+1)//2 if x%2 else x//2
P={}
for x in range(1,2**m,2):
 y=x;k=0
 for _ in range(m):k+=y%2;y=H(y)
 P.setdefault(k,Counter())[y%Q]+=1
T={}
for z in range(Q):
 y=z;j=0
 for _ in range(t):j+=y%2;y=H(y)
 T.setdefault(j,Counter())[z]=1
def hat(f,n):return sum(v*cmath.exp(-2j*cmath.pi*n*z/Q) for z,v in f.items())
G=json.loads(Path(__file__).with_name('RESULT.json').read_text())['rows'][0]['G']
errors=[];energy=0
for eta in range(Q):
 rhs=sum(hat(T.get(r-k,{}),(pow(3,-k,Q)*eta)%Q)*hat(p,(-pow(3,-k,Q)*eta)%Q) for k,p in P.items())
 lhs=hat(dict(enumerate(G)),eta)
 errors.append(abs(lhs-rhs))
 assert abs(lhs-rhs)<1e-7
 if eta:energy+=abs(rhs)**2/Q**2
exactV=F(json.loads(Path(__file__).with_name('RESULT.json').read_text())['rows'][0]['variance'])
assert abs(energy-float(exactV))<1e-7
out=dict(status='PASS',scope='floating-point independent Fourier identity check on r10; proof is algebraic',max_error=max(errors),spectral_variance=energy,exact_variance=str(exactV))
Path(__file__).with_name('FOURIER_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
