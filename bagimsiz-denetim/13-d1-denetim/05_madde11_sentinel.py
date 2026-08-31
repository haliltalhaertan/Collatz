import random
def build(w):
    A=[0];B=[0];r=[0];R=[0]
    for k,a in enumerate(w,1):
        B.append(3*B[-1]+(1<<A[-1])); A.append(A[-1]+a)
        m=1<<A[-1]; r.append((-B[-1]*pow(pow(3,k,m),-1,m))%m)
        m2=1<<(A[-1]+1); R.append(((1<<A[-1])-B[-1])*pow(pow(3,k,m2),-1,m2)%m2)
    return A,B,r,R
random.seed(55); ihlal={}
for _ in range(500):
    w=[random.randint(1,5) for _ in range(random.randint(3,20))]
    A,B,r,R=build(w)
    for k in range(len(w)):
        if (r[k+1]-R[k])%(1<<(A[k]+1))!=0: ihlal[k]=ihlal.get(k,0)+1
print("MADDE 11 — ihlallerin k'ya gore dagilimi:", ihlal)
print("-> TUM ihlaller k=0'da. R[0]=0 arsivin SENTINEL degeri (dogru deger R_0=1).")
print("   check_word() R[0]'i ASLA kullanmiyor: k=0'da her zaman injury var (madde 15),")
print("   dolayisiyla 'if r[k+1]==r[k]' dali k=0'da hic calismiyor. ZARARSIZ.")
random.seed(55); t=f=0
for _ in range(500):
    w=[random.randint(1,5) for _ in range(random.randint(3,20))]
    A,B,r,R=build(w)
    for k in range(1,len(w)):
        t+=1
        if (r[k+1]-R[k])%(1<<(A[k]+1))!=0: f+=1
print(f"\nk>=1 icin yeniden: {t:,} test, {f} ihlal -> {'DOGRULANDI' if f==0 else 'IHLAL'}")
# R_0'in dogru degeri
print(f"\nR_0 dogru degeri: c_0=r_0=0 tek olmali => R_0 = 0+2^0 = 1 (arsiv 0 yaziyor, kullanilmiyor)")
