from __future__ import annotations
from math import comb, cos, sin, pi
from random import Random
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def walk(h,m):
    x=h;k=0
    for _ in range(m):
        e=x&1;k+=e;x=(3*x+1)//2 if e else x//2
    return x,k

def source_hist(m,k,s):
    q=1<<s;p=[0]*q
    for h in range(1,1<<m,2):
        y,w=walk(h,m)
        if w==k:p[y%q]+=1
    return p

def even_transfer(P,c,s):
    N=1<<(s+1);q=1<<s;c%=N
    return [P[(2*z)%N]+P[(2*z-c)%N] for z in range(q)]

def odd_transfer(P,c,s):
    N=1<<(s+1);q=1<<s;c%=N;r=pow(3,-1,N)
    return [P[(r*(2*z-1))%N]+P[(r*(2*z-1)-c)%N] for z in range(q)]

def corr(v):
    n=len(v);return [sum(v[u]*v[(u+d)%n] for u in range(n)) for d in range(n)]

def mixed_plus_numerators(x):
    n=len(x);q=n//2;h0=q//2
    x0=[x[2*u] for u in range(q)];x1=[x[2*u+1] for u in range(q)]
    B=[sum(x0[u]*x1[(u+b)%q] for u in range(q)) for b in range(q)]
    Z=[B[b]-B[(b+h0)%q] for b in range(q)]
    return [Z[h]+Z[(-h-1)%q] for h in range(h0)]

def first_level_direct(x,y):
    n=len(x);H=n//2;cx=corr(x);cy=corr(y)
    DX=[cx[d]-cx[d+H] for d in range(H)];DY=[cy[d]-cy[d+H] for d in range(H)]
    odd=range(1,H,2)
    return (sum(DX[d]*DY[d] for d in odd),sum(DX[d]**2 for d in odd),sum(DY[d]**2 for d in odd))

def dft(v):
    n=len(v);out=[]
    for a in range(n):
        z=0j
        for u,x in enumerate(v):
            th=-2*pi*a*u/n;z += x*complex(cos(th),sin(th))
        out.append(z)
    return out

def exact_source_checks():
    checks=0
    for m in range(1,11):
        for s in range(1,min(6,m+1)+1):
            N=1<<(s+1);zero=[0]*N
            for k in range(1,m+2):
                lhs=source_hist(m+1,k,s)
                pk=source_hist(m,k,s+1) if k<=m else zero
                pm=source_hist(m,k-1,s+1) if 1<=k-1<=m else zero
                rhs=[a+b for a,b in zip(even_transfer(pk,pow(3,k,N),s),odd_transfer(pm,pow(3,k-1,N),s))]
                assert lhs==rhs
                assert sum(lhs)==comb(m,k-1)
                checks+=1
    return checks

def mixed_plus_checks():
    rng=Random(20260912);checks=0
    for s in range(2,7):
        n=1<<s
        for _ in range(50):
            x=[rng.randrange(5) for _ in range(n)];y=[rng.randrange(6) for _ in range(n)]
            G,S,T=first_level_direct(x,y)
            xp=mixed_plus_numerators(x);yp=mixed_plus_numerators(y)
            assert G==sum(a*b for a,b in zip(xp,yp))
            assert S==sum(a*a for a in xp)
            assert T==sum(b*b for b in yp)
            checks+=1
    return checks

def fourier_transfer_checks():
    rng=Random(3);checks=0;maxerr=0.0
    for s in range(1,6):
        N=1<<(s+1);q=1<<s
        for _ in range(20):
            P=[rng.randrange(5) for _ in range(N)];c=rng.randrange(1,N,2)
            Ph=dft(P);Eh=dft(even_transfer(P,c,s));Oh=dft(odd_transfer(P,c,s))
            for a in range(q):
                z=complex(cos(-2*pi*a*c/N),sin(-2*pi*a*c/N))
                predE=((1+z)*Ph[a]+(1-z)*Ph[a+q])/2
                eta=complex(cos(-2*pi*a/N),sin(-2*pi*a/N))
                z2=complex(cos(-2*pi*3*a*c/N),sin(-2*pi*3*a*c/N))
                A=Ph[(3*a)%N];B=Ph[((3*a)%N+q)%N]
                predO=eta*((1+z2)*A+(z2-1)*B)/2
                maxerr=max(maxerr,abs(Eh[a]-predE),abs(Oh[a]-predO));checks+=2
    assert maxerr<1e-9
    return checks,maxerr

def main():
    ec=exact_source_checks();mc=mixed_plus_checks();fc,err=fourier_transfer_checks()
    out={'status':'PASS','source_transfer_exact_checks':ec,'first_level_mixed_plus_exact_checks':mc,
         'fourier_transfer_numeric_coeff_checks':fc,'max_fourier_numeric_error':err,
         'same_session_check':True,'independent_agent_audit':False}
    (HERE/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
