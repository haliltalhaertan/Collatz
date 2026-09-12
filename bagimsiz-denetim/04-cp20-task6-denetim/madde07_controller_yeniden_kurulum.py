"""
MADDE 7 + 10 — controller'i TANIMINDAN bagimsiz olarak yeniden kur ve
SHA256'yi dogrula. Arsivdeki engine dosyalarina BAKILMADI; yalnizca
CP20_TASK6_CONTROLLER_DEFINITION.md'deki kural kullanildi.

Kanonik controller SHA'si a_k sembollerinin HAM BYTE dizisi uzerinden
alinmistir: sha256(bytes(a)). Metin olarak birlestirilmis "123..." dizisinin
SHA'si farklidir ve yalniz tanisal olarak raporlanir.
"""
import hashlib
import math
from decimal import Decimal, getcontext, ROUND_FLOOR

getcontext().prec = 120
ALPHA = Decimal(3).ln() / Decimal(2).ln()
K = 100000
F = [int((ALPHA * k).to_integral_value(rounding=ROUND_FLOOR)) for k in range(K + 2)]
g = [F[k + 1] - F[k] for k in range(K + 1)]


def esik_saglaniyor(s, m):
    """s <= (1053/1000)*log2(m) <=> 2^(1000s) <= m^1053."""
    if s <= 0:
        return True
    return (1 << (1000 * s)) <= m**1053


a = []
s = 0
z_min = 10**9
z_max = -10**9
for k in range(K):
    m = max(2, k + 1)
    d = 1 if (g[k] == 2 and esik_saglaniyor(s, m)) else -1
    a.append(g[k] - d)
    s += d
    if k >= 100:
        q = max(0, int(1.053 * math.log2(m)))
        target = m**1053
        while q > 0 and (1 << (1000 * q)) > target:
            q -= 1
        while (1 << (1000 * (q + 1))) <= target:
            q += 1
        z = s - q
        z_min = min(z_min, z)
        z_max = max(z_max, z)

h_raw = hashlib.sha256(bytes(a)).hexdigest()
h_text = hashlib.sha256("".join(map(str, a)).encode("ascii")).hexdigest()
beklenen = "31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2"

print(f"Uretilen sembol sayisi : {len(a):,}")
print(f"alfabe a_k in {{1,2,3}} : {'EVET' if set(a) <= {1,2,3} else 'HAYIR'}  (gorulen: {sorted(set(a))})")
print(f"zero-critical a_k != g_k: {'EVET' if all(a[k] != g[k] for k in range(K)) else 'HAYIR'}")
print()
print(f"SHA256 (kanonik raw bytes(a)): {h_raw}")
print(f"SHA256 (tani icin digit-string): {h_text}")
print(f"SHA256 (arsivde)              : {beklenen}")
print(f"ESLESME                       : {'EVET — bagimsiz yeniden kurulum dogrulandi' if h_raw == beklenen else 'HAYIR'}")
print()
print("Bounded tracking lemma: z_k = s_k - q_k araligi (k>=100)")
print(f"  gozlenen : [{z_min}, {z_max}]")
print("  iddia    : [-41, 1]")
print(f"  saglaniyor mu: {'EVET' if -41 <= z_min and z_max <= 1 else 'HAYIR'}")

if h_raw != beklenen:
    raise SystemExit("Kanonik raw-byte SHA256 eslesmedi")
