"""
Iki bagimsiz kontrol daha (arsivdeki engine'lere bakmadan):

(1) Sturmian sayim: g_k = floor(a(k+1)) - floor(ak) kelimesinin
    uzunluk-r farkli faktor sayisi gercekten r+1 mi?

(2) Controller varligi: kappa=1.053 ile
      a_k in {1,2,3}, a_k != g_k, s_k = kappa*log2(k) + O(1)
    saglayan bir SEMBOLIK dizi kurulabiliyor mu?
    (Teorem bunu disliyorsa, once boyle bir seyin var oldugunu bilmeliyiz.)
"""
from fractions import Fraction
import math

# --- alpha = log2(3) icin yuksek hassasiyetli kesirli yaklasim ---
from decimal import Decimal, getcontext
getcontext().prec = 120
ALPHA = Decimal(3).ln() / Decimal(2).ln()

def F(k):
    return int((ALPHA * k).to_integral_value(rounding='ROUND_FLOOR'))

N = 200_000
g = [F(k + 1) - F(k) for k in range(N)]
assert set(g) <= {1, 2}, set(g)

# (1) Sturmian faktor sayimi
print("Sturmian kontrolu  (beklenen p_g(r) = r+1):")
ok = True
for r in range(1, 21):
    p = len({tuple(g[i:i + r]) for i in range(N - r)})
    flag = "OK" if p == r + 1 else "HATA"
    if p != r + 1:
        ok = False
    print(f"  r={r:2d}  p_g(r)={p:3d}  beklenen={r+1:3d}  {flag}")
print(f"  --> {'dogrulandi' if ok else 'IHLAL VAR'}\n")

# (2) Controller: geri beslemeli insa
KAPPA = Decimal('1.053')
LOG2 = Decimal(2).ln()

def hedef(k):
    if k < 2:
        return Decimal(0)
    return KAPPA * (Decimal(k).ln() / LOG2)

a = []
s = 0          # s_k = F_k - A_k;  s_{k+1} - s_k = g_k - a_k
sapmalar = []
ihlal_alfabe = ihlal_kritik = 0

for k in range(N):
    h = hedef(k + 1)
    gk = g[k]
    # a_k != g_k, a_k in {1,2,3}
    adaylar = [x for x in (1, 2, 3) if x != gk]
    # s_{k+1} = s + gk - a  -> hedefe en yakin a'yi sec
    en_iyi = min(adaylar, key=lambda x: abs(Decimal(s + gk - x) - h))
    a.append(en_iyi)
    s = s + gk - en_iyi
    if not (1 <= en_iyi <= 3):
        ihlal_alfabe += 1
    if en_iyi == gk:
        ihlal_kritik += 1
    if k >= 10:
        sapmalar.append(float(Decimal(s) - h))

print("Controller kontrolu (kappa=1.053, a_k in {1,2,3}, a_k != g_k):")
print(f"  alfabe ihlali          : {ihlal_alfabe}")
print(f"  zero-critical ihlali   : {ihlal_kritik}   (a_k = g_k olan yer sayisi)")
print(f"  sapma  E_k = s_k - kappa*log2(k):")
print(f"    min={min(sapmalar):+.4f}  max={max(sapmalar):+.4f}  "
      f"aralik={max(sapmalar)-min(sapmalar):.4f}")
print(f"  --> sapma {N:,} adimda sinirli kaliyor mu? "
      f"{'EVET (O(1) gorunuyor)' if max(sapmalar)-min(sapmalar) < 5 else 'HAYIR'}")

# gozlenen faktor karmasikligi vs teoremin gerektirdigi alt sinir
print("\nFaktor karmasikligi (controller kelimesi a):")
alpha_f = float(ALPHA); kappa_f = float(KAPPA)
print(f"  teorem alt siniri : log2(p_a(r))/r >= alpha/kappa = {alpha_f/kappa_f:.6f}")
print(f"  zero-critical ust : log2((r+1)*2^r)/r -> 1.0")
for r in (5, 10, 15, 20, 25):
    p = len({tuple(a[i:i + r]) for i in range(N - r)})
    print(f"  r={r:2d}  p_a(r)={p:6d}  log2(p)/r={math.log2(p)/r:.4f}  "
          f"ust sinir (r+1)2^r={(r+1)*2**r:,}")
