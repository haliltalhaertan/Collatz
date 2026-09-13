from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def H(x):return (3*x+1)//2 if x&1 else x//2

def J(a):
    n=len(a);h=n//2
    return h*sum((a[u]-a[u+h])**2 for u in range(h))

def corr(a,d):
    n=len(a);d%=n
    return sum(a[u]*a[(u+d)%n] for u in range(n))

def direct_categories(m,s):
    N=1<<(s+1);q=1<<s
    Pin=defaultdict(lambda:[0]*N)
    E=defaultdict(lambda:[0]*q);O=defaultdict(lambda:[0]*q)
    for h in range(1,1<<m,2):
        x=h;k=0
        for _ in range(m):
            k+=x&1;x=H(x)
        Pin[k][x%N]+=1
        xl=h+(1<<m);yl=xl;kl=0
        for _ in range(m):
            kl+=yl&1;yl=H(yl)
        assert kl==k and abs(yl-x)==3**k
        for y in (x,yl):
            if y&1: O[k][H(y)%q]+=1
            else: E[k][H(y)%q]+=1
    Pout=defaultdict(lambda:[0]*q)
    for k in range(1,m+1):
        for z,c in enumerate(E[k]):Pout[k][z]+=c
        for z,c in enumerate(O[k]):Pout[k+1][z]+=c
    return Pin,E,O,Pout

def check(m,s):
    N=1<<(s+1);half=N//2;q=1<<s
    P,E,O,Pout=direct_categories(m,s)
    I=Fraction();F=Fraction();L=Fraction()
    for k in range(1,m+1):
        n=comb(m-1,k-1);c=pow(3,k,N)
        I+=Fraction(J(P[k]),n)
        F+=Fraction(J(E[k])+J(O[k]),n)
        L+=Fraction(half*(corr(P[k],c)-corr(P[k],c+half)),n)
    Out=sum((Fraction(J(Pout[k]),comb(m,k-1)) for k in range(1,m+2)),Fraction())
    M=Fraction()
    for k in range(2,m+1):
        a=comb(m-1,k-1);b=comb(m-1,k-2)
        diff=[b*E[k][z]-a*O[k-1][z] for z in range(q)]
        M+=Fraction(J(diff),a*b*(a+b))
    assert F-I==L
    assert F-Out==M
    assert I-Out==M-L
    return I,F,Out,L,M

rows=0
for m in range(2,13):
    for s in range(1,min(6,m-1)+1):
        check(m,s);rows+=1
out={'status':'PASS','cases':rows,'method':'direct enumeration of both lifted starts; no import of producer transfer code','same_session_second_implementation':True,'independent_agent_audit':False}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
