"""Somut karsi-ornek incelemesi: r stabil ama R stabil degil?"""
import random
def seq(a):
    A=[0];B=[0]
    for k,ak in enumerate(a):
        B.append(3*B[k]+2**A[k]); A.append(A[k]+ak)
    r=[];R=[];C=[]
    for k in range(1,len(a)+1):
        m=1<<A[k]
        rk=(-B[k]*pow(pow(3,k,m),-1,m))%m
        c=(3**k*rk+B[k])//m
        r.append(rk); C.append(c)
        R.append(rk if (c%2==1) else rk+m)
    return r,R,A,B,C

random.seed(5)
bulundu=None
for _ in range(4000):
    a=[random.randint(1,3) for _ in range(random.randint(8,26))]
    r,R,A,B,C=seq(a)
    if len(r)>=6 and len(set(r[-4:]))==1 and len(set(R[-4:]))!=1:
        bulundu=(a,r,R,A,B,C); break

a,r,R,A,B,C=bulundu
print(f"kelime a = {a}\n")
print(f"{'k':>3} {'a_k':>4} {'A_k':>5} {'r_k':>12} {'c=n_k':>14} {'c tek?':>7} {'R_k':>14}")
for k in range(len(r)):
    print(f"{k+1:>3} {a[k]:>4} {A[k+1]:>5} {r[k]:>12,} {C[k]:>14,} {str(C[k]%2==1):>7} {R[k]:>14,}")

print("\nSON 5 ADIM:")
print(f"  r son 5: {r[-5:]}")
print(f"  R son 5: {R[-5:]}")

print("\nTESHIS — R gercekten nested mi? (son birkac adim, elle)")
for k in range(len(R)-4, len(R)-1):
    mod=1<<(A[k+1]+1)
    print(f"  R[{k+1}] mod 2^(A_{k+1}+1)={mod:,}: {R[k]%mod:,}   "
          f"R[{k+2}] mod ayni: {R[k+1]%mod:,}   esit mi: {R[k]%mod==R[k+1]%mod}")

print("\nKRITIK KONTROL — n_j hepsi TEK mi? (R_k'nin gercek anlami)")
print("  R_k yalnizca n_k'yi tek yapiyor. Ama Syracuse TUM n_j'lerin tek olmasini ister.")
for k in (len(r)-1,):
    n0=R[k]
    n=n0; ok=True; tekler=[]
    for j in range(k+1):
        tekler.append(n%2==1)
        m=3*n+1; v=(m&-m).bit_length()-1
        if v!=a[j]: ok=False; break
        n=m>>v
    print(f"  n_0=R[{k+1}]={n0:,} ile ileri kosma: valuationlar uyustu mu={ok}")
    print(f"  ara n_j'lerin hepsi tek mi: {all(tekler)}  (ilk 12: {tekler[:12]})")
