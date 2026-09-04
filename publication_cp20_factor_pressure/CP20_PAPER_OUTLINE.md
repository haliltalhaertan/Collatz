# CP20 PAPER OUTLINE

## Working title

**Factor-Complexity and Pressure Barriers for Critical-Log Syracuse Valuation Words**

Alternative:

**Entropy–Pressure Constraints on Critical-Log Syracuse Orbits**

Status: `[WORKING OUTLINE — NO NEW MATHEMATICS]`

---

# 1. Paper thesis

The paper studies positive ordinary orbits of the accelerated odd Collatz/Syracuse map under the global discrepancy law

` s_k = kappa log_2 k + O(1),  kappa>1. `

Its core result is a quantitative incompatibility between two forms of symbolic complexity:

- arithmetic repetition forces the valuation word to have exponentially many factors;
- zero/sparse critical structure forces the same word into a lower-pressure language.

The conjunction yields an explicit lower threshold on `kappa` and, after resolving critical sites by type, a quantitative critical-density phase constraint.

The paper does **not** prove Collatz, exclude all divergent orbits, or exclude all cycles.

---

# 2. Abstract skeleton

Suggested abstract logic:

1. Define the accelerated odd map and the valuation word.
2. Assume the critical-log discrepancy law.
3. State the exponential factor-complexity lower bound
   `liminf log_2 p_a(r)/r >= alpha/kappa`.
4. Under zero-criticality, state the deterministic weighted-pressure upper bound and the consequence
   `kappa > 2.784` uniformly without a preassigned alphabet bound.
5. Relax pointwise zero-criticality to a two-type critical-site density theorem; if critical sites have zero density, the same threshold remains.
6. Give one or two certified `rho_min(kappa)` examples.
7. Close with exact scope: this is a conditional structural obstruction inside the critical-log regime, not a proof of the Collatz conjecture.

Avoid “first,” “introduce factor complexity,” or “new entropy method.”

---

# 3. Introduction

## 3.1 Problem setting

Introduce the odd-only Syracuse map

`n_{k+1}=(3n_k+1)/2^{v_2(3n_k+1)}`

and valuation sequence `a_k`.

Define

`alpha=log_2 3`,
`F_k=floor(alpha k)`,
`s_k=F_k-A_k`.

Explain the critical-log regime

`s_k=kappa log_2 k+O(1)`

as a highly structured hypothetical near-critical behaviour, not a property asserted for all Collatz orbits.

## 3.2 Main contributions

State three main theorems in compressed form:

**Theorem A — factor-complexity lower rate**

`liminf log_2 p_a(r)/r >= alpha/kappa`.

**Theorem B — zero-critical pressure obstruction**

`limsup log_2 p_a(r)/r <= h_B`, hence `kappa>=alpha/h_B`, and uniformly

`kappa > 2.784`.

**Theorem C — critical-site density pressure theorem**

Every audited scale-family accumulation density lies in the feasible region and satisfies

`h(rho_1,rho_2)>=alpha/kappa`.

Then state the zero-density and certified `rho_min` corollaries.

## 3.3 Relation to earlier work

This subsection must be unusually explicit because contemporary prior art is close.

Recommended order:

1. **Classical parity/stopping-time and stochastic background** — Terras, Everett, Lagarias, Lagarias–Weiss.
2. **Valuation/E-sequence approach** — Wang.
3. **Word complexity in Collatz-related codings** — Dubickas.
4. **Sturmian Collatz conjugacy** — López–Stoll.
5. **Bounded-amplitude entropy barriers** — Witteveen 2026.
6. **Integral-escape / repetition-complexity residual language** — `docbgm2002/collatz-things`, July 2026, treated as a public structural-notes source unless/until a formal publication is identified.

The comparison paragraph should say explicitly:

> The present argument does not claim novelty for affine repetition, Sturmian structure, factor complexity, or entropy barriers individually. Its distinguishing feature is the quantitative critical-log entropy-pressure chain for the ordinary Syracuse valuation word and the resulting two-type critical-density pressure surface.

---

# 4. Syracuse algebra and the critical-log regime

Definitions:

- `A_k` cumulative valuation;
- `F_k`, `s_k`;
- valuation factor `W` and its mass `A(W)`;
- factor complexity `p_a(r)`;
- phase word `g_k=F_{k+1}-F_k`;
- critical site `a_k=g_k`.

Prove or cite internally extracted lemmas:

### Lemma 4.1 — affine iterate

Exact word map.

### Lemma 4.2 — polynomial state growth

`n_k=O(k^kappa)`.

### Lemma 4.3 — local valuation mass

`A(u,r)>=alpha r-O(1)` on the required windows.

Keep all quantifier restrictions exactly as in the frozen V3 source.

---

# 5. Repeated factors and exponential complexity

## 5.1 Repeated-factor spacing

Derive

`2^{A(W)} | (n_v-n_u)`

for equal valuation factors at two starts.

Handle the equal-state branch explicitly via eventual periodicity and irrationality of `alpha`.

## 5.2 Exponential counting window

Take

`N_r=floor(2^{(alpha/kappa-epsilon)r})`,
`0<epsilon<alpha/kappa`.

Show that two equal factors in the selected start window would require both

`|n_v-n_u| >= 2^{alpha r-O(1)}`

and

`|n_v-n_u| <= 2^{(alpha-kappa epsilon)r+O(1)}`,

contradiction for large `r`.

## 5.3 Theorem A

Conclude

`liminf log_2 p_a(r)/r >= alpha/kappa`.

### Related-work remark

This is the place to distinguish the theorem from:

- Dubickas's linear complexity lower bound for a different coding;
- Witteveen's bounded-amplitude cycle factor-count mechanism;
- the qualitative low-complexity exclusions in the integral-escape residual programme.

---

# 6. Zero-critical deterministic pressure

## 6.1 Sturmian phase

Explain that `g` is Sturmian and that its length-`r` factors have:

- exactly `r+1` possibilities;
- two Parikh vectors differing by one site.

No novelty claim.

## 6.2 Defect language

Define `d_k=g_k-a_k`.

Under zero-criticality, record the exact finite-`B` supports at `g=1` and `g=2` sites.

Use

`sum d_i=s_{u+r}-s_u=O(log r)`.

## 6.3 Chernoff generating function

Write the coefficient inequality with the audited sign:

`N(S)t^S<=P(t)`,

thus

`N(S)<=P(t)t^{-S}`.

Emphasize that the `O(log r)` band costs only polynomial overhead.

## 6.4 Pressure constant

Define `h_B` exactly.

Prove

`limsup log_2 p_a(r)/r <= h_B`.

## 6.5 Theorem B

Combine with Theorem A:

`kappa>=alpha/h_B`.

Then develop the `B=infinity` uniform envelope and exact interval certificate:

`alpha/h_infinity > 348/125 = 2.784`.

### Precision note

Use “no a priori alphabet bound.” Do not say that an actually unbounded valuation sequence is covered as a realized critical-log orbit.

---

# 7. Critical-site density pressure

This should be a full principal section rather than an appendix; it is the strongest conceptual extension beyond the zero-critical theorem.

## 7.1 Two critical types

Type 1: `g=1,a=1`.  
Type 2: `g=2,a=2`.

Define `rho_1,rho_2` and the feasible region `F`.

Explain why the feasibility inequality is necessary and why the original full-box formulation was repaired.

## 7.2 Exact pressure surface

Define

`h(rho_1,rho_2)`

through the entropy terms and one-parameter pressure infimum.

## 7.3 Concavity and boundary saddle

Include the exact saddle equation and the `Q=P` boundary regime.

## 7.4 Uniform low-pressure count

Present the repaired two-regime uniformity lemma:

- bounded-saddle interior;
- large fixed Chernoff parameter near the boundary.

Avoid the superseded one-piece compactness argument entirely.

## 7.5 Theorem C — audited scale-family accumulation

State only the frozen quantifiers:

for `epsilon_r->0`, `r epsilon_r->infinity`, and the associated Task-6 scales `N_r`, every accumulation point of the type-density pair satisfies

`rho in F`,
`h(rho)>=alpha/kappa`.

Do NOT replace this with arbitrary `N->infinity`; that strengthening is not frozen.

---

# 8. Density corollaries and certified phase geometry

## 8.1 Natural-density corollary

If natural type densities exist, apply Theorem C.

## 8.2 Sparse critical sites

If total critical count is `o(N)`, deduce the zero-density endpoint and therefore

`kappa>2.784`.

Highlight this as a hypothesis-form strengthening of pointwise zero-criticality.

## 8.3 Minimum critical density

Define

`rho_min(kappa)=inf{rho_1+rho_2: rho in F, h(rho)>=alpha/kappa}`.

Give certified intervals for `kappa=1.06,1.5,2.0`.

A figure of `rho_min(kappa)` is desirable later, but any plotted curve must be generated from the certified/formally specified pressure and visually distinguished from proof-critical interval assertions.

## 8.4 CP19 consistency endpoint

Show that maximizing `h` over `F` recovers the older unrestricted entropy exactly.

State explicitly that there is **no** strict optimized Sturmian phase cost.

---

# 9. Scope and limitations

A dedicated section should state:

The results do not prove Collatz and do not exclude:

- discrepancy laws outside `s_k=kappa log_2 k+O(1)`;
- all high-`kappa` critical-log regimes;
- general positive divergent trajectories;
- general nontrivial cycles;
- the CP19 Task-5 survivor by Task-8A, because of hypothesis mismatch.

Also distinguish:

- theorem-level results;
- certified numerical constants;
- historical exploratory observations not used in the manuscript.

---

# 10. Reproducibility and exact certification

Include a concise reproducibility section or appendix listing:

- frozen theorem source versions;
- independent audit decisions;
- exact interval certificate scripts and output hashes;
- proof-critical rational inequalities;
- informational high-precision decimals.

The manuscript should be mathematically readable without running code. Code certifies numerical inequalities; it does not replace proofs of universal statements.

---

# 11. Appendices

## Appendix A — Exact pressure algebra

Finite `B`, `B=infinity`, convexity/minimizer details.

## Appendix B — Task-8A feasible-domain and two-regime uniformity details

This is where the audit repairs should be made maximally transparent.

## Appendix C — Certificate specification

State exact rational target inequalities and reproduction commands.

## Appendix D — Extended prior-art comparison

Optional, but advisable if introduction length becomes excessive. Include a theorem-by-theorem comparison table for Witteveen and `collatz-things`.

---

# 12. Claim-discipline checklist before manuscript freeze

The manuscript must pass all of the following:

1. Every theorem is traceable to an audited/frozen source.
2. No arbitrary-`N` Task-8A strengthening appears as proved.
3. The Chernoff sign is correct everywhere.
4. “Unbounded valuations” is not used as a theorem claim.
5. The CP19 Task-5 hypothesis mismatch is respected.
6. Witteveen 2026 is cited before claiming novelty around factor complexity/entropy/repeated factors.
7. The July 2026 integral-escape residual work is discussed before any claim about complexity/repetition versus integrality.
8. No “first” claim appears without a new specialist priority audit.
9. Certified decimals are separated from exact inequalities.
10. The abstract and title do not imply a proof of the Collatz conjecture.

---

# 13. Recommended drafting order

1. Sections 4–6: frozen Task-6/7 proof spine.
2. Section 7: frozen Task-8A repaired theorem.
3. Section 8: corollaries/certificates.
4. Related work / novelty section.
5. Introduction and abstract last.

This order minimizes the risk that publication rhetoric outruns the exact frozen theorem scope.
