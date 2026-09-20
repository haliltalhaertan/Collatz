# Manager Decision — CP23/CP24 Chain-Kill Integration and Sign-Sensitive Pilot

**Date:** 2026-09-20  
**Status:** ACCEPTED (scope-limited)  
**Collatz status:** OPEN / NOT PROVED

## Accepted

1. CP21–CP24 and the mixed-Gram branch are now present on canonical `main` through PRs #2–#6.
2. CP24 proves the scoped reflection statement for the built-in energy observable: under the stated shared hypotheses, the `3n+1` and `3n−1` energy tables agree analytically. The 44-row executable grid is a finite regression check, not the proof.
3. The executable analogue diagnostic is accepted as a fail-closed research tool. A finite `BLIND_ON_TEST_GRID` or `VALUE_SEPARATES_ON_TEST_GRID` result is not a theorem and not claim approval.
4. Shared auxiliary lemmas need not distinguish `3n+1` from analogues. The obstruction applies only when the proposed conclusion relies solely on reflection-invariant data and hypotheses shared by the compared maps.
5. The earlier inference from finite, unnormalised fixed-resolution energy data to failure of asymptotic decay is withdrawn.
6. Mixed-Gram work is strategically paused because no bridge from that recurrence to sign-sensitive cycle exclusion is established. This is not an impossibility theorem for the recurrence.

## Prohibited inferences

- Do not claim that every lemma valid for `3n−1` is useless for Collatz.
- Do not promote finite-grid agreement or disagreement to a universal theorem.
- Do not use the 44-row regression as the proof of CP24's analytic reflection result.
- Do not claim that the finite raw-energy observations refute an asymptotic normalised statement.
- Do not claim that Mixed-Gram methods are mathematically impossible.
- Do not claim Collatz is solved.

## Exactly one next action

Open `CP25_SIGN_SENSITIVE_CYCLE_PILOT_20260920`.

Start from the exact affine cycle equation for the shortcut maps,

`(2^m - 3^k) x = b B_w`, with `b in {+1,-1}`,

and test whether the sign of `2^m-3^k`, together with exact integrality and parity-word realisability, yields a statement that separates positive `3n+1` cycle candidates from positive `3n−1` cycle candidates. Produce:

1. a written quantified statement and derivation from definitions;
2. a deterministic exact-arithmetic enumerator that does not import archive engines;
3. finite tables clearly labelled `[EXACT COMPUTATION]`;
4. explicit kill conditions: stop if the candidate is reflection-invariant, merely restates positivity, or supplies no bridge beyond the classical cycle equation;
5. an analogue check against `3n−1` and `5n+1`.

No novelty or proof claim is permitted without literature review and independent mathematical verification.
