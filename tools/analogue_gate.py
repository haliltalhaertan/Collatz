#!/usr/bin/env python3
"""
analogue_gate.py -- finite value diagnostic and fail-closed claim-review gate.

Grid observations are not universal proofs or claim-level separation. CP24 section 3
separately proves built-in Ecal's reflection invariance for 3n+1 / 3n-1. Together
with the positive 5 -> 7 -> 10 -> 5 witness, it blocks cycle-exclusion arguments
using only invariant observations and hypotheses valid on both maps. A shared
auxiliary lemma can still be useful with additional map-specific information.

Usage: python tools/analogue_gate.py [--diagnostic] [--max-m 11] [--max-r 5]
                                   [--json tools/analogue_gate_verdict.json]
Exit 1: ship gate blocked/unassessed (default; no automatic claim approval).
Exit 0: explicit --diagnostic completed, NOT claim approval (also --help).
Exit 2: invalid/empty input, consistency failure or JSON output I/O failure.

Exact integer/Fraction arithmetic. Enumeration remains exponential in max_m;
see ANALOGUE_GATE.md for scope, bounds, extension API and resource costs.
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
        if v % 2 != 0:
            raise ValueError(f"(p*x+b) must be even for odd x: p={p} b={b} x={x}")
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
        e, k = h, 0
        for _ in range(m):
            k += e % 2
            e = H_step(e, p, b)
        if k not in hist:
            hist[k] = [0] * q
        hist[k][e % q] += 1
    # Explicit raises survive python -O; missing strata must not silently vanish.
    if set(hist) != set(range(1, m + 1)):
        raise AssertionError(f"missing or unexpected strata at m={m}, r={r}")
    for k, vec in hist.items():
        if sum(vec) != n_k(m, k):
            raise AssertionError(f"stratum mass mismatch at m={m}, r={r}, k={k}")
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
    """Bounded positive cycle witnesses, not a cycle-absence decision.

    Starts: 1 <= start < limit; states: 0 < x < 400*limit;
    at most 4000 steps per start. Exclude the conventional {1}, {1,2}
    cycles. Rotate to the minimum; never sort vertices out of orbit order.
    An empty list means only NOT_FOUND_WITHIN_BOUNDS.
    """
    seen, cycles = set(), []
    for start in range(1, limit):
        x, path, idx = start, [], {}
        while x not in idx and 0 < x < limit * 400 and len(path) < 4000:
            idx[x] = len(path)
            path.append(x)
            x = H_step(x, p, b)
        if x in idx:
            cyc = path[idx[x]:]
            key = frozenset(cyc)
            if key not in seen and set(cyc) != {1, 2} and set(cyc) != {1}:
                seen.add(key)
                pivot = cyc.index(min(cyc))
                cycles.append(cyc[pivot:] + cyc[:pivot])
    return cycles


# ---------------------------------------------------------------- gate

MAPS = {
    "3n+1": (3, 1),
    "3n-1": (3, -1),
    "5n+1": (5, 1),
}


def run_gate(max_m: int = 11, max_r: int = 5, *, quantity=None) -> dict:
    """Finite value diagnostic; custom exact quantities never inherit CP24's proof."""
    builtin = quantity is None
    measure = Ecal if builtin else quantity
    if type(max_m) is not int or type(max_r) is not int or max_m < 2 or max_r < 1:
        raise ValueError("max_m must be an integer >= 2 and max_r an integer >= 1")
    grid = [(m, r) for m in range(2, max_m + 1) for r in range(1, min(max_r, m) + 1)]
    if not grid:
        raise ValueError("empty test grid")

    tables: dict[str, dict[str, int | Fraction]] = {}
    for name, (p, b) in MAPS.items():
        table = {}
        for m, r in grid:
            value = measure(m, r, p, b)
            if type(value) not in (int, Fraction):
                raise TypeError(
                    f"quantity must return exact int or Fraction; got {type(value).__name__} "
                    f"for map={name}, m={m}, r={r}"
                )
            table[f"{m},{r}"] = value
        tables[name] = table

    base = tables["3n+1"]
    comparisons = {}
    for name in ("3n-1", "5n+1"):
        other = tables[name]
        diffs = [kk for kk in base if base[kk] != other[kk]]
        cycles = find_cycles(*MAPS[name])  # one bounded search per analogue
        comparisons[name] = {
            "rows_compared": len(base),
            "rows_differing": len(diffs),
            "identical": len(diffs) == 0,
            "value_status": "VALUE_SEPARATES_ON_TEST_GRID" if diffs else "BLIND_ON_TEST_GRID",
            "first_differences": diffs[:5],
            "cycle_search_status": "WITNESS_FOUND" if cycles else "NOT_FOUND_WITHIN_BOUNDS",
            "example_cycles": cycles[:2],
        }

    blind_on_grid = [name for name, c in comparisons.items() if c["identical"]]
    verdict = "BLIND_ON_TEST_GRID" if blind_on_grid else "VALUE_SEPARATES_ON_TEST_GRID"
    analytic = None
    if builtin:
        if not comparisons["3n-1"]["identical"] or [5, 7, 10] not in comparisons["3n-1"]["example_cycles"]:
            raise AssertionError("built-in Ecal reflection/witness regression failed")
        analytic = {
            "status": "PROVED_BLIND",
            "analogue": "3n-1",
            "citation": "bagimsiz-denetim/06-cp24-recovery-20260914/CP24_REPORT.md, section 3",
            "scope": (
                "For all integers m>=1, r>=1, Ecal(m,r;3,+1)=Ecal(m,r;3,-1). "
                "Only cycle-exclusion arguments using reflection-invariant observations "
                "and the same hypotheses valid on both maps are obstructed. "
                "Shared auxiliary lemmas remain useful with additional map-specific hypotheses."
            ),
            "basis": "CP24 analytic reflection derivation, not the finite grid; not formal verification",
            "positive_cycle_witness": [5, 7, 10],
        }

    return {
        "gate": "analogue_filter",
        "source": "CP24 scope correction to CP23 chain-kill",
        "quantity": "Ecal(m,r) - odd-character source energy" if builtin else "custom exact quantity",
        "grid_rows": len(grid),
        "max_m": max_m,
        "max_r": max_r,
        "grid_scope": "2 <= m <= max_m; 1 <= r <= min(max_r,m)",
        "comparisons": comparisons,
        "cycle_search_bounds": {"start_min": 1, "start_max_exclusive": 4000,
                                "state_min_exclusive": 0, "state_max_exclusive": 1600000,
                                "max_steps_per_start": 4000,
                                "excluded_vertex_sets": [[1], [1, 2]]},
        "blind_on_test_grid_to": blind_on_grid,
        "verdict": verdict,
        "analytical_result": analytic,
        "ship_gate": {"approved": False,
                      "status": "BLOCKED_FOR_STATED_SCOPE" if builtin else "NOT_ASSESSED"},
        "meaning": (
            "Grid verdicts compare values only, not claim truth or universal behaviour. "
            "A value difference does not establish claim-level separation. "
            "This diagnostic never authorizes a claim; an explicit claim and its hypotheses need review."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="CP24-scoped analogue diagnostic and fail-closed ship gate")
    ap.add_argument("--max-m", type=int, default=11)
    ap.add_argument("--max-r", type=int, default=5)
    ap.add_argument("--json", metavar="PATH", help="write result as JSON (not approval)")
    ap.add_argument("--diagnostic", action="store_true",
                    help="exit 0 after a valid diagnostic, never claim approval")
    args = ap.parse_args()
    if args.max_m < 2 or args.max_r < 1:
        ap.error("--max-m must be >= 2 and --max-r must be >= 1 (empty grids forbidden)")

    try:
        # Finite regression, not CP24's analytic proof.
        for m in range(1, 9):
            for h in range(1, 1 << m, 2):
                if parity_word(h, m, 3, 1) != parity_word((1 << m) - h, m, 3, -1):
                    raise AssertionError("reflection identity broken")
        res = run_gate(args.max_m, args.max_r)
        if res["grid_rows"] <= 0:
            raise ValueError("empty test grid")
        if args.json:
            with open(args.json, "w", encoding="utf-8", newline="\n") as f:
                json.dump(res, f, indent=1)
                f.write("\n")
    except (ValueError, AssertionError, OSError) as exc:
        print(f"GATE ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"ANALOGUE GATE - {res['quantity']}")
    print(f"grid rows: {res['grid_rows']} (m <= {res['max_m']}, r <= min({res['max_r']}, m))")
    for name, c in res["comparisons"].items():
        print(f"  3n+1 vs {name}: {c['value_status']} ({c['rows_differing']}/{c['rows_compared']} rows differ)")
        print(f"    cycles: {c['cycle_search_status']}; examples in orbit order: {c['example_cycles']}")
    print(f"VERDICT: {res['verdict']}")
    if res["analytical_result"]:
        proof = res["analytical_result"]
        print(f"ANALYTIC: {proof['status']} - {proof['citation']}")
        print(f"  Scope: {proof['scope']}")
    print(f"SHIP GATE: {res['ship_gate']['status']} (not claim approval)")
    if args.json:
        print(f"wrote {args.json}")
    if args.diagnostic:
        print("DIAGNOSTIC ONLY: completed; not claim approval")
        return 0
    # A finite raw-value diagnostic cannot approve an unspecified claim.
    return 1


if __name__ == "__main__":
    sys.exit(main())
