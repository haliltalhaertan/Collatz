"""TASK 7 — genel B icin h_B ve esik kappa_B* = alpha/h_B.
Teoremin nerede ise yaramaz hale geldigini bul."""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps = 50
ALPHA = log(3)/log(2)
def l2(x): return log(x)/log(2)

def hB(B):
    # g=1 -> a in {2..B},  d = 1-a in {-1,...,-(B-1)}
    # g=2 -> a in {1,3..B}, d = 2-a in {+1,-1,...,-(B-2)}
    def f(lam):
        A  = sum(exp(lam*(1-a)) for a in range(2,B+1))
        Bb = sum(exp(lam*(2-a)) for a in range(1,B+1) if a!=2)
        return (2-ALPHA)*l2(A) + (ALPHA-1)*l2(Bb)
    lam = findroot(lambda L: diff(f,L), mpf('1.4'))
    return f(lam), lam

print(f"{'B':>3} {'h_B':>14} {'lambda*':>12} {'kappa_B* = alpha/h_B':>22} {'dislanan aralik':>22}")
prev=None
for B in range(3, 17):
    h,lam = hB(B)
    k = ALPHA/h
    aralik = f"1 < kappa < {mp.nstr(k,8)}" if k>1 else "*** BOS — hicbir sey dislanmaz"
    print(f"{B:>3} {mp.nstr(h,12):>14} {mp.nstr(lam,8):>12} {mp.nstr(k,12):>22} {aralik:>22}")

print("\nArsivin Task 7'de verdigi: B=4 -> kappa < 2.8207161949241867")
print("Ayni yontem B=3'e uygulanirsa -> kappa < 3.0278192656397885")
print("  ama Task 6 B=3 icin yalnizca kappa < alpha = 1.5849625 veriyor (kaba sinir).")
print("  => Task 7'nin yontemi Task 6'nin B=3 sonucunu ~2 KAT iyilestirir.")
print("     Bu, Task 7 findings'inde BELIRTILMEMIS.")

print("\nB -> buyudukce ne oluyor?")
for B in (20,30,50,100,200):
    h,_=hB(B); k=ALPHA/h
    print(f"  B={B:>4}  h_B={mp.nstr(h,10):>12}  kappa_B*={mp.nstr(k,10):>12}"
          f"  {'hala anlamli' if k>1 else '*** BOS'}")
