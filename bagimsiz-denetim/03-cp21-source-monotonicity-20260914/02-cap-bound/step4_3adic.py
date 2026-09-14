"""
STEP 4 -- the 3-adic collision criterion and the final bounds.

T1 [PROOF] sharpened isometry: v2(h_w-h_w') = v2(B_w-B_w') = d(w,w')
T2 [PROOF] range lemma: 1 <= e_w <= 3^k - 1
T7 [PROOF] 3-ADIC EXACT-COLLISION CRITERION:
        e_w = e_w'   <==>   B_w = B_w'  (mod 3^k)
T7r [PROOF] general r:
        e_w = e_w' mod 2^r  <==>  exists t, |t| <= (3^k-2)/2^r,
                                  B_w - B_w' = 2^{m+r} t  (mod 3^k)
T8 [PROOF] top-position parity: e_w = e_w'  ==>  i_k = i_k'  (mod 2)
T4 [PROOF] B-spread / closeness:
        |B_w - B_w'| < 2^{m-q}(3^q - 2^q), q = k - p, p >= 1 = prefix weight
        ==> exact-collision class has h-diameter < 2^{m-k+1}(3^{k-1}-2^{k-1})/3^k
        ==> M(m,k) <= floor(2^{m-k}(3^{k-1}-2^{k-1})/3^k) + 1
T3 [PROOF] stabilisation: 2^r >= 3^k - 1 ==> cap(m,k,r) = M(m,k)
T5 [PROOF] FINAL BOUND
        cap(m,k,r) <= min( n_k, (floor((3^k-2)/2^r)+1) * Mbnd(m,k) )
        Mbnd(m,k)  = min( n_k, floor(2^{m-k}(3^{k-1}-2^{k-1})/3^k)+1, Par(m,k) )
        Par(m,k)   = max_eps sum_{i=eps mod 2, k-1<=i<=m-1} C(i-1,k-2)   (k>=2)
T6 [PROOF] parent identity:
        P_{m,k,r}(z) = Q_k(a) + Q_k(a-3^k) + Q_{k-1}(c) + Q_{k-1}(c-3^{k-1}),
        Q_j = P_{m-1,j,r+1},  a = 2z mod 2^{r+1},  c = 3^{-1}(2z-1) mod 2^{r+1}
        ==> cap(m,k,r) <= 2 cap(m-1,k,r+1) + 2 cap(m-1,k-1,r+1)
"""
import sys, json, statistics
from math import comb
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\cap-proof")
from collatz_cap_core import *

cnt, fail = {}, {}
def chk(tag, ok):
    cnt[tag] = cnt.get(tag, 0) + 1
    if not ok:
        fail[tag] = fail.get(tag, 0) + 1

# ---------------------------------------------------------------- T7 / T7r / T8
MM = 13
pairs = 0
for m in range(2, MM + 1):
    for k in range(1, m + 1):
        L = layer(m, k)
        if len(L) > 200:
            L = L[:200]
        pk = 3 ** k
        for a in range(len(L)):
            wa, Ba, ha, ea = L[a]
            ika = positions(wa)[-1]
            for b in range(a + 1, len(L)):
                wb, Bb, hb, eb = L[b]
                pairs += 1
                # T7
                chk("T7", (ea == eb) == ((Ba - Bb) % pk == 0))
                # T8
                if ea == eb:
                    ikb = positions(wb)[-1]
                    chk("T8", (ika - ikb) % 2 == 0)
                # T7r
                for r in range(1, 9):
                    lhs = (ea - eb) % (1 << r) == 0
                    lim = (pk - 2) // (1 << r)
                    rhs = any((Ba - Bb - (1 << (m + r)) * t) % pk == 0
                              for t in range(-lim, lim + 1))
                    chk("T7r", lhs == rhs)
                # T4 spread with p>=1
                d = next(i for i in range(m) if wa[i] != wb[i])
                p = sum(wa[:d]); q = k - p
                chk("T4a", p >= 1)
                chk("T4b", abs(Ba - Bb) < (1 << (m - q)) * (3 ** q - 2 ** q)
                          if q > 0 else Ba == Bb)
                if ea == eb:
                    # h-diameter bound (integer form)
                    chk("T4c", 3 ** k * abs(ha - hb)
                              < (1 << (m - k + 1)) * (3 ** (k - 1) - 2 ** (k - 1)))

# ---------------------------------------------------------------- T6 parent id
for m in range(3, 12):
    for k in range(1, m + 1):
        for r in range(1, 7):
            P = histogram(m, k, r)
            mod2 = 1 << (r + 1)
            Qk = histogram(m - 1, k, r + 1) if 1 <= k <= m - 1 else {}
            Qk1 = histogram(m - 1, k - 1, r + 1) if 1 <= k - 1 <= m - 1 else {}
            inv3 = pow(3, -1, mod2)
            for z in range(1 << r):
                a = (2 * z) % mod2
                c = (inv3 * (2 * z - 1)) % mod2
                tot = (Qk.get(a, 0) + Qk.get((a - 3 ** k) % mod2, 0)
                       + Qk1.get(c, 0) + Qk1.get((c - 3 ** (k - 1)) % mod2, 0))
                chk("T6", tot == P.get(z, 0))

print("=== STEP 4 VERIFICATION ===")
print("word pairs:", pairs)
tot = 0
for t in sorted(cnt):
    tot += cnt[t]
    print(f"  {t:5s} checks={cnt[t]:9d} failures={fail.get(t,0)}")
print("TOTAL exact checks:", tot, " ANY FAILURE:", bool(fail))
print()

# ---------------------------------------------------------------- final bound
def Par(m, k):
    if k < 2:
        return 1
    s = [0, 0]
    for i in range(k - 1, m):
        s[i % 2] += comb(i - 1, k - 2)
    return max(s)

def Mbnd(m, k):
    nk = comb(m - 1, k - 1)
    b_int = (1 << (m - k)) * (3 ** (k - 1) - 2 ** (k - 1)) // 3 ** k + 1
    return min(nk, b_int, Par(m, k))

def capbnd(m, k, r):
    nk = comb(m - 1, k - 1)
    N = (3 ** k - 2) // (1 << r) + 1
    return min(nk, N * Mbnd(m, k))

Mtab = json.load(open(r"C:\Users\MDP\collatz-analysis\cap-proof\M_table.json"))
captab = json.load(open(r"C:\Users\MDP\collatz-analysis\cap-proof\cap_table.json"))

# M bound check
vM = 0; ratM = []
for key, M in Mtab.items():
    m, k = map(int, key.split(","))
    b = Mbnd(m, k)
    if M > b:
        vM += 1; print("  M VIOLATION", m, k, M, b)
    ratM.append((b / M, m, k, M, b))
print("T4/T8 M-bound: cases=%d violations=%d" % (len(Mtab), vM))
ratM.sort()
print("  M-bound tightness bound/actual: min %.2f  median %.2f  max %.1f"
      % (ratM[0][0], statistics.median(x[0] for x in ratM), ratM[-1][0]))
print("  worst cell:", ratM[-1][1:])

# cap bound check
vC = 0; rows = []
for key, c in captab.items():
    m, k, r = map(int, key.split(","))
    b = capbnd(m, k, r)
    nk = comb(m - 1, k - 1)
    if c > b:
        vC += 1; print("  CAP VIOLATION", m, k, r, c, b)
    rows.append((m, k, r, c, nk, b, b / c, b < nk))
print()
print("T5 cap-bound: cases=%d violations=%d" % (len(rows), vC))
nt = [x for x in rows if x[7]]
print("  strictly beats trivial n_k in %d of %d cells (%.0f%%)"
      % (len(nt), len(rows), 100 * len(nt) / len(rows)))
rr = sorted(nt, key=lambda x: x[6])
print("  tightness on those cells: min %.2f  median %.2f  max %.1f"
      % (rr[0][6], statistics.median(x[6] for x in nt), rr[-1][6]))
print("  tightest cell (m,k,r,actual,bound):", rr[0][:4], rr[0][5])
print("  loosest cell (m,k,r,actual,bound):", rr[-1][:4], rr[-1][5])

# stabilised regime only
st = [x for x in rows if (1 << x[2]) >= 3 ** x[1] - 1]
print()
print("  stabilised regime (2^r >= 3^k-1): %d cells, tightness min %.2f median %.2f max %.1f"
      % (len(st), min(x[6] for x in st), statistics.median(x[6] for x in st),
         max(x[6] for x in st)))

# T6 corollary
vT6 = 0; nT6 = 0
for key, c in captab.items():
    m, k, r = map(int, key.split(","))
    if m - 1 >= 1 and r + 1 <= 9:
        a = captab.get(f"{m-1},{k},{r+1}", 0)
        b = captab.get(f"{m-1},{k-1},{r+1}", 0)
        nT6 += 1
        if c > 2 * a + 2 * b:
            vT6 += 1
print("  T6 corollary cap<=2cap+2cap: cases=%d violations=%d" % (nT6, vT6))
