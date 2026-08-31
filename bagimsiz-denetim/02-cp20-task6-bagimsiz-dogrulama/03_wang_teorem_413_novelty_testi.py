"""
NOVELTY TESTI — CP20 Task 6 teoremi Wang Theorem 4.13'un kapsaminda mi?

Wang Thm 4.13 hipotezleri (arXiv:1809.02278v4, s.12):
  (i)  3^n > 2^{b_n}  her n icin            [b_n = sum_{i<=n} a_i]
  (ii) bir c > log2(3) sabiti var oyle ki SONSUZ COKLUKTA (r,l) cifti icin:
         l > r,  b_{l+r} > l*c,  ve  a_{l+k} = a_k  (1<=k<=r)
       yani ILK ONEK (a_1..a_r) l konumunda tekrar ediyor.
  Sonuc: Omega-lim a_n = infinity  (Omega-divergent, yani realize edilemez)

Eger CP20 controller'i bu hipotezleri sagliyorsa, Task 6'nin sonucu
Wang 4.13'ten zaten cikar -> NOVELTY YOK.
"""
from decimal import Decimal, getcontext
import math
getcontext().prec = 200
ALPHA = Decimal(3).ln() / Decimal(2).ln()
LOG2 = Decimal(2).ln()
KAPPA = Decimal('1.053')

N = 300_000
F = [0]*(N+2)
for k in range(N+2):
    F[k] = int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR'))
g = [F[k+1]-F[k] for k in range(N+1)]

# controller (onceki dogrulamayla ayni insa)
a = []          # a[0] = a_1  (Wang 1-indexli)
s = 0
for k in range(N):
    h = KAPPA*(Decimal(k+1).ln()/LOG2) if k >= 1 else Decimal(0)
    gk = g[k]
    ad = [x for x in (1,2,3) if x != gk]
    best = min(ad, key=lambda x: abs(Decimal(s+gk-x)-h))
    a.append(best); s = s+gk-best

# b_n = a_1+...+a_n   (b[0]=0)
b = [0]*(N+1)
for n in range(1, N+1):
    b[n] = b[n-1] + a[n-1]

alpha_f = float(ALPHA)
print(f"alpha = log2(3) = {alpha_f:.9f}\n")

# --- Hipotez (i): 3^n > 2^{b_n}  <=>  b_n < alpha*n ---
ihlal_i = [n for n in range(1, N+1) if b[n] >= alpha_f*n]
print("Hipotez (i)  3^n > 2^{b_n}:")
print(f"  ihlal sayisi: {len(ihlal_i)}" + (f"  ilk ihlaller: {ihlal_i[:5]}" if ihlal_i else "  -> SAGLANIYOR"))

# --- Hipotez (ii): ilk onek tekrari ---
# a_{l+k} = a_k for 1<=k<=r  ==>  a[l:l+r] == a[0:r]  (0-indexli)
print("\nHipotez (ii)  ilk onek (a_1..a_r) l konumunda tekrari:")
print("  r icin, oneki tekrar eden l konumlari ve b_{l+r} > l*c sarti\n")
print(f"  {'r':>4} {'tekrar l sayisi':>16} {'en iyi c = b_(l+r)/l':>22} {'c > alpha?':>12}")
bulunan = {}
for r in (1,2,3,4,5,6,8,10,12,15,20,30,50):
    onek = a[:r]
    ls = []
    for l in range(r+1, N-r):
        if a[l:l+r] == onek:
            ls.append(l)
    if ls:
        # c = b_{l+r}/l  degerinin ustunu ariyoruz (buyuk c iyi)
        best_c = max(b[l+r]/l for l in ls)
        bulunan[r] = (len(ls), best_c)
        print(f"  {r:>4} {len(ls):>16,} {best_c:>22.6f} {'EVET' if best_c > alpha_f else 'hayir':>12}")
    else:
        print(f"  {r:>4} {0:>16} {'-':>22} {'-':>12}")

print("\nYorum:")
print("  b_{l+r}/l ~ alpha*(l+r)/l = alpha*(1+r/l).")
print("  c > alpha icin r/l oraninin sifirdan uzak kalmasi gerekir,")
print("  yani onek tekrarlari l'ye ORANTILI r uzunlugunda olmali.")

# asil test: sabit c > alpha icin SONSUZ COKLUKTA (r,l) var mi?
# r = beta*l seklinde tarayalim
print("\n  Olceklenen test: r ~ beta*l icin onek tekrari var mi?")
print(f"  {'beta':>6} {'denenen l':>12} {'onek tekrari':>14} {'c=b_(l+r)/l':>14}")
for beta in (0.1, 0.25, 0.5, 1.0):
    hit = 0; ornek_c = None
    denenen = 0
    for l in range(100, min(N//2, 40000)):
        r = int(beta*l)
        if r < 1 or l+r >= N: continue
        denenen += 1
        if a[l:l+r] == a[:r]:
            hit += 1
            if ornek_c is None: ornek_c = b[l+r]/l
    print(f"  {beta:>6} {denenen:>12,} {hit:>14,} {(f'{ornek_c:.6f}' if ornek_c else '-'):>14}")
