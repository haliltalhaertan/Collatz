# Analogue Gate — finite diagnostics, scoped proof, fail-closed review

`tools/analogue_gate.py` uses exact integer / `Fraction` arithmetic and reconstructs
histograms from the map definitions, without importing the CP23 engine.
**Collatz is not solved.**

## What the analogue argument does and does not say

[CP24_REPORT.md, section 3](../bagimsiz-denetim/06-cp24-recovery-20260914/CP24_REPORT.md)
proves analytically that for all integers `m>=1, r>=1`,
`Ecal(m,r;3,+1) = Ecal(m,r;3,-1)`. The identity `H_-(-x)=-H_+(x)` matches
parity words, reflects endpoints by `e -> 3^k-e`, and permutes the squared
complementary-bin differences defining `J_r`. The positive `3n-1` cycle
`5 -> 7 -> 10 -> 5` is an exact witness.

This obstructs **only** a cycle-exclusion argument using reflection-invariant
observations and the **same hypotheses** valid on both maps. Adding sign, magnitude,
initial labels or map-specific conditions need not preserve that argument.
An **auxiliary lemma** can be useful even when true for both maps; it is not required
to separate their raw values. This is not an impossibility theorem about all mixing,
modular or combinatorial methods.

The finite grid is a regression test, not the analytic proof. Similarly, different
raw values do not establish different truth values for a claim. The targeted tests
also evaluate `Ecal(m,s+1) >= Ecal(m+1,s)` for `2<=m<=10, 1<=s<=min(4,m)`:
33 pairs on each map. Such finite predicate checks are still not universal theorems.

## Three separate layers in JSON

| Field / status | Meaning |
|---|---|
| comparison `BLIND_ON_TEST_GRID` | Values match this analogue on the stated finite grid only. |
| comparison `VALUE_SEPARATES_ON_TEST_GRID` | At least one value differs on this finite grid; not claim separation. |
| top-level `verdict` | `BLIND_ON_TEST_GRID` if at least one tested analogue matches every row; otherwise `VALUE_SEPARATES_ON_TEST_GRID`. Independent of whether a cycle was found. |
| `analytical_result.status = PROVED_BLIND` | Built-in Ecal only: external analytic derivation with explicit scope, citation and positive cycle witness. Not inferred from the grid and not kernel-verified. |
| `ship_gate` | Always `approved: false`. Built-in: `BLOCKED_FOR_STATED_SCOPE`. Custom quantity: `NOT_ASSESSED`. |

The default grid is `2<=m<=11, 1<=r<=min(5,m)`: **44 rows**, **0 differences**
against `3n-1`, **38 differences** against `5n+1`. Thus the obstruction specifically
comes from the reflected `3n-1` partner; no analogous universal invariance theorem
is asserted for `5n+1`.

## CLI and exit contract

```bash
python -B tools/analogue_gate.py
# exit 1: valid diagnostic, built-in energy-only cycle-exclusion route blocked

python -B tools/analogue_gate.py --diagnostic
# exit 0: computation completed; NEVER claim approval

python -B tools/analogue_gate.py --diagnostic --max-m 11 --max-r 5 --json tools/analogue_gate_verdict.json
# regenerate the checked-in diagnostic; JSON still says approved:false

python -B -m unittest discover -s tools -p test_analogue_gate.py -v
```

| Exit | Contract |
|---|---|
| `0` | Explicit `--diagnostic` completed, or `--help` displayed. Not a ship approval. |
| `1` | Default ship mode: blocked or unassessed. Neither matching nor different raw values can approve an unspecified claim. |
| `2` | Invalid arguments, empty grid, detected internal consistency failure, or JSON I/O error. Applies in diagnostic mode too. |

`max_m>=2` and `max_r>=1` are mandatory integers. Zero, negative and empty CLI
values fail rather than producing a vacuous verdict. No upper bound is silently
imposed: choose resource limits deliberately. On Windows use native `C:/...` paths.
Invalid input does not replace an old JSON file: consumers must check this invocation's
exit code and must not treat a stale artifact as a new result. Unexpected runtime
exceptions also fail nonzero; exit 2 is the handled validation/consistency/I/O contract.

A publication pipeline must review the explicit claim, quantifiers and hypotheses;
it must not treat `--diagnostic` success as passing that review. This tool intentionally
has **no automatic approval path**. Shared lemmas are not rejected by the scoped
mathematical obstruction; their usefulness and the full proof need separate review.

## Runtime and regression checks

- The CLI checks reflected parity words for `m<=8` before measurement.
- Every generated histogram must contain exactly the strata `k=1,...,m` and satisfy
  `sum(P_k) == C(m-1,k-1)`. Explicit exceptions retain these checks under `python -O`.
- Endpoints are counted directly into `e % 2^r`; no truncation is used.
  Tests independently compare fine-to-coarse modulo sums for all three maps on the
  default grid, and test parity, endpoint and energy reflection through `m=12`.
- Cycle witnesses are strictly positive, rotated to their smallest element, and retain
  **orbit order**, including the closing edge. Examples are `[5,7,10]` and
  `[1,3,8,4,2]`, not sorted sets of vertices.
- `find_cycles` is bounded: starts `1<=start<4000`, states `0<x<1600000`, at most
  4000 steps per start. The conventional vertex sets `{1}` and `{1,2}` are excluded.
  These exclusions are a reporting convention, not a universal definition of
  nontriviality for new maps. `WITNESS_FOUND` certifies displayed cycles;
  `NOT_FOUND_WITHIN_BOUNDS` means only that search found none, **not** that none exist.

## Extending the diagnostic, not importing an Ecal theorem

Use the Python API `run_gate(max_m, max_r, quantity=my_exact_quantity)`, with
`my_exact_quantity(m,r,p,b)` returning an exact integer or `Fraction`. Keep the
`(p,b)` meaning and evaluate the same coordinates on all three maps. A custom
quantity receives only finite value statuses, `analytical_result: null` and
`ship_gate: {approved: false, status: NOT_ASSESSED}`. Even explicitly passing an
Ecal wrapper does not inherit the built-in proof. Do not replace built-in Ecal
in place and leave its proof annotation attached to an unrelated observable.

For a claim-level investigation, separately specify its logical predicate and
hypotheses, check that they transfer, and give a quantified analytic argument where
one is claimed. A different quantity needs its own proof/citation, not 44 equal rows.

## Cost and limits

Enumeration remains **exponential**. At fixed small `R=max_r`, orbit work over
`m<=M` is approximately `Theta(R*M*2^M)` map steps (three maps). Large `R` also
costs dense histogram allocation/energy work; a per-row histogram has `O(m*2^r)`
entries. Bit complexity of large integer and Fraction operations adds further cost.

Parity count and endpoint now share one walk per start, histogram vectors are
allocated only once per stratum, and cycle search is called once per analogue.
However, the same orbits are still recomputed for each resolution `r`; this is a
small-window reference diagnostic, not an optimized large-sweep engine. No new
large search, asymptotic decay theorem, Mixed-Gram impossibility theorem, human
review or formal verification is supplied by these repairs.
