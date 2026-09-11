"""
CP20 TASK 8B2 D1 — SPARSE-INJURY GEOMETRY, ZERO-TRUST DENETIM.
Arsivin engine'lerine bakilmadi.

2026-09-11 clarification: the final finite-window comparison in the historical
version mixed a global finite minimum with an asymptotic liminf and could print
'TUTARSIZ'. It is retained below only as a finite diagnostic. The actual
liminf diagnostic is the tail test in 03_madde10_kuyruk.py.
"""
import math, random
from decimal import Decimal, getcontext
getcontext().prec=60
ALPHA=Decimal(3).ln()/Decimal(2).ln()

def seq(a):
    A=[0];B=[0]
    for k,ak in enumerate(a):
        B.append(3*B[k]+2**A[k]); A.append(A[k]+ak)
    r=[0]; R=[]
    for k in range(1,len(a)+1):
        m=1<<A[k]
        rk=(-B[k]*pow(pow(3,k,m),-1,m))%m
        r.append(rk)
        c=(3**k*rk+B[k])//m
        R.append(rk if c%2==1 else rk+m)
    return r,R,A,B

print("MADDE 1-2 — r_{k+1}=r_k+m_k 2^{A_k}, 0<=m_k<2^{a_k}, telescoping\n")
random.seed(21); t=f1=f2=f3=0
for _ in range(600):
    a=[random.randint(1,4) for _ in range(random.randint(6,26))]
    r,R,A,B=seq(a)
    for k in range(len(a)):
        num=r[k+1]-r[k]; t+=1
        if num%(1<<A[k])!=0: f1+=1
        m=num//(1<<A[k])
        if not (0<=m<(1<<a[k])): f2+=1
        if (m==0)!=(r[k+1]==r[k]): f3+=1
    for k in range(1,len(a)+1):
        s=sum(((r[j+1]-r[j])//(1<<A[j]))*(1<<A[j]) for j in range(k))
        if s!=r[k]: f2+=1
print(f"  test {t:,}   m_k tam sayi degil: {f1}   aralik ihlali: {f2}   m=0<=>injury yok ihlali: {f3}")
print(f"  -> {'DOGRULANDI' if f1==f2==f3==0 else 'IHLAL'}")

N=6000
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]
def controller(kappa_num,kappa_den,n=N):
    a=[];s=0
    for k in range(n):
        m=max(2,k+1)
        ok=True if s<=0 else (1<<(kappa_den*s))<=m**kappa_num
        d=1 if (g[k]==2 and ok) else -1
        a.append(g[k]-d); s+=d
    return a

print("\nMADDE 3 — kritik-log => a_k EVENTUALLY BOUNDED")
for kn,kd,lbl in ((1053,1000,'1.053'),(3,2,'1.5'),(2,1,'2.0')):
    a=controller(kn,kd)
    print(f"  kappa={lbl:<6} max a_k={max(a)} son1000 max={max(a[-1000:])} alfabe={sorted(set(a))}")

print("\nMADDE 4-5 — plato ve sandwich")
a=controller(1053,1000); r,R,A,B=seq(a)
inj=[k for k in range(len(a)) if r[k+1]!=r[k]]
print(f"  injury sayisi: {len(inj)}, ilk 12: {inj[:12]}")
t=f=0
for j in range(len(inj)-1):
    tj,tj1=inj[j],inj[j+1]
    for k in range(tj+1,tj1+1):
        t+=1
        if r[k]!=r[tj+1]: f+=1
        if not ((1<<A[tj])<=r[k]<(1<<A[tj+1])): f+=1
print(f"  plato noktasi {t:,} ihlal {f} -> {'DOGRULANDI' if f==0 else 'IHLAL'}")

print("\nMADDE 8 — rho_r plato uzerinde monoton azalan")
t=f=0
for j in range(len(inj)-1):
    tj,tj1=inj[j],inj[j+1]; ks=list(range(tj+1,tj1+1))
    if len(ks)<2: continue
    rho=[math.log(1+r[k])/k for k in ks]; t+=1
    if any(rho[i]<rho[i+1]-1e-15 for i in range(len(rho)-1)): f+=1
    if abs(min(rho)-rho[-1])>1e-15: f+=1
print(f"  plato {t:,} monotonluk/min ihlali {f} -> {'DOGRULANDI' if f==0 else 'IHLAL'}")

print("\nMADDE 6 — trough asimptotigi rho_r(t_{j+1}) = ln3*t_j/t_{j+1}+O(log t_j/t_{j+1})")
ln3=math.log(3)
for j in range(len(inj)-6,len(inj)-1):
    tj,tj1=inj[j],inj[j+1]
    obs=math.log(1+r[tj1])/tj1; pred=ln3*tj/tj1
    print(f"  j={j:>4} t_j={tj:>6} t_j+1={tj1:>6} obs={obs:.6f} pred={pred:.6f} fark={obs-pred:+.6f}")

print("\nMADDE 10 — finite diagnostic; NOT an asymptotic liminf certificate")
oran=[inj[j+1]/inj[j] for j in range(1,len(inj)-1)]
tj_ratio=[inj[j]/inj[j+1] for j in range(1,len(inj)-1)]
rhoall=[math.log(1+r[k])/k for k in range(max(1,len(inj)//2),len(r))]
print(f"  finite t_{{j+1}}/t_j range: [{min(oran):.4f}, {max(oran):.4f}]")
print(f"  finite min t_j/t_{{j+1}}={min(tj_ratio):.4f}; ln3*min={ln3*min(tj_ratio):.4f}")
print(f"  finite window min rho={min(rhoall):.4f}")
print("  NO VERDICT from comparing these two global finite minima: they may occur at different indices.")
print("  Use 03_madde10_kuyruk.py, which compares aligned tail/trough quantities and shows the discrepancy tends to 0.")
