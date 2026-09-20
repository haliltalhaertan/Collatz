#!/usr/bin/env python3
"""Task2: test A3 collision criterion and cycle reformulation. Exact ints."""
from collections import defaultdict

def Hp(x): return (3*x+1)//2 if x%2!=0 else x//2
def B_of_word(w):
    B=0
    for i,wi in enumerate(w):
        B=(3**wi)*B+wi*(2**i)
    return B

def orbit_stats_from_h(h,m):
    x=h; k=0; w=[]
    for i in range(m):
        wi=1 if x%2!=0 else 0
        w.append(wi)
        if wi: k+=1
        x=Hp(x)
    return k,x,w

def words_of_m(m):
    n=1<<(m-1)
    for mask in range(n):
        w=[1]*m
        for i in range(1,m):
            w[i]=(mask>>(i-1))&1
        yield w

def test_A3(m):
    # group words by (k) then by e exact and by B mod 3^k
    from collections import defaultdict
    print(f"=== m={m} ===")
    for k in range(1,m+1):
        ws=[w for w in words_of_m(m) if sum(w)==k]
        if not ws: continue
        # compute h_w: unique odd h<2^m with word w (find via brute h scan)
        # build map h->word
        h_to_w={}
        for h in range(1,2**m,2):
            kk,ee,ww=orbit_stats_from_h(h,m)
            h_to_w[h]=tuple(ww)
        w_to_h={v:k2 for k2,v in h_to_w.items()}
        # check bijection: number of words with w0=1 equals 2^{m-1}
        # compute e_w, B_w, h_w
        e_of={}; B_of={}; h_of={}
        for w in ws:
            t=tuple(w)
            assert t in w_to_h, f"word {w} missing!"
            h=w_to_h[t]
            kk,ee,ww=orbit_stats_from_h(h,m)
            assert kk==k and list(ww)==w
            B=B_of_word(w)
            assert (2**m)*ee==(3**k)*h+B
            e_of[t]=ee; B_of[t]=B; h_of[t]=h
        # partitions
        # by e exact
        by_e=defaultdict(list)
        for t in e_of: by_e[e_of[t]].append(t)
        # by B mod 3^k
        mod=3**k
        by_Bmod=defaultdict(list)
        for t in B_of: by_Bmod[B_of[t]%mod].append(t)
        # by e mod 3^k
        by_emod=defaultdict(list)
        for t in e_of: by_emod[e_of[t]%mod].append(t)
        # check: e exact partition == Bmod partition?
        # convert to sets of frozensets
        def part(s): return set(frozenset(v) for v in s.values())
        eq_exact = (part(by_e)==part(by_Bmod))
        eq_cong = (part(by_emod)==part(by_Bmod))
        maxe=max(e_of.values()); mine=min(e_of.values())
        print(f" k={k} n={len(ws)} e_range=[{mine},{maxe}] 3^k={mod} "
              f"#e_classes={len(by_e)} #Bmod_classes={len(by_Bmod)} #emod_classes={len(by_emod)} "
              f"exact==Bmod? {eq_exact}  emod==Bmod? {eq_cong}")
        if not eq_exact:
            # show witness: two words same Bmod but different e, or same e but different Bmod
            # find example
            for cls in by_Bmod.values():
                es=set(e_of[t] for t in cls)
                if len(es)>1:
                    print(f"   witness Bmod-collision splits e: Bmod class size {len(cls)} e values {sorted(es)[:5]}")
                    break
        # range bound check 1<=e<=3^k-1 ?
        viol=sum(1 for e in e_of.values() if not (1<=e<=mod-1))
        print(f"   range-bound 1<=e<=3^k-1 violations: {viol}/{len(ws)}")
        # cycle words in this stratum? e==h ?
        cyc=[t for t in e_of if e_of[t]==h_of[t]]
        print(f"   cycles (e==h): {len(cyc)} {cyc[:3]}")

for m in [4,5,6,8]:
    test_A3(m)
