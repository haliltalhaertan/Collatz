"""Exact split-join diagnostic; preserves both full residue histograms."""
from collections import Counter
from functools import lru_cache
from math import comb, isqrt
from fractions import Fraction
from pathlib import Path
import hashlib,json

@lru_cache(None)
def numerators(length,total):
    if length==1:
        return (1,)
    out=[]
    # B for word prefix followed by m.
    for m in range(1,total-length+2):
        a=total-m
        out.extend(3*B+2**a for B in numerators(length-1,a))
    assert len(out)==comb(total-1,length-1)
    return tuple(out)

def run():
    root=Path(__file__).resolve().parent
    src=root.parent/'research_compressed_count_20260908/RESULT.json'
    raw=src.read_bytes(); old=json.loads(raw)
    rows=[]
    for x in old['rows']:
        r,A,L=x['r'],x['A'],x['L']
        if r<4:continue
        k=1
        while 3**k<L:k+=1
        j=r-k
        assert j>=1
        modulus=3**j; suffixmod=3**k
        Q=fiber=cs=candidates=0; baseline=Fraction(0); terms=[]
        for R in range(k,A-j+1):
            a=A-R
            prefix=Counter((B*pow(2,-a,modulus))%modulus for B in numerators(j,a))
            demand=Counter()
            for B in numerators(k,R):
                n=B*pow(2,-R,suffixmod)%suffixmod
                if n<L:
                    delta=2**R*n-B
                    assert delta%suffixmod==0
                    target=(delta//suffixmod)%modulus
                    lifted=B*pow(2,-R,3**r)%(3**r)
                    assert lifted%suffixmod==n
                    assert target==(-pow(2,R,modulus)*(lifted//suffixmod))%modulus
                    demand[target]+=1
            C=sum(demand.values()); M=max(prefix.values())
            exact=sum(v*demand[z] for z,v in prefix.items())
            ep=sum(v*v for v in prefix.values()); ed=sum(v*v for v in demand.values())
            prod=ep*ed; cb=isqrt(prod); cb+=int(cb*cb<prod)
            Q+=exact; fiber+=M*C; cs+=cb; candidates+=C
            baseline+=Fraction(sum(prefix.values())*C,modulus)
            terms.append(dict(R=R,prefix_mass=a,prefix_words=sum(prefix.values()),
                suffix_candidates=C,prefix_maxfiber=M,prefix_energy=ep,
                demand_energy=ed,exact=exact,fiber_bound=M*C,cs_bound=cb))
        assert Q==x['Q'] and Q<=fiber and Q<=cs
        # Independent unsplit closed endpoint enumeration on the same word set.
        direct=sum((B*pow(2,-A,3**r))%(3**r)<L for B in numerators(r,A))
        assert direct==Q
        rows.append(dict(r=r,A=A,b=x['b'],L=L,j=j,k=k,N=x['N'],Q=Q,
            suffix_candidates=candidates,maxfiber_bound=fiber,cs_bound=cs,
            uniform_target_baseline=str(baseline),terms=terms))
    out=dict(status='PASS',source_sha256=hashlib.sha256(raw).hexdigest(),cases=len(rows),rows=rows)
    (root/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',cases=len(rows),examples=[x for x in rows if x['r']==10 and x['A']==15]),indent=2))

if __name__=='__main__':run()
