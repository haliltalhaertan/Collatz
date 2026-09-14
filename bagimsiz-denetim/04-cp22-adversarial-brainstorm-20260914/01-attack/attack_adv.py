"""Task 3: adversarial family respecting real caps + supports.
Target: hot interval (20,3)[14,16] (radius-2) and sanity (18,2)[14,14] (radius-2).
Constraints per stratum k on Z/N: sum P = n_k; P[z] = 0 outside true support;
0 <= P[z] <= cap_k (weak) or 1 <= P[z] <= cap_k on true support (strong/full-use).
Objective: gap G = demand([a,b]) - supply(window) with demand=sum max(L,0),
supply = sum M over radius-2 window. Violation iff G > 0.
Method: exact-integer multi-restart single-unit hill-climbing (int arithmetic for
C/J; Fraction only for final gaps). Failure to find G>0 is HEURISTIC, not proof.
Run: python3 attack_adv.py -> attack_adv_results.json
"""
import sys, json, random, time
sys.path.insert(0, "/home/mdp/muse-work/cp22-attack")
from fractions import Fraction
from math import comb
import numpy as np

OWN_SEED = 20260914


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
    return {kk: [int(v) for v in np.bincount(z[k == kk], minlength=R)] for kk in range(1, m + 1)}


def Lk_of(P, k, nk, s):
    N = 1 << (s + 1)
    q = 1 << s
    c = pow(3, k, N)
    c1 = sum(P[u] * P[(u + c) % N] for u in range(N))
    c2 = sum(P[u] * P[(u + c + q) % N] for u in range(N))
    return Fraction(q * (c1 - c2), nk)


def transfer_of(P, k, s):
    N = 1 << (s + 1)
    q = 1 << s
    ck = pow(3, k, N)
    rinv = pow(3, -1, N)
    E = [P[(2 * z) % N] + P[(2 * z - ck) % N] for z in range(q)]
    O = [P[(rinv * (2 * z - 1)) % N] + P[(rinv * (2 * z - 1) - ck) % N] for z in range(q)]
    return E, O


def Jint(X, s):
    half = 1 << (s - 1)
    return (1 << (s - 1)) * sum((X[u] - X[u + half]) ** 2 for u in range(half))


def Mj_of(Ph, j, n, s):
    Ej, _ = transfer_of(Ph[j], j, s)
    _, Oj1 = transfer_of(Ph[j - 1], j - 1, s)
    D = [n[j - 1] * a - n[j] * b for a, b in zip(Ej, Oj1)]
    return Fraction(Jint(D, s), n[j] * n[j - 1] * (n[j] + n[j - 1]))


def gap_of(Ph, n, m, s, a, b):
    L = {k: Lk_of(Ph[k], k, n[k], s) for k in range(1, m + 1)}
    dem = sum((v for k, v in L.items() if a <= k <= b and v > 0), Fraction(0))
    lo = max(a - 1, 2)
    hi = min(b + 2, m)
    sup = sum((Mj_of(Ph, j, n, s) for j in range(lo, hi + 1)), Fraction(0))
    return dem - sup, dem, sup, L


def support_cap_report(m, s):
    karr, xfin = trajectory(m)
    hist = hist_from_traj(karr, xfin, m, s + 1)
    del karr, xfin
    N = 1 << (s + 1)
    print(f"--- caps/supports (m={m},s={s}) N={N} ---")
    info = {}
    for kk in range(1, m + 1):
        P = hist[kk]
        nk = comb(m - 1, kk - 1)
        cap = max(P)
        supp = [z for z in range(N) if P[z] > 0]
        slack = N * cap - nk
        forced_min = nk - (N - 1) * cap
        info[kk] = dict(n=nk, cap=cap, supp=supp, slack=slack, minbin=min(P),
                        forced_min=forced_min, P=P)
        if 10 <= kk <= 19:
            print(f" k={kk} n={nk} cap={cap} |supp|={len(supp)}/{N} slack={slack} "
                  f"min={min(P)} forced_min={forced_min} max/mean={Fraction(cap*N, nk)}")
    return hist, info


def flat_init(nk, N, cap, allowed, rng):
    P = [0] * N
    base, rem = divmod(nk, N)
    assert base + (1 if rem else 0) <= cap, "infeasible"
    order = list(range(N))
    rng.shuffle(order)
    for i, z in enumerate(order):
        P[z] = base + (1 if i < rem else 0)
    return P


def random_feasible_init(nk, N, cap, allowed, rng, lo):
    P = [0] * N
    # start flat on allowed bins (assumes allowed == all when full support)
    assert set(allowed) == set(range(N)), "only full-support case randomized here"
    P = flat_init(nk, N, cap, allowed, rng)
    # random walk
    for _ in range(5 * N):
        u = rng.randrange(N)
        v = rng.randrange(N)
        if u == v or P[u] <= lo or P[v] >= cap:
            continue
        P[u] -= 1
        P[v] += 1
    return P


def hill_climb(Ph0, n, m, s, a, b, allowed, caps, lo, steps, rng, verbose=False):
    Ph = {k: list(v) for k, v in Ph0.items()}
    N = 1 << (s + 1)
    lo_w = max(a - 1, 2)
    hi_w = min(b + 2, m)
    relevant = set(range(a, b + 1)) | set(range(lo_w - 1, hi_w + 1))
    relevant = {k for k in relevant if 1 <= k <= m}
    g, dem, sup, _ = gap_of(Ph, n, m, s, a, b)
    best = g
    for t in range(steps):
        k = rng.choice(sorted(relevant))
        u = rng.randrange(N)
        v = rng.randrange(N)
        if u == v or u not in allowed[k] or v not in allowed[k]:
            continue
        if Ph[k][u] <= lo or Ph[k][v] >= caps[k]:
            continue
        Ph[k][u] -= 1
        Ph[k][v] += 1
        g2, dem2, sup2, _ = gap_of(Ph, n, m, s, a, b)
        if g2 > g:
            g, dem, sup = g2, dem2, sup2
            if g > best:
                best = g
        else:
            Ph[k][u] += 1
            Ph[k][v] -= 1
    return best, Ph


def attack_row(m, s, a, b, restarts=8, steps=6000, seed=OWN_SEED):
    rng = random.Random(seed)
    hist, info = support_cap_report(m, s)
    n = {k: comb(m - 1, k - 1) for k in range(1, m + 1)}
    N = 1 << (s + 1)
    caps = {k: info[k]["cap"] for k in range(1, m + 1)}
    allowed = {k: set(info[k]["supp"]) for k in range(1, m + 1)}
    g0, dem0, sup0, L0 = gap_of(hist, n, m, s, a, b)
    print(f"TRUE gap[{a},{b}] = {g0} (dem={dem0} sup={sup0})")
    results = {}
    for variant, lo in [("weak", 0), ("strong", 1)]:
        # feasibility of strong: every allowed bin >= 1 requires n_k >= |supp|
        feas = all(n[k] >= len(allowed[k]) for k in range(1, m + 1))
        if lo == 1 and not feas:
            print(f" variant {variant}: infeasible, skipped")
            continue
        best_overall = g0
        best_Ph = None
        for ri in range(restarts):
            if ri == 0:
                init = {k: list(hist[k]) for k in range(1, m + 1)}
            elif ri == 1:
                init = {k: (flat_init(n[k], N, caps[k], allowed[k], rng) if set(allowed[k]) == set(range(N)) else list(hist[k])) for k in range(1, m + 1)}
            else:
                init = {}
                for k in range(1, m + 1):
                    if set(allowed[k]) == set(range(N)):
                        init[k] = random_feasible_init(n[k], N, caps[k], allowed[k], rng, lo)
                    else:
                        init[k] = list(hist[k])
                # enforce lo on inits
                for k in range(1, m + 1):
                    for z in allowed[k]:
                        if init[k][z] < lo:
                            # take from a donor bin
                            for w in allowed[k]:
                                if init[k][w] > lo:
                                    init[k][w] -= 1
                                    init[k][z] += 1
                                    break
            bg, bPh = hill_climb(init, n, m, s, a, b, allowed, caps, lo, steps, rng)
            tag = "true" if ri == 0 else ("flat" if ri == 1 else f"rand{ri}")
            print(f" variant={variant} restart={tag}: best gap = {bg} {'> VIOLATION <' if bg > 0 else ''}")
            if bg > best_overall:
                best_overall = bg
                best_Ph = bPh
        results[variant] = str(best_overall)
        print(f"==> ({m},{s})[{a},{b}] variant={variant}: TRUE gap={g0}, ADV best={best_overall}")
    return dict(m=m, s=s, a=a, b=b, true_gap=str(g0), best=results)


def single_stratum_maxL(m, s, ks, seed=OWN_SEED):
    """Max L_k under cap+support per stratum independently (hill-climb, heuristic)."""
    rng = random.Random(seed + 999)
    hist, info = support_cap_report(m, s) if False else (None, None)
    # reuse trajectory once
    karr, xfin = trajectory(m)
    hist = hist_from_traj(karr, xfin, m, s + 1)
    del karr, xfin
    N = 1 << (s + 1)
    out = {}
    for kk in ks:
        nk = comb(m - 1, kk - 1)
        cap = max(hist[kk])
        trueL = Lk_of(hist[kk], kk, nk, s)
        best = trueL
        for ri in range(6):
            P = list(hist[kk]) if ri == 0 else flat_init(nk, N, cap, set(range(N)), rng)
            if ri >= 2:
                for _ in range(5 * N):
                    u = rng.randrange(N)
                    v = rng.randrange(N)
                    if u != v and P[u] > 0 and P[v] < cap:
                        P[u] -= 1
                        P[v] += 1
            cur = Lk_of(P, kk, nk, s)
            for _ in range(4000):
                u = rng.randrange(N)
                v = rng.randrange(N)
                if u == v or P[u] <= 0 or P[v] >= cap:
                    continue
                P[u] -= 1
                P[v] += 1
                nl = Lk_of(P, kk, nk, s)
                if nl > cur:
                    cur = nl
                else:
                    P[u] += 1
                    P[v] -= 1
            if cur > best:
                best = cur
        out[kk] = dict(true=str(trueL), maxfound=str(best))
        print(f" k={kk}: true L={trueL}, maxfound L={best}")
    return out


def main():
    t0 = time.time()
    res = {}
    res["hot203"] = attack_row(20, 3, 14, 16, restarts=8, steps=6000)
    res["sanity182"] = attack_row(18, 2, 14, 14, restarts=6, steps=4000)
    print("--- single-stratum L maxima (20,3) k=12..18 ---")
    res["singleL203"] = single_stratum_maxL(20, 3, list(range(12, 19)))
    print("--- single-stratum L maxima (18,2) k=12..17 ---")
    res["singleL182"] = single_stratum_maxL(18, 2, list(range(12, 18)))
    res["secs"] = time.time() - t0
    with open("/home/mdp/muse-work/cp22-attack/attack_adv_results.json", "w") as f:
        json.dump(res, f, indent=1)
    print(f"wrote attack_adv_results.json in {res['secs']:.1f}s")


if __name__ == "__main__":
    main()
