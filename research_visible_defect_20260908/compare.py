from pathlib import Path
from fractions import Fraction as F
import json
p=Path(__file__).resolve().parent
root=json.loads((p/'DIAGNOSTIC.json').read_text())
ind=json.loads((p/'INDEPENDENT_CHECK.json').read_text())['panels']
summary=[]
for a,b in zip(root,ind):
    assert (a['r'],a['A'],a['m'],a['t'],a['G'])==(b['r'],b['A'],b['m'],b['t'],b['G'])
    W=sum(map(F,a['sum_layer_variances_by_conductor']))
    cap=sum(map(F,a['source_caps_by_conductor']))
    V=sum(map(F,a['total_variances_by_conductor']))
    assert (W,cap,V)==(F(b['sumVk']),F(b['qD2']),F(b['V']))
    summary.append(dict(r=a['r'],W=str(W),qD2=str(cap),V=str(V),
        visible_fraction=float(W/cap),
        finest_total_fraction=float(F(a['total_variances_by_conductor'][-1])/V)))
out=dict(status='PASS',panels=summary)
(p/'COMPARISON.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
