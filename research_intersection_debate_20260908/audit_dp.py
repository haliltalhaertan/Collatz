"""Exact modular arithmetic-progression quotient, retaining joint prefix/tail weights."""
from collections import defaultdict
from pathlib import Path
from time import perf_counter
import json
from fractions import Fraction
from math import ceil

def H(x):
    return (3*x+1)//2 if x&1 else x//2

def joint_dp(m,t,N0=None):
    assert m>=1 and t>=0
    if N0 is None:N0=1<<(m-1)
    assert 0<=N0<=1<<(m-1)
    if N0==0:return {},[]
    depth=1
    modulus=1<<(m+t-depth)
    states={(1,2%modulus,N0):1}
    trace=[dict(depth=depth,states=1,multiplicity=1,represented_starts=N0)]
    powers=[3**k for k in range(m+1)]
    while depth<m:
        newmod=1<<(m+t-depth-1)
        nxt=defaultdict(int)
        for (k,b,N),mult in states.items():
            for h in (0,1):
                Nh=(N+1-h)//2
                if not Nh:continue
                c=b+powers[k]*h
                p=c&1
                v=((3*c+1)//2 if p else c//2)%newmod
                nxt[k+p,v,Nh]+=mult
        states=nxt;depth+=1
        multsum=sum(states.values())
        represented=sum(N*mult for (k,b,N),mult in states.items())
        assert represented==N0
        trace.append(dict(depth=depth,states=len(states),multiplicity=multsum,
                          represented_starts=represented))
    joint=defaultdict(int)
    for (k,b,N),mult in states.items():
        assert N==1
        j=0
        for _ in range(t):
            j+=b&1;b=H(b)
        joint[k,j]+=mult
    assert sum(joint.values())==N0
    return dict(joint),trace

def direct(m,t,N0=None):
    if N0 is None:N0=1<<(m-1)
    out=defaultdict(int)
    for x in range(1,2*N0,2):
        k=j=0
        for _ in range(m):k+=x&1;x=H(x)
        for _ in range(t):j+=x&1;x=H(x)
        out[k,j]+=1
    return dict(out)

def main():
    checks=0
    partial_checks=0
    for m in range(1,13):
        for t in range(1,6):
            got,_=joint_dp(m,t)
            assert got==direct(m,t),(m,t)
            checks+=1
            for N0 in sorted(set([0,1,(1<<(m-1))//3,(1<<(m-1))-1])):
                got,_=joint_dp(m,t,N0)
                assert got==direct(m,t,N0),(m,t,N0)
                partial_checks+=1
    original=[]
    for L,expected in [(256,10),(4096,140)]:
        X=Fraction(2**15*L,3**10)
        m=1
        while 2**m<X:m+=1
        N0=max(0,ceil((X-1)/2))
        counts,_=joint_dp(m,15-m,N0)
        actual=sum(n for (k,j),n in counts.items() if k+j==10)
        assert actual==expected,(L,actual)
        original.append(dict(r=10,A=15,L=L,X=str(X),m=m,N0=N0,F=actual))
    start=perf_counter()
    counts,trace=joint_dp(20,5)
    elapsed=perf_counter()-start
    total16=sum(n for (k,j),n in counts.items() if k+j==16)
    assert total16==41142,total16
    out=dict(status='PASS',small_joint_checks=checks,partial_joint_checks=partial_checks,
             original_interval_checks=original,benchmark=dict(m=20,t=5,
             total_weight_16_count=total16,represented_starts=1<<19,
             peak_states=max(row['states'] for row in trace),
             sum_states=sum(row['states'] for row in trace),
             final_states=trace[-1]['states'],seconds=elapsed,trace=trace))
    Path(__file__).with_name('audit_dp_result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
