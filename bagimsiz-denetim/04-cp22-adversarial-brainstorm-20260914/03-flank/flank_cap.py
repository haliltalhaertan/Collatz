"""FLANK cap analysis -- B_w mod 3^k distribution + provable bounds -- from scratch.

[EXACT COMPUTATION] All counts/integers/Fractions exact. Floats only for
display of uniformity diagnostics, never as claimed bounds.
"""
from itertools import combinations
from fractions import Fraction
from math import comb
import sys
sys.set_int_max_str_digits(1000000)


def words_mk(m, k):
    if k < 1 or k > m:
        return
    for rest in combinations(range(1, m), k - 1):
        w = [0] * m
        w[0] = 1
        for i in rest:
            w[i] = 1
        yield tuple(w)


def B_of_word(w):
    B = 0
    for i, b in enumerate(w):
        if b:
            B = 3 * B + (1 << i)
    return B


def h_of_word(w):
    m = len(w)
    k = sum(w)
    B = B_of_word(w)
    return (-B * pow(pow(3, k), -1, 1 << m)) % (1 << m)


def e_of_word(w):
    m = len(w)
    k = sum(w)
    B = B_of_word(w)
    h = h_of_word(w)
    num = pow(3, k) * h + B
    assert num % (1 << m) == 0
    return num >> m


def Bmod_dist(m, k):
    """Return dict residue->count for B_w mod 3^k over W_{m,k}. Exact."""
    mod = pow(3, k)
    hist = {}
    for w in words_mk(m, k):
        r = B_of_word(w) % mod
        hist[r] = hist.get(r, 0) + 1
    return hist


def T4_bound(m, k):
    # floor(2^(m-k)(3^(k-1)-2^(k-1))/3^k)+1
    num = (1 << (m - k)) * (pow(3, k - 1) - (1 << (k - 1)))
    return num // pow(3, k) + 1


def T6_bound(m, k, r, memo):
    """Recursive cap bound via T6: cap(m,k,r)<=2cap(m-1,k,r+1)+2cap(m-1,k-1,r+1).
    Base: cap<=n_k trivially; cap(m,1,r)=cap(m,m,r)=1 (single/forced word)."""
    key = (m, k, r)
    if key in memo:
        return memo[key]
    if k < 1 or k > m:
        memo[key] = 0
        return 0
    nk = comb(m - 1, k - 1)
    if k == 1 or k == m:
        memo[key] = 1
        return 1
    # stabilised base: if 2^r >= 3^k-1 use T4 (r-independent ceiling)
    if (1 << r) >= pow(3, k) - 1:
        memo[key] = min(nk, T4_bound(m, k))
        return memo[key]
    if r > 30 or m <= 2:
        memo[key] = nk
        return nk
    v = 2 * T6_bound(m - 1, k, r + 1, memo) + 2 * T6_bound(m - 1, k - 1, r + 1, memo)
    v = min(v, nk, T4_bound(m, k))
    memo[key] = v
    return v


if __name__ == "__main__":
    import json
    Mt = json.load(open("ref/M_table.json"))
    print("== T2/T7 spot checks (exact) ==")
    # T2: 1<=e<=3^k-1 on samples
    for (m, k) in [(7, 3), (10, 4), (13, 6)]:
        es = [e_of_word(w) for w in words_mk(m, k)]
        print(f"  (m={m},k={k}) e range [{min(es)},{max(es)}] vs [1,{pow(3,k)-1}] ok={1<=min(es) and max(es)<=pow(3,k)-1}")
    # T7: e==e' <=> B==B' mod 3^k on full small layer
    for (m, k) in [(7, 3), (8, 3)]:
        Ws = list(words_mk(m, k))
        Bs = [B_of_word(w) % pow(3, k) for w in Ws]
        Es = [e_of_word(w) for w in Ws]
        bad = 0
        for i in range(len(Ws)):
            for j in range(i + 1, len(Ws)):
                if (Es[i] == Es[j]) != (Bs[i] == Bs[j]):
                    bad += 1
        print(f"  T7 (m={m},k={k}) violations={bad} (0 means iff holds)")

    print("== B_w mod 3^k distributions (exact) ==")
    for (m, k) in [(10, 4), (12, 4), (13, 4), (15, 5), (18, 6), (20, 6)]:
        nk = comb(m - 1, k - 1)
        Ncls = pow(3, k)
        hist = Bmod_dist(m, k)
        occ = len(hist)
        mx = max(hist.values())
        trueM = Mt.get(f"{m},{k}", None)
        # uniform expectation
        mean = Fraction(nk, Ncls)
        # birthday: expected #colliding pairs under uniform = C(n,2)/N
        exp_pairs = Fraction(nk * (nk - 1) // 2, Ncls) if Ncls else None
        obs_pairs = sum(c * (c - 1) // 2 for c in hist.values())
        print(f"  (m={m},k={k}) n={nk} classes={Ncls} occ={occ} "
              f"maxpile={mx} trueM={trueM} mean={mean} expPairs={exp_pairs} obsPairs={obs_pairs}")
        # top piles
        top = sorted(hist.values(), reverse=True)[:6]
        print(f"     top piles={top}")
        # chi-square distance from uniform (display float only)
        # chi2 = sum (c-mean)^2/mean over occupied + unoccupied zeros
        # compute exactly as Fraction
        chi2 = sum((Fraction(c) - mean) ** 2 for c in hist.values()) / mean if mean else None
        chi2 += (Ncls - occ) * mean  # zero-class contribution: (0-mean)^2/mean * count = mean*count
        print(f"     chi2={float(chi2):.3f} (display) chi2/dof={float(chi2/Ncls):.3f}")

    print("== T4 tightness vs true M (exact ratios) ==")
    for (m, k) in [(10, 4), (12, 5), (13, 4), (15, 5), (18, 6), (20, 6), (20, 5), (14, 4)]:
        t4 = T4_bound(m, k)
        trueM = Mt.get(f"{m},{k}")
        print(f"  (m={m},k={k}) T4={t4} true={trueM} ratio={Fraction(t4,trueM)} ~{t4/trueM:.2f}")

    print("== T6-combined bound tightness ==")
    memo = {}
    for (m, k, r) in [(10, 4, 2), (12, 5, 2), (13, 4, 4), (8, 4, 2), (7, 3, 2)]:
        b = T6_bound(m, k, r, memo)
        print(f"  cap({m},{k},{r}) T6-combined<={b}")
