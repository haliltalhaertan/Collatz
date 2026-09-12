"""Exact trace-identity checks and signed-vs-angular slack audit."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
R=Path(__file__).resolve().parent
def cyc_product(a,b):
 H=len(a);out=[0]*H
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   e=i+j;out[e%H]+=(1 if e<H else -1)*x*y
 return out
tests=[]
for t,j in [(10,6),(12,8),(14,9)]:
 for s in range(2,8):
  n=2**s;H=n//2;v=[]
  for u in range(n):
   x=u;k=0
   for _ in range(s):
    b=x%2;k+=b;x=(3*x+1)//2 if b else x//2
   v.append(comb(t-s,j-k) if 0<=j-k<=t-s else 0)
  c=[sum(v[u]*v[(u+d)%n] for u in range(n)) for d in range(n)]
  beta=[c[u]-c[u+H] for u in range(H)]
  trace=H*beta[0];trace2=H*cyc_product(beta,beta)[0]
  correlation_value=H*sum((c[u]-c[u+H])**2 for u in range(H))
  assert trace2==correlation_value
  tests.append({'t':t,'j':j,'s':s,'trace':trace,'trace_square':trace2,'C_Y':str(F(H*trace2,trace**2))})
base=json.loads((R.parent/'research_peak_peeling_20260912/RESULTS.json').read_text())['panels']
cs={v['r']:v for v in json.loads((R.parent/'research_concentration_audit_20260912/RESULTS.json').read_text())['panels']}
slack=[]
for panel in base:
 W=F(panel['W']);negative=sum((F(row['flat'])-F(row['V']) for row in panel['rows'] if F(row['flat'])>F(row['V'])),F(0))
 U=cs[panel['r']]['centered_upper_over_W']*float(W)
 sign_loss=2*negative;angular=U-float(W+sign_loss)
 assert angular>=-1e-8*max(1,float(W))
 slack.append({'r':panel['r'],'W':str(W),'sign_loss_exact':str(sign_loss),'sign_preserving_magnitude_bound_over_W':(U-float(sign_loss))/float(W),'absolute_actual_correction_bound_over_W':float((W+sign_loss)/W),'sign_fraction_of_slack':float(sign_loss)/(U-float(W)) if U-float(W)>1e-10*max(1,float(W)) else None,'angular_loss_over_W':angular/float(W)})
counter=[]
for s in range(2,9):
 H=2**(s-1)
 trace=H*H;trace2=H*sum((H-2*u)**2 for u in range(H))
 C=F(H*trace2,trace*trace)
 assert C==F(H*H+2,3*H)
 counter.append({'s':s,'H':H,'C_Y':str(C),'scope':'Block indicator, not the Collatz parity-weight filter'})
record={'scope':'Exact algebraic identities and sign corrections; angular losses inherit FFT diagnostics. No uniform Collatz estimate.','trace_identity_checks':tests,'slack':slack,'algebraic_only_counterfamily':counter}
(R/'RESULTS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'exact_trace_checks':len(tests),'selected_slack':[p for p in slack if p['r'] in [12,18,19,20]],'counterfamily':counter},indent=2))
