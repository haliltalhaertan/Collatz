"""
TASK 7 DENETIMI — pressure ust sinirini bagimsiz DP sayimiyla test et.
Arsivin engine'lerine BAKILMADI.

N(r, C_D) = defect toplami |S| <= C_D olan, zero-critical, B-alfabeli,
Sturmian g uzerinde uzunluk-r kelime sayisi.  Iddia: log2 N / r -> h_B.
"""
from collections import defaultdict
from decimal import Decimal, getcontext
import math
getcontext().prec = 60
ALPHA = Decimal(3).ln()/Decimal(2).ln(); af=float(ALPHA)
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(4000)]
g=[F[k+1]-F[k] for k in range(3999)]

def N(r, CD, B, phase=0):
    dp={0:1}
    for i in range(r):
        gk=g[phase+i]
        ds=[gk-a for a in range(1,B+1) if a!=gk]
        nd=defaultdict(int)
        for s,c in dp.items():
            for d in ds: nd[s+d]+=c
        dp=nd
    return sum(c for s,c in dp.items() if abs(s)<=CD)

H4=0.56190073413740076093
H3=0.52346668069246471639

for B,H in ((4,H4),(3,H3)):
    print(f"\n=== B={B}   teorik h_{B} = {H:.14f} ===")
    print(f"  {'r':>4} {'C_D=0':>14} {'log2N/r':>10}   {'C_D=2':>14} {'log2N/r':>10}   "
          f"{'C_D=8':>14} {'log2N/r':>10}")
    for r in (10,20,40,80,160,320,640):
        row=f"  {r:>4}"
        for CD in (0,2,8):
            n=N(r,CD,B)
            row+=f" {n:>14,} {(math.log2(n)/r if n>0 else float('nan')):>10.5f}  " if n<10**14 else \
                 f" {'~2^%.1f'%math.log2(n):>14} {math.log2(n)/r:>10.5f}  "
        print(row)
    print(f"  -> h_{B} = {H:.5f} ; oranlar bu degere YUKARIDAN mi yaklasiyor?")

# faz bagimsizligi (Sturmian dengelilik)
print("\n=== Sturmian faz bagimsizligi (Parikh farki <= 1?) ===")
for r in (10,50,200,1000):
    cnt={}
    for u in range(0, 2000):
        n2=sum(1 for i in range(r) if g[u+i]==2)
        cnt[n2]=cnt.get(n2,0)+1
    ks=sorted(cnt)
    print(f"  r={r:>4}: gorulen g=2 sayilari {ks}  fark={max(ks)-min(ks)}  "
          f"{'DENGELI' if max(ks)-min(ks)<=1 else 'DENGESIZ (!)'}")

# faz farkinin N uzerindeki etkisi
print("\n=== farkli fazlarda N(r,0) degisiyor mu? ===")
for r in (20,40,80):
    vs=[N(r,0,4,phase=p) for p in range(6)]
    print(f"  r={r:>3}: {vs}  oran max/min = {max(vs)/min(vs):.4f}")
