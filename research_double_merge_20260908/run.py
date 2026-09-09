import json, hashlib
from pathlib import Path
base=Path(__file__).resolve().parent
inputs=[base.parent/p/'CERTIFICATES.json' for p in ('research_checkpoint_bridge_20260908','research_merge_extension_20260908')]
covered=set()
for p in inputs: covered.update(c['k_residue'] for c in json.loads(p.read_text()))
A=27*65536

def forward(a,b,j):
    for _ in range(j):
        assert a%2==0
        a,b=(3*a//2,(3*b+1)//2) if b%2 else (a//2,b//2)
    return a,b

def parent(a,b,u):
    a,b=(2**u)*a,(2**u)*b-1
    if a%3 or b%3: return None
    a,b=a//3,b//3
    return (a,b) if a%2==0 and b>0 and b%2 else None

def witness(A,B,j,u,v,w):
    a,b=forward(A,B,j)
    p=parent(a,b,u)
    if p is None: return None
    p=parent(*p,v)
    if p is None: return None
    s,t=p[0]*2**w,p[1]*2**w
    if s%27 or t%27!=20 or s>A or not 0<t<B: return None
    # Check the target path independently in the forward direction.
    sa,sb=s,t
    for _ in range(w):
        assert sa%2==0 and sb%2==0
        sa,sb=sa//2,sb//2
    for exponent in (v,u):
        assert sa%2==0 and sb%2==1
        sa,sb=3*sa,3*sb+1
        for _ in range(exponent):
            assert sa%2==0 and sb%2==0
            sa,sb=sa//2,sb//2
    assert (sa,sb)==(a,b)
    return s,t

new=[]
for r in range(65536):
    if r in covered: continue
    B=20+27*r
    a,b=A,B
    found=None
    for j in range(17):
        for u in range(1,5):
            p=parent(a,b,u)
            if p is None: continue
            for v in range(1,5):
                pp=parent(*p,v)
                if pp is None: continue
                for w in range(5):
                    s,t=pp[0]*2**w,pp[1]*2**w
                    if s%27==0 and t%27==20 and s<=A and 0<t<B:
                        assert witness(A,B,j,u,v,w)==(s,t)
                        found=dict(k_residue=r,j=j,u=u,v=v,w=w,target_a=s,target_b=t)
                        break
                if found: break
            if found: break
        if found: break
        if j<16: a,b=forward(a,b,1)
    if found:new.append(found)

# Seek shorter parameterizations for each discovered witness, verifying afresh.
compressed={}
for c in new:
    for d in range(c['j'],17):
        residue=c['k_residue']%(2**d)
        result=witness(27*2**d,20+27*residue,c['j'],c['u'],c['v'],c['w'])
        if result:
            key=(d,residue,c['j'],c['u'],c['v'],c['w'])
            compressed[key]=dict(depth=d,k_residue=residue,j=c['j'],u=c['u'],v=c['v'],w=c['w'],target_a=result[0],target_b=result[1])
            break
rules=sorted(compressed.values(),key=lambda c:(c['depth'],c['k_residue']))
summary=dict(previous=len(covered),additional=len(new),total=len(covered)+len(new),remaining=65536-len(covered)-len(new),forward_depth=16,u_max=4,v_max=4,w_max=4,compressed_witness_count=len(rules),examples=rules[:5])
for name,data in [('CERTIFICATES.json',new),('RULES.json',rules),('RESULT.json',summary)]:
    (base/name).write_text(json.dumps(data,indent=2)+'\n')
(base/'INPUTS.json').write_text(json.dumps([dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs],indent=2)+'\n')
print(json.dumps(summary,indent=2))
