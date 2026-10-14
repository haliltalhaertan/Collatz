#!/usr/bin/env python3
"""Exact 3-adic offset separation for finite truncations of a countable IFS.

Convention: T_(a1,...,ak)=f_a1∘...∘f_ak;
T_w(0)=sum_{j=1}^k 3^(j-1) 2^(-sum_{i=1}^j ai).
For countably infinite alphabet, inf of distances at EACH k is 0 (not attained).
"""
from itertools import product
from fractions import Fraction
import json, argparse

def offset(word):
    s=sum(word)
    return Fraction(sum(3**j * 2**(s-sum(word[:j+1])) for j in range(len(word))),2**s)

def vp3(n):
    if n==0:raise ValueError('zero: exact overlap')
    c=0
    while n%3==0:n//=3;c+=1
    return c

def compute(k,A):
    words=list(product(range(1,A+1),repeat=k))
    vals=[offset(w) for w in words]
    assert len(set(vals))==len(vals),'unexpected exact overlap'
    # A collision modulo 3^m gives a pair with v3 >= m.  Find last m with a collision.
    # This hash algorithm uses exact rational arithmetic and avoids O(A^(2k)) pairs.
    last_pair=None;m=1
    while True:
        p=3**m;seen={};hit=None
        for w,x in zip(words,vals):
            r=(x.numerator*pow(x.denominator,-1,p))%p
            if r in seen:
                hit=(seen[r],w);break
            seen[r]=w
        if hit is None:break
        last_pair=hit;m+=1
        if m>200:raise RuntimeError('safety: near collision too deep')
    exponent=m-1
    if last_pair:
        x,y=map(offset,last_pair)
        assert vp3((x-y).numerator)==exponent
    return {'k':k,'alphabet_max_A':A,'word_count':len(words),
            'max_pair_v3':exponent,'min_pair_distance':f'3^-{exponent}',
            'natural_scale':f'3^-{k}','distance_over_natural_scale':f'3^{k-exponent}',
            'witness':last_pair}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-k',type=int,default=7)
    ap.add_argument('--max-words',type=int,default=22000)
    args=ap.parse_args()
    rows=[compute(k,A) for A in (2,3,4,6) for k in range(1,args.max_k+1) if A**k<=args.max_words]
    for r in rows:print(f"A={r['alphabet_max_A']:2d} k={r['k']} words={r['word_count']:6d} v_max={r['max_pair_v3']:2d} scale=3^-{r['k']} witness={r['witness']}")
    with open('separation_data.json','w') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
    # k=1, a and a+2*3^(m-1) both positive: ord_(3^m)(2)=2*3^(m-1).
    # Appending the same (k-1)-letter suffix preserves congruence modulo 3^m.
    for m in (1,2,3,4,5):
        a,b=1,1+2*3**(m-1)
        assert vp3((offset((a,))-offset((b,))).numerator)>=m
    print('Infinite alphabet: inf distance=0 at each fixed k (no minimum); exact word offsets remain distinct.')
if __name__=='__main__':main()
