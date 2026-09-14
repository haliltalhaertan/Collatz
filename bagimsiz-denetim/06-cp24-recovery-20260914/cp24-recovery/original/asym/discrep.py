#!/usr/bin/env python3
"""Assignment-discrepancy between Hp=(3x+1)/2 and Hm=(3x-1)/2, m=4..14. Exact ints."""
def Hp(x): return (3*x+1)//2 if (x & 1) else x//2
def Hm(x): return (3*x-1)//2 if (x & 1) else x//2

def weight(H, h, m):
    x = h; k = 0
    for _ in range(m):
        k += x & 1
        x = H(x)
    return k

print("m | n_odd | disagree #{h:k+!=k-} | frac disagree | L1=sum|dk| | mean|dk| (exact) | max|dk| | pairing #{h:k-(2^m-h)==k+(h)}")
for m in range(4, 15):
    N = 2**(m-1)
    disag = 0; L1 = 0; mx = 0; pair_ok = 0
    for h in range(1, 2**m, 2):
        kp = weight(Hp, h, m); km = weight(Hm, h, m)
        d = abs(kp - km)
        disag += (d != 0); L1 += d; mx = max(mx, d)
        if weight(Hm, 2**m - h, m) == kp:
            pair_ok += 1
    from fractions import Fraction
    print(f"{m:2d} | {N:4d} | {disag:4d} | {Fraction(disag, N)} ~= {disag/N:.4f} | {L1} | {Fraction(L1, N)} ~= {L1/N:.4f} | {mx} | {pair_ok}/{N}")

# same-h detail at m=8: distribution of (k+, k-) and example h=1
print("== m=8 joint (k+,k-) counts ==")
m = 8
from collections import Counter
C = Counter()
for h in range(1, 2**m, 2):
    C[(weight(Hp, h, m), weight(Hm, h, m))] += 1
for kk in sorted(C):
    print(f"  k+={kk[0]} k-={kk[1]}: {C[kk]}")
print("  h=1:", "k+ =", weight(Hp, 1, m), " k- =", weight(Hm, 1, m))
