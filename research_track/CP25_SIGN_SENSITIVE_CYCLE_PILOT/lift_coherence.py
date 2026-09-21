#!/usr/bin/env python3
"""Exact oriented lift-coherence diagnostics for CP25."""
from __future__ import annotations

from fractions import Fraction
from typing import Iterable


def _bits(word: Iterable[int]) -> tuple[int, ...]:
    bits = tuple(word)
    if not bits or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("word must be a nonempty binary iterable of exact integers")
    return bits


def _validate_p(p: int) -> None:
    if type(p) is not int or p < 3 or p % 2 == 0:
        raise ValueError("p must be an odd exact integer >= 3")


def _validate_max_m(max_m: int) -> None:
    if type(max_m) is not int or max_m < 1:
        raise ValueError("max_m must be a positive exact integer")


def B_value(p: int, word: Iterable[int]) -> int:
    bits = _bits(word)
    _validate_p(p)
    value = 0
    for j, bit in enumerate(bits):
        if bit:
            value = p * value + (1 << j)
    return value


def h_residue(p: int, b: int, word: Iterable[int]) -> int:
    bits = _bits(word)
    _validate_p(p)
    if type(b) is not int or b not in (-1, 1):
        raise ValueError("b must be the exact integer +1 or -1")
    modulus = 1 << len(bits)
    pk = pow(p, sum(bits), modulus)
    residue = (-b * B_value(p, bits) * pow(pk, -1, modulus)) % modulus
    return residue or modulus


def is_primitive(word: Iterable[int]) -> bool:
    bits = _bits(word)
    m = len(bits)
    return all(m % d or bits != bits[:d] * (m // d) for d in range(1, m))


def rotations(word: Iterable[int]) -> tuple[tuple[int, ...], ...]:
    bits = _bits(word)
    return tuple(bits[i:] + bits[:i] for i in range(len(bits)))


def lift_profile(p: int, word: Iterable[int]) -> dict[str, object]:
    bits = _bits(word)
    _validate_p(p)
    m = len(bits)
    k = sum(bits)
    if k == 0:
        raise ValueError("word must contain at least one odd step")
    D = (1 << m) - p**k
    b = 1 if D > 0 else -1
    A = abs(D)
    rows = []
    modulus = 1 << m
    for i, rotated in enumerate(rotations(bits)):
        B = B_value(p, rotated)
        q = Fraction(B, A)
        h = h_residue(p, b, rotated)
        t_numerator = B - A * h
        if t_numerator % modulus:
            raise RuntimeError("lift residue failed to make B-Ah divisible by 2^m")
        t = t_numerator // modulus
        if (q >= h) != (t >= 0):
            raise RuntimeError("lift dominance and carry sign disagree")
        rows.append(
            {
                "index": i,
                "word": rotated,
                "B": B,
                "q": q,
                "h": h,
                "t": t,
                "dominates": t >= 0,
            }
        )
    for i, row in enumerate(rows):
        next_h = rows[(i + 1) % m]["h"]
        epsilon = row["word"][0]
        carry_numerator = (p**epsilon) * row["h"] + b * epsilon - 2 * next_h
        if carry_numerator % modulus:
            raise RuntimeError("adjacent lift representatives do not define an integer carry")
        row["carry"] = carry_numerator // modulus
    return {
        "p": p,
        "word": bits,
        "m": m,
        "k": k,
        "D": D,
        "b": b,
        "A": A,
        "primitive": is_primitive(bits),
        "integral": B_value(p, bits) % A == 0,
        "all_dominate": all(row["dominates"] for row in rows),
        "rotations": tuple(rows),
    }


def product_barrier_profile(p: int, word: Iterable[int]) -> dict[str, object]:
    """Evaluate ChatGPT Web's exact Product Barrier sub-lemma."""
    profile = lift_profile(p, word)
    if profile["integral"]:
        raise ValueError("Product Barrier is stated only for nonintegral words")
    modulus = 1 << profile["m"]
    product = Fraction(1)
    factors = []
    for row in profile["rotations"]:
        if row["word"][0] == 0:
            continue
        y = Fraction(row["h"] * profile["A"] + modulus, profile["A"])
        factor = Fraction(p) + Fraction(profile["b"], y)
        product *= factor
        factors.append({"index": row["index"], "y": y, "factor": factor})
    barrier_holds = product < modulus if profile["b"] == 1 else product > modulus
    return {
        "p": p,
        "word": profile["word"],
        "m": profile["m"],
        "k": profile["k"],
        "b": profile["b"],
        "A": profile["A"],
        "M": modulus,
        "product": product,
        "barrier_holds": barrier_holds,
        "factors": tuple(factors),
    }


def scan_product_barrier(p: int, max_m: int) -> dict[str, object]:
    _validate_p(p)
    _validate_max_m(max_m)
    seen: set[tuple[int, ...]] = set()
    nonintegral = 0
    counterexamples = []
    by_sign = {"+1": 0, "-1": 0}
    for m in range(1, max_m + 1):
        for tail in range(1 << (m - 1)):
            word = (1,) + tuple((tail >> j) & 1 for j in range(m - 1))
            if not is_primitive(word):
                continue
            necklace = min(rotations(word))
            if necklace in seen:
                continue
            seen.add(necklace)
            profile = lift_profile(p, necklace)
            if profile["integral"]:
                continue
            nonintegral += 1
            sign = "+1" if profile["b"] == 1 else "-1"
            by_sign[sign] += 1
            barrier = product_barrier_profile(p, necklace)
            if not barrier["barrier_holds"] and len(counterexamples) < 10:
                counterexamples.append(
                    {
                        "word": "".join(map(str, necklace)),
                        "m": m,
                        "k": profile["k"],
                        "b": profile["b"],
                        "A": profile["A"],
                        "product": str(barrier["product"]),
                        "M": barrier["M"],
                    }
                )
    return {
        "p": p,
        "max_m": max_m,
        "primitive_necklaces": len(seen),
        "nonintegral_necklaces": nonintegral,
        "nonintegral_by_sign": by_sign,
        "counterexamples": counterexamples,
    }


def scan_all_words(p: int, max_m: int) -> dict[str, object]:
    _validate_p(p)
    _validate_max_m(max_m)
    words = prefilter = premise = integral_premise = 0
    counterexamples = []
    by_m = []
    for m in range(1, max_m + 1):
        row = {"m": m, "words": 0, "all_q_at_least_one": 0, "premise_rows": 0, "integral_premise_rows": 0}
        for tail in range(1 << (m - 1)):
            word = (1,) + tuple((tail >> j) & 1 for j in range(m - 1))
            row["words"] += 1
            words += 1
            k = sum(word)
            D = (1 << m) - p**k
            b = 1 if D > 0 else -1
            A = abs(D)
            rotated_words = rotations(word)
            Bs = tuple(B_value(p, rotated) for rotated in rotated_words)
            if any(B < A for B in Bs):
                continue
            row["all_q_at_least_one"] += 1
            prefilter += 1
            if any(B < A * h_residue(p, b, rotated) for B, rotated in zip(Bs, rotated_words)):
                continue
            row["premise_rows"] += 1
            premise += 1
            integral = Bs[0] % A == 0
            if integral:
                row["integral_premise_rows"] += 1
                integral_premise += 1
            elif len(counterexamples) < 10:
                counterexamples.append(
                    {"word": "".join(map(str, word)), "m": m, "k": k, "b": b, "A": A, "B": Bs[0]}
                )
        by_m.append(row)
    return {
        "p": p,
        "max_m": max_m,
        "words": words,
        "all_q_at_least_one_rows": prefilter,
        "premise_rows": premise,
        "integral_premise_rows": integral_premise,
        "nonintegral_premise_rows": premise - integral_premise,
        "counterexamples": counterexamples,
        "by_m": by_m,
    }


def scan_lift(p: int, max_m: int) -> dict[str, object]:
    _validate_p(p)
    _validate_max_m(max_m)
    raw = 0
    seen: set[tuple[int, ...]] = set()
    survivors = []
    by_sign = {
        "+1": {
            "necklaces": 0,
            "all_q_at_least_one": 0,
            "dominance_survivors": 0,
            "integral_survivors": 0,
        },
        "-1": {
            "necklaces": 0,
            "all_q_at_least_one": 0,
            "dominance_survivors": 0,
            "integral_survivors": 0,
        },
    }
    for m in range(1, max_m + 1):
        for tail in range(1 << (m - 1)):
            word = (1,) + tuple((tail >> j) & 1 for j in range(m - 1))
            if not is_primitive(word):
                continue
            raw += 1
            necklace = min(rotations(word))
            if necklace in seen:
                continue
            seen.add(necklace)
            profile = lift_profile(p, necklace)
            sign = "+1" if profile["b"] == 1 else "-1"
            by_sign[sign]["necklaces"] += 1
            if all(row["q"] >= 1 for row in profile["rotations"]):
                by_sign[sign]["all_q_at_least_one"] += 1
            if not profile["all_dominate"]:
                continue
            by_sign[sign]["dominance_survivors"] += 1
            if profile["integral"]:
                by_sign[sign]["integral_survivors"] += 1
            survivors.append(
                {
                    "word": "".join(map(str, necklace)),
                    "m": profile["m"],
                    "k": profile["k"],
                    "b": profile["b"],
                    "A": profile["A"],
                    "B": B_value(p, necklace),
                    "integral": profile["integral"],
                }
            )
    dominance = len(survivors)
    integral = sum(bool(row["integral"]) for row in survivors)
    return {
        "p": p,
        "max_m": max_m,
        "primitive_raw_starting_one": raw,
        "primitive_necklaces": len(seen),
        "dominance_survivors": dominance,
        "integral_survivors": integral,
        "nonintegral_survivors": dominance - integral,
        "by_sign": by_sign,
        "survivors": survivors,
    }
