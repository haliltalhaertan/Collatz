"""Rigoroz rasyonel aralik sertifikasi: h_3 ve h_infinity.

Yalniz Python standart kutuphanesi kullanilir. Tum esas hesaplar Fraction ile
kesindir. ln(y), y>0 icin ln(y)=2*sum z^(2n+1)/(2n+1), z=(y-1)/(y+1)
serisi ve geometrik kuyruk ust siniri kullanilir. Kayan nokta proof-critical
kararlarda kullanilmaz.
"""
from fractions import Fraction as F

LOG_TERMS = 260

def I(lo, hi=None): return (lo, lo if hi is None else hi)
def iadd(a,b): return (a[0]+b[0], a[1]+b[1])
def ineg(a): return (-a[1], -a[0])
def isub(a,b): return iadd(a,ineg(b))
def imul(a,b):
    vals=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return (min(vals),max(vals))
def idiv(a,b):
    if b[0] <= 0 <= b[1]: raise ZeroDivisionError("interval contains zero")
    return imul(a,(F(1,1)/b[1],F(1,1)/b[0]))
def iscale(a,c): return imul(a,I(F(c)))

def ln_bounds(y, terms=LOG_TERMS):
    if y <= 0: raise ValueError("ln domain")
    z=(y-1)/(y+1); z2=z*z; term=z; partial=F(0)
    for n in range(terms):
        partial += term/F(2*n+1); term *= z2
    partial *= 2
    az=abs(z)
    rem=2*(az**(2*terms+1))/F(2*terms+1)/(1-az*az)
    return (partial-rem,partial+rem)

def ln_interval(a): return (ln_bounds(a[0])[0],ln_bounds(a[1])[1])

def decimal_floor(q,digits=36):
    scale=10**digits; n=(q.numerator*scale)//q.denominator; s=str(n).rjust(digits+1,"0")
    return s[:-digits]+"."+s[-digits:]
def decimal_ceil(q,digits=36):
    scale=10**digits; num=q.numerator*scale; n=(num+q.denominator-1)//q.denominator; s=str(n).rjust(digits+1,"0")
    return s[:-digits]+"."+s[-digits:]

LN2=ln_bounds(F(2)); LN3=ln_bounds(F(3)); ALPHA=idiv(LN3,LN2)
C1=isub(I(F(2)),ALPHA); C2=isub(ALPHA,I(F(1)))

def derivative_h3(x):
    t1=idiv(isub(I(F(3)),iscale(ALPHA,2)),I(x))
    t2=idiv(C1,I(1+x))
    t3=idiv(iscale(imul(C2,I(x)),2),I(1+x*x))
    return iadd(iadd(t1,t2),t3)

def derivative_hinf(x):
    t1=idiv(isub(I(F(3)),iscale(ALPHA,2)),I(x))
    t2=I(F(1,1-x))
    t3=imul(C2,I(F(2*x-1,1-x+x*x)))
    return iadd(iadd(t1,t2),t3)

def h3_interval(L,U):
    arg_a=(L*(1+L),U*(1+U)); arg_b=(U+F(1,U),L+F(1,L))
    return idiv(iadd(imul(C1,ln_interval(arg_a)),imul(C2,ln_interval(arg_b))),LN2)

def hinf_interval(L,U):
    arg_a=(L/F(1-L),U/F(1-U)); B=lambda x:(1-x+x*x)/(x*(1-x)); arg_b=(B(U),B(L))
    return idiv(iadd(imul(C1,ln_interval(arg_a)),imul(C2,ln_interval(arg_b))),LN2)

def certify(name,center,derivative,evaluator):
    c=F(center); eps=F(1,10**35); L,U=c-eps,c+eps
    dL=derivative(L); dU=derivative(U)
    if not dL[1] < 0: raise AssertionError(f"{name}: left derivative is not rigorously negative")
    if not dU[0] > 0: raise AssertionError(f"{name}: right derivative is not rigorously positive")
    h=evaluator(L,U); kappa=idiv(ALPHA,h)
    return L,U,h,kappa

CERTS={
 "h_3":certify("h_3","0.2727193458208187674766070241526830608436",derivative_h3,h3_interval),
 "h_infinity":certify("h_infinity","0.2025445839318756265276280767546863855878979652759160322558509",derivative_hinf,hinf_interval),
}

print("RATIONAL INTERVAL PRESSURE CERTIFICATE: PASS")
print(f"ln-series terms={LOG_TERMS}")
print(f"alpha in [{decimal_floor(ALPHA[0])}, {decimal_ceil(ALPHA[1])}]")
for name,(L,U,h,kappa) in CERTS.items():
    print(f"{name} minimizer x in [{decimal_floor(L)}, {decimal_ceil(U)}]")
    print(f"{name} in [{decimal_floor(h[0])}, {decimal_ceil(h[1])}]")
    print(f"alpha/{name} in [{decimal_floor(kappa[0])}, {decimal_ceil(kappa[1])}]")
