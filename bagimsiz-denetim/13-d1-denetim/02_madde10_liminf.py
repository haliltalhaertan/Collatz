"""MADDE 10 — historical finite diagnostic and diagnosis of its own flaw.

The old calculation compared minima taken over different finite index sets and
could end with `UYUMLU: False`. That is not a counterexample to an asymptotic
liminf identity. This file now reports the mismatch diagnostically only.
The aligned tail/trough check is `03_madde10_kuyruk.py` and is the current
numerical diagnostic.
"""
import math
from decimal import Decimal,getcontext
getcontext().prec=60
ALPHA=Decimal(3).ln()/Decimal(2).ln(); ln3=math.log(3)

def seq(a):
    A=[0];B=[0]
    for k,ak in enumerate(a):
        B.append(3*B[k]+2**A[k]); A.append(A[k]+ak)
    r=[0]
    for k in range(1,len(a)+1):
        m=1<<A[k]
        r.append((-B[k]*pow(pow(3,k,m),-1,m))%m)
    return r,A,B

N=6000
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]
def controller(kn,kd,n=N):
    a=[];s=0
    for k in range(n):
        m=max(2,k+1); ok=True if s<=0 else (1<<(kd*s))<=m**kn
        d=1 if (g[k]==2 and ok) else -1
        a.append(g[k]-d); s+=d
    return a

a=controller(1053,1000); r,A,B=seq(a)
inj=[k for k in range(len(a)) if r[k+1]!=r[k]]; n=len(r)-1
rho=[None]+[math.log(1+r[k])/k for k in range(1,n+1)]
print(f"controller: {len(a)} adim, {len(inj)} injury (yogunluk {len(inj)/len(a):.3f})")

print("\nA) ESKI GLOBAL-FINITE TEST — VERDICT DEGIL")
eski_rho_min=min(rho[k] for k in range(max(1,len(inj)//2),n+1))
eski_ratio_min=min(inj[j]/inj[j+1] for j in range(1,len(inj)-1))
kmin=min(range(max(1,len(inj)//2),n+1),key=lambda k:rho[k])
jmin=min(range(1,len(inj)-1),key=lambda j:inj[j]/inj[j+1])
print(f"   finite min rho={eski_rho_min:.6f} at k={kmin}")
print(f"   ln3*finite min ratio={ln3*eski_ratio_min:.6f} at pair ({inj[jmin]},{inj[jmin+1]})")
print("   These extrema occur at different indices; comparing them is not a liminf test.")

print("\nB) ALIGNED TROUGH DIAGNOSTIC")
print(f"   {'j':>5} {'t_j':>6} {'t_j+1':>6} {'rho(t_j+1)':>13} {'ln3*t_j/t_j+1':>16} {'fark':>10}")
for j in range(max(1,len(inj)-7),len(inj)-1):
    tj,tj1=inj[j],inj[j+1]; obs=rho[tj1]; pred=ln3*tj/tj1
    print(f"   {j:>5} {tj:>6} {tj1:>6} {obs:>13.6f} {pred:>16.6f} {obs-pred:>+10.6f}")

print("\nC) CURRENT STATUS")
print("   No asymptotic verdict is inferred from a single finite global minimum.")
print("   Run 03_madde10_kuyruk.py for increasing tail cutoffs; there the aligned")
print("   trough discrepancy is observed to tend toward zero, matching the report correction.")
