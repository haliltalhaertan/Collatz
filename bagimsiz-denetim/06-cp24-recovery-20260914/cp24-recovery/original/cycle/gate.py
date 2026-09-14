#!/usr/bin/env python3
"""Grounding gate: reproduce (a)(b)(c) with exact arithmetic."""
from fractions import Fraction
from math import comb

def Hp(x: int) -> int:
    if x % 2 == 1:
        assert (3*x+1) % 2 == 0
        return (3*x+1)//2
    else:
        return x//2

def Hm(x: int) -> int:
    if x % 2 == 1:
        assert (3*x-1) % 2 == 0
        return (3*x-1)//2
    else:
        return x//2

def orbit_stats(H, h, m):
    """Run m steps of H from h. Return (k, e, word list)."""
    x = h
    k = 0
    w = []
    for i in range(m):
        wi = x % 2  # 1 if odd else 0 ; x positive so fine
        w.append(wi)
        if wi == 1:
            k += 1
        x = H(x)
    e = x
    return k, e, w

def B_of_word(w):
    B = 0
    for i, wi in enumerate(w):
        B = (3**wi)*B + wi*(2**i)
    return B

# (a) affine identity on every odd h < 2^8
m = 8
N = 2**m
fails = 0
checked = 0
for h in range(1, N, 2):
    k, e, w = orbit_stats(Hp, h, m)
    B = B_of_word(w)
    lhs = (2**m)*e
    rhs = (3**k)*h + B
    cond_identity = (lhs == rhs)
    cond_Bodd = (B % 2 == 1)
    cond_Bmod3 = (B % 3 != 0)
    checked += 1
    if not (cond_identity and cond_Bodd and cond_Bmod3):
        fails += 1
        print(f"FAIL h={h} k={k} e={e} B={B} id={cond_identity} odd={cond_Bodd} mod3={cond_Bmod3}")
print(f"(a) checked={checked} fails={fails}")

# Also verify B recurrence matches A1 and B odd etc.
# (b) Ecal
def Ecal(H, m, r):
    # P_{m,k,r}(z) for each k: dict z -> count
    # k ranges? odd h => k>=1, up to m
    from collections import defaultdict
    P = {}  # k -> list length 2^r
    for k in range(0, m+1):
        P[k] = [0]*(2**r)
    for h in range(1, 2**m, 2):
        k, e, w = orbit_stats(H, h, m)
        z = e % (2**r)
        P[k][z] += 1
    E = Fraction(0,1)
    details = {}
    for k in range(0, m+1):
        n_k = comb(m-1, k-1) if 1 <= k <= m else 0
        if n_k == 0:
            # check P empty
            assert sum(P[k]) == 0, f"m={m} k={k} sum={sum(P[k])} n_k=0"
            continue
        # sanity: sum_z P = n_k ?
        s = sum(P[k])
        assert s == n_k, f"m={m} k={k} sum={s} n_k={n_k}"
        J = Fraction(0,1)
        # J_r(X) = 2^{r-1} sum_{u<2^{r-1}} (X(u)-X(u+2^{r-1}))^2
        half = 2**(r-1)
        sumsq = 0
        for u in range(half):
            d = P[k][u] - P[k][u+half]
            sumsq += d*d
        J = Fraction(half * sumsq, 1)
        E += Fraction(J, n_k)
        details[k] = (P[k], n_k, J)
    return E, details

E43, d43 = Ecal(Hp, 4, 3)
E52, d52 = Ecal(Hp, 5, 2)
print(f"(b) Ecal(4,3)={E43} expected 40/3 -> {'OK' if E43==Fraction(40,3) else 'MISMATCH'}")
print(f"(b) Ecal(5,2)={E52} expected 31/3 -> {'OK' if E52==Fraction(31,3) else 'MISMATCH'}")
for k,(P,n,J) in sorted(d43.items()):
    print(f"  m=4,r=3,k={k} n={n} J={J} P={P}")
for k,(P,n,J) in sorted(d52.items()):
    print(f"  m=5,r=2,k={k} n={n} J={J} P={P}")

# (c) 3n-1 cycle 5->7->10->5 under Hm
seq = [5, Hm(5), Hm(Hm(5)), Hm(Hm(Hm(5)))]
print(f"(c) Hm orbit from 5: {seq} -> {'OK' if seq[:3]==[5,7,10] and seq[3]==5 else 'MISMATCH'}")
# also check each step explicitly
print(f"  Hm(5)={Hm(5)} (expect 7), Hm(7)={Hm(7)} (expect 10), Hm(10)={Hm(10)} (expect 5)")
gate_ok = (checked==128 and fails==0 and E43==Fraction(40,3) and E52==Fraction(31,3) and seq[:3]==[5,7,10] and seq[3]==5)
print(f"GATE_OK={gate_ok}")
