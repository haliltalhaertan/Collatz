"""
TASK 8A v3 — ANALITIK SADELESTIRME.
dF/dmu_i = 0  =>  2^{mu_1} = r1*A/(2-a-r1),  2^{mu_2} = r2*B/(a-1-r2)
Yerine koyunca (tam cebir):

  h(r1,r2) = inf_{lam>0} [ (2-a-r1) log2 A(lam) + (a-1-r2) log2 B(lam) ] + E1 + E2

  E1 = (2-a)log2(2-a) - (2-a-r1)log2(2-a-r1) - r1 log2 r1
  E2 = (a-1)log2(a-1) - (a-1-r2)log2(a-1-r2) - r2 log2 r2

E terimleri lam'dan BAGIMSIZ: "hangi siteler kritik" seciminin entropisi.
Kritik siteler dondurulmus (tek secenek), kalanlar basinc altinda.
"""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps=30
A=log(3)/log(2); M1=2-A; M2=A-1
def l2(x): return log(x)/log(2)
Af=lambda l: exp(-l)/(1-exp(-l))
Bf=lambda l: exp(l)+exp(-l)/(1-exp(-l))
def xlx(x): return mpf(0) if x<=0 else x*l2(x)

def h(r1,r2):
    if r1<0 or r2<0 or r1>M1 or r2>M2: return None
    w1,w2 = M1-r1, M2-r2
    if w1<=0 and w2<=0: return mpf(0)
    f=lambda lam: w1*l2(Af(lam))+w2*l2(Bf(lam))
    try:
        lam=findroot(lambda L: diff(f,L), mpf('1.6'))
        if lam<=0: raise ValueError
    except Exception:
        best=None
        for k in range(1,400):
            L=mpf(k)/50; v=f(L)
            if best is None or v<best[0]: best=(v,L)
        lam=best[1]
    E1 = xlx(M1)-xlx(w1)-xlx(r1)
    E2 = xlx(M2)-xlx(w2)-xlx(r2)
    return f(lam)+E1+E2

print(f"rho_1 <= {mp.nstr(M1,7)}   rho_2 <= {mp.nstr(M2,7)}\n")
print("h yuzeyi ve kappa esigi")
print(f"{'rho_1':>7} {'rho_2':>7} {'toplam':>8} {'h':>11} {'kappa esigi':>12}")
for r1,r2 in [(0,0),('0.01',0),(0,'0.01'),('0.05','0.05'),('0.1','0.1'),
              ('0.2',0),(0,'0.2'),('0.2','0.2'),('0.3','0.4'),('0.41','0.58')]:
    r1,r2=mpf(r1),mpf(r2); v=h(r1,r2)
    if v is not None:
        e = A/v if v>0 else mpf('inf')
        print(f"{mp.nstr(r1,4):>7} {mp.nstr(r2,4):>7} {mp.nstr(r1+r2,4):>8} {mp.nstr(v,8):>11} {mp.nstr(e,8):>12}")

# maksimum h
print("\nMAKSIMUM h taramasi:")
best=None
for i in range(0,41):
    for j in range(0,41):
        r1,r2=M1*i/40,M2*j/40
        v=h(r1,r2)
        if v is not None and (best is None or v>best[0]): best=(v,r1,r2)
print(f"  max h = {mp.nstr(best[0],10)}  at rho_1={mp.nstr(best[1],6)}, rho_2={mp.nstr(best[2],6)}")
print(f"  minimum ulasilabilir kappa esigi = {mp.nstr(A/best[0],10)}")

# rho_min(kappa)
print("\nrho_min(kappa) — gereken minimum TOPLAM kritik yogunluk")
print(f"{'kappa':>8} {'gereken h':>11} {'rho_min':>10} {'(r1*,r2*)':>20}")
for kap in ('1.06','1.5','2.0','2.5','2.784','2.9'):
    k=mpf(kap); hedef=A/k
    en=None
    for i in range(0,41):
        for j in range(0,41):
            r1,r2=M1*i/40,M2*j/40
            v=h(r1,r2)
            if v is not None and v>=hedef:
                t=r1+r2
                if en is None or t<en[0]: en=(t,r1,r2)
    if en:
        print(f"{kap:>8} {mp.nstr(hedef,8):>11} {mp.nstr(en[0],7):>10} "
              f"({mp.nstr(en[1],4)}, {mp.nstr(en[2],4)})")
    else:
        print(f"{kap:>8} {mp.nstr(hedef,8):>11} {'ULASILAMAZ':>10}   -> kappa tamamen kapali")
