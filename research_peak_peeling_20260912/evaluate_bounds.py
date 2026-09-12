"""Post-hoc evaluation of the proved enclosure; FFT values are diagnostic."""
from pathlib import Path
from fractions import Fraction
import json
R=Path(__file__).parent
d=json.loads((R/'RESULTS.json').read_text())
out=[]
for panel in d['panels']:
 q=2**panel['t']; w=float(Fraction(panel['W'])); flat=float(Fraction(panel['W_flat']))
 bounds={}
 for L in [0,1,2,4]:
  total=0.; max_bulk=0.
  for row in panel['rows']:
   pairs=row['pairs_by_tail']; chosen=pairs[:L]; rest=pairs[L:]
   factor=1 if row['s']==1 else 2
   bulk=rest[0]['tail'] if rest else 0.
   energy=factor*sum(p['source'] for p in rest)
   total+=sum(p['contribution'] for p in chosen)+bulk*energy/q**2
   if row['D']: max_bulk=max(max_bulk,bulk/row['D'])
  assert total>=w-1e-7*max(1,w)
  bounds[str(L)]={'upper_over_W':total/w,'upper_over_flat':total/flat,'max_remaining_tail_over_D':max_bulk}
 assert all(bounds[str(a)]['upper_over_W']>=bounds[str(b)]['upper_over_W']-1e-10 for a,b in [(0,1),(1,2),(2,4)])
 # Post-hoc candidate: energy-weighted tail profile, exponent 2.
 # At a multiplier threshold use >= (the left limit of the layer-cake tail).
 weak_C=0.; worst=None
 for row in panel['rows']:
  pairs=row['pairs_by_tail']; S=sum(p['source'] for p in pairs)
  if not S or not row['D']:continue
  for p in pairs:
   u=p['tail']/row['D']
   if u<1:continue
   mass=sum(v['source'] for v in pairs if v['tail']>=p['tail']-1e-9*max(1,p['tail']))/S
   val=u*u*mass
   if val>weak_C:weak_C=val;worst={'k':row['k'],'j':row['j'],'s':row['s'],'u':u,'source_energy_fraction':mass}
 out.append({'r':panel['r'],'bounds':bounds,'diagnostic_weak_tail_exponent_2_C':weak_C,'weak_tail_worst':worst})
record={'scope':'Post-hoc floating evaluation of exact analytic enclosure. Not interval-certified numbers or uniform bound. L chosen per (k,s).','panels':out}
(R/'BOUND_RESULTS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
for row in out:
 if row['r'] in [12,14,18,19,20]:print(json.dumps(row))
