"""Residue-stratified centered bounds on the fixed exact-join panel."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from collections import Counter
from math import comb,isqrt
import importlib.util,json,hashlib

root=Path(__file__).resolve().parent
impl=root.parent/'research_exact_join_20260908/run.py'
spec=importlib.util.spec_from_file_location('join_source',impl)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
nums=mod.numerators
src=root.parent/'research_exact_join_20260908/RESULT.json'
raw=src.read_bytes();prior=json.loads(raw)

def bound(P,D,j,depth):
    def visit(c,level):
        modulus=3**level; size=3**(j-level)
        p=[v for t,v in P.items() if t%modulus==c]
        d=[v for t,v in D.items() if t%modulus==c]
        n,C=sum(p),sum(d)
        if not n or not C:return 0
        X=size*sum(v*v for v in p)-n*n
        Y=size*sum(v*v for v in d)-C*C
        assert X>=0 and Y>=0
        z=X*Y; s=isqrt(z); s+=int(s*s<z)
        parent=(n*C+s+size-1)//size
        if level==min(depth,j):return parent
        children=sum(visit(c+v*modulus,level+1) for v in range(3))
        return min(parent,children)
    return visit(0,0)

rows=[]
for row in prior['rows']:
    r,A,L,j,k=(row[x] for x in ('r','A','L','j','k'))
    total=[0,0,0];exact=0;demand0=0;terms=[]
    for R in range(k,A-j+1):
        a=A-R;M=3**j
        P=Counter(B*pow(2,-a,M)%M for B in nums(j,a));D=Counter()
        for B in nums(k,R):
            Z=B*pow(2,-R,3**r)%(3**r)
            n=Z%(3**k)
            if n<L:D[(-2**R*(Z//(3**k)))%M]+=1
        pc=[sum(v for t,v in P.items() if t%3==c) for c in range(3)]
        if j==1:
            formula=[0,0,0];formula[pow(2,-a,3)]=1
        else:
            formula=[0,0,0]
            for m in range(1,a-j+2):
                formula[pow(2,-m,3)]+=comb(a-m-1,j-2)
        assert pc==formula and pc[0]==0
        Q=sum(v*D[t] for t,v in P.items());exact+=Q
        levels=[bound(P,D,j,s) for s in (0,1,2)]
        assert Q<=levels[2]<=levels[1]<=levels[0]
        assert bound(P,D,j,j)==Q
        dc=[sum(v for t,v in D.items() if t%3==c) for c in range(3)]
        demand0+=dc[0]
        for s in range(3):total[s]+=levels[s]
        terms.append(dict(R=R,prefix_class_counts=pc,demand_class_counts=dc,Q=Q,bounds=levels))
    assert exact==row['Q']
    rows.append(dict(r=r,A=A,b=row['b'],L=L,j=j,k=k,N=row['N'],Q=exact,
        bounds=total,rejected_nonunit_demands=demand0,terms=terms))
out=dict(status='PASS',cases=len(rows),source_sha256=hashlib.sha256(raw).hexdigest(),
    imported_code_sha256=hashlib.sha256(impl.read_bytes()).hexdigest(),rows=rows)
(root/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status='PASS',cases=len(rows),
    depth1_improved=sum(x['bounds'][1]<x['bounds'][0] for x in rows),
    depth2_improved=sum(x['bounds'][2]<x['bounds'][1] for x in rows),
    nonfull_depth2_rows=sum(x['j']>2 for x in rows),
    examples=[{k:v for k,v in x.items() if k!='terms'} for x in rows if x['r']==10 and x['A']==15]),indent=2))
