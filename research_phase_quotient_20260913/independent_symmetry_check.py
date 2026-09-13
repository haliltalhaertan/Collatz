from functools import lru_cache
from math import comb
from random import Random
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def C(n,k):return comb(n,k) if 0<=k<=n else 0
def delta(t,l):return C(t-1,l)-C(t-1,l-1)
def canon(p):return tuple(sorted(tuple(x) for x in p))
@lru_cache(None)
def Q(t,j,n,c,pairs):
    N=1<<n;c%=N;pairs=canon(pairs)
    if n==1:
        z=1
        for d,e in pairs:z*=delta(t,j-d)
        return -z if c&1 else z
    q=N//2;r=pow(3,-1,q);cc=(4*r-1)%N;tot=0
    for mask in range(16):
        if (c+mask.bit_count())&1:continue
        sm=0;np=[]
        for i,(d,e) in enumerate(pairs):
            mu=e*pow(pow(3,d,N),-1,N)%N
            if mask>>i&1:sm+=mu;np.append((d+1,e))
            else:np.append((d,e))
        num=c+cc*sm;assert num%2==0
        tot+=2*Q(t-1,j,n-1,(num//2)%q,canon(np))
    return tot
rng=Random(20260913)
common=half=conj=0
for _ in range(80):
    n=rng.randint(2,5);N=1<<n;t=rng.randint(n+3,n+9);j=rng.randint(0,t)
    ds=[rng.randint(1,3) for __ in range(4)]
    pairs=canon([(ds[0],1),(ds[1],1),(ds[2],-1),(ds[3],-1)])
    c=rng.randrange(N)
    h=rng.randint(1,min(ds))
    a=Q(t,j,n,c,pairs)
    b=Q(t,j-h,n,(c*pow(3,h,N))%N,canon((d-h,e) for d,e in pairs))
    assert a==b;common+=1
    assert Q(t,j,n,(c+(N//2))%N,pairs)==-a;half+=1
    assert Q(t,j,n,(-c)%N,canon((d,-e) for d,e in pairs))==a;conj+=1
out={'status':'PASS','common_shift_checks':common,'half_character_checks':half,'sign_conjugation_checks':conj,
     'same_session_second_implementation':True,'independent_agent_audit':False}
(HERE/'SYMMETRY_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
