"""Exact witnesses distinguishing low-endpoint and demand collisions."""
from collections import Counter
from pathlib import Path
import json

def rows(j,R,L):
    q=3**(j+2); out=[]
    for a in range(1,R):
        B=3+2**a; Z=B*pow(2,-R,q)%q
        n,h=Z%9,Z//9
        if n<L:
            out.append(dict(word=[a,R-a],B=B,Z=Z,low=n,high=h,
                            target=(-2**R*h)%(3**j)))
    return out

w=rows(1,9,3)
assert [x['word'] for x in w]==[[2,7],[5,4],[8,1]]
assert w[0]['low']!=w[1]['low'] and w[0]['target']==w[1]['target']
assert w[0]['low']==w[2]['low'] and w[0]['target']!=w[2]['target']
energy=[]
for j,R,L,expected in [(1,8,9,(9,25)),(2,9,9,(12,8))]:
    a=rows(j,R,L)
    low=Counter(x['low'] for x in a); demand=Counter(x['target'] for x in a)
    el=sum(v*v for v in low.values()); ed=sum(v*v for v in demand.values())
    assert (el,ed)==expected
    assert ed<=L*el and el<=3**j*ed
    energy.append(dict(j=j,k=2,R=R,L=L,low_energy=el,demand_energy=ed))
out=dict(status='PASS',scope='algebraic witnesses, not critical-band evidence',
         common_parameters=dict(j=1,k=2,R=9,L=3),witnesses=w,energy_examples=energy)
Path(__file__).with_name('WITNESSES.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
