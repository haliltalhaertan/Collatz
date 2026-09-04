# CP20 MANUSCRIPT V1 — STATUS

Date: 2026-09-04

Branch: `cp20-publication-factor-pressure-v1-20260904`

Manuscript:

`publication_cp20_factor_pressure/CP20_MANUSCRIPT.tex`

Manuscript creation commit:

`6934312f7e51e08d71b8083b49a374ed3af70020`

Latest manuscript citation/preflight commit:

`ab1afd5a52ca015c75438e32f70ffd4b30d764ce`

Bibliography:

`publication_cp20_factor_pressure/CP20_REFERENCES.bib`

Status:

`[DRAFT V1 COMPILES — ATTRIBUTION CONCESSIONS LANDED — PDF PREFLIGHT PASS WITH LAYOUT WARNINGS — MANUSCRIPT ZERO-TRUST AUDIT READY]`

## 1. Source gate

The manuscript was drafted only after the independent publication-extraction audit returned `[PASS WITH EDITORIAL REPAIRS]` and the blocking T4/T5/T6 repairs were integrated.

No new theorem is intentionally introduced in V1.

Principal theorem chain included:

1. critical-log factor-complexity lower rate `alpha/kappa`;
2. finite-`B` zero-critical deterministic pressure with explicit `1<=a_k<=B`;
3. uniform no-a-priori-bound envelope `kappa>2.784`;
4. frozen Task-8A scale-family critical-density pressure theorem;
5. natural-density, zero-critical-density, and certified `rho_min` corollaries.

## 2. Mandatory audit repairs present in manuscript readback

GitHub readback confirms:

- finite `B>=3` pressure theorem explicitly assumes `1<=a_k<=B`;
- the `B=3` consequence is stated only inside that finite-`B` theorem;
- Task-6 counting uses `0<epsilon<alpha/kappa`;
- Task-8A theorem uses `0<epsilon_r<alpha/kappa`, `epsilon_r->0`, `r epsilon_r->infinity`;
- no arbitrary-`N` density theorem is claimed;
- “no a priori valuation-alphabet bound” wording is used for the uniform envelope;
- scope explicitly says the paper does not prove Collatz or exclude all divergent/cyclic behavior.

## 3. Prior-art discipline present in manuscript readback

V1 explicitly states:

- repeated-factor divisibility is not claimed as a new device;
- Witteveen's `3^r` endpoint divisibility and CP20's `2^{A(W)}` start-value divisibility are dual readings of the same affine subtraction identity;
- the general entropy-rate-versus-Diophantine/discrepancy threshold architecture is not claimed as new;
- `collatz-things` July 2026 residual-language results are discussed as close prior art;
- the novelty claim is restricted to the critical-log quantitative synthesis.

The post-audit attribution gap identified before compilation is now closed in the manuscript body:

- Nicholson–Rampersad 2016 is cited explicitly where the shifted exponential distinct-factor window is compared, carefully, with the prefix-based notion of initial non-repetitive complexity; the manuscript says only that the theorem is a windowed analogue and does not identify the two invariants;
- Pesin–Weiss 2001 is cited explicitly at the Legendre/variational representation to concede that this thermodynamic-formalism machinery is standard and is not part of the novelty claim.

## 4. Bibliography gate

The compiled manuscript now resolves citations to:

- Lagarias;
- Lagarias–Weiss;
- Morse–Hedlund;
- Dubickas;
- López–Stoll;
- Wang;
- Nicholson–Rampersad;
- Pesin–Weiss;
- Witteveen;
- `collatz-things`.

Bibliographic metadata still requires the dedicated manuscript zero-trust bibliography check before freeze.

## 5. Compilation and PDF preflight gate

`[PASS WITH NONBLOCKING LAYOUT WARNINGS]`.

Local preflight sequence executed on the exact manuscript source corresponding to commit `ab1afd5a52ca015c75438e32f70ffd4b30d764ce`:

1. `pdflatex -interaction=nonstopmode -halt-on-error CP20_MANUSCRIPT.tex`;
2. BibTeX 0.99d (`bibtex.original`) on `CP20_MANUSCRIPT`;
3. `pdflatex` twice more.

Result:

- compile completed successfully;
- final PDF page count: 16;
- no unresolved references or citations in the final pass;
- no missing bibliography entry;
- no fatal TeX error or undefined control sequence;
- both new concessions are visibly present in the PDF and bibliography;
- rendered 16-page visual contact-sheet inspection found no clipped page body, broken glyphs, or equation overflow.

Nonblocking typography warnings remain:

- one large overfull box is caused by the long literal certificate filename in the reproducibility section;
- the narrow prior-art comparison table produces several underfull boxes and a few small overfull boxes.

These are editorial layout defects, not mathematical or citation failures. They should be repaired before final manuscript freeze, but they do not block the independent manuscript proof audit.

Preflight PDF persisted to Drive as:

`CP20_MANUSCRIPT_V1_PREFLIGHT_2026-09-04.pdf`.

## 6. Mathematical manuscript audit gate

`[READY FOR INDEPENDENT ZERO-TRUST AUDIT]`.

The compiled draft must now receive a new zero-trust audit that compares every theorem and proof against the frozen Task-6/7/8A sources and specifically attacks:

- uniformity in the `O(1)` / `O(log r)` estimates;
- finite-`B` hypotheses at every use of `h_B`;
- the `B=infinity` envelope argument;
- the Task-8A two-regime uniformity summary;
- the double-counting bridge from block types to `D_i(N_r)`;
- exact versus certified-numerical statements;
- novelty wording against Witteveen, `collatz-things`, Nicholson–Rampersad, and general thermodynamic formalism;
- correctness and sufficiency of the two newly added attribution concessions.

## 7. Specialist priority gate

`[OPEN — REQUIRED BEFORE SUBMISSION]`.

The targeted LLM literature screen found no abstract theorem that subsumes T4 or T5, but a human specialist check in combinatorics on words / symbolic dynamics remains required by the independent audit.

## 8. Current next action

Run the independent zero-trust manuscript audit against the compiled manuscript at commit `ab1afd5a52ca015c75438e32f70ffd4b30d764ce` and its bibliography. Do not label the manuscript submission-ready until that verdict is integrated.
