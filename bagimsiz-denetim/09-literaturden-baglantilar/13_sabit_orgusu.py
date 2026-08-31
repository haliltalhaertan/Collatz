"""Arsivde ortaya cikan TUM sabitler arasinda sistematik iliski taramasi."""
from mpmath import mp, mpf, exp, log, findroot, diff, sqrt
mp.dps=40
A=log(3)/log(2)
def l2(x): return log(x)/log(2)
def hB(B):
    if B==0:
        f=lambda L:(2-A)*l2(exp(-L)/(1-exp(-L)))+(A-1)*l2(exp(L)+exp(-L)/(1-exp(-L)))
    else:
        f=lambda L:(2-A)*l2(sum(exp(L*(1-a)) for a in range(2,B+1)))+(A-1)*l2(sum(exp(L*(2-a)) for a in range(1,B+1) if a!=2))
    lam=findroot(lambda L:diff(f,L),mpf('1.5')); return f(lam)

S={
 "alpha=log2(3)"      : A,
 "alpha-1 (Sturm egim)": A-1,
 "2-alpha"            : 2-A,
 "1/(alpha-1) Dubickas": 1/(A-1),
 "h_3"                : hB(3),
 "h_4"                : hB(4),
 "h_inf"              : hB(0),
 "h(alpha) geometrik" : A*l2(A)/A if False else l2(A)+(A-1)*(l2(A)-l2(A-1)),
 "K17"                : mpf('2.742881438765941863306095'),
 "K11"                : mpf('4.91656355094999688084663'),
 "kappa_3*"           : A/hB(3),
 "kappa_inf*"         : A/hB(0),
 "kappa_0 (CP19T4)"   : mpf('1.0526808586079717'),
 "pi^2/48"            : mp.pi**2/48,
}
print("SABIT HAVUZU")
for k,v in S.items(): print(f"  {k:<22} {mp.nstr(v,18)}")

print("\nSISTEMATIK ILISKI TARAMASI (12+ basamak eslesme)")
ks=list(S); bulunan=[]
import itertools
for i,j in itertools.permutations(range(len(ks)),2):
    a,b=S[ks[i]],S[ks[j]]
    if b==0: continue
    for ad,val in (("/",a/b),("-",a-b),("*",a*b),("+",a+b)):
        for k2 in range(len(ks)):
            c=S[ks[k2]]
            if abs(val-c)<mpf('1e-12') and not (ad in "+*" and i>j):
                if ks[i]!=ks[k2] and ks[j]!=ks[k2]:
                    bulunan.append(f"  {ks[i]} {ad} {ks[j]}  =  {ks[k2]}   ({mp.nstr(val,15)})")
for b in sorted(set(bulunan)): print(b)

print("\nBASIT SAYILARLA ILISKILER")
for k,v in S.items():
    for c,ad in ((mpf(2),"2"),(mpf(3),"3"),(A,"alpha"),((A+2)/2,"(alpha+2)/2"),(mpf(1)/2,"1/2")):
        r=v/c
        for k2,v2 in S.items():
            if k2!=k and abs(r-v2)<mpf('1e-12'):
                print(f"  {k} / {ad} = {k2}")

print("\nYAKIN AMA ESIT OLMAYANLAR (0.1'den yakin, ama >1e-12)")
for i,j in itertools.combinations(range(len(ks)),2):
    a,b=S[ks[i]],S[ks[j]]
    d=abs(a-b)
    if mpf('1e-12')<d<mpf('0.06'):
        print(f"  {ks[i]:<22} {mp.nstr(a,12):>16}   vs {ks[j]:<22} {mp.nstr(b,12):>16}   fark {mp.nstr(d,6)}")
