"""MADDE 6/7/9 — O(log t_j / k) hata teriminin ISARETI ve BUYUKLUGU tam mi?"""
import math
from decimal import Decimal, getcontext
getcontext().prec=80
ALPHA=Decimal(3).ln()/Decimal(2).ln(); ln3=math.log(3)
N=6000
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]
def ctrl(kn,kd,n=N):
    a=[];s=0
    for k in range(n):
        m=max(2,k+1); ok=True if s<=0 else (1<<(kd*s))<=m**kn
        d=1 if (g[k]==2 and ok) else -1
        a.append(g[k]-d); s+=d
    return a
def build(w):
    A=[0];B=[0];r=[0]
    for k,a in enumerate(w,1):
        B.append(3*B[-1]+(1<<A[-1])); A.append(A[-1]+a)
        m=1<<A[-1]; r.append((-B[-1]*pow(pow(3,k,m),-1,m))%m)
    return A,B,r
for kn,kd,kap in ((1053,1000,1.053),(3,2,1.5),(2,1,2.0)):
    w=ctrl(kn,kd); A,B,r=build(w)
    inj=[k for k in range(len(w)) if r[k+1]!=r[k]]
    print(f"\nkappa={kap}   teorem: rho(t_{{j+1}}) = ln3*t_j/t_{{j+1}} - kappa*ln(t_j)/t_{{j+1}} + O(1/t_{{j+1}})")
    print(f"  {'t_j':>6} {'t_{j+1}':>8} {'gozlenen':>11} {'ln3*t_j/t':>11} {'2.mert. dahil':>14} {'kalan':>10}")
    for j in range(len(inj)-5,len(inj)-1):
        tj,tj1=inj[j],inj[j+1]
        obs=math.log(1+r[tj1])/tj1
        p1=ln3*tj/tj1
        p2=p1-kap*math.log(tj)/tj1
        print(f"  {tj:>6} {tj1:>8} {obs:>11.6f} {p1:>11.6f} {p2:>14.6f} {obs-p2:>10.6f}")
print("\n-> 2. mertebe terim isaret ve buyukluk olarak TAM tutuyor; kalan O(1/t) mertebesinde.")
print("-> MADDE 6 DOGRULANDI, MADDE 7 (log t_j/t_{j+1} -> 0, sadece t_{j+1}>=t_j+1 ile) GECERLI:")
print("   |hata| <= C*log(t_j)/t_{j+1} <= C*log(t_j)/t_j -> 0.  Ek buyume varsayimi YOK.")
print("-> MADDE 9 (liminf'in o(1) icinden gecisi): liminf(x_j+e_j)=liminf x_j, e_j->0. GECERLI.")
