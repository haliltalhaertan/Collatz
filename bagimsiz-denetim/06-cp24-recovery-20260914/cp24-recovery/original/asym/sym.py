#!/usr/bin/env python3
"""Symmetry analysis: pairing identities + Ecal invariance (exact ints/Fractions).
Maps: Hp=(3x+1)/2, Hm=(3x-1)/2, G5=(5x+1)/2 on odd; x/2 on even.
"""
from fractions import Fraction
from math import comb

def Hp(x): return (3*x+1)//2 if (x & 1) else x//2
def Hm(x): return (3*x-1)//2 if (x & 1) else x//2
def G5(x): return (5*x+1)//2 if (x & 1) else x//2

def traj(H, h, m):
    x = h; w = []; k = 0
    for _ in range(m):
        b = x & 1
        w.append(b)
        k += b
        x = H(x)
    return tuple(w), k, x

def B_of(H, h, m, a):
    # affine coefficient with odd-step constant a (+1 / -1): 2^m e = c^k h + B, c=3 or 5
    w, k, e = traj(H, h, m)
    c = 3 if H is not G5 else 5
    return (2**m)*e - (c**k)*h, w, k, e

print("== S1: pointwise negation identity Hm(-x) == -Hp(x), x in [-50,50] ==")
ok = all(Hm(-x) == -Hp(x) for x in range(-50, 51))
print("S1 pass:", ok, "(proof is by cases in report; this is a finite check)")

print("== S2: word pairing k^-(2^m-h)==k^+(h), B negation, endpoint sum == 3^k ==")
for m in (4, 6, 8, 10):
    n = 0; fail = 0
    for h in range(1, 2**m, 2):
        hs = 2**m - h
        wp, kp, ep = traj(Hp, h, m)
        wm, km, em = traj(Hm, hs, m)
        Bp = (2**m)*ep - (3**kp)*h
        Bm = (2**m)*em - (3**km)*hs
        n += 1
        if not (wm == wp and km == kp and Bm == -Bp and em + ep == 3**kp):
            fail += 1
            if fail < 3:
                print(f"  m={m} h={h} FAIL wp={wp} wm={wm} kp={kp} km={km} ep={ep} em={em} Bp={Bp} Bm={Bm}")
    print(f"  m={m}: {n-fail}/{n} paired, failures={fail}")

print("== S3: |B| multiset identity vs literal B multiset identity, m=8 ==")
m = 8
Bp_list = sorted(B_of(Hp, h, m, 1)[0] for h in range(1, 2**m, 2))
Bm_list = sorted(B_of(Hm, h, m, 1)[0] for h in range(1, 2**m, 2))
print("  literal sorted B multisets equal:", Bp_list == Bm_list)
print("  |B| sorted multisets equal:", sorted(abs(b) for b in Bp_list) == sorted(abs(b) for b in Bm_list))
print("  negated multisets equal ({-b}=={b'}):", sorted(-b for b in Bp_list) == Bm_list)
print("  Hp B range:", Bp_list[0], "..", Bp_list[-1], " all>0:", all(b > 0 for b in Bp_list))
print("  Hm B range:", Bm_list[0], "..", Bm_list[-1], " all<0:", all(b < 0 for b in Bm_list))
print("  Hp endpoints multiset == Hm endpoints multiset:",
      sorted(traj(Hp, h, m)[2] for h in range(1, 2**m, 2)) == sorted(traj(Hm, h, m)[2] for h in range(1, 2**m, 2)))

def Ecal(H, m, r):
    P = {}
    for h in range(1, 2**m, 2):
        _, k, e = traj(H, h, m)
        P.setdefault(k, [0]*(2**r))
        P[k][e % (2**r)] += 1
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

print("== S4: Ecal equality Hp vs Hm, and G5 comparison (exact Fractions) ==")
for (m, r) in [(2,2),(3,2),(4,2),(4,3),(5,2),(5,3),(6,2),(6,3)]:
    a, b, c = Ecal(Hp,m,r), Ecal(Hm,m,r), Ecal(G5,m,r)
    print(f"  Ecal({m},{r}): Hp={a} Hm={b} equal={a==b} | G5={c}")
