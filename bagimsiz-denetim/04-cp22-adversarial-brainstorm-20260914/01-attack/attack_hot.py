"""Task 1: hot window m=19..24, s=2,3,4. Exact ratios for intervals with L>0 endpoints.
Trajectory computed once per m with numpy exact integer arithmetic; all claimed
numbers are int / Fraction. Run: python3 attack_hot.py
Outputs: attack_hot_results.json
"""
import sys, json, time
sys.path.insert(0, "/home/mdp/muse-work/cp22-attack")
from fractions import Fraction
from math import comb
import numpy as np
from attack_engine import (
    J_of, Ecal_of, transfer_of, L_terms_of, M_terms_of,
    demand_of, supply_radius2,
)

MS = list(range(19, 25))
SS = [2, 3, 4]


def trajectory(m):
    """Return (karr, xfin) for all odd h<2^m. Exact int64 arithmetic."""
    t0 = time.time()
    N = 1 << (m - 1)
    x = np.arange(1, 1 << m, 2, dtype=np.int64)
    k = np.zeros(N, dtype=np.int64)
    for _ in range(m):
        odd = x & 1
        k += odd
        x = np.where(odd.astype(bool), (3 * x + 1) // 2, x // 2)
    dt = time.time() - t0
    print(f"  traj m={m} N={N} done in {dt:.1f}s", flush=True)
    return k, x


def hist_from_traj(k, xfin, m, r):
    R = 1 << r
    z = (xfin & (R - 1)).astype(np.int64)
    res = {}
    for kk in range(1, m + 1):
        sel = z[k == kk]
        bc = np.bincount(sel, minlength=R)
        assert int(bc.sum()) == comb(m - 1, kk - 1), (m, kk, r)
        res[kk] = [int(v) for v in bc]
    return res


def main():
    t_all = time.time()
    # histograms: hi[m][r], need r sets
    HISTS = {}
    for m in range(19, 26):
        k, xfin = trajectory(m)
        if m == 19:
            rs = [3, 4, 5]
        elif m == 25:
            rs = [2, 3, 4]
        else:
            rs = [2, 3, 4, 5]
        HISTS[m] = {}
        for r in rs:
            HISTS[m][r] = hist_from_traj(k, xfin, m, r)
        del k, xfin

    rows = []
    global_min = None  # (ratio, m, s, a, b, demand, supply)
    for m in MS:
        for s in SS:
            hist_hi = HISTS[m][s + 1]
            hist_out = HISTS[m + 1][s]
            I = Ecal_of(hist_hi, m, s + 1)
            Out = Ecal_of(hist_out, m + 1, s)
            F = Fraction(0)
            for kk in range(1, m + 1):
                nk = comb(m - 1, kk - 1)
                E, O = transfer_of(hist_hi[kk], kk, s)
                F += (J_of(E, s) + J_of(O, s)) / nk
            L = F - I
            Lterms = L_terms_of(hist_hi, m, s)
            Mterms = M_terms_of(hist_hi, m, s)
            Mm = sum((Mterms[j] for j in range(2, m + 1)), Fraction(0))
            assert Mm == F - Out, (m, s)
            assert sum(Lterms.values(), Fraction(0)) == L, (m, s)
            # ratio table over intervals with L>0 at both endpoints
            table = []
            for a in range(1, m + 1):
                if not (Lterms[a] > 0):
                    continue
                for b in range(a, m + 1):
                    if not (Lterms[b] > 0):
                        continue
                    dem = demand_of(Lterms, a, b)
                    assert dem > 0
                    lo = max(a - 1, 2)
                    hi = min(b + 2, m)
                    sup = sum((Mterms[j] for j in range(lo, hi + 1)), Fraction(0)) if lo <= hi else Fraction(0)
                    ratio = sup / dem
                    table.append(dict(a=a, b=b, demand=str(dem), supply=str(sup), ratio=str(ratio)))
                    if global_min is None or ratio < global_min[0]:
                        global_min = (ratio, m, s, a, b, dem, sup)
            # tightest in this row
            row_min = min(table, key=lambda e: Fraction(e["ratio"])) if table else None
            print(f"(m={m},s={s}) L={L} M={Mm} defect={I-Out} npos={sum(1 for v in Lterms.values() if v>0)} "
                  f"row_min={row_min}", flush=True)
            rows.append(dict(m=m, s=s, I=str(I), F=str(F), Out=str(Out), L=str(L), M=str(Mm),
                             defect=str(I - Out),
                             Lterms={str(kk): str(v) for kk, v in Lterms.items()},
                             Mterms={str(j): str(v) for j, v in Mterms.items()},
                             ratio_table=table,
                             row_min=row_min))
    print(f"GLOBAL MIN: ratio={global_min[0]} at (m={global_min[1]},s={global_min[2]}) "
          f"[{global_min[3]},{global_min[4]}] demand={global_min[5]} supply={global_min[6]}", flush=True)
    print(f"total {time.time()-t_all:.1f}s", flush=True)
    out = dict(rows=rows,
               global_min=dict(ratio=str(global_min[0]), m=global_min[1], s=global_min[2],
                               a=global_min[3], b=global_min[4], demand=str(global_min[5]),
                               supply=str(global_min[6])))
    with open("/home/mdp/muse-work/cp22-attack/attack_hot_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote /home/mdp/muse-work/cp22-attack/attack_hot_results.json", flush=True)


if __name__ == "__main__":
    main()
