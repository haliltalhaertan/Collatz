"""
MADDE 1 — ortusen (overlapping) occurrence'larda Lemma B hala gecerli mi?
MADDE 6 — p_a(r) <= (r+1)(B-1)^r ust siniri; bir a-faktoru birden fazla
          g-faktoruyle iliskilendirilebiliyorsa sinir bozuluyor mu?
"""
from decimal import Decimal, getcontext
import math, random
getcontext().prec = 60
ALPHA = Decimal(3).ln()/Decimal(2).ln()

# ---------- MADDE 1: ortusen tekrarlar ----------
def orbit(n0, steps=500):
    ns,av=[n0],[]; n=n0
    for _ in range(steps):
        m=3*n+1; v=(m&-m).bit_length()-1; n=m>>v
        av.append(v); ns.append(n)
        if n==1: break
    return ns,av

ort_test=ort_fail=ayr_test=ayr_fail=0
for n0 in range(3, 120000, 2):
    ns,av=orbit(n0)
    L=len(av)
    for r in range(3,13):
        if L<r+2: break
        seen={}
        for u in range(L-r+1):
            W=tuple(av[u:u+r])
            if W in seen:
                for uu in seen[W]:
                    AW=sum(W); d=ns[u]-ns[uu]
                    ortusuyor = (u - uu) < r
                    if ortusuyor:
                        ort_test+=1
                        if d % (2**AW)!=0: ort_fail+=1
                    else:
                        ayr_test+=1
                        if d % (2**AW)!=0: ayr_fail+=1
                seen[W].append(u)
            else: seen[W]=[u]

print("MADDE 1 — Lemma B, ortusme durumuna gore ayrilmis")
print(f"  ORTUSEN  (v-u < r) : {ort_test:>10,} test, {ort_fail} ihlal")
print(f"  AYRIK    (v-u >= r): {ayr_test:>10,} test, {ayr_fail} ihlal")
print(f"  -> Lemma B ortusmeden BAGIMSIZ olarak gecerli: "
      f"{'DOGRULANDI' if ort_fail==0 and ayr_fail==0 else 'IHLAL'}")
print("     (beklenen: ispat sadece W'nin iki kez GECMESINI kullaniyor,")
print("      konumlarin ayrik olmasini degil -> ortusme onemsiz)\n")

# ---------- MADDE 6: ust sinir ----------
N=200000
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]
print("MADDE 6 — p_a(r) <= (r+1)(B-1)^r   [B=3 -> (r+1)2^r]")
print("  Uc farkli zero-critical kelime uzerinde test:\n")
print(f"  {'kelime':<26} {'r':>3} {'p_a(r)':>9} {'ust sinir':>14} {'saglaniyor':>11}")

# (i) controller  (ii) rastgele  (iii) adversarial: maksimum cesitlilik hedefli
L2=Decimal(2).ln(); KAP=Decimal('1.053')
ctrl=[];s=0
for k in range(N):
    h=KAP*(Decimal(k+1).ln()/L2) if k>=1 else Decimal(0)
    ad=[x for x in (1,2,3) if x!=g[k]]
    b=min(ad,key=lambda x:abs(Decimal(s+g[k]-x)-h)); ctrl.append(b); s=s+g[k]-b
random.seed(11)
rnd=[random.choice([x for x in (1,2,3) if x!=g[k]]) for k in range(N)]
# adversarial: her konumda oncekinden farkli sec -> cesitliligi artir
adv=[]; prev=0
for k in range(N):
    ad=[x for x in (1,2,3) if x!=g[k]]
    c=[x for x in ad if x!=prev] or ad
    adv.append(c[0]); prev=c[0]

for isim,w in (("controller (kappa=1.053)",ctrl),("rastgele",rnd),("adversarial",adv)):
    for r in (5,10,15,20):
        p=len({tuple(w[i:i+r]) for i in range(N-r)})
        ust=(r+1)*2**r
        print(f"  {isim:<26} {r:>3} {p:>9,} {ust:>14,} {'EVET' if p<=ust else 'HAYIR':>11}")
    print()

print("  Not: bir a-faktoru birden fazla g-faktoruyle iliskilendirilebilir.")
print("  Bu, birlesim kumesini KUCULTUR (ortusme), buyutmez.")
print("  Dolayisiyla (r+1)(B-1)^r sayimi ust sinir olarak GECERLI kalir.")
