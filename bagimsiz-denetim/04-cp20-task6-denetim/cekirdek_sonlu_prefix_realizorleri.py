"""
DOGRU YONTEM. 2^{A_k} n_k = 3^k n_0 + B_k  ve  n_k TEK olmali:
    3^k n_0 + B_k = 2^{A_k} (mod 2^{A_k+1})
=>  n_0 = (2^{A_k} - B_k) * 3^{-k}  (mod 2^{A_k+1})
Bu, k adiminin valuationunu TAM olarak a_{k-1} yapar.
Her k icin cozup tutarlilik kontrol edilir, sonra ileri kosarak DOGRULANIR.
"""
from decimal import Decimal, getcontext
import math
getcontext().prec = 60
ALPHA = Decimal(3).ln()/Decimal(2).ln(); L2 = Decimal(2).ln()
KAPPA = Decimal('1.053'); kf = float(KAPPA)

NMAX = 300
F = [int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(NMAX+2)]
g = [F[k+1]-F[k] for k in range(NMAX+1)]
a=[]; s=0
for k in range(NMAX):
    h = KAPPA*(Decimal(k+1).ln()/L2) if k>=1 else Decimal(0)
    ad=[x for x in (1,2,3) if x!=g[k]]
    b=min(ad,key=lambda x:abs(Decimal(s+g[k]-x)-h)); a.append(b); s=s+g[k]-b
A=[0]*(NMAX+1)
for k in range(NMAX): A[k+1]=A[k]+a[k]

Bk=[0]*(NMAX+1)
for k in range(1, NMAX+1):
    Bk[k] = 3*Bk[k-1] + 2**A[k-1]        # B_k = 3 B_{k-1} + 2^{A_{k-1}}

def n0_for(r):
    mod = 1 << (A[r]+1)
    return ((2**A[r] - Bk[r]) * pow(pow(3, r, mod), -1, mod)) % mod

# tutarlilik: x_r  ==  x_k  (mod 2^{A_k+1}) ?
tut = all(n0_for(300) % (1<<(A[k]+1)) == n0_for(k) for k in range(1, 301, 17))
print(f"2-adic tutarlilik (x_r = x_k mod 2^(A_k+1)): {'TUTARLI' if tut else 'TUTARSIZ'}\n")

print(f"{'r':>4} {'A_r':>5} {'n_0 basamak':>12} {'dogru':>7} {'max n_k/k^kappa':>18} {'artis':>9}")
onceki=None
for r in (5,10,20,30,50,80,120,160,200,250,300):
    n0 = n0_for(r)
    n = n0; ok=True; worst=0.0
    for k in range(r):
        m = 3*n+1
        v = (m & -m).bit_length()-1
        if v != a[k]: ok=False; break
        n = m >> v
        if k+1>=2: worst=max(worst, n/(k+1)**kf)
    bg = f"{worst/onceki:.1f}x" if onceki and worst else "-"
    onceki = worst if worst else onceki
    print(f"{r:>4} {A[r]:>5} {len(str(n0)):>12} {'EVET' if ok else 'HAYIR':>7} {worst:>18.3e} {bg:>9}")

print("\n  Lemma A ne diyordu: n_k <= C * k^kappa, C sabit (n_0'a bagli, r'ye DEGIL).")
print("  Gozlenen: max n_k/k^kappa orani r ile ustel buyuyor.")
print("  => sonsuz prefixi tasiyacak SABIT bir n_0 yok. Teoremin celiskisi somut.")
