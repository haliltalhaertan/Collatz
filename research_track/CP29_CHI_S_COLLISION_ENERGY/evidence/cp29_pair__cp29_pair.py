"""CP29_PAIR: first-divergence renewal and independently checked finite-level transfer.
Usage: python3 cp29_pair.py [max_s=8].  NumPy float64 for s>2; no probability-tail truncation.
"""
import json, math, sys
import numpy as np
from fractions import Fraction

REF='/mnt/c/Users/MDP/collatz-analysis/cp29_chi/chi_s_exact.json'

def weights(phi):
    # W(a mod phi), a=1,...,phi, geometric series, exact support.
    if phi < 1024:
        return np.array([math.ldexp(1.,-a)/(1.-math.ldexp(1.,-phi)) for a in range(1,phi+1)])
    a=np.arange(1,phi+1)
    return np.exp2(-a.astype(float))/(1.-2.**(-phi))

def distribution(prev,s):
    m=3**s; phi=2*3**(s-1); x=np.arange(len(prev)); z=1+3*x
    ans=np.zeros(m); w=weights(phi); inv=1
    for a in range(1,phi+1):
        inv=inv*pow(2,-1,m)%m
        # for large a underflows, no loss of significant precision
        if w[a-1]:np.add.at(ans,(inv*z)%m,w[a-1]*prev)
    return ans

def correlations(prev,s):
    n=3**(s-1); m=3*n
    log4=np.full(m,-1,np.int32); v=1
    for j in range(n):
        log4[v]=j;v=v*4%m
    assert v==1 and (log4[1+3*np.arange(n)]>=0).all()
    h=np.zeros(n)
    np.add.at(h,log4[1+3*np.arange(n)],prev)
    # truly direct autocorrelation; no Fourier FFT, no pair-word truncation
    return np.array([np.dot(h,np.roll(h,-j)) for j in range(n)])

def off_from_corr(c,s):
    n=len(c); j=np.arange(n,dtype=float)
    den=-np.expm1(-n*math.log(4))
    # sum over ALL integer l congruent to j mod n, excluding literal l=0
    k=(np.exp2(-2*j)+np.exp2(-2*(n-j)))/den
    k[0]-=1.
    return float(np.dot(k,c)/3), k

def exact_small():
    out=[]; prev=[Fraction(1)]
    for s in (1,2):
        m=3**s;phi=2*3**(s-1);den=2**phi-1
        q=[Fraction(0) for _ in range(m)]
        for a in range(1,phi+1):
            w=Fraction(2**(phi-a),den);inv=pow(2,-a,m)
            for x,px in enumerate(prev):q[(inv*(1+3*x))%m]+=w*px
        col=sum(v*v for v in q);prevcol=sum(v*v for v in prev)
        off=col-prevcol/3
        # Enumerate every first-letter pair and suffix pair, not FFT/log kernel.
        brute=Fraction(0)
        for a in range(1,phi+1):
            for b in range(1,phi+1):
                wa=Fraction(2**(phi-a),den);wb=Fraction(2**(phi-b),den)
                pair_mass=wa*wb if a!=b else wa*wb-Fraction(4**(phi-a),4**phi-1)
                ia=pow(2,-a,m);ib=pow(2,-b,m)
                for x,px in enumerate(prev):
                    for y,py in enumerate(prev):
                        if (ia*(1+3*x)-ib*(1+3*y))%m==0:
                            brute+=pair_mass*px*py
        assert brute==off
        out.append({'s':s,'chi_exact':str(m*col),'E_exact':str(m*off),
                    'first_mismatch_exact':str(brute),'q_exact':str(col)})
        prev=q
    return out

def main(smax):
    assert 1<=smax<=9, 's<=9 direct O(3^(2s)) autocorrelations are intended'
    reference=json.load(open(REF)); prev=np.array([1.]); chi_prev=1.; results=[]
    for s in range(1,smax+1):
        p=distribution(prev,s);m=3**s;n=m//3
        q=float(np.dot(p,p));direct=m*q
        corr=correlations(prev,s)
        r,k=off_from_corr(corr,s)
        e=m*r
        contributions={str(l): float(n*4.**(-l)*(corr[l%n]+corr[-l%n])) for l in range(1, min(7,3*n)+1)}
        qprev=float(np.dot(prev,prev));renewal=(qprev/3+r)*m
        # telescoping by FIRST different A position; same-prefix probability 3^-k
        prefix=1.+sum(v['E_pair'] for v in results)+e
        entry={'s':s,'chi_direct':direct,'E_pair':e,'E_difference':direct-chi_prev,
               'first_mismatch_probability':r,'q':q,'gap_contributions':contributions,'renewal_chi':renewal,
               'first_divergence_chi':prefix,'mass':float(p.sum()),
               'ref_chi':reference[s-1]['chi'],'ref_E':reference[s-1]['E'],
               'max_error':max(abs(direct-chi_prev-e),abs(renewal-direct),
                               abs(prefix-direct),abs(direct-reference[s-1]['chi']))}
        print(s,direct,e,'max_err',entry['max_error'],flush=True)
        assert entry['max_error']<3.e-8
        results.append(entry);prev=p;chi_prev=direct
    exact=exact_small()
    out={'method':'exact-period A finite transfer; independent brute correlations of log_4(1+3X); two exact enumerations',
         'exact_s1_s2':exact,'results':results,'G1':False,'G2':False,'G3':False,
         'source':'Tao arXiv:1909.03562 Remark 1.13, Proposition 1.17, Lemma 6.2 (primary PDF and HTML checked)',
         'note':'float64, not proof of growth; no finite uniform-state reduction claimed'}
    with open('cp29_pair.json','w') as f:json.dump(out,f,indent=2,ensure_ascii=False)

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 8)
