"""
KRITIK TEST: g kelimesi q=665 icin 15600 adim PERIYODIK.
Controller a_k = g_k - d_k de o bolgede periyodik mi?

Eger a[u..u+r-1] = a[u+665..u+665+r-1] ise (uzun faktor tekrari):
  Task 6 Lemma B  ->  |n_{u+665} - n_u| >= 2^{A(W)} ~ 2^{alpha*r}
  Task 6 Lemma A  ->  n_k = O(k^kappa)
Buyuk r icin CELISKI — ve asimptotik degil, SOMUT k'da.
"""
from decimal import Decimal, getcontext
import math
getcontext().prec=60
ALPHA=Decimal(3).ln()/Decimal(2).ln(); af=float(ALPHA)
N=60000
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]

def esik(s,m):
    if s<=0: return True
    return (1<<(1000*s)) <= m**1053
a=[];s=0;S=[0]
for k in range(N):
    m=max(2,k+1)
    d=1 if (g[k]==2 and esik(s,m)) else -1
    a.append(g[k]-d); s+=d; S.append(s)

print("g ve a kelimelerinin q-kaydirma altinda uyusmasi\n")
print(f"{'q':>7} {'g uyusma':>11} {'a uyusma':>11} {'a: en uzun ortak blok':>24}")
for q in (53,306,665,15601):
    if q>=N-10: continue
    gu=sum(1 for k in range(N-q) if g[k]==g[k+q])/(N-q)
    au=sum(1 for k in range(N-q) if a[k]==a[k+q])/(N-q)
    # en uzun ardisik blok
    best=cur=0
    for k in range(N-q):
        if a[k]==a[k+q]: cur+=1; best=max(best,cur)
        else: cur=0
    print(f"{q:>7} {gu:>11.6f} {au:>11.6f} {best:>24,}")

# q=665 icin: en uzun tekrarli faktor nerede, ve celiski ne zaman?
q=665
runs=[];cur=0;st=0
for k in range(N-q):
    if a[k]==a[k+q]:
        if cur==0: st=k
        cur+=1
    else:
        if cur>0: runs.append((st,cur)); cur=0
if cur>0: runs.append((st,cur))
runs.sort(key=lambda t:-t[1])
print(f"\nq={q} icin en uzun 5 ortak blok (baslangic, uzunluk):")
for st,L in runs[:5]:
    AW=sum(a[st:st+L])
    nmax=(st+q+L)**1.053
    print(f"  u={st:>6}  r={L:>6}  A(W)={AW:>7}  ->  2^A(W) ~ 2^{AW}")
    print(f"      Lemma A ust siniri: n_k = O(k^1.053) ~ {nmax:,.0f} = 2^{math.log2(nmax):.1f}")
    print(f"      CELISKI MI? 2^{AW} > 2^{math.log2(nmax):.1f} ->  {AW > math.log2(nmax)}")
    if AW > math.log2(nmax):
        print(f"      *** EVET — {AW - math.log2(nmax):.0f} bit marjla ***")
    break
print(f"\nToplam ortak blok sayisi (q={q}): {len(runs):,}")
print(f"Uzunlugu >100 olan blok sayisi: {sum(1 for _,L in runs if L>100):,}")
