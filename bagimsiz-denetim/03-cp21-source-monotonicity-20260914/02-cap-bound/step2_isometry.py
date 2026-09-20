"""
STEP 2 -- the isometry, sharpened, and the exact collision condition.

CLAIMS TO VERIFY (all exact integer arithmetic):

 (I1)  For w != w' in W_{m,k} (SAME weight k), let d(w,w') = min{i : w_i != w'_i}.
       Then   v2(h_w - h_w') = v2(B_w - B_w') = d(w,w').
       [ this is the programme's isometry, SHARPENED: both equal the purely
         combinatorial first-difference index ]

 (I2)  Closed form  B_w = sum_{i in S} 3^{t_i} 2^i,  t_i = #{j in S : j > i}.
       Prefix factorisation: if w,w' share the length-u prefix P of weight p
       then  B_w - B_w' = Bsuf(w) - Bsuf(w'),  Bsuf(x) = sum_{i in S_x, i>=u} 3^{t_i}2^i
       (the prefix contribution 3^{k-p} B(P) cancels EXACTLY).

 (I3)  Range lemma:  1 <= e_w <= 3^k - 1.

 (I4)  COLLISION CONDITION.  With u = d(w,w'), A = (h_w-h_w')/2^u,
       C = (B_w-B_w')/2^u  (A, C both ODD):
            3^k A + C = 2^{m-u} (e_w - e_w')
       and  e_w = e_w' mod 2^r   <=>   2^{m+r-u} | 3^k A + C.
       In particular v2(3^k A + C) >= 1 ALWAYS (A,C odd) and a collision needs
       v2(3^k A + C) >= m+r-u >= r+1.

 (I5)  |Delta| bound:  |B_w - B_w'| < 2^{m-q}(3^q - 2^q),  q = k - p.

 (I6)  EXACT-collision closeness:  e_w = e_w'  =>  |h_w - h_w'| < 2^{m-k} (2/3)^p
       (checked as 3^p |h_w-h_w'| < 2^{m-k+p}, integer form)
       and hence d(w,w') <= m-k-1.

 (I7)  TAIL REFORMULATION.  Q_r : Z/2^r -> {0,1}^r, e |-> parities of e,H(e),...,H^{r-1}(e)
       is a bijection, and
         P_{m,k,r}(z) = #{ odd h < 2^m : |parities_0..m-1| = k, parities_m..m+r-1 = Q_r(z) }.
"""
import sys, json, itertools
from math import comb
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\cap-proof")
from collatz_cap_core import *

R = {}
cnt = {}


def bump(tag, ok):
    cnt[tag] = cnt.get(tag, 0) + 1
    if not ok:
        R.setdefault(tag + "_FAIL", []).append(1)


# ---------------------------------------------------------- I1,I2,I4,I5,I6
MMAX = 12
pairs_checked = 0
for m in range(2, MMAX + 1):
    for k in range(1, m + 1):
        L = layer(m, k)
        if len(L) > 260:            # cap pair count per (m,k) for runtime
            L = L[:260]
        for a in range(len(L)):
            wa, Ba, ha, ea = L[a]
            for b in range(a + 1, len(L)):
                wb, Bb, hb, eb = L[b]
                pairs_checked += 1
                d = next(i for i in range(m) if wa[i] != wb[i])
                # I1
                bump("I1", v2(ha - hb) == d and v2(Ba - Bb) == d)
                # I2 prefix cancellation
                Sa = positions(wa); Sb = positions(wb)
                ta = {i: sum(1 for j in Sa if j > i) for i in Sa}
                tb = {i: sum(1 for j in Sb if j > i) for i in Sb}
                sufa = sum(pow(3, ta[i]) * (1 << i) for i in Sa if i >= d)
                sufb = sum(pow(3, tb[i]) * (1 << i) for i in Sb if i >= d)
                bump("I2", sufa - sufb == Ba - Bb)
                p = sum(wa[:d]); q = k - p
                # I5
                bump("I5", abs(Ba - Bb) < (1 << (m - q)) * (3 ** q - 2 ** q))
                # I4
                A = (ha - hb) >> d
                C = (Ba - Bb) >> d
                bump("I4a", A % 2 == 1 and C % 2 == 1)
                bump("I4b", pow(3, k) * A + C == (1 << (m - d)) * (ea - eb))
                for r in range(1, 11):
                    lhs = (ea - eb) % (1 << r) == 0
                    rhs = (pow(3, k) * A + C) % (1 << (m + r - d)) == 0
                    bump("I4c", lhs == rhs)
                # I6
                if ea == eb:
                    bump("I6a", 3 ** p * abs(ha - hb) < (1 << (m - k + p)))
                    bump("I6b", d <= m - k - 1)

# ---------------------------------------------------------- I3
for m in range(1, 15):
    for k in range(1, m + 1):
        for (w, B, h, e) in layer(m, k):
            bump("I3", 1 <= e <= 3 ** k - 1)

# ---------------------------------------------------------- I7
def Qr(e, r):
    out = []
    x = e
    for _ in range(r):
        out.append(x & 1)
        x = H(x)
    return tuple(out)

for r in range(1, 9):
    seen = {}
    for z in range(1 << r):
        seen[Qr(z, r)] = z
    bump("I7bij", len(seen) == (1 << r))

for m in range(2, 12):
    for r in range(1, 7):
        for k in range(1, m + 1):
            hist = histogram(m, k, r)
            alt = {}
            for h in range(1, 1 << m, 2):
                full = parity_word(h, m + r)
                if sum(full[:m]) != k:
                    continue
                tail = full[m:]
                alt[tail] = alt.get(tail, 0) + 1
            alt2 = {}
            for tail, c in alt.items():
                # invert Q_r
                z = next(zz for zz in range(1 << r) if Qr(zz, r) == tail)
                alt2[z] = c
            bump("I7", alt2 == hist)

print("=== STEP 2 VERIFICATION ===")
print("word pairs examined:", pairs_checked)
tot = 0
for t in sorted(cnt):
    f = len(R.get(t + "_FAIL", []))
    tot += cnt[t]
    print(f"  {t:8s} checks={cnt[t]:8d} failures={f}")
print("TOTAL exact checks:", tot)
print("ANY FAILURE:", any(k.endswith("_FAIL") for k in R))
json.dump({"pairs": pairs_checked, "counts": cnt,
           "fails": {k: len(v) for k, v in R.items()}},
          open(r"C:\Users\MDP\collatz-analysis\cap-proof\step2_verification.json", "w"))
