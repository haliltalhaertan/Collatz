"""Grounding gate: shortcut Collatz census energy Ecal(m,r) from scratch.

Shortcut map H(x) = (3x+1)//2 if x odd else x//2.
For odd h < 2^m run m steps; k = number of odd steps.
P_{m,k,r}(z) = #{odd h < 2^m : odd-count k, H^m(h) = z mod 2^r}
n_k = binom(m-1,k-1)
J_r(X) = 2^(r-1) sum_{u<2^(r-1)} (X(u)-X(u+2^(r-1)))^2
Ecal(m,r) = sum_k J_r(P_{m,k,r})/n_k

CHECK 1: Ecal(4,3) = 40/3.  CHECK 2: Ecal(5,2) = 31/3.
Exact arithmetic via fractions.Fraction.
"""
from fractions import Fraction
from math import comb


def H(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2


def Ecal(m, r):
    counts = {k: [0] * (2 ** r) for k in range(1, m + 1)}
    for h in range(1, 2 ** m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = H(x)
        counts[k][x % (2 ** r)] += 1
    total = Fraction(0)
    for k in range(1, m + 1):
        n_k = comb(m - 1, k - 1)
        X = counts[k]
        half = 2 ** (r - 1)
        s = sum((X[u] - X[u + half]) ** 2 for u in range(half))
        total += Fraction((2 ** (r - 1)) * s, n_k)
    return total


if __name__ == "__main__":
    v1 = Ecal(4, 3)
    v2 = Ecal(5, 2)
    print("Ecal(4,3) =", v1)
    print("Ecal(5,2) =", v2)
    assert v1 == Fraction(40, 3), v1
    assert v2 == Fraction(31, 3), v2
    print("GATE OK: both checks match.")
