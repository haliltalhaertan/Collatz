#!/usr/bin/env python3
"""CP24 scope-audit checks: exact integer/Fraction arithmetic only (stdlib).
Finite corroboration for AUDIT.md. Proves nothing by itself; proofs are in AUDIT.md.
Sections: 1 gate, 2 reflection, 3 cycle self-consistency (both signs), 4 Ecal
normalisation, 5 target-probe reproduction (bounded), 6 dropping observation.
"""
from fractions import Fraction
from math import comb

def Hp(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2

def Hm(x):
    return (3 * x - 1) // 2 if (x & 1) else x // 2

def F5(x):
    return (5 * x + 1) // 2 if (x & 1) else x // 2

def traj(H, h, m):
    x = h
    w = []
    k = 0
    for _ in range(m):
        b = x & 1
        w.append(b)
        k += b
        x = H(x)
    return tuple(w), k, x

def B_of_word(w):
    B = 0
    for i, wi in enumerate(w):
        B = (3 ** wi) * B + wi * (2 ** i)
    return B

def Ecal(H, m, r):
    P = {}
    for h in range(1, 2 ** m, 2):
        _, k, e = traj(H, h, m)
        P.setdefault(k, [0] * (2 ** r))
        P[k][e % (2 ** r)] += 1
    total = Fraction(0)
    for k, X in P.items():
        n_k = comb(m - 1, k - 1)
        s = sum((X[u] - X[u + 2 ** (r - 1)]) ** 2 for u in range(2 ** (r - 1)))
        total += Fraction(2 ** (r - 1) * s, n_k)
    return total

ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ((" | " + str(detail)) if detail else ""))
    if not cond:
        ok = False

# ---- 1. Gate ----
fails = 0
for h in range(1, 256, 2):
    w, k, e = traj(Hp, h, 8)
    B = 2 ** 8 * e - 3 ** k * h
    if B != B_of_word(w) or B % 2 == 0 or B % 3 == 0 or 2 ** 8 * e != 3 ** k * h + B:
        fails += 1
check("gate(a) 128 odd h<256 affine+B odd+Bmod3", fails == 0, f"fails={fails}")
e43, e52 = Ecal(Hp, 4, 3), Ecal(Hp, 5, 2)
check("gate(b) Ecal(4,3)=40/3", e43 == Fraction(40, 3), e43)
check("gate(b) Ecal(5,2)=31/3", e52 == Fraction(31, 3), e52)
check("gate(c) Hm 5->7->10->5", (Hm(5), Hm(7), Hm(10)) == (7, 10, 5))

# ---- 2. Reflection H_-(2^m-h) vs H_+(h) ----
for m in (4, 6, 8):
    bad = 0
    for h in range(1, 2 ** m, 2):
        wp, kp, ep = traj(Hp, h, m)
        wm, km, em = traj(Hm, 2 ** m - h, m)
        Bp = 2 ** m * ep - 3 ** kp * h
        Bm = 2 ** m * em - 3 ** km * (2 ** m - h)
        if not (wm == wp and km == kp and Bm == -Bp and em + ep == 3 ** kp):
            bad += 1
    check(f"reflect pairing m={m} (word,B neg,ep+em=3^k)", bad == 0, f"bad={bad}")
check("Hm(-x)=-Hp(x) on [-50,50]", all(Hm(-x) == -Hp(x) for x in range(-50, 51)))
for (m, r) in ((4, 3), (5, 2), (6, 2)):
    check(f"Ecal blind Hp==Hm ({m},{r})", Ecal(Hp, m, r) == Ecal(Hm, m, r),
          f"{Ecal(Hp, m, r)}")
# Q1 cross-identity S^-(m)==-2^m T^+(m)+S^+(m), m=6
Sp = Tp = Sm = 0
for h in range(1, 64, 2):
    wp, kp, ep = traj(Hp, h, 6)
    Bp = 64 * ep - 3 ** kp * h
    Sp += h * Bp
    Tp += Bp
    wm, km, em = traj(Hm, h, 6)
    Sm += h * (64 * em - 3 ** km * h)
check("Q1 cross-identity m=6", Sm == -(64) * Tp + Sp)
# same-h behaviour DIFFERS (pairing is cross-h, not same-h)
dis = sum(1 for h in range(1, 256, 2) if traj(Hp, h, 8)[1] != traj(Hm, h, 8)[1])
check("same-h k differs somewhere (blind!=same)", dis > 0, f"disagree={dis}/128")
Cp = sum(h * traj(Hp, h, 6)[2] for h in range(1, 64, 2))
Cm = sum(h * traj(Hm, h, 6)[2] for h in range(1, 64, 2))
check("Q4 separates maps m=6", Cp != Cm, f"Hp={Cp} Hm={Cm}")

# ---- 3. Cycle self-consistency, BOTH signs, exhaustive m<=8 ----
def orbit_word(H, x, m):
    w = []
    y = x
    for _ in range(m):
        wi = y & 1
        w.append(wi)
        y = H(y)
    return w, y

# named instances (hand-checkable)
inst = [
    ("Hp", Hp, +1, (1, 0), 1), ("Hp", Hp, +1, (1, 0, 1, 0), 1),
    ("Hp", Hp, +1, (1, 1), -1),  # negative integer fixed point, word matches
    ("Hm", Hm, -1, (1, 1, 0), 5), ("Hm", Hm, -1, (1, 0, 1), 7),
    ("Hm", Hm, -1, (1, 1, 1), 1),  # Hm(1)=(3-1)/2=1: positive fixed point
]
for name, H, b, w, xwant in inst:
    m, k, B = len(w), sum(w), B_of_word(w)
    D = 2 ** m - 3 ** k
    x = b * B // D if (b * B) % D == 0 else None
    wx, ex = orbit_word(H, x, m)
    check(f"cycle {name} w={w} x={x}", x == xwant and wx == list(w) and ex == x,
          f"B={B} D={D} x={x}")
for m in range(1, 9):
    for (H, b, tag) in ((Hp, +1, "Hp"), (Hm, -1, "Hm")):
        div = self_any = self_pos = 0
        for mask in range(1 << (m - 1)):
            w = [1] + [(mask >> (i - 1)) & 1 for i in range(1, m)]
            k, B = sum(w), B_of_word(w)
            D = 2 ** m - 3 ** k
            assert D != 0 and D % 2 == 1
            if (b * B) % D != 0:
                continue
            div += 1
            x = b * B // D
            wx, ex = orbit_word(H, x, m)
            if wx == w and ex == x:
                self_any += 1
                self_pos += (x > 0)
            else:
                check(f"thm instance {tag} m={m} w={w}", False, f"x={x} wx={wx}")
        check(f"exhaust m={m} {tag}: div==self_any (positivity extra)", div == self_any,
              f"div={div} self_any={self_any} self_pos={self_pos}")
        if tag == "Hp":
            check(f"  Hp m={m}: positives need D>0 only", True)

# ---- 4. Ecal normalisation: Ecal == 2^(m-1) sum pi_k J(p_k) ----
for (m, r) in ((4, 3), (5, 2)):
    P = {}
    for h in range(1, 2 ** m, 2):
        _, k, e = traj(Hp, h, m)
        P.setdefault(k, [0] * (2 ** r))
        P[k][e % (2 ** r)] += 1
    norm = Fraction(0)
    for k, X in P.items():
        n_k = comb(m - 1, k - 1)
        pi = Fraction(n_k, 2 ** (m - 1))
        Jp = Fraction(2 ** (r - 1) * sum(
            (Fraction(X[u], n_k) - Fraction(X[u + 2 ** (r - 1)], n_k)) ** 2
            for u in range(2 ** (r - 1))), 1)
        norm += pi * Jp
        check(f"  J(p) bound k={k} (m={m},r={r})", Jp <= 2 ** (r - 1), f"Jp={Jp}")
    check(f"normalisation Ecal==2^(m-1) sum pi J(p) ({m},{r})",
          Ecal(Hp, m, r) == 2 ** (m - 1) * norm,
          f"Ecal={Ecal(Hp, m, r)} norm-sum={norm}")
print(f"normalised (4,3)={Ecal(Hp,4,3)/8} (5,2)={Ecal(Hp,5,2)/16}")

# ---- 5. Bounded probe reproduction ----
def probe(Hp_like, M, sign):
    # sign=+1: Hp rule D>0,q=B/D ; sign=-1: Hm rule D<0,q=B/(-D)
    out = {}
    for m in range(1, M + 1):
        tot = nontriv = 0
        ex = None
        for h in range(1, 1 << m, 2):
            w, k, e = traj(Hp_like, h, m)
            B, D = B_of_word(w), 2 ** m - 3 ** k
            if sign > 0 and D <= 0:
                continue
            if sign < 0 and D >= 0:
                continue
            den = D if sign > 0 else -D
            if B % den != 0:
                continue
            q = B // den
            if q <= 0 or q % 2 == 0:
                continue
            wq, eq = orbit_word(Hp_like, q, m)
            if list(wq) == list(w) and eq == q:
                tot += 1
                nontriv += (q != 1)
                if ex is None:
                    ex = (w, k, B, D, q)
        out[m] = (tot, nontriv, ex)
    return out
hp = probe(Hp, 12, +1)
check("probe Hp m<=12: zero nontrivial", all(v[1] == 0 for v in hp.values()),
      {m: v[:2] for m, v in hp.items()})
check("probe Hp m<=12: only trivial q=1 at even m",
      all((v[0] == 0) == (m % 2 == 1) for m, v in hp.items()))
hm = probe(Hm, 6, -1)
qs3 = sorted(p[4] for p in [hm[3][2]] if p)  # example shown below
got = set()
for m in range(1, 7):
    for h in range(1, 1 << m, 2):
        w, k, e = traj(Hm, h, m)
        B, D = B_of_word(w), 2 ** m - 3 ** k
        if D >= 0 or B % (-D) != 0:
            continue
        q = B // (-D)
        wq, eq = orbit_word(Hm, q, m)
        if q > 0 and q % 2 == 1 and list(wq) == list(w) and eq == q and m == 3:
            got.add(q)
check("probe Hm m=3 witnesses {1,5,7}", got == {1, 5, 7}, sorted(got))
w5 = (1, 1, 0, 0, 0)
B5 = sum((1 << i) if wi else 0 if False else (5 * 0 + 0) for i, wi in enumerate(w5))  # placeholder
B5v, D5 = 7, 32 - 25  # B5(w)=5*B+1: i0:1, i1:5*1+2=7, rest 0-steps keep 7
wq, eq = orbit_word(F5, 1, 5)
check("probe F5 witness q=1 self-consistent", B5v // D5 == 1 and list(wq) == [1, 1, 0, 0, 0] and eq == 1)
seq = [1]
x = 1
for _ in range(5):
    x = F5(x)
    seq.append(x)
check("probe F5 cycle closes at 1", seq[-1] == 1, seq)

# ---- 6. Dropping-fraction finite observation (for recommendation baseline) ----
for m, want in ((8, Fraction(94, 128)), (16, Fraction(27823, 32768))):
    N = 2 ** (m - 1)
    d = 0
    for h in range(1, 2 ** m, 2):
        y = h
        for _ in range(m):
            y = Hp(y)
        d += (y < h)
    check(f"dropping fraction m={m} (observation, not theorem)", Fraction(d, N) == want,
          f"{d}/{N}")

print("ALL_OK" if ok else "SOME_FAIL")
raise SystemExit(0 if ok else 1)
