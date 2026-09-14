#!/usr/bin/env python3
"""Task 1: self-consistency vs divisibility for m<=20. Exact integer arithmetic.
Enumerate all binary words w length m with w0=1 (odd start). For each:
  B_w via B_{i+1}=3^{w_i} B_i + w_i 2^i, B_0=0
  k = weight, D = 2^m - 3^k
  divisibility: D | B_w  (D != 0 always for m>=1)
  x = B_w / D (exact Fraction, integer when divisible)
  self-consistency: x integer, and parity word of x under Hp for m steps == w,
                    and Hp^m(x)==x.
We count (i) divisibility passes, (ii) self-consistent among them.
Distinguish D>0 vs D<0, positive-x vs any-integer self-consistency.
"""
import numpy as np
from fractions import Fraction

def Hp(x: int) -> int:
    if x % 2 != 0:
        return (3*x+1)//2
    else:
        return x//2

def Hp_pos(x):
    # for positive ints fast path
    return (3*x+1)//2 if (x & 1) else x//2

def parity_word_Hp(x, m):
    w=[]
    y=x
    for i in range(m):
        wi = 1 if (y % 2 != 0) else 0
        w.append(wi)
        if wi==1:
            # (3y+1)//2 exact even numerator
            y=(3*y+1)//2
        else:
            y//=2
    return w, y

def enumerate_m(m):
    # returns arrays over all words w0=1: B, k, mask
    n = 1 << (m-1)  # number of words; m=1 -> 1 word
    masks = np.arange(n, dtype=np.int64)
    B = np.ones(n, dtype=np.int64)  # after i=0, B1=1 for all (since w0=1)
    # Actually for m=1, done: B=B1? Let's see: word length1, B_1 =1. Yes.
    # For m>1, iterate i=1..m-1
    pow2 = 1
    for i in range(1, m):
        bit = ((masks >> (i-1)) & 1).astype(np.int64)  # w_i
        # B_{i+1} = 3^{w_i} B_i + w_i 2^i
        # mult = 3 if bit else 1
        # Use in-place with int64 (exact: max B ~3^20 fits)
        B = B * (1 + 2*bit) + bit * (1 << i)
        # B*3 where bit=1 else B*1: 1+2*bit gives 1 or 3. exact.
    # k = 1 + popcount(masks restricted to m-1 bits)
    # popcount via bit_count vectorized? use python loop? numpy has bit_count in 2.0?
    try:
        pop = np.bit_count(masks)  # numpy2
    except AttributeError:
        pop = np.array([bin(int(v)).count("1") for v in masks], dtype=np.int64)
    k = 1 + pop
    # For m=1, masks=[0], B=[1]? Check: B1=1 correct. k=1.
    return masks, B, k

def word_from_mask(mask, m):
    w=[1]*m
    w[0]=1
    for i in range(1,m):
        w[i]=(mask >> (i-1)) & 1
    return w

def run_all(max_m=20):
    pow2m = {m: 2**m for m in range(max_m+1)}
    pow3k = {k: 3**k for k in range(max_m+1)}
    total_words=0
    total_div=0
    total_self_pos=0
    total_self_any=0
    rows=[]
    details_div=[]  # list of (m,k,B,D,x,self_any,self_pos,word)
    for m in range(1, max_m+1):
        masks,Barr,karr = enumerate_m(m)
        n=len(masks)
        total_words+=n
        div_pos=0; div_neg=0; div_zeroD=0
        self_pos=0; self_any=0
        # per (m,k) breakdown
        # iterate over indices where D|B
        P2=2**m
        for idx in range(n):
            B=int(Barr[idx]); k=int(karr[idx])
            D=P2-3**k
            assert D!=0, f"D=0 at m={m} k={k} impossible"
            if B % D != 0:
                continue
            x = B//D
            if D>0:
                div_pos+=1
            else:
                div_neg+=1
            total_div+=1
            # self-consistency: compute parity word of x
            # x could be negative or zero? B>0 so x!=0. x could be negative.
            w_true = word_from_mask(int(masks[idx]), m)
            w_x, e_x = parity_word_Hp(x, m)
            is_self = (w_x==w_true and e_x==x)
            if is_self:
                total_self_any+=1
                self_any+=1
                if x>0:
                    total_self_pos+=1
                    self_pos+=1
                    details_div.append((m,k,B,D,x,True,True,w_true))
                else:
                    details_div.append((m,k,B,D,x,True,False,w_true))
            else:
                details_div.append((m,k,B,D,x,False,(x>0),w_true))
        rows.append((m,n,div_pos+div_neg,div_pos,div_neg,self_any,self_pos))
        print(f"m={m:2d} nwords={n:6d} div_total={div_pos+div_neg:4d} (D>0:{div_pos:3d} D<0:{div_neg:3d}) self_any={self_any} self_pos={self_pos}", flush=True)
    print(f"TOTAL words={total_words} div={total_div} self_any={total_self_any} self_pos={total_self_pos}")
    return rows, details_div

if __name__=="__main__":
    rows, det = run_all(20)
    print("\n--- divisibility passes detail ---")
    for (m,k,B,D,x,sa,sp,w) in det:
        print(f"m={m} k={k} B={B} D={D} x={x} self_any={sa} self_pos={sp} w={w}")
    # summary for JSON
    import json
    out={"rows":[{"m":r[0],"nwords":r[1],"div_total":r[2],"div_Dpos":r[3],"div_Dneg":r[4],"self_any":r[5],"self_pos":r[6]} for r in rows],
         "passes":[{"m":m,"k":k,"B":B,"D":D,"x":x,"self_any":sa,"self_pos":sp,"w":w} for (m,k,B,D,x,sa,sp,w) in det]}
    open("/home/mdp/muse-work/cp24-cycle/task1.json","w").write(json.dumps(out,indent=1))
    print("wrote task1.json")
