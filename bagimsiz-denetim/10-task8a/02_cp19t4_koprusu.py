"""max h = h(alpha) mi? Yani Task 8A yuzeyi CP19 T4'e YAKINSIYOR mu?"""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps=30
A=log(3)/log(2); M1=2-A; M2=A-1
def l2(x): return log(x)/log(2)
Af=lambda l: exp(-l)/(1-exp(-l)); Bf=lambda l: exp(l)+exp(-l)/(1-exp(-l))
def xlx(x): return mpf(0) if x<=0 else x*l2(x)
def h(r1,r2):
    if r1<0 or r2<0 or r1>=M1 or r2>=M2: return None
    w1,w2=M1-r1,M2-r2
    f=lambda lam: w1*l2(Af(lam))+w2*l2(Bf(lam))
    try:
        lam=findroot(lambda L: diff(f,L), mpf('1.6'))
        if lam<=0: return None
    except Exception: return None
    return f(lam)+xlx(M1)-xlx(w1)-xlx(r1)+xlx(M2)-xlx(w2)-xlx(r2)

h_alpha = l2(A)+(A-1)*(l2(A)-l2(A-1))
print(f"CP19 T4 geometrik maksimum entropi  h(alpha) = {mp.nstr(h_alpha,18)}")
print(f"CP19 T4 esigi  alpha/h(alpha)                = {mp.nstr(A/h_alpha,18)}")
print(f"arsivde kayitli kappa_0                      = 1.0526808586079717\n")

# ince arama (Nelder-Mead yerine iteratif incelme)
b=(mpf(0),M1/2,M2/2)
for it in range(6):
    st1,st2 = M1/(8*2**it), M2/(8*2**it)
    for i in range(-8,9):
        for j in range(-8,9):
            r1,r2=b[1]+i*st1,b[2]+j*st2
            v=h(r1,r2)
            if v is not None and v>b[0]: b=(v,r1,r2)
print(f"Task 8A yuzeyinin MAKSIMUMU (ince arama):")
print(f"  max h   = {mp.nstr(b[0],18)}   at (rho_1,rho_2)=({mp.nstr(b[1],7)}, {mp.nstr(b[2],7)})")
print(f"  fark    = {mp.nstr(abs(b[0]-h_alpha),6)}")
print(f"  esitler mi (12 basamak)? {mp.nstr(b[0],12)==mp.nstr(h_alpha,12)}")
print()
print(f"  optimal rho_1/M1 = {mp.nstr(b[1]/M1,8)}   rho_2/M2 = {mp.nstr(b[2]/M2,8)}")
print(f"  toplam kritik yogunluk = {mp.nstr(b[1]+b[2],8)}")
print()
print("KOPRU: Task 8A yuzeyi arsivin IKI ayri sonucunu ucuna aliyor:")
print(f"  rho=0        -> h={mp.nstr(h(mpf(0),mpf(0)),10)}  kappa>={mp.nstr(A/h(mpf(0),mpf(0)),10)}  [Task 7 + guclendirme]")
print(f"  rho=optimal  -> h={mp.nstr(b[0],10)}  kappa>={mp.nstr(A/b[0],10)}  [CP19 T4]")
