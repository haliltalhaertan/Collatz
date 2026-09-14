"""Regenerate the CP21 extension from trajectories; never edit the originals."""
from pathlib import Path
import json, time
from fractions import Fraction as F
from math import comb
import numpy as np
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent

def J(p):
 q=len(p)//2
 return q*sum((p[z]-p[z+q])**2 for z in range(q))

def histogram(m,r,chunk=1<<19):
 R=1<<r
 # Bound every int64 trajectory intermediate including unselected odd branch.
 bound=(1<<m)-1
 for _ in range(m):
  assert 3*bound+1<2**63
  bound=(3*bound+1)//2
 hist=np.zeros((m+1,R),dtype=np.int64)
 for first in range(0,1<<(m-1),chunk):
  end=min(first+chunk,1<<(m-1));x=2*np.arange(first,end,dtype=np.int64)+1;k=np.zeros(len(x),dtype=np.int64)
  for _ in range(m):
   odd=x&1;k+=odd;x=np.where(odd!=0,(3*x+1)//2,x//2)
  hist+=np.bincount(k*R+x%R,minlength=(m+1)*R).reshape(m+1,R)
 out={k:[int(v) for v in hist[k]] for k in range(1,m+1)}
 assert all(sum(v)==comb(m-1,k-1) for k,v in out.items())
 return out

def fold(hist,r):
 R=1<<r
 return {k:[sum(p[z::R]) for z in range(R)] for k,p in hist.items()}

def calc(hist,m,s):
 q=1<<s;N=q*2;inv=pow(3,-1,N);EO={};lt={};mt={};broken={}
 I=sum((F(J(p),comb(m-1,k-1)) for k,p in hist.items()),F(0));fine=F(0)
 for k,p in hist.items():
  c=pow(3,k,N)
  e=[p[2*z]+p[(2*z-c)%N] for z in range(q)]
  o=[p[(inv*(2*z-1))%N]+p[(inv*(2*z-1)-c)%N] for z in range(q)]
  EO[k]=(e,o);n=comb(m-1,k-1)
  fine+=F(J(e)+J(o),n)
  lt[k]=F(J(e)+J(o)-J(p),n)
 for k in range(2,m+1):
  a=comb(m-1,k-2);b=comb(m-1,k-1)
  y=[a*e-b*o for e,o in zip(EO[k][0],EO[k-1][1])]
  mt[k]=F(J(y),a*b*(a+b))
  # Negative control: emulate signed int64 arithmetic at squaring and reduction.
  def wrap(v):return (v+(1<<63))%(1<<64)-(1<<63)
  half=q//2
  broken[k]=F(wrap(half*sum(wrap((y[z]-y[z+half])**2) for z in range(half))),a*b*(a+b))
 out_hist={}
 for k in range(1,m+2):
  e=EO[k][0] if k in EO else [0]*q
  o=EO[k-1][1] if k-1 in EO else [0]*q
  out_hist[k]=[x+y for x,y in zip(e,o)]
 Out=sum((F(J(p),comb(m,k-1)) for k,p in out_hist.items()),F(0))
 assert sum(mt.values())==fine-Out and sum(lt.values())==fine-I
 return {'m':m,'s':s,'input':str(I),'fine':str(fine),'output':str(Out),'lift':str(fine-I),'merge':str(fine-Out),'defect':str(I-Out),'lift_terms':{str(k):str(v) for k,v in lt.items()},'merge_terms':{str(k):str(v) for k,v in mt.items()}},out_hist,broken

if __name__=='__main__':
 start=time.time(); gate,_,_=calc(histogram(4,3),4,2)
 assert [gate[k] for k in ('input','fine','output','lift','merge','defect')]==['40/3','16','31/3','8/3','17/3','3']
 old=json.loads((BASE/'cp21_lead_extension_m25_m26.json').read_text())['rows']
 results=[];comparison=[];hh={}
 for m in (25,26,27):
  hh[m]=histogram(m,7 if m<27 else 6)
  (ROOT/f'hist_m{m}.json').write_text(json.dumps(hh[m]))
  print('histogram',m,'complete',round(time.time()-start,2),flush=True)
 for r in old:
  m,s=r['m'],r['s'];new,predicted,broken=calc(fold(hh[m],s+1),m,s)
  assert predicted==fold(hh[m+1],s),('transfer vs independent next-level trajectories',m,s)
  diffs={k:{'old':r[k],'new':new[k]} for k in ('input','fine','output','lift','merge','defect') if F(r[k])!=F(new[k])}
  changed=[k for k in new['merge_terms'] if F(r['merge_terms'][k])!=F(new['merge_terms'][k])]
  overflow_matches=all(F(r['merge_terms'][k])==broken[int(k)] for k in new['merge_terms'])
  comparison.append({'m':m,'s':s,'scalar_differences':diffs,'changed_merge_terms':changed,'signed_int64_negative_control_reproduces_old':overflow_matches,'lift_terms_match':r['lift_terms']==new['lift_terms']})
  results.append(new)
 (ROOT/'corrected_extension.json').write_text(json.dumps({'source':'Fresh bounded int64 trajectories; Python arbitrary-precision energy; direct next-level crosscheck','rows':results},indent=2))
 (ROOT/'extension_comparison.json').write_text(json.dumps(comparison,indent=2))
 print(json.dumps(comparison,indent=2));print('elapsed',round(time.time()-start,2))
