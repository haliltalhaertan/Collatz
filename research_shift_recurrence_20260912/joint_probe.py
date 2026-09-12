"""Exact affine joint-weight recursion and separately bounded state-count probe."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json,time
R=Path(__file__).parent
def branches(n,a,b):
 q=1<<(n-1)
 for e in [0,1]:
  f=(a*e+b)&1
  aa=(a*(3 if f>e else pow(3,-1,q) if f<e else 1))%q
  bb=((3**f*(a*e+b)+f)//2-2*e*aa)%q
  yield e,f,aa,bb
def polynomial_recursion():
 @lru_cache(None)
 def joint(n,a,b):
  if n==0:return ((0,0,1),)
  out=Counter()
  for e,f,aa,bb in branches(n,a,b):
   for k,j,v in joint(n-1,aa,bb):out[k+e,j+f]+=v
  return tuple((k,j,v) for (k,j),v in sorted(out.items()))
 return joint
def weights(s):
 out=[]
 for v in range(1<<s):
  k=0;x=v
  for _ in range(s):
   e=x&1;k+=e;x=(3*x+1)//2 if e else x//2
  out.append(k)
 return out
def exhaustive(s):
 started=time.perf_counter();n=1<<s;w=weights(s);joint=polynomial_recursion()
 for d in range(n):
  expected=Counter((w[v],w[(v+d)%n]) for v in range(n))
  actual={(k,j):v for k,j,v in joint(s,1,d)}
  assert actual==expected,(s,d)
  if d%2==0:
   # Specialized even-shift identity J_s(2d)=J_(s-1)(d)+xy J_(s-1)(3d).
   v=Counter({(k,j):z for k,j,z in joint(s-1,1% (n//2),d//2)})
   for k,j,z in joint(s-1,1%(n//2),(3*d//2)%(n//2)):v[k+1,j+1]+=z
   assert dict(v)==actual
 return {'s':s,'shifts':n,'ordered_pairs':n*n,'passed':True,'cached_states_all_shifts':joint.cache_info().currsize,'seconds':time.perf_counter()-started}
def state_count(s):
 d=((1<<s)//3)|1;levels=Counter();started=time.perf_counter()
 @lru_cache(None)
 def visit(n,a,b):
  levels[s-n]+=1
  if n:
   for e,f,aa,bb in branches(n,a,b):visit(n-1,aa,bb)
 visit(s,1,d)
 for depth,count in levels.items():assert count<=min(2**depth,(2*depth+1)*2**(s-depth))
 return {'s':s,'shift':d,'states':visit.cache_info().currsize,'leaves_naive':1<<s,'levels':dict(sorted(levels.items())),'seconds':time.perf_counter()-started}
if __name__=='__main__':
 plan=json.loads((R/'PLAN.json').read_text());checks=[];counts=[]
 for s in plan['exhaustive_joint_checks_s']:
  row=exhaustive(s);checks.append(row);print(json.dumps(row),flush=True)
 for s in plan['state_count_s']:
  row=state_count(s);counts.append(row);print(json.dumps(row),flush=True)
 (R/'JOINT_RESULTS.json').write_text(json.dumps({'plan':plan,'exact_joint_checks':checks,'single_shift_state_counts':counts},indent=2)+'\n',encoding='utf-8',newline='\n')
