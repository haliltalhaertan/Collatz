from __future__ import annotations
from functools import lru_cache
from math import comb
from fractions import Fraction
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent

def C(n,k): return comb(n,k) if 0<=k<=n else 0
def delta(t,l): return C(t-1,l)-C(t-1,l-1)
def cp(p): return tuple(sorted(tuple(x) for x in p))
@lru_cache(None)
def inv3(n,d):
    N=1<<n; return pow(pow(3,d,N),-1,N)
@lru_cache(None)
def p3(n,d): return pow(3,d,1<<n)
ROOT=cp(((0,1),(0,1),(0,-1),(0,-1)))

@lru_cache(None)
def raw(t,j,n,Cp,pairs):
    N=1<<n; Cp%=N; pairs=cp(pairs)
    if n==1:
        z=1
        for d,e in pairs:z*=delta(t,j-d)
        return -z if Cp&1 else z
    q=N//2;r=pow(3,-1,q);c=(4*r-1)%N
    mus=[e*inv3(n,d)%N for d,e in pairs]
    total=0
    for mask in range(16):
        if (Cp+mask.bit_count())&1:continue
        sm=0;new=[]
        for i,(d,e) in enumerate(pairs):
            if mask>>i&1:sm+=mus[i];new.append((d+1,e))
            else:new.append((d,e))
        num=Cp+c*sm; assert num%2==0
        total+=2*raw(t-1,j,n-1,(num//2)%q,cp(new))
    return total

def norm(j,n,Cp,pairs):
    N=1<<n;sgn=1;pairs=list(pairs)
    h=min(d for d,e in pairs)
    if h:
        Cp=Cp*p3(n,h)%N;j-=h;pairs=[(d-h,e) for d,e in pairs]
    pairs=cp(pairs);Cp%=N;half=N//2
    if Cp>=half:Cp-=half;sgn=-sgn
    ar=(-Cp)%N;asgn=1
    if ar>=half:ar-=half;asgn=-1
    ap=cp((d,-e) for d,e in pairs)
    if (ar,ap)<(Cp,pairs):sgn*=asgn;Cp,pairs=ar,ap
    return sgn,j,Cp,pairs

@lru_cache(None)
def qq(t,j,n,Cp,pairs):
    N=1<<n
    if n==1:
        z=1
        for d,e in pairs:z*=delta(t,j-d)
        return z
    q=N//2;r=pow(3,-1,q);c=(4*r-1)%N
    mus=[e*inv3(n,d)%N for d,e in pairs]
    ch={}
    for mask in range(16):
        if (Cp+mask.bit_count())&1:continue
        sm=0;new=[]
        for i,(d,e) in enumerate(pairs):
            if mask>>i&1:sm+=mus[i];new.append((d+1,e))
            else:new.append((d,e))
        num=Cp+c*sm; assert num%2==0
        s,cj,cC,cP=norm(j,n-1,(num//2)%q,tuple(new))
        key=(t-1,cj,n-1,cC,cP)
        ch[key]=ch.get(key,0)+2*s
    return sum(coef*qq(*key) for key,coef in ch.items() if coef)

def quot(t,j,n,Cp,pairs=ROOT):
    s,j,Cp,pairs=norm(j,n,Cp,pairs);return s*qq(t,j,n,Cp,pairs)

def kw(u,s):
    k=0
    for _ in range(s):
        e=u&1;k+=e;u=(3*u+1)//2 if e else u//2
    return k

def dm4(t,j,s):
    v=[C(t-s,j-kw(u,s)) for u in range(1<<s)];n=len(v);H=n//2
    co=[sum(v[u]*v[(u+d)%n] for u in range(n)) for d in range(n)]
    return H*sum((co[d]-co[d+H])**2 for d in range(H))

def small():
    z=0
    for t in range(2,9):
      for s in range(1,min(t,5)+1):
       for j in range(t+1):
        raw.cache_clear();qq.cache_clear()
        a=raw(t,j,s,0,ROOT);b=quot(t,j,s,0);c=dm4(t,j,s)
        assert a==b==c,(t,j,s,a,b,c);z+=1
    return z

def counts(sel):
    o=[]
    for s in sel:
        t=2*s;j=round(t/1.584962500721156)
        qq.cache_clear();v=quot(t,j,s,0);ns=qq.cache_info().currsize
        o.append({'s':s,'states':ns,'direct':1<<s,'ratio':str(Fraction(ns,1<<s)),'value':str(v)})
    return o

def main():
    st=time.perf_counter();checks=small();ct=counts((4,8,12,16))
    out={'status':'PASS','small_exact_checks':checks,'selected_quotient_counts':ct,
         'independent_agent_audit':False,'same_session_implementation':True,
         'symmetries':['common offset','primitive half-character anti-periodicity','xi->-xi sign conjugation'],
         'elapsed_seconds':time.perf_counter()-st}
    (HERE/'CORE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
