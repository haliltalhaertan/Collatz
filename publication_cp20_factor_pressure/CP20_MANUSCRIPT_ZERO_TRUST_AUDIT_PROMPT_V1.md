# CP20 MANUSCRIPT V1 — ZERO-TRUST PUBLICATION AUDIT

Date: 2026-09-04

Repository: `haliltalhaertan/Collatz`

Branch: `cp20-publication-factor-pressure-v1-20260904`

Immutable manuscript target commit: `ab1afd5a52ca015c75438e32f70ffd4b30d764ce`

Target manuscript blob SHA: `be040e901a656a546a275992283b939293d9794f`

Manuscript creation commit: `6934312f7e51e08d71b8083b49a374ed3af70020`

Later branch commits may contain only status/audit-handoff metadata. Audit the manuscript content fixed by the immutable target commit above; do not infer mathematical changes from later editorial metadata commits.

Primary manuscript:

`publication_cp20_factor_pressure/CP20_MANUSCRIPT.tex`

Bibliography:

`publication_cp20_factor_pressure/CP20_REFERENCES.bib`

Publication extraction audit verdict already completed:

`[PASS WITH EDITORIAL REPAIRS]`

Those repairs are recorded in:

`publication_cp20_factor_pressure/CP20_PUBLICATION_AUDIT_REPAIR_INTEGRATION_2026-09-04.md`.

Two additional attribution concessions were inserted before this audit target was sealed:

- `\cite{NicholsonRampersad2016}` in the factor-complexity section, with an explicit warning that initial non-repetitive complexity is prefix-based whereas the CP20 proof uses a shifted window;
- `\cite{PesinWeiss2001}` at the Legendre/variational pressure representation, explicitly conceding that thermodynamic-formalism machinery is standard.

A local preflight compile of the exact target manuscript succeeded and produced a 16-page PDF with no unresolved references/citations. This is non-authoritative evidence only: you must independently compile and inspect it. The preflight PDF is persisted in the CP20 publication Drive folder as `CP20_MANUSCRIPT_V1_PREFLIGHT_2026-09-04.pdf`.

Known nonblocking preflight warnings to inspect independently:

- a large overfull box at the literal certificate filename in the reproducibility section;
- several underfull and small overfull boxes in the narrow prior-art table.

Do not treat these as already adjudicated; verify their visual materiality yourself.

## Role

You are an independent adversarial manuscript auditor. Do not produce new mathematics and do not silently repair a broken proof. Your job is to determine whether the manuscript faithfully and correctly turns the already audited/frozen Task-6/7/8A results into a self-contained mathematical paper, whether it compiles cleanly, and whether its attribution/novelty language is defensible.

Try to break the manuscript.

---

# 1. Authoritative mathematical sources

The theorem source of truth is the frozen/audited CP20 archive, not the manuscript and not this prompt.

Use at minimum:

- `CP20_TASK6_MAJOR_THEOREM_V3_AUDITED_FROZEN`;
- `CP20_TASK6_STRENGTHENED_COROLLARY_V3_AUDITED_FROZEN`;
- `CP20_TASK7_PRESSURE_GENERALIZATION_THEOREM_V3_AUDITED_FROZEN`;
- `CP20_TASK8A_CRITICAL_SITE_DENSITY_PRESSURE_THEOREM_V3`;
- `CP20_TASK8A_FINAL_FREEZE_DECISION_2026-08-26`.

Do not import the unfrozen arbitrary-`N` Task-8A extension, E7/E7R/B4, continued-fraction candidates, or any CP19 Task-5 exclusion.

---

# 2. Stage A — mechanical compilation audit

Independently compile `CP20_MANUSCRIPT.tex` with its bibliography using a standard LaTeX/BibTeX sequence or `latexmk`.

Required checks:

1. no fatal TeX errors;
2. all `\ref` / `\cref` references resolve;
3. all citations resolve, including `NicholsonRampersad2016` and `PesinWeiss2001`;
4. no missing bibliography entry;
5. no multiply-defined labels;
6. no undefined control sequence;
7. record every overfull/underfull box that is materially visible;
8. record final page count;
9. inspect the rendered PDF visually for clipping, broken glyphs, table overflow, equation overflow, or unreadable bibliography;
10. specifically inspect the long literal certificate filename and the prior-art comparison table, because the local preflight reported layout warnings there.

If compilation fails in a way caused by the manuscript source, verdict must be `[COMPILE FAIL]` unless the defect is a purely mechanical one-line editorial fix explicitly identified.

Do not alter the source during this stage.

---

# 3. Stage B — theorem-statement extraction audit

Compare every principal theorem/corollary in the manuscript against the frozen source.

Mandatory checks:

## Theorem A / lower complexity

- exact hypothesis `s_k=kappa log_2 k+O(1)`, `kappa>1`;
- no valuation-alphabet assumption introduced;
- exact epsilon range `0<epsilon<alpha/kappa` in the proof;
- correct shifted start window;
- correct `liminf >= alpha/kappa` conclusion.

## Finite-B pressure theorem

- finite `B>=3`;
- explicit `1<=a_k<=B` for every `k`;
- pointwise zero-criticality `a_k!=g_k`;
- exact defect supports;
- exact `h_B` formula;
- correct Chernoff/coefficient sign;
- `B=3 => kappa>3.027` only under the `B=3` hypotheses.

## Uniform envelope

- no claim about genuinely unbounded realized valuations;
- correct explanation that the critical-log law implies a finite bound along each fixed trajectory;
- correct monotonicity `h_B<=h_{B+1}<=h_infinity`;
- exact certified inequalities `h_infinity<56931/100000`, `alpha/h_infinity>348/125`.

## Critical-density theorem

- exact feasible region `F`;
- exact pressure surface;
- exact scale-family quantifiers `0<epsilon_r<alpha/kappa`, `epsilon_r->0`, `r epsilon_r->infinity`;
- no arbitrary-`N` strengthening;
- natural-density and zero-critical-density corollaries correctly derived;
- certified `rho_min` intervals copied exactly.

Assign to every statement one of:

`[PASS]`, `[EDITORIAL REPAIR]`, `[OVERCLAIM]`, `[FAIL]`.

---

# 4. Stage C — proof audit

Do not merely compare statements. Independently re-derive each load-bearing proof step.

## C1. Exact affine iterate

Verify the indexing and correction sum in

`2^{A_k} n_k = 3^k n_0 + sum_{j=0}^{k-1} 3^{k-1-j} 2^{A_j}`.

## C2. Polynomial state bound

Verify that

`2^{A_j}/3^j = 2^{-s_j-{alpha j}} = O(j^{-kappa})`

is used correctly, that the factor `1/3` in the affine carry sum is harmless, and that `kappa>1` is exactly what gives convergence.

## C3. Local mass uniformity

Verify the passage

`s_{u+r}-s_u = kappa log_2((u+r)/u)+O(1)`

uniformly on `u>=r`, including the meaning of the global `O(1)` error sequence.

## C4. Repeated-factor spacing

Verify both coprime divisibility and the nonzero branch. In particular, independently confirm that equality of start states gives eventual periodicity and that this contradicts `A_k/k->alpha` with irrational `alpha` under the stated hypotheses.

## C5. Exponential distinct-factor window

Check all exponents and floor effects in the comparison

`2^{alpha r-O(1)}` versus `2^{(alpha-kappa epsilon)r+O(1)}`.

Also check that the manuscript's comparison with Nicholson–Rampersad is attribution-only: their named invariant is initial/prefix based, whereas CP20 uses starts in the shifted window `[N_r,2N_r-r]`. Any claim identifying the two invariants is an attribution defect.

## C6. Deterministic pressure count

Verify:

- phase proportions;
- defect supports under finite `B` and zero-criticality;
- the uniform `O(log r)` defect band;
- coefficient positivity / Chernoff sign;
- polynomial overhead from defect values and Sturmian phase factors;
- conversion to base-2 entropy rate;
- infimum over lambda.

## C7. Uniform `B=infinity` envelope

Verify the two infinite partition sums, convergence domain `lambda>0`, monotonicity in `B`, and the logical step that a fixed critical-log trajectory has bounded valuations.

## C8. Critical-density pressure

Independently verify:

- feasibility condition `Q>=P` and its equivalent rho inequality;
- binomial entropy contribution;
- pressure formula;
- concavity via Legendre representation;
- saddle equation `(Q-P)y^2-Py-(P+Q)=0`;
- boundary `Q=P` optimizer escape;
- exact `O(1/T)` boundary overshoot.

The Legendre/variational machinery itself is not claimed as novel; verify that `PesinWeiss2001` is used only as background attribution and not as support for a Syracuse-specific theorem it does not state.

## C9. Two-regime uniformity

The manuscript summarizes the frozen repaired lemma. Determine whether the summary is sufficient for a self-contained paper. If a load-bearing estimate is only asserted rather than proved at publishable rigor, mark `[EDITORIAL REPAIR]` if the missing material can be copied from the frozen audited source; otherwise mark `[FAIL]` and stop.

## C10. Density bridge

Independently attack:

- why on Task-6 exponential windows `s_{u+r}-s_u=O(1)` rather than only `O(log r)`;
- why only `O(r^2)` type pairs occur;
- exponential negligibility of low-pressure types;
- Jensen/concavity direction;
- use of `h>=0`;
- projection error `O(1/r)`;
- double-counting identity connecting mean block densities to `D_i(N_r)` with `O(r/N_r)` boundary error;
- passage to accumulation points.

This is a load-bearing section. Try especially hard to find a quantifier or uniformity gap.

---

# 5. Stage D — numerical/certificate audit

Recompute independently, without trusting the manuscript decimals:

- `h_3` and `alpha/h_3`;
- `h_infinity` and `alpha/h_infinity`;
- zero-density saddle root `t_0`;
- all three `rho_min` interval targets if the canonical certificate is available.

Check that no informational decimal is used for a proof-critical sign.

---

# 6. Stage E — prior art and attribution audit

Mandatory sources:

- Dubickas 2009;
- López–Stoll 2009;
- Wang 2019;
- Lagarias–Weiss;
- Witteveen 2026, `kulltc/collatz-entropy-barriers`, initial release commit `fc0854799b094fa04250ce8309279609276f3c58`;
- `docbgm2002/collatz-things`, especially July 2026 IEF12–IEF21;
- Nicholson–Rampersad 2016, *Initial Non-Repetitive Complexity of Infinite Words*;
- classical pressure / Birkhoff-average thermodynamic formalism, including Pesin–Weiss 2001 or an equivalent authoritative source;
- `CP20_SPECIALIST_LITERATURE_SCREEN_V1_2026-09-04.md` as a working screen, not as authority.

Verify that the manuscript does not claim novelty for:

- non-repetitive complexity as a concept;
- repeated-factor divisibility as a device;
- Sturmian Collatz methods;
- factor complexity in Collatz generally;
- pressure/Chernoff/Legendre machinery generally;
- the architecture “constrained-language entropy versus Diophantine/discrepancy parameter yields a threshold.”

The two direct body citations are already present. Audit their accuracy rather than merely their presence:

1. `NicholsonRampersad2016` must be framed as the prefix-based initial non-repetitive-complexity precedent, with CP20 explicitly distinguished as a shifted-window analogue;
2. `PesinWeiss2001` must be framed as general thermodynamic/multifractal background, not as a source for the Syracuse-specific pressure formula.

Classify any misframing as `[ATTRIBUTION REPAIR]` unless it changes a mathematical theorem claim.

The narrow novelty target is only:

> the quantitative critical-log Syracuse synthesis `alpha/kappa` lower factor-complexity rate + finite-`B` deterministic pressure `h_B` + uniform `kappa>2.784` consequence + two-type critical-site density pressure surface.

Try to falsify even this narrow claim.

---

# 7. Stage F — bibliography audit

Verify every bibliography entry against an authoritative source where possible:

- exact author spelling;
- title;
- journal/book;
- year;
- volume/issue;
- pages/article number;
- DOI/arXiv identifier;
- chronology for 2026 repository sources.

Flag repository-only sources clearly as such; do not present them as peer-reviewed papers.

---

# 8. Scope audit

The manuscript must not claim or imply:

- proof of the Collatz conjecture;
- exclusion of all divergent trajectories;
- exclusion of all nontrivial cycles;
- exclusion of CP19 Task-5 survivor;
- arbitrary-`N` Task-8A theorem;
- E7/E7R/B4 Fourier conclusions.

Check title, abstract, introduction, theorem statements, conclusion/scope, and appendix.

---

# 9. Stop rule

Stop and report immediately if any of the following is established:

1. a principal manuscript theorem is stronger than its frozen source;
2. a load-bearing proof step is invalid or materially incomplete and cannot be restored verbatim from the frozen audited source;
3. finite-`B` hypotheses are dropped at any theorem-critical use;
4. the Task-8A density bridge has a genuine quantifier/uniformity gap;
5. a prior source subsumes the narrow principal quantitative claim;
6. the source fails to compile in a mathematically material way.

Do not invent a repair theorem.

---

# 10. Required final report

## A. Overall verdict

Exactly one of:

- `[MANUSCRIPT PROOF VALID]`
- `[VALID AFTER EDITORIAL REPAIRS]`
- `[PROOF EXTRACTION FAIL]`
- `[PRIOR ART / ATTRIBUTION REPAIR REQUIRED]`
- `[COMPILE FAIL]`

## B. Compilation table

Compiler sequence, warnings, unresolved refs/cites, page count, visual issues.

## C. Theorem/proof table

For each load-bearing theorem/lemma: source, manuscript location, verdict, exact defect if any.

## D. Numerical table

Independent recomputations and match/no-match.

## E. Attribution table

Retain / add citation / narrow / delete language.

## F. Exact repairs

Only verbatim/editorial repairs supported by frozen source or verified bibliography. No new mathematics.

## G. Submission gate

Exactly one:

- `READY FOR FINAL MANUSCRIPT FREEZE AFTER LISTED EDITORIAL REPAIRS`
- `NOT READY — MATHEMATICAL REPAIR REQUIRED`
- `NOT READY — PRIORITY / ATTRIBUTION CHECK REQUIRED`

Nothing in the report may claim that the Collatz conjecture has been proved.
