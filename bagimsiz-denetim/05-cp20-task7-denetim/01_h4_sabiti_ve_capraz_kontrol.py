"""CP20 TASK 7 — h_4 sabitinin bagimsiz hesabi ve capraz kontroller."""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps = 80
ALPHA = log(3)/log(2)
def l2(x): return log(x)/log(2)

# g=1 yogunluk 2-alpha, izinli defect d in {-1,-2,-3} -> e^{lambda d}
# g=2 yogunluk alpha-1, izinli defect d in {+1,-1,-2}
def f4(lam):
    A = exp(-lam)+exp(-2*lam)+exp(-3*lam)
    Bb= exp(lam)+exp(-lam)+exp(-2*lam)
    return (2-ALPHA)*l2(A) + (ALPHA-1)*l2(Bb)

# minimize
lam_star = findroot(lambda L: diff(f4, L), mpf('1.5'))
h4 = f4(lam_star)
print("B=4 pressure:")
print(f"  lambda* (hesaplanan) = {mp.nstr(lam_star, 50)}")
print(f"  lambda* (arsivde)    = 1.5330136684139087818253460674861024575235320530573")
print(f"  h_4     (hesaplanan) = {mp.nstr(h4, 50)}")
print(f"  h_4     (arsivde)    = 0.5619007341374007609268031818280392747963893519951")
print(f"  ikinci turev (min mi?) = {mp.nstr(diff(f4, lam_star, 2), 10)}  "
      f"{'-> MINIMUM' if diff(f4,lam_star,2)>0 else '-> MAKSIMUM (!)'}")
k4 = ALPHA/h4
print(f"\n  alpha/h_4 (hesaplanan) = {mp.nstr(k4, 50)}")
print(f"  alpha/h_4 (arsivde)    = 2.8207161949241867869006891038446082915753302064363")
print(f"  sertifika araligi      = [2.82071619492418598504..., 2.82071619492418758875...]")
print(f"  hesaplanan aralikta mi? {mpf('2.8207161949241859850')<k4<mpf('2.8207161949241875888')}")

# --- CAPRAZ KONTROL: ayni yontem B=3'e uygulanirsa ---
def f3(lam):
    A = exp(-lam)+exp(-2*lam)          # g=1 -> a in {2,3}, d in {-1,-2}
    Bb= exp(lam)+exp(-lam)             # g=2 -> a in {1,3}, d in {+1,-1}
    return (2-ALPHA)*l2(A) + (ALPHA-1)*l2(Bb)
lam3 = findroot(lambda L: diff(f3, L), mpf('1.0'))
h3 = f3(lam3)
print(f"\nCAPRAZ KONTROL — ayni pressure yontemi B=3'e uygulanirsa:")
print(f"  lambda*_3 = {mp.nstr(lam3, 30)}")
print(f"  h_3       = {mp.nstr(h3, 30)}")
print(f"  Task 6'nin B=3 icin kullandigi KABA sinir: log2(B-1) = 1")
print(f"  alpha/h_3 = {mp.nstr(ALPHA/h3, 30)}   (Task 6'nin verdigi: alpha = {mp.nstr(ALPHA,20)})")
print(f"  -> pressure yontemi B=3'te de {'DAHA GUCLU' if h3<1 else 'daha zayif'} bir sinir veriyor")

print(f"\nTUTARLILIK SORUSU:")
print(f"  B=4 dilinde her sitede 3 secenek, B=3'te 2 secenek.")
print(f"  Daha COK secenek -> daha YUKSEK entropi -> dislama daha ZOR olmali.")
print(f"    h_3 = {mp.nstr(h3,20)}")
print(f"    h_4 = {mp.nstr(h4,20)}")
print(f"  h_4 > h_3 mi? {h4 > h3}  {'(beklenen)' if h4>h3 else '<-- TERS! INCELENMELI'}")
