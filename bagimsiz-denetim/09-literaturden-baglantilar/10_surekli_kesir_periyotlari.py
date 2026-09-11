"""
YENI EKSEN: alpha = log2(3)'un SUREKLI KESIRI ve buyuk kismi bolumler.

Bu surum mpmath gerektirmez; Python Decimal ile 70 basamak hassasiyet kullanir.
Sayisal ciktilar kesif/tekrar-uretim amaclidir, proof-critical aralik
sertifikasi degildir.
"""
from decimal import Decimal, getcontext, ROUND_FLOOR

getcontext().prec = 70
A = Decimal(3).ln() / Decimal(2).ln()

x = A
cf = []
convs = []
p0, q0, p1, q1 = 0, 1, 1, 0
for _ in range(30):
    ai = int(x.to_integral_value(rounding=ROUND_FLOOR))
    cf.append(ai)
    p0, p1 = p1, ai * p1 + p0
    q0, q1 = q1, ai * q1 + q0
    err = abs(A - Decimal(p1) / Decimal(q1))
    convs.append((p1, q1, err))
    fr = x - ai
    if fr == 0:
        break
    x = 1 / fr

print("alpha = log2(3) surekli kesir:")
print(" ", cf[:20])
print()
print(f"{'i':>3} {'a_i':>5} {'p/q':>22} {'|alpha - p/q|':>14} {'q^2*hata':>10} {'kalite'}")
for i, (p, q, e) in enumerate(convs[:16]):
    kal = "***COK IYI***" if i + 1 < len(cf) and cf[i + 1] >= 5 else ""
    e_short = f"{float(e):.5e}"
    qe_short = f"{float(Decimal(q*q)*e):.4g}"
    print(f"{i:>3} {cf[i]:>5} {str(p)+'/'+str(q):>22} {e_short:>14} {qe_short:>10} {kal}")

NM = 200000
F = [int((A * k).to_integral_value(rounding=ROUND_FLOOR)) for k in range(NM + 2)]
g = [F[k + 1] - F[k] for k in range(NM + 1)]
print("\ng kelimesinin q-kaydirma altinda UYUSMA orani:")
print(f"{'q':>8} {'uyusma orani':>14} {'ilk uyusmazlik':>16}")
for p, q, e in convs[2:13]:
    if q > NM // 2:
        break
    ayni = sum(1 for k in range(NM - q) if g[k] == g[k + q])
    oran = ayni / (NM - q)
    ilk = next((k for k in range(NM - q) if g[k] != g[k + q]), None)
    print(f"{q:>8} {oran:>14.6f} {ilk if ilk is not None else '-':>16}")

print("\nYORUM:")
print("  Buyuk kismi bolumden ONCEKI konverjant (ornegin a_9=23 oncesi q)")
print("  g kelimesini cok uzun araliklarda PERIYODIK yapar.")
print("  Bu araliklarda a kelimesi de yapisal tekrar baskisi altinda:")
print("  Task 6 Lemma B tam burada devreye girer.")
