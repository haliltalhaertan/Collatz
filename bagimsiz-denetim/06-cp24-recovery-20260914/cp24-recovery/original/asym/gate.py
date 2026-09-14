#!/usr/bin/env python3
"""Grounding gate: affine identity, Ecal values, Hm cycle. Exact arithmetic only."""
from fractions import Fraction
from math import comb

def Hp(x):
    return (3*x+1)//2 if (x & 1) else x//2

def Hm(x):
    return (3*x-1)//2 if (x & 1) else x//2

# (a) affine identity on every odd h < 2^8, m=8
m = 8
fails = 0
for h in range(1, 2**m, 2):
    x = h
    k = 0
    for _ in range(m):
        if x & 1:
            k += 1
        x = Hp(x)
    e = x
    B = (2**m)*e - (3**k)*h
    if (2**m)*e != (3**k)*h + B:
        fails += 1
        print(f"MISMATCH identity h={h}")
    if B % 2 == 0:
        fails += 1
        print(f"MISMATCH B even h={h} k={k} e={e} B={B}")
    if B % 3 == 0:
        fails += 1
        print(f"MISMATCH B 0 mod3 h={h} k={k} e={e} B={B}")
print(f"(a) affine identity odd h<2^8: checked 128, failures={fails}")

# (b) Ecal
def Ecal(H, m, r):
    # P_k(z): dict k -> list length 2^r
    from collections import defaultdict
    P = {}
    for h in range(1, 2**m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = H(x)
        e = x
        z = e % (2**r)
        P.setdefault(k, [0]*(2**r))
        P[k][z] += 1
    total = Fraction(0)
    for k, X in P.items():
        n_k = comb(m-1, k-1)
        J = Fraction(0)
        for u in range(2**(r-1)):
            d = X[u] - X[u + 2**(r-1)]
            J += d*d
        J *= 2**(r-1)
        total += J / n_k
    return total

e43 = Ecal(Hp, 4, 3)
e52 = Ecal(Hp, 5, 2)
print(f"(b) Ecal(4,3) = {e43} (expect 40/3), ok={e43 == Fraction(40,3)}")
print(f"(b) Ecal(5,2) = {e52} (expect 31/3), ok={e52 == Fraction(31,3)}")

# (c) Hm cycle 5->7->10->5
seq = [5, Hm(5), Hm(Hm(5))]
print(f"(c) Hm trajectory from 5: {seq}, closes={Hm(seq[2])==5} (Hm(10)={Hm(10)})")
ok = (fails == 0) and (e43 == Fraction(40,3)) and (e52 == Fraction(31,3)) and (seq == [5,7,10] and Hm(10)==5)
print("GATE_OK" if ok else "GATE_FAIL")
