"""Second implementation check for shift-valuation / lift-Haar identities.

No imports from the repository research modules. Uses scalar loops and a direct complex DFT
only as a normalization cross-check; the main theorem is algebraic and the primary code is integer-only.
This is NOT an independent agent audit: it is a separate implementation in the same assistant session.
"""
from math import comb, cos, sin, pi
from random import Random
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def walk(x,n):
    w=0
    for _ in range(n):
        e=x&1;w+=e;x=(3*x+1)//2 if e else x//2
    return x,w

def corr(v,w=None):
    if w is None:w=v
    n=len(v);return [sum(v[u]*w[(u+d)%n] for u in range(n)) for d in range(n)]

def dft(v):
    n=len(v); out=[]
    for a in range(n):
        z=0j
        for u,x in enumerate(v):
            ang=-2*pi*a*u/n
            z += x*complex(cos(ang),sin(ang))
        out.append(z)
    return out

def stats(x,y):
    n=len(x);H=n//2;cx=corr(x);cy=corr(y)
    DX=[cx[d]-cx[d+H] for d in range(H)];DY=[cy[d]-cy[d+H] for d in range(H)]
    if not DX[0] or not DY[0]:return None
    A=sum(DX[d]*DY[d] for d in range(H))/(DX[0]*DY[0])
    lev=[]
    for ell in range(1,n.bit_length()-1):
        step=1<<(ell-1); inds=list(range(step,H,2*step))
        if not inds:break
        lev.append(sum(DX[d]*DY[d] for d in inds)/(DX[0]*DY[0]))
    return A,lev,DX,DY

def spectral_alignment(x,y):
    n=len(x);H=n//2;X=dft(x);Y=dft(y)
    odd=range(1,n,2)
    sx=sum(abs(X[a])**2 for a in odd);sy=sum(abs(Y[a])**2 for a in odd)
    if sx==0 or sy==0:return None
    return H*sum(abs(X[a])**2*abs(Y[a])**2 for a in odd)/(sx*sy)

def arbitrary_checks():
    rng=Random(20260912);cases=0;maxerr=0.0
    for n in (4,8,16,32):
        for _ in range(20):
            x=[rng.randrange(0,8) for _ in range(n)];y=[rng.randrange(0,7) for _ in range(n)]
            st=stats(x,y);sp=spectral_alignment(x,y)
            if st is None or sp is None:continue
            A,lev,_,_=st
            err=abs(A-sp);maxerr=max(maxerr,err)
            assert err<1e-8*max(1,abs(A),abs(sp))
            assert abs(A-(1+sum(lev)))<1e-12
            cases+=1
    return cases,maxerr

def tail_channels(t,j,s):
    q=1<<(s-1);H=q//2
    g=[choose(t-s,j-k) for k in range(s+1)]
    wt=[walk(u,s-1)[1] for u in range(q)]
    f0=[g[k] for k in wt];f1=[g[k+1] for k in wt]
    A0=corr(f0);A1=corr(f1)
    inv3=pow(3,-1,q)
    U=[f0[(inv3*z)%q] for z in range(q)];B=corr(U,f1)
    d0=[A0[b]-A0[(b+H)%q] for b in range(q)];d1=[A1[b]-A1[(b+H)%q] for b in range(q)];db=[B[b]-B[(b+H)%q] for b in range(q)]
    NB=sum(db[h]**2 for h in range(H));O=sum(db[(3*h+2)%q]*db[(-3*h-1)%q] for h in range(H));Np=(NB+O)/2
    return q,H,d0,d1,NB,Np

def block_formula_check(t,j,s):
    q,H,d0,d1,NB,Np=tail_channels(t,j,s)
    Bs=[]
    for r in range(s-1):
        Bs.append(sum(d0[h]*d1[(3*h)%q] for h in range(0,H,1<<r)))
    assert Bs[0]==NB
    g=[choose(t-s,j-k) for k in range(s+1)];wt=[walk(u,s-1)[1] for u in range(q)];f0=[g[k] for k in wt];f1=[g[k+1] for k in wt]
    F0=dft(f0);F1=dft(f1)
    for r,B in enumerate(Bs):
        M=q>>r; total=0.0
        for a in range(1,q,2):
            for b in range(1,q,2):
                if (a+3*b)%M==0:
                    total += abs(F0[a])**2*abs(F1[b])**2
        pred=2*total/(q*(1<<r))
        assert abs(pred-B)<1e-7*max(1,abs(B))
    parent=[choose(t-s,j-walk(u,s)[1]) for u in range(1<<s)]
    C=corr(parent);HH=1<<(s-1);D=[C[d]-C[d+HH] for d in range(HH)]
    odd_energy=sum(D[d]**2 for d in range(1,HH,2))
    assert abs(odd_energy-4*Np)<1e-9
    return len(Bs)

def actual_grid():
    cases=blocks=0
    for t in range(4,9):
        for s in range(3,min(t,6)+1):
            for j in range(t+1):
                blocks += block_formula_check(t,j,s);cases+=1
    return cases,blocks

def main():
    ac,err=arbitrary_checks();tc,bc=actual_grid()
    out={'status':'PASS','same_session_second_implementation':True,'not_independent_agent_audit':True,
         'arbitrary_vector_alignment_cases':ac,'max_direct_DFT_error':err,
         'actual_filter_block_formula_cases':tc,'actual_filter_cumulative_levels_checked':bc}
    (HERE/'INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
