#!/usr/bin/env python3
"""Asymmetric functionals Q1..Q4 on Hp, Hm, G5. Exact integer arithmetic only."""
from collections import Counter

def Hp(x): return (3*x+1)//2 if (x & 1) else x//2
def Hm(x): return (3*x-1)//2 if (x & 1) else x//2
def G5(x): return (5*x+1)//2 if (x & 1) else x//2
MAPS = {"Hp(3n+1)": (Hp, 3), "Hm(3n-1)": (Hm, 3), "G5(5n+1)": (G5, 5)}

def src(H, h, m):
    x = h; w = []
    for _ in range(m):
        w.append(x & 1)
        x = H(x)
    return tuple(w), sum(w), x

def word_of(H, x, m):
    w = []
    for _ in range(m):
        w.append(x & 1)
        x = H(x)
    return tuple(w)

print("== Q1: S(m) = sum_h h*B(h), exact ==")
for m in (4, 5, 6, 7, 8):
    out = {}
    for name, (H, c) in MAPS.items():
        S = 0
        for h in range(1, 2**m, 2):
            w, k, e = src(H, h, m)
            B = (2**m)*e - (c**k)*h
            S += h*B
        out[name] = S
    vals = set(out.values())
    print(f"  m={m}: " + " | ".join(f"{n}={v}" for n, v in out.items()) + f" | all-distinct={len(vals)==3}")

print("== Q1 identity check: S^-(m) == -2^m*T^+(m) + S^+(m), T=sum B^+ ==")
for m in (4, 6, 8):
    Sp = Tp = 0; Sm = 0
    for h in range(1, 2**m, 2):
        wp, kp, ep = src(Hp, h, m)
        Bp = (2**m)*ep - (3**kp)*h
        Sp += h*Bp; Tp += Bp
        wm, km, em = src(Hm, h, m)
        Bm = (2**m)*em - (3**km)*h
        Sm += h*Bm
    print(f"  m={m}: holds={Sm == -(2**m)*Tp + Sp}")

print("== Q2: A(m) = N1-N2, Nj=#{h: e(h)==j mod 3}, exact (+antisymmetry check) ==")
for m in range(2, 11):
    out = {}
    for name, (H, c) in MAPS.items():
        n1 = n2 = 0
        for h in range(1, 2**m, 2):
            _, _, e = src(H, h, m)
            r = e % 3
            n1 += (r == 1); n2 += (r == 2)
        out[name] = n1 - n2
    print(f"  m={m}: " + " | ".join(f"{n}={v}" for n, v in out.items())
          + f" | Hp+Hm={out['Hp(3n+1)']+out['Hm(3n-1)']} (expect 0)")

print("== Q4: C(m) = sum_h h*e(h), exact ==")
for m in (4, 5, 6, 7, 8):
    out = {}
    for name, (H, c) in MAPS.items():
        out[name] = sum(h*src(H, h, m)[2] for h in range(1, 2**m, 2))
    vals = set(out.values())
    print(f"  m={m}: " + " | ".join(f"{n}={v}" for n, v in out.items()) + f" | all-distinct={len(vals)==3}")

print("== Q3: I(m) = #{odd h<2^m: D|B, x=B/D positive int, word_m(x)==w(h)} [total (nontrivial x!=1)] ==")
for m in range(1, 9):
    row = {}
    for name, (H, c) in MAPS.items():
        tot = 0; nontriv = []; trivial = 0
        for h in range(1, 2**m, 2):
            w, k, e = src(H, h, m)
            B = (2**m)*e - (c**k)*h
            D = 2**m - c**k
            if D == 0 or B % D != 0:
                continue
            x = B // D
            if x <= 0:
                continue
            if word_of(H, x, m) == w:
                tot += 1
                if x == 1:
                    trivial += 1
                else:
                    nontriv.append((h, x, k))
        row[name] = (tot, trivial, nontriv)
    print(f"  m={m}:")
    for n, (t, tr, nt) in row.items():
        print(f"    {n}: I={t} (x==1:{tr}, x!=1:{len(nt)}) {nt if nt else ''}")
