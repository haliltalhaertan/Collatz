"""
YENI EKSEN: alpha = log2(3)'un SUREKLI KESIRI ve buyuk kismi bolumler.

Iyi bir rasyonel yaklasim p/q  =>  Sturmian g kelimesi q-periyoduna
COK YAKIN olur (uzun neredeyse-periyodik bloklar).

Task 6'nin mekanizmasi: TEKRARLANAN faktor -> 2^{A(W)} | (n_v - n_u)
                        -> devasa ayrisma.
Eger g'de q uzunlugunda neredeyse-tekrarlar varsa, a kelimesinde de
yapisal tekrar baskisi olur. Bu, arsivin argumanina EKSTRA GUC verebilir.
"""
from mpmath import mp, mpf, log, floor
mp.dps=60
A=log(3)/log(2)

# surekli kesir acilimi
x=A; cf=[]; convs=[]
p0,q0,p1,q1=0,1,1,0
for i in range(30):
    ai=int(mp.floor(x)); cf.append(ai)
    p0,p1=p1,ai*p1+p0
    q0,q1=q1,ai*q1+q0
    convs.append((p1,q1,abs(A-mpf(p1)/q1)))
    fr=x-ai
    if fr==0: break
    x=1/fr

print("alpha = log2(3) surekli kesir:")
print(" ",cf[:20])
print()
print(f"{'i':>3} {'a_i':>5} {'p/q':>22} {'|alpha - p/q|':>14} {'q^2*hata':>10} {'kalite'}")
for i,(p,q,e) in enumerate(convs[:16]):
    kal = "***COK IYI***" if i+1<len(cf) and cf[i+1]>=5 else ""
    print(f"{i:>3} {cf[i]:>5} {str(p)+'/'+str(q):>22} {mp.nstr(e,6):>14} {mp.nstr(q*q*e,4):>10} {kal}")

# g kelimesi ve q-periyodikligi
NM=200000
F=[int(mp.floor(A*k)) for k in range(NM+2)]
g=[F[k+1]-F[k] for k in range(NM+1)]
print("\ng kelimesinin q-kaydirma altinda UYUSMA orani:")
print(f"{'q':>8} {'uyusma orani':>14} {'ilk uyusmazlik':>16}")
for p,q,e in convs[2:13]:
    if q>NM//2: break
    ayni=sum(1 for k in range(NM-q) if g[k]==g[k+q])
    oran=ayni/(NM-q)
    ilk=next((k for k in range(NM-q) if g[k]!=g[k+q]), None)
    print(f"{q:>8} {oran:>14.6f} {ilk if ilk is not None else '-':>16}")

print("\nYORUM:")
print("  Buyuk kismi bolumden ONCEKI konverjant (ornegin a_9=23 oncesi q)")
print("  g kelimesini cok uzun araliklarda PERIYODIK yapar.")
print("  Bu araliklarda a kelimesi de yapisal tekrar baskisi altinda:")
print("  Task 6 Lemma B tam burada devreye girer.")
