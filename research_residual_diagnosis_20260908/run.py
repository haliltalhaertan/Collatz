"""Diagnose unchanged witness bounds; allow a finite exceptional parameter prefix."""
import json, hashlib
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parent
dirs=['research_checkpoint_bridge_20260908','research_merge_extension_20260908','research_double_merge_20260908']
covered=set(); inputs=[]
for d in dirs:
    p=P.parent/d/'CERTIFICATES.json'
    inputs.append(dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    covered.update(c['k_residue'] for c in json.loads(p.read_text()))
A=27*65536
def parent(a,b,u):
    x,y=a*2**u,b*2**u-1
    if x%3 or y%3: return None
    x,y=x//3,y//3
    return (x,y) if x%2==0 and y>0 and y%2 else None
def candidates(a,b,j):
    if j: yield a,b,[],0
    for u in range(1,7):
        p=parent(a,b,u)
        if p:
            for w in range(7):yield p[0]*2**w,p[1]*2**w,[u],w
    for u in range(1,5):
        p=parent(a,b,u)
        if not p:continue
        for v in range(1,5):
            q=parent(*p,v)
            if q:
                for w in range(5):yield q[0]*2**w,q[1]*2**w,[u,v],w
def verify(c):
    a,b=A,20+27*c['r']
    for _ in range(c['j']):
        assert a%2==0
        a,b=(3*a//2,(3*b+1)//2) if b%2 else (a//2,b//2)
    x,y=c['a'],c['b']
    for _ in range(c['w']):
        assert x%2==y%2==0
        x,y=x//2,y//2
    for e in reversed(c['parents']):
        assert x%2==0 and y%2==1
        x,y=3*x,3*y+1
        for _ in range(e):
            assert x%2==y%2==0
            x,y=x//2,y//2
    assert (a,b)==(x,y)
    t=c['threshold']; B=20+27*c['r']
    assert c['a']<A and c['a']*t+c['b']<A*t+B
    assert t==0 or c['a']*(t-1)+c['b']>=A*(t-1)+B
    assert c['a']%27==0 and c['b']%27==20 and c['b']>0

counts=Counter(); certs=[]; obstructed=[]
for r in range(65536):
    if r in covered:continue
    B=20+27*r;a,b=A,B;best=None;valid=False
    for j in range(17):
        for x,y,parents,w in candidates(a,b,j):
            if x%27 or y%27!=20 or y<=0:continue
            valid=True
            if x<A:
                threshold=max(0,(y-B)//(A-x)+1)
                c=dict(r=r,j=j,a=x,b=y,parents=parents,w=w,threshold=threshold)
                if best is None or threshold<best['threshold']:best=c
            elif x==A and y<B:
                raise AssertionError('previous search missed an unconditional rule')
        if j<16:
            assert a%2==0
            a,b=(3*a//2,(3*b+1)//2) if b%2 else (a//2,b//2)
    if best:
        verify(best);certs.append(best);counts['tail_descent']+=1
    else:
        counts['no_contracting_checkpoint' if valid else 'no_checkpoint']+=1
        obstructed.append(r)

# Base cases are checked directly, never inferred from minimum exclusion.
base=[]
for c in certs:
    assert c['threshold']<=1000, 'retain certificate but review larger base separately'
    for t in range(c['threshold']):
        n=A*t+20+27*c['r'];x=n;steps=0
        while x!=1 and steps<100000:
            x=x//2 if x%2==0 else (3*x+1)//2;steps+=1
        assert x==1
        base.append(dict(r=c['r'],t=t,n=n,steps=steps))
result=dict(original_unresolved=65536-len(covered),categories=dict(counts),
            new_minimum_excluded=len(certs),remaining=65536-len(covered)-len(certs),
            max_threshold=max([c['threshold'] for c in certs],default=0),base_checks=base,
            scope='Tail merging plus individually verified finite bases; not convergence of entire cylinders.')
for name,data in [('RESULT.json',result),('CERTIFICATES.json',certs),('OBSTRUCTED.json',obstructed),('INPUTS.json',inputs)]:
    (P/name).write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(result,indent=2))
