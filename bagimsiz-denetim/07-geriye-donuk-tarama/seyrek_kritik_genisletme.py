"""Ic ice optimizasyon: her nu icin lambda optimize, sonra nu uzerinde tara.
Kisit: kritik yogunluk <= eps  ->  nu <= 0  (Chernoff cezasi)
F(lam,nu) = (2-a)log2(2^nu + A(lam)) + (a-1)log2(2^nu + B(lam)) - nu*eps
"""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps=30
A=log(3)/log(2)
def l2(x): return log(x)/log(2)
Af=lambda lam: exp(-lam)/(1-exp(-lam))
Bf=lambda lam: exp(lam)+exp(-lam)/(1-exp(-lam))

def F(lam,nu,eps):
    t=mpf(2)**nu
    return (2-A)*l2(t+Af(lam))+(A-1)*l2(t+Bf(lam))-nu*eps

def h_eps(eps):
    best=None
    def inner(nu):
        try:
            lam=findroot(lambda L: diff(lambda x:F(x,nu,eps),L), mpf('1.6'))
            if lam<=0: return None,None
            return F(lam,nu,eps),lam
        except Exception: return None,None
    # nu <= 0 uzerinde kaba tarama, sonra incelt
    grid=[mpf(x)/4 for x in range(-160,1)]
    for nu in grid:
        v,lam=inner(nu)
        if v is not None and (best is None or v<best[0]): best=(v,lam,nu)
    if best is None: return None
    # incelt
    nu0=best[2]
    for _ in range(4):
        step=mpf('0.25')/(10**_)
        for k in range(-12,13):
            nu=nu0+k*step/10
            if nu>0: continue
            v,lam=inner(nu)
            if v is not None and v<best[0]: best=(v,lam,nu)
        nu0=best[2]
    return best

def h_kaba(eps):
    f=lambda lam:(2-A)*l2(Af(lam))+(A-1)*l2(Bf(lam))
    lam=findroot(lambda L:diff(f,L),mpf('1.6')); h0=f(lam)
    Hb=mpf(0) if eps<=0 or eps>=1 else -eps*l2(eps)-(1-eps)*l2(1-eps)
    return (1-eps)*h0+Hb

T5=mpf(1)-mpf('0.999855041504')
print("SEYREK KRITIK SITE — titiz (iki-Lagrange) vs kaba (karisim)\n")
print(f"{'eps':>12} {'h titiz':>12} {'esik titiz':>12} {'h kaba':>12} {'esik kaba':>11}")
sonuc={}
for eps in [mpf('1e-5'), T5, mpf('1e-3'), mpf('0.01'), mpf('0.05')]:
    r=h_eps(eps)
    hk=h_kaba(eps)
    if r:
        sonuc[str(eps)]=r
        m="  <- T5" if eps==T5 else ""
        print(f"{mp.nstr(eps,5):>12} {mp.nstr(r[0],8):>12} {mp.nstr(A/r[0],8):>12} "
              f"{mp.nstr(hk,8):>12} {mp.nstr(A/hk,8):>11}{m}")

r=h_eps(T5)
print(f"\nCP19 T5 SURVIVOR TESTI")
print(f"  eps (kritik site yogunlugu) = {mp.nstr(T5,8)}")
print(f"  titiz h = {mp.nstr(r[0],12)}   (lambda*={mp.nstr(r[1],7)}, nu*={mp.nstr(r[2],7)})")
print(f"  esik: kappa >= {mp.nstr(A/r[0],12)}")
print(f"  survivor kappa = 1.06")
print(f"  1.06 < esik ?  {mpf('1.06') < A/r[0]}")
print(f"  -> {'SURVIVOR DISLANIR' if mpf('1.06')<A/r[0] else 'survivor hayatta'}")
