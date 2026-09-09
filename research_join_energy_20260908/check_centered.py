"""Exact centered moment bounds on the previously fixed split-join panel."""
from pathlib import Path
from math import isqrt,log2
from fractions import Fraction
import hashlib,json

root=Path(__file__).resolve().parent
source=root.parent/'research_exact_join_20260908/RESULT.json'
raw=source.read_bytes(); prior=json.loads(raw)
rows=[]
for row in prior['rows']:
    m=3**row['j']; bound=0; terms=[]
    for a in row['terms']:
        n,C=a['prefix_words'],a['suffix_candidates']
        X=m*a['prefix_energy']-n*n
        Y=m*a['demand_energy']-C*C
        assert X>=0 and Y>=0
        z=X*Y; upper_sqrt=isqrt(z)
        upper_sqrt+=int(upper_sqrt*upper_sqrt<z)
        term=(n*C+upper_sqrt+m-1)//m
        assert a['exact']<=term<=a['cs_bound']
        bound+=term
        terms.append(dict(R=a['R'],prefix_excess_numerator=X,
            demand_excess_numerator=Y,mean_term=str(Fraction(n*C,m)),
            centered_bound=term,raw_bound=a['cs_bound'],exact=a['exact']))
    assert row['Q']<=bound<=row['cs_bound']
    rows.append(dict(r=row['r'],A=row['A'],b=row['b'],j=row['j'],k=row['k'],
        L=row['L'],N=row['N'],Q=row['Q'],raw_bound=row['cs_bound'],
        centered_bound=bound,terms=terms))
alpha=log2(3); h=alpha*log2(alpha)-(alpha-1)*log2(alpha-1)
b,kappa=1.2,1.053
calibration=dict(alpha=alpha,h=h,b=b,kappa=kappa,
    conditional_raw_loss_floor=(alpha-h)*(1-b/alpha)/2,
    allowed_loss=alpha-h-b*(1-1/kappa),
    conditional_optimum_b=alpha*alpha/(alpha+h),
    conditional_kappa_ceiling=2*alpha*alpha/(h*(alpha+h)))
out=dict(status='PASS',cases=len(rows),source_sha256=hashlib.sha256(raw).hexdigest(),
    strict_improvements=sum(x['centered_bound']<x['raw_bound'] for x in rows),
    calibration=calibration,rows=rows)
(root/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status='PASS',cases=len(rows),strict_improvements=out['strict_improvements'],
    examples=[{k:v for k,v in x.items() if k!='terms'} for x in rows if x['r']==10 and x['A']==15],
    calibration=calibration),indent=2))
