"""CP29 verification of the proved identities for the mod-3^s collision energy chi_s.

Model: A_i iid, P(A=a)=2^-a (a>=1).  X_0=0, X_s = 2^{-A}(1+3X_{s-1}) mod 3^s (fresh A).
p_s(y)=P(X_s=y), q_s=sum p_s^2, chi_s=3^s q_s, E_s=chi_s-chi_{s-1}.

Checks:
  I1  q_s = q_{s-1}/3 + r_s, r_s=P(collision, A_1!=A'_1); E_s=3^s r_s; r_1=2/9, r_2=10/189 (exact Fraction).
  I2  E_s = 3^{s-1} sum_{l!=0} 4^{-|l|} C_s(l mod 3^{s-1}), C_s(j)=P(T'=4^j T mod 3^s), T=1+3X_{s-1}  (float64, s<=8).
  I3  E_s = 3^s sum_{r,t} (q_s(r,t)-p_{s-1}(r)/3)^2  (float64, s<=8).
  I4  v_3(x-y) alone is not a Markov state: (x,y)=(1,2),(2,4) mod 9 -> P(u=u' mod 27) = 16400/786429 vs 1280/786429 (exact).
Collatz remains OPEN; growth of chi_s beyond O(s^4) remains OPEN.
Usage: python cp29_verify.py   (needs numpy; writes cp29_verify.json)
"""
import json
from fractions import Fraction
import numpy as np


def exact_dist(s):
    """Exact law of X_s mod 3^s using A mod 2*3^(s-1) (2 is a primitive root mod 3^s)."""
    M = 3 ** s; L = 2 * 3 ** (s - 1); den = 2 ** L - 1
    wA = {r: Fraction(2 ** (L - r), den) for r in range(1, L + 1)}   # P(A = r mod L), r in 1..L
    inv2 = pow(2, -1, M)
    p = {0: Fraction(1)}
    for k in range(1, s + 1):
        Mk = 3 ** k; Lk = 2 * 3 ** (k - 1); denk = 2 ** Lk - 1; i2 = pow(2, -1, Mk)
        new = {}
        for x, px in p.items():
            t = (1 + 3 * x) % Mk
            for r in range(1, Lk + 1):
                y = t * pow(i2, r, Mk) % Mk
                new[y] = new.get(y, 0) + px * Fraction(2 ** (Lk - r), denk)
        p = new
    return p


def exact_r(s):
    """q_s and r_s exactly (A_1 is the outermost fresh letter)."""
    M = 3 ** s; L = 2 * 3 ** (s - 1); den = 2 ** L - 1; i2 = pow(2, -1, M)
    prev = exact_dist(s - 1) if s > 1 else {0: Fraction(1)}
    w = [Fraction(2 ** (L - r), den) for r in range(1, L + 1)]
    # law of (A mod L, X_s) pairs
    joint = {}
    for x, px in prev.items():
        t = (1 + 3 * x) % M
        for r in range(1, L + 1):
            y = t * pow(i2, r, M) % M
            joint[(r, y)] = joint.get((r, y), 0) + px * w[r - 1]
    q = sum(v * v for v in exact_dist(s).values())
    # same A_1 (as integers): P(A=A')=1/3, and then collision iff X_{s-1} collision
    q_prev = sum(v * v for v in prev.values())
    same = Fraction(1, 3) * q_prev
    return q, q - same, q_prev


def markov_counterexample():
    M, L = 27, 18; den = 2 ** L - 1; i2 = pow(2, -1, M)
    w = [Fraction(2 ** (L - r), den) for r in range(1, L + 1)]
    out = {}
    for x, y in [(1, 2), (2, 4)]:
        tot = Fraction(0)
        for r in range(1, L + 1):
            u = (1 + 3 * x) * pow(i2, r, M) % M
            for rp in range(1, L + 1):
                if u == (1 + 3 * y) * pow(i2, rp, M) % M:
                    tot += w[r - 1] * w[rp - 1]
        out[f"{x},{y}"] = f"{tot.numerator}/{tot.denominator}"
    return out


def pow2_table(M, phi):
    p = np.empty(phi, dtype=np.int64); p[0] = 1; k = 1
    while k < phi:
        m = min(k, phi - k); f = int(p[k - 1]) * 2 % M
        p[k:k + m] = (p[:m] * f) % M; k += m
    return p


def float_checks(smax=8):
    rows = []; p_prev = np.array([1.0]); chi_prev = 1.0
    for s in range(1, smax + 1):
        M = 3 ** s; phi = 2 * 3 ** (s - 1); n = 3 ** (s - 1)
        pw = pow2_table(M, phi); dlog = np.full(M, -1, dtype=np.int64); dlog[pw] = np.arange(phi)
        Z = (1 + 3 * np.arange(n, dtype=np.int64)) % M
        qZ = np.zeros(phi); np.add.at(qZ, dlog[Z], p_prev)
        r = np.arange(phi, dtype=float); w = np.where(r > 0, 2.0 ** -r, 2.0 ** -phi) / (1 - 2.0 ** -phi)
        qX = np.fft.irfft(np.fft.rfft(qZ) * np.conj(np.fft.rfft(w)), n=phi); qX[qX < 0] = 0
        p = np.zeros(M); p[pw] = qX
        chi = M * float((p * p).sum()); E = chi - chi_prev
        qrt = p.reshape(3, n).T                                   # q_s(r,t), y = r + t*3^(s-1)
        E_fib = M * float(((qrt - p_prev[:, None] / 3.0) ** 2).sum())
        PT = np.zeros(M); PT[Z] = p_prev; four = pw[::2][:n]; t = np.arange(M)
        C = np.array([np.dot(PT, PT[(int(four[j]) * t) % M]) for j in range(n)])
        wl = np.zeros(n)
        for l in range(1, 6 * n + 40):
            wl[l % n] += 4.0 ** -l; wl[(-l) % n] += 4.0 ** -l
        E_cor = n * float(np.dot(wl, C))
        rows.append({"s": s, "chi": chi, "E": E, "err_I2": abs(E - E_cor), "err_I3": abs(E - E_fib)})
        p_prev = p; chi_prev = chi
    return rows


if __name__ == "__main__":
    res = {}
    ex = {}
    for s in (1, 2):
        q, r, qp = exact_r(s)
        ex[s] = {"q": str(q), "r": str(r), "chi": str(3 ** s * q), "E": str(3 ** s * r),
                 "I1_holds": q == qp / 3 + r}
    assert ex[1]["r"] == "2/9" and ex[2]["r"] == "10/189", ex
    assert ex[1]["chi"] == "5/3" and ex[2]["chi"] == "15/7", ex
    chi3 = 27 * sum(v * v for v in exact_dist(3).values())
    assert chi3 == Fraction(177005, 67963), chi3
    ce = markov_counterexample()
    assert ce == {"1,2": "16400/786429", "2,4": "1280/786429"}, ce
    rows = float_checks(8)
    res = {"exact_s12": ex, "chi3": str(chi3), "I4_mod27": ce, "float_rows": rows,
           "max_err_I2": max(r["err_I2"] for r in rows), "max_err_I3": max(r["err_I3"] for r in rows)}
    json.dump(res, open("cp29_verify.json", "w", newline="\n"), indent=1)
    print("exact", ex, "chi3", chi3, "I4", ce)
    print("max_err_I2", res["max_err_I2"], "max_err_I3", res["max_err_I3"])
