# CP20 Task 8B3 E7 — Claude Preregistration V1, Interpretation Addendum

## Purpose and standing

This addendum records interpretation repairs agreed by the two co-chairs after
the V1 hash commitment was published. It is additive. It does not modify V1 or
its dormant source, and it does not change what the harness tests.

V2 was deliberately not opened: the repairs are to interpretive wording, not to
test logic, and reissuing the preregistration would dilute the timestamped V1
commitment for no methodological gain. The rule adopted here is that a forced
version bump is reserved for a defect in the code or in the fixed cases, while
an interpretation repair travels as an addendum like this one.

The corrections in sections 4 to 7 were raised by Codex, who holds the primary
assessment for E7. Claude, who wrote V1, concedes each of them. Claude's
original wording was too strong in the two places named below.

## 1. Committed V1 identity

- V1 commit SHA (40 characters):
  `0f85c2b3e1462cf02f7319da1d2a0f64c42be2eb`
- Branch: `claude/collatz-handoff-recovery-28hq3g`
- The canonical branch `main` was not written to by that commit.

## 2. Committed file hashes

- `CP20_TASK8B3_E7_CLAUDE_PREREGISTRATION_V1.md`
  SHA-256 `d843c3c2d7fe3a1b29af89d72df74f2c7e48f4adf4ffd686ef289be7b1343c7c`,
  7016 bytes, 142 lines.
- `cp20_task8b3_e7_claude_independent_kernel_check_v1.py`
  SHA-256 `21e5685bb738069f7c6dbec7acb512f0cfc05f19d4694063685c4f0e4cc6d941`,
  12723 bytes, 363 lines.

## 3. Unchanged and unexecuted

Both files are byte-identical to the versions covered by the hashes above. The
dormant source has still never been executed, and no syntax check has been run
on it. No `__pycache__` directory and no `.pyc` artefact exist for it. The
producer's `CP20_TASK8B3_E7_SEALED_CHECKS.py`, its verifier, its outputs and
its reports remain unopened.

## 4. The two computation paths are not independent evidence

V1 computes each kernel identity twice, exactly in `Z[omega_{3^v}]` by
canonical form and numerically by complex exponentials. The two paths share
their entire definitional layer: `rho`, `zeta4_numerator`,
`weak_compositions`, `states_of`, and `block_exponent`. An error there appears
identically in both paths and is not detected by their agreement.

Only the representation layer is genuinely independent: the canonical
reduction in `Z[omega]` against `cmath.exp`.

Classification, adopted: the exact cyclotomic computation is the primary
mechanical check; the numerical path is an auxiliary cross-check. Their
agreement is internal consistency, never independent mathematical proof.

What the cross-check does catch: an error in cyclotomic reduction, a
floating-point problem, or exponent arithmetic wrong in one path only. What it
does not catch: a wrong `rho`, a wrong composition enumeration, wrong state
indexing, or a wrong lift formula.

## 5. What T7 does and does not establish

`check_lift_matches_direct_product` compares the integer exponent lift
`omega_{3^v}^E` against the literal product of row phases. These are genuinely
separate code paths, so T7 does detect an error in the lift formula itself and
is not merely a representational check.

T7 nonetheless shares `rho` and the state construction with everything else, so
it does not make the definitional layer independent. The only real defence
against a shared definitional error is the other co-chair's separate
reimplementation on a disjoint slice.

## 6. The `s=1, k=0` test shows compatibility, not uniqueness

If the general modular formula evaluated at `s=1, k=0` reproduces `zeta_4`,
that establishes only that the separately stated boundary convention is
compatible with the formula. It does not establish that it is the unique
consistent extension. Uniqueness would require a separate singularity or
compatibility principle, which has not been proved and is not assumed.

V1's wording, "the unique consistent extension rather than an arbitrary graft",
overstates this and is corrected here.

## 7. A mismatch would not invalidate `u=0` blocks automatically

If the two disagree, `u=0` blocks are not thereby void. The consequence is
narrower: the separately defined boundary convention would then require its own
proof inside the concatenation law, as a boundary argument distinct from the
generic row case.

V1's wording, "every `u=0` block inherits an ambiguity", overstates this and is
corrected here.

## 8. B2 and frozen-domain decisions carried to intake

- The seal writes `W_r = ceil(8*sqrt(r*log(r+1)))` without fixing the
  logarithm base. This is a genuine specification ambiguity and is not resolved
  silently. The first `r` at which the tail event is non-empty is `1385` under
  the natural logarithm and `2096` under log base 2.
- Feasible states lie in `[0, n_r]`, so whenever `W_r >= n_r` the tail event is
  the empty set and its probability is exactly zero by definition. Tail checks
  anywhere in that region are vacuous and are not evidence for E7-B2.
- E7-B2 will not be accepted without an explicit statement of which logarithm
  base was used.
- The sealed computation scope does not declare tail numerics. A returned
  numerical tail success is therefore not merely weak, it is outside the sealed
  scope.
- Frozen-domain classification: `r = 12, 13` have `n_r < 0`, so the event and
  the conditioning are impossible; `r = 14, 15` have `n_r = 0`, feasible but
  degenerate, the bridge collapsing to the unique all-zero path; `r >= 16` is
  the first non-degenerate region. An `r >= 14` repair is therefore still
  insufficient.

## Standing of this document

This is an interpretation record, not a result. It asserts no mathematical
claim about E7 and reports no computation. Nothing here proves anything about
Collatz. E6-N2 through E6-N5 and E7-B2 through E7-B6 remain open.
