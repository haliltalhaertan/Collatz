"""SHA uyusmazligi: kural varyanti mi, serilestirme farki mi?"""
import hashlib
from decimal import Decimal, getcontext
getcontext().prec = 150
ALPHA = Decimal(3).ln()/Decimal(2).ln(); L2 = Decimal(2).ln()
KAP = Decimal(1053)/Decimal(1000)
K = 100000
F = [int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(K+2)]
g = [F[k+1]-F[k] for k in range(K+1)]
HEDEF = "31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2"

# q_k'yi Decimal ile hizli hesapla (sinir durumu kontrolu ile)
def qtab(mfun):
    q=[0]*(K+1)
    for k in range(K+1):
        m = mfun(k)
        v = KAP*(Decimal(m).ln()/L2)
        fl = int(v.to_integral_value(rounding='ROUND_FLOOR'))
        if abs(v - fl) < Decimal('1e-60') or abs(v - (fl+1)) < Decimal('1e-60'):
            while (1 << (1000*(fl+1))) <= m**1053: fl += 1
        q[k]=fl
    return q

def uret(q, strict=False):
    a=[]; s=0
    for k in range(K):
        kos = (s < q[k]) if strict else (s <= q[k])
        d = 1 if (g[k]==2 and kos) else -1
        a.append(g[k]-d); s+=d
    return a

def hashes(a):
    w="".join(map(str,a))
    return {
      "join":            hashlib.sha256(w.encode()).hexdigest(),
      "join+nl":         hashlib.sha256((w+"\n").encode()).hexdigest(),
      "newline-sep":     hashlib.sha256("\n".join(map(str,a)).encode()).hexdigest(),
      "newline-sep+nl":  hashlib.sha256(("\n".join(map(str,a))+"\n").encode()).hexdigest(),
      "comma":           hashlib.sha256(",".join(map(str,a)).encode()).hexdigest(),
      "space":           hashlib.sha256(" ".join(map(str,a)).encode()).hexdigest(),
      "raw-bytes":       hashlib.sha256(bytes(a)).hexdigest(),
    }

varyantlar = {
  "A: m=max(2,k+1), s<=q":      (lambda k: max(2,k+1), False),
  "B: m=max(2,k+1), s<q":       (lambda k: max(2,k+1), True),
  "C: m=max(2,k),   s<=q":      (lambda k: max(2,k),   False),
  "D: m=k+2,        s<=q":      (lambda k: k+2,        False),
}
bulundu=False
for isim,(mf,st) in varyantlar.items():
    q = qtab(mf)
    a = uret(q, st)
    ozet = f"alfabe={'OK' if set(a)<={1,2,3} else 'X'} zc={'OK' if all(a[k]!=g[k] for k in range(K)) else 'X'}"
    hs = hashes(a)
    hit = [k for k,v in hs.items() if v==HEDEF]
    print(f"{isim:<30} {ozet}  {'*** ESLESME: '+hit[0] if hit else 'eslesme yok'}")
    if hit: bulundu=True; print(f"    -> {hs[hit[0]]}")
if not bulundu:
    print("\nHicbir varyant+serilestirme kombinasyonu hedef SHA'yi vermedi.")
    print("A varyantinin hash'leri (referans):")
    for k,v in hashes(uret(qtab(lambda k:max(2,k+1)))).items():
        print(f"  {k:<16} {v}")
