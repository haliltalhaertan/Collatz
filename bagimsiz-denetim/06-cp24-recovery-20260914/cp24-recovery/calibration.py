"""Bounded calibration only; two routes: direct iterates vs abstract words.
A fixed-m endpoint descent count is not an all-integers stopping-time theorem.
"""
import json
from pathlib import Path

def direct(m):
 out={}
 for h in range(1,1<<m,2):
  x=h
  for _ in range(m):x=(3*x+1)//2 if x%2 else x//2
  out[h]=x<h
 return out

def words(m):
 out={};coefficient_only=[]
 for mask in range(1<<(m-1)):
  bits=[1]+[(mask>>i)&1 for i in range(m-1)]
  k=sum(bits);B=sum((1<<i)*3**sum(bits[i+1:]) for i in range(m) if bits[i])
  h=(-B*pow(3**k,-1,1<<m))%(1<<m)
  assert h%2 and h not in out
  D=(1<<m)-3**k
  out[h]=D*h>B
  if D>0 and not out[h]:coefficient_only.append(h)
 return out,coefficient_only

result=[]
for m,want in ((8,94),(16,27823)):
 a=direct(m);b,exceptions=words(m)
 assert a==b and sum(a.values())==want
 result.append({'m':m,'starts':len(a),'descents':sum(a.values()),'pointwise_agreement':True,'D_positive_but_no_endpoint_descent':sorted(exceptions)})
# Boundary and negative controls for auditor prose, not only main theorems.
assert (1<<1)-1==1 # reflection has a fixed source at m=1
assert (3*1+1)//2==2 # Hp(1) is NOT 1
assert (3*2+1)//2!=1 # the odd branch is inapplicable to even 2
assert 2//2==1
out={'calibration':result,'auditor_prose_corrections_verified':['m=1 reflection fixed source h=1','Hp trivial orbit is a 2-cycle, not a fixed point'],
 'scope':'No novelty, density limit, all-start descent, or Collatz proof claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
