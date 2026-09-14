"""Cycles analysis: A1 affine form + B_w formula, A3 collision criterion,
cycle equation x = B_w/(2^m - 3^k), word-enumeration cycle scan,
and independence of D-divisibility from A3 class. Exact integer arithmetic.
"""
import numpy as np
from collections import defaultdict
import statistics


def H(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2


def word_B_endpoint(h, m):
    x = h
    w = []
    for _ in range(m):
        w.append(x & 1)
        x = H(x)
    k = sum(w)
    suf = 0
    B = 0
    for j in range(m - 1, -1, -1):
        if w[j]:
            B += (3 ** suf) * (2 ** j)
            suf += 1
    return w, k, x, B


def B_table(m):
    """B_w for all 2^{m-1} words with w_0 = 1. Returns (K, B)."""
    n = 2 ** (m - 1)
    words = np.arange(n, dtype=np.int64)
    K = 1 + np.array([bin(v).count("1") for v in range(n)], dtype=np.int64)
    B = np.zeros(n, dtype=object)
    B[:] = 0
    for j in range(1, m):
        bit = ((words >> (j - 1)) & 1).astype(object)
        higher = words >> j
        suf = np.array([bin(int(v)).count("1") for v in higher], dtype=object)
        B = B + bit * (3 ** suf) * (2 ** j)
    B = B + (3 ** (K.astype(object) - 1))
    return K, np.array([int(b) for b in B], dtype=object)


if __name__ == "__main__":
    # A1 + B odd + B % 3 != 0, m <= 8
    for m in range(1, 9):
        for h in range(1, 2 ** m, 2):
            w, k, e, B = word_B_endpoint(h, m)
            assert e == (3 ** k * h + B) // (2 ** m)
            assert (3 ** k * h + B) % (2 ** m) == 0
            assert B % 2 == 1 and B % 3 != 0
    print("A1 + B odd + B%3!=0, m<=8: OK")

    # A3: same endpoint <=> same B mod 3^k within stratum, m <= 8
    for m in range(1, 9):
        byk = {}
        for h in range(1, 2 ** m, 2):
            w, k, e, B = word_B_endpoint(h, m)
            byk.setdefault(k, []).append((e, B))
        for k, lst in byk.items():
            mod = 3 ** k
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    assert (lst[i][0] == lst[j][0]) == (
                        (lst[i][1] - lst[j][1]) % mod == 0
                    )
    print("A3 collision criterion, m<=8: OK")

    # Cycle scan m <= 12 (+ spot m in {14,...,20}): only trivial-cycle repetitions
    def scan(m, full_verify=True):
        K, B = B_table(m)
        sols = []
        divs = 0
        for idx in range(len(K)):
            kk, bb = int(K[idx]), int(B[idx])
            D = 2 ** m - 3 ** kk
            if D > 0 and bb % D == 0:
                divs += 1
                x = bb // D
                xx = x
                okw = True
                for j in range(m):
                    want = 1 if j == 0 else int((idx >> (j - 1)) & 1)
                    if (xx & 1) != want:
                        okw = False
                        break
                    xx = H(xx)
                if okw and xx == x:
                    sols.append(x)
        return divs, sols

    for m in range(1, 13):
        divs, sols = scan(m)
        assert set(sols) <= {1}, (m, sols)
        print(f"m={m}: D-divisible words={divs} cycles={sorted(set(sols))}")
    for m in [14, 16, 18, 20]:
        divs, sols = scan(m)
        assert set(sols) <= {1}, (m, sols)
        print(f"m={m}: D-divisible words={divs} nontrivial={set(sols)-{1}}")

    # Independence: D-divisibility rate overall vs conditional on A3 class
    for (m, k) in [(4, 2), (5, 3), (7, 4), (8, 5), (10, 6), (13, 8)]:
        K, B = B_table(m)
        D = 2 ** m - 3 ** k
        mod = 3 ** k
        sel = [i for i in range(len(K)) if int(K[i]) == k]
        cls = defaultdict(list)
        for i in sel:
            cls[int(B[i]) % mod].append(i)
        cond = [
            sum(1 for i in mem if int(B[i]) % D == 0) / len(mem)
            for mem in cls.values()
        ]
        base = sum(1 for i in sel if int(B[i]) % D == 0) / len(sel)
        print(
            f"(m,k)={(m, k)}: D={D} n={len(sel)} base={base:.5f} "
            f"1/D={1 / D:.5f} cond_mean={statistics.mean(cond):.5f} "
            f"cond_max={max(cond):.5f}"
        )
    print("CYCLES OK")
