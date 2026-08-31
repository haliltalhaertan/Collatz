"""MADDE 2 — Sturmian Parikh ozdesligi:
   n2(u,r) = #{i in [u,u+r) : g_i = 2} = floor((alpha-1)(u+r)) - floor((alpha-1)u)
ve sabit r icin sadece IKI deger alip aralarinda en fazla 1 fark olmasi."""
from decimal import Decimal, getcontext
getcontext().prec = 80
A = Decimal(3).ln()/Decimal(2).ln()
Am1 = A - 1
def fl(x): return int(x.to_integral_value(rounding='ROUND_FLOOR'))
N = 300000
F=[fl(A*k) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]

test=fail=0
for r in (1,2,3,5,8,13,21,34,55,100,377,1000):
    for u in range(0, 20000):
        n2 = sum(1 for i in range(u,u+r) if g[i]==2)
        pred = fl(Am1*(u+r)) - fl(Am1*u)
        test+=1
        if n2!=pred: fail+=1
print(f"Parikh ozdesligi  n2(u,r) = floor((a-1)(u+r)) - floor((a-1)u)")
print(f"  test: {test:,}   ihlal: {fail}   -> {'DOGRULANDI' if fail==0 else 'IHLAL'}")

print(f"\nSabit r icin kac farkli Parikh degeri? (dengelilik)")
kotu=0
for r in (1,2,3,5,8,13,21,34,55,100,377,1000,5000):
    vals = {fl(Am1*(u+r))-fl(Am1*u) for u in range(0,50000)}
    ok = (len(vals)<=2 and max(vals)-min(vals)<=1)
    if not ok: kotu+=1
    print(f"  r={r:>5}: degerler={sorted(vals)}  fark={max(vals)-min(vals)}  {'OK' if ok else 'IHLAL'}")
print(f"  -> {'hepsi en fazla 1 fark: DENGELI' if kotu==0 else 'DENGESIZ VAR'}")
