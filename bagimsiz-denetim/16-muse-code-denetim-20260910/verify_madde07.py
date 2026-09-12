# Madde 7 yeniden kurulum - semantik birebir, sadece q_k hesabi monotone hizlandirilmis
import hashlib
from decimal import Decimal, getcontext
getcontext().prec = 120
ALPHA = Decimal(3).ln()/Decimal(2).ln()

K = 100000
F = [int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(K+2)]
g = [F[k+1]-F[k] for k in range(K+1)]

a=[]; s=0; q=0; z_min=10**9; z_max=-10**9
for k in range(K):
    m = max(2, k+1)
    P = m**1053  # tek buyuk us per k (orijinalde while dongusu icinde ~18 kez)
    d = 1 if (g[k]==2 and (s <= 0 or (1 << (1000*s)) <= P)) else -1
    a.append(g[k]-d)
    s += d
    if k >= 100:
        while (1 << (1000*(q+1))) <= P: q += 1
        z = s - q
        z_min = min(z_min, z); z_max = max(z_max, z)

w = "".join(map(str, a))
h_digits = hashlib.sha256(w.encode()).hexdigest()
h_bytes  = hashlib.sha256(bytes(a)).hexdigest()
beklenen = "31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2"

print(f"sembol: {len(a):,}")
print(f"alfabe {{1,2,3}}: {sorted(set(a))}")
print(f"zero-critical: {all(a[k]!=g[k] for k in range(K))}")
print(f"SHA256(digit-string) = {h_digits}")
print(f"SHA256(raw bytes)    = {h_bytes}")
print(f"SHA256(arsiv)        = {beklenen}")
print(f"digits eslesme : {h_digits == beklenen}")
print(f"bytes  eslesme : {h_bytes == beklenen}")
print(f"z araligi: [{z_min}, {z_max}]  (iddia [-41,1]) -> {'OK' if (-41 <= z_min and z_max <= 1) else 'IHLAL'}")
