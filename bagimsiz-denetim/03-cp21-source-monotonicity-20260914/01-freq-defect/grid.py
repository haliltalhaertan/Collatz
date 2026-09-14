"""Full grid runner + the gauge-independent kill test.

Adds two extra mandatory per-k verifications beyond freq.py:
  (A) Round-7 lift law, per k, exactly:
        J_s(E_k) + J_s(O_k) - J_{s+1}(P_k)
          == sum_{xi odd mod N} cos(2 pi 3^k xi / N) |Phat_k(xi)|^2
  (B) merge per-k spectral form, exactly:
        J_s(n_{k-1}E_k - n_k O_{k-1})
          == (1/2) sum_{xi odd mod N} |n_{k-1}Ehat_k(xi) - n_k Ohat_{k-1}(xi)|^2

GAUGE-INDEPENDENT KILL TEST.  L^(a) is canonical: the Round-7 law expresses
L_lift as a sum over genuine input frequencies with no freedom.  M^(a) carries
a lift convention (each odd residue mod q has two lifts mod N).  But ANY
decomposition of M_merge into nonnegative per-frequency parts obeys
M^(a) <= M_merge.  Hence
        L^(a) > M_merge   ==>   Delta^(a) < 0 for EVERY such decomposition.
We report that stronger, convention-free test alongside the plain sign.
"""
import sys, os, json, time
from fractions import Fraction
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, sign_of_real, to_rational, approx_str
from source import prefix_hist, J, Ecal, transfer, row, merge_identity, run_gate
from freq import dft, parseval_check, decompose, fmt


def per_k_laws(m, s):
    """Return (lift_law_ok, merge_spec_ok) -- exact per-k identity checks."""
    N = 1 << (s + 1)
    d = N // 2
    r = row(m, s)
    hist = r["hist_hi"]
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
    lift_ok = True
    for k in range(1, m + 1):
        lhs = J(r["EO"][k][0], s) + J(r["EO"][k][1], s) - J(hist[k], s + 1)
        acc = Cyc(d)
        for xi in range(1, N, 2):
            cosv = (Cyc.zpow(d, ck_xi := (pow(3, k, N) * xi) % N) + Cyc.zpow(d, -ck_xi)).scale(Fraction(1, 2))
            acc = acc + cosv * norm2(Ph[k][xi])
        v = to_rational(acc)
        if v is None or v != lhs:
            lift_ok = False
    merge_ok = True
    for k in range(2, m + 1):
        nk = comb(m - 1, k - 1)
        nkm = comb(m - 1, k - 2)
        q = 1 << s
        D = [nkm * r["EO"][k][0][z] - nk * r["EO"][k - 1][1][z] for z in range(q)]
        lhs = J(D, s)
        acc = Cyc(d)
        for xi in range(1, N, 2):
            Dv = Eh[k][xi].scale(nkm) - Oh[k - 1][xi].scale(nk)
            acc = acc + norm2(Dv)
        v = to_rational(acc)
        if v is None or v / 2 != lhs:
            merge_ok = False
    return lift_ok, merge_ok


def run_grid(pairs, out_json):
    rows = []
    t_all = time.time()
    for (m, s) in pairs:
        t0 = time.time()
        R = decompose(m, s)
        lift_ok, merge_ok = per_k_laws(m, s)
        N = R["N"]
        # conjugate-class representatives: a in 1..N/2 odd
        classes = [a for a in range(1, N // 2 + 1, 2)]
        Mtot = R["M"]
        rec = dict(m=m, s=s, N=N,
                   I=str(R["I"]), F=str(R["F"]), Out=str(R["Out"]),
                   L=str(R["L"]), M=str(R["M"]), defect=str(R["defect"]),
                   parseval_ok=R["parseval_ok"], eo_ok=R["eo_ok"],
                   bij_ok=R["bij_ok"], lift_law_ok=lift_ok, merge_spec_ok=merge_ok,
                   id_L=R["id_L"], id_M=R["id_M"], id_D=R["id_D"], id_merge=R["id_merge"],
                   sum_D=str(R["sum_D"]))
        freqs = []
        neg = []
        robust_neg = []
        for a in R["odd_a"]:
            sg = R["signs"][a]
            # gauge-independent test: L^(a) - M_merge > 0  =>  Delta^(a)<0 always
            gi = sign_of_real(R["Lpart"][a] - Cyc.const(N // 2, Mtot))
            freqs.append(dict(a=a, sign=sg,
                              L=fmt(R["Lpart"][a]), M=fmt(R["Mpart"][a]),
                              D=fmt(R["Dpart"][a]),
                              L_gt_Mtotal=(gi > 0)))
            if sg < 0:
                neg.append(a)
            if gi > 0:
                robust_neg.append(a)
        rec["freqs"] = freqs
        rec["negative_a"] = neg
        rec["robust_negative_a"] = robust_neg
        rec["secs"] = round(time.time() - t0, 3)
        rows.append(rec)
        print("(m=%2d,s=%d) N=%2d checks[parseval=%s eo=%s bij=%s liftlaw=%s mergespec=%s sumL=%s sumM=%s sumD=%s] "
              "defect=%-12s neg_a=%s robust_neg_a=%s  %.2fs"
              % (m, s, N, R["parseval_ok"], R["eo_ok"], R["bij_ok"], lift_ok, merge_ok,
                 R["id_L"], R["id_M"], R["id_D"], R["defect"], neg, robust_neg, rec["secs"]))
        sys.stdout.flush()
    with open(out_json, "w") as f:
        json.dump(rows, f, indent=1)
    print("TOTAL %.2fs -> %s" % (time.time() - t_all, out_json))
    return rows


if __name__ == "__main__":
    assert run_gate(), "GATE FAILED"
    print()
    pairs = [(m, s) for s in (2, 3, 4) for m in range(4, 13) if s <= m - 1]
    here = os.path.dirname(os.path.abspath(__file__))
    rows = run_grid(pairs, os.path.join(here, "grid.json"))
    print()
    nneg = sum(1 for r in rows if r["negative_a"])
    nrob = sum(1 for r in rows if r["robust_negative_a"])
    print("rows with some Delta^(a) < 0            : %d / %d" % (nneg, len(rows)))
    print("rows with a gauge-INDEPENDENT negative  : %d / %d" % (nrob, len(rows)))
