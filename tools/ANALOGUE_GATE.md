# Analogue Gate — CP23 ship-gate, executable

`tools/analogue_gate.py`

## The rule

CP23 proved: `3n+1` and `3n-1` have **identical** `Ecal` tables, because
`H_{3n-1}(-x) = -H_{3n+1}(x)` and the energy functional is blind to the sign of the
affine constant. But `3n-1` has nontrivial cycles (`5 -> 7 -> 10 -> 5`).

> **A quantity that does not separate `3n+1` from a CYCLING analogue cannot carry a
> Collatz-specific claim.** Any proof built on it applies verbatim where cycles exist.

This is a mandatory gate in the publication cycle: run it before labelling anything
as Collatz progress.

## Result on the programme's own target quantity

```
$ python tools/analogue_gate.py --max-m 11

ANALOGUE GATE — Ecal(m,r) — odd-character source energy
grid rows: 44 (m <= 11)
  3n+1 vs 3n-1 : IDENTICAL                    | has cycles  e.g. [5, 7, 10]
  3n+1 vs 5n+1 : differs on 38 rows           | has cycles  e.g. [1, 2, 3, 4, 8]

VERDICT: BLIND
  Blind to: 3n-1
  => This quantity CANNOT carry a Collatz-specific claim.
```

Independent reproduction of CP23's central finding, from definitions, with no reuse of
the CP23 engine: 44 `(m,r)` rows, zero differences against `3n-1`, and the cycle
`[5,7,10]` located by direct search.

Note `5n+1` **differs on 38/44 rows** — it is not blind. The kill comes specifically
from `3n-1`, the sign-flipped partner, exactly as the reflection identity predicts.

## Verdicts

| verdict | meaning |
|---|---|
| `BLIND` | identical values on a map that provably has cycles → not Collatz-specific |
| `SEPARATES` | distinguishes `3n+1` from its cycling analogues → **necessary, not sufficient** |

`SEPARATES` is not a licence to claim Collatz progress. It only means the quantity
survived this filter.

## Self-check

Before measuring, the script verifies CP24's reflection identity on `m <= 8`: the
`3n+1` orbit from `h` and the `3n-1` orbit from `2^m - h` must produce the same parity
word. Exit code `2` if that fails.

All arithmetic is exact integer / `Fraction`. No floating point decides anything.

## Usage

```bash
python tools/analogue_gate.py                        # default sweep, m <= 11
python tools/analogue_gate.py --max-m 13             # larger sweep (slower)
python tools/analogue_gate.py --json verdict.json    # machine-readable
```

On Windows pass a native path (`C:/...`) to `--json`; an MSYS-style `/c/...` path fails.

## Extending to a new claim

The built-in gate measures `Ecal`. For a different quantity, replace the `Ecal` call in
`run_gate()` with that quantity's exact computation, keeping the same `(p, b)`
parametrisation so the same grid is evaluated on all three maps.
