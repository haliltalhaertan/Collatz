#!/usr/bin/env python3
"""Exact cycle-word arithmetic for the CP25 sign-sensitive pilot."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import argparse
import json


@dataclass(frozen=True)
class Candidate:
    p: int
    b: int
    word: tuple[int, ...]
    k: int
    B: int
    D: int
    x: int | None


def _validate_map_parameters(p: int, b: int) -> None:
    if type(p) is not int or p < 3 or p % 2 == 0:
        raise ValueError("p must be an odd exact integer >= 3")
    if type(b) is not int or b not in (-1, 1):
        raise ValueError("b must be the exact integer +1 or -1")


def candidate_from_word(p: int, b: int, word: Iterable[int]) -> Candidate:
    bits = tuple(word)
    _validate_map_parameters(p, b)
    if not bits or bits[0] != 1 or any(
        type(bit) is not int or bit not in (0, 1) for bit in bits
    ):
        raise ValueError("word must be a nonempty exact-integer binary tuple beginning with 1")

    m = len(bits)
    k = sum(bits)
    suffix_ones = k
    B = 0
    for j, bit in enumerate(bits):
        if bit:
            suffix_ones -= 1
            B += (2**j) * (p**suffix_ones)
    D = 2**m - p**k
    x = None if D == 0 or (b * B) % D else (b * B) // D
    return Candidate(p=p, b=b, word=bits, k=k, B=B, D=D, x=x)


def follows_word_and_returns(candidate: Candidate) -> bool:
    if candidate.x is None:
        return False
    y = candidate.x
    for bit in candidate.word:
        if y % 2 != bit:
            return False
        y = (candidate.p * y + candidate.b) // 2 if bit else y // 2
    return y == candidate.x


def _primitive_cycle(candidate: Candidate) -> tuple[int, ...]:
    if candidate.x is None or candidate.x <= 0:
        raise ValueError("candidate must be a positive integer cycle")
    orbit = []
    y = candidate.x
    for _ in candidate.word:
        orbit.append(y)
        y = (candidate.p * y + candidate.b) // 2 if y % 2 else y // 2
        if y == candidate.x:
            rotations = [tuple(orbit[i:] + orbit[:i]) for i in range(len(orbit))]
            return min(rotations)
    raise ValueError("candidate did not return within the word length")


def enumerate_map(p: int, b: int, max_m: int) -> dict[str, object]:
    _validate_map_parameters(p, b)
    if type(max_m) is not int or max_m < 1:
        raise ValueError("max_m must be a positive exact integer")
    words = divisible = positive = realized = 0
    cycles: set[tuple[int, ...]] = set()
    by_m: list[dict[str, int]] = []
    for m in range(1, max_m + 1):
        row = {"m": m, "words": 0, "divisible": 0, "positive_integer": 0, "realized": 0}
        for tail in range(1 << (m - 1)):
            word = (1,) + tuple((tail >> j) & 1 for j in range(m - 1))
            candidate = candidate_from_word(p, b, word)
            words += 1
            row["words"] += 1
            if candidate.x is None:
                continue
            divisible += 1
            row["divisible"] += 1
            if candidate.x <= 0:
                continue
            positive += 1
            row["positive_integer"] += 1
            if follows_word_and_returns(candidate):
                realized += 1
                row["realized"] += 1
                cycles.add(_primitive_cycle(candidate))
        by_m.append(row)
    return {
        "p": p,
        "b": b,
        "max_m": max_m,
        "words": words,
        "divisible": divisible,
        "positive_integer": positive,
        "realized_word_rows": realized,
        "cycles": tuple(sorted(cycles)),
        "by_m": by_m,
    }


def run_suite(max_m: int) -> dict[str, dict[str, object]]:
    return {
        "3n+1": enumerate_map(3, 1, max_m),
        "3n-1": enumerate_map(3, -1, max_m),
        "5n+1": enumerate_map(5, 1, max_m),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=18)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()
    payload = run_suite(args.max_m)
    text = json.dumps(payload, indent=2) + "\n"
    if args.output:
        from pathlib import Path

        Path(args.output).write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")
