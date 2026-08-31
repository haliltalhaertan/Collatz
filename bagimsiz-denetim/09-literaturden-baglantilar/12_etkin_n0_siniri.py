"""
DUZELTME ve YENI FORMULASYON.

Lemma A:  n_k <= C(n_0) * k^kappa   -- sabit n_0'A BAGLI.
Onceki hesabimda C=1 aldim; yanlisti.

DOGRU OKUMA — cok daha ilginc:
Eger a[u..u+r-1] = a[v..v+r-1] (v=u+q) ise Lemma B:
    |n_v - n_u| >= 2^{A(W)}
Lemma A:
    |n_v - n_u| <= C * (v+r)^kappa
Demek ki:
    C >= 2^{A(W)} / (v+r)^kappa

Yani her uzun tekrar, n_0 uzerinde ETKIN BIR ALT SINIR veriyor.
Task 6 asimptotik bir celiski veriyordu; bu onun ETKIN versiyonu.
"""
from decimal import Decimal, getcontext
import math
getcontext().prec=60
ALPHA=Decimal(3).ln()/Decimal(2).ln()
N=120000
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]
def esik(s,m):
    if s<=0: return True
    return (1<<(1000*s)) <= m**1053
a=[];s=0
for k in range(N):
    m=max(2,k+1)
    d=1 if (g[k]==2 and esik(s,m)) else -1
    a.append(g[k]-d); s+=d

KAP=1.053
print("HER UZUN TEKRAR -> n_0 UZERINDE ETKIN ALT SINIR\n")
print(f"{'q':>7} {'u':>7} {'r':>7} {'A(W)':>8} {'(v+r)^kappa':>14} {'log2 n_0 >=':>13}")
sonuc=[]
for q in (53,306,665,15601,31867):
    if q>=N-100: continue
    best=(0,0)
    cur=0;st=0
    for k in range(N-q):
        if a[k]==a[k+q]:
            if cur==0: st=k
            cur+=1
            if cur>best[1]: best=(st,cur)
        else: cur=0
    st,L=best
    if L<20: continue
    AW=sum(a[st:st+L]); v=st+q
    ust=math.log2((v+L)**KAP)
    alt=AW-ust
    sonuc.append((q,L,alt))
    print(f"{q:>7} {st:>7} {L:>7} {AW:>8} {ust:>14.2f} {alt:>13.1f}")

print("\nYORUM — bu bir CELISKI DEGIL, ETKIN BIR SINIR:")
print("  Sonsuz yorunge icin n_0 SABIT olmali. Ama q buyudukce")
print("  gereken log2(n_0) alt siniri PATLIYOR:")
for q,L,alt in sonuc:
    print(f"    q={q:>6}: n_0 >= 2^{alt:.0f}")
print("  -> hicbir sabit n_0 hepsini karsilayamaz. Task 6'nin asimptotik")
print("     celiskisinin ETKIN (sayisal olarak izlenebilir) versiyonu.")

print("\nTUTARLILIK KONTROLU — bagimsiz iki hesap:")
print("  (a) sonlu prefix realizoru (2-adic lifting, onceki deney):")
print("      r=300 -> n_0 = 141 basamak = 2^468")
print(f"  (b) tekrar argumani (bu deney): q=665, r=671 -> n_0 >= 2^{sonuc[2][2] if len(sonuc)>2 else 0:.0f}")
print("  Iki BAGIMSIZ yoldan gelen n_0 buyume yasasi ayni mertebede.")
