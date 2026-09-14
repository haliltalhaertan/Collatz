"""FLANK per-frequency decomposition + forced-index verification -- from scratch.

[EXACT COMPUTATION] All spectra in Z[zeta_N] with Fraction coefficients.
Floats appear ONLY as display midpoints for trend discussion, never as claims.
"""
from fractions import Fraction
from math import comb
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flank_cyc import Zeta2, abs2, as_rational, certified_sign, enclosure_mid
from flank_gate import prefix_hist, J_energy, transfer_EO, full_row


def dft_all(X, N):
    d = N // 2
    R = len(X)
    assert R == N
    out = []
    for xi in range(N):
        a = Zeta2(d)
        for z, v in enumerate(X):
            if v:
                e = (xi * z) % N
                if e < d:
                    a.c[e] += v
                else:
                    a.c[e - d] -= v
        out.append(a)
    return out


def check_parseval(X, r):
    N = 1 << r
    H = dft_all(X, N)
    tot = Zeta2(N // 2)
    for xi in range(1, N, 2):
        tot = tot + abs2(H[xi])
    v = as_rational(tot)
    return (v is not None and v == J_energy(X, r)), v


def decompose_row(m, s):
    """Exact per-frequency data. Returns dict with pair (mod-q) Deltas."""
    N = 1 << (s + 1)
    q = 1 << s
    d = N // 2
    r = full_row(m, s)
    hist = r["hist_hi"]

    # spectra of P_k
    Phat = {k: dft_all(hist[k], N) for k in range(1, m + 1)}
    # even/odd splits
    Ahat, Bhat = {}, {}
    for k in range(1, m + 1):
        P = hist[k]
        Ae = [P[z] if z % 2 == 0 else 0 for z in range(N)]
        Bo = [P[z] if z % 2 == 1 else 0 for z in range(N)]
        Ahat[k] = dft_all(Ae, N)
        Bhat[k] = dft_all(Bo, N)

    # Ehat/Ohat via closed forms; verify energies
    Ehat, Ohat = {}, {}
    for k in range(1, m + 1):
        ck = pow(3, k, N)
        Ek, Ok = {}, {}
        for xi in range(1, N, 2):
            w = Zeta2.root(d, xi * ck)
            Ek[xi] = Ahat[k][xi] + w * Bhat[k][xi]
            x3 = (3 * xi) % N
            w3 = Zeta2.root(d, 3 * xi * ck)
            Ok[xi] = Zeta2.root(d, xi) * (Bhat[k][x3] + w3 * Ahat[k][x3])
        Ehat[k] = Ek
        Ohat[k] = Ok

    eo_ok = True
    for k in range(1, m + 1):
        for arr, H in ((r["EO"][k][0], Ehat[k]), (r["EO"][k][1], Ohat[k])):
            tot = Zeta2(d)
            for xi in range(1, N, 2):
                tot = tot + abs2(H[xi])
            v = as_rational(tot)
            if v is None or v / 2 != J_energy(arr, s):
                eo_ok = False

    # ---- forced-index verification ----
    # (i) q-periodicity: Ehat_k(xi+q) == Ehat_k(xi), same for Ohat
    periodic_ok = True
    for k in range(1, m + 1):
        for xi in range(1, N, 2):
            x2 = (xi + q) % N
            if x2 % 2 == 1:
                if not (Ehat[k][xi] == Ehat[k][x2] and Ohat[k][xi] == Ohat[k][x2]):
                    periodic_ok = False
    # (ii) anti-periodicity of lift weight: cos(2pi c_k (xi+q)/N) = -cos(...)
    # c_k odd => c_k*q = q mod N => shift by half turn. Verify c_k odd + cos identity
    # as Cyc identity: z^{c(xi+q)} + z^{-c(xi+q)} == -(z^{c xi}+z^{-c xi})
    anti_ok = True
    for k in range(1, m + 1):
        ck = pow(3, k, N)
        assert ck % 2 == 1
        for xi in range(1, N, 2):
            lhs = Zeta2.root(d, ck * (xi + q)) + Zeta2.root(d, -ck * (xi + q))
            rhs = -(Zeta2.root(d, ck * xi) + Zeta2.root(d, -ck * xi))
            if not (lhs == rhs):
                anti_ok = False

    # ---- gauge decomposition per a odd mod N ----
    inv3 = pow(3, -1, N)
    oddN = list(range(1, N, 2))
    Lpart, Mpart = {}, {}
    for a in oddN:
        acc = Zeta2(d)
        for k in range(1, m + 1):
            xi = (pow(inv3, k, N) * a) % N
            acc = acc + abs2(Phat[k][xi]).scale(Fraction(1, comb(m - 1, k - 1)))
        cosa = (Zeta2.root(d, a) + Zeta2.root(d, -a)).scale(Fraction(1, 2))
        Lpart[a] = cosa * acc
        Mv = Zeta2(d)
        for k in range(2, m + 1):
            nk = comb(m - 1, k - 1)
            nkm = comb(m - 1, k - 2)
            xi = (pow(inv3, k, N) * a) % N
            Dv = Ehat[k][xi].scale(nkm) - Ohat[k - 1][xi].scale(nk)
            Mv = Mv + abs2(Dv).scale(Fraction(1, 2 * nk * nkm * (nk + nkm)))
        Mpart[a] = Mv

    sL = Zeta2(d)
    sM = Zeta2(d)
    for a in oddN:
        sL = sL + Lpart[a]
        sM = sM + Mpart[a]
    sumL = as_rational(sL)
    sumM = as_rational(sM)
    idL = (sumL is not None and sumL == r["L"])
    idM = (sumM is not None and sumM == r["M"])

    # ---- pair (mod-q) grouping: [a] = {a, a+q} ----
    # representatives: odd a in [1, q)
    reps = [a for a in range(1, q, 2)]
    pairL, pairM, pairD = {}, {}, {}
    pair_sign = {}
    for a in reps:
        b = a + q
        pairL[a] = Lpart[a] + Lpart[b]
        pairM[a] = Mpart[a] + Mpart[b]
        pairD[a] = pairM[a] - pairL[a]
        pair_sign[a] = certified_sign(pairD[a])
    sPD = Zeta2(d)
    for a in reps:
        sPD = sPD + pairD[a]
    sumPD = as_rational(sPD)
    idD = (sumPD is not None and sumPD == r["defect"])

    # per-N (mod-N refined) signs -> expect spurious negatives
    perN_sign = {a: certified_sign(Mpart[a] - Lpart[a]) for a in oddN}

    return dict(m=m, s=s, N=N, q=q, I=r["I"], F=r["F"], Out=r["Out"],
                L=r["L"], M=r["M"], defect=r["defect"],
                eo_ok=eo_ok, periodic_ok=periodic_ok, anti_ok=anti_ok,
                idL=idL, idM=idM, idD=idD, sumL=sumL, sumM=sumM, sumPD=sumPD,
                Lpart=Lpart, Mpart=Mpart, pairL=pairL, pairM=pairM,
                pairD=pairD, pair_sign=pair_sign, perN_sign=perN_sign,
                reps=reps, oddN=oddN)


if __name__ == "__main__":
    import json
    rows = [(4, 2), (3, 2), (2, 1), (5, 4), (13, 4)]
    for (m, s) in rows:
        print(f"--- (m={m},s={s}) ---")
        R = decompose_row(m, s)
        print(f"  eo_ok={R['eo_ok']} periodic={R['periodic_ok']} anti={R['anti_ok']}")
        print(f"  idL={R['idL']} idM={R['idM']} idD={R['idD']} defect={R['defect']}")
        for a in R["reps"]:
            mid, _ = enclosure_mid(R["pairD"][a])
            print(f"    pair a={a}: sign={R['pair_sign'][a]:+d} mid~{mid:.6f}")
        negs = [a for a in R["oddN"] if R["perN_sign"][a] < 0]
        print(f"  per-N negatives: {len(negs)}/{len(R['oddN'])} {negs}")
