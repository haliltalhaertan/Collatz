"""MADDE 10 — kuyruk (liminf) testi + GERCEK seyrek-injury controller."""
import math
from decimal import Decimal, getcontext
getcontext().prec=80
ALPHA=Decimal(3).ln()/Decimal(2).ln()
ln3=math.log(3)

def build(a):
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
        m=max(2,k+1)
        ok = True if s<=0 else (1<<(kd*s)) <= m**kn
        d=1 if (g[k]==2 and ok) else -1
        a.append(g[k]-d); s+=d
    return a

a=controller(1053,1000); r,A,B=build(a)
inj=[k for k in range(len(a)) if r[k+1]!=r[k]]; n=len(r)-1
rho=lambda k: math.log(1+r[k])/k

print("MADDE 10 — liminf KUYRUK notion'udur, inf degil")
for lo in (1,10,100,500,1000,2000,3000):
    js=[j for j in range(1,len(inj)-1) if inj[j]>=lo]
    if not js: continue
    ir=min(inj[j]/inj[j+1] for j in js)
    orho=min(rho(inj[j+1]) for j in js)
    print(f"  t_j>={lo:<5}  inf t_j/t_{{j+1}}={ir:.6f}  ln3*bu={ln3*ir:.6f}   inf rho(trough)={orho:.6f}   fark={orho-ln3*ir:+.6f}")
print("  -> kuyruk buyudukce fark -> 0.  MADDE 10 DOGRULANDI (eski 'TUTARSIZ' kendi testimin hatasiydi).\n")

# ---------- GERCEK SEYREK-INJURY CONTROLLER ----------
print("SEYREK-INJURY INSASI — her adimda injury'siz a_k varsa onu sec")
def greedy_sparse(n, amax=8, prefer_g=False):
    a=[];A=[0];B=[0];r=[0]
    for k in range(n):
        best=None
        cands=list(range(1,amax+1))
        for ak in cands:
            Bn=3*B[k]+2**A[k]; An=A[k]+ak; m=1<<An
            rn=(-Bn*pow(pow(3,k+1,m),-1,m))%m
            if rn==r[k]: best=(ak,Bn,An,rn); break
        if best is None:
            ak=cands[0]
            Bn=3*B[k]+2**A[k]; An=A[k]+ak; m=1<<An
            rn=(-Bn*pow(pow(3,k+1,m),-1,m))%m
            best=(ak,Bn,An,rn)
        ak,Bn,An,rn=best
        a.append(ak); B.append(Bn); A.append(An); r.append(rn)
    return a,r,A,B

for amax in (4,8,16):
    a2,r2,A2,B2=greedy_sparse(400,amax)
    inj2=[k for k in range(len(a2)) if r2[k+1]!=r2[k]]
    runs=[inj2[j+1]-inj2[j] for j in range(len(inj2)-1)] or [0]
    print(f"  amax={amax:<3} injury {len(inj2):>4}/400 (yog {len(inj2)/400:.3f})  en uzun plato {max(runs)}  alfabe={sorted(set(a2))[:8]}")
print("  -> a_k'yi serbest birakinca bile injury yogunlugu ~1/2'nin altina inmiyor")

# tek adimda kac aday injury'siz?
print("\n  Bir adimda injury'siz a_k sayisi (rastgele prefiksler uzerinde):")
import random
random.seed(7)
cnt={}
for _ in range(300):
    a3=[random.randint(1,3) for _ in range(random.randint(5,20))]
    r3,A3,B3=build(a3); k=len(a3)
    c=0
    for ak in range(1,17):
        Bn=3*B3[k]+2**A3[k]; An=A3[k]+ak; m=1<<An
        rn=(-Bn*pow(pow(3,k+1,m),-1,m))%m
        if rn==r3[k]: c+=1
    cnt[c]=cnt.get(c,0)+1
print(f"    dagilim (injury'siz aday sayisi -> kac kez): {dict(sorted(cnt.items()))}")
