# CP20 MANUSCRIPT V1 — STATUS

Date: 2026-09-04

Branch: `cp20-publication-factor-pressure-v1-20260904`

Manuscript:

`publication_cp20_factor_pressure/CP20_MANUSCRIPT.tex`

Manuscript creation commit:

`6934312f7e51e08d71b8083b49a374ed3af70020`

Bibliography:

`publication_cp20_factor_pressure/CP20_REFERENCES.bib`

Status:

`[DRAFT V1 CREATED — GITHUB READBACK PASS — COMPILE PENDING — MANUSCRIPT ZERO-TRUST AUDIT PENDING]`

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

A targeted post-audit literature screen additionally identified Nicholson–Rampersad's established non-repetitive-complexity terminology and classical pressure/Birkhoff-average thermodynamic formalism. These are recorded in `CP20_SPECIALIST_LITERATURE_SCREEN_V1_2026-09-04.md` and the bibliography has been expanded accordingly. A later manuscript revision should decide whether to cite these directly in the body.

## 4. Bibliography gate

GitHub readback confirms bibliography entries for all citations currently used by V1:

- Lagarias;
- Lagarias–Weiss;
- Morse–Hedlund;
- Dubickas;
- López–Stoll;
- Wang;
- Witteveen;
- `collatz-things`.

Additional specialist-screen references are also staged:

- Nicholson–Rampersad 2016;
- Pesin–Weiss 2001.

Bibliographic metadata should receive a final dedicated audit before submission.

## 5. Compilation gate

`[PENDING]`.

The manuscript has not yet been promoted as compiled or visually clean. A LaTeX compile, unresolved-reference scan, warning scan, and rendered-PDF inspection are required before manuscript audit.

Do not label this draft submission-ready until that gate passes.

## 6. Mathematical manuscript audit gate

`[PENDING]`.

The finished compiled draft must receive a new zero-trust audit that compares every theorem and proof against the frozen Task-6/7/8A sources and specifically attacks:

- uniformity in the `O(1)` / `O(log r)` estimates;
- finite-`B` hypotheses at every use of `h_B`;
- the `B=infinity` envelope argument;
- the Task-8A two-regime uniformity summary;
- the double-counting bridge from block types to `D_i(N_r)`;
- exact versus certified-numerical statements;
- novelty wording against Witteveen, `collatz-things`, Nicholson–Rampersad, and general thermodynamic formalism.

## 7. Specialist priority gate

`[OPEN — REQUIRED BEFORE SUBMISSION]`.

The targeted LLM literature screen found no abstract theorem that subsumes T4 or T5, but a human specialist check in combinatorics on words / symbolic dynamics remains required by the independent audit.

## 8. Current next action

1. compile the LaTeX source;
2. repair mechanical/typographic issues only;
3. render and inspect the PDF;
4. create a sealed manuscript-audit package;
5. run a fresh independent zero-trust manuscript audit.
