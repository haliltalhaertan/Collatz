from fractions import Fraction
from math import comb

def H(x):
    return (3*x+1)//2 if (x & 1) else x//2

def Ecal(m, r):
    mod = 1 << r
    half = 1 << (r-1)
    # P[k][z]
    P = {}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = H(x)
        z = x % mod
        P.setdefault(k, [0]*mod)
        P[k][z] += 1
    total = Fraction(0, 1)
    for k, arr in sorted(P.items()):
        n_k = comb(m-1, k-1)
        s = 0
        for u in range(half):
            d = arr[u] - arr[u+half]
            s += d*d
        J = (half * s)  # 2^(r-1) * sum
        total += Fraction(J, n_k)
    return total

for (m, r, exp) in [(4,3,Fraction(40,3)), (5,2,Fraction(31,3))]:
    got = Ecal(m, r)
    print(f"Ecal({m},{r}) = {got}  expected {exp}  match={got==exp}")
