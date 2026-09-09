"""Exact small recurrence check, not an asymptotic experiment."""
from functools import lru_cache
from math import log2, floor, comb
from pathlib import Path
import json

def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for m in range(1, total-length+2):
        for tail in compositions(total-m, length-1):
            yield (m,)+tail

rows=[]
for r in range(2,8):
    for d in (-1,0,1):
        A=floor(log2(3)*r)+d
        if A<r:
            continue
        q=3**r
        L=floor(2**(0.8*r))
        inv=pow(pow(2,A,q),-1,q)
        @lru_cache(None)
        def V(j,a,z):
            if j==r:
                assert a==A
                return int((inv*z)%q<L)
            k,R=r-j,A-a
            letters=(R,) if k==1 else range(1,R-k+2)
            return sum(V(j+1,a+m,(3*z+pow(2,a,q))%q) for m in letters)
        exact=V(0,0,0)
        direct=total=0
        for w in compositions(A,r):
            prefixes=[sum(w[:i]) for i in range(r)]
            B=sum(3**(r-1-i)*2**prefixes[i] for i in range(r))
            direct+=int((B*inv)%q<L)
            total+=1
        assert total==comb(A-1,r-1)
        assert direct==exact
        rows.append(dict(r=r,A=A,L=L,words=total,Q=exact,states=V.cache_info().currsize))
out=dict(status='PASS',cases=len(rows),rows=rows)
Path(__file__).with_name('CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status='PASS',cases=len(rows),words_checked=sum(x['words'] for x in rows))))
