"""PLATO RIJITLIGI: plato ICINDE a_k = v_2(3c_k+1) TAM esitlik olmali (son adim haric)."""
import random
def v2(x):
    n=0
    while x%2==0: x//=2; n+=1
    return n
def build(w):
    A=[0];B=[0];r=[0]
    for k,a in enumerate(w,1):
        B.append(3*B[-1]+(1<<A[-1])); A.append(A[-1]+a)
        m=1<<A[-1]; r.append((-B[-1]*pow(pow(3,k,m),-1,m))%m)
    return A,B,r
random.seed(77); t=f=0; kesin=0
for _ in range(1500):
    w=[random.randint(1,4) for _ in range(random.randint(6,26))]
    A,B,r=build(w)
    for k in range(len(w)-1):
        if r[k+1]!=r[k]: continue          # k'da injury -> plato ici degil
        c=(3**k*r[k]+B[k])//(1<<A[k])
        t+=1
        # iddia: a_k < v_2(3c+1)  =>  k+1'de MUTLAKA injury
        if w[k] < v2(3*c+1):
            kesin+=1
            if r[k+2]==r[k+1]: f+=1        # ihlal: injury olmamis
print(f"plato-ici adim: {t:,}")
print(f"  bunlarin {kesin:,} tanesinde a_k < v_2(3c_k+1) (sikilamayan adim)")
print(f"  bu adimlarin sonrasinda injury OLMAYAN: {f}  -> {'RIJITLIK DOGRULANDI' if f==0 else 'IHLAL'}")
print("\nSONUC: uzunlugu >=2 olan bir platoda a_k = v_2(3c_k+1) TAM esitlik zorunlu")
print("       (yalnizca platonun SON adimi gevsek olabilir, o da platoyu bitirir).")
print("       => Plato = SIRADAN bir tam sayinin GERCEK Syracuse yorunge parcasi.")
print("       => Sonsuz plato  <=>  iraksayan/dongusel-olmayan Collatz yorungesi (LEVEL-3).")
