"""Exact arithmetic for a joint interval/residue Bellman certificate."""
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import hashlib

def choices(r,A,j,a):
    k,R=r-j,A-a
    return (R,) if k==1 else range(1,R-k+2)

def hybrid(r,A,L,t,ell):
    assert 0<=t<=r and 0<=ell<=r-t
    q,H,P=3**r,3**t,3**ell
    W=q//H
    @lru_cache(None)
    def successors(a,b,s):
        c=pow(2,a-A,q)
        lo,hi=b*W,(b+1)*W-1
        first=lo+(s-lo)%P
        last=hi-(hi-s)%P
        assert first<=last
        out=[]
        for v in range((3*first+c)//W,(3*last+c)//W+1):
            lower=max(lo,-(-(v*W-c)//3))
            upper=min(hi,((v+1)*W-1-c)//3)
            candidate=lower+(s-lower)%P
            if candidate<=upper:
                out.append((v%H,(3*s+c)%P))
        return tuple(sorted(set(out)))
    @lru_cache(None)
    def F(j,a,b,s):
        if j==r:
            # W is divisible by P, so the cell's least integer is bW+s.
            return int(b*W+s<L)
        nxt=successors(a,b,s)
        assert nxt
        return sum(max(F(j+1,a+m,b2,s2) for b2,s2 in nxt)
                   for m in choices(r,A,j,a))
    x1=pow(2,-A,q)
    value=sum(F(1,m,x1//W,x1%P) for m in choices(r,A,0,0))
    return dict(ell=ell,upper=value,states=F.cache_info().currsize,
                successor_states=successors.cache_info().currsize,
                exact_precision=(t+ell==r))

def main():
    root=Path(__file__).resolve().parent
    source=root.parent/'research_compressed_count_20260908'/'RESULT.json'
    raw=source.read_bytes()
    previous=json.loads(raw)
    rows=[]
    for x in previous['rows']:
        r,A,L=x['r'],x['A'],x['L']
        t=min(3,r-1); N=comb(A-1,r-1)
        values=[hybrid(r,A,L,t,ell) for ell in range(min(3,r-t)+1)]
        old=next(y['upper'] for y in x['high'] if y['t']==t)
        assert values[0]['upper']==old
        for i,v in enumerate(values):
            assert x['Q']<=v['upper']<=N
            if i: assert v['upper']<=values[i-1]['upper']
            if v['exact_precision']: assert v['upper']==x['Q']
            elif L>=3**v['ell']:
                assert v['upper']*3**t>=N
        rows.append(dict(r=r,A=A,b=x['b'],L=L,N=N,Q=x['Q'],
                         exact_states=x['exact_states'],t=t,hybrid=values))
    splice=[hybrid(2,3,3,1,ell) for ell in (0,1)]
    assert [v['upper'] for v in splice]==[2,1]
    # A compressed, low-residue-preserving spurious path for w=(1,1,1,3).
    # Actual path: 0->19->14->37->20. Relaxation substitutes14->11,28->31.
    word=(1,1,1,3); x=0; a=0; actual=[0]
    for m in word:
        x=(3*x+pow(2,a-6,81))%81; a+=m; actual.append(x)
    assert actual==[0,19,14,37,20]
    replacements=[(14,11),(28,31)]
    assert all(old//9==new//9 and old%3==new%3 for old,new in replacements)
    assert (3*11+pow(2,2-6,81))%81==28
    assert (3*31+pow(2,3-6,81))%81==2
    assert actual[-1]>=9 and 2<9
    witness=dict(r=4,A=6,L=9,t=2,ell=1,word=word,actual=actual,
                 replacements=replacements,abstract_endpoint=2)
    result=dict(status='PASS',source_sha256=hashlib.sha256(raw).hexdigest(),
                cases=len(rows),bounds=sum(len(x['hybrid']) for x in rows),
                splice=splice,compressed_spurious_witness=witness,rows=rows)
    (root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    compressed=[(x,v) for x in rows for v in x['hybrid']
                if v['ell'] and not v['exact_precision']]
    print(json.dumps(dict(status='PASS',cases=len(rows),bounds=result['bounds'],
        compressed_refinements=len(compressed),
        strict_improvements=sum(v['upper']<x['hybrid'][0]['upper'] for x,v in compressed),
        r10_examples=[x for x in rows if x['r']==10 and x['A']==15]),indent=2))

if __name__=='__main__': main()
