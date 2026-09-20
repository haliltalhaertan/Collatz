from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from math import comb
from decimal import Decimal, getcontext
from pathlib import Path
import json, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'research_w_continuation_20260912'))
import check_shell_alignment as wcheck
getcontext().prec=60

def choose(n,k): return comb(n,k) if 0<=k<=n else 0

def walk(x,n):
    wt=0
    for _ in range(n):
        e=x&1; wt+=e; x=(3*x+1)//2 if e else x//2
    return x,wt

def corr(v,w=None):
    if w is None:w=v
    n=len(v); assert len(w)==n
    return [sum(v[u]*w[(u+d)%n] for u in range(n)) for d in range(n)]

def v2pos(d):
    assert d>0
    return (d&-d).bit_length()-1

def tail_filter(t,j,s):
    return [choose(t-s,j-walk(u,s)[1]) for u in range(1<<s)]

def cross_channels(t,j,s):
    q=1<<(s-1); H=q//2
    g=[choose(t-s,j-k) for k in range(s+1)]
    weights=[walk(u,s-1)[1] for u in range(q)]
    f0=[g[k] for k in weights]; f1=[g[k+1] for k in weights]
    A0=corr(f0); A1=corr(f1)
    inv3=pow(3,-1,q) if q>1 else 0
    U=[f0[(inv3*z)%q] for z in range(q)] if q>1 else f0[:]
    B=corr(U,f1)
    d0=[A0[b]-A0[(b+H)%q] for b in range(q)]
    d1=[A1[b]-A1[(b+H)%q] for b in range(q)]
    db=[B[b]-B[(b+H)%q] for b in range(q)]
    NB=sum(db[h]*db[h] for h in range(H))
    O=sum(db[(3*h+2)%q]*db[(-3*h-1)%q] for h in range(H))
    Nplus=F(NB+O,2); Nminus=F(NB-O,2)
    return dict(q=q,H=H,d0=d0,d1=d1,db=db,NB=NB,O=O,Nplus=Nplus,Nminus=Nminus)

def shift_valuation_stats(x,y):
    assert len(x)==len(y) and len(x)>=2 and len(x)&(len(x)-1)==0
    n=len(x); H=n//2
    cx=corr(x); cy=corr(y)
    DX=[cx[d]-cx[d+H] for d in range(H)]
    DY=[cy[d]-cy[d+H] for d in range(H)]
    RX=DX[0]; RY=DY[0]
    if RX==0 or RY==0:
        return dict(RX=RX,RY=RY,alignment=None,levels=[],DX=DX,DY=DY)
    levels=[]
    for ell in range(1,n.bit_length()-1):
        inds=[d for d in range(1,H) if v2pos(d)==ell-1]
        if not inds: break
        cross=sum(DX[d]*DY[d] for d in inds)
        sx=sum(DX[d]**2 for d in inds)
        sy=sum(DY[d]**2 for d in inds)
        levels.append(dict(ell=ell,cross=cross,source_energy=sx,tail_energy=sy,count=len(inds)))
    num=RX*RY+sum(z['cross'] for z in levels)
    return dict(RX=RX,RY=RY,alignment=F(num,RX*RY),levels=levels,DX=DX,DY=DY)

def retained_upper(stats,L):
    if stats['alignment'] is None:return None
    levels=stats['levels']; L=min(L,len(levels)); RX=stats['RX'];RY=stats['RY']
    signed=sum(z['cross'] for z in levels[:L])
    sx=sum(z['source_energy'] for z in levels[L:])
    sy=sum(z['tail_energy'] for z in levels[L:])
    base=Decimal(RX*RY+signed)
    rad=(Decimal(sx)*Decimal(sy)).sqrt()
    return (base+rad)/Decimal(RX*RY)

def cumulative_bridge(t,j,s):
    ch=cross_channels(t,j,s); q=ch['q'];H=ch['H'];d0=ch['d0'];d1=ch['d1']
    B=[]
    for r in range(max(1,s-1)):
        step=1<<r
        B.append(sum(d0[h]*d1[(3*h)%q] for h in range(0,H,step)))
    return ch,B

def tail_valuation_energy(t,j,s):
    v=tail_filter(t,j,s); n=len(v);H=n//2;c=corr(v)
    D=[c[d]-c[d+H] for d in range(H)]
    levels=[]
    for ell in range(1,s):
        inds=[d for d in range(1,H) if v2pos(d)==ell-1]
        if not inds: break
        levels.append(sum(D[d]**2 for d in inds))
    return D[0],levels,D

def theorem_checks():
    checked=0; bridge_pos=0; nonmono=[]; rec_checks=0; first_level_checks=0
    for t in range(4,13):
      for s in range(3,min(t,8)+1):
       for j in range(t+1):
        ch,B=cumulative_bridge(t,j,s)
        assert B[0]==ch['NB']
        assert all(z>=0 for z in B)
        bridge_pos += len(B)
        if any(B[r+1]>B[r] for r in range(len(B)-1)) and len(nonmono)<20:
            nonmono.append(dict(t=t,j=j,s=s,B=B))
        R0,TL,D=tail_valuation_energy(t,j,s)
        if TL:
            assert F(TL[0],1)==4*ch['Nplus']
            first_level_checks+=1
        child0=tail_valuation_energy(t-1,j,s-1)[1]
        child1=tail_valuation_energy(t-1,j-1,s-1)[1]
        d0=ch['d0'];d1=ch['d1'];q=ch['q'];H=ch['H']
        for ell in range(2,len(TL)+1):
            r=ell-2
            inds=[h for h in range(1,H) if v2pos(h)==r]
            mixed=sum(d0[h]*d1[(3*h)%q] for h in inds)
            lhs=TL[ell-1]
            rhs=child0[ell-2]+child1[ell-2]+2*mixed
            assert lhs==rhs
            if r+1 < len(B): assert mixed==B[r]-B[r+1]
            rec_checks+=1
        checked+=1
    return dict(cases=checked,bridge_nonnegative_checks=bridge_pos,
                first_level_Nplus_checks=first_level_checks,
                valuation_recurrence_checks=rec_checks,
                nonmonotone_bridge_examples=nonmono)

def exact_source_panels():
    panels=[]
    for r in (5,10,12,14):
        A=(3**r).bit_length()-1; m=(6*r+4)//5; t=A-m; Q=1<<t
        source=Counter()
        for h in range(1,1<<m,2):
            y,k=walk(h,m);source[k,y%Q]+=1
        tails=[walk(z,t)[1] for z in range(Q)]
        W=F(0); Wflat=F(0); bounds={L:Decimal(0) for L in range(4)}; rows=[]; signed_levels={}
        for k in range(max(1,r-t),min(m,r)+1):
            j=r-k; pfull=[source[k,z] for z in range(Q)]
            g=[sum(pfull[z] for z in range(Q) if tails[(z+pow(3,k,Q)*a)%Q]==j) for a in range(Q)]
            visible=wcheck.variances(g)
            for s in range(1,t+1):
                n=1<<s;H=n//2
                p=[sum(pfull[u::n]) for u in range(n)]
                f=[sum(tails[z]==j for z in range(u,Q,n)) for u in range(n)]
                st=shift_valuation_stats(p,f)
                RX=st['RX'];RY=st['RY']
                flat=F(H*RX*RY,Q*Q)
                V=visible[s-1]
                if flat:
                    assert st['alignment']==V/flat
                    for L in bounds:
                        ub=retained_upper(st,L)
                        bounds[L]+=Decimal(flat.numerator)/Decimal(flat.denominator)*ub
                else:
                    assert V==0
                W+=V;Wflat+=flat
                levout=[]
                for z in st['levels']:
                    zz={kk:(str(vv) if isinstance(vv,F) else vv) for kk,vv in z.items()}
                    if RX and RY:
                        gamma=F(z['cross'],RX*RY); zz['normalized_signed_contribution']=str(gamma)
                        signed_levels[z['ell']]=signed_levels.get(z['ell'],F(0))+flat*gamma
                    levout.append(zz)
                rows.append(dict(k=k,j=j,s=s,V=str(V),flat=str(flat),alignment=str(st['alignment']) if st['alignment'] is not None else None, levels=levout))
        Wd=Decimal(W.numerator)/Decimal(W.denominator)
        panels.append(dict(r=r,A=A,m=m,t=t,W=str(W),Wflat=str(Wflat),W_over_Wflat=str(W/Wflat),
                           retained_upper_over_W={str(L):str(bounds[L]/Wd) for L in bounds},
                           aggregate_signed_level_contribution_over_W={str(ell):str(val/W) for ell,val in sorted(signed_levels.items())}, rows=rows))
    return panels

def inherited_fft_diagnostics():
    path=ROOT/'research_peak_peeling_20260912'/'RESULTS.json'
    data=json.loads(path.read_text())['panels']; out=[]
    import math
    for pan in data:
        if pan['r'] not in (12,18,19,20): continue
        W=float(F(pan['W'])); sums={L:0.0 for L in (0,1,2,3)}
        for row in pan['rows']:
            flat=float(F(row['flat']))
            if flat==0: continue
            s=row['s']; H=1<<(s-1); n=1<<s; vals={}
            for p in row['pairs_by_tail']:
                vals[p['a']]=(p['source'],p['tail']); vals[p['conjugate']]=(p['source'],p['tail'])
            odds=list(range(1,n,2)); X=[vals[a][0] for a in odds];Y=[vals[a][1] for a in odds]
            sx=sum(X);sy=sum(Y)
            if not sx or not sy: continue
            x=[z/sx for z in X];y=[z/sy for z in Y]
            dx=[];dy=[]; cx=x[:];cy=y[:]
            while len(cx)>1:
                h=len(cx)//2
                dx.append([(cx[i]-cx[i+h])/(2**0.5) for i in range(h)])
                dy.append([(cy[i]-cy[i+h])/(2**0.5) for i in range(h)])
                cx=[(cx[i]+cx[i+h])/(2**0.5) for i in range(h)]
                cy=[(cy[i]+cy[i+h])/(2**0.5) for i in range(h)]
            cross=[H*sum(a*b for a,b in zip(aa,bb)) for aa,bb in zip(dx,dy)]
            ex=[sum(a*a for a in aa) for aa in dx];ey=[sum(b*b for b in bb) for bb in dy]
            for L in sums:
                L0=min(L,len(dx)); signed=sum(cross[:L0]); rx=sum(ex[L0:]);ry=sum(ey[L0:])
                ub=1+signed+H*math.sqrt(max(0,rx*ry)); sums[L]+=flat*ub
        signed_levels={}
        for row in pan['rows']:
            flat=float(F(row['flat']))
            if flat==0: continue
            s=row['s'];H=1<<(s-1);n=1<<s;vals={}
            for pp in row['pairs_by_tail']:
                vals[pp['a']]=(pp['source'],pp['tail']); vals[pp['conjugate']]=(pp['source'],pp['tail'])
            odds=list(range(1,n,2));X=[vals[a][0] for a in odds];Y=[vals[a][1] for a in odds];sx=sum(X);sy=sum(Y)
            if not sx or not sy: continue
            cx=[z/sx for z in X];cy=[z/sy for z in Y]; ell=1
            while len(cx)>1:
                h=len(cx)//2; dx=[(cx[i]-cx[i+h])/(2**0.5) for i in range(h)];dy=[(cy[i]-cy[i+h])/(2**0.5) for i in range(h)]
                signed_levels[ell]=signed_levels.get(ell,0.0)+flat*H*sum(a*b for a,b in zip(dx,dy))/W
                cx=[(cx[i]+cx[i+h])/(2**0.5) for i in range(h)];cy=[(cy[i]+cy[i+h])/(2**0.5) for i in range(h)];ell+=1
        out.append(dict(r=pan['r'],source='inherited FFT pair diagnostics from research_peak_peeling_20260912/RESULTS.json',
                        retained_upper_over_W={str(L):sums[L]/W for L in sums},
                        aggregate_signed_level_contribution_over_W={str(k):v for k,v in sorted(signed_levels.items())},
                        W_over_Wflat=float(F(pan['W'])/F(pan['W_flat']))))
    return out

def main():
    checks=theorem_checks(); exact=exact_source_panels(); inherited=inherited_fft_diagnostics()
    out=dict(status='proved identities + exact finite checks + separately labelled inherited FFT diagnostics',
             theorem_checks=checks, exact_source_panels=exact, inherited_fft_diagnostics=inherited)
    (HERE/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    summary=dict(theorem_checks={k:v for k,v in checks.items() if k!='nonmonotone_bridge_examples'},
                 first_nonmonotone_bridge=checks['nonmonotone_bridge_examples'][0] if checks['nonmonotone_bridge_examples'] else None,
                 exact_panels=[{k:v for k,v in p.items() if k!='rows'} for p in exact], inherited_fft_diagnostics=inherited)
    print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
