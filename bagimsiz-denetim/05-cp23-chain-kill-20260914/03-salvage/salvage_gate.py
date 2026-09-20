"""Salvage-session verification: gate + assets A1-A4, A6, collision-count corollary.

From-scratch exact arithmetic (fractions.Fraction / int only).
Run: python3 salvage_gate.py
"""
from fractions import Fraction
from math import comb, ceil, log2
from collections import defaultdict


def H(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2


def Ecal(m, r):
    P = defaultdict(lambda: defaultdict(int))
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = H(x)
        P[k][x % (1 << r)] += 1
    tot = Fraction(0)
    for k, d in P.items():
        Jr = (1 << (r - 1)) * sum(
            (d.get(u, 0) - d.get(u + (1 << (r - 1)), 0)) ** 2
            for u in range(1 << (r - 1))
        )
        tot += Fraction(Jr, comb(m - 1, k - 1))
    return tot


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def words(m):
    out = {}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = H(x)
        out[h] = (k, (1 << m) * x - (3 ** k) * h, x)
    return out


def main():
    # GATE
    g1, g2 = Ecal(4, 3), Ecal(5, 2)
    print("CHECK 1 Ecal(4,3) =", g1, "->", "PASS" if g1 == Fraction(40, 3) else "FAIL")
    print("CHECK 2 Ecal(5,2) =", g2, "->", "PASS" if g2 == Fraction(31, 3) else "FAIL")
    assert g1 == Fraction(40, 3) and g2 == Fraction(31, 3)

    # A1: affine form + B odd (m <= 8)
    for m in range(1, 9):
        for h, (k, B, e) in words(m).items():
            assert e * (1 << m) == (3 ** k) * h + B and B & 1
    print("A1 affine form + B odd (m<=8): PASS")

    # A2: 2-adic isometry, same-weight pairs (m <= 7)
    n = 0
    for m in range(1, 8):
        W = words(m)
        hs = list(W)
        for i in range(len(hs)):
            for j in range(i + 1, len(hs)):
                k1, B1, _ = W[hs[i]]
                k2, B2, _ = W[hs[j]]
                if k1 == k2:
                    assert v2(B1 - B2) == v2(hs[i] - hs[j]), (m, hs[i], hs[j])
                    n += 1
    print(f"A2 isometry ({n} pairs, m<=7): PASS")

    # A3 strong (exact collision <=> B congruence) + corollary counts (m <= 12 spot)
    for m in [8, 10, 12]:
        W = words(m)
        groups = defaultdict(list)
        for h, (k, B, e) in W.items():
            groups[k].append((h, B, e))
        for k, L in groups.items():
            seen = {}
            for h, B, e in L:
                r = B % (3 ** k)
                for (h2, e2) in seen.get(r, []):
                    assert e == e2, ("A3 converse FAIL", m, k, h, h2)
                seen.setdefault(r, []).append((h, e))
            E = len(set(e for _, _, e in L))
            R = len(seen)
            assert E == R, ("count corollary FAIL", m, k)
            assert R <= 2 * 3 ** (k - 1), ("reachability FAIL", m, k)
    print("A3 exact-collision criterion + count corollary (m=8,10,12): PASS")

    # A4: B never 0 mod 3 (m <= 10)
    tot = 0
    for m in range(1, 11):
        for h, (k, B, e) in words(m).items():
            assert B % 3 != 0, (m, h)
            tot += 1
    print(f"A4 B never 0 mod 3 ({tot} words): PASS")

    # A6: cap stabilisation at 2^r >= 3^k - 1
    for (m, k) in [(6, 2), (7, 3), (8, 4), (9, 4), (10, 5)]:
        thresh = 3 ** k - 1
        r0 = ceil(log2(thresh))

        def mx(r):
            d = defaultdict(int)
            for h, (kk, B, e) in words(m).items():
                if kk == k:
                    d[e % (1 << r)] += 1
            return max(d.values())

        caps = [mx(r) for r in range(r0, r0 + 3)]
        assert caps[0] == caps[1] == caps[2], (m, k, caps)
        print(f"A6 stabilised max (m={m},k={k},thresh={thresh}): {caps[0]} PASS")


if __name__ == "__main__":
    main()
    print("ALL CHECKS PASS")
