"""
Collatz prefix-source histogram: core exact-arithmetic engine, built from
the DEFINITION only (no reuse of any archive engine).

Shortcut map:  H(x) = (3x+1)//2 if x odd else x//2.
Words:         W_{m,k} = { w in {0,1}^m : w_0 = 1, |w| = k }.
Affine form:   H^m(x) = (3^k x + B_w)/2^m   for x in the residue class of w.
B recursion:   B_0 = 0,  B_{i+1} = 3^{w_i} B_i + w_i 2^i.

ALL INTEGER ARITHMETIC.  No floats anywhere in returned values.
"""
from itertools import combinations
from functools import lru_cache


# ---------------------------------------------------------------- base map
def H(x):
    return (3 * x + 1) // 2 if x & 1 else x // 2


def parity_word(h, m):
    """Parity word of the first m iterates of h (w_i = parity of H^i(h))."""
    w = []
    x = h
    for _ in range(m):
        w.append(x & 1)
        x = H(x)
    return tuple(w)


# ---------------------------------------------------------------- words
def words(m, k):
    """All w in {0,1}^m with w_0 = 1 and weight k, as tuples."""
    if k < 1 or k > m:
        return
    for rest in combinations(range(1, m), k - 1):
        w = [0] * m
        w[0] = 1
        for i in rest:
            w[i] = 1
        yield tuple(w)


def positions(w):
    return tuple(i for i, b in enumerate(w) if b)


# ---------------------------------------------------------------- B, h, e
def B_of(w):
    """Forward recursion B_{i+1} = 3^{w_i} B_i + w_i 2^i."""
    B = 0
    for i, b in enumerate(w):
        if b:
            B = 3 * B + (1 << i)
        # b == 0  =>  B unchanged
    return B


def B_closed(w):
    """Closed form  B_w = sum_j 3^{k-j} 2^{i_j},  i_1<...<i_k the 1-positions."""
    S = positions(w)
    k = len(S)
    return sum(pow(3, k - j) * (1 << S[j - 1]) for j in range(1, k + 1))


def h_of(w):
    """The unique odd h in (0, 2^m) whose length-m parity word is w."""
    m = len(w)
    k = sum(w)
    B = B_of(w)
    return (-B * pow(pow(3, k), -1, 1 << m)) % (1 << m)


def e_of(w):
    """e_w = H^m(h_w) = (3^k h_w + B_w)/2^m."""
    m = len(w)
    k = sum(w)
    B = B_of(w)
    h = h_of(w)
    num = pow(3, k) * h + B
    assert num % (1 << m) == 0, "affine identity broken"
    return num >> m


def v2(n):
    if n == 0:
        return None  # infinity
    n = abs(n)
    return (n & -n).bit_length() - 1


def v3(n):
    if n == 0:
        return None
    n = abs(n)
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


# ---------------------------------------------------------------- bulk data
@lru_cache(maxsize=None)
def layer(m, k):
    """[(w, B_w, h_w, e_w)] for all w in W_{m,k}."""
    out = []
    for w in words(m, k):
        B = B_of(w)
        h = h_of(w)
        e = (pow(3, k) * h + B) >> m
        out.append((w, B, h, e))
    return out


def histogram(m, k, r):
    """P_{m,k,r} as dict z -> count."""
    mod = 1 << r
    hist = {}
    for (_w, _B, _h, e) in layer(m, k):
        z = e % mod
        hist[z] = hist.get(z, 0) + 1
    return hist


def cap(m, k, r):
    h = histogram(m, k, r)
    return max(h.values()) if h else 0
