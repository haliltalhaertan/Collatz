"""
STEP 5 -- refined provable bounds + the precise obstruction.

BOUND FAMILY (all [PROOF], see proof document):
  W(k,r,s) = 2*3^(s-1) * ( floor((3^k-2)/(2^r*3^s)) + 1 )     s = 0..k
             (s=0 term: W = floor((3^k-2)/2^r)+1 , no 3-adic split)
  cap(m,k,r) <= min_s W(k,r,s) * M(m,k)
  M(m,k)     <= MB(m,k) := min( n_k,
                                floor(2^(m-k)(3^(k-1)-2^(k-1))/3^k) + 1,
                                Top_s(m,k) for s=1,2,3 )
  Top_s(m,k) = max_{c mod 3^s} #{ w : sigma_s(w) = c mod 3^s },
               sigma_s(w) = sum_{j>k-s} 3^(k-j) 2^(i_j)   (top s positions only)

Also tests the two REFUTATIONS:
  R1: cap(m,k,r) <= 2^(m-r) is FALSE  (find explicit counterexamples)
  R2: cap(m,k,r) <= C absolute constant is FALSE (M(m,k) unbounded)
and measures the square-root obstruction  M ~ 2^((m-k)/2).
"""
import sys, json, statistics
from math import comb
from itertools import combinations
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\cap-proof")
from collatz_cap_core import *

OUT = r"C:\Users\MDP\collatz-analysis\cap-proof"
Mtab = {k: v for k, v in json.load(open(OUT + r"\M_table.json")).items()}
captab = json.load(open(OUT + r"\cap_table.json"))

cnt, fail = {}, {}
def chk(tag, ok, info=None):
    cnt[tag] = cnt.get(tag, 0) + 1
    if not ok:
        fail.setdefault(tag, []).append(info)

# ------------------------------------------------------------------ Top_s
def Top_s(m, k, s):
    """max over c mod 3^s of #{w in W_{m,k}: sigma_s(w) = c mod 3^s}.
    sigma_s depends only on the top s 1-positions; lower positions counted
    by a binomial.  Valid for any m (no enumeration of W_{m,k})."""
    if s < 1 or s > k:
        return comb(m - 1, k - 1)
    mod = 3 ** s
    acc = {}
    # choose top s positions  i_{k-s+1} < ... < i_k  in [0, m-1]
    for T in combinations(range(m), s):
        lo = T[0]
        # remaining k-s positions strictly below lo, must include 0
        if k - s == 0:
            if lo != 0:
                continue
            ways = 1
        else:
            # positions 0 and (k-s-1) more from {1..lo-1}
            if lo < 1:
                continue
            ways = comb(lo - 1, k - s - 1)
        if ways == 0:
            continue
        sig = sum(pow(3, s - 1 - j) * (1 << T[j]) for j in range(s)) % mod
        acc[sig] = acc.get(sig, 0) + ways
    return max(acc.values()) if acc else 0

# validate Top_s against brute force (it must be an UPPER bound on M, and
# Top_k must EQUAL M)
print("=== validating Top_s ===")
for m in range(2, 13):
    for k in range(1, m + 1):
        M = Mtab[f"{m},{k}"]
        for s in range(1, k + 1):
            t = Top_s(m, k, s)
            chk("Top_upper", M <= t, (m, k, s, M, t))
        chk("Top_exact_at_k", Top_s(m, k, k) == M, (m, k, Top_s(m, k, k), M))
        # cross-check total mass
        chk("Top_mass", sum(1 for _ in words(m, k)) == comb(m - 1, k - 1))
print("  Top_upper checks:", cnt.get("Top_upper"), "fails:", len(fail.get("Top_upper", [])))
print("  Top_exact_at_k checks:", cnt.get("Top_exact_at_k"), "fails:", len(fail.get("Top_exact_at_k", [])))
if fail.get("Top_exact_at_k"):
    print("   sample:", fail["Top_exact_at_k"][:5])

# ------------------------------------------------------------------ MB
def MB(m, k, smax=3):
    nk = comb(m - 1, k - 1)
    b_int = (1 << (m - k)) * (3 ** (k - 1) - 2 ** (k - 1)) // 3 ** k + 1
    b = min(nk, b_int)
    for s in range(1, min(smax, k) + 1):
        b = min(b, Top_s(m, k, s))
    return b

vM = 0; ratM = []
for key, M in Mtab.items():
    m, k = map(int, key.split(","))
    b = MB(m, k)
    if M > b:
        vM += 1; print("  MB VIOLATION", m, k, M, b)
    ratM.append((b / M, m, k, M, b))
print()
print("MB-bound on M: cases=%d violations=%d" % (len(Mtab), vM))
ratM.sort()
print("  tightness bound/actual: min %.2f median %.2f max %.1f"
      % (ratM[0][0], statistics.median(x[0] for x in ratM), ratM[-1][0]))
print("  exact (ratio 1.0) in %d cells" % sum(1 for x in ratM if x[0] == 1.0))
print("  worst cell (m,k,M,bound):", ratM[-1][1:])

# ------------------------------------------------------------------ window
def W(k, r, s):
    if s == 0:
        return (3 ** k - 2) // (1 << r) + 1
    return 2 * 3 ** (s - 1) * ((3 ** k - 2) // ((1 << r) * 3 ** s) + 1)

def capbnd(m, k, r):
    nk = comb(m - 1, k - 1)
    w = min(W(k, r, s) for s in range(0, k + 1))
    return min(nk, w * MB(m, k))

vC = 0; rows = []
for key, c in captab.items():
    m, k, r = map(int, key.split(","))
    b = capbnd(m, k, r)
    nk = comb(m - 1, k - 1)
    if c > b:
        vC += 1; print("  CAP VIOLATION", m, k, r, c, b)
    rows.append((m, k, r, c, nk, b, b / c, b < nk))
print()
print("FINAL cap-bound: cases=%d violations=%d" % (len(rows), vC))
nt = [x for x in rows if x[7]]
print("  strictly beats trivial n_k in %d/%d cells (%.0f%%)"
      % (len(nt), len(rows), 100 * len(nt) / len(rows)))
if nt:
    rr = sorted(nt, key=lambda x: x[6])
    print("  tightness on those: min %.2f median %.2f max %.1f"
          % (rr[0][6], statistics.median(x[6] for x in nt), rr[-1][6]))
    print("  tightest (m,k,r,actual)=%s bound=%d" % (rr[0][:4], rr[0][5]))
    print("  loosest  (m,k,r,actual)=%s bound=%d" % (rr[-1][:4], rr[-1][5]))
st = [x for x in rows if (1 << x[2]) >= 3 ** x[1] - 1]
print("  stabilised regime (2^r>=3^k-1): %d cells, tightness min %.2f median %.2f max %.1f"
      % (len(st), min(x[6] for x in st), statistics.median(x[6] for x in st),
         max(x[6] for x in st)))
ex = [x for x in st if x[6] == 1.0]
print("  EXACT (bound==actual) in %d of the %d stabilised cells" % (len(ex), len(st)))

# ------------------------------------------------------------------ R1, R2
print()
print("=== REFUTATIONS ===")
ce1 = [(m, k, r, c) for key, c in captab.items()
       for m, k, r in [tuple(map(int, key.split(",")))]
       if c > max(1, 2 ** (m - r)) or (m - r < 0 and c > 1)]
ce1b = []
for key, c in captab.items():
    m, k, r = map(int, key.split(","))
    b = 2 ** (m - r) if m >= r else 0
    if c > b:
        ce1b.append((m, k, r, c, b))
print("R1: cap <= 2^(m-r) is FALSE. counterexamples:", len(ce1b))
for x in ce1b[:8]:
    print("    (m,k,r)=%s cap=%d  2^(m-r)=%s" % (x[:3], x[3], x[4]))
print("R2: cap bounded by absolute constant is FALSE; M(m,k) attains",
      max(Mtab.values()), "at",
      [k for k, v in Mtab.items() if v == max(Mtab.values())])

# ------------------------------------------------------------------ obstruction
print()
print("=== OBSTRUCTION: interval bound vs truth (square-root gap) ===")
print(" m-k |  max_m M | 2^(m-k)/3 | 2^((m-k)/2) | ratio provable/true")
for d in range(4, 20):
    vals = [v for key, v in Mtab.items()
            if int(key.split(",")[0]) - int(key.split(",")[1]) == d]
    if not vals:
        continue
    Mx = max(vals)
    prov = (1 << d) // 3 + 1
    sq = int(2 ** (d / 2))
    print(f" {d:3d} | {Mx:8d} | {prov:9d} | {sq:11d} | {prov/Mx:8.1f}")

json.dump({"counts": cnt, "fails": {k: len(v) for k, v in fail.items()}},
          open(OUT + r"\step5_verification.json", "w"))
print()
print("TOTAL step5 exact checks:", sum(cnt.values()),
      " failures:", sum(len(v) for v in fail.values()))
