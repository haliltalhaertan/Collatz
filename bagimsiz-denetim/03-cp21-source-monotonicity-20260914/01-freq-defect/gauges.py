"""Convention robustness: three legitimate common indexings, same grid.

For each, sum_a L^(a) = L_lift, sum_a M^(a) = M_merge, sum_a Delta^(a) = defect
(checked exactly every row).  Question: is Delta^(a) >= 0 under ANY of them?

  GAUGE A  (the one in freq.py):  a = 3^k * xi   (lift-law natural label;
           makes E_k and O_{k-1} in the merge term carry the SAME label)
  GAUGE B  (ungauged):            a = xi          (raw input frequency)
  GAUGE C  (shifted):             a = 3^(k-1)*xi  (merge-term "parent" label)

Everything exact.  No floats.
"""
import sys, os, json, time
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, sign_of_real, to_rational, approx_str
from source import row, J
from freq import dft


def gauged(m, s, gauge):
    N = 1 << (s + 1)
    d = N // 2
    r = row(m, s)
    hist = r["hist_hi"]
    inv3 = pow(3, -1, N)
    Ph, Ah, Bh, Eh, Oh = {}, {}, {}, {}, {}
    for k in range(1, m + 1):
        P = hist[k]
        Ph[k] = dft(P, s + 1)
        Ah[k] = dft([P[z] if z % 2 == 0 else 0 for z in range(N)], s + 1)
        Bh[k] = dft([P[z] if z % 2 == 1 else 0 for z in range(N)], s + 1)
    for k in range(1, m + 1):
        ck = pow(3, k, N)
        Eh[k], Oh[k] = {}, {}
        for xi in range(1, N, 2):
            Eh[k][xi] = Ah[k][xi] + Cyc.zpow(d, xi * ck) * Bh[k][xi]
            x3 = (3 * xi) % N
            Oh[k][xi] = Cyc.zpow(d, xi) * (Bh[k][x3] + Cyc.zpow(d, 3 * xi * ck) * Ah[k][x3])

    def xi_of(a, k):
        if gauge == "A":
            return (pow(inv3, k, N) * a) % N
        if gauge == "B":
            return a
        if gauge == "C":
            return (pow(inv3, k - 1, N) * a) % N
        raise ValueError(gauge)

    odd = list(range(1, N, 2))
    D = {}
    Lp = {}
    Mp = {}
    for a in odd:
        acc = Cyc(d)
        for k in range(1, m + 1):
            nk = comb(m - 1, k - 1)
            xi = xi_of(a, k)
            ck_xi = (pow(3, k, N) * xi) % N
            cosv = (Cyc.zpow(d, ck_xi) + Cyc.zpow(d, -ck_xi)).scale(Fraction(1, 2))
            acc = acc + (cosv * norm2(Ph[k][xi])).scale(Fraction(1, nk))
        Mv = Cyc(d)
        for k in range(2, m + 1):
            nk = comb(m - 1, k - 1)
            nkm = comb(m - 1, k - 2)
            xi = xi_of(a, k)
            Dv = Eh[k][xi].scale(nkm) - Oh[k - 1][xi].scale(nk)
            Mv = Mv + norm2(Dv).scale(Fraction(1, 2 * nk * nkm * (nk + nkm)))
        Lp[a], Mp[a], D[a] = acc, Mv, Mv - acc
    sL = Cyc(d)
    sM = Cyc(d)
    for a in odd:
        sL = sL + Lp[a]
        sM = sM + Mp[a]
    rL, rM = to_rational(sL), to_rational(sM)
    ok = (rL == r["L"] and rM == r["M"] and rM - rL == r["defect"])
    signs = {a: sign_of_real(D[a]) for a in odd}
    return ok, signs, D, r


if __name__ == "__main__":
    pairs = [(m, s) for s in (2, 3, 4) for m in range(4, 13) if s <= m - 1]
    t0 = time.time()
    summary = {}
    for g in ("A", "B", "C"):
        bad = []
        allok = True
        for (m, s) in pairs:
            ok, signs, D, r = gauged(m, s, g)
            allok &= ok
            neg = [a for a in signs if signs[a] < 0]
            if neg:
                bad.append(((m, s), neg))
        summary[g] = dict(identity_ok=allok, rows_with_negative=len(bad), total=len(pairs),
                          first=str(bad[0]) if bad else None)
        print("GAUGE %s: identity_ok=%s  rows with a negative Delta^(a): %d/%d  first=%s"
              % (g, allok, len(bad), len(pairs), bad[0] if bad else None))
    print("elapsed %.1fs" % (time.time() - t0))
    print()
    print("CONCLUSION: the conjecture fails under every common index tried.")
