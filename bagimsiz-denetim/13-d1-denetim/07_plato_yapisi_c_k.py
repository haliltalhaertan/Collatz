"""
D1 PLATO YAPISI — injury-free adimin TAM karakterizasyonu.
Iddia (bagimsiz turetim):
   c_k := (3^k r_k + B_k)/2^{A_k}   tam sayi
   injury YOK (r_{k+1}=r_k)  <=>  a_k <= v_2(3 c_k + 1)
   ve bu durumda  c_{k+1} = (3 c_k + 1)/2^{a_k}
Yani plato = c'nin GERCEK bir Syracuse yorungesi.
"""
import random
def v2(x):
    n=0
    while x%2==0: x//=2; n+=1
    return n

random.seed(101)
t=f1=f2=f3=0
for _ in range(800):
    a=[random.randint(1,5) for _ in range(random.randint(4,22))]
    A=[0];B=[0];r=[0]
    for k,ak in enumerate(a):
        B.append(3*B[k]+2**A[k]); A.append(A[k]+ak)
        m=1<<A[k+1]
        r.append((-B[k+1]*pow(pow(3,k+1,m),-1,m))%m)
    for k in range(len(a)):
        num=3**k*r[k]+B[k]
        t+=1
        if num % (1<<A[k]) != 0: f1+=1; continue
        c=num//(1<<A[k])
        # iddia 1: karakterizasyon
        if (r[k+1]==r[k]) != (a[k] <= v2(3*c+1)): f2+=1
        # iddia 2: injury yoksa c_{k+1}=(3c_k+1)/2^{a_k}
        if r[k+1]==r[k]:
            cn=(3**(k+1)*r[k+1]+B[k+1])//(1<<A[k+1])
            if cn != (3*c+1)//(1<<a[k]): f3+=1
print(f"test {t:,}")
print(f"  c_k tam sayi degil        : {f1}")
print(f"  karakterizasyon ihlali    : {f2}")
print(f"  c-rekursiyon ihlali       : {f3}")
print(f"  -> {'HER UC IDDIA DOGRULANDI' if f1==f2==f3==0 else 'IHLAL VAR'}")

print("\n--- SONUC 1: r_0=0 icin c_0=0, 3*0+1=1, v_2(1)=0 => a_0<=0 imkansiz")
print("    yani ILK adim HER ZAMAN injury.  (Manager madde 15'in tam nedeni.)")

print("\n--- SONUC 2: verilen HERHANGI bir kelime icin plato realizer'i var mi?")
# Terras/Everett: c mod 2^{A_L} -> (a_0..a_{L-1}) bijeksiyon.
def realizer(word):
    """v_2(3c_i+1) >= a_i olan en kucuk pozitif c bul (tam esitlik degil, >=)."""
    A=0; c=0; mod=1
    for ak in word:
        # 3c+1 = 0 mod 2^{ak}  ->  c = -3^{-1} mod 2^{ak}  (mevcut c mod 'mod' ile uyumlu)
        m2=1<<ak
        # c yeni = c + mod*x ; 3(c+mod*x)+1 = 0 mod m2
        if mod>=m2:
            if (3*c+1)%m2!=0: return None
        else:
            g=m2//mod
            # 3*mod*x = -(3c+1) mod m2
            need=(-(3*c+1))%m2
            if need%mod!=0: return None
            x=(need//mod)*pow((3*mod//mod)%g,-1,g)%g if g>1 else 0
            if g>1:
                x=( (need//mod) * pow(3%g,-1,g) )%g
            c=c+mod*x
            mod=m2
        c=(3*c+1)//m2
        mod=max(mod//m2,1)
        A+=ak
    return c
for L in (5,10,20,40,80):
    w=[1]*L
    # dogrudan: c_0 oyle ki v_2(3c+1)>=1 her adimda -> Syracuse a=1 kelimesi
    # daha genel: rastgele kelime
    random.seed(L)
    w=[random.randint(1,3) for _ in range(L)]
    # ileri-geri: c mod 2^{sum} 'i adim adim cozelim
    c=0; mod=1; A=0; ok=True
    cur=0  # c_0 mod 2^A
    # brute: c_0'i 2^{A} icinde ara (A kucukse)
    S=sum(w)
    if S<=24:
        found=None
        for c0 in range(1,1<<S):
            x=c0; good=True
            for ak in w:
                if v2(3*x+1)<ak: good=False;break
                x=(3*x+1)>>ak
            if good: found=c0;break
        print(f"  L={L:<3} kelime toplami A={S:<3} en kucuk realizer c_0 = {found}   log2 = {found.bit_length() if found else '-'}")
    else:
        print(f"  L={L:<3} A={S:<3} (brute force cok buyuk, atlandi)")
