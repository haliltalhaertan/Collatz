"""CP20 Task 8B3 E7 - Claude independent kernel check, preregistration V1.

Independent reproduction harness for the E7 block kernels and the candidate
concatenation law. Written from the E7 pre-run seal document (sections 3-5) and
the accepted E5-S1 / E6-N1 identities only.

Independence discipline for this file:
  - no producer module is imported;
  - CP20_TASK8B3_E7_SEALED_CHECKS.py, the producer verifier, its outputs and
    its reports were not read before this file was written and hashed;
  - this file was never executed, and no syntax check was run, before its
    SHA-256 was announced;
  - the cases and the expected contracts below are fixed in advance.

The window W_r and the tail event are deliberately absent. The seal does not
fix the logarithm base in W_r = ceil(8*sqrt(r*log(r+1))), and no test here
needs it. That ambiguity is recorded in the preregistration note instead of
being silently resolved in code.

Everything is computed twice and cross-checked, because this file could not be
run before it was committed:
  - exactly, in Z[omega_{3^v}], as integer coefficient vectors;
  - numerically, as complex numbers.
A disagreement between the two paths is itself a reported failure.
"""

from __future__ import annotations

import cmath
import math

# ---------------------------------------------------------------- conventions

UNDEFINED = "UNDEFINED"          # normalized kernel outside its domain
TOL = 1e-9                       # complex cross-check tolerance


def zeta4_numerator() -> int:
    """(2^-4 mod 3). Equals 1; kept as a computation, not a literal."""
    return pow(2, -4, 3)


def rho(s: int, k: int) -> int:
    """rho_{s,k} = 2^(s+k-5) mod 3^s.

    Python's three-argument pow evaluates a negative exponent through the
    modular inverse, so every s+k<5 case stays exact and is never replaced by
    a real exponent.
    """
    if s < 1 or k < 0:
        raise ValueError("rho requires s>=1 and k>=0")
    return pow(2, s + k - 5, 3 ** s)


def p_fin(s: int, k: int) -> complex:
    """Finite row phase p^fin_{s,k,4} as a complex number."""
    if s == 1:
        if k != 0:
            raise ValueError("row s=1 is only defined at k=0")
        return cmath.exp(2j * math.pi * zeta4_numerator() / 3)
    return cmath.exp(2j * math.pi * rho(s, k) / (3 ** s))


# ------------------------------------------------------------- combinatorics

def weak_compositions(q: int, m: int):
    """All x in Z_{>=0}^m with x_1+...+x_m = q."""
    if m == 0:
        if q == 0:
            yield ()
        return
    if m == 1:
        yield (q,)
        return
    for first in range(q + 1):
        for rest in weak_compositions(q - first, m - 1):
            yield (first,) + rest


def states_of(k: int, x) -> list:
    """T_0=k, T_j=k+x_1+...+x_j."""
    out = [k]
    total = k
    for xi in x:
        total += xi
        out.append(total)
    return out


def positive_kernel(u: int, v: int, k: int, ell: int) -> int:
    """K^+_{u,v}(k,ell), with the frozen edge conventions."""
    if u == v:
        return 1 if k == ell else 0
    if k > ell:
        return 0
    if u == 0 and k != 0:
        return 0
    m = v - u
    q = ell - k
    return math.comb(q + m - 1, m - 1)


# --------------------------------------------------------- exact cyclotomics

def block_exponent(u: int, w: int, states: list, v_ref: int) -> int:
    """E_{u,w}(k;x) written as a power of omega_{3^v_ref}, with v_ref >= w.

    Scaling a block exponent from base 3^w to base 3^v_ref multiplies every
    3^(w-s) by 3^(v_ref-w), which is exactly the 3^(v_ref-s) written here, so
    left and right blocks of a concatenation share one root of unity.
    """
    if v_ref < w:
        raise ValueError("v_ref must be at least w")
    modulus = 3 ** v_ref
    exponent = 0
    if u == 0:
        exponent += 3 ** (v_ref - 1) * zeta4_numerator()
    for s in range(max(2, u + 1), w + 1):
        exponent += 3 ** (v_ref - s) * rho(s, states[s - u - 1])
    return exponent % modulus


def canonical(term_counts: dict, v_ref: int) -> dict:
    """Canonical form in Z[omega_N], N=3^v_ref.

    The minimal polynomial of omega_{3^t} is x^(2*3^(t-1)) + x^(3^(t-1)) + 1,
    so with n1=3^(v_ref-1) and e=a*n1+b the exponents reduce onto a in {0,1}:
    a=2 becomes -(a=1) - (a=0) at the same b. Two elements are equal exactly
    when their canonical dictionaries agree.
    """
    n1 = 3 ** (v_ref - 1)
    out: dict = {}
    for exponent, coeff in term_counts.items():
        a, b = divmod(exponent % (3 ** v_ref), n1)
        if a == 2:
            out[(1, b)] = out.get((1, b), 0) - coeff
            out[(0, b)] = out.get((0, b), 0) - coeff
        else:
            out[(a, b)] = out.get((a, b), 0) + coeff
    return {key: val for key, val in out.items() if val != 0}


def complex_value(term_counts: dict, v_ref: int) -> complex:
    modulus = 3 ** v_ref
    total = 0j
    for exponent, coeff in term_counts.items():
        total += coeff * cmath.exp(2j * math.pi * (exponent % modulus) / modulus)
    return total


def convolve(left: dict, right: dict, v_ref: int) -> dict:
    modulus = 3 ** v_ref
    out: dict = {}
    for e1, c1 in left.items():
        for e2, c2 in right.items():
            key = (e1 + e2) % modulus
            out[key] = out.get(key, 0) + c1 * c2
    return out


def add_into(acc: dict, other: dict) -> None:
    for exponent, coeff in other.items():
        acc[exponent] = acc.get(exponent, 0) + coeff


# ------------------------------------------------------------- block kernels

def complex_kernel_terms(u: int, w: int, k: int, ell: int, v_ref: int) -> dict:
    """K^(4)_{u,w}(k,ell) as {exponent mod 3^v_ref: integer count}.

    An empty dictionary is the exact zero, which is what the seal assigns
    outside the feasible domain.
    """
    if u == w:
        return {0: 1} if k == ell else {}
    if k > ell:
        return {}
    if u == 0 and k != 0:
        return {}
    terms: dict = {}
    for x in weak_compositions(ell - k, w - u):
        exponent = block_exponent(u, w, states_of(k, x), v_ref)
        terms[exponent] = terms.get(exponent, 0) + 1
    return terms


def direct_block_phase(u: int, w: int, states: list) -> complex:
    """Phi_{u,w}(k;x) as a literal product of row phases."""
    value = 1 + 0j
    for j in range(1, w - u + 1):
        value *= p_fin(u + j, states[j - 1])
    return value


def normalized_kernel(u: int, w: int, k: int, ell: int, v_ref: int):
    """Normalized kernel, or UNDEFINED where the seal refuses a value."""
    denominator = positive_kernel(u, w, k, ell)
    if denominator == 0:
        return UNDEFINED
    return complex_value(complex_kernel_terms(u, w, k, ell, v_ref), v_ref) / denominator


# -------------------------------------------------------- preregistered cases
# (u, w, v, k, ell) with u < w < v for the concatenation tests.

CASES = {
    "A_u0_convention_with_negative_exponent": (0, 2, 5, 0, 4),
    "B_negative_exponent_isolated_from_u0": (1, 3, 6, 0, 3),
    "C1_infeasible_k_greater_than_ell": (2, 4, 6, 5, 3),
    "C2_u0_with_nonzero_k": (0, 2, 5, 1, 4),
    "E_central_case_r24": (8, 12, 16, 2, 4),
}

EMPTY_BLOCK_CASES = [(3, 3, 4, 4), (3, 3, 4, 5)]

# rho_{s,k} for every (s,k) with s+k<5 and s>=2: the modular-inverse branch.
NEGATIVE_EXPONENT_TABLE = {
    (2, 0): 8,
    (2, 1): 7,
    (2, 2): 5,
    (3, 0): 7,
    (3, 1): 14,
    (4, 0): 41,
}

# Cases whose kernels must be exactly zero and whose normalized kernel must be
# UNDEFINED rather than 0.
UNDEFINED_EXPECTED = ["C1_infeasible_k_greater_than_ell", "C2_u0_with_nonzero_k"]


# --------------------------------------------------------------------- checks

def check_negative_exponent_table(report: list) -> None:
    for (s, k), expected in sorted(NEGATIVE_EXPONENT_TABLE.items()):
        actual = rho(s, k)
        report.append(
            ("T4_residue", f"s={s},k={k}", actual == expected, f"{actual} vs {expected}")
        )


def check_row_one_consistency(report: list) -> None:
    """The u=0 convention should be the general formula extended to s=1.

    The seal states p^fin_{1,0,4} := zeta_4 as a separate convention. If the
    general modular formula at s=1,k=0 disagrees with it, the convention is an
    arbitrary graft and every u=0 block inherits that ambiguity.
    """
    general = cmath.exp(2j * math.pi * rho(1, 0) / 3)
    convention = p_fin(1, 0)
    report.append(
        ("T6_row1", "zeta_4 == general formula at s=1",
         abs(general - convention) < TOL, f"delta={abs(general - convention):.3e}")
    )


def check_lift_matches_direct_product(report: list) -> None:
    """omega^E must equal the literal product of row phases."""
    for name, (u, w, v, k, ell) in sorted(CASES.items()):
        if k > ell or (u == 0 and k != 0):
            continue
        worst = 0.0
        for x in weak_compositions(ell - k, v - u):
            states = states_of(k, x)
            exponent = block_exponent(u, v, states, v)
            lifted = cmath.exp(2j * math.pi * exponent / (3 ** v))
            worst = max(worst, abs(lifted - direct_block_phase(u, v, states)))
        report.append(("T7_lift", name, worst < TOL, f"max delta={worst:.3e}"))


def check_positive_concatenation(report: list) -> None:
    for name, (u, w, v, k, ell) in sorted(CASES.items()):
        left = positive_kernel(u, v, k, ell)
        right = sum(
            positive_kernel(u, w, k, j) * positive_kernel(w, v, j, ell)
            for j in range(k, ell + 1)
        )
        report.append(("T2_positive", name, left == right, f"{left} vs {right}"))


def check_complex_concatenation(report: list) -> None:
    for name, (u, w, v, k, ell) in sorted(CASES.items()):
        whole = complex_kernel_terms(u, v, k, ell, v)
        split: dict = {}
        for j in range(k, ell + 1):
            add_into(
                split,
                convolve(
                    complex_kernel_terms(u, w, k, j, v),
                    complex_kernel_terms(w, v, j, ell, v),
                    v,
                ),
            )
        exact_ok = canonical(whole, v) == canonical(split, v)
        delta = abs(complex_value(whole, v) - complex_value(split, v))
        numeric_ok = delta < TOL
        report.append(("T1_exact", name, exact_ok, "canonical forms"))
        report.append(("T1_numeric", name, numeric_ok, f"delta={delta:.3e}"))
        report.append(
            ("T1_agree", name, exact_ok == numeric_ok, "exact and numeric agree")
        )


def check_normalized_law(report: list) -> None:
    for name, (u, w, v, k, ell) in sorted(CASES.items()):
        whole = normalized_kernel(u, v, k, ell, v)
        if name in UNDEFINED_EXPECTED:
            report.append(
                ("T5_undefined", name, whole is UNDEFINED, f"got {whole!r}")
            )
            continue
        denominator = positive_kernel(u, v, k, ell)
        total = 0j
        weight_sum = 0.0
        for j in range(k, ell + 1):
            weight = (
                positive_kernel(u, w, k, j) * positive_kernel(w, v, j, ell)
            ) / denominator
            if weight == 0:
                continue
            weight_sum += weight
            total += weight * normalized_kernel(u, w, k, j, v) * normalized_kernel(w, v, j, ell, v)
        report.append(
            ("T3_normalized", name, abs(whole - total) < TOL, f"delta={abs(whole - total):.3e}")
        )
        report.append(
            ("T3_weights", name, abs(weight_sum - 1.0) < TOL, f"sum={weight_sum:.12f}")
        )


def check_empty_block(report: list) -> None:
    for u, v, k, ell in EMPTY_BLOCK_CASES:
        expected = 1 if k == ell else 0
        pos_ok = positive_kernel(u, v, k, ell) == expected
        terms = complex_kernel_terms(u, v, k, ell, max(v, 1))
        cplx_ok = (complex_value(terms, max(v, 1)).real > 0.5) == (k == ell)
        report.append(
            ("T5_empty", f"u=v={u},k={k},ell={ell}", pos_ok and cplx_ok, f"expected {expected}")
        )


def main() -> int:
    report: list = []
    check_negative_exponent_table(report)
    check_row_one_consistency(report)
    check_lift_matches_direct_product(report)
    check_positive_concatenation(report)
    check_complex_concatenation(report)
    check_normalized_law(report)
    check_empty_block(report)

    failures = 0
    for test, label, passed, detail in report:
        if not passed:
            failures += 1
        print(f"{'PASS' if passed else 'FAIL'}  {test:16s} {label:44s} {detail}")
    print()
    print(f"checks={len(report)} failures={failures}")
    print("CLAUDE INDEPENDENT KERNEL CHECK: " + ("PASS" if failures == 0 else "FAIL"))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
