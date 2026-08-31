"""
SUREKLI KESIR BULGUSUNUN ZERO-TRUST DENETIMI (kendi isim).
Doktrin: kirmaya calis.

S1: Her konverjant q_n icin uzun ortak blok VAR MI? (yoksa sonsuzluk cokuyor)
S2: r/q orani sabit mi, yoksa sonuyor mu?
S3: Controller'a mi ozgu, yoksa genel zero-critical kritik-log kelimelerde de var mi?
"""
from decimal import Decimal, getcontext
import math, random
getcontext().prec=60
A=Decimal(3).ln()/Decimal(2).ln()
N=400000
F=[int((A*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]

# konverjantlar
x=A; cf=[]; convs=[]; p0,q0,p1,q1=0,1,1,0
for i in range(22):
    ai=int(x); cf.append(ai)
    p0,p1=p1,ai*p1+p0; q0,q1=q1,ai*q1+q0
    convs.append(q1)
    fr=x-ai
    if fr==0: break
    x=1/fr

def controller(kappa_str, n=N):
    KAP=Decimal(kappa_str)
    def esik(s,m):
        if s<=0: return True
        num,den = KAP.as_integer_ratio()
        return (1<<(den*s)) <= m**num
    a=[];s=0
    for k in range(n):
        m=max(2,k+1)
        d=1 if (g[k]==2 and esik(s,m)) else -1
        a.append(g[k]-d); s+=d
    return a

def en_uzun_blok(w,q):
    best=cur=0; st=0; bst=0
    L=len(w)-q
    for k in range(L):
        if w[k]==w[k+q]:
            if cur==0: st=k
            cur+=1
            if cur>best: best=cur; bst=st
        else: cur=0
    return bst,best

a=controller('1.053')
print("S1/S2 — HER konverjantta uzun blok var mi? r/q orani?\n")
print(f"{'n':>3} {'q_n':>8} {'cf sonraki':>11} {'en uzun blok r':>15} {'r/q':>8} {'A(W)':>9} {'log2 n0>=':>11}")
oranlar=[]
for i,q in enumerate(convs):
    if q<3 or q>N//3: continue
    st,L=en_uzun_blok(a,q)
    if L<2: 
        print(f"{i:>3} {q:>8} {cf[i+1] if i+1<len(cf) else '-':>11} {L:>15} {'-':>8}")
        continue
    AW=sum(a[st:st+L]); v=st+q
    alt=AW-1.053*math.log2(v+L)
    oranlar.append(L/q)
    print(f"{i:>3} {q:>8} {cf[i+1] if i+1<len(cf) else '-':>11} {L:>15,} {L/q:>8.3f} {AW:>9,} {alt:>11,.0f}")

print(f"\n  r/q oranlari: min={min(oranlar):.3f} max={max(oranlar):.3f}")
print(f"  -> {'oran SIFIRA GITMIYOR (iyi)' if min(oranlar)>0.05 else 'DIKKAT: bazi q icin oran cok kucuk'}")

print("\nS3 — controller'a mi ozgu? Farkli kappa ve RASTGELE zero-critical:")
print(f"{'kelime':>26} {'q=665 blok':>12} {'q=15601 blok':>14}")
for kap in ('1.053','1.2','1.5','2.0'):
    w=controller(kap)
    _,b1=en_uzun_blok(w,665); _,b2=en_uzun_blok(w,15601)
    print(f"{'controller kappa='+kap:>26} {b1:>12,} {b2:>14,}")
random.seed(3)
rnd=[random.choice([t for t in (1,2,3) if t!=g[k]]) for k in range(N)]
_,b1=en_uzun_blok(rnd,665); _,b2=en_uzun_blok(rnd,15601)
print(f"{'rastgele zero-critical':>26} {b1:>12,} {b2:>14,}")
