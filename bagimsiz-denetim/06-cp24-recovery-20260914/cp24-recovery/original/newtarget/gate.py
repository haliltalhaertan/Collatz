"""Grounding gate reproduction: exact integer / Fraction arithmetic only."""
from fractions import Fraction
from math import comb

def Hp(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2

def Hm(x):
    return (3 * x - 1) // 2 if (x & 1) else x // 2

def check_a(m=8):
    fails = 0
    total = 0
    for h in range(1, 1 << m, 2):
        total += 1
        x = h
        k = 0
        B = 0
        for i in range(m):
            w = x & 1
            if w:
                k += 1
                B = 3 * B + (1 << i)
            x = Hp(x)
        e = x
        B2 = (1 << m) * e - pow(3, k) * h
        if B2 != B:
            fails += 1
        if (B % 2 == 0) or (B % 3 == 0):
            fails += 1
        if (1 << m) * e != pow(3, k) * h + B:
            fails += 1
    return total, fails

def Ecal(m, r, f=Hp):
    mod = 1 << r
    P = {k: [0] * mod for k in range(1, m + 1)}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = f(x)
        P[k][x % mod] += 1
    total = Fraction(0, 1)
    for k in range(1, m + 1):
        nk = comb(m - 1, k - 1)
        X = P[k]
        half = 1 << (r - 1)
        s = 0
        for u in range(half):
            d = X[u] - X[u + half]
            s += d * d
        total += Fraction(half * s, nk)
    return total

def check_c():
    seq = [5]
    x = 5
    for _ in range(3):
        x = Hm(x)
        seq.append(x)
    return seq

if __name__ == "__main__":
    tot, fails = check_a(8)
    print(f"gate_a_total_odd={tot} gate_a_fails={fails}")
    print(f"Ecal(4,3)={Ecal(4,3)} expected={Fraction(40,3)} match={Ecal(4,3)==Fraction(40,3)}")
    print(f"Ecal(5,2)={Ecal(5,2)} expected={Fraction(31,3)} match={Ecal(5,2)==Fraction(31,3)}")
    seq = check_c()
    print(f"Hm_cycle={seq} match={seq==[5,7,10,5]}")
    print(f"Hm(5)={(3*5-1)//2} Hm(7)={(3*7-1)//2} Hm(10)={10//2}")
