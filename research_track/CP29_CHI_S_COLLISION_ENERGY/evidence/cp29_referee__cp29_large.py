#!/usr/bin/env python3
"""Independent memory-bounded density recursion, output in RAM one level at a time.
No other candidate code imported. Array h_s(y)=3^s P(X_s=y) (float64).
Truncate geometric A after 56, omitted mass 2^-56 per level.
"""
import json, os, time, sys
import numpy as np
K=int(os.environ.get('CP29_CUTOFF','56'))
STOP=int(os.environ.get('CP29_STOP','18'))
BLOCK=int(os.environ.get('CP29_BLOCK','1000000'))
old=np.ones(1,dtype=np.float64)
chi_before=1.
results=[]
for s in range(1,STOP+1):
    tic=time.monotonic()
    n=old.size
    m=3*n
    nxt=np.zeros(m, dtype=np.float64)
    # All A leading to a given unit residue r have fixed parity.
    # y=r+3j: x=((2^a*r-1)//3+2^a*j) mod n.
    for a in range(1,K+1):
        pow2=pow(2,a,m)
        r=1 if a%2==0 else 2
        offset=((pow2*r-1)%m)//3
        mult=pow2%n
        w=3.0*2.0**(-a)
        target=nxt[r::3]
        for start in range(0,n,BLOCK):
            end=min(start+BLOCK,n)
            ix=np.arange(start,end,dtype=np.int64)
            ix *= mult
            ix += offset
            ix %= n
            # unique output locations for each A; no add.at needed
            target[start:end] += w*old[ix]
    chi=float(np.dot(nxt,nxt)/m)
    peak=float(nxt.max())
    # sum density is 3^s(1-2^-K)^s; mass = sum(h)/3^s
    mass=float(nxt.sum()/m)
    row={'s':s,'chi':chi,'E':chi-chi_before,'max_scaled':peak,
         'mass':mass,'seconds':time.monotonic()-tic,'cutoff':K}
    print(json.dumps(row),flush=True)
    results.append(row)
    del old
    old=nxt
    chi_before=chi
    if s in (17,18):
        with open('cp29_large_partial.json','w') as f:json.dump(results,f,indent=2)
with open('cp29_large.json','w') as f:json.dump(results,f,indent=2)
