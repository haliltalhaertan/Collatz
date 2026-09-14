#!/usr/bin/env python3
"""Independent verification of Task1 for m<=10 with pure-Python loops, no numpy."""
from fractions import Fraction

def Hp(x):
    return (3*x+1)//2 if x%2!=0 else x//2

def B_of_word(w):
    B=0
    for i,wi in enumerate(w):
        B=(3**wi)*B+wi*(2**i)
    return B

def orbit_word(x,m):
    w=[]
    y=x
    for i in range(m):
        wi=1 if y%2!=0 else 0
        w.append(wi)
        y=Hp(y)
    return w,y

for m in range(1,9):
    n=1<<(m-1)
    div=0
    self_any=0
    for mask in range(n):
        w=[1]*m
        for i in range(1,m):
            w[i]=(mask>>(i-1))&1
        k=sum(w)
        B=B_of_word(w)
        D=2**m-3**k
        assert D!=0
        if B%D==0:
            div+=1
            x=B//D
            wx,ex=orbit_word(x,m)
            if wx==w and ex==x:
                self_any+=1
            else:
                print(f"NON-SELF m={m} w={w} B={B} D={D} x={x} wx={wx} ex={ex}")
    print(f"m={m} n={n} div={div} self={self_any} match={div==self_any}")
