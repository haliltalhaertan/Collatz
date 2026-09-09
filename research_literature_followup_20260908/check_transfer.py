"""Small exact transfer checks motivated by literature; no asymptotic claim."""
from pathlib import Path
from fractions import Fraction
import json

def H(x): return (3*x+1)//2 if x&1 else x//2
def parity_word(x,t):
    w=0
    for i in range(t):
        w|=(x&1)<<i; x=H(x)
    return w

def complement(t):
    q=1<<t; words=[parity_word(x,t) for x in range(q)]
    assert len(set(words))==q
    inverse={v:x for x,v in enumerate(words)}
    omega=[inverse[w^(q-1)] for w in words]
    assert all(omega[omega[x]]==x and
        words[x].bit_count()+words[omega[x]].bit_count()==t for x in range(q))
    c=omega[0]; slope=(omega[1]-c)%q
    affine=all(omega[x]==(slope*x+c)%q for x in range(q))
    return dict(t=t,omega=omega,affine=affine,
        forced_affine_slope=slope,forced_affine_offset=c)

def spectrum(row):
    G=row['G']; q=len(G); t=row['t']; total=sum(G)
    W=[sum(v*(-1 if (a&s).bit_count()%2 else 1)
           for a,v in enumerate(G)) for s in range(q)]
    energy=[sum(W[s]**2 for s in range(1,q) if s.bit_count()==d)
            for d in range(t+1)]
    var=Fraction(sum(energy),q*q)
    assert var==Fraction(row['variance'])
    return dict(r=row['r'],t=t,centered_walsh_degree=max(
        (s.bit_count() for s in range(1,q) if W[s]),default=0),
        energy_by_degree=[str(Fraction(e,q*q)) for e in energy],
        normalized_moment_22=str(sum((Fraction(abs(q*g-total),total)**22
            for g in G),Fraction(0))/q))

if __name__=='__main__':
    root=Path(__file__).resolve().parent.parent
    old=json.loads((root/'research_reassessment_20260908/GROUPED_VARIANCE.json').read_text())
    out=dict(complement_checks=[complement(t) for t in range(1,6)],
             spectra=[spectrum(row) for row in old['panels']])
    Path(__file__).with_name('TRANSFER_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(complement_mod8=out['complement_checks'][2],
        spectra=[{k:v for k,v in row.items() if k!='normalized_moment_22'}
                 for row in out['spectra']]),indent=2))
