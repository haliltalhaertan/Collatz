"""CP27 X-A corridor feasibility: constructive check (b=+1).
Claim: for any K, M with 2^M > 3^K and any q with K >= 2q, the block word below
has every proper block prefix strictly below the line (2^{E_t} < 3^{S_t}),
so the X-A corridor inequality Delta_t < t*log(1+1/X) holds trivially.
Also reports the rational cycle candidate's minimum (integer numerators / D).
"""
import json, math, sys, time

def fl(s):  # floor(s*log2 3) for s>=1 (exact)
    return (3**s).bit_length() - 1

def construct(K, M, q):
    base = K // q; s = [base] * q
    for i in range(K - base * q): s[i] += 1
    e = [fl(x) for x in s[:-1]]; e.append(M - sum(e))
    gaps = []
    for sj, ej in zip(s, e):
        d = ej - (sj - 1); assert d >= 2, (sj, ej)
        gaps += [1] * (sj - 1) + [d]
    return s, e, gaps

def check(K, M, q):
    s, e, g = construct(K, M, q)
    assert len(g) == K and sum(g) == M
    D = (1 << M) - 3**K; assert D > 0
    B = 0; A = 0
    for a in g: B = 3 * B + (1 << A); A += a
    X = B; mn = X; imn = 0
    for i, a in enumerate(g):
        num = 3 * X + D
        assert num % (1 << a) == 0
        X = num >> a
        if i + 1 < K and X < mn: mn, imn = X, i + 1
    assert X == B  # closes
    S = E = 0; below = True
    for t in range(q - 1):
        S += s[t]; E += e[t]
        if (1 << E) > 3**S: below = False
    return dict(K=K, M=M, q=q, all_proper_block_prefixes_below=below,
                global_min_index=imn, global_min_at_block0=(imn == 0),
                log2_nmin=round(math.log2(mn) - math.log2(D), 3) if mn else None,
                integral=(B % D == 0))

if __name__ == '__main__':
    out = []; t0 = time.time()
    for K in [306, 665, 1636, 3274, 15601]:
        M = (3**K).bit_length()
        for q in (92, 100, 120):
            if K >= 2 * q:
                out.append(check(K, M, q)); print(out[-1], flush=True)
    json.dump({'status': 'EXACT_COMPUTATION_NOT_PROOF', 'results': out,
               'seconds': round(time.time() - t0, 1)},
              open(sys.argv[1] if len(sys.argv) > 1 else 'cp27_xa_construct.json', 'w'), indent=1)
