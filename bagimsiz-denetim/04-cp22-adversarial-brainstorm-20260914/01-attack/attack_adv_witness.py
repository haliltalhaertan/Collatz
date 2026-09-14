"""Task 3b: persist + independently verify a caps+supports-respecting radius-2 violator.
Independent verification uses attack_engine (separate code path) and checks:
masses, caps, supports, exact gap>0, and minimal violating intervals.
Run: python3 attack_adv_witness.py -> attack_witness.json
"""
import sys, json, random
sys.path.insert(0, "/home/mdp/muse-work/cp22-attack")
from fractions import Fraction
from math import comb
import attack_adv as A
import attack_engine as E


def verify_witness(Ph, n, m, s, caps, allowed, a, b):
    N = 1 << (s + 1)
    # 1. masses / caps / supports
    for k in range(1, m + 1):
        assert sum(Ph[k]) == n[k], (k, sum(Ph[k]), n[k])
        assert max(Ph[k]) <= caps[k], (k, max(Ph[k]), caps[k])
        for z in range(N):
            if Ph[k][z] != 0:
                assert z in allowed[k], (k, z)
        assert all(v >= 0 and v == int(v) for v in Ph[k]), k
    # 2. independent gap via attack_engine primitives
    L = E.L_terms_of({k: list(Ph[k]) for k in Ph}, m, s)
    M = E.M_terms_of({k: list(Ph[k]) for k in Ph}, m, s)
    dem = E.demand_of(L, a, b)
    sup = E.supply_radius2(M, m, a, b)
    gap = dem - sup
    # 3. all radius-2 violations (any [x,y]) + minimal ones with L>0 endpoints
    bad = E.charging_violations_r2(L, M, m)
    return gap, dem, sup, L, M, bad


def main():
    m, s, a, b = 20, 3, 14, 16
    seed = 777
    rng = random.Random(seed)
    karr, xfin = A.trajectory(m)
    hist = A.hist_from_traj(karr, xfin, m, s + 1)
    del karr, xfin
    n = {k: comb(m - 1, k - 1) for k in range(1, m + 1)}
    N = 1 << (s + 1)
    caps = {k: max(hist[k]) for k in range(1, m + 1)}
    allowed = {k: set(z for z in range(N) if hist[k][z] > 0) for k in range(1, m + 1)}
    g0, dem0, sup0, _ = A.gap_of(hist, n, m, s, a, b)
    print(f"TRUE gap[{a},{b}] = {g0}")
    # targeted search (weak, lo=0), relevant strata only, more steps
    init = {k: list(hist[k]) for k in range(1, m + 1)}
    best, Ph = A.hill_climb(init, n, m, s, a, b, allowed, caps, 0, 12000, rng)
    print(f"hill-climb best gap = {best}")
    gap, dem, sup, L, M, bad = verify_witness(Ph, n, m, s, caps, allowed, a, b)
    print(f"INDEPENDENT verify: gap={gap} dem={dem} sup={sup}")
    assert gap == best, (gap, best)
    print(f"number of violating intervals (all [x,y]): {len(bad)}")
    for (x, y, d, su) in bad[:12]:
        print(f"  [{x},{y}] dem={d} sup={su} gap={d-su} Lx>0:{L[x]>0} Ly>0:{L[y]>0}")
    # minimal violating intervals with positive endpoints
    pos = [t for t in bad if L[t[0]] > 0 and L[t[1]] > 0]
    print(f"violations with L>0 at both endpoints: {len(pos)}")
    for (x, y, d, su) in pos[:12]:
        print(f"  [{x},{y}] dem={d} sup={su} gap={d-su}")
    assert gap > 0 and len(bad) > 0, "no violation to report"
    # save witness (only strata 1..m arrays; small)
    with open("/home/mdp/muse-work/cp22-attack/attack_witness.json", "w") as f:
        json.dump(dict(m=m, s=s, a=a, b=b, gap=str(gap), dem=str(dem), sup=str(sup),
                       caps={str(k): caps[k] for k in caps},
                       Ph={str(k): list(Ph[k]) for k in Ph},
                       truePh={str(k): list(hist[k]) for k in hist},
                       violations=[[x, y, str(d), str(su)] for (x, y, d, su) in bad],
                       L={str(k): str(v) for k, v in L.items()},
                       M={str(j): str(v) for j, v in M.items()}), f)
    print("wrote /home/mdp/muse-work/cp22-attack/attack_witness.json")
    print(f"WITNESS_VERIFIED actor gap={gap} (>0: {gap > 0})")


if __name__ == "__main__":
    main()
