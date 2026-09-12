"""AUDIT MADDE 8 — karsi-ornek disiplini.
Her aday karsi-ornegi HANGI hipotezin blokladigini kesin tespit et.
Teorem hipotezleri: (H1) s_k=kappa*log2(k)+O(1), (H2) kappa>1,
(H3) 1<=a_k<=B, (H4) a_k!=g_k.

2026-09-12 integration correction: report finite s_N/N observations without
inferring an asymptotic H1 verdict. The proposed kappa=.5 violates H2; a
finite controller or seeded random sample does not itself settle H1.
"""
from decimal import Decimal, getcontext
import math, random
getcontext().prec=60
ALPHA=Decimal(3).ln()/Decimal(2).ln(); af=float(ALPHA)

def F(k): return int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR'))
N=60000
g=[F(k+1)-F(k) for k in range(N+1)]

def s_profil(a,isim,N=N):
    A=0; s_list=[]
    for k in range(min(len(a),N)):
        A+=a[k]; s_list.append(F(k+1)-A)
    oranlar=[s_list[k]/math.log2(k+1) for k in range(100,len(s_list)) if k>1]
    son=s_list[-1]; lin=son/len(s_list)
    kritik_ihlal=sum(1 for k in range(min(len(a),N)) if a[k]==g[k])
    alfabe_ihlal=sum(1 for x in a[:N] if not (1<=x<=3))
    print(f"\n--- {isim} ---")
    print(f"  s_k son deger      : {son:,}")
    print(f"  s_k / k            : {lin:+.6f} {'(SONLU DRIFT GOZLEMI; H1 KARARI DEGIL)' if abs(lin)>0.01 else ''}")
    if oranlar:
        print(f"  s_k/log2(k) finite araligi: [{min(oranlar):+.3f}, {max(oranlar):+.3f}]")
        print("  NOTE: sonlu aralik tek basina H1'i ne ispatlar ne de curutur; asimptotik drift ayri ispat gerektirir.")
    print(f"  (H3) alfabe ihlali : {alfabe_ihlal}")
    print(f"  (H4) a_k=g_k sayisi: {kritik_ihlal}")
    return son,lin

print("="*66); print("MADDE 8 — adaylar hangi hipotezle bloklaniyor?"); print("="*66)

s_profil([2]*N,"(a) a_k=2 sabiti (gercek 1-dongusu)")
print("  BLOKLAYAN: H1 (cebirle). s_k=floor(alpha*k)-2*k; alpha-2 != 0.")

per=([1,2,1,3]*(N//4+1))[:N]
s_profil(per,"(b) eventually periodic (1,2,1,3)")
print("  BLOKLAYAN: H1. Periyot ortalamasi 7/4 != alpha; s_k lineer.")

def controller(kappa_str,N=N):
    KAP=Decimal(kappa_str); L2=Decimal(2).ln(); a=[]; s=0
    for k in range(N):
        h=KAP*(Decimal(k+1).ln()/L2) if k>=1 else Decimal(0)
        ad=[x for x in (1,2,3) if x!=g[k]]
        b=min(ad,key=lambda x:abs(Decimal(s+g[k]-x)-h)); a.append(b); s=s+g[k]-b
    return a

a_low=controller('0.5')
_,lin_low=s_profil(a_low,"(c) kappa=0.5 hedefli controller")
print("  Onerilen kappa=0.5 icin BLOKLAYAN: H2 (kappa<=1).")
print(f"  Sonlu controller gozlemi: s_N/N={lin_low:+.6f}; bu tek basina H1 hakkinda asimptotik karar vermez.")
for kap in (0.5,0.9,1.0,1.053,1.5):
    S=sum(j**(-kap) for j in range(1,200001))
    print(f"     kappa={kap:<6} sum_{{j<=2e5}} j^-kappa = {S:>12.2f} {'IRAKSAK' if kap<=1 else 'yakinsak'}")

print("\n--- (d) B=4 zero-critical ---")
print(f"  kaba ust sinir alpha/kappa <= log2(3)={af:.6f} => kappa>=1")
print("  H2 zaten kappa>1; bu kaba B=4 sayimi yeni kisit vermez.")
print("  NOT: daha guclu basinç sonucu ayri dosyalarda ele alinmistir.")

random.seed(7)
a_rnd=[random.choice([x for x in (1,2,3) if x!=g[k]]) for k in range(N)]
son,lin=s_profil(a_rnd,"(e) rastgele bounded zero-critical (B=3)")
print("  SONLU ORNEK: gozlenen sapma sqrt(N) olceginden buyuktur:")
print(f"             |s_N|={abs(son):,}, sqrt(N)={math.sqrt(N):.0f}, s_N/N={lin:+.6f}.")
print("             Bu sonlu seeded ornekten H1'in asimptotik olarak yanlis oldugu sonucu cikmaz.")
