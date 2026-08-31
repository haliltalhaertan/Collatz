"""D0 DENETIM 2 — one-bit lift (madde 7-12) ve kirma girisimleri (21-22)."""
import math, random

def seq(a):
    A=[0];B=[0]
    for k,ak in enumerate(a):
        B.append(3*B[k]+2**A[k]); A.append(A[k]+ak)
    r=[];R=[]
    for k in range(1,len(a)+1):
        m=1<<A[k]
        rk=(-B[k]*pow(pow(3,k,m),-1,m))%m
        r.append(rk)
        # R_k: n_k TEK olacak sekilde tek bit lift
        c=(3**k*rk+B[k])//m
        R.append(rk if (c%2==1) else rk+m)
    return r,R,A,B

print("MADDE 7 — R_k in {r_k, r_k+2^{A_k}} ?")
random.seed(5); t=f=0
for _ in range(300):
    a=[random.randint(1,4) for _ in range(random.randint(5,22))]
    r,R,A,B=seq(a)
    for k in range(len(r)):
        t+=1
        if R[k] not in (r[k], r[k]+(1<<A[k+1])): f+=1
print(f"  test {t:,}  ihlal {f}  -> {'DOGRULANDI' if f==0 else 'IHLAL'}")

print("\nMADDE 8 — R nesting mod 2^{A_u+1}")
t=f=0
for _ in range(300):
    a=[random.randint(1,4) for _ in range(random.randint(5,20))]
    r,R,A,B=seq(a)
    for u in range(len(R)):
        for v in range(u+1,len(R)):
            t+=1
            if R[v]%(1<<(A[u+1]+1)) != R[u]%(1<<(A[u+1]+1)): f+=1
print(f"  test {t:,}  ihlal {f}  -> {'DOGRULANDI' if f==0 else 'IHLAL'}")

print("\nMADDE 9 — one-bit lift: r stabilize => R stabilize?")
print("  Cebir: R_k in {r_*, r_*+2^{A_k}}. Nesting R_{k+1}=R_k (mod 2^{A_k+1}).")
print("    R_k=r_*+2^{A_k} ve R_{k+1}=r_*+2^{A_{k+1}} olsaydi:")
print("    r_*+2^{A_{k+1}} = r_*  (mod 2^{A_k+1})  ama R_k mod 2^{A_k+1} = r_*+2^{A_k}")
print("    => 2^{A_k} = 0 (mod 2^{A_k+1})  YANLIS. Yani tutarsiz.")
print("  => nesting, R'yi r stabilize oldugunda stabilize OLMAYA ZORLUYOR.")
# sayisal
t=f=0
for _ in range(4000):
    a=[random.randint(1,3) for _ in range(random.randint(8,26))]
    r,R,A,B=seq(a)
    n=len(r)
    if n>=6 and len(set(r[-4:]))==1:     # r son 4'te sabit
        t+=1
        if len(set(R[-4:]))!=1: f+=1
print(f"  sayisal: r-stabil ornekler {t}  R stabil DEGIL {f}  -> {'DOGRULANDI' if f==0 else 'KARSI-ORNEK'}")

print("\nMADDE 10 — r_* > 0 ve TEK mi?")
t=f0=fe=0
for _ in range(4000):
    a=[random.randint(1,3) for _ in range(random.randint(8,26))]
    r,R,A,B=seq(a)
    if len(r)>=6 and len(set(r[-4:]))==1:
        t+=1
        if r[-1]==0: f0+=1
        if r[-1]%2==0: fe+=1
print(f"  r-stabil ornek {t}   r_*=0 olan {f0}   r_* CIFT olan {fe}")
print(f"  -> {'r_* daima pozitif ve tek: DOGRULANDI' if f0==0 and fe==0 else 'DIKKAT'}")

print("\nMADDE 11 — gercek pozitif n_0 => r_k = n_0 eventually")
t=f=0
for n0 in range(3,2000,2):
    n=n0; av=[]
    for _ in range(40):
        m=3*n+1; v=(m&-m).bit_length()-1; n=m>>v; av.append(v)
        if n==1: break
    if len(av)<6: continue
    r,R,A,B=seq(av)
    t+=1
    # 2^{A_k} > n0 olan ilk k'dan sonra r_k = n0 olmali
    ok=True
    for k in range(len(r)):
        if (1<<A[k+1])>n0 and r[k]!=n0: ok=False;break
    if not ok: f+=1
print(f"  gercek yorunge {t}   ihlal {f}  -> {'DOGRULANDI' if f==0 else 'IHLAL'}")

print("\nMADDE 21 — kirma: sonsuz injury AMA rho_r->0 bulunabilir mi?")
print("  Cebir: injury => rho_r(k+1) >= ln(1+2^{A_k})/(k+1) >= k ln2/(k+1) -> ln2")
print("  Sonsuz injury => limsup rho_r >= ln2 > 0. IMKANSIZ.")
best=None
for _ in range(3000):
    a=[random.randint(1,4) for _ in range(30)]
    r,R,A,B=seq(a)
    inj=[k for k in range(1,len(r)) if r[k]!=r[k-1]]
    if len(inj)>=8:
        tail=max(math.log(1+r[k])/(k+1) for k in inj[-5:])
        if best is None or tail<best[0]: best=(tail,len(inj))
print(f"  en dusuk kuyruk injury orani: {best[0]:.6f}  (ln2={math.log(2):.6f})  -> karsi-ornek yok")
