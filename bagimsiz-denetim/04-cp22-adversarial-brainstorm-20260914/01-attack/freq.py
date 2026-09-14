"""Per-frequency decomposition of lift and merge; Delta^(a) = M^(a) - L^(a).

ALL EXACT: integers, fractions.Fraction, and Z[zeta_N] power-basis vectors.
No floating point enters any claimed number.

--------------------------------------------------------------------------
DERIVATION (self-contained, re-derived here; every step verified in code)
--------------------------------------------------------------------------
N = 2^(s+1), q = 2^s, zeta = zeta_N primitive N-th root, c_k = 3^k mod N.

(0) Odd-character Parseval.  For X on Z/2^r,  Xhat(xi) = sum_z X(z) zeta_r^(xi z):
      sum_{xi odd mod 2^r} |Xhat(xi)|^2
        = 2^r sum_z X^2 - 2^(r-1) sum_u (X(u)+X(u+h))^2      (h = 2^(r-1))
        = 2^(r-1) sum_u (X(u)-X(u+h))^2  =  J_r(X).
    (checked in code on every array we decompose.)

(1) Split Phat_k(xi) = A_k(xi) + B_k(xi), A over even z, B over odd z.
    Then, writing w = zeta^(xi c_k),
      Ehat_k(xi) = A_k(xi) + w B_k(xi)
      Ohat_k(xi) = zeta^xi * [ B_k(3 xi) + zeta^(3 xi c_k) A_k(3 xi) ]
    Both are invariant under xi -> xi + q, hence
      J_s(E_k) = (1/2) sum_{xi odd mod N} |Ehat_k(xi)|^2,  same for O_k.

(2) Lift law.  (1/2)(|A+wB|^2 + |B+wA|^2) - |A+B|^2 = 2 Re(A conj(B)) (Re w - 1),
    and Re(A conj(B)) = (|Phat(xi)|^2 - |Phat(xi+q)|^2)/4; pairing xi <-> xi+q
    and using cos(2 pi c_k (xi+q)/N) = -cos(2 pi c_k xi /N) gives
      J_s(E_k) + J_s(O_k) - J_(s+1)(P_k)
          = sum_{xi odd mod N} cos(2 pi 3^k xi / N) |Phat_k(xi)|^2.
    (the published Round-7 law; reproduced independently here.)

(3) GAUGE.  a := 3^k xi mod N, i.e. xi_k(a) = 3^(-k) a.  Multiplication by 3 is
    a bijection on odd residues mod 2^t, so a <-> xi is a bijection per k.
      L^(a) := cos(2 pi a / N) * sum_{k=1..m} |Phat_k(xi_k(a))|^2 / n_k
    and sum_a L^(a) = L_lift exactly.

(4) MERGE over the SAME gauge.  The merge identity term k reads E_k at xi and
    O_(k-1) at xi -- but Ohat_(k-1)(xi) reads P_(k-1) at frequency 3 xi.  With
    xi = xi_k(a) = 3^(-k) a we get 3 xi = 3^(-(k-1)) a = xi_(k-1)(a): the SAME
    gauge label a.  This is why the gauge is the right common index.  Define
      M^(a) := sum_{k=2..m} (1/2) |n_(k-1) Ehat_k(xi_k(a)) - n_k Ohat_(k-1)(xi_k(a))|^2
                              / ( n_k n_(k-1) (n_k + n_(k-1)) )
    Each term is (1/2)|.|^2 / positive, so M^(a) >= 0 for every a [PROOF].
    Summing over a re-runs the bijection per k and returns, by (1),
      sum_a M^(a) = sum_k J_s(n_(k-1)E_k - n_k O_(k-1))/(n_k n_(k-1)(n_k+n_(k-1)))
                  = M_merge.

(5) Delta^(a) := M^(a) - L^(a);  sum_a Delta^(a) = M_merge - L_lift = defect.
    CORRECTNESS CRITERION: that rational identity is checked on every row.
"""
import sys, os, json, time
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, sign_of_real, to_rational, approx_str  # noqa: E402
from source import prefix_hist, J, Ecal, transfer, row, merge_identity  # noqa: E402


# ------------------------------------------------------- Fourier helpers ----

def dft(X, r):
    """Xhat(xi) for all xi mod 2^r, as Cyc elements in Z[zeta_{2^r}]."""
    R = 1 << r
    d = R // 2
    out = []
    for xi in range(R):
        a = Cyc(d)
        for z, v in enumerate(X):
            if v:
                e = (xi * z) % R
                if e < d:
                    a.c[e] += v
                else:
                    a.c[e - d] -= v
        out.append(a)
    return out


def parseval_check(X, r):
    """MANDATORY: sum_{xi odd} |Xhat(xi)|^2 == J_r(X) as rationals."""
    R = 1 << r
    H = dft(X, r)
    tot = Cyc(R // 2)
    for xi in range(1, R, 2):
        tot = tot + norm2(H[xi])
    val = to_rational(tot)
    return val is not None and val == J(X, r)


def embed(a_small, d_big):
    """Z[zeta_{2d_small}] -> Z[zeta_{2d_big}] via zeta_small = zeta_big^(ratio)."""
    ratio = d_big // a_small.d
    out = Cyc(d_big)
    for j, v in enumerate(a_small.c):
        if v:
            e = j * ratio
            if e < d_big:
                out.c[e] += v
            else:
                out.c[e - d_big] -= v
    return out


# ------------------------------------------------------- the decomposition --

def decompose(m, s, verbose=False):
    t0 = time.time()
    N = 1 << (s + 1)
    q = 1 << s
    d = N // 2                       # degree of Z[zeta_N]
    r = row(m, s)
    hist = r["hist_hi"]              # P_{m,k,s+1}, arrays of length N

    # ---- mandatory Parseval verification on every array we decompose -------
    pchecks = []
    for k in range(1, m + 1):
        pchecks.append(parseval_check(hist[k], s + 1))
        E, O = r["EO"][k]
        pchecks.append(parseval_check(E, s))
        pchecks.append(parseval_check(O, s))
    parseval_ok = all(pchecks)

    # ---- per-k spectra in Z[zeta_N] ---------------------------------------
    Ph = {}      # Phat_k(xi)
    Ah = {}
    Bh = {}
    for k in range(1, m + 1):
        P = hist[k]
        Ph[k] = dft(P, s + 1)
        Ae = [P[z] if z % 2 == 0 else 0 for z in range(N)]
        Bo = [P[z] if z % 2 == 1 else 0 for z in range(N)]
        Ah[k] = dft(Ae, s + 1)
        Bh[k] = dft(Bo, s + 1)

    # ---- Ehat_k(xi), Ohat_k(xi) for xi odd mod N (verify against J_s) -----
    Eh = {}
    Oh = {}
    for k in range(1, m + 1):
        ck = pow(3, k, N)
        Ek = {}
        Ok = {}
        for xi in range(1, N, 2):
            w = Cyc.zpow(d, xi * ck)
            Ek[xi] = Ah[k][xi] + w * Bh[k][xi]
            x3 = (3 * xi) % N
            w3 = Cyc.zpow(d, 3 * xi * ck)
            Ok[xi] = Cyc.zpow(d, xi) * (Bh[k][x3] + w3 * Ah[k][x3])
        Eh[k] = Ek
        Oh[k] = Ok
    # verify J_s(E_k) == (1/2) sum_xi |Ehat|^2  (and same for O)
    eo_ok = True
    for k in range(1, m + 1):
        for arr, H in ((r["EO"][k][0], Eh[k]), (r["EO"][k][1], Oh[k])):
            tot = Cyc(d)
            for xi in range(1, N, 2):
                tot = tot + norm2(H[xi])
            v = to_rational(tot)
            if v is None or v / 2 != J(arr, s):
                eo_ok = False

    # ---- gauge a = 3^k xi  -------------------------------------------------
    inv3 = pow(3, -1, N)
    # bijection check
    bij_ok = sorted((3 * xi) % N for xi in range(1, N, 2)) == list(range(1, N, 2))

    odd_a = list(range(1, N, 2))
    Lpart = {}
    Mpart = {}
    Dpart = {}
    half = Fraction(1, 2)
    for a in odd_a:
        # L^(a) = cos(2 pi a/N) * sum_k |Phat_k(3^{-k}a)|^2 / n_k
        acc = Cyc(d)
        for k in range(1, m + 1):
            nk = comb(m - 1, k - 1)
            xi = (pow(inv3, k, N) * a) % N
            acc = acc + norm2(Ph[k][xi]).scale(Fraction(1, nk))
        cosa = (Cyc.zpow(d, a) + Cyc.zpow(d, -a)).scale(half)
        L = cosa * acc
        # M^(a)
        Mv = Cyc(d)
        for k in range(2, m + 1):
            nk = comb(m - 1, k - 1)
            nkm = comb(m - 1, k - 2)
            xi = (pow(inv3, k, N) * a) % N
            Dv = Eh[k][xi].scale(nkm) - Oh[k - 1][xi].scale(nk)
            wgt = Fraction(1, 2 * nk * nkm * (nk + nkm))
            Mv = Mv + norm2(Dv).scale(wgt)
        Lpart[a] = L
        Mpart[a] = Mv
        Dpart[a] = Mv - L

    # ---- exact identity checks --------------------------------------------
    sL = Cyc(d)
    sM = Cyc(d)
    for a in odd_a:
        sL = sL + Lpart[a]
        sM = sM + Mpart[a]
    rL = to_rational(sL)
    rM = to_rational(sM)
    id_L = (rL is not None and rL == r["L"])
    id_M = (rM is not None and rM == r["M"])
    sD = rM - rL if (rL is not None and rM is not None) else None
    id_D = (sD is not None and sD == r["defect"])
    mident, _ = merge_identity(r)
    id_merge = (mident == r["M"])

    # ---- signs (certified, via rational enclosures) ------------------------
    signs = {a: sign_of_real(Dpart[a]) for a in odd_a}
    msigns = {a: sign_of_real(Mpart[a]) for a in odd_a}
    lsigns = {a: sign_of_real(Lpart[a]) for a in odd_a}

    return dict(
        m=m, s=s, N=N,
        I=r["I"], F=r["F"], Out=r["Out"], L=r["L"], M=r["M"], defect=r["defect"],
        parseval_ok=parseval_ok, eo_ok=eo_ok, bij_ok=bij_ok,
        id_L=id_L, id_M=id_M, id_D=id_D, id_merge=id_merge,
        sum_L=rL, sum_M=rM, sum_D=sD,
        Lpart=Lpart, Mpart=Mpart, Dpart=Dpart,
        signs=signs, msigns=msigns, lsigns=lsigns,
        odd_a=odd_a, secs=time.time() - t0,
    )


def fmt(el):
    v = to_rational(el)
    if v is not None:
        return str(v)
    return "~" + approx_str(el, 18)


if __name__ == "__main__":
    for (m, s) in [(4, 2), (3, 2), (2, 1)]:
        R = decompose(m, s)
        print("(m=%d,s=%d) N=%d parseval=%s EOhat=%s bijection=%s" %
              (m, s, R["N"], R["parseval_ok"], R["eo_ok"], R["bij_ok"]))
        print("   I=%s F=%s Out=%s L=%s M=%s defect=%s" %
              (R["I"], R["F"], R["Out"], R["L"], R["M"], R["defect"]))
        print("   sum_a L^a = %s (==L: %s)   sum_a M^a = %s (==M: %s)   sum_a D^a = %s (==defect: %s)" %
              (R["sum_L"], R["id_L"], R["sum_M"], R["id_M"], R["sum_D"], R["id_D"]))
        for a in R["odd_a"]:
            print("     a=%-3d L^a=%-28s M^a=%-28s D^a=%-28s sign=%+d" %
                  (a, fmt(R["Lpart"][a]), fmt(R["Mpart"][a]), fmt(R["Dpart"][a]), R["signs"][a]))
