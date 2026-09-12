"""Post-hoc complete coefficient evaluations after the state-count probe."""
from pathlib import Path
from math import comb
import time,json
from joint_probe import polynomial_recursion
R=Path(__file__).parent;out=[]
for s in [20,24]:
 d=((1<<s)//3)|1;calc=polynomial_recursion();start=time.perf_counter()
 coeff=calc(s,1,d);seconds=time.perf_counter()-start
 assert sum(v for k,j,v in coeff)==1<<s
 assert all(sum(v for k,j,v in coeff if k==i)==comb(s,i) for i in range(s+1))
 assert all(sum(v for k,j,v in coeff if j==i)==comb(s,i) for i in range(s+1))
 row={'s':s,'shift':d,'cached_states':calc.cache_info().currsize,'seconds':seconds,'nonzero_coefficients':len(coeff),'coefficients':coeff,'total_and_binomial_marginals':'PASS','scope':'Actual full coefficient evaluation; independent exhaustive comparison was limited to small s, not these large cases.'}
 out.append(row);print(json.dumps({k:v for k,v in row.items() if k!='coefficients'}),flush=True);calc.cache_clear()
(R/'FULL_JOINT_RESULTS.json').write_text(json.dumps({'status':'POST_HOC_FOLLOWUP','cases':out},indent=2)+'\n',encoding='utf-8',newline='\n')
