"""Adversary consistency gate + support/cap exclusion roles + cited-number confirmation."""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist, transfer, J, generic_LM, autocorr
from defend_R import w_of, Tpow, dot
from defend_LXbound import real_cap
from defend_step import interval_failures

print("== (a) adversaries violate M>=L (reproduced) ==")
P1 = {1: [0,0,1,0,0,0,0,0], 2: [1,0,0,0,0,0,0,1], 3: [0,0,0,0,1,0,0,0]}
I, F, M, L, per, EO = generic_LM(P1, 3, 2)
print("ADV1: L=%s M=%s violates=%s" % (L, M, L > M))
P2 = {1: [0,0,1,0,0,0,0,0], 2: [0,3,1,0,0,0,0,0], 3: [0,3,0,0,2,0,1,0],
      4: [1,0,0,0,3,0,0,0], 5: [0,0,1,0,0,0,0,0]}
I, F, M, L, per, EO = generic_LM(P2, 5, 2)
print("ADV2: L=%s M=%s violates=%s" % (L, M, L > M))

print("== (b) corrected R1/R2 equalities hold on ADV1 (algebra, no over-proof) ==")
N = 8; q = 4; m = 3; s = 2
for k in range(1, 4):
    P = P1[k]
    d = pow(3, k, N)
    Lk = Fraction(q*(autocorr(P, d)-autocorr(P, (d+q) % N)), comb(m-1, k-1))
    w = w_of(P, s)
    R1 = Fraction(q*dot(w, Tpow(w, d, s)), comb(m-1, k-1))
    print("  ADV1 k=%d L=%s R1=%s match=%s" % (k, Lk, R1, Lk == R1))
# merge identity on ADV1
from defend_gate import transfer as tr
EO1 = {k: tr(P1[k], k, 2) for k in range(1, 4)}
tot = Fraction(0)
for j in range(2, 4):
    nj = comb(2, j-1); njm = comb(2, j-2)
    D = [njm*EO1[j][0][z]-nj*EO1[j-1][1][z] for z in range(4)]
    tot += Fraction(J(D, 2), nj*njm*(nj+njm))
print("  ADV1 merge-identity sum=%s M=%s match=%s" % (tot, M if False else generic_LM(P1, 3, 2)[2], tot == generic_LM(P1, 3, 2)[2]))

print("== (c) cap/support exclusion roles ==")
real = prefix_hist(3, 3)
for k in range(1, 4):
    rs = sorted(z for z, v in enumerate(real[k]) if v)
    a1 = sorted(z for z, v in enumerate(P1[k]) if v)
    a2 = sorted(z for z, v in enumerate(P2[k]) if v)
    print("  k=%d realcap=%d real_supp=%s | ADV1 max=%d supp=%s | ADV2 max=%d supp=%s" % (
        k, max(real[k]), rs, max(P1[k]), a1, max(P2[k]), a2))
print("  ADV1: satisfies real caps, support WRONG (excluded by support).")
print("  ADV2: piles of 3 where real max is 1 (excluded by cap).")

print("== (d) W-parent T6prop-cap membership (reading b) ==")
for k in range(1, 4):
    prop = 2*(1 if 1 <= k <= 2 else 0)+2*(1 if 1 <= k-1 <= 2 else 0)  # real_cap(2,*,5)=1 (mass 1)
    pile = [1, 2, 1][k-1]
    print("  Q%d: pile=%d T6prop(3,%d,4)=%d %s" % (k, pile, k, prop, "OK" if pile <= prop else "EXCEEDS"))

print("== (e) the single closing interval at (7,1); (9,2) supply detail ==")
fails, data, Lr, Mr = interval_failures(7, 1, "DBsup")
nint = 7*8//2
closed = [(a, b) for a in range(1, 8) for b in range(a, 8)
          if (a, b) not in [(x[0], x[1]) for x in fails]]
print("  (7,1) closed intervals: %s" % closed)
for (a, b) in closed:
    dem = sum(data[k]["DBsup"] for k in range(a, b+1))
    lo = max(a-1, 2); hi = min(b+2, 7)
    print("    [%d,%d] bound=%s supply=%s" % (a, b, dem, sum(Mr[j] for j in range(lo, hi+1))))
_, data9, L9, M9 = interval_failures(9, 2, "DBsup")
print("  (9,2) k=5: L=%s DBsup=%s supply[4..7]=%s" % (
    data9[5]["L"], data9[5]["DBsup"], sum(M9[j] for j in range(4, 8))))
print("  (9,2) M=%s" % {j: str(M9[j]) for j in sorted(M9)})
