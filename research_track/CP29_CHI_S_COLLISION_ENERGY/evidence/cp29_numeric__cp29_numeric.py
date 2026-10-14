#!/usr/bin/env python3
"""CP29: float64 FFT-free full-support transfer, high-precision checks and diagnostics.
Requires numpy, scipy, mpmath. Writes cp29_numeric.json in cwd.
The transfer uses scipy.signal.lfilter and NumPy power-table doubling.
Usage: python3 cp29_numeric.py [smax=18]  (RAM guard uses /proc/meminfo).
"""
import sys, json, time
from pathlib import Path
import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
from scipy.signal import lfilter

def pow4_table(modulus, length):
    powers=np.empty(length,np.int64);powers[0]=1;k=1
    while k<length:
        m=min(k,length-k)
        factor=int(powers[k-1])*4 %modulus
        powers[k:k+m]=(powers[:m]*factor)%modulus
        k+=m
    return powers

def transfer_numpy(modulus,prev,make_next):
    """Stable reverse geometric filter; exactly same all-support transfer as the FFT."""
    L=modulus//3;phi=2*L
    powers=pow4_table(modulus,L)
    q=np.zeros(phi,float)
    # process in blocks to avoid gigantic fancy-index intermediate arrays.
    for lo in range(0,L,1_000_000):
        hi=min(lo+1_000_000,L)
        indices=(powers[lo:hi]-1)//3
        q[2*lo:2*hi:2]=prev[indices]
    del powers
    a=min(L,530)
    initial=float(np.dot(q[:2*a:2], np.exp2(-2*np.arange(a,dtype=float)-1)))
    if phi<1075:initial/= -np.expm1(-phi*np.log(2.))
    # lfilter receives q[phi-1],...,q[1]; initial condition = .5*initial
    rev, _ = lfilter([.5],[1.,-.5],q[:0:-1],zi=[.5*initial])
    del q
    x=np.empty(phi,float);x[-1]=initial;x[:-1]=rev[::-1]
    del rev
    result={'mass':float(np.sum(x)), 'chi':float(modulus*np.dot(x,x)),
            'max_scaled':float(modulus*np.max(x)),
            'negative_mass_before_clipping':float(-np.sum(x[x<0]))}
    nxt=None
    if make_next:
        nxt=np.zeros(modulus,float)
        # scatter powers of two in chunks using period-doubling construction.
        powers=np.empty(phi,np.int64);powers[0]=1;k=1
        while k<phi:
            m=min(k,phi-k);factor=int(powers[k-1])*2%modulus
            powers[k:k+m]=(powers[:m]*factor)%modulus;k+=m
        nxt[powers]=x
        del powers
    return result,nxt

def high_precision(smax=10):
    mp.mp.dps=60; p=[mp.mpf(1)]; out=[]; prev=mp.mpf(1)
    for s in range(1,smax+1):
        M=3**s; L=M//3; phi=2*L
        q=[mp.mpf(0)]*phi; v=1
        for k in range(L):
            q[2*k]=p[(v-1)//3];v=(4*v)%M
        initial=mp.fsum([mp.ldexp(q[2*k],-2*k-1) for k in range(min(L,300))])
        initial/= -mp.expm1(-phi*mp.log(2))
        x=[mp.mpf(0)]*phi;x[-1]=initial
        for k in range(phi-2,-1,-1):x[k]=(x[k+1]+q[k+1])/2
        p=[mp.mpf(0)]*M; v=1
        for k in range(phi): p[v]=x[k];v=(2*v)%M
        chi=M*mp.fsum(v*v for v in x)
        out.append({'s':s,'chi':mp.nstr(chi,57),'E':mp.nstr(chi-prev,57),'max_scaled':mp.nstr(M*max(x),55),
                    'mass_error':mp.nstr(mp.fsum(x)-1,4)})
        prev=chi
    return out

def fit_models(rows):
    res={}; names={'constant':lambda t:0*t+1, 'a+b/s':lambda t:1/t,
                   'a+b log(s)':np.log, 'a+b/log(s)':lambda t:1/np.log(t),
                   'a+b/sqrt(s)':lambda t:1/np.sqrt(t)}
    for start,end in [(a,b) for b in [16,18] for a in [3,5,8,10,12] if b<=len(rows)]:
        ss=np.array([r['s'] for r in rows if start<=r['s']<=end],float)
        yy=np.array([r['E'] for r in rows if start<=r['s']<=end])
        rr={}
        for name,fn in names.items():
            X=np.ones((len(ss),1)) if name=='constant' else np.column_stack([np.ones(len(ss)),fn(ss)])
            coef=np.linalg.lstsq(X,yy,rcond=None)[0]; err=yy-X@coef
            rr[name]={'parameters_a_b':[float(v) for v in coef], 'rmse':float(np.linalg.norm(err)/np.sqrt(len(err))),
                      'max_abs_residual':float(np.max(np.abs(err))),
                      'residual_at_end':float(err[-1]), 'predicted_E_18':float(np.array([1.,fn(np.array([18.]))[0]])@coef) if name!='constant' else float(coef[0])}
        res[f'{start}:{end}']=rr
    return res

def original_fft_small_diagnostics(high,smax=10):
    """Replicate read-only CP17 FFT transfer without clipping, then with clipping."""
    p=np.array([1.]);res=[];prev=1.
    for s in range(1,min(smax,len(high))+1):
        M=3**s;phi=2*M//3
        powers=np.empty(phi,np.int64);powers[0]=1;k=1
        while k<phi:
            m=min(k,phi-k);factor=int(powers[k-1])*2%M
            powers[k:k+m]=(powers[:m]*factor)%M;k+=m
        logs=np.full(M,-1,np.int64);logs[powers]=np.arange(phi)
        z=1+3*np.arange(M//3)
        qz=np.zeros(phi);np.add.at(qz,logs[z],p)
        rr=np.arange(phi,dtype=float)
        weights=np.where(rr>0,np.exp2(-rr),np.exp2(-float(phi)))/(-np.expm1(-phi*np.log(2.)))
        qx=np.fft.irfft(np.fft.rfft(qz)*np.conj(np.fft.rfft(weights)),n=phi)
        neg=qx<0; negative_mass=float(-qx[neg].sum()); negative_count=int(neg.sum())
        rawchi=M*np.dot(qx,qx)
        qx[neg]=0
        clipchi=M*np.dot(qx,qx)
        res.append({'s':s,'negative_count':negative_count,'negative_mass_before_clipping':negative_mass,
                    'fft_chi_raw':float(rawchi),'fft_chi_clipped':float(clipchi),
                    'clip_change_in_chi':float(clipchi-rawchi),
                    'raw_chi_mp60_error':float(abs(mp.mpf(rawchi)-mp.mpf(high[s-1]['chi']))),
                    'clipped_chi_mp60_error':float(abs(mp.mpf(clipchi)-mp.mpf(high[s-1]['chi']))),
                    'zero_index_weight_underflow':bool(phi>1074),
                    'zero_index_true_weight_bound':float(np.exp2(-float(phi)))})
        p=np.zeros(M);p[powers]=qx
    return res

def independent_small_checks(rows,smax=8):
    """Direct summation over x and A-residue, no discrete logs/FFT/filter."""
    p=np.array([1.]); chi_prev=1.;result=[]
    for s in range(1,min(smax,len(rows))+1):
        M=3**s;phi=2*(M//3);z=1+3*np.arange(M//3)
        cur=np.zeros(M)
        inv2=pow(2,-1,M); invpow=1
        for a in range(1,min(phi,1074)+1):
            invpow=invpow*inv2%M
            w=np.exp2(-float(a))/(-np.expm1(-phi*np.log(2.)))
            np.add.at(cur,(invpow*z)%M,w*p)
        chi=M*np.dot(cur,cur)
        centered=cur-p[np.arange(M)% (M//3)]/3
        E_lift=M*np.dot(centered,centered)
        result.append({'s':s,'chi_direct':float(chi),'E_lift_direct':float(E_lift),
                       'max_scaled_direct':float(M*max(cur)),
                       'chi_discrepancy':float(chi-rows[s-1]['chi']),
                       'lift_vs_direct_delta':float(E_lift-(chi-chi_prev)),
                       'lift_vs_transfer_E':float(E_lift-rows[s-1]['E'])})
        p=cur;chi_prev=chi
    return result

def brute_pairs(rows, smax=3, cutoff=40):
    """Literal enumeration of A WORDS (not just A residue classes).
    Return unconditional 3^s* collision from every first split j and same word;
    discarding any A>cutoff has absolute contribution <=2*s*3^s*2^-cutoff.
    """
    from collections import defaultdict
    from itertools import product
    ans=[]
    for s in range(1,min(smax,len(rows))+1):
        M=3**s
        groups=[defaultdict(float) for j in range(s+1)]
        inv2=[0]+[pow(pow(2,a,M),-1,M) for a in range(1,cutoff+1)]
        for word in product(range(1,cutoff+1),repeat=s):
            # accumulated 3^(i) * 2^(-sum A) modulo M
            v=0; scale=1; three=1
            for a in word:
                scale=scale*inv2[a]%M
                v=(v+three*scale)%M;three=three*3%M
            w=2.**(-sum(word))
            for j in range(s+1): groups[j][(word[:j],v)]+=w
        B=[float(M*sum(z*z for z in g.values())) for g in groups]
        first=[B[j-1]-B[j] for j in range(1,s+1)]
        expected=[rows[s-j]['E'] for j in range(1,s+1)]
        same=(1-4.**(-cutoff))**s
        ans.append({'s':s,'cutoff_A':cutoff,'tail_collision_bound_scaled':2*s*M*2.**(-cutoff),
                    'first_split_scaled':first,'expected_E_reversed':expected,
                    'same_word_scaled':B[s], 'same_word_analytic_truncated':same,
                    'sum_scaled':B[0], 'chi':rows[s-1]['chi'],
                    'max_abs_first_split_discrepancy':max(abs(a-b) for a,b in zip(first,expected))})
    return ans

def main():
    smax=int(sys.argv[1]) if len(sys.argv)>1 else 18
    available_kib=int(next(line.split()[1] for line in open('/proc/meminfo') if line.startswith('MemAvailable:')))
    avail=available_kib*1024
    # Upper bound on main live arrays prev, q, x, power table, and next p.
    peak=8*(3**smax+3**(smax-1)+4*3**(smax-1))
    if peak>0.7*avail: raise MemoryError(f'Projected {peak/2**30:.2f} GiB exceeds 70% of available {avail/2**30:.2f} GiB')
    p=np.array([1.],float); prev=1.; rows=[]
    for s in range(1,smax+1):
        start=time.monotonic(); M=3**s
        diag,nxt=transfer_numpy(M,p,s<smax)
        chi=diag.pop('chi')
        row={'s':s,'chi':chi,'E':chi-prev,**diag,'seconds':time.monotonic()-start}
        rows.append(row); print(json.dumps(row),flush=True)
        del p;p=nxt;prev=chi
    high=high_precision(min(10,smax))
    for r,h in zip(rows,high):
        r['mp60_chi_abs_error']=float(abs(mp.mpf(r['chi'])-mp.mpf(h['chi'])))
        r['mp60_E_abs_error']=float(abs(mp.mpf(r['E'])-mp.mpf(h['E'])))
    pair=[{'s':r['s'],'same_A_word_scaled_exact':1.0,
           'first_separation_j_scaled':[{'j':j,'value':rows[r['s']-j]['E']}
                                         for j in range(1,r['s']+1)],
           'total':r['chi']} for r in rows]
    u=2.**-53
    errors=[]
    for r in rows:
        s=r['s']; M=3**s; phi=2*M//3; delta=s*1100*u+2**-1060
        gamma=(phi+1)*u/(1-(phi+1)*u)
        ec=2*r['max_scaled']*delta+M*delta**2+gamma*(r['chi']+2*r['max_scaled']*delta+M*delta**2)
        errors.append({'s':s,'conservative_chi_abs_bound':ec,'conservative_E_abs_bound':ec+(errors[-1]['conservative_chi_abs_bound'] if errors else 0.),
                       'l1_transfer_bound':delta,'naive_dot_gamma':gamma})
    M17=3**17; M18=3**18
    obj={'memory_original_fft_estimates':{'s17_states':M17,'s18_states':M18,
        's17_minimum_peak_bytes':int((19.63e9)/3),'s18_minimum_peak_bytes':int(19.63e9),
        's17_time_seconds_estimate':95,'s18_time_seconds_estimate':305,
        'baseline_s16_seconds_source':'user context approx 30 seconds; scaling 3*N log(N)',
        's18_original_skipped':True,'original_fft_peak_note':'pw,dlog,Z,qZ,r,w,p_prev, 2 complex FFT outputs and product; excludes FFT workspace and allocation temporaries'},
         'roundoff_bounds':{'assumptions':'IEEE float64, exact int64 modular arithmetic, ordinary sequential dot worst-case gamma_N, positive transfer. Bound 1100*u*s for total variation L1 incl initialization (at most 530 positive terms and 2u local). Each chi error <= 2*M*max(p_computed)*delta+M*delta^2+gamma_(phi+1)*chi. Conservative, not certified for arbitrary vendor nonstandard BLAS.','per_s':errors},
         'pair_breakdown':pair,'method':'numpy/scipy float64, exact periodic geometric weights in reverse stable recurrence; no FFT/clipping; mp60 reference',
         'free_g_command':'free -g', 'memory_available_bytes':avail,'alternative_peak_upper_bytes':peak,
         'rows':rows,'mp60':high,'fft_small':original_fft_small_diagnostics(high),'brute_first_split':brute_pairs(rows),'direct_checks_s_le_8':independent_small_checks(rows),'fits':fit_models(rows) if smax>=16 else {}}
    (HERE/'cp29_numeric.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
