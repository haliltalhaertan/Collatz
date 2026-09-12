"""Audit the submitted concentration proposal against stored actual panels.

Panel diagnostics reuse FFT pairs and are not interval certificates.
The r12 source/tail fourth moments below use exact integer autocorrelations.
"""
from pathlib import Path
from fractions import Fraction as F
import json, math
R=Path(__file__).resolve().parent
panels=json.loads((R.parent/'research_peak_peeling_20260912/RESULTS.json').read_text())['panels']
out=[];target=None
for panel in panels:
 rows=[];U=0
 for row in panel['rows']:
  pairs=row['pairs_by_tail'];mult=1 if row['s']==1 else 2;h=len(pairs)*mult
  sx=sum(mult*p['source'] for p in pairs);sy=sum(mult*p['tail'] for p in pairs)
  if sx==0 or sy==0:continue
  cx=h*sum(mult*p['source']**2 for p in pairs)/sx**2
  cy=h*sum(mult*p['tail']**2 for p in pairs)/sy**2
  A=float(F(row['alignment']));bound=math.sqrt(max(0,cx-1)*max(0,cy-1))
  assert abs(A-1)<=bound+1e-10
  U+=float(F(row['flat']))*(1+bound)
  rec={'k':row['k'],'j':row['j'],'s':row['s'],'C_X':cx,'C_Y':cy,'A':A,'centered_CS':bound}
  rows.append(rec)
  if (panel['r'],row['k'],row['s'])==(12,10,4):
   target={**rec,'source_pair_3_13_fraction':sum(mult*p['source'] for p in pairs if p['a']==3)/sx,'tail_pair_3_13_fraction':sum(mult*p['tail'] for p in pairs if p['a']==3)/sy,'centered_correlation':(A-1)/bound}
 out.append({'r':panel['r'],'max_C_X':max(rows,key=lambda row:row['C_X']),'centered_upper_over_W':U/float(F(panel['W'])),'centered_upper_over_flat':U/float(F(panel['W_flat'])),'rows':rows})
P=[124,115,123,123,138,140,124,118,121,125,132,126,111,126,125,131]
T=[0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0]
def moments(v):
 n=len(v);H=n//2
 cp=[sum(v[u]*v[(u+d)%n] for u in range(n)) for d in range(n)]
 M2=H*(cp[0]-cp[H])
 M4=H*sum(cp[d]**2-cp[d]*cp[(d+H)%n] for d in range(n))
 return {'primitive_second_moment':M2,'primitive_fourth_moment':M4,'concentration':str(F(H*M4,M2*M2))}
exact={'source_histogram':P,'tail_indicator':T,'source':moments(P),'tail':moments(T),'A':'14768/7764'}
# A=461.5/(10352*6/256), reduced exactly.
exact['A']=str(F(923,2)/F(10352*6,256))
record={'scope':'Claim audit: exact target moments, FFT panel diagnostics, no new asymptotic theorem','target':target,'exact_target':exact,'panels':out}
(R/'RESULTS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'target':target,'exact':exact,'selected_panels':[{k:p[k] for k in ['r','max_C_X','centered_upper_over_W']} for p in out if p['r'] in [12,18,19,20]]},indent=2))
