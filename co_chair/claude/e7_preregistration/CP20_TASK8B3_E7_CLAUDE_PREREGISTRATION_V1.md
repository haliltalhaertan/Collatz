# CP20 Task 8B3 E7 — Claude Independent Reproduction, Preregistration V1

## Status

Outcome-free preregistration. Written before the E7 Stage 1 package was seen.
The companion source was never executed, and no syntax check was run, before
this document and that source were hashed.

This is not an E7 computation. It produces no E7 result and asserts no
mathematical claim. It fixes in advance what will be checked, so that the later
check cannot be tuned to the producer's output.

## Co-chair context

Codex holds the primary mathematical and artifact assessment for E7. Claude
holds the independent adversarial review and this reproduction, because Claude
authorized E7 Stage 1 and must not be the sole judge of its result.

Sources used: the E7 pre-run seal document (sections 3-5) and the accepted
E5-S1 and E6-N1 identities. Not used, and not opened: the producer's
`CP20_TASK8B3_E7_SEALED_CHECKS.py`, its verifier, its outputs, and its reports.

## Independence discipline

1. No producer module is imported, and no producer source was read.
2. Every definition is rebuilt from the seal document's own statements.
3. The source has its own SHA-256, distinct from any producer artifact.
4. The source is dormant until the package returns.
5. After the hash is announced the files do not change. A forced correction
   becomes a V2 preregistration with a stated reason; the V1 hash is kept and
   no silent edit is made.

## Slice ownership

Codex's declared slice: `(2,4,7,3,8)` and `(3,5,7,4,4)`. Both have
`min(s+T) >= 6`, so neither reaches the `s+k<5` modular-inverse branch. This
slice is complementary and deliberately covers that branch.

| Case | `(u,w,v,k,ell)` | Target |
|---|---|---|
| A | `(0,2,5,0,4)` | `u=0` convention together with `2^-3 mod 9` |
| B | `(1,3,6,0,3)` | negative exponent isolated from the `u=0` convention |
| C1 | `(2,4,6,5,3)` | `k>ell`: kernels exactly zero, normalized UNDEFINED |
| C2 | `(0,2,5,1,4)` | `u=0, k!=0`: same contract, propagated through a split |
| D | `u=v=3`, `(k,ell)` in `{(4,4),(4,5)}` | empty-block convention `1_{k=ell}` |
| E | `(8,12,16,2,4)` at `r=24` | central case at the frozen geometry |

A and B are separated on purpose. If a `u=0` block fails, B decides whether the
fault is the boundary convention or the modular-inverse branch.

Case E replaces an earlier `r=12` proposal that Codex correctly rejected:
`n_12 = n_13 = -1`, so `S_r = n_r` is unsatisfiable there. At `r=24`,
`n_24 = 6`, `u = floor(r/3) = 8`, `v = 16`, and the linear bridge centres
`u*n_r/r = 2` and `v*n_r/r = 4` are exactly the chosen `k` and `ell`. The split
`w = 12` is Claude's, chosen as the midpoint.

## Contracts fixed in advance

- `rho(s,k) = 2^(s+k-5) mod 3^s`, with `s+k<5` evaluated by modular inverse and
  never by a real exponent. The six such values with `s>=2` are pinned as a
  table: `(2,0)->8`, `(2,1)->7`, `(2,2)->5`, `(3,0)->7`, `(3,1)->14`,
  `(4,0)->41`.
- The exponent lift `omega_{3^v}^E` must equal the literal product of row
  phases, for every composition in every feasible case.
- `K^+` must satisfy the Vandermonde concatenation identity exactly.
- `K` must satisfy the complex concatenation identity, checked twice: exactly
  in `Z[omega_{3^v}]` by canonical form, and numerically. The two paths must
  agree with each other; a disagreement is itself a reported failure.
- The normalized concatenation weights must sum to exactly one on every
  feasible case.
- Outside the feasible domain the normalized kernel must be UNDEFINED. A
  returned `0` is a contract violation, not a near miss.

## Row-one consistency check

The seal introduces `p^fin_{1,0,4} := zeta_4` as a separate convention, while
`s>=2` uses the modular formula. The harness checks whether the general formula
evaluated at `s=1, k=0` reproduces `zeta_4`. If it does, the convention is the
unique consistent extension rather than an arbitrary graft. If it does not,
every `u=0` block inherits an ambiguity and the concatenation law needs a
separate boundary argument. This is recorded as a question, not an assumption.

## Deliberate omission: the window and the tail

`W_r` and the tail event are absent from the source. Two reasons.

First, the seal writes `W_r = ceil(8*sqrt(r*log(r+1)))` without fixing the
logarithm base. The mathematical default is the natural logarithm, but that is
not stated, and it is not assumed here. The two readings give different
thresholds for the first `r` at which the tail event is non-empty: `r = 1385`
under natural log, `r = 2096` under log base 2.

Second, the feasible states lie in `[0, n_r]`, so the deviation
`max_s |S_s - s*n_r/r|` never exceeds `n_r`. Whenever `W_r >= n_r` the tail
event is the empty set and its probability is exactly zero by definition. That
holds throughout the range where exact enumeration is possible, so no
small-`r` tail computation carries information about E7-B2. Sample values
under natural log: `r=24` gives `n_r=6, W_r=71`; `r=100` gives `50, 172`;
`r=1000` gives `576, 665`; the event first becomes non-empty at `r=1385`.

Neither point is a defect in the asymptotic B2 target. Both bound how a
returned numerical tail statement may be read. The sealed computation scope
does not declare tail numerics at all, so such an output would also be outside
the sealed scope.

## Frozen-geometry and domain findings carried to intake

1. `r = 12, 13`: `n_r < 0`, the conditioned bridge is undefined. The literal
   `r >= 12` is false. Found by Codex.
2. `r = 14, 15`: `n_r = 0`, feasible but degenerate — the bridge collapses to
   the unique all-zero path. An `r >= 14` repair is therefore still
   insufficient; `r >= 16` is the first non-degenerate value.
3. The window is vacuous below `r ~ 1385`, as above.
4. The logarithm base is unspecified.

These enter the intake gate under "frozen geometry and domain audit". They are
not a dissent, and they are not grounds to interrupt the sealed run.

## Execution order after the package returns

1. Run this source once, before any producer file is opened.
2. Hash its output immediately.
3. Confirm the source hash still matches the announced hash.
4. Only then open the producer package.
5. Write the comparison and the adversarial assessment.

Assessments follow commit-reveal: each co-chair completes its text without
seeing the other's, both SHA-256 commitments are recorded, and only then are
the texts exchanged.

## Known risk of this preregistration

The source was written blind and never executed, so it may contain ordinary
programming errors. That is the intended cost of preregistration. It is
mitigated by computing each kernel identity twice, exactly and numerically, and
by treating disagreement between the two paths as a failure. A defect found on
first execution is reported as a V2 preregistration with its reason, never as a
silent edit, and a harness failure is never converted into a claim about the
producer.

Nothing in this document proves anything about Collatz. E6-N2 through E6-N5 and
E7-B2 through E7-B6 remain open.
