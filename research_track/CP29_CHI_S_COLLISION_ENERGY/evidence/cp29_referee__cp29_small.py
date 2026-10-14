#!/usr/bin/env python3
"""Independent exact / high-precision modular checks for CP29."""
import json
from fractions import Fraction
from decimal import Decimal, localcontext

CLAIM_E = [None, '0.666666667', '0.476190476', '0.461574680', '0.464214408', '0.465514920', '0.466168761', '0.465491430', '0.465921120']

def pair_collision(x,y,m=27):
    order = 1
    while pow(2,order,m) != 1: order += 1
    den = 2**order-1
    counts = [0]*m
    for a in range(1,order+1):
        counts[(pow(2,-a,m)*(1+3*x))%m] += 2**(order-a)
    counts2 = [0]*m
    for a in range(1,order+1):
        counts2[(pow(2,-a,m)*(1+3*y))%m] += 2**(order-a)
    return Fraction(sum(t*u for t,u in zip(counts,counts2)),den**2)

def high_precision(stop=10,digits=75,cut=285):
    # Total omitted geometric tail is < 2^-cut at each step. Multiplication
    # by 3^stop bounds the chi error by 2*3^stop*stop*2^-cut.
    with localcontext() as ctx:
        ctx.prec = digits
        prev=[Decimal(1)]
        chi0=Decimal(1)
        data=[]
        for s in range(1,stop+1):
            mod=3**s
            den=3**(s-1)
            curr=[Decimal(0)]*mod
            inv2=pow(2,-1,mod)
            unit=inv2
            weight=Decimal(1)/2
            for a in range(1,cut+1):
                for x,v in enumerate(prev):
                    if v:
                        idx=(unit*(1+3*x))%mod
                        curr[idx] += v*weight
                unit=unit*inv2%mod
                weight/=2
            # Omitted tail is put into its exact distribution of residues via
            # the full periodicity of powers of 2 modulo 3^s.
            # Distribution of residue A mod period has weight 2^-a/(1-2^-period).
            # For s<=5, period is short enough to do this directly; for all
            # larger s period exceeds cut by orders and correction < 2^-cut.
            if s<=5:
                order=2*3**(s-1)
                if order <= cut:
                    # subtract the already-counted repeated terms, then use
                    # exact geometric mass for each distinct exponent.
                    curr=[Decimal(0)]*mod
                    for a in range(1,order+1):
                        w=Decimal(2)**(-a)/(1-Decimal(2)**(-order))
                        mult=pow(2,-a,mod)
                        for x,v in enumerate(prev):
                            if v: curr[(mult*(1+3*x))%mod]+=w*v
            norm=sum(curr)
            chi=Decimal(mod)*sum(v*v for v in curr)
            e=chi-chi0
            peak=Decimal(mod)*max(curr)
            data.append({'s':s,'chi':str(chi),'E':str(e),'max_scaled':str(peak), 'mass':str(norm),
                         'claimed_E': CLAIM_E[s] if s<len(CLAIM_E) else None})
            print(s,'chi',chi,'E',e,'max_scaled',peak,'mass',norm,flush=True)
            prev=curr
            chi0=chi
        return data

if __name__=='__main__':
    p1=pair_collision(1,2)
    p2=pair_collision(2,4)
    print('I4',str(p1),str(p2),flush=True)
    d=high_precision()
    with open('cp29_small.json','w') as f:json.dump({'I4':[str(p1),str(p2)],'precision':d},f,indent=2)
