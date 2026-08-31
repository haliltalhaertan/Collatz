"""B -> sonsuz: SINIRSIZ valuation alfabesi icin pressure sabiti.
Task 7 'unbounded valuations' i hala ACIK sayiyor. Oyle mi?"""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps = 50
ALPHA = log(3)/log(2)
def l2(x): return log(x)/log(2)

# g=1 -> a in {2,3,4,...}, d=1-a in {-1,-2,-3,...}: geometrik
#        A(lam) = e^-lam/(1-e^-lam)
# g=2 -> a in {1,3,4,...}, d=2-a in {+1,-1,-2,...}
#        Bb(lam) = e^lam + e^-lam/(1-e^-lam)
def f(lam):
    q = exp(-lam)
    A  = q/(1-q)
    Bb = exp(lam) + q/(1-q)
    return (2-ALPHA)*l2(A) + (ALPHA-1)*l2(Bb)

lam = findroot(lambda L: diff(f,L), mpf('1.6'))
h_inf = f(lam)
k_inf = ALPHA/h_inf
print("SINIRSIZ ALFABE (B = sonsuz), geometrik seriler:")
print(f"  lambda*_inf = {mp.nstr(lam, 25)}")
print(f"  h_inf       = {mp.nstr(h_inf, 25)}")
print(f"  kappa_inf*  = alpha/h_inf = {mp.nstr(k_inf, 25)}")
print(f"  ikinci turev = {mp.nstr(diff(f,lam,2),8)}  "
      f"{'-> gercek minimum' if diff(f,lam,2)>0 else '-> MINIMUM DEGIL (!)'}")
print(f"  seri yakinsiyor mu? lambda* > 0: {lam>0}  (q=e^-lam={mp.nstr(exp(-lam),8)} < 1)")
print()
print(f"  B=16 degeri (onceki tablodan): 2.78401090316")
print(f"  B=sonsuz limiti              : {mp.nstr(k_inf,15)}")
print(f"  -> B->inf limiti SONLU ve pozitif.")
print()
print("SONUC: pressure argumani sinirli alfabeye BAGLI DEGIL.")
print("Eger arguman gecerliyse, SINIRSIZ valuationlu zero-critical")
print("kritik-log diziler icin de 1 < kappa < %s dislanir." % mp.nstr(k_inf,10))
print("Task 7 findings ise 'unbounded valuations' i ACIK sayiyor.")
print("=> Teorem, iddia ettiginden DAHA GENIS; kapsam ifadesi eksik.")
