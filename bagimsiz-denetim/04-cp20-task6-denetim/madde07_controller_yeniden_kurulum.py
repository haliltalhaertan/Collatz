"""
MADDE 7 + 10 — controller'i TANIMINDAN bagimsiz olarak yeniden kur ve
SHA256'yi dogrula.  Arsivdeki engine dosyalarina BAKILMADI; yalnizca
CP20_TASK6_CONTROLLER_DEFINITION.md'deki kural kullanildi:

  q_k = floor(kappa * log2(max(2, k+1))),  kappa = 1053/1000
  d_k = +1  eger g_k = 2 VE s_k <= q_k ;  aksi halde -1
  a_k = g_k - d_k ,  s_{k+1} = s_k + d_k ,  s_0 = 0

Esik kosulu tam sayi formunda (float YOK):
  s_k <= kappa*log2(m)  <=>  2^(1000*s_k) <= m^1053      [m = max(2,k+1)]
"""
import hashlib
from decimal import Decimal, getcontext
getcontext().prec = 120
ALPHA = Decimal(3).ln()/Decimal(2).ln()

K = 100000
F = [int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(K+2)]
g = [F[k+1]-F[k] for k in range(K+1)]

def esik_saglaniyor(s, m):
    """s <= kappa*log2(m)  <=>  2^(1000 s) <= m^1053  (tam sayi)"""
    if s <= 0:
        return True
    return (1 << (1000*s)) <= m**1053

a=[]; s=0; z_min=10**9; z_max=-10**9
for k in range(K):
    m = max(2, k+1)
    d = 1 if (g[k]==2 and esik_saglaniyor(s, m)) else -1
    a.append(g[k]-d)
    s += d
    if k >= 100:
        # q_k'yi tam bul (z_k = s_k - q_k icin)
        q = 0
        while (1 << (1000*(q+1))) <= m**1053: q += 1
        z = s - q
        z_min = min(z_min, z); z_max = max(z_max, z)

w = "".join(map(str, a))
h = hashlib.sha256(w.encode()).hexdigest()
beklenen = "31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2"

print(f"Uretilen sembol sayisi : {len(a):,}")
print(f"alfabe  a_k in {{1,2,3}} : {'EVET' if set(a)<={1,2,3} else 'HAYIR'}  (gorulen: {sorted(set(a))})")
print(f"zero-critical a_k != g_k: {'EVET' if all(a[k]!=g[k] for k in range(K)) else 'HAYIR'}")
print()
print(f"SHA256 (hesaplanan): {h}")
print(f"SHA256 (arsivde)   : {beklenen}")
print(f"ESLESME            : {'EVET — bagimsiz yeniden kurulum dogrulandi' if h==beklenen else 'HAYIR'}")
print()
print(f"Bounded tracking lemma:  z_k = s_k - q_k  araligi (k>=100)")
print(f"  gozlenen : [{z_min}, {z_max}]")
print(f"  iddia    : [-41, 1]")
print(f"  saglaniyor mu: {'EVET' if -41 <= z_min and z_max <= 1 else 'HAYIR'}")
