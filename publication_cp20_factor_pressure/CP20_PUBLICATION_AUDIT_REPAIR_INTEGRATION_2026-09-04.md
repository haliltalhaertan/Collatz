# CP20 PUBLICATION AUDIT — REPAIR INTEGRATION

Date: 2026-09-04

Publication branch: `cp20-publication-factor-pressure-v1-20260904`

Independent audit verdict: `[PASS WITH EDITORIAL REPAIRS]`

Audit-time branch tip: `23f5c541830be1dbb2a35db6b68a4f31935151cf`

Post-repair branch tip before this integration record: `e46b79248dc223b1259152a92bfb532aa536d2f5`

## 1. Audit persistence

The complete independent audit verdict has been persisted to Google Drive as:

`CP20_PUBLICATION_ZERO_TRUST_AUDIT_VERDICT_2026-09-04`

Drive document ID:

`1UrNiIB-ZY0LAddGEt1kx8Ka9mvJ3r4YvZBjdLegWvIc`

Drive parent folder:

`CP20_PUBLICATION_FACTOR_PRESSURE_V1_2026-09-04`

Folder ID:

`19y_ZYCGCL8wEn3WkruQOkCuVlxnYwaaE`

Drive import: PASS.

Drive move into publication folder: PASS.

Drive text read-back: PASS; the document contains the audit header, exact branch chronology, `[PASS WITH EDITORIAL REPAIRS]` verdict, T1–T12 table, prior-art table, required repairs, and next-action section.

## 2. Blocking theorem-extraction repairs

### T4 epsilon range — REPAIRED

`CP20_THEOREM_INVENTORY.md` now states exactly

`0 < epsilon < alpha/kappa`

rather than the vague phrase “sufficiently small epsilon.”

### T5 finite-alphabet hypothesis — REPAIRED

The finite-`B` pressure theorem now explicitly assumes

`B>=3`,

`1<=a_k<=B` for every `k`,

and pointwise zero-criticality `a_k!=g_k`.

### T6 B=3 corollary — REPAIRED

The special consequence `kappa>3.027` is now explicitly conditioned on the `B=3` hypotheses, including `1<=a_k<=3`, zero-criticality, and the critical-log law. The missing source line has been restored.

### Branch status headline — REPAIRED

`CP20_PUBLICATION_BRANCH_STATUS.md` now carries the finite-alphabet hypothesis in the finite-`B` headline statement rather than presenting `h_B` as alphabet-bound-free.

## 3. Optional tightening accepted

Task-8A T8 now uses the stricter audited V3 scale-family quantifiers:

`0 < epsilon_r < alpha/kappa`,

`epsilon_r -> 0`,

`r epsilon_r -> infinity`.

No arbitrary-`N` strengthening is admitted.

## 4. Prior-art architecture repair

`CP20_DEEP_NOVELTY_AUDIT_V1.md`, `CP20_NOVELTY_MATRIX.md`, and `CP20_PAPER_OUTLINE.md` now explicitly record that:

1. Witteveen's `3^r` endpoint divisibility and CP20's `2^{A(W)}` start-value divisibility are dual coprime consequences of the same affine subtraction identity; repeated-factor divisibility is therefore not claimed as a new device.
2. The broad architecture “entropy rate of a constrained Collatz word language versus a Diophantine/discrepancy parameter yields a threshold” is prior art and is not claimed as new.
3. The defensible novelty target is the different critical-log hypothesis class and the quantitative synthesis `alpha/kappa` lower rate + finite-`B` deterministic pressure `h_B` + uniform `kappa>2.784` envelope + two-type critical-density pressure surface.

## 5. Manuscript control checklist

The outline now includes the mandatory control:

> Every finite-`B` statement carries the hypothesis `1<=a_k<=B` explicitly.

It also forbids novelty claims for the general entropy-threshold architecture.

## 6. Mechanical read-back

GitHub read-back confirms the repaired theorem inventory contains:

- T4 exact epsilon range;
- T5 `1<=a_k<=B`;
- T6 conditioned `B=3` consequence and source line;
- T8 strict scale-family epsilon quantifier.

No frozen mathematical source was edited. No E7/E7R/B4 result was imported.

## 7. Remaining publication risk

The independent audit leaves one non-blocking-for-drafting but blocking-for-submission item:

`[OPEN — SPECIALIST CHECK REQUIRED]`

Possible abstract subsumption of T4/T5 by a general combinatorics-on-words or symbolic-dynamics theorem stated outside Collatz terminology.

The manuscript may now be drafted, but it must not be publicly submitted until this specialist literature risk is addressed and the finished manuscript receives a fresh zero-trust publication audit.

## 8. Milestone verdict

`[AUDIT REPAIRS INTEGRATED — MANUSCRIPT DRAFT AUTHORIZED]`

Next action: draft `CP20_MANUSCRIPT.tex` from the repaired theorem inventory and repaired paper outline, without introducing new mathematics.
