#!/usr/bin/env python3
"""
audit_recompute.py -- independent zero-trust recomputation for the package
research_manager/exploratory/prefix_bridge_20260906/ (derivation/EXACT_PREFIX_REDUCTION.md).

RULES OBSERVED
  * No producer module is imported.  Nothing under prefix_bridge_20260906/ is read or executed
    by this script (the integrity script audit_integrity.py reads bytes for hashing only).
  * Every load-bearing identity is rebuilt from the DEFINITIONS in the derivation and checked
    with exact integer / fractions.Fraction arithmetic.  mpmath is used only for an
    illustrative high-precision margin report; the decisive irrational-beta comparison
    n_r <= beta (r-1) is done as the equivalent EXACT integer inequality 2^(n_r+r-1) <= 3^(r-1).
  * B_r(a) is computed as a direct power sum (the producer uses a Horner recurrence; the
    package auditor uses a direct sum too, but this code is written from the formula, not
    copied).

DEFINITIONS (from derivation section 1, 3, 4, 5)
  z weak composition of n into r parts, a_i = z_i + 1, A_0 = 0, A_j = a_1 + ... + a_j,
  B_r(a) = sum_{s=1}^r 3^(r-s) 2^(A_(s-1)),
  F_r(a) = e_(16*3^r)(B_r(a)),  e_M(x) = exp(2 pi i x / M),
  row phases (frozen PROJECT_DEFINITIONS): zeta_4 = e_48(1) for s = 1 and
      exp(2 pi i 2^(s + S_(s-1) - 5) / 3^s) for s >= 2, S_j = z_1 + ... + z_j,
  m = r - 4, p = (a_1..a_4), j = z_1+..+z_4, b = (a_5..a_r),
  C4(j) = C(j+3,3), Cm(k) = C(k+m-1,m-1), N = C(n+r-1,r-1), w(j) = C4(j) Cm(n-j) / N.
"""
from fractions import Fraction
from math import comb
import json
import sys
import time

T0 = time.perf_counter()
RESULT = {"script": "audit_recompute.py", "arithmetic": "exact int / Fraction; mpmath only for margin report",
          "sections": {}}
FAILS = []


def fail(section, msg):
    FAILS.append({"section": section, "msg": msg})
    print("FAIL", section, msg)


def weak_compositions(n, k):
    """All k-tuples of non-negative integers summing to n (k >= 1)."""
    if k == 1:
        yield (n,)
        return
    for x in range(n + 1):
        for rest in weak_compositions(n - x, k - 1):
            yield (x,) + rest


def B(a):
    """B_r(a) = sum_{s=1}^{r} 3^(r-s) 2^(A_(s-1)); direct power sum."""
    r = len(a)
    A = 0
    tot = 0
    for s in range(1, r + 1):
        tot += 3 ** (r - s) * 2 ** A
        A += a[s - 1]
    return tot


def row_exponent_sum(z):
    """Sum over rows of the analytic row exponents (as exact rationals, negative powers of two
    kept analytic): 1/48 for s=1, 2^(s+S_(s-1)-5)/3^s for s>=2."""
    r = len(z)
    tot = Fraction(1, 48)
    S = 0  # S_(s-1)
    for s in range(2, r + 1):
        S += z[s - 2]  # S_(s-1) = z_1 + ... + z_(s-1)
        e = s + S - 5
        if e >= 0:
            tot += Fraction(2 ** e, 3 ** s)
        else:
            tot += Fraction(1, 2 ** (-e) * 3 ** s)
    return tot


def mod1(q):
    return q - (q.numerator // q.denominator)


# --------------------------------------------------------------------------------------
# B(i) pathwise integer identity + exact phase identity (P); B(ii) row-phase connection.
# r in 5..9, n in 0..5 (protocol), plus the full 31 declared producer cases r=4..8,n=0..5,(16,1)
# are covered separately in section E.
# --------------------------------------------------------------------------------------
sec = {"cases": [], "paths": 0, "int_identity_ok": 0, "phase_identity_exact_ok": 0,
       "phase_identity_mod1_ok": 0, "row_product_exact_ok": 0, "row_product_mod1_ok": 0,
       "B_odd_ok": 0, "mod16_first_four_ok": 0, "mod16_key_consistent": True,
       "crt_ok": 0, "e16_factor_nontrivial_ok": 0}
mod16_keys = {}
for r in range(5, 10):
    m = r - 4
    M = 16 * 3 ** r
    for n in range(0, 6):
        cnt = 0
        for z in weak_compositions(n, r):
            cnt += 1
            a = tuple(x + 1 for x in z)
            Br = B(a)
            p, b = a[:4], a[4:]
            j = sum(z[:4])
            B4, Bm = B(p), B(b)
            # integer identity B_r = 3^m B_4(p) + 2^(4+j) B_m(b)
            if Br == 3 ** m * B4 + 2 ** (4 + j) * Bm:
                sec["int_identity_ok"] += 1
            else:
                fail("B(i)", f"integer identity r={r} n={n} a={a}")
            # exact phase identity  B_r/(16 3^r) == B_4/1296 + 2^j B_m / 3^(m+4)
            lhs = Fraction(Br, M)
            rhs = Fraction(B4, 1296) + Fraction(2 ** j * Bm, 3 ** (m + 4))
            if lhs == rhs:
                sec["phase_identity_exact_ok"] += 1
            else:
                fail("B(i)", f"phase identity exact r={r} n={n} a={a}")
            if mod1(lhs) == mod1(rhs):
                sec["phase_identity_mod1_ok"] += 1
            # row-phase connection: sum of analytic row exponents == B_r/(16 3^r)
            rs = row_exponent_sum(z)
            if rs == lhs:
                sec["row_product_exact_ok"] += 1
            else:
                fail("B(ii)", f"row product exact r={r} n={n} z={z} rows={rs} B/(16 3^r)={lhs}")
            if mod1(rs) == mod1(lhs):
                sec["row_product_mod1_ok"] += 1
            # section 2 claims
            if Br % 2 == 1:
                sec["B_odd_ok"] += 1
            else:
                fail("C-sec2", f"B_r even r={r} a={a}")
            first4 = sum(3 ** (r - s) * 2 ** sum(a[:s - 1]) for s in range(1, 5))
            if Br % 16 == first4 % 16:
                sec["mod16_first_four_ok"] += 1
            else:
                fail("C-sec2", f"B mod 16 != first four summands r={r} a={a}")
            key = (r % 4, min(a[0], 4), min(a[1], 4), min(a[2], 4))
            if key in mod16_keys and mod16_keys[key] != Br % 16:
                sec["mod16_key_consistent"] = False
                fail("C-sec2", f"mod16 key inconsistency key={key}")
            mod16_keys[key] = Br % 16
            # CRT: 16u + 3^r v = 1 ; B/(16 3^r) = uB/3^r + vB/16 exactly ; vB odd
            u = pow(16, -1, 3 ** r)
            v = (1 - 16 * u) // 3 ** r
            assert 16 * u + 3 ** r * v == 1
            if Fraction(Br, M) == Fraction(u * Br, 3 ** r) + Fraction(v * Br, 16):
                sec["crt_ok"] += 1
            else:
                fail("C-sec2", f"CRT exponent identity r={r} a={a}")
            if (v * Br) % 16 != 0 and v % 2 == 1:
                sec["e16_factor_nontrivial_ok"] += 1
            else:
                fail("C-sec2", f"e16 factor trivial or v even r={r} a={a}")
        if cnt != comb(n + r - 1, r - 1):
            fail("B(i)", f"composition count r={r} n={n}: {cnt} != {comb(n+r-1,r-1)}")
        sec["cases"].append({"r": r, "n": n, "paths": cnt})
        sec["paths"] += cnt
sec["mod16_keys_seen"] = len(mod16_keys)
sec["mod16_residues_seen"] = sorted(set(mod16_keys.values()))
RESULT["sections"]["B_i_ii_pathwise_and_row_phase"] = sec
print("B(i)/(ii): paths", sec["paths"], "int_identity", sec["int_identity_ok"], "phase_exact", sec["phase_identity_exact_ok"],
      "row_product_exact", sec["row_product_exact_ok"], "crt", sec["crt_ok"], "B_odd", sec["B_odd_ok"],
      "mod16_first4", sec["mod16_first_four_ok"], "keys", sec["mod16_keys_seen"], "residues", sec["mod16_residues_seen"])

# --------------------------------------------------------------------------------------
# B(iii) mixture identity (M): exact cyclotomic-vector test + uniformity/independence + normalization
# --------------------------------------------------------------------------------------
sec = {"cases": 0, "vector_identity_ok": 0, "uniform_independent_ok": 0, "weights_sum_one_ok": 0,
       "numeric_G_maxdiff": None}
try:
    import mpmath
    mpmath.mp.dps = 50
    HAVE_MP = True
except Exception:
    HAVE_MP = False
maxdiff = mpmath.mpf(0) if HAVE_MP else None
for r in range(5, 10):
    m = r - 4
    M = 16 * 3 ** r
    for n in range(0, 6):
        N = comb(n + r - 1, r - 1)
        sec["cases"] += 1
        # LHS: residue counts of B_r(a) mod M over all a, and pairs grouped by j
        count_full = {}
        pairs_by_j = {}
        for z in weak_compositions(n, r):
            a = tuple(x + 1 for x in z)
            rho = B(a) % M
            count_full[rho] = count_full.get(rho, 0) + 1
            j = sum(z[:4])
            pairs_by_j.setdefault(j, set()).add((z[:4], z[4:]))
        # uniformity + independence: for every j the set of (prefix, tail) pairs equals the full
        # Cartesian product of weak compositions of j into 4 parts and n-j into m parts
        ok_ui = True
        wsum = Fraction(0)
        conv = {}
        for j in range(0, n + 1):
            P = set(weak_compositions(j, 4))
            Tl = set(weak_compositions(n - j, m))
            product = {(p, t) for p in P for t in Tl}
            if pairs_by_j.get(j, set()) != product or len(product) != comb(j + 3, 3) * comb(n - j + m - 1, m - 1):
                ok_ui = False
                fail("B(iii)", f"uniform/independent structure fails r={r} n={n} j={j}")
            wsum += Fraction(comb(j + 3, 3) * comb(n - j + m - 1, m - 1), N)
            # RHS residue multiset: conv of prefix residues 3^m B_4(p) and tail residues 2^(4+j) B_m(b)
            pres = {}
            for p in P:
                rp = (3 ** m * B(tuple(x + 1 for x in p))) % M
                pres[rp] = pres.get(rp, 0) + 1
            tres = {}
            for t in Tl:
                rt = (2 ** (4 + j) * B(tuple(x + 1 for x in t))) % M
                tres[rt] = tres.get(rt, 0) + 1
            for rp, cp in pres.items():
                for rt, ct in tres.items():
                    rho = (rp + rt) % M
                    conv[rho] = conv.get(rho, 0) + cp * ct
        if ok_ui:
            sec["uniform_independent_ok"] += 1
        if wsum == 1:
            sec["weights_sum_one_ok"] += 1
        else:
            fail("B(iii)", f"weights do not sum to 1 r={r} n={n}: {wsum}")
        if conv == count_full and sum(conv.values()) == N:
            sec["vector_identity_ok"] += 1
        else:
            fail("B(iii)", f"cyclotomic residue-vector identity fails r={r} n={n}")
        if HAVE_MP:
            # illustrative numeric: G = (1/N) sum_rho count[rho] e_M(rho)  vs  sum_j w D_j H_j
            G1 = sum(c * mpmath.expjpi(2 * mpmath.mpf(rho) / M) for rho, c in count_full.items()) / N
            G2 = mpmath.mpc(0)
            for j in range(0, n + 1):
                C4 = comb(j + 3, 3)
                Cm = comb(n - j + m - 1, m - 1)
                w = mpmath.mpf(C4 * Cm) / N
                D = sum(mpmath.expjpi(2 * mpmath.mpf(B(tuple(x + 1 for x in p))) / 1296) for p in weak_compositions(j, 4)) / C4
                H = sum(mpmath.expjpi(2 * mpmath.mpf(2 ** j * B(tuple(x + 1 for x in t))) / 3 ** (m + 4)) for t in weak_compositions(n - j, m)) / Cm
                G2 += w * D * H
            d = abs(G1 - G2)
            if d > maxdiff:
                maxdiff = d
sec["numeric_G_maxdiff"] = mpmath.nstr(maxdiff, 5) if HAVE_MP else "mpmath unavailable"
RESULT["sections"]["B_iii_mixture_identity"] = sec
print("B(iii): cases", sec["cases"], "vector_identity_ok", sec["vector_identity_ok"], "uniform_independent_ok",
      sec["uniform_independent_ok"], "weights_sum_one_ok", sec["weights_sum_one_ok"], "numeric maxdiff", sec["numeric_G_maxdiff"])

# --------------------------------------------------------------------------------------
# B(iv) cutoff inequality (C), exact, r in 5..12, n in 0..10, L in 0..n
# --------------------------------------------------------------------------------------
sec = {"triples": 0, "bound_C_ok": 0, "single_coord_formula_ok": 0, "product_formula_ok": 0,
       "single_coord_le_power_ok": 0, "union_bound_ok": 0, "brute_force_checked": 0, "brute_force_ok": 0}
for r in range(5, 13):
    m = r - 4
    for n in range(0, 11):
        N = comb(n + r - 1, r - 1)
        w = [Fraction(comb(j + 3, 3) * comb(n - j + m - 1, m - 1), N) for j in range(n + 1)]
        assert sum(w) == 1
        brute = None
        if comb(n + r - 1, r - 1) <= 20000:
            # brute force distribution of J and of z_1 from the actual uniform law
            J_counts = {}
            z1_counts = {}
            for z in weak_compositions(n, r):
                J = sum(z[:4])
                J_counts[J] = J_counts.get(J, 0) + 1
                z1_counts[z[0]] = z1_counts.get(z[0], 0) + 1
            brute = (J_counts, z1_counts)
        for L in range(0, n + 1):
            sec["triples"] += 1
            q = L // 4 + 1
            P_JgtL = sum(w[L + 1:], Fraction(0))
            # single-coordinate probability P(z_1 >= q) = C(n-q+r-1, r-1)/N (0 if q > n)
            P_z1 = Fraction(comb(n - q + r - 1, r - 1), N) if q <= n else Fraction(0)
            if q <= n:
                prod = Fraction(1)
                for h in range(q):
                    prod *= Fraction(n - h, n + r - 1 - h)
                if prod == P_z1:
                    sec["product_formula_ok"] += 1
                else:
                    fail("B(iv)", f"product formula r={r} n={n} q={q}")
            else:
                sec["product_formula_ok"] += 1
            ratio = Fraction(n, n + r - 1)
            if P_z1 <= ratio ** q:
                sec["single_coord_le_power_ok"] += 1
            else:
                fail("B(iv)", f"single coordinate power bound r={r} n={n} q={q}")
            if P_JgtL <= 4 * P_z1:
                sec["union_bound_ok"] += 1
            else:
                fail("B(iv)", f"union bound r={r} n={n} L={L}: {P_JgtL} > 4*{P_z1}")
            if P_JgtL <= 4 * ratio ** q:
                sec["bound_C_ok"] += 1
            else:
                fail("B(iv)", f"bound (C) r={r} n={n} L={L}: {P_JgtL} > {4*ratio**q}")
            if brute is not None:
                sec["brute_force_checked"] += 1
                Jc, z1c = brute
                bf_J = Fraction(sum(c for J, c in Jc.items() if J > L), N)
                bf_z1 = Fraction(sum(c for x, c in z1c.items() if x >= q), N)
                if bf_J == P_JgtL and bf_z1 == P_z1:
                    sec["brute_force_ok"] += 1
                    sec["single_coord_formula_ok"] += 1
                else:
                    fail("B(iv)", f"brute force mismatch r={r} n={n} L={L}")
RESULT["sections"]["B_iv_cutoff_inequality"] = sec
print("B(iv): triples", sec["triples"], "bound_C_ok", sec["bound_C_ok"], "union_bound_ok", sec["union_bound_ok"],
      "single_coord_le_power_ok", sec["single_coord_le_power_ok"], "product_formula_ok", sec["product_formula_ok"],
      "brute_force_checked", sec["brute_force_checked"], "brute_force_ok", sec["brute_force_ok"])

# --------------------------------------------------------------------------------------
# B(iv) continued: critical target n_r = floor(beta r) - 8, beta = log2(3) - 1.
#   floor(beta r) = floor(r log2 3) - r = (bit_length(3^r) - 1) - r   (exact)
#   n_r <= beta (r-1)  <=>  n_r + r - 1 <= (r-1) log2 3  <=>  2^(n_r + r - 1) <= 3^(r-1)   (exact)
#   n_r/(n_r+r-1) <= rho = beta/(1+beta)  <=>  n_r (1+beta) <= beta (n_r + r - 1) <=> n_r <= beta (r-1)
# --------------------------------------------------------------------------------------
sec = {"r_range": [14, 2000], "n_r_nonneg_ok": 0, "n_r_le_beta_rm1_exact_ok": 0, "domain_table": {},
       "mpmath_min_margin_beta_rm1_minus_n_r": None, "cutoff_chain_checks": 0, "cutoff_chain_ok": 0}
for r in range(10, 18):
    k = (3 ** r).bit_length() - 1  # floor(r log2 3)
    sec["domain_table"][r] = k - r - 8
for r in range(14, 2001):
    k = (3 ** r).bit_length() - 1
    n_r = k - r - 8
    if n_r >= 0:
        sec["n_r_nonneg_ok"] += 1
    else:
        fail("B(iv)-critical", f"n_r negative at r={r}")
    if 2 ** (n_r + r - 1) <= 3 ** (r - 1):
        sec["n_r_le_beta_rm1_exact_ok"] += 1
    else:
        fail("B(iv)-critical", f"n_r > beta(r-1) at r={r}")
if HAVE_MP:
    mpmath.mp.dps = 60
    beta = mpmath.log(3, 2) - 1
    rho = beta / (1 + beta)
    minmargin = None
    for r in range(14, 2001):
        k = (3 ** r).bit_length() - 1
        n_r = k - r - 8
        margin = beta * (r - 1) - n_r
        if minmargin is None or margin < minmargin:
            minmargin = margin
        # illustrative chain: L_r = ceil(4(1+delta) ln r / |ln rho|), q = floor(L/4)+1, rho^q <= r^(-1-delta)
        for delta in (mpmath.mpf('0.1'), mpmath.mpf('0.5'), mpmath.mpf(1)):
            L = int(mpmath.ceil(4 * (1 + delta) * mpmath.log(r) / abs(mpmath.log(rho))))
            q = L // 4 + 1
            sec["cutoff_chain_checks"] += 1
            if q > mpmath.mpf(L) / 4 and rho ** q <= mpmath.mpf(r) ** (-(1 + delta)) and \
               mpmath.mpf(n_r) / (n_r + r - 1) <= rho:
                sec["cutoff_chain_ok"] += 1
            else:
                fail("B(iv)-critical", f"cutoff chain fails r={r} delta={delta}")
    sec["mpmath_min_margin_beta_rm1_minus_n_r"] = mpmath.nstr(minmargin, 12)
    sec["beta_60dps"] = mpmath.nstr(beta, 40)
    sec["rho_60dps"] = mpmath.nstr(rho, 40)
RESULT["sections"]["B_iv_critical_target"] = sec
print("B(iv) critical: n_r table r=10..17:", sec["domain_table"])
print("B(iv) critical: r=14..2000 n_r>=0 ok", sec["n_r_nonneg_ok"], "exact n_r<=beta(r-1) ok", sec["n_r_le_beta_rm1_exact_ok"],
      "min margin beta(r-1)-n_r", sec["mpmath_min_margin_beta_rm1_minus_n_r"], "cutoff chain ok",
      sec["cutoff_chain_ok"], "/", sec["cutoff_chain_checks"])

# --------------------------------------------------------------------------------------
# E. Independent re-implementation of the producer's 8 declared checks over the 31 declared
#    cases (r=4..8, n=0..5, plus (16,1)) -- written from PLAN.md's description, NOT from the
#    producer source.  Both the WRONG V1 tail denominator 16*3^(r-3) and the corrected V2
#    denominator 16*3^r are evaluated, to reproduce "V1 fails on every path / V2 passes".
# --------------------------------------------------------------------------------------
sec = {"cases": 0, "paths": 0, "checks_total": 0, "v1_wrong_denominator_failures": 0, "v2_correct_failures": 0,
       "other_check_failures": 0, "residue_keys": 0, "observed_B_mod16": None, "sample_r16": None}
keys = {}
residues = set()
cases = [(r, n) for r in range(4, 9) for n in range(6)] + [(16, 1)]
for r, n in cases:
    sec["cases"] += 1
    Mr = 3 ** r
    u = pow(16, -1, Mr)
    v = (1 - 16 * u) // Mr
    for z in weak_compositions(n, r):
        sec["paths"] += 1
        a = tuple(x + 1 for x in z)
        b = B(a)
        pre, tail = B(a[:3]), B(a[3:])
        s = sum(a[:3])
        # 1 bezout, 2 crt_fraction, 3 integer concatenation (three-prefix), 4 phase concatenation,
        # 5 residue formula, 6 residue key consistency, 7 oddness, 8 nontrivial mod-16 factor
        c1 = (16 * u + Mr * v == 1)
        c2 = (mod1(Fraction(b, 16 * Mr) - Fraction(u * b, Mr) - Fraction(v * b, 16)) == 0)
        c3 = (b == 3 ** (r - 3) * pre + 2 ** s * tail)
        c4_v1 = (Fraction(b, 16 * Mr) == Fraction(pre, 16 * 27) + Fraction(2 ** s * tail, 16 * 3 ** (r - 3)))
        c4_v2 = (Fraction(b, 16 * Mr) == Fraction(pre, 16 * 27) + Fraction(2 ** s * tail, 16 * 3 ** r))
        residue = (3 ** (r - 1) + 3 ** (r - 2) * 2 ** a[0] + 3 ** (r - 3) * 2 ** (a[0] + a[1]) + 3 ** (r - 4) * 2 ** s) % 16
        c5 = (b % 16 == residue)
        key = (r % 4, min(a[0], 4), min(a[1], 4), min(a[2], 4))
        c6 = (key not in keys or keys[key] == residue)
        keys[key] = residue
        c7 = (b % 2 == 1 and v % 2 == 1)
        c8 = ((v * b) % 16 != 0)
        residues.add(b % 16)
        sec["checks_total"] += 8
        if not c4_v1:
            sec["v1_wrong_denominator_failures"] += 1
        if not c4_v2:
            sec["v2_correct_failures"] += 1
        if not all((c1, c2, c3, c5, c6, c7, c8)):
            sec["other_check_failures"] += 1
        if r == 16 and z[0] == 1:
            sec["sample_r16"] = {"a": a, "B": b, "u": u, "v": v, "project_exponent": str(Fraction(b, 16 * Mr)),
                                 "ternary_exponent_mod1": str(mod1(Fraction(u * b, Mr))),
                                 "mod16_exponent_mod1": str(mod1(Fraction(v * b, 16))),
                                 "ternary_minus_project_mod1": str(mod1(Fraction(u * b, Mr) - Fraction(b, 16 * Mr)))}
sec["residue_keys"] = len(keys)
sec["observed_B_mod16"] = sorted(residues)
# first V1 failure witness from REPORT.md: r=4, a=(1,1,1,1): B_4=65, B_3=19, tail=1, s=3
sec["witness_r4"] = {"B4": B((1, 1, 1, 1)), "B3": B((1, 1, 1)), "Btail": B((1,)),
                     "correct": str(Fraction(19, 432) + Fraction(8, 1296)), "v1_wrong": str(Fraction(19, 432) + Fraction(8, 48)),
                     "target": str(Fraction(65, 1296))}
RESULT["sections"]["E_producer_checks_reimplemented"] = sec
print("E: cases", sec["cases"], "paths", sec["paths"], "checks", sec["checks_total"], "V1-denominator failures",
      sec["v1_wrong_denominator_failures"], "V2-denominator failures", sec["v2_correct_failures"], "other failures",
      sec["other_check_failures"], "residue keys", sec["residue_keys"], "residues", sec["observed_B_mod16"])
print("E: r=16 sample", json.dumps(sec["sample_r16"]))
print("E: r=4 witness", json.dumps(sec["witness_r4"]))

# --------------------------------------------------------------------------------------
# F. Count arithmetic quoted in the package (auditor 1161/20/60; producer 31 cases / 2935 paths / 23480)
# --------------------------------------------------------------------------------------
sec = {"auditor_paths_r5to8_n0to4": sum(comb(n + r - 1, r - 1) for r in range(5, 9) for n in range(5)),
       "auditor_pairs": 4 * 5, "auditor_cutoff_triples": sum(n + 1 for r in range(5, 9) for n in range(5)),
       "producer_cases": len(cases), "producer_paths": sum(comb(n + r - 1, r - 1) for r, n in cases),
       "producer_checks": 8 * sum(comb(n + r - 1, r - 1) for r, n in cases)}
RESULT["sections"]["F_quoted_counts"] = sec
print("F:", json.dumps(sec))

RESULT["failures"] = FAILS
RESULT["status"] = "PASS" if not FAILS else "FAIL"
RESULT["elapsed_seconds"] = time.perf_counter() - T0
print("OVERALL", RESULT["status"], "failures", len(FAILS), "elapsed", round(RESULT["elapsed_seconds"], 2), "s")
with open(sys.argv[1] if len(sys.argv) > 1 else "audit_recompute_results.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(RESULT, f, indent=1, default=str)
