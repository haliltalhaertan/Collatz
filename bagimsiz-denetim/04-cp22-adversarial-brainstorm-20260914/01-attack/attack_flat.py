"""Task 2: flat/spiky mechanism in the hot window. Exact arithmetic only (int/Fraction).
For selected hot rows, per stratum k: cap, mean (Fraction), max/mean (Fraction),
variance numerator V = sum_z (N*P[z]-n_k)^2 (int, scale-free flatness),
and per merge link j: D_j = n_{j-1}E_j - n_j O_{j-1}, S_j = sum_z D[z]^2 (int),
J_j = J_s(D_j) (exact int), frac J/S (Fraction), max|D| (int), M_j (Fraction).
Also: bin-by-bin normalized gap G_j[z] = E_j[z]*n_{j-1} - O_{j-1}[z]*n_j = D_j[z],
reported via S_j and max|D| (exact).
Run: python3 attack_flat.py -> attack_flat_results.json
"""
import sys, json, time
sys.path.insert(0, "/home/mdp/muse-work/cp22-attack")
from fractions import Fraction
from math import comb
import numpy as np
from attack_engine import J_of, transfer_of, L_terms_of, M_terms_of


def trajectory(m):
    N = 1 << (m - 1)
    x = np.arange(1, 1 << m, 2, dtype=np.int64)
    k = np.zeros(N, dtype=np.int64)
    for _ in range(m):
        odd = x & 1
        k += odd
        x = np.where(odd.astype(bool), (3 * x + 1) // 2, x // 2)
    return k, x


def hist_from_traj(k, xfin, m, r):
    R = 1 << r
    z = (xfin & (R - 1)).astype(np.int64)
    res = {}
    for kk in range(1, m + 1):
        sel = z[k == kk]
        bc = np.bincount(sel, minlength=R)
        res[kk] = [int(v) for v in bc]
    return res


HOT = [(20, 3), (21, 3), (22, 3), (20, 2), (22, 2), (18, 2)]


def analyze(m, s):
    r = s + 1
    N = 1 << r
    q = 1 << s
    karr, xfin = trajectory(m)
    hist = hist_from_traj(karr, xfin, m, r)
    del karr, xfin
    n = {kk: comb(m - 1, kk - 1) for kk in range(1, m + 1)}
    L = L_terms_of(hist, m, s)
    M = M_terms_of(hist, m, s)
    strata = {}
    for kk in range(1, m + 1):
        P = hist[kk]
        cap = max(P)
        mean = Fraction(n[kk], N)
        maxmean = Fraction(cap * N, n[kk])  # cap/mean exact
        # variance numerator: sum (P[z]-mean)^2 = (sum (N*P[z]-n)^2)/N^2 ; report int numerator
        V = sum((N * v - n[kk]) ** 2 for v in P)
        # min/max bin
        strata[kk] = dict(n=n[kk], cap=cap, mean=str(mean), maxmean=str(maxmean),
                          varnum=V, min=min(P), hist=P, L=str(L[kk]))
    links = {}
    for j in range(2, m + 1):
        Ej, _ = transfer_of(hist[j], j, s)
        _, Oj1 = transfer_of(hist[j - 1], j - 1, s)
        D = [n[j - 1] * a - n[j] * b for a, b in zip(Ej, Oj1)]
        S = sum(v * v for v in D)
        J = int(J_of(D, s))  # J is integral (half * sum of squares of ints)
        maxabs = max(abs(v) for v in D)
        # normalized max gap per unit mass: maxabs/(n_j n_{j-1}) as Fraction
        links[j] = dict(M=str(M[j]), S=S, J=J, JoverS=str(Fraction(J, S)) if S else "undef",
                        maxabsD=maxabs,
                        maxgap=str(Fraction(maxabs, n[j] * n[j - 1])),
                        Ej=Ej, Oj1=Oj1, D=D)
    return dict(m=m, s=s, N=N, strata=strata, links=links,
                L={str(kk): str(v) for kk, v in L.items()},
                M={str(j): str(v) for j, v in M.items()})


def main():
    out = {}
    for (m, s) in HOT:
        t0 = time.time()
        print(f"analyzing ({m},{s})...", flush=True)
        out[f"{m},{s}"] = analyze(m, s)
        print(f"  done in {time.time()-t0:.1f}s", flush=True)
    with open("/home/mdp/muse-work/cp22-attack/attack_flat_results.json", "w") as f:
        # drop raw hist arrays? keep them (small). D arrays length<=8, fine.
        json.dump(out, f, indent=1)
    print("wrote /home/mdp/muse-work/cp22-attack/attack_flat_results.json")
    # console summary for hot k range
    for key in ["20,3", "21,3", "22,3", "20,2", "18,2"]:
        d = out[key]
        m, s = d["m"], d["s"]
        print(f"--- ({m},{s}) strata k=12..18: [k, n, cap, max/mean, varnum, L_k]")
        for kk in range(12, 19):
            if kk not in d["strata"]:
                continue
            st = d["strata"][kk]
            print(f"  k={kk} n={st['n']} cap={st['cap']} max/mean={st['maxmean']} V={st['varnum']} L={st['L']}")
        print(f"    links j=12..19: [j, M_j, S, J, J/S, max|D|]")
        for j in range(12, 20):
            if j not in d["links"]:
                continue
            li = d["links"][j]
            print(f"  j={j} M={li['M']} S={li['S']} J={li['J']} J/S={li['JoverS']} max|D|={li['maxabsD']}")


if __name__ == "__main__":
    main()
