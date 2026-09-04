# CP20 MANUSCRIPT V1 — ZERO-TRUST AUDIT RESULT

Date: 2026-09-04

Audited immutable target:

- commit: `ab1afd5a52ca015c75438e32f70ffd4b30d764ce`
- manuscript blob SHA: `be040e901a656a546a275992283b939293d9794f`
- manuscript: `publication_cp20_factor_pressure/CP20_MANUSCRIPT.tex`

Independent auditor verdict:

`[VALID AFTER EDITORIAL REPAIRS]`

Submission gate returned by auditor:

`READY FOR FINAL MANUSCRIPT FREEZE AFTER LISTED EDITORIAL REPAIRS`

No mathematical stop-rule condition was triggered.

## Auditor-confirmed passes

- independent MiKTeX compile: 16 pages;
- no fatal TeX error;
- no unresolved references or citations;
- no multiply-defined labels;
- all four principal theorem statements faithful to frozen sources;
- finite-`B` hypothesis present at every theorem-critical use of `h_B`;
- uniform-envelope logic valid;
- Task-8A density bridge valid;
- Chernoff signs valid;
- independently recomputed numerical constants match;
- no Collatz-solved implication;
- Witteveen / `collatz-things` / general entropy-pressure concessions are appropriately narrow.

## Required editorial repairs from the audit

### R1 — priority attribution

The V1 remark incorrectly said Nicholson--Rampersad introduced initial non-repetitive complexity. The auditor verified that the underlying prefix-based notion was first defined by T. K. Subrahmonian Moothathu.

Required repair: add Moothathu 2012 and reword the remark so Nicholson--Rampersad are described as later studying the initial non-repetitive complexity.

### R2 — Task-8A two-regime proof detail

The V1 manuscript compressed the frozen repaired two-regime uniformity argument to a few sentences. The auditor classified this as `[EDITORIAL REPAIR]`, not a mathematical failure, because the missing estimates are present in the frozen audited source.

The repair must explicitly include the interior optimizer

`y_* = (P + sqrt(P^2 + 4 q (P+Q))) / (2 q)`, `q=Q-P`,

and the uniform bound

`y_* <= (1+sqrt(5))/(2 eta)` for `q>=eta`,

followed by the compact finite-parameter cover and the separate fixed-`T` boundary-strip argument.

### R3 — rendered-PDF layout

The auditor visually confirmed two material layout defects:

- page 14: the long canonical certificate filename clipped beyond the physical page edge;
- page 15: the narrow prior-art table produced a `collatz-things` column collision.

Required repair: make the filename line-breakable and replace/reformat the narrow table.

## Bibliography note

The auditor marked the Pesin--Weiss 2001 book-chapter metadata as not independently verified in Crossref. A subsequent targeted check found independent bibliographic confirmation for the title, authors, book, Bristol publisher context, year 2001, and pp. 419--431. No DOI is required in the bibliography unless independently verified.

## Integration status

The three required editorial repairs were integrated on the publication branch by commit:

`911d615025832ccb5db6e35a9d73f02641efb3a4`

The repaired manuscript blob is:

`7421c8ac2051800981be548057bc97005c32c05e`

Specific integrated changes:

1. Moothathu 2012 added and priority wording corrected;
2. explicit `Uniform low-pressure cover` lemma and two-regime proof inserted;
3. canonical certificate filename changed to a line-breakable `\path{...}` form;
4. narrow prior-art table replaced by prose paragraphs.

Post-repair compile and visual checks remain the final mechanical gate before freeze. The human-specialist abstract-priority check in combinatorics on words / symbolic dynamics remains open before external submission.