"""Exact cross terms of the parity split; all convolution digits certified."""
from pathlib import Path
from math import comb,isqrt,sqrt
from fractions import Fraction as F
import sys,json,time
R=Path(__file__).parent
sys.path.insert(0,str(R.parent/'research_shift_recurrence_20260912'))
from exact_moment import actual_filter,cyclic_correlation_exact,moments_from_correlation,parity_weight
def cross(v,w):
 assert len(v)==len(w) and all(isinstance(x,int) and x>=0 for x in v+w)
 n=len(v);bound=isqrt(sum(x*x for x in v)*sum(x*x for x in w))
 if not bound:return [0]*n
 width=max(1,(bound.bit_length()+7)//8)
 x=int.from_bytes(b''.join(a.to_bytes(width,'little') for a in v),'little')
 y=int.from_bytes(b''.join(a.to_bytes(width,'little') for a in reversed(w)),'little')
 raw=(x*y).to_bytes((2*n-1)*width,'little')
 coeff=[int.from_bytes(raw[i:i+width],'little') for i in range(0,len(raw),width)]
 assert max(coeff)<=bound
 out=[coeff[n-1]]+[coeff[n-1-d]+coeff[2*n-1-d] for d in range(1,n)]
 assert sum(out)==sum(v)*sum(w)
 return out
def direct(v,w):
 return [sum(v[u]*w[(u+d)%len(v)] for u in range(len(v))) for d in range(len(v))]
def panel(t,j,s,check_direct=False):
 start=time.perf_counter();q=1<<(s-1);h0=q//2
 g=[comb(t-s,j-k) if 0<=j-k<=t-s else 0 for k in range(s+1)]
 weights=[parity_weight(u,s-1) for u in range(q)]
 v=[g[k] for k in weights];w=[g[k+1] for k in weights]
 A0=cross(v,v);A1=cross(w,w);U=[v[(pow(3,-1,q)*z)%q] for z in range(q)];B=cross(U,w)
 if check_direct:
  assert A0==direct(v,v) and A1==direct(w,w) and B==direct(U,w)
 parent,_=cyclic_correlation_exact(actual_filter(t,j,s))
 assert all(parent[2*h]==A0[h]+A1[(3*h)%q] and parent[2*h+1]==B[(3*h+2)%q]+B[(-3*h-1)%q] for h in range(q))
 d0=[A0[b]-A0[(b+h0)%q] for b in range(q)]
 d1=[A1[b]-A1[(b+h0)%q] for b in range(q)]
 db=[B[b]-B[(b+h0)%q] for b in range(q)]
 r0=sum(d0[h]**2 for h in range(h0));r1=sum(d1[h]**2 for h in range(h0));rb=sum(db[h]**2 for h in range(h0))
 E=sum(d0[h]*d1[(3*h)%q] for h in range(h0))
 O=sum(db[(3*h+2)%q]*db[(-3*h-1)%q] for h in range(h0))
 assert E==rb and E*E<=r0*r1 and abs(O)<=rb
 S=r0+r1+2*rb+2*(E+O)
 assert S==sum((parent[d]-parent[d+q])**2 for d in range(q))
 moments=moments_from_correlation(parent);assert q*S==int(moments['primitive_fourth_moment'])
 baseline=r0+r1+2*rb
 plus=F(rb+O,2);minus=F(rb-O,2)
 assert S==r0+r1+6*plus+2*minus and baseline<=S<=2*baseline
 return {'t':t,'j':j,'s':s,'R0':str(r0),'R1':str(r1),'RB':str(rb),'even_cross':str(E),'odd_cross':str(O),'even_rho_display':E/sqrt(r0*r1) if r0*r1 else None,'odd_rho_exact':str(F(O,rb)) if rb else None,'odd_rho_display':float(F(O,rb)) if rb else None,'reflection_plus_norm':str(plus),'reflection_minus_norm':str(minus),'even_energy':str(r0+r1+2*E),'odd_energy':str(2*(rb+O)),'uncoupled_energy':str(baseline),'total_energy':str(S),'coupling_ratio':str(F(S,baseline)) if baseline else None,'identity_upper_over_actual_exact':str(F(r0+r1+6*rb,S)) if S else None,'naive_Cauchy_over_actual_display':(r0+r1+2*sqrt(r0*r1)+4*rb)/S if S else None,'seconds':time.perf_counter()-start,**moments}
if __name__=='__main__':
 assert cross([1,2,3,4],[0,1,0,3])==direct([1,2,3,4],[0,1,0,3])
 plan=json.loads((R/'PLAN.json').read_text());checks=[]
 for t in range(2,plan['direct_filter_checks']['t_max']+1):
  for j in range(t+1):
   for s in range(2,min(t,plan['direct_filter_checks']['s_max'])+1):checks.append(panel(t,j,s,True))
 print(json.dumps({'direct_cases':len(checks),'negative_odd':sum(int(p['odd_cross'])<0 for p in checks),'positive_odd':sum(int(p['odd_cross'])>0 for p in checks)}),flush=True)
 family=[]
 for s in plan['large_family']['s']:
  row=panel(plan['large_family']['t'],plan['large_family']['j'],s);family.append(row);print(json.dumps(row),flush=True)
 (R/'RESULTS.json').write_text(json.dumps({'plan':plan,'direct_checks':checks,'family':family},indent=2)+'\n',encoding='utf-8',newline='\n')
