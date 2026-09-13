"""Separate direct-DFT normalization cross-check for the phase Gram block.

This is a finite numerical implementation check, NOT the proof.  It does not
import phase_gram_round2.py and does not use FFT/correlation packing.
"""
from __future__ import annotations
from math import comb,cos,sin,pi
from pathlib import Path
import json,sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'research_shift_recurrence_20260912'))
from exact_moment import actual_filter


def dft(v,a):
    n=len(v); re=0.0; im=0.0
    for u,x in enumerate(v):
        th=-2*pi*a*u/n
        re += x*cos(th); im += x*sin(th)
    return complex(re,im)


def direct_K(t,j,s):
    N=1<<s; PN=2*N
    xs=[[],[],[]]
    parents=[]
    for d in range(3):
        parents.append(actual_filter(t+1,j-d,s+1) if j-d>=0 else [0]*PN)
    inv3=pow(3,-1,PN)
    for a in range(1,N,2):
        for d in range(3):
            m=pow(inv3,d,PN)
            fp=dft(parents[d],(m*a)%PN)
            fm=dft(parents[d],(m*(a+N))%PN)
            x=(abs(fp)**2-abs(fm)**2)/4.0
            xs[d].append(x)
    return [[sum(xs[e][i]*xs[f][i] for i in range(len(xs[0]))) for f in range(3)] for e in range(3)]

sys.path.insert(0,str(ROOT/'research_cross_terms_20260912'))
import probe
from exact_moment import cyclic_correlation_exact,moments_from_correlation
from functools import lru_cache

@lru_cache(None)
def G(t,j,s,d):
    if not (1<=s<=t and d>=0 and 0<=j-d<=t): return 0
    if d==0:
        c,_=cyclic_correlation_exact(actual_filter(t,j,s))
        return int(moments_from_correlation(c)['primitive_fourth_moment'])
    q=1<<s; H=q//2
    f=actual_filter(t,j,s); g=actual_filter(t,j-d,s)
    inv=pow(pow(3,d,q),-1,q)
    U=[f[(inv*z)%q] for z in range(q)]
    Z=[sum(U[u]*g[(u+b)%q] for u in range(q)) for b in range(q)]
    DZ=[Z[b]-Z[(b+H)%q] for b in range(q)]
    return H*sum(DZ[b]**2 for b in range(H))

def H0(t,j,s):
    row=probe.panel(t+1,j,s+1,False)
    from fractions import Fraction
    return (1<<(s-1))*float(Fraction(row['reflection_plus_norm']))

def Hd(t,j,s,d):
    if d==0:return H0(t,j,s)
    lhs=G(t+1,j,s+1,d)
    base=2*(G(t,j,s,d)+G(t,j,s,d+1)+G(t,j-1,s,d-1)+G(t,j-1,s,d))
    return (lhs-base)/8

def residual_K(t,j,s):
    return [[H0(t,j,s),Hd(t,j,s,1),Hd(t,j,s,2)],
            [Hd(t,j,s,1),H0(t,j-1,s),Hd(t,j-1,s,1)],
            [Hd(t,j,s,2),Hd(t,j-1,s,1),H0(t,j-2,s)]]

rows=[]; max_abs=0.0; max_rel=0.0
for t in range(5,11):
  for s in range(2,min(t,5)+1):
    for j in range(2,t+1):
      A=direct_K(t,j,s);B=residual_K(t,j,s)
      errs=[]
      for e in range(3):
        for f in range(3):
          err=abs(A[e][f]-B[e][f]); max_abs=max(max_abs,err)
          scale=max(1.0,abs(B[e][f]));max_rel=max(max_rel,err/scale);errs.append(err/scale)
      rows.append({'t':t,'j':j,'s':s,'max_rel_error':max(errs)})
assert max_rel < 2e-8
out={'status':'PASS numerical direct-DFT cross-check only','cases':len(rows),'max_abs_error':max_abs,'max_rel_error':max_rel,'rows':rows}
(HERE/'DIRECT_CROSSCHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
