"""Analogue kill: 3n+1 vs 3n-1 Ecal identity, explicit analogue cycles,
5n+1 monotonicity coexisting with a proven cycle. Exact arithmetic.
"""
from fractions import Fraction
from math import comb


def make_H(a, b):
    def H(x):
        return (a * x + b) // 2 if (x & 1) else x // 2
    return H


Hp, Hm, H5 = make_H(3, 1), make_H(3, -1), make_H(5, 1)


def Ecal_per_k(m, r, H):
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
    per_k = {}
    for k in range(1, m + 1):
        n_k = comb(m - 1, k - 1)
        X = counts[k]
        half = 2 ** (r - 1)
        s = sum((X[u] - X[u + half]) ** 2 for u in range(half))
        per_k[k] = (2 ** (r - 1)) * s
        total += Fraction(per_k[k], n_k)
    return total, per_k


if __name__ == "__main__":
    # pointwise negation identity
    for x in list(range(-50, 51)) + [10 ** 18 + 3, 10 ** 18 + 4]:
        assert Hp(-x) == -Hm(x), x
    print("Hp(-x) = -Hm(x): OK")

    # 3n-1 affine form with the SAME B_w
    for m in range(1, 9):
        for h in range(1, 2 ** m, 2):
            x = h
            w = []
            for _ in range(m):
                w.append(x & 1)
                x = Hm(x)
            k = sum(w)
            suf, B = 0, 0
            for j in range(m - 1, -1, -1):
                if w[j]:
                    B += (3 ** suf) * (2 ** j)
                    suf += 1
            assert x == (3 ** k * h - B) // (2 ** m)
            assert (3 ** k * h - B) % (2 ** m) == 0
    print("3n-1 same-B affine form, m<=8: OK")

    # explicit analogue cycles
    t = [1]
    for _ in range(5):
        t.append(H5(t[-1]))
    assert t == [1, 3, 8, 4, 2, 1], t
    assert Hm(1) == 1
    t = [5]
    for _ in range(3):
        t.append(Hm(t[-1]))
    assert t == [5, 7, 10, 5], t
    print("analogue cycles (5n+1 5-cycle, 3n-1 fixed point + 3-cycle): OK")

    # Ecal identity, total and per-stratum
    ntest = 0
    for m in range(2, 11):
        for r in range(1, 6):
            a, pa = Ecal_per_k(m, r, Hp)
            b, pb = Ecal_per_k(m, r, Hm)
            assert a == b and pa == pb, (m, r)
            ntest += 1
    print(f"Ecal(3n+1)==Ecal(3n-1) total+per-stratum on {ntest} pairs: OK")

    # 5n+1 mixing rows despite proven cycle
    v = 0
    for m in range(2, 12):
        for s in range(1, 5):
            assert Ecal_per_k(m, s + 1, H5)[0] >= Ecal_per_k(m + 1, s, H5)[0]
            v += 1
    print(f"5n+1 monotonicity on {v} rows despite 5-cycle: OK")
    print("ANALOGUES OK")
