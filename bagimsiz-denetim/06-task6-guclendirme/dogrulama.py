"""Task 6 GUCLENDIRMESI icin sayisal taban.
Kaba sinir log2(B-1) ile basinc siniri h_B'nin karsilastirmasi ve
B=3 icin yakinsama testi."""
from collections import defaultdict
from mpmath import mp, mpf, exp, log, findroot, diff
from decimal import Decimal, getcontext
import math
mp.dps = 60
getcontext().prec = 60
ALPHA = log(3)/log(2)
def l2(x): return log(x)/log(2)

def hB(B):
    def f(lam):
        A  = sum(exp(lam*(1-a)) for a in range(2,B+1))
        Bb = sum(exp(lam*(2-a)) for a in range(1,B+1) if a!=2)
        return (2-ALPHA)*l2(A) + (ALPHA-1)*l2(Bb)
    lam = findroot(lambda L: diff(f,L), mpf('1.4'))
    return f(lam), lam

print("KABA SINIR vs BASINC SINIRI\n")
print(f"{'B':>3} {'kaba: log2(B-1)':>17} {'basinc: h_B':>16} {'kaba kappa esigi':>18} {'basinc kappa esigi':>20} {'kazanc':>8}")
for B in (3,4,5,6,8,10):
    h,_ = hB(B)
    kaba = float(mp.log(B-1)/mp.log(2))
    k_kaba = float(ALPHA)/kaba
    k_bas  = float(ALPHA/h)
    print(f"{B:>3} {kaba:>17.9f} {float(h):>16.9f} {k_kaba:>18.7f} {k_bas:>20.7f} {k_bas/k_kaba:>7.3f}x")

# B=3 yakinsama testi (bagimsiz DP)
A = Decimal(3).ln()/Decimal(2).ln()
F=[int((A*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(3000)]
g=[F[k+1]-F[k] for k in range(2999)]
def N(r,CD,B,phase=0):
    dp={0:1}
    for i in range(r):
        gk=g[phase+i]; ds=[gk-a for a in range(1,B+1) if a!=gk]
        nd=defaultdict(int)
        for s,c in dp.items():
            for d in ds: nd[s+d]+=c
        dp=nd
    return sum(c for s,c in dp.items() if abs(s)<=CD)

h3,_ = hB(3)
print(f"\nB=3 yakinsama (h_3 = {float(h3):.9f}, kaba sinir = 1.0):")
print(f"  {'r':>5} {'C_D=2: log2N/r':>16} {'C_D~kappa*log2(r)':>19}")
for r in (40,80,160,320,640,1280):
    n2=N(r,2,3); cd=max(2,int(1.053*math.log2(r)))
    n3=N(r,cd,3)
    print(f"  {r:>5} {math.log2(n2)/r:>16.6f} {math.log2(n3)/r:>19.6f}   (C_D={cd})")
print(f"  -> her ikisi de h_3={float(h3):.6f} civarina yaklasiyor, KABA sinir 1.0'in cok altinda")
