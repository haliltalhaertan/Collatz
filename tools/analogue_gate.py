#!/usr/bin/env python3
"""
analogue_gate.py — CP23 ship-gate, executable form.

CP23 proved the programme's intended route is dead: `3n+1` and `3n-1` have identical
Ecal tables, because H_{3n-1}(-x) = -H_{3n+1}(x) and the energy functional is blind to
the sign of the affine constant. But `3n-1` has nontrivial cycles (5 -> 7 -> 10 -> 5).
So any claim that also holds for `3n-1` (or `5n+1`, which also cycles) cannot be
about Collatz specifically.

THE RULE: a quantity that does NOT separate 3n+1 from its cycling analogues cannot
carry a Collatz-specific claim. This script measures that separation exactly.

Usage:
    python tools/analogue_gate.py                 # built-in Ecal gate over a default grid
    python tools/analogue_gate.py --json out.json # machine-readable verdict
    python tools/analogue_gate.py --max-m 12      # smaller/larger sweep

Exit codes:
    0 = gate produced a verdict (read it; BLIND means the claim is not Collatz-specific)
    2 = internal consistency failure (a cross-check assertion failed)

All arithmetic is exact integer / Fraction. No floating point decides anything.
"""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction


# ---------------------------------------------------------------- maps

def H_step(x: int, p: int, b: int) -> int:
    """Shortcut map: odd -> (p*x + b)/2, even -> x/2. Requires p*x+b even for odd x."""
    if x % 2:
        v = p * x + b
        assert v % 2 == 0, f"(p*x+b) must be even for odd x: p={p} b={b} x={x}"
        return v // 2
    return x // 2


def parity_word(h: int, m: int, p: int, b: int) -> tuple[int, ...]:
    """First m parities (1 = odd step) starting from h."""
    w, x = [], h
    for _ in range(m):
        w.append(x % 2)
        x = H_step(x, p, b)
    return tuple(w)


def endpoint(h: int, m: int, p: int, b: int) -> int:
    x = h
    for _ in range(m):
        x = H_step(x, p, b)
    return x


# ---------------------------------------------------------------- Ecal

def source_histograms(m: int, r: int, p: int, b: int) -> dict[int, list[int]]:
    """P_{m,k,r}: for odd h < 2^m with k odd-steps, count endpoints mod 2^r."""
    q = 1 << r
    hist: dict[int, list[int]] = {}
    for h in range(1, 1 << m, 2):
        w = parity_word(h, m, p, b)
        k = sum(w)
        e = endpoint(h, m, p, b)
        hist.setdefault(k, [0] * q)[e % q] += 1
    return hist


def J_r(vec: list[int], r: int) -> int:
    """Odd-character energy: 2^(r-1) * sum over half of (X(u) - X(u+2^(r-1)))^2."""
    half = 1 << (r - 1)
    return half * sum((vec[u] - vec[u + half]) ** 2 for u in range(half))


def n_k(m: int, k: int) -> int:
    from math import comb
    return comb(m - 1, k - 1)


def Ecal(m: int, r: int, p: int, b: int) -> Fraction:
    """Ecal(m,r) = sum_k J_r(P_k)/n_k — exact rational."""
    total = Fraction(0)
    for k, vec in source_histograms(m, r, p, b).items():
        nk = n_k(m, k)
        if nk:
            total += Fraction(J_r(vec, r), nk)
    return total


# ---------------------------------------------------------------- cycles

def find_cycles(p: int, b: int, limit: int = 4000) -> list[list[int]]:
    """Nontrivial positive cycles of the shortcut map, searched up to `limit`."""
    seen, cycles = set(), []
    for start in range(1, limit):
        x, path, idx = start, [], {}
        while x not in idx and x < limit * 400 and len(path) < 4000:
            idx[x] = len(path)
            path.append(x)
            x = H_step(x, p, b)
        if x in idx:
            cyc = path[idx[x]:]
            key = frozenset(cyc)
            if key not in seen and set(cyc) != {1, 2} and set(cyc) != {1}:
                seen.add(key)
                cycles.append(sorted(cyc))
    return cycles


# ---------------------------------------------------------------- gate

MAPS = {
    "3n+1": (3, 1),
    "3n-1": (3, -1),
    "5n+1": (5, 1),
}


def run_gate(max_m: int = 11, max_r: int = 5) -> dict:
    grid = [(m, r) for m in range(2, max_m + 1) for r in range(1, min(max_r, m) + 1)]

    tables: dict[str, dict[str, str]] = {}
    for name, (p, b) in MAPS.items():
        tables[name] = {f"{m},{r}": str(Ecal(m, r, p, b)) for (m, r) in grid}

    base = tables["3n+1"]
    comparisons = {}
    for name in ("3n-1", "5n+1"):
        other = tables[name]
        diffs = [kk for kk in base if base[kk] != other[kk]]
        comparisons[name] = {
            "rows_compared": len(base),
            "rows_differing": len(diffs),
            "identical": len(diffs) == 0,
            "first_differences": diffs[:5],
            "has_nontrivial_cycles": bool(find_cycles(*MAPS[name])),
            "example_cycles": [c for c in find_cycles(*MAPS[name])[:2]],
        }

    # A quantity is Collatz-specific only if it separates 3n+1 from every CYCLING analogue.
    blind_to = [n for n, c in comparisons.items()
                if c["identical"] and c["has_nontrivial_cycles"]]
    verdict = "BLIND" if blind_to else "SEPARATES"

    return {
        "gate": "analogue_filter",
        "source": "CP23 chain-kill, 2026-09-14",
        "quantity": "Ecal(m,r) — odd-character source energy",
        "grid_rows": len(grid),
        "max_m": max_m,
        "comparisons": comparisons,
        "blind_to": blind_to,
        "verdict": verdict,
        "meaning": (
            "BLIND: the quantity takes identical values on a map that provably HAS cycles, "
            "so no claim built on it can exclude cycles for 3n+1. It is not Collatz-specific. "
            "SEPARATES: the quantity distinguishes 3n+1 from its cycling analogues and may "
            "carry a Collatz-specific claim (necessary, not sufficient)."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="CP23 analogue filter ship-gate")
    ap.add_argument("--max-m", type=int, default=11)
    ap.add_argument("--max-r", type=int, default=5)
    ap.add_argument("--json", metavar="PATH", help="write verdict as JSON")
    args = ap.parse_args()

    # self-check: the reflection identity CP24 proved, on a small window
    for m in range(1, 9):
        for h in range(1, 1 << m, 2):
            if parity_word(h, m, 3, 1) != parity_word((1 << m) - h, m, 3, -1):
                print("SELF-CHECK FAILED: reflection identity broken", file=sys.stderr)
                return 2

    res = run_gate(args.max_m, args.max_r)

    print(f"ANALOGUE GATE — {res['quantity']}")
    print(f"grid rows: {res['grid_rows']} (m <= {res['max_m']})")
    for name, c in res["comparisons"].items():
        state = "IDENTICAL" if c["identical"] else f"differs on {c['rows_differing']} rows"
        cyc = "has cycles" if c["has_nontrivial_cycles"] else "no cycles found"
        ex = f"  e.g. {c['example_cycles'][0]}" if c["example_cycles"] else ""
        print(f"  3n+1 vs {name:5s}: {state:28s} | {cyc}{ex}")
    print(f"\nVERDICT: {res['verdict']}")
    if res["verdict"] == "BLIND":
        print(f"  Blind to: {', '.join(res['blind_to'])}")
        print("  => This quantity CANNOT carry a Collatz-specific claim.")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=1)
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
