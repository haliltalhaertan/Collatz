"""
AUDIT MADDE 8 — karsi-ornek disiplini.
Her aday karsi-ornegi HANGI hipotezin blokladigini kesin tespit et.
Teorem hipotezleri: (H1) s_k = kappa*log2(k)+O(1), (H2) kappa>1,
                    (H3) 1<=a_k<=B,  (H4) a_k != g_k
"""
from decimal import Decimal, getcontext
import math, random
getcontext().prec = 60
ALPHA = Decimal(3).ln()/Decimal(2).ln()
af = float(ALPHA)

def F(k): return int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR'))
N = 60000
g = [F(k+1)-F(k) for k in range(N+1)]

def s_profil(a, isim, N=N):
    """s_k = F_k - A_k; kappa*log2(k)+O(1) formuna uyuyor mu?"""
    A = 0; s_list = []
    for k in range(min(len(a), N)):
        A += a[k]
        s_list.append(F(k+1)-A)
    # s_k / log2(k) oraninin kararlilagi -> kappa var mi?
    oranlar = [s_list[k]/math.log2(k+1) for k in range(100, len(s_list)) if k>1]
    son = s_list[-1]
    # lineer mi? s_k/k
    lin = son/len(s_list)
    kritik_ihlal = sum(1 for k in range(min(len(a),N)) if a[k]==g[k])
    alfabe_ihlal = sum(1 for x in a[:N] if not (1 <= x <= 3))
    print(f"\n--- {isim} ---")
    print(f"  s_k son deger      : {son:,}")
    print(f"  s_k / k            : {lin:+.6f}   {'(LINEER buyume)' if abs(lin)>0.01 else ''}")
    if oranlar:
        print(f"  s_k / log2(k) araligi: [{min(oranlar):+.3f}, {max(oranlar):+.3f}]")
        sabit = max(oranlar)-min(oranlar) < 0.3
        print(f"  -> kappa*log2(k)+O(1) formuna uyuyor mu? {'EVET' if sabit else 'HAYIR'}")
    print(f"  (H3) alfabe ihlali : {alfabe_ihlal}")
    print(f"  (H4) a_k=g_k sayisi: {kritik_ihlal}")

print("="*66)
print("MADDE 8 — her aday karsi-ornek hangi hipotezle bloklaniyor?")
print("="*66)

# (a) gercek 1-dongusu: n=1 -> 3*1+1=4 -> a=2 -> n=1 ...
s_profil([2]*N, "(a) a_k = 2 sabiti (gercek 1-dongusu)")
print("  BLOKLAYAN: (H1). s_k lineer -inf'e gidiyor, log formu yok.")
print("             Ayrica eventually periodic -> A_k/k -> 2 rasyonel != alpha.")

# (b) eventually periodic
per = ([1,2,1,3]*(N//4+1))[:N]
s_profil(per, "(b) eventually periodic (1,2,1,3 tekrari)")
print("  BLOKLAYAN: (H1). periyot ortalamasi 7/4=1.75 != alpha -> s_k lineer.")

# (c) kappa <= 1 : s_k = 0.5*log2(k) hedefli controller
def controller(kappa_str, N=N):
    KAP = Decimal(kappa_str); L2 = Decimal(2).ln()
    a=[]; s=0
    for k in range(N):
        h = KAP*(Decimal(k+1).ln()/L2) if k>=1 else Decimal(0)
        ad=[x for x in (1,2,3) if x!=g[k]]
        b=min(ad,key=lambda x:abs(Decimal(s+g[k]-x)-h)); a.append(b); s=s+g[k]-b
    return a
a_low = controller('0.5')
s_profil(a_low, "(c) kappa = 0.5  (kappa <= 1)")
print("  BLOKLAYAN: (H2). Lemma A'da sum j^(-kappa) IRAKSAK -> B_k/3^k = O(1)")
print("             cokuyor -> n_k = O(k^kappa) turetilemiyor. Teorem sessiz.")
# sayisal: sum j^-kappa
for kap in (0.5, 0.9, 1.0, 1.053, 1.5):
    S = sum(j**(-kap) for j in range(1, 200001))
    print(f"     kappa={kap:<6} sum_{{j<=2e5}} j^-kappa = {S:>12.2f}  "
          f"{'IRAKSAK' if kap<=1 else 'yakinsak'}")

# (d) B = 4 zero-critical
print("\n--- (d) B = 4 zero-critical ---")
print(f"  ust sinir kosulu: alpha/kappa <= log2(B-1) = log2(3) = {af:.6f}")
print(f"  yani kappa >= alpha/log2(3) = alpha/alpha = 1")
print(f"  ama (H2) zaten kappa > 1 diyor -> YENI KISIT YOK, teorem BOS.")
print("  BLOKLAYAN: hicbir sey — teorem B>=4'u dislamiyor, §9'da dogru belirtilmis.")

# (e) rastgele bounded zero-critical
random.seed(7)
a_rnd = [random.choice([x for x in (1,2,3) if x!=g[k]]) for k in range(N)]
s_profil(a_rnd, "(e) rastgele zero-critical (B=3)")
print(f"  BLOKLAYAN: (H1). rastgele yuruyus -> s_k ~ sqrt(k) mertebesinde,")
print(f"             log2(k) degil. (son |s_k|={abs(sum(g[k]-a_rnd[k] for k in range(N))):,}, "
      f"sqrt(N)={math.sqrt(N):.0f})")
