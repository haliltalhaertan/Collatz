"""Wang Thm 4.11: c>log2(3) sabiti ve sonsuz cokta (k,l): l>kc, a_{k+1}=...=a_l=1.
Yani UZUN 1-RUN gerekiyor (uzunluk ~ (c-1)k, k ile orantili)."""
from decimal import Decimal, getcontext
getcontext().prec = 200
ALPHA = Decimal(3).ln()/Decimal(2).ln(); LOG2 = Decimal(2).ln(); KAPPA = Decimal('1.053')
N = 300_000
F = [int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g = [F[k+1]-F[k] for k in range(N+1)]
a=[]; s=0
for k in range(N):
    h = KAPPA*(Decimal(k+1).ln()/LOG2) if k>=1 else Decimal(0)
    ad=[x for x in (1,2,3) if x!=g[k]]
    bst=min(ad,key=lambda x:abs(Decimal(s+g[k]-x)-h)); a.append(bst); s=s+g[k]-bst

# en uzun 1-run (ve g'deki en uzun 2-run)
def en_uzun(seq, val):
    best=cur=0; pos=0; bpos=0
    for i,x in enumerate(seq):
        if x==val:
            cur+=1
            if cur>best: best=cur; bpos=i-cur+1
        else: cur=0
    return best,bpos
r1,p1 = en_uzun(a,1); r2,p2 = en_uzun(g,2)
print(f"controller a: en uzun 1-run  = {r1}  (konum {p1:,})")
print(f"Sturmian  g : en uzun 2-run  = {r2}  (konum {p2:,})")
print(f"\nWang 4.11 icin gereken: l > k*c, c>{float(ALPHA):.4f}")
print(f"  yani k konumundan sonra ~{float(ALPHA)-1:.3f}*k uzunlugunda 1-run.")
print(f"  k={p1:,} icin gereken run uzunlugu ~ {0.585*p1:,.0f}, mevcut en uzun: {r1}")
print(f"  --> Wang 4.11 {'UYGULANABILIR' if r1 > 0.585*p1 else 'UYGULANAMAZ'}")

# alfabe dagilimi (genel resim)
from collections import Counter
c=Counter(a); t=len(a)
print(f"\ncontroller sembol dagilimi: " + ", ".join(f"{k}:{v/t:.4f}" for k,v in sorted(c.items())))
print(f"ortalama valuation A_k/k   = {sum(a)/len(a):.9f}   (alpha={float(ALPHA):.9f})")
