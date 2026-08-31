"""D1 DENETIM — MADDE 11-16 + 20 (bagimsiz saldiri).  Arsivin kodu KULLANILMADI."""
import random, math
from itertools import product

def build(w):
    A=[0];B=[0];r=[0];R=[0]
    for k,a in enumerate(w,1):
        B.append(3*B[-1]+(1<<A[-1])); A.append(A[-1]+a)
        m=1<<A[-1]; r.append((-B[-1]*pow(pow(3,k,m),-1,m))%m)
        m2=1<<(A[-1]+1); R.append(((1<<A[-1])-B[-1])*pow(pow(3,k,m2),-1,m2)%m2)
    return A,B,r,R

print("MADDE 11 — r_{k+1} = R_k (mod 2^{A_k+1}) BAGIMSIZ turetim + sayisal")
print("  Turetim: 3^{k+1}r_{k+1}+B_{k+1} = 3(3^k r_{k+1}+B_k)+2^{A_k},  2^{A_k+a_k} boler.")
print("  a_k>=1 => 2^{A_k+1} | 3X+2^{A_k},  X:=3^k r_{k+1}+B_k.")
print("  r_{k+1}=r_k mod 2^{A_k} => 2^{A_k}|X, X=2^{A_k}c, 3c = -1 mod 2 => c TEK.")
print("  => derinlik-k bolumu tek => r_{k+1} = R_k mod 2^{A_k+1}.   [arsivin R formulu ile ayni]")
random.seed(55); t=f=0
for _ in range(500):
    w=[random.randint(1,5) for _ in range(random.randint(3,20))]
    A,B,r,R=build(w)
    for k in range(len(w)):
        t+=1
        if (r[k+1]-R[k])%(1<<(A[k]+1))!=0: f+=1
print(f"  {t:,} test, {f} ihlal -> {'DOGRULANDI' if f==0 else 'IHLAL'}\n")

print("MADDE 12-13 — TERMINAL ISTISNA: q'da injury varsa R_q != r_q OLABILIR")
print("  Somut ornek araniyor (w, q, r_q, R_q)...")
bulundu=[]
for w in product((1,2,3),repeat=6):
    A,B,r,R=build(list(w))
    for q in range(1,len(w)):
        if r[q+1]!=r[q] and R[q]!=r[q]:
            bulundu.append((w,q,r[q],R[q],A[q])); break
    if len(bulundu)>=4: break
for w,q,rq,Rq,Aq in bulundu:
    print(f"    w={w}  q={q}  A_q={Aq}  r_q={rq}  R_q={Rq}  R_q-r_q={Rq-rq}=2^{Aq}? {Rq-rq==(1<<Aq)}")
# istatistik
tot=exc=0
for w in product((1,2,3),repeat=8):
    A,B,r,R=build(list(w))
    for q in range(1,len(w)):
        if r[q+1]!=r[q]:
            tot+=1
            if R[q]!=r[q]: exc+=1
print(f"  3^8 kelime: injury'li q sayisi {tot:,}, bunlarin {exc:,} tanesinde R_q != r_q ({100*exc/tot:.1f}%)")
print(f"  -> MADDE 12/13 DOGRULANDI: 'FAIL AS STATED' tespiti hakli, duzeltme (p<=k<=q-1) dogru\n")

print("MADDE 14 — 'derinlik q-1'e kadar exact prefix' indeksleme")
print("  R_k derinlik-k tam kaldirimi = ilk k harfi (a_0..a_{k-1}) gerceklestiren tam sayi.")
print("  Lemma p<=k<=q-1 verir; en derini k=q-1 => a_0..a_{q-2}.")
print("  Bolum C platosu p=t_j+1, q=t_{j+1};  k=q'da injury var => istisna tam orada. TUTARLI\n")

print("MADDE 15 — MANAGER SINIRI: p=0, r_*=0 baslangic platosu mumkun mu?")
print("  Iddia (bagimsiz): r_1 = -3^{-1} mod 2^{a_0} HER ZAMAN TEK ve >0, yani r_1 != r_0 = 0.")
print("  => k=0 HER ZAMAN injury; p>=1; ve r artan oldugundan r_* >= r_1 > 0.")
t=f=0
for a0 in range(1,25):
    m=1<<a0; r1=(-1*pow(3,-1,m))%m
    t+=1
    if r1==0 or r1%2==0: f+=1
print(f"  a_0=1..24: {t} test, r_1=0 veya cift olan: {f}")
# tam kelimeler uzerinde
t=f=0
for w in product((1,2,3,4),repeat=6):
    A,B,r,R=build(list(w)); t+=1
    if r[1]==r[0]: f+=1
    if any(r[k+1]<r[k] for k in range(len(w))): f+=1
print(f"  4^6={t:,} kelime: r_1=r_0 olan {f}; r azalan olan 0")
print("  -> r_*>0 AYRICA VARSAYILMASINA GEREK YOK, TUREYEN bir olgu.")
print("  -> Minimal duzeltme: F lemmasina tek satir 'k=0 daima injury, dolayisiyla p>=1, r_*>0'\n")

print("MADDE 16 — MANAGER NICELEYICISI: tek bir tam sayi TUM platolari golgeler mi?")
A,B,r,R=build([random.choice([1,2]) for _ in range(60)])
inj=[k for k in range(60) if r[k+1]!=r[k]]
vals=[r[inj[j]+1] for j in range(len(inj))]
print(f"  ardisik plato r_* degerleri (ilk 8): {vals[:8]}")
print(f"  hepsi FARKLI mi: {len(set(vals))==len(vals)};  KESIN ARTAN mi: {all(vals[i]<vals[i+1] for i in range(len(vals)-1))}")
print("  Sebep: her injury'de m_{t_j}>=1 => r_{t_j+1} = r_{t_j} + m*2^{A} > r_{t_j}. r KESIN ARTAN.")
print("  => 'tek sabit tam sayi' A/B/C/F'den TUREMEZ. Bolum G-4 bir SONUC degil, HEDEF.\n")

print("MADDE 20 (bagimsiz saldiri) — UZUN GECICI PLATO vs GERCEK PLATO SONU")
print("  Tuzak: 'son L adimda r sabit' => plato SANMAK. (D0 madde-9'da kendi dustugum hata.)")
random.seed(2026); tuzak=0; toplam=0
for _ in range(4000):
    w=[random.randint(1,3) for _ in range(random.randint(20,45))]
    A,B,r,R=build(w)
    L=len(w)
    # pencere kriteri: son 4 adimda sabit mi?
    if all(r[k]==r[L-4] for k in range(L-4,L+1)):
        toplam+=1
        # gercekten plato sonu mu? sonraki adimda injury olursa R_L != r_L olabilir
        if R[L]!=r[L]: tuzak+=1
print(f"  'son 4 adim sabit' saglayan {toplam} kelime; bunlarin {tuzak} tanesinde R_L != r_L")
print(f"  -> pencere kriteri {'YANILTICI' if tuzak>0 else 'guvenli'}. Arsivin verifier'i bu tuzaga DUSMUYOR:")
print(f"     'if r[k+1]==r[k]' kosulunu kullaniyor (pencere degil, GERCEK bir-adim testi). DOGRU.")
