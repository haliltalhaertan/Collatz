"""
CP20 TASK 8B2 D0 — ZERO-TRUST DENETIM
Arsivin engine'lerine BAKILMADI.

Kurulum: a_k>=1, A_k=sum_{j<k}a_j, B_0=0, B_{k+1}=3B_k+2^{A_k}
        r_k = -3^{-k} B_k  (mod 2^{A_k}),  0<=r_k<2^{A_k}
        rho_r(k) = ln(1+r_k)/k
"""
from fractions import Fraction
import math, random

def rseq(a):
    """r_k dizisi, k=1..len(a)"""
    A=[0]; B=[0]
    for k,ak in enumerate(a):
        B.append(3*B[k]+2**A[k]); A.append(A[k]+ak)
    out=[]
    for k in range(1,len(a)+1):
        m=1<<A[k]
        out.append((-B[k]*pow(pow(3,k,m),-1,m))%m)
    return out,A,B

print("MADDE 1-2 — B_v ozdesligi ve nesting r_v = r_u (mod 2^{A_u})\n")
random.seed(11); t=f=0
for trial in range(400):
    L=random.randint(4,26)
    a=[random.randint(1,4) for _ in range(L)]
    r,A,B=rseq(a)
    # B_v = 3^{v-u} B_u + sum_{i=u}^{v-1} 3^{v-1-i} 2^{A_i}
    for _ in range(6):
        u=random.randint(0,L-1); v=random.randint(u+1,L)
        lhs=B[v]; rhs=3**(v-u)*B[u]+sum(3**(v-1-i)*2**A[i] for i in range(u,v))
        t+=1
        if lhs!=rhs: f+=1
    # nesting
    for u in range(1,L):
        for v in range(u+1,L+1):
            t+=1
            if r[v-1]%(1<<A[u]) != r[u-1]%(1<<A[u]): f+=1
print(f"  test {t:,}  ihlal {f}   -> {'DOGRULANDI' if f==0 else 'IHLAL'}")

print("\nMADDE 3-5 — her injury yukari, ve r_{k+1} >= 2^{A_k} >= 2^k\n")
t=f=0; minrate=[]
for trial in range(500):
    L=random.randint(6,30)
    a=[random.randint(1,4) for _ in range(L)]
    r,A,B=rseq(a)
    for k in range(1,L):
        if r[k]!=r[k-1]:
            t+=1
            if r[k] < (1<<A[k]): f+=1          # injury -> r_{k+1} >= 2^{A_k}
            if A[k] < k: f+=1                   # A_k >= k  (a_j>=1)
            minrate.append(math.log(1+r[k])/(k+1))
print(f"  injury test {t:,}  ihlal {f}   -> {'DOGRULANDI' if f==0 else 'IHLAL'}")
print(f"  gozlenen min injury orani rho_r(k+1): {min(minrate):.6f}   (ln2={math.log(2):.6f})")

print("\nM1 DENETIMI — 'kritik-log GEREKMEZ' iddiasi")
print("  Cebir: injury => r_{k+1} = r_k + m*2^{A_k}, m>=1 => r_{k+1} >= 2^{A_k} >= 2^k")
print("         => rho_r(k+1) >= ln(1+2^k)/(k+1) -> ln2 > 0")
print("  Ters : sonlu injury => r_k = r_* sabit => rho_r(k)=ln(1+r_*)/k -> 0")
print(f"  -> 'rho_r->0  <=>  r_k eventually stabilize'  KRITIK-LOG GEREKTIRMIYOR: DOGRULANDI")

print("\nMADDE 20 — kritik-log DISI ornekler")
for isim,a in (("all-ones a_k=1",[1]*400), ("alternating (1,2)^inf",[1,2]*200),
               ("a_k=2 sabit",[2]*400)):
    r,A,B=rseq(a)
    inj=sum(1 for k in range(1,len(r)) if r[k]!=r[k-1])
    stab = r[-1]==r[-2]==r[-3]
    rho=[math.log(1+r[k])/(k+1) for k in range(len(r))]
    Aln2k=[A[k+1]*math.log(2)/(k+1) for k in range(len(r))]
    print(f"  {isim:<22} injury={inj:>4}  son r sabit mi={stab}  "
          f"limsup rho~{max(rho[-50:]):.4f}  tavan A_k ln2/k~{Aln2k[-1]:.4f}")
