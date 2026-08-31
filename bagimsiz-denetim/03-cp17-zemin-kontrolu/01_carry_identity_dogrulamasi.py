"""
CP17 ZEMIN KONTROLU — carry identity'lerinin bagimsiz dogrulanmasi.

CP17 butun CP18-CP20 zincirinin dayandigi tek donmus teorem. Ozeti su
identity'leri load-bearing olarak veriyor:

  (1) D_k = -s_k - {alpha*k}                      [s_k = floor(alpha*k) - A_k]
  (2) n_k = n_0 * 3^k * 2^{-A_k} * U_k            [U_k = prod_{i<k}(1+1/(3n_i))]
  (3) U_{k+1} - U_k = 2^{D_k} / (3 n_0)
  (4) U_N = 1 + X_N/(3 n_0)                       [X_N = sum_{k<N} 2^{D_k}]
  (5) 0 <= H_N - 3*log(U_N) <= pi^2/48            [H_N = sum_{k<N} 1/n_k]

(1)-(4) KESIN cebirsel ozdeslikler olmali -> Fraction ile tam aritmetik.
(5) bir esitsizlik -> yuksek hassasiyetli ondalik.

Arsivdeki hicbir koda bakilmadi.
"""
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import math
getcontext().prec = 80

ALPHA = Decimal(3).ln()/Decimal(2).ln()
PI2_48 = (Decimal('3.14159265358979323846264338327950288419716939937510')**2)/48

def orbit(n0, steps):
    ns, av = [n0], []
    n = n0
    for _ in range(steps):
        m = 3*n+1
        a = (m & -m).bit_length()-1
        n = m >> a
        av.append(a); ns.append(n)
        if n == 1: break
    return ns, av

def floor_alpha(k):
    return int((ALPHA*k).to_integral_value(rounding='ROUND_FLOOR'))

fail = {1:0, 2:0, 3:0, 4:0, 5:0}
tested = {1:0, 2:0, 3:0, 4:0, 5:0}
worst5_lo = Decimal(10); worst5_hi = Decimal(-10)

for n0 in range(3, 4001, 2):
    ns, av = orbit(n0, 400)
    K = len(av)
    if K < 5: continue
    A = [0]*(K+1)
    for k in range(K): A[k+1] = A[k] + av[k]

    # U_k tam kesir olarak
    U = [Fr(1)]
    for k in range(K):
        U.append(U[k] * (1 + Fr(1, 3*ns[k])))

    X = [Fr(0)]
    for k in range(K):
        X.append(X[k] + Fr(2)**A[k] * Fr(1,1) if False else X[k])  # placeholder, asagida gercek

    # gercek X_N: sum 2^{D_k}, D_k = A_k - alpha*k  -> 2^{D_k} = 2^{A_k}/3^k
    X = [Fr(0)]
    for k in range(K):
        X.append(X[k] + Fr(2**A[k], 3**k))

    for k in range(1, K+1):
        # (2) n_k = n_0 * 3^k * 2^{-A_k} * U_k
        tested[2] += 1
        if Fr(ns[k]) != Fr(n0) * Fr(3**k, 2**A[k]) * U[k]:
            fail[2] += 1

    for k in range(K):
        # (3) U_{k+1}-U_k = 2^{D_k}/(3 n_0) = 2^{A_k}/(3^k * 3 * n_0)
        tested[3] += 1
        if U[k+1]-U[k] != Fr(2**A[k], 3**k * 3 * n0):
            fail[3] += 1

    for N in range(1, K+1):
        # (4) U_N = 1 + X_N/(3 n_0)
        tested[4] += 1
        if U[N] != 1 + X[N]/(3*n0):
            fail[4] += 1

    # (1) D_k = -s_k - {alpha k}   (ondalik, tanim gereği)
    for k in range(0, min(K,60)+1):
        tested[1] += 1
        s_k = floor_alpha(k) - A[k]
        D_k = Decimal(A[k]) - ALPHA*k
        frac = ALPHA*k - floor_alpha(k)
        if abs(D_k - (-Decimal(s_k) - frac)) > Decimal('1e-50'):
            fail[1] += 1

    # (5) 0 <= H_N - 3 log U_N <= pi^2/48
    H = Fr(0)
    for N in range(1, K+1):
        H += Fr(1, ns[N-1])
        tested[5] += 1
        lhs = Decimal(H.numerator)/Decimal(H.denominator)
        u = Decimal(U[N].numerator)/Decimal(U[N].denominator)
        gap = lhs - 3*u.ln()
        if gap < worst5_lo: worst5_lo = gap
        if gap > worst5_hi: worst5_hi = gap
        if gap < Decimal('-1e-40') or gap > PI2_48:
            fail[5] += 1

isim = {1:"D_k = -s_k - {alpha k}",
        2:"n_k = n_0*3^k*2^-A_k*U_k",
        3:"U_{k+1}-U_k = 2^D_k/(3n_0)",
        4:"U_N = 1 + X_N/(3n_0)",
        5:"0 <= H_N-3logU_N <= pi^2/48"}
print("CP17 carry identity dogrulamasi (n0 = 3,5,...,3999; tam kesir aritmetigi)\n")
print(f"{'#':>2} {'ozdeslik':<30} {'test':>10} {'ihlal':>8}  {'durum'}")
for i in (1,2,3,4,5):
    d = "TAMAM" if fail[i]==0 else "IHLAL"
    print(f"{i:>2} {isim[i]:<30} {tested[i]:>10,} {fail[i]:>8}  {d}")
print(f"\n(5) gozlenen aralik: [{worst5_lo:.2e}, {worst5_hi:.6f}]")
print(f"    teorik ust sinir pi^2/48 = {PI2_48:.6f}")
print(f"    marj: {PI2_48-worst5_hi:.6f}")
