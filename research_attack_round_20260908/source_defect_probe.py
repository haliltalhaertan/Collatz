"""Only the preassigned r=5..12, critical masses +/-1 grid; exact arithmetic."""
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

def prefixes(m):
    counts=Counter()
    for h in range(1,1<<m,2):
        x=h;k=0
        for _ in range(m):
            k+=x&1
            x=(3*x+1)//2 if x&1 else x//2
        counts[k,x]+=1
    return counts

def panel(r,A,m,raw):
    t=A-m;q=1<<t
    P=Counter()
    for (k,x),count in raw.items():P[k,x%q]+=count
    D=F(0); D2=F(0); layers=[]
    for k in range(max(1,r-t),min(m,r)+1):
        N=comb(m-1,k-1); c=comb(t,r-k)
        assert sum(P[k,z] for z in range(q))==N
        e=F(sum(P[k,z]**2 for z in range(q)))-F(N*N,q)
        contribution=e*F(c*(q-c),q*q)
        D+=contribution
        contribution2=e*F(c*c,q*q)
        D2+=contribution2
        layers.append(dict(k=k,N=N,e=str(e),contribution=str(contribution),contribution_D2=str(contribution2)))
    B=F(comb(A-1,r-1),q)
    assert D2<=D
    return dict(r=r,A=A,m=m,t=t,B=str(B),Dsrc=str(D),D2=str(D2),D2_ratio=str(D2/B),ratio=str(D/B),
                violates=D>B,layers=layers)

def main():
    panels=[];skipped=[]
    for r in range(5,13):
        m=(6*r+4)//5
        # floor(log2(3)*r) computed without floating point.
        critical=(3**r).bit_length()-1
        raw=prefixes(m)
        for d in [-1,0,1]:
            A=critical+d
            if A-m<1:
                skipped.append(dict(r=r,A=A,m=m,reason='t<1'));continue
            panels.append(panel(r,A,m,raw))
    violations=[p for p in panels if p['violates']]
    out=dict(scope='Fixed r5..12, A=floor(alpha*r)+d, d=-1,0,1, m=ceil(1.2*r), t>=1',
             panels=panels,skipped=skipped,violations=violations,
             first_violation=violations[0] if violations else None,
             max_ratio_panel=max(panels,key=lambda p:F(p['ratio'])))
    Path(__file__).with_name('SOURCE_DEFECT_PROBE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(tested=len(panels),skipped=skipped,
        violations=[{k:p[k] for k in ['r','A','m','t','B','Dsrc','ratio']} for p in violations],
        max_ratio={k:out['max_ratio_panel'][k] for k in ['r','A','m','t','B','Dsrc','ratio']}),indent=2))

if __name__=='__main__':main()
