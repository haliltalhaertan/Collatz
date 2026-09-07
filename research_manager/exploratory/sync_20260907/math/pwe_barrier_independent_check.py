import json
import math
from itertools import accumulate
from pathlib import Path

ALPHA = math.log2(3.0)
BETA = ALPHA - 1.0
RHO = BETA / ALPHA
HERE = Path(__file__).resolve().parent


def ncrit(r):
    return math.floor(BETA * r) - 8


def phase(modulus, exponent):
    residue = pow(2, exponent, modulus)
    return complex(math.cos(2 * math.pi * residue / modulus),
                   math.sin(2 * math.pi * residue / modulus))


def h_value(r, j):
    m = r - 4
    k = ncrit(r) - j
    if k < 0:
        raise ValueError("infeasible H")
    v = [0j] * (k + 1)
    v[0] = 1 + 0j
    for s in range(1, m + 1):
        mod = 3 ** (s + 4)
        for ysum in range(k + 1):
            v[ysum] *= phase(mod, j + s - 1 + ysum)
        v = list(accumulate(v))
    return v[k] / math.comb(k + m - 1, m - 1)


def cap_for(s, threshold):
    # delta_s = S_(s-1) - beta*s - 5 <= threshold.
    return math.floor(BETA * s + 5 + threshold + 1e-12)


def g_value(r, threshold=None):
    n = ncrit(r)
    v = [0j] * (n + 1)
    v[0] = 1 + 0j
    counts = [0] * (n + 1)
    counts[0] = 1
    for s in range(1, r + 1):
        cap = n if threshold is None else min(n, cap_for(s, threshold))
        if cap < 0:
            return 0j, 0
        mod = 16 * 3 ** s
        for ysum in range(cap + 1):
            v[ysum] *= phase(mod, s - 1 + ysum)
        if cap < n:
            v[cap + 1:] = [0j] * (n - cap)
            counts[cap + 1:] = [0] * (n - cap)
        v = list(accumulate(v))
        counts = list(accumulate(counts))
    total = math.comb(n + r - 1, r - 1)
    return v[n] / total, counts[n]


def main():
    result = {"classification": "NUM", "pwe": [], "barrier": []}
    delta = 0.5
    for r in (30, 40, 50, 60):
        n = ncrit(r)
        cutoff = math.ceil(4 * (1 + delta) * math.log(r) / abs(math.log(RHO)))
        end = min(n, cutoff)
        hs = [abs(h_value(r, j)) for j in range(end + 1)]
        increases = [{"from_j": j, "to_j": j + 1, "from": hs[j], "to": hs[j + 1]}
                     for j in range(end) if hs[j + 1] > hs[j] + 1e-13]
        argmax = max(range(end + 1), key=lambda j: hs[j])
        result["pwe"].append({"r": r, "n": n, "L": cutoff, "j_end": end,
                              "abs_h0": hs[0], "argmax": argmax,
                              "max_over_h0": hs[argmax] / hs[0],
                              "adjacent_increases": increases})
    for r in (30, 60, 100):
        full, _ = g_value(r)
        total = math.comb(ncrit(r) + r - 1, r - 1)
        for threshold in (-4, 0):
            inside, count = g_value(r, threshold)
            outside = full - inside
            result["barrier"].append({"r": r, "T": threshold,
                                      "probability": count / total,
                                      "abs_full": abs(full),
                                      "abs_inside": abs(inside),
                                      "abs_outside": abs(outside),
                                      "inside_over_probability":
                                          abs(inside) / (count / total) if count else None})
    out = HERE / "PWE_BARRIER_CHECK_RESULTS.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
