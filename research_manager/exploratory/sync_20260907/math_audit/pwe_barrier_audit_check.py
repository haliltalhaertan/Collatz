"""Independent bounded checks for the PWE/barrier review.

This file deliberately imports no project or producer module.  It evaluates
only representative cases from the producer's predeclared finite set.  All
outputs are numerical evidence, never theorem evidence.
"""

import cmath
import json
import math
from pathlib import Path


ALPHA = math.log2(3.0)
BETA = ALPHA - 1.0
OUT = Path(__file__).with_name("PWE_BARRIER_AUDIT_CHECK.json")


def critical_total(r: int) -> int:
    return math.floor(BETA * r) - 8


def root_phase(modulus: int, exponent: int) -> complex:
    angle = 2.0 * math.pi * pow(2, exponent, modulus) / modulus
    return cmath.exp(1j * angle)


def independent_h(r: int, j: int) -> complex:
    """Coefficient DP: new[z] = sum_{p<=z} old[p]*row_phase(p)."""
    rows = r - 4
    total = critical_total(r) - j
    old = [0j] * (total + 1)
    old[0] = 1.0 + 0j
    for row in range(1, rows + 1):
        modulus = 3 ** (row + 4)
        new = [0j] * (total + 1)
        running = 0j
        for z in range(total + 1):
            running += old[z] * root_phase(modulus, j + row - 1 + z)
            new[z] = running
        old = new
    return old[total] / math.comb(total + rows - 1, rows - 1)


def independent_g(r: int, barrier=None):
    """Direct transition DP, with a barrier imposed before each row."""
    total = critical_total(r)
    amps = [0j] * (total + 1)
    ways = [0] * (total + 1)
    amps[0] = 1.0 + 0j
    ways[0] = 1
    for row in range(1, r + 1):
        modulus = 16 * 3 ** row
        next_amps = [0j] * (total + 1)
        next_ways = [0] * (total + 1)
        for before in range(total + 1):
            delta = before - BETA * row - 5.0
            if barrier is not None and delta > barrier + 2e-15:
                continue
            weighted = amps[before] * root_phase(modulus, row - 1 + before)
            for after in range(before, total + 1):
                next_amps[after] += weighted
                next_ways[after] += ways[before]
        amps, ways = next_amps, next_ways
    denom = math.comb(total + r - 1, r - 1)
    return amps[total] / denom, ways[total], denom


def main() -> None:
    h_cases = [(30, j) for j in (6, 7, 8, 9)] + [(60, 12), (60, 13)]
    h_rows = []
    for r, j in h_cases:
        value = independent_h(r, j)
        h_rows.append({"r": r, "j": j, "real": value.real,
                       "imag": value.imag, "absolute": abs(value)})

    full, full_count, denom = independent_g(30)
    barrier_rows = []
    for threshold in (-4, 0):
        inside, count, check_denom = independent_g(30, threshold)
        assert check_denom == denom
        barrier_rows.append({
            "r": 30,
            "threshold": threshold,
            "probability": count / denom,
            "inside_absolute": abs(inside),
            "outside_absolute": abs(full - inside),
            "decomposition_residual": abs(full - (inside + (full - inside))),
        })

    payload = {
        "classification": "NUMERICAL_REPRESENTATIVE_REPRODUCTION_ONLY",
        "implementation": "independent direct-transition/coefficient DP",
        "h": h_rows,
        "barrier": barrier_rows,
        "g30_absolute": abs(full),
        "unrestricted_count": full_count,
        "expected_unrestricted_count": denom,
        "count_normalization_pass": full_count == denom,
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
