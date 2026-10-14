#!/usr/bin/env python3
"""Independent finite-level Syracuse law and chi; cutoff error on TV <= 2**(-cutoff)."""
import argparse,json
p=argparse.ArgumentParser();p.add_argument('--s',type=int,default=10);p.add_argument('--cutoff',type=int,default=53);args=p.parse_args()
v=[1.0];chi0=1.;out=[]
for s in range(1,args.s+1):
 m=3**s;w=[2.0**-a for a in range(1,args.cutoff+1)]; powers=[pow(2,-a,m) for a in range(1,args.cutoff+1)]
 z=[0.] * m
 for x,p in enumerate(v):
  if not p:continue
  t=3*x+1
  for a in range(args.cutoff): z[(t*powers[a])%m]+=p*w[a]
 c=m*sum(t*t for t in z)
 out.append({'s':s,'chi':c,'E':c-chi0});print(s,round(c,9),round(c-chi0,9),flush=True)
 chi0=c;v=z
with open('chi_small_check.json','w') as f:json.dump({'method':'finite geometric cutoff, unrenormalized, discarded probability at level s <= s*2^-cutoff','cutoff':args.cutoff,'rows':out},f,indent=2)
