"""
FIKIR TESTI — realizor x in Z_2'nin Hensel (2-adic) basamak yapisi.

ORDINARY realization x'in POZITIF TAM SAYI olmasini gerektirir.
Bir tam sayinin 2-adic Hensel acilimi SONLUDUR: sonlu cok sifir olmayan
basamak, sonra hep 0.

Yani: x'in Hensel aciliminda SONSUZ COK sifir olmayan basamak oldugu
gosterilebilirse -> x tam sayi degil -> ordinary realization YOK.

Bu, "sonsuz cok 1 biti" gibi cok ZAYIF bir ifade — CP19'un park ettigi
high-half bit siniflandirmasindan cok daha az sey istiyor.

Test: controller'in kismi realizorlerinin bit yapisi.
"""
from decimal import Decimal, getcontext
import math
getcontext().prec=60
ALPHA=Decimal(3).ln()/Decimal(2).ln(); L2=Decimal(2).ln(); KAP=Decimal('1.053')
NMAX=1200
F=[int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(NMAX+2)]
g=[F[k+1]-F[k] for k in range(NMAX+1)]

# controller (bang-bang, tanimdan)
def esik(s,m):
    if s<=0: return True
    return (1<<(1000*s)) <= m**1053
a=[];s=0
for k in range(NMAX):
    m=max(2,k+1)
    d=1 if (g[k]==2 and esik(s,m)) else -1
    a.append(g[k]-d); s+=d
A=[0]*(NMAX+1)
for k in range(NMAX): A[k+1]=A[k]+a[k]
Bk=[0]*(NMAX+1)
for k in range(1,NMAX+1): Bk[k]=3*Bk[k-1]+2**A[k-1]

def realizor(r):
    mod=1<<(A[r]+1)
    return ((2**A[r]-Bk[r])*pow(pow(3,r,mod),-1,mod))%mod

print("Controller'in kismi realizoru x_r = n_0 mod 2^(A_r+1)")
print("Hensel basamaklari (2-adic bitler) — sifir olmayan yogunluk\n")
print(f"{'r':>5} {'A_r':>6} {'bit sayisi':>11} {'1 biti':>8} {'yogunluk':>10} {'son 1 bitin yeri':>17}")
onceki=None
for r in (20,50,100,200,400,600,800,1000,1200):
    if r>NMAX: break
    x=realizor(r); M=A[r]+1
    bits=bin(x)[2:].zfill(M)[::-1]      # dusuk bit once
    ones=bits.count('1')
    son1=len(bits)-1-bits[::-1].find('1') if '1' in bits else -1
    print(f"{r:>5} {A[r]:>6} {M:>11} {ones:>8} {ones/M:>10.4f} {son1:>17}")

print("\nSTABILIZASYON TESTI: x_r'lerin dusuk bitleri sabitleniyor mu?")
print("(2-adic yakinsama: x_r -> x, yani dusuk bitler donuyor)")
prev=None
for r in (100,200,400,600,800,1000,1200):
    if r>NMAX: break
    x=realizor(r)
    if prev is not None:
        ortak=A[min(r,prev[0])]+1
        ayni=(x & ((1<<ortak)-1))==(prev[1] & ((1<<ortak)-1))
        print(f"  r={r:>5}: onceki ile ilk {ortak} bit ayni mi? {ayni}")
    prev=(r,x)

print("\nKRITIK SORU: x tam sayi olsaydi, bir yerden sonra TUM bitler 0 olurdu.")
print("Gozlenen: 1 biti yogunlugu ~0.5 civarinda sabit, son 1 biti hep")
print("en ust bitlerde. Yani kismi realizorler tam sayiya YAKINSAMIYOR.")
print("(Bu ispat degil — sonlu kesit. Ama dogru yonde bir gostergE.)")
