"""
D1 — 'exact-realizer plato' insa edilebilir mi?  VE bedeli nedir?
Bagimsiz iddia: w=(a_0..a_{L-1}) kelimesini gerceklestiren EN KUCUK pozitif tam sayi
tam olarak r_L(w) = -3^{-L}B_L mod 2^{A_L}'dir.
"""
import random, math
def v2(x):
    n=0
    while x%2==0: x//=2; n+=1
    return n
def rL(w):
    A=0;B=0
    for ak in w:
        B=3*B+2**A; A+=ak
    m=1<<A
    return (-B*pow(pow(3,len(w),m),-1,m))%m, A

print("A) 'en kucuk realizer = r_L' iddiasi — brute force ile kiyas")
random.seed(3); t=f=0
for _ in range(120):
    L=random.randint(2,7); w=[random.randint(1,3) for _ in range(L)]
    r,A=rL(w)
    if A>22: continue
    found=None
    for c0 in range(1,1<<A):
        x=c0; good=True
        for ak in w:
            if v2(3*x+1)<ak: good=False;break
            x=(3*x+1)>>ak
        if good: found=c0;break
    t+=1
    exp = r if r>0 else (1<<A)
    if found!=exp: f+=1; print(f"   FARK w={w} brute={found} r_L={r}")
print(f"   {t} kelime, {f} fark -> {'DOGRULANDI' if f==0 else 'IHLAL'}")

print("\nB) PLATO BEDELI — L uzadikca realizer ne kadar buyuyor?")
print(f"   {'L':>5} {'A_L':>6} {'log2 r_L':>10} {'log2 r_L / L':>13} {'ln3':>8}")
random.seed(9)
for L in (10,25,50,100,200,400,800,1600):
    w=[random.choice([1,1,2]) for _ in range(L)]      # alpha-tipik kelime
    r,A=rL(w)
    print(f"   {L:>5} {A:>6} {r.bit_length():>10} {r.bit_length()/L:>13.6f} {math.log(3)/math.log(2):>8.6f}")
print("   -> log2 r_L / L -> A_L/L ~ alpha.  Yani ln(1+r_*)/L -> ln2*alpha = ln3.")

print("\nC) SONUC: uzun plato KURULABILIR ama rho_r'yi DUSURMEZ")
print("   Plato [t_j+1, t_{j+1}] boyunca r sabit = r_*, log2 r_* ~ A_{t_j+1} ~ alpha*t_j")
print("   rho_r(k) = ln(1+r_*)/k, k=t_{j+1}'de minimum: ~ ln3 * t_j / t_{j+1}")
print("   liminf rho_r = 0 icin t_j/t_{j+1} -> 0, yani plato uzunlugu t_{j+1}-t_j")
print("   ONCEKI TUM tarihe gore super-lineer buyumeli.")
print("\nD) Boyle bir plato dizisi kurulabilir mi? -> gereken kelime uzunlugu")
print(f"   {'j':>3} {'t_j':>10} {'t_{j+1}':>12} {'plato uzunlugu':>15} {'gereken realizer bit':>21}")
tj=10
for j in range(1,9):
    tj1=tj*tj if tj<10**6 else tj*10
    print(f"   {j:>3} {tj:>10,} {tj1:>12,} {tj1-tj:>15,} {int(1.585*tj):>21,}")
    tj=tj1
    if tj>10**8: break
print("   -> t_{j+1}=t_j^2 gibi bir buyume gerekli; her plato'nun realizer'i onceki")
print("      tarihin tamamini tasiyan tek bir tam sayi. Bu LEVEL-3 probleminin ta kendisi.")
