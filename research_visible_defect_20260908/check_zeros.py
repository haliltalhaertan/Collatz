"""Exact coefficient test for primitive power-of-two Fourier zeros."""
from math import comb
from pathlib import Path
import json

def H(x):return (3*x+1)//2 if x&1 else x//2
def K(x,t):
    k=0
    for _ in range(t):k+=x&1;x=H(x)
    return k
def C(n,k):return comb(n,k) if 0<=k<=n else 0

def main():
    checks=0;zeros=[]
    for t in range(1,11):
        full=[K(z,t) for z in range(1<<t)]
        for s in range(1,t+1):
            q=1<<s;prefix=[K(z,s) for z in range(q)]
            for j in range(t+1):
                f=[C(t-s,j-h) for h in prefix]
                direct=[sum(full[z]==j for z in range(u,1<<t,q)) for u in range(q)]
                assert f==direct
                iszero=f[:q//2]==f[q//2:]
                assert iszero==(s==1 and 2*j==t),(t,j,s)
                if iszero:zeros.append(dict(t=t,j=j,s=s))
                checks+=1
    out=dict(status='PASS',conductor_cases=checks,scope='1<=t<=10,0<=j<=t,1<=s<=t',
        method='direct tail residue counts vs binomial lift; exact cyclotomic divisibility by equal halves',zeros=zeros)
    Path(__file__).with_name('ZERO_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
