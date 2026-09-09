"""Bounded exact experiment: sound count majorants, no asymptotic fit."""
from functools import lru_cache
from math import comb, floor, log2
from pathlib import Path
import json

def letters(r,A,j,a):
    k,R=r-j,A-a
    return (R,) if k==1 else range(1,R-k+2)

def exact(r,A,L):
    q=3**r; inv=pow(2,-A,q)
    @lru_cache(None)
    def V(j,a,c):
        if j==r:
            return int(inv*c%q<L)
        mod=3**(j+1)
        return sum(V(j+1,a+m,(3*c+pow(2,a,mod))%mod) for m in letters(r,A,j,a))
    return V(0,0,0),V.cache_info().currsize

def high_bound(r,A,L,t):
    q=3**r; H=3**t; W=q//H
    @lru_cache(None)
    def successors(a,b):
        c=pow(2,a-A,q)
        lo,hi=b*W,(b+1)*W-1
        bins=[]
        for v in range((3*lo+c)//W,(3*hi+c)//W+1):
            lower=max(lo,-(-(v*W-c)//3))
            upper=min(hi,((v+1)*W-1-c)//3)
            if lower<=upper:
                bins.append(v%H)
        return tuple(sorted(set(bins)))
    @lru_cache(None)
    def F(j,a,b):
        if j==r:
            return int(b*W<L)
        nxt=successors(a,b)
        return sum(max(F(j+1,a+m,c) for c in nxt) for m in letters(r,A,j,a))
    # The root x=0 and first transition are exact, not an initial interval.
    b1=pow(2,-A,q)//W
    value=sum(F(1,m,b1) for m in letters(r,A,0,0))
    return value,F.cache_info().currsize

def direct(r,A,L):
    q=3**r; inv=pow(2,-A,q)
    def words(R,k):
        if k==1:
            yield (R,)
        else:
            for m in range(1,R-k+2):
                for tail in words(R-m,k-1): yield (m,)+tail
    total=hit=0
    for w in words(A,r):
        B=sum(3**(r-1-i)*2**sum(w[:i]) for i in range(r))
        total+=1; hit+=int(B*inv%q<L)
    assert total==comb(A-1,r-1)
    return hit

rows=[]
for r in range(3,11):
    for d in (-1,0,1):
        A=floor(log2(3)*r)+d
        if A<r: continue
        for b in (.8,1.2):
            L=floor(2**(b*r)); N=comb(A-1,r-1)
            Q,states=exact(r,A,L)
            assert direct(r,A,L)==Q
            bounds=[]
            for t in range(1,min(4,r)):
                upper,nstates=high_bound(r,A,L,t)
                assert Q<=upper<=N
                H,W=3**t,3**(r-t)
                assert upper*H>=N*((L+W-1)//W)
                bounds.append(dict(t=t,upper=upper,states=nstates,ratio=upper/N))
            if r<=5:
                assert high_bound(r,A,L,r)[0]==Q
            rows.append(dict(r=r,A=A,b=b,L=L,N=N,Q=Q,exact_states=states,high=bounds))
out=dict(status='PASS',cases=len(rows),rows=rows)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
nontrivial=[dict(r=x['r'],A=x['A'],b=x['b'],N=x['N'],Q=x['Q'],**v)
            for x in rows for v in x['high'] if v['upper']<x['N']]
print(json.dumps(dict(status='PASS',cases=len(rows),nontrivial_count=len(nontrivial),examples=nontrivial[:12]),indent=2))
