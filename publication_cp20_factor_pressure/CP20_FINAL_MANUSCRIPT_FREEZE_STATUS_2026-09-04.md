# CP20 FINAL MANUSCRIPT FREEZE STATUS

Date: 2026-09-04

Branch: `cp20-publication-factor-pressure-v1-20260904`

Status:

`[FINAL MANUSCRIPT FREEZE — INTERNAL PROOF / EDITORIAL / COMPILE / VISUAL GATES PASSED — SPECIALIST PRIORITY CHECK OPEN]`

## 1. Audit lineage

Independent manuscript audit target:

- commit: `ab1afd5a52ca015c75438e32f70ffd4b30d764ce`
- manuscript blob: `be040e901a656a546a275992283b939293d9794f`
- verdict: `[VALID AFTER EDITORIAL REPAIRS]`
- gate: `READY FOR FINAL MANUSCRIPT FREEZE AFTER LISTED EDITORIAL REPAIRS`
- no mathematical stop-rule condition triggered.

Canonical audit result record:

`publication_cp20_factor_pressure/CP20_MANUSCRIPT_V1_ZERO_TRUST_AUDIT_RESULT_2026-09-04.md`

## 2. Integrated editorial repairs

Repair commit:

`911d615025832ccb5db6e35a9d73f02641efb3a4`

Repaired manuscript blob SHA:

`7421c8ac2051800981be548057bc97005c32c05e`

Integrated repairs:

1. priority attribution corrected: Moothathu 2012 is cited for the prefix-based non-repetitive subword complexity; Nicholson--Rampersad are described as later studying initial non-repetitive complexity;
2. the Task-8A two-regime uniformity argument is expanded into an explicit `Uniform low-pressure cover` lemma with the audited interior optimizer bound, finite compact parameter cover, and separate boundary-strip argument;
3. the long canonical certificate filename is made line-breakable with `\path{...}`;
4. the narrow prior-art table is replaced by prose paragraphs to remove the rendered column collision.

No principal theorem was strengthened and no new mathematical claim was introduced by these repairs.

## 3. Post-repair compile gate

A clean GitHub Actions build checked out the repaired source and ran:

`pdflatex -> BibTeX -> pdflatex -> pdflatex`.

Result:

- workflow job conclusion: `success`;
- final PDF: 17 pages;
- no fatal TeX errors;
- no unresolved references/citations after the final pass;
- no multiply-defined labels;
- no overfull boxes in the final log;
- one bibliography underfull box for the repository entry, classified cosmetic.

Compile artifact:

- artifact ID: `9941105735`;
- artifact ZIP SHA-256: `cb1cbd3ac8b956a1c548fc1f47a4a2bd91908ad5ac386af23affa498e8d94a7c`.

## 4. Visual gate

The exact post-repair PDF was rendered page-by-page at 150 DPI and all 17 pages were inspected.

The two audit-identified visual defects are closed:

- the certificate filename on the reproducibility page now wraps fully inside the text block;
- the former `collatz-things` prior-art table collision is absent because the comparison is now prose.

No clipped page body, broken glyph, visible equation overflow, or text collision was observed in the final render.

Final PDF SHA-256:

`115edb78911213f27b24725dd4b159983023e682fb4fd23ca84855723b57390b`

Drive copy:

- file: `CP20_MANUSCRIPT_FINAL_FREEZE_CANDIDATE_2026-09-04.pdf`
- Drive file ID: `1eMuiwumi5X6fc0s_tlJYHorv74x9hzSl`.

## 5. Bibliography gate

The Moothathu entry added by the repair is:

- T. K. Subrahmonian Moothathu, `Eulerian Entropy and Non-Repetitive Subword Complexity`, Theoretical Computer Science 420(1), 80--88 (2012), DOI `10.1016/j.tcs.2011.11.013`.

The Pesin--Weiss chapter metadata was independently cross-checked against bibliographic references: title, authors, book, Bristol publisher context, year 2001, and pp. 419--431 are supported. No unverified DOI is asserted.

## 6. Scope lock

The frozen manuscript remains conditional on the global critical-log law. It does not claim a proof of the Collatz conjecture, does not exclude all divergent or cyclic trajectories, and does not import the unfrozen arbitrary-`N` Task-8A extension, continued-fraction candidates, or E7/E7R/B4 results.

## 7. Remaining external-submission gate

`[OPEN]` Human-specialist priority/subsumption check in combinatorics on words / symbolic dynamics.

This is not an internal proof defect. The independent audit and targeted literature screens found no source subsuming the narrow quantitative synthesis, but this specialist priority check remains required before external submission.

Until that gate closes, describe the manuscript as internally frozen rather than externally submission-ready.