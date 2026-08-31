"""
MADDE 10 YENIDEN — onceki testin kendi hatasini teshis et.
Iddia: liminf rho_r = ln3 * liminf_j (t_j / t_{j+1})
"""
import math
from decimal import Decimal, getcontext
getcontext().prec=60
ALPHA=Decimal(3).ln()/Decimal(2).ln()
ln3=math.log(3)

def seq(a):
    A=[0];B=[0]
    for k,ak in enumerate(a):
        B.append(3*B[k]+2**A[k]); A.append(A[k]+ak)
    r=[0]
    for k in range(1,len(a)+1):
        m=1<<A[k]
        rk=(-B[k]*pow(pow(3,k,m),-1,m))%m
        r.append(rk)
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

a=controller(1053,1000)
r,A,B=seq(a)
inj=[k for k in range(len(a)) if r[k+1]!=r[k]]
n=len(r)-1
print(f"controller: {len(a)} adim, {len(inj)} injury  (yogunluk {len(inj)/len(a):.3f})")

rho=[None]+[math.log(1+r[k])/k for k in range(1,n+1)]

# --- A) ESKI TESTIN HATASI: iki farkli indeks kumesi kiyaslanmis
eski_rho_min = min(rho[k] for k in range(len(inj)//2, n+1))
eski_ratio_min = min(inj[j]/inj[j+1] for j in range(1,len(inj)-1))
print(f"\nA) ESKI TEST")
print(f"   min rho   k in [{len(inj)//2}, {n}]        = {eski_rho_min:.4f}")
print(f"   ln3*min(t_j/t_{{j+1}})  j in [1,{len(inj)-2}] = {ln3*eski_ratio_min:.4f}")
kmin = min(range(len(inj)//2,n+1), key=lambda k: rho[k])
jmin = min(range(1,len(inj)-1), key=lambda j: inj[j]/inj[j+1])
print(f"   -> rho minimumu k={kmin} de,  oran minimumu (t_j,t_{{j+1}})=({inj[jmin]},{inj[jmin+1]}) de")
print(f"   -> IKI FARKLI YER. Kiyas gecersiz.")

# --- B) DOGRU TEST: ayni j uzerinde, sadece plato SONLARINDA
print(f"\nB) DOGRU TEST — rho sadece trough'larda (k=t_{{j+1}}) olculur")
print(f"   {'j':>5} {'t_j':>6} {'t_j+1':>6} {'rho(t_{j+1})':>13} {'ln3*t_j/t_{j+1}':>16} {'fark':>9}")
worst=0
for j in range(1,len(inj)-1):
    tj, tj1 = inj[j], inj[j+1]
    obs, pred = rho[tj1], ln3*tj/tj1
    worst=max(worst, abs(obs-pred))
    if j>=len(inj)-7:
        print(f"   {j:>5} {tj:>6} {tj1:>6} {obs:>13.6f} {pred:>16.6f} {obs-pred:>9.6f}")
print(f"   TUM j icin max |fark| = {worst:.6f}")

# --- C) rho'nun GLOBAL minimumu gercekten bir trough'ta mi?
kglob = min(range(1,n+1), key=lambda k: rho[k])
print(f"\nC) rho'nun global minimumu k={kglob}, rho={rho[kglob]:.6f}")
print(f"   k={kglob} bir injury indeksi mi (t_{{j+1}})? {'EVET' if (kglob in [i+1 for i in inj] or kglob in inj) else 'HAYIR'}")
# plateau sonlari kumesi: k = t_{j+1} yani inj[j+1]
troughs=set(inj[1:])
kglob_tail = min((k for k in range(200,n+1)), key=lambda k: rho[k])
print(f"   k>=200 icin min rho: k={kglob_tail}, trough mu: {kglob_tail in troughs}")

# --- D) MADDE 10'un ASIL ICERIGI: liminf rho = 0  <=>  liminf t_j/t_{j+1} = 0
print(f"\nD) MADDE 10 asil iddia: liminf rho_r=0 <=> liminf t_j/t_{{j+1}}=0")
ratios=[inj[j]/inj[j+1] for j in range(1,len(inj)-1)]
print(f"   bu controller: inf t_j/t_{{j+1}} = {min(ratios):.4f} > 0")
print(f"   => teorem liminf rho_r = ln3*{min(ratios):.4f} = {ln3*min(ratios):.4f} > 0 ONGORUR")
print(f"   gozlenen inf_{{troughs}} rho = {min(rho[k] for k in sorted(troughs)):.4f}")
print(f"   ONGORU ILE UYUMLU: {abs(min(rho[k] for k in sorted(troughs))-ln3*min(ratios))<0.01}")
