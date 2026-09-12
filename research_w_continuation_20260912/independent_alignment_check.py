"""Exact cyclic autocorrelation/Ramanujan verification, without DFT floats."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import json
P=Path(__file__).parent
data=json.loads((P/'RESULTS.json').read_text())
checks=0;violations=[];maxima=[]
for panel in data['panels']:
 m,t=panel['m'],panel['t'];q=2**t
 source={}
 for h in range(1,2**m,2):
  y=h;k=0
  for step in range(m):
   odd=y%2;k+=odd;y=(3*y+1)//2 if odd else y//2
  source.setdefault(k,Counter())[y%q]+=1
 weights=[]
 for z in range(q):
  y=z;j=0
  for step in range(t):
   odd=y%2;j+=odd;y=(3*y+1)//2 if odd else y//2
  weights.append(j)
 for row in panel['rows']:
  k,j,s=row['k'],row['j'],row['s'];n=2**s;H=n//2
  A=[sum(source[k].get(z,0) for z in range(u,q,n)) for u in range(n)]
  B=[sum(weights[z]==j for z in range(u,q,n)) for u in range(n)]
  C=[sum(A[u]*A[(u+d)%n] for u in range(n)) for d in range(n)]
  D=[sum(B[u]*B[(u+d)%n] for u in range(n)) for d in range(n)]
  numerator=H*sum(C[d]*(D[d]-D[(d+H)%n]) for d in range(n))
  exact=Fraction(numerator,q*q)
  assert exact==Fraction(row['V'])
  R=sum((A[u]-A[u+H])**2 for u in range(H))
  budget=sum((B[u]-B[u+H])**2 for u in range(H))
  assert R==row['R'] and budget==row['D']
  flat=Fraction(H*R*budget,q*q)
  assert flat==Fraction(row['flat'])
  cap=1 if s==1 else H//2
  assert exact<=cap*flat
  if s<=2:assert exact==flat
  if exact>flat:violations.append({'r':panel['r'],'k':k,'j':j,'s':s,'ratio':str(exact/flat)})
  checks+=1
assert violations,'The expected flat-alignment obstruction was not found'
out={'method':'Integer cyclic autocorrelation and primitive Ramanujan sum; independent of conditional variance projections','rows_verified':checks,'all_variances_and_R_D_match':True,'real_conjugate_pair_bound':'PASS','first_two_conductors_exact_flat':'PASS','flat_alignment_counterexamples':violations,'scope':'Exact finite identities and counterexamples only; no asymptotic claim'}
(P/'INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'rows':checks,'flat_violations':len(violations),'max_ratio':str(max(Fraction(v['ratio']) for v in violations))}))
