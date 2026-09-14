"""Gate: from-scratch exact reproduction of Ecal checks.

[EXACT COMPUTATION] Everything in this file is exact integer / Fraction arithmetic.
Definitions (from task text):
  H(x) = (3x+1)//2 if x odd else x//2
  For odd h < 2^m run m steps; k = number of odd steps (visits).
  P_{m,k,r}(z) = #{odd h < 2^m : odd-count k, H^m(h) = z mod 2^r}
  n_k = binom(m-1,k-1)
  J_r(X) = 2^(r-1) * sum_{u < 2^(r-1)} (X(u) - X(u+2^(r-1)))^2
  Ecal(m,r) = sum_k J_r(P_{m,k,r}) / n_k
Checks: Ecal(4,3) == 40/3 and Ecal(5,2) == 31/3.
"""
from fractions import Fraction
from math import comb


def H(x: int) -> int:
    return (3 * x + 1) // 2 if (x & 1) else x // 2


def census(m: int, r: int):
    """Return {k: [counts over z mod 2^r]}. Exact integer table."""
    N = 1 << r
    counts = {k: [0] * N for k in range(1, m + 1)}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = H(x)
        counts[k][x % N] += 1
    return counts


def Ecal(m: int, r: int) -> Fraction:
    counts = census(m, r)
    half = 1 << (r - 1)
    total = Fraction(0)
    for k in range(1, m + 1):
        nk = comb(m - 1, k - 1)
        X = counts[k]
        s = sum((X[u] - X[u + half]) ** 2 for u in range(half))
        Jr = (1 << (r - 1)) * s
        total += Fraction(Jr, nk)
    return total


if __name__ == "__main__":
    e1 = Ecal(4, 3)
    e2 = Ecal(5, 2)
    print(f"Ecal(4,3) = {e1}")
    print(f"Ecal(5,2) = {e2}")
    assert e1 == Fraction(40, 3), f"CHECK 1 mismatch: {e1}"
    assert e2 == Fraction(31, 3), f"CHECK 2 mismatch: {e2}"
    print("gate_ok = True")
