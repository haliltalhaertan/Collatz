# CP20 MANUSCRIPT V1 — PREFLIGHT AND ZERO-TRUST AUDIT HANDOFF

Date: 2026-09-04

Branch: `cp20-publication-factor-pressure-v1-20260904`

## Immutable manuscript target

- manuscript commit: `ab1afd5a52ca015c75438e32f70ffd4b30d764ce`
- manuscript blob SHA: `be040e901a656a546a275992283b939293d9794f`
- primary source: `publication_cp20_factor_pressure/CP20_MANUSCRIPT.tex`
- bibliography: `publication_cp20_factor_pressure/CP20_REFERENCES.bib`

Later commits on the publication branch may update only status/audit-handoff metadata. The manuscript audit target is the immutable commit above.

## Attribution repairs added before compile

Two direct concessions were added to the manuscript body before the audit target was sealed:

1. `NicholsonRampersad2016` is cited in the factor-complexity section. The manuscript explicitly says that Nicholson–Rampersad's initial non-repetitive complexity is prefix-based, while the CP20 proof uses the shifted window `u in [N_r,2N_r-r]`; CP20 is described only as a windowed analogue, not as the same invariant.
2. `PesinWeiss2001` is cited at the Legendre/variational pressure representation. The manuscript explicitly says that the thermodynamic-formalism / large-deviation machinery is standard and is not part of the novelty claim.

No theorem, proof constant, or frozen mathematical dependency was changed by these attribution repairs.

## Local compile preflight

The exact target source was compiled locally with:

1. `pdflatex -interaction=nonstopmode -halt-on-error CP20_MANUSCRIPT.tex`
2. BibTeX 0.99d (`bibtex.original CP20_MANUSCRIPT`)
3. `pdflatex` twice more.

Result:

- compile: PASS;
- final PDF: 16 pages;
- unresolved refs/citations: none on final pass;
- missing bibliography entries: none;
- fatal TeX errors / undefined control sequences: none;
- both new citations visible in PDF text and bibliography.

Rendered-PDF preflight inspected all 16 pages. No clipped page body, broken glyphs, or equation overflow was observed.

Known nonblocking layout warnings:

- one large overfull box caused by the long literal certificate filename in the reproducibility section;
- several underfull and small overfull boxes in the narrow prior-art comparison table.

These remain editorial layout items for the independent manuscript auditor/final typography pass; they are not treated here as proof defects.

## Drive persistence

Publication Drive folder:

`CP20_PUBLICATION_FACTOR_PRESSURE_V1_2026-09-04`

Folder ID:

`19y_ZYCGCL8wEn3WkruQOkCuVlxnYwaaE`

Preflight PDF:

`CP20_MANUSCRIPT_V1_PREFLIGHT_2026-09-04.pdf`

Drive file ID:

`1cCVuX2vjIe5TgA6g4nOJBMbvWbsTYAN3`

Zero-trust handoff Google Doc:

`CP20_MANUSCRIPT_V1_ZERO_TRUST_AUDIT_HANDOFF`

Drive document ID:

`1XLlqt4QFpwSDo5xdeW2ZXmNjfenbV226QJKVSmGdMco`

Drive handoff readback after update: PASS.

## Canonical audit prompt

GitHub file:

`publication_cp20_factor_pressure/CP20_MANUSCRIPT_ZERO_TRUST_AUDIT_PROMPT_V1.md`

Audit-prompt retargeting commit:

`3bea2133ea48b483c3e7b882be3fdcb7ab41d6f8`

The prompt requires an independent recompile/render, theorem/proof re-derivation from frozen Task-6/7/8A sources, numerical recomputation, bibliography/attribution audit, and stop-rule adjudication.

## Current gate

Status:

`[MANUSCRIPT V1 PREFLIGHT COMPLETE — ZERO-TRUST AUDIT READY]`

Next permitted action:

Run the independent zero-trust manuscript audit against manuscript commit `ab1afd5a52ca015c75438e32f70ffd4b30d764ce`.

Do not label the manuscript submission-ready until the resulting audit verdict is integrated.
