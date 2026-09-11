"""Task 6 GUCLENDIRMESI icin sayisal taban.

Kaba sinir log2(B-1) ile basinc siniri h_B'nin karsilastirmasi ve
B=3 icin yakinsama testi.

Bu surum yalniz Python standart kutuphanesini kullanir. Basinc minimizasyonu
Decimal aritmetiginde, turev icin isaret-degistiren bir aralik bulunup
bisection uygulanarak yapilir. Sayisal tablo bir ispat sertifikasi degildir;
rigoroz h_3 / h_infinity araliklari interval_pressure_certificate.py'dedir.
"""
from collections import defaultdict
from decimal import Decimal, getcontext, ROUND_FLOOR
import math

getcontext().prec = 70
D0 = Decimal(0)
D1 = Decimal(1)
D2 = Decimal(2)
LN2 = D2.ln()
ALPHA = Decimal(3).ln() / LN2


def l2(x: Decimal) -> Decimal:
    return x.ln() / LN2


def _terms(B: int, lam: Decimal, family: int):
    if family == 1:
        exponents = [Decimal(1 - a) for a in range(2, B + 1)]
    else:
        exponents = [Decimal(2 - a) for a in range(1, B + 1) if a != 2]
    return [(c, (lam * c).exp()) for c in exponents]


def _logsum_stats(B: int, lam: Decimal, family: int):
    terms = _terms(B, lam, family)
    total = sum((w for _, w in terms), D0)
    mean = sum((c * w for c, w in terms), D0) / total
    second = sum((c * c * w for c, w in terms), D0) / total
    variance = second - mean * mean
    return total, mean, variance


def pressure(B: int, lam: Decimal) -> Decimal:
    A, _, _ = _logsum_stats(B, lam, 1)
    Bb, _, _ = _logsum_stats(B, lam, 2)
    return ((D2 - ALPHA) * A.ln() + (ALPHA - D1) * Bb.ln()) / LN2


def pressure_derivative(B: int, lam: Decimal) -> Decimal:
    _, mean_a, _ = _logsum_stats(B, lam, 1)
    _, mean_b, _ = _logsum_stats(B, lam, 2)
    return ((D2 - ALPHA) * mean_a + (ALPHA - D1) * mean_b) / LN2


def pressure_second_derivative(B: int, lam: Decimal) -> Decimal:
    _, _, var_a = _logsum_stats(B, lam, 1)
    _, _, var_b = _logsum_stats(B, lam, 2)
    return ((D2 - ALPHA) * var_a + (ALPHA - D1) * var_b) / LN2


def hB(B: int):
    lo = D0
    hi = D2
    dlo = pressure_derivative(B, lo)
    dhi = pressure_derivative(B, hi)
    while dlo * dhi > 0:
        hi *= 2
        dhi = pressure_derivative(B, hi)
        if hi > Decimal(128):
            raise RuntimeError(f"B={B}: pressure derivative could not be bracketed")

    for _ in range(240):
        mid = (lo + hi) / 2
        dm = pressure_derivative(B, mid)
        if dm == 0:
            lo = hi = mid
            break
        if dlo * dm <= 0:
            hi = mid
            dhi = dm
        else:
            lo = mid
            dlo = dm

    lam = (lo + hi) / 2
    curvature = pressure_second_derivative(B, lam)
    if curvature <= 0:
        raise AssertionError(f"B={B}: non-positive pressure curvature")
    return pressure(B, lam), lam


print("KABA SINIR vs BASINC SINIRI\n")
print(f"{'B':>3} {'kaba: log2(B-1)':>17} {'basinc: h_B':>16} {'kaba kappa esigi':>18} {'basinc kappa esigi':>20} {'kazanc':>8}")
for B in (3, 4, 5, 6, 8, 10):
    h, _ = hB(B)
    kaba = math.log2(B - 1)
    k_kaba = float(ALPHA) / kaba
    k_bas = float(ALPHA / h)
    print(f"{B:>3} {kaba:>17.9f} {float(h):>16.9f} {k_kaba:>18.7f} {k_bas:>20.7f} {k_bas/k_kaba:>7.3f}x")

F = [int((ALPHA * k).to_integral_value(rounding=ROUND_FLOOR)) for k in range(3000)]
g = [F[k + 1] - F[k] for k in range(2999)]


def N(r, CD, B, phase=0):
    dp = {0: 1}
    for i in range(r):
        gk = g[phase + i]
        ds = [gk - a for a in range(1, B + 1) if a != gk]
        nd = defaultdict(int)
        for s, c in dp.items():
            for d in ds:
                nd[s + d] += c
        dp = nd
    return sum(c for s, c in dp.items() if abs(s) <= CD)


h3, _ = hB(3)
print(f"\nB=3 yakinsama (h_3 = {float(h3):.9f}, kaba sinir = 1.0):")
print(f"  {'r':>5} {'C_D=2: log2N/r':>16} {'C_D~kappa*log2(r)':>19}")
for r in (40, 80, 160, 320, 640, 1280):
    n2 = N(r, 2, 3)
    cd = max(2, int(1.053 * math.log2(r)))
    n3 = N(r, cd, 3)
    print(f"  {r:>5} {math.log2(n2)/r:>16.6f} {math.log2(n3)/r:>19.6f}   (C_D={cd})")
print(f"  -> her ikisi de h_3={float(h3):.6f} civarina yaklasiyor, KABA sinir 1.0'in cok altinda")
