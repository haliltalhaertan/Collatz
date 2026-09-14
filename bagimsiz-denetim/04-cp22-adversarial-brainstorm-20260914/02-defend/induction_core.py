"""
Core exact-arithmetic machinery for the Collatz prefix source, radius-2 charging,
and the PARENT IDENTITY.  Integers / fractions.Fraction only -- no floating point.

Conventions (taken verbatim from the task setup, validated against ADVERSARY 1):

  H(x) = (3x+1)//2 if x odd else x//2
  P_{m,k,r}[z] = #{ h odd, h < 2^m, #odd-steps in H^0..H^{m-1}(h) == k, H^m(h) == z mod 2^r }
  n_k = C(m-1,k-1)
  J_r(X) = 2^(r-1) * sum_{u < 2^(r-1)} (X[u] - X[u+2^(r-1)])^2      (X has length 2^r)

  At N = 2^(s+1), q = 2^s, c_k = 3^k mod N, rinv = 3^{-1} mod N, P_k = P_{m,k,s+1}:
     E_k[z] = P_k[(2z) % N]              + P_k[(2z - c_k) % N]            z < q
     O_k[z] = P_k[(rinv*(2z-1)) % N]     + P_k[(rinv*(2z-1) - c_k) % N]   z < q

     C_k(d) = sum_u P_k[u] P_k[(u+d) % N]
     L_k    = q * ( C_k(3^k) - C_k(3^k + q) ) / n_k
     M_j    = J_s( n_{j-1} E_j - n_j O_{j-1} ) / ( n_j n_{j-1} (n_j + n_{j-1}) ),  j = 2..m
     M_1 = M_{m+1} = 0
"""
from fractions import Fraction
from math import comb
from functools import lru_cache


# ----------------------------------------------------------------- the source
def H(x):
    return (3 * x + 1) // 2 if x & 1 else x // 2


@lru_cache(maxsize=None)
def source(m, r):
    """Return tuple of tuples: P[k] for k=0..m (P[0] is the all-zero array).
    Each P[k] has length 2^r and total mass C(m-1,k-1)."""
    R = 1 << r
    P = [[0] * R for _ in range(m + 2)]
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = H(x)
        P[k][x % R] += 1
    return tuple(tuple(row) for row in P)


def masses(m):
    return [0] + [comb(m - 1, k - 1) for k in range(1, m + 1)]


# ------------------------------------------------------------------ operators
def E_op(P, s, c):
    """E at modulus N=2^(s+1): array of length 2^(s+1) -> array of length 2^s.
    Gauge exponent supplied as c = 3^k (reduced mod N inside)."""
    N = 1 << (s + 1)
    q = 1 << s
    c %= N
    return [P[(2 * z) % N] + P[(2 * z - c) % N] for z in range(q)]


def O_op(P, s, c):
    N = 1 << (s + 1)
    q = 1 << s
    c %= N
    rinv = pow(3, -1, N)
    return [P[(rinv * (2 * z - 1)) % N] + P[(rinv * (2 * z - 1) - c) % N]
            for z in range(q)]


def J(X, r):
    """J_r on an array of length 2^r."""
    half = 1 << (r - 1)
    assert len(X) == (1 << r), (len(X), r)
    return (1 << (r - 1)) * sum((X[u] - X[u + half]) ** 2 for u in range(half))


def autocorr(P, d, N):
    return sum(P[u] * P[(u + d) % N] for u in range(N))


# --------------------------------------------------------- per-stratum L and M
def L_terms(P_list, m, s):
    """L_k for k=1..m.  P_list[k] must be P_{m,k,s+1} (length 2^(s+1))."""
    N = 1 << (s + 1)
    q = 1 << s
    n = masses(m)
    out = {}
    for k in range(1, m + 1):
        if n[k] == 0:
            out[k] = Fraction(0)
            continue
        d = pow(3, k, N)
        val = autocorr(P_list[k], d, N) - autocorr(P_list[k], (d + q) % N, N)
        out[k] = Fraction(q * val, n[k])
    return out


def M_terms(P_list, m, s):
    """M_j for j=1..m+1 (M_1 = M_{m+1} = 0)."""
    n = masses(m)
    out = {1: Fraction(0), m + 1: Fraction(0)}
    for j in range(2, m + 1):
        Ej = E_op(P_list[j], s, pow(3, j))
        Oj1 = O_op(P_list[j - 1], s, pow(3, j - 1))
        X = [n[j - 1] * a - n[j] * b for a, b in zip(Ej, Oj1)]
        num = J(X, s)
        den = n[j] * n[j - 1] * (n[j] + n[j - 1])
        out[j] = Fraction(num, den)
    return out


def row(m, s):
    """All exact per-stratum data for level (m,s)."""
    P = source(m, s + 1)
    L = L_terms(P, m, s)
    M = M_terms(P, m, s)
    return {"m": m, "s": s, "P": P, "L": L, "M": M, "n": masses(m)}


# ------------------------------------------------------- radius-2 charging test
def charging_violations(L, M, m, radius=2):
    """Return list of (a,b,demand,supply) violating
       sum_{k=a..b} max(L_k,0) <= sum_{j=max(a-1,2)}^{min(b+radius,m)} M_j."""
    bad = []
    for a in range(1, m + 1):
        for b in range(a, m + 1):
            demand = sum(x for x in (L[k] for k in range(a, b + 1)) if x > 0)
            lo = max(a - 1, 2)
            hi = min(b + radius, m)
            supply = sum(M[j] for j in range(lo, hi + 1)) if lo <= hi else Fraction(0)
            if demand > supply:
                bad.append((a, b, demand, supply))
    return bad


# ------------------------------------------------------------- PARENT IDENTITY
def parent_pieces(m, s):
    """A_k = E^par(Q_k) with gauge 3^k, B_k = O^par(Q_k) with gauge 3^k,
    where Q_j = P_{m-1,j,s+2}, operators live at modulus 2^(s+2) and output
    arrays of length 2^(s+1).  PARENT IDENTITY claims P_{m,k,s+1} = A_k + B_{k-1}."""
    Q = source(m - 1, s + 2)
    A, B = {}, {}
    for k in range(0, m + 1):
        Qk = Q[k] if k < len(Q) else [0] * (1 << (s + 2))
        A[k] = E_op(Qk, s + 1, pow(3, k))
        B[k] = O_op(Qk, s + 1, pow(3, k))
    return A, B


def check_parent_identity(m, s):
    """Return (ok, ndetail) for level (m,s); m>=2, s>=0."""
    P = source(m, s + 1)
    A, B = parent_pieces(m, s)
    ok = True
    for k in range(1, m + 1):
        lhs = list(P[k])
        rhs = [a + b for a, b in zip(A[k], B[k - 1])]
        if lhs != rhs:
            ok = False
    return ok
