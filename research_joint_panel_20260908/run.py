from pathlib import Path
from fractions import Fraction as F
from math import comb,log2
from collections import Counter
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research_intersection_debate_20260908'))
from audit_dp import joint_dp

rows=[]
for r in range(10,23,2):
 A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m
 start=time.perf_counter();counts,trace=joint_dp(m,t)
 elapsed=time.perf_counter()-start
 cells=[];total=sum(v for (k,j),v in counts.items() if k+j==r)
 base=F(comb(A-1,r-1),2**t)
 mean=F(1)+F((m-1)*(r-1),A-1)
 for k in range(max(1,r-t),min(m,r)+1):
  actual=counts.get((k,r-k),0)
  null=F(comb(m-1,k-1)*comb(t,r-k),2**t)
  cells.append(dict(k=k,actual=actual,baseline=str(null),ratio=str(F(actual)/null)))
 tv=sum((abs(F(c['actual'],total)-F(c['baseline'])/base) for c in cells),F(0))/2
 rows.append(dict(r=r,A=A,m=m,t=t,total=total,baseline=str(base),ratio=str(F(total)/base),
  finite_log_ratio_over_r=log2(float(F(total)/base))/r,
  hypergeometric_mean=str(mean),actual_mode=[c['k'] for c in cells if c['actual']==max(z['actual'] for z in cells)],
  total_variation=str(tv),seconds=elapsed,peak_states=max(z['states'] for z in trace),cells=cells))
 print(json.dumps({k:rows[-1][k] for k in ('r','total','baseline','ratio','finite_log_ratio_over_r','actual_mode','seconds','peak_states')}),flush=True)
out=dict(status='PASS',design='fixed r=10,12,...,22; A=floor(alpha*r); m=ceil(1.2*r); full initial dyadic block; descriptive exact counts, not inferential p-values',rows=rows)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
