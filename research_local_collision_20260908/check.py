from itertools import combinations
from pathlib import Path
import json

def words(r,A):
    for cuts in combinations(range(1,A),r-1):
        c=(0,)+cuts+(A,)
        yield tuple(c[i+1]-c[i] for i in range(r))
def B(w):
    b=0;a=0
    for v in w:b=3*b+2**a;a+=v
    return b
def v3(x):
    x=abs(x);v=0
    while x%3==0:x//=3;v+=1
    return v
checks=0;witness=None
for r in range(2,12):
    A=int(r*1.584962500721156)
    seen=set()
    for w in words(r,A):
        b=B(w)
        assert b not in seen
        seen.add(b)
        for i in range(r-1):
            for d in range(1,w[i+1]):
                z=list(w);z[i]+=d;z[i+1]-=d
                diff=B(z)-b
                formula=3**(r-i-2)*2**sum(w[:i+1])*(2**d-1)
                assert diff==formula
                expected=r-i-2+(0 if d%2 else 1+v3(d//2))
                assert v3(diff)==expected
                collision=diff%3**r==0
                assert collision==(d%(2*3**(i+1))==0)
                if collision and witness is None:witness=dict(r=r,A=A,w=w,z=z,B=b,B2=B(z),residue=b*pow(2,-A,3**r)%3**r)
                checks+=1
out=dict(status='PASS',local_move_checks=checks,first_critical_band_collision=witness)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
