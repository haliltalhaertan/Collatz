"""CP28 PBM exact check (finite evidence, NOT a proof).

For every odd x in [2^m, 2^(m+1)): Syracuse U(x)=(3x+1)/2^a, a=v2(3x+1),
S_j = a_0+...+a_{j-1}, tau = min{j : S_j > m}.  Over the post-budget block
i in [tau, tau+L), L=floor(delta*m), count a_i == k.
PBM predicts: frequency -> 2^-k, and block distribution -> iid Geom(1/2).
Exact integer arithmetic (numpy uint64; m<=24 keeps values < 2^63).
"""
import json, sys
import numpy as np

def run(m, delta=0.25, kmax=4):
    L = max(1, int(delta * m))
    x = np.arange((1 << m) + 1, 1 << (m + 1), 2, dtype=np.uint64)
    n = len(x)
    s = np.zeros(n, np.int64); j = np.zeros(n, np.int64)
    tau = np.full(n, -1, np.int64)
    cnt = np.zeros((n, kmax + 1), np.int64)   # col kmax = "a >= kmax"
    tot = np.zeros(n, np.int64)
    alive = np.ones(n, bool)
    while alive.any():
        ids = np.flatnonzero(alive)
        v = 3 * x[ids] + np.uint64(1)
        a = np.zeros(len(ids), np.int64)
        ev = (v & np.uint64(1)) == 0
        while ev.any():
            v[ev] >>= np.uint64(1); a[ev] += 1
            ev = (v & np.uint64(1)) == 0
        t = tau[ids]
        inblk = (t >= 0) & (j[ids] >= t) & (j[ids] < t + L)
        ii = ids[inblk]; aa = np.minimum(a[inblk], kmax)
        np.add.at(cnt, (ii, aa), 1); tot[ii] += a[inblk]
        s[ids] += a; j[ids] += 1; x[ids] = v
        newt = (t < 0) & (s[ids] > m)
        tau[ids[newt]] = j[ids[newt]]
        t = tau[ids]
        alive[ids] = (t < 0) | (j[ids] < t + L)
    freq = cnt[:, 1:].sum(0) / (n * L)
    ideal = [2.0 ** -k for k in range(1, kmax)] + [2.0 ** -(kmax - 1)]
    # TV of block sum sum(a_i) vs NegBin(L, 1/2) shifted (sum of L iid Geom>=1)
    from math import comb
    hist = np.bincount(tot); smax = len(hist) - 1
    pmf = np.array([comb(sv - 1, L - 1) * 0.5 ** sv if sv >= L else 0.0
                    for sv in range(smax + 1)])
    tv = 0.5 * (np.abs(hist / n - pmf).sum() + max(0.0, 1 - pmf.sum()))
    return {"m": m, "N": int(n), "L": L,
            "freq_a=1,2,3,>=4": [round(float(f), 6) for f in freq],
            "ideal": ideal, "TV_blocksum": round(float(tv), 6)}

if __name__ == "__main__":
    ms = [int(a) for a in sys.argv[1:]] or [14, 16, 18, 20, 22]
    out = [run(m) for m in ms]
    for r in out: print(json.dumps(r))
    json.dump(out, open("cp28_pbm_check.json", "w", newline="\n"), indent=1)
