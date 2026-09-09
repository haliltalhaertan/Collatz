"""Bounded exact merging extension of the existing 16-step checkpoint sieve."""
import json
from pathlib import Path
base=Path(__file__).resolve().parent
old=json.loads((base.parent/'research_checkpoint_bridge_20260908/CERTIFICATES.json').read_text())
covered={c['k_residue'] for c in old}
A=27*2**16
new=[]
for r in range(2**16):
    if r in covered: continue
    B=20+27*r
    a,b=A,B
    found=None
    for j in range(17):
        for u in range(1,7):
            ca,cb=2**u*a,2**u*b-1
            if ca%3 or cb%3: continue
            ma,mb=ca//3,cb//3
            if ma%2 or mb%2!=1: continue
            for v in range(7):
                sa,sb=2**v*ma,2**v*mb
                if sa%27==0 and sb%27==20 and sa<=A and 0<sb<B:
                    found=dict(k_residue=r,forward_steps=j,inverse_exponent=u,
                               doublings=v,target_a=sa,target_b=sb,
                               common_a=a,common_b=b)
                    break
            if found: break
        if found: break
        if j==16: break
        assert a%2==0
        a,b=(3*a//2,(3*b+1)//2) if b%2 else (a//2,b//2)
    if found: new.append(found)

# Verify BOTH affine paths meet, including all-parameter parity invariants.
for c in new:
    a,b=A,20+27*c['k_residue']
    for _ in range(c['forward_steps']):
        assert a%2==0
        a,b=(3*a//2,(3*b+1)//2) if b%2 else (a//2,b//2)
    assert (a,b)==(c['common_a'],c['common_b'])
    s,t=c['target_a'],c['target_b']
    assert s%27==0 and t%27==20 and s<=A and 0<t<20+27*c['k_residue']
    for _ in range(c['doublings']):
        assert s%2==0 and t%2==0
        s,t=s//2,t//2
    assert s%2==0 and t%2==1
    s,t=3*s,3*t+1
    for _ in range(c['inverse_exponent']):
        assert s%2==0 and t%2==0
        s,t=s//2,t//2
    assert (s,t)==(a,b)

summary=dict(old_certified=len(covered),new_merge_certified=len(new),
             total_certified=len(covered)+len(new),remaining=2**16-len(covered)-len(new),
             forward_depth=16,inverse_exponent_max=6,doublings_max=6,
             verified=True,examples=new[:8])
(base/'CERTIFICATES.json').write_text(json.dumps(new,separators=(',',':'))+'\n')
(base/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
