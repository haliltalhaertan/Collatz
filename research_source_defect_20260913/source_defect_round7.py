from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path
import json, time

HERE=Path(__file__).resolve().parent

def H(x:int)->int:
    return (3*x+1)//2 if x&1 else x//2

def source_histograms(m:int,Smax:int):
    q=1<<Smax
    full=defaultdict(lambda:[0]*q)
    for h in range(1,1<<m,2):
        x=h;k=0
        for _ in range(m):
            if x&1:k+=1
            x=H(x)
        full[k][x%q]+=1
    out={}
    for k,arr in full.items():
        for s in range(1,Smax+1):
            qs=1<<s;a=[0]*qs
            for z,c in enumerate(arr):
                if c:a[z%qs]+=c
            out[k,s]=a
    return out

def J(arr):
    n=len(arr);h=n//2
    return h*sum((arr[u]-arr[u+h])**2 for u in range(h))

def corr_shift(arr,d):
    n=len(arr);d%=n
    return sum(arr[u]*arr[(u+d)%n] for u in range(n))

def Eop(P,c,s):
    N=1<<(s+1);q=1<<s;c%=N
    return [P[(2*z)%N]+P[(2*z-c)%N] for z in range(q)]

def Oop(P,c,s):
    N=1<<(s+1);q=1<<s;c%=N;r=pow(3,-1,N)
    return [P[(r*(2*z-1))%N]+P[(r*(2*z-1)-c)%N] for z in range(q)]

def row(m,s,hin,hout):
    N=1<<(s+1);q=1<<s;half=N//2
    I=Fraction();F=Fraction();Lphysical=Fraction()
    Ec={};Oc={}
    for k in range(1,m+1):
        nk=comb(m-1,k-1)
        P=hin.get((k,s+1),[0]*N)
        I += Fraction(J(P),nk)
        c=pow(3,k,N)
        Ec[k]=Eop(P,c,s);Oc[k]=Oop(P,c,s)
        F += Fraction(J(Ec[k])+J(Oc[k]),nk)
        Lphysical += Fraction(half*(corr_shift(P,c)-corr_shift(P,c+half)),nk)
    Out=Fraction()
    for k in range(1,m+2):
        nout=comb(m,k-1)
        Out += Fraction(J(hout.get((k,s),[0]*q)),nout)
    Mphysical=Fraction()
    for k in range(2,m+1):
        a=comb(m-1,k-1);b=comb(m-1,k-2)
        diff=[b*Ec[k][z]-a*Oc[k-1][z] for z in range(q)]
        Mphysical += Fraction(J(diff),a*b*(a+b))
    L=F-I;M=F-Out;D=I-Out
    assert L==Lphysical
    assert M==Mphysical
    assert D==M-L
    return dict(m=m,s=s,input=str(I),fine=str(F),output=str(Out),
                lift=str(L),merge=str(M),defect=str(D),
                output_over_input=str(Out/I) if I else None,
                merge_over_lift=str(M/L) if L>0 else None)

def arbitrary_nonnegative_counterexample():
    m=3;s=2;N=8;q=4
    P={
      1:[0,0,1,0,0,0,0,0],
      2:[1,0,0,0,0,0,0,1],
      3:[0,0,0,0,1,0,0,0],
    }
    Ec={};Oc={};I=Fraction();F=Fraction()
    for k in range(1,m+1):
        nk=comb(m-1,k-1);c=pow(3,k,N)
        I+=Fraction(J(P[k]),nk)
        Ec[k]=Eop(P[k],c,s);Oc[k]=Oop(P[k],c,s)
        F+=Fraction(J(Ec[k])+J(Oc[k]),nk)
    Out=Fraction()
    for k in range(1,m+2):
        arr=[a+b for a,b in zip(Ec.get(k,[0]*q),Oc.get(k-1,[0]*q))]
        Out+=Fraction(J(arr),comb(m,k-1))
    return dict(m=m,s=s,histograms=P,input=str(I),fine=str(F),output=str(Out),
                lift=str(F-I),merge=str(F-Out),defect=str(I-Out),output_over_input=str(Out/I))

def main():
    started=time.perf_counter()
    cache={m:source_histograms(m,11) for m in range(2,23)}
    prescribed=[]
    for m in range(2,19):
        for s in range(1,min(8,m-1)+1):
            prescribed.append(row(m,s,cache[m],cache[m+1]))
    posthoc=[]
    for m in range(10,19):
        for s in (9,10):
            if s<=m-1:posthoc.append(row(m,s,cache[m],cache[m+1]))
    for m in range(19,22):
        for s in range(1,11):
            posthoc.append(row(m,s,cache[m],cache[m+1]))
    allrows=prescribed+posthoc
    for r in allrows: assert Fraction(r['defect'])>=0
    positive=[r for r in allrows if Fraction(r['lift'])>0]
    min_ml=min((Fraction(r['merge'])/Fraction(r['lift']),r['m'],r['s']) for r in positive)
    max_oi=max((Fraction(r['output'])/Fraction(r['input']),r['m'],r['s']) for r in allrows if Fraction(r['input']))
    ce=arbitrary_nonnegative_counterexample()
    assert Fraction(ce['output'])>Fraction(ce['input'])
    out={
      'status':'PASS',
      'theorem_checks':{
        'prescribed_cases':len(prescribed),'posthoc_stress_cases':len(posthoc),'total_cases':len(allrows),
        'identity_L_equals_physical_shift_form':'PASS all rows',
        'identity_M_equals_weighted_merge_slack':'PASS all rows',
        'identity_input_minus_output_equals_M_minus_L':'PASS all rows'},
      'actual_source_diagnostics':{
        'positive_lift_cases':len(positive),'positive_lift_rows':positive,
        'minimum_merge_over_lift_when_lift_positive':str(min_ml[0]),
        'minimum_location':{'m':min_ml[1],'s':min_ml[2]},
        'maximum_output_over_input':str(max_oi[0]),'maximum_location':{'m':max_oi[1],'s':max_oi[2]}},
      'generic_nonnegative_counterexample':ce,'prescribed_rows':prescribed,'posthoc_rows':posthoc,
      'elapsed_seconds':time.perf_counter()-started,'real_subagents':False,'paid_provider_calls':False}
    (HERE/'RESULTS.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    summary={'status':'PASS','prescribed_cases':len(prescribed),'posthoc_cases':len(posthoc),
      'positive_lift_cases':len(positive),'min_M_over_L_positive':str(min_ml[0]),
      'generic_counterexample_output_over_input':ce['output_over_input'],'elapsed_seconds':out['elapsed_seconds']}
    (HERE/'RESULTS_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
