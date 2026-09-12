from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 70
HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'RESULTS.json').read_text(encoding='utf-8'))

def qf(x): return F(x)
def dec(q:F): return Decimal(q.numerator)/Decimal(q.denominator)
def sqrtq(q:F): return dec(q).sqrt()
rows=[]
for P in src['exact_source_panels']:
    q=1<<P['t']; q2=q*q
    W=qf(P['W']); Wf=qf(P['Wflat'])
    maxell=max((lv['ell'] for r in P['rows'] for lv in r['levels']), default=0)
    deltas=[]
    for ell in range(1,maxell+1):
        z=F(0)
        for r in P['rows']:
            H=1<<(r['s']-1)
            for lv in r['levels']:
                if lv['ell']==ell:
                    z += F(H*lv['cross'], q2)
        deltas.append(z)
    assert Wf + sum(deltas,F(0)) == W
    bounds=[]
    for L in range(0,maxell+1):
        signed=sum(deltas[:L],F(0))
        S=T=F(0)
        for r in P['rows']:
            H=1<<(r['s']-1)
            for lv in r['levels']:
                if lv['ell']>L:
                    S += H*lv['source_energy']
                    T += H*lv['tail_energy']
        ub=dec(Wf)+dec(signed)
        if S and T:
            ub += sqrtq(S*T)/Decimal(q2)
        ratio=ub/dec(W) if W else Decimal(1)
        assert ratio >= Decimal(1) - Decimal('1e-60')
        bounds.append({'L':L,'Sagg':str(S),'Tagg':str(T),'upper_over_W':str(ratio)})
    rows.append({'r':P['r'],'q':q,'W':str(W),'Wflat':str(Wf),
                 'signed_deltas':[str(x) for x in deltas], 'bounds':bounds})
out={'status':'PASS','statement':'Exact aggregate identity and global residual Cauchy checks on existing exact source panels.', 'panels':rows}
(HERE/'AGGREGATE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('AGGREGATE WEIGHTED CHECK: PASS')
for row in rows:
    print('r=',row['r'],'deltas=',row['signed_deltas'])
    for b in row['bounds'][:4]: print('  L',b['L'],'upper/W',b['upper_over_W'])
