# CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1 — STAGE 1 ZERO-TRUST LOAD-BEARING AUDIT

Audit date: 2026-09-04

## FINAL VERDICT

**[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]**

Execution integrity: **[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]**  
Package integrity: **[PACKAGE INTEGRITY PASS]**

This audit does not integrate canonical state, does not continue mathematical research, does not rerun Stage 1, and does not begin weighted/operator work or E8.

## 1. Scope and authoritative inputs

Repository: `haliltalhaertan/Collatz`  
Canonical authorization commit: `9119a39957705f53060c380acf3e8f4dd6609565`  
Stage-1 result branch: `cp20-e7r-literature-transfer-v1-stage1-audit-stop-20260904`  
Stage-1 branch HEAD: `93201a44924562eddb951d083370e42e0ec8bf00`

Authorized Stage-0 seal ZIP SHA-256:

`403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79`

Stage-1 complete package SHA-256:

`978d8b90c58131dcf350699920a241fee7a7d7b4c2abeff5cb1ea45da96e120e`

Stage-1 manifest SHA-256:

`f8afcf1778722bd8715a78792d9855c65c0849c8fc722f00096fd67bc6c9d4c4`

Independent finite-phase implementation SHA-256:

`a6384e10c11b1e7b61183d1009811eaed4837112666c715bfca70f9d8df106b4`

The producer report/verifier was not treated as independent mathematical evidence.

## 2. Integrity and provenance adjudication

### 2.1 Package / seal integrity

Independent raw-byte recomputation gives exactly the authorized hashes above.

The Stage-1 ZIP contains exactly 10 members. Member names are unique. ZIP CRC verification passes. The Stage-1 SHA-256 manifest itself has the stated SHA-256, and every manifested Stage-1 member independently rehashes to its recorded value.

The embedded pre-run seal independently rehashes to the authorized Stage-0 seal SHA-256. It contains 18 frozen members, and every entry of its pre-run manifest verifies independently.

Frozen source hashes independently recomputed from the embedded seal are:

- Tao v7 PDF: `62cf49d4d8e8e681c7a4738ebaf56f3dbb7b67de95f37ccbac6e428ef3fc394e`;
- Tao v7 source tar: `ba81acd6254838251f1ee585256a6f9f223cdc9c73bed0a3c4fd25782d0124ad`;
- Si GitHub `main.tex`: `c1ff1f11f442fed1b2f7a37be61fe0e3c0916719549018557446ca01e81e0811`;
- Si GitHub `main.pdf`: `0dfad7f22df91c14c36182d7557aee537a462ef0a2a548422c366d21e2bd06c8`;
- Si Zenodo `main.pdf`: the same `0dfad7f22df91c14c36182d7557aee537a462ef0a2a548422c366d21e2bd06c8`.

The package downloaded afresh from the declared Drive file rehashes to the authoritative Stage-1 package SHA-256. Therefore the Drive package read-back is byte-identical to the audited package.

### 2.2 Independent finite-phase implementation

The file with SHA-256 `a6384e10...106b4` does not import the sealed candidate helper and is byte-distinct from it. The sealed helper exposes `candidate_m3_project_exponent`; the independent implementation instead defines its own analytic phase, inverse-correction, unified-residue, affine-offset and exact-composition routines. It is therefore distinct in both bytes and implementation structure.

The independent audit reproduction additionally rederived all six negative-exponent values exactly and checked 461 small composition cases of the load-bearing M3 identity with zero failures.

### 2.3 Execution history and missing addendum

The exact string `STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT_ADDENDUM` is absent from the canonical repository state inspected by this audit. Thus the previously recommended addendum was not canonicalized before the run.

This is a real documentation gap, but it does not by itself invalidate the preserved run.

The following are independently recoverable:

1. the canonical authorization commit predates the Stage-1 result branch and explicitly records Stage 1 as authorized but not yet executed;
2. the result branch is a linear descendant of that authorization commit;
3. the branch contains one preserved Stage-1 result/provenance set bound to the authorized seal;
4. the preserved mechanical result and provenance each record execution count `1`;
5. authorization required the candidate M3 helper not be used as evidence and required an independent exact implementation; the returned package contains such a distinct implementation;
6. the only GitHub Actions run on the Stage-1 result branch was a later persistence workflow, and it failed before creating any job (`jobs.total_count=0`), so it did not execute or rerun Stage-1 mathematics;
7. the branch history after the LT-CT audit stop consists of result/report/hash/provenance/persistence/read-back recording, with no weighted/operator or E8 work;
8. the Drive package read-back is byte-identical to the immutable package hash.

What cannot be established cryptographically after the fact, because the addendum was not precommitted, is the stronger statement that no unrecorded local/private invocation of the Stage-1 script could possibly have occurred. There is no evidence of such an extra run, but there is no pre-run one-shot nonce/output-absence contract that would make that negative fact cryptographically complete.

Accordingly:

**[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]**

A rerun is neither needed nor authorized merely to repair that paperwork gap.

## 3. M1 — exact microcanonical law

Let `A_i=Z_i+1`. Under `S_r=n_r`,

\[
\sum_{i=1}^r A_i=r+n_r
=r+\lfloor(\alpha-1)r\rfloor-8
=\lfloor\alpha r\rfloor-8=:T_r.
\]

For every weak composition `z_1+...+z_r=n_r`, the iid project probability is

\[
\prod_i2^{-(z_i+1)}=2^{-(n_r+r)},
\]

so the conditional law is exactly uniform. Shifting by one is a bijection from weak compositions of `n_r` into `r` parts to positive compositions of `T_r` into `r` parts.

Under Si's positive `Geom(2)` convention, a tuple `a_i>=1` has iid mass `2^{-\sum a_i}`. Hence conditioning on `\sum a_i=T_r` also gives the exact uniform positive-composition law. This is equality of finite conditional distributions, not ensemble equivalence.

**M1: [PASS]**  
**LT-N1: [PROVED — AUDITED]**  
**F1: NOT_TRIGGERED**

## 4. M2 — Bernoulli bridge

For a positive composition `(b_1,...,b_r)` of `T_r`, read the reversed composition `b_i=a_{r+1-i}`. Stars-and-bars uses a binary word of length

\[
m=T_r-1
\]

with exactly

\[
r-1
\]

ones. If `p_t=b_1+...+b_t`, the `t`-th one occurs at position `p_t`. Conversely, with `p_0=0,p_r=T_r`, one recovers `b_t=p_t-p_{t-1}`.

This is exactly the frozen Si Bernoulli-bridge convention: `m=s-1`, bridge one-count `r_Si=n-1`, with literature `n=r_project`, `s=T_r`. Reversal is a bijection and preserves the uniform microcanonical law. No `+1/-1` mismatch remains.

**M2: [PASS]**  
**LT-N2: [PROVED — AUDITED]**  
**F2: NOT_TRIGGERED**

## 5. M3 — exact project phase / affine-offset identity

Tao's frozen affine offset is

\[
F_r^{\rm aff}(a_1,\dots,a_r)
=\sum_{m=1}^r3^{r-m}2^{-a_{[m,r]}}.
\]

Put `T=\sum_i a_i` and `a_i=Z_i+1`. For project row `s>=2`,

\[
s+S_{s-1}-5
=\sum_{i<s}a_i-4.
\]

The boundary row `s=1` is

\[
\zeta_4=e(1/48)=e\!\left(\frac{2^{-4}}3\right),
\]

which is exactly the same prefix formula with empty prefix.

Therefore the total project phase exponent is

\[
\Phi_r
=\frac1{16}\sum_{s=1}^r\frac{2^{a_{[1,s-1]}}}{3^s}.
\]

On the other hand,

\[
\frac{2^T}{16\,3^r}F_r^{\rm aff}
=\frac1{16}\sum_{m=1}^r\frac{2^{T-a_{[m,r]}}}{3^m}
=\frac1{16}\sum_{m=1}^r\frac{2^{a_{[1,m-1]}}}{3^m}
=\Phi_r.
\]

Thus the identity is exact as a rational phase:

\[
\boxed{
F_{r,4}^{\rm project}
=\exp\!\left(2\pi i\frac{2^T F_r^{\rm aff}}{16\,3^r}\right).
}
\]

### Six negative-exponent rows

Independent modular-inverse-plus-dyadic-correction calculations give exactly:

- `(2,0)`: `1/72`;
- `(2,1)`: `1/36`;
- `(2,2)`: `1/18`;
- `(3,0)`: `1/108`;
- `(3,1)`: `1/54`;
- `(4,0)`: `1/162`.

For example, `(2,0)` has `rho=8 mod 9`, `8*8=1+7*9`, hence

\[
\frac89-\frac78=\frac1{72}.
\]

The unified modulus formula gives the same phases, including `M_1=48,R_{1,0}=1` at the boundary.

The independent audit script checked 461 small composition instances of the complete M3 rational identity and found zero failures.

### Fixed-total character

Under `T=T_r`, `2^T F_r^{aff}` is integral modulo `3^r`, and the factor `1/16` is a unit modulo `3^r`. Hence

\[
F_{r,4}^{\rm project}
=\mathbf e_{3^r}(\eta_rF_r^{\rm aff}),
\qquad
\eta_r=2^{T_r-4}\pmod{3^r}.
\]

No separate mod-16 cocycle survives globally. The dyadic factor is fully absorbed into the primitive ternary frequency.

**M3: [PASS]**  
**LT-N3: [PROVED — AUDITED]**  
**F3: NOT_TRIGGERED**

## 6. M4 — frequency and effective depth

Since `eta_r` is a power of two modulo `3^r`,

\[
v_3(\eta_r)=0.
\]

For the global project modulus there is no oversampling: `k=0`. Therefore

\[
h=k-v_3(\eta_r)=0,
\qquad
d=r+h=r.
\]

In Si's bridge normalization,

\[
q_r\equiv\eta_r2^{-T_r}\equiv2^{-4}\pmod{3^r}.
\]

Tao uses the character convention `exp(-2*pi*i xi x/3^r)` whereas the project/Si convention here is positive. Thus the project coefficient corresponds to Tao's primitive frequency `xi_Tao=-eta_r`; Tao's uniform primitive-frequency statement is invariant under this sign replacement.

The global target is therefore **not** in Si's new `h>=1` hard-frequency regime; it is an `h=0` primitive coefficient.

**M4: [PASS]**  
**LT-N4: [PROVED — AUDITED]**  
**F4: TRIGGERED**

## 7. M5 — observable type

After M3-M4, the exact object is

\[
G_r=
\mathbb E\left[
\mathbf e_{3^r}(\eta_rF_r^{\rm aff})
\mid \sum_{i=1}^ra_i=T_r
\right].
\]

This is literally one primitive microcanonical Fourier coefficient of the affine offset. It is not a derivative, finite difference, adjacent-frequency extraction, centered degree-one correction, or parameter derivative.

**M5: [PASS]**

## 8. M6 — Si regime / entropy parameter

With literature variables `n=r`, `s=T_r`, `h=0`, and `theta_r={alpha r}`,

\[
\Delta_r
=T_r\log_3 2-r
=\frac{\alpha r-\theta_r-8}{\alpha}-r
=-\frac{\theta_r+8}{\alpha}.
\]

Since `0<=theta_r<1`,

\[
-\frac9\alpha<\Delta_r\le-\frac8\alpha.
\]

So the algebraic `Delta` correspondence is exact and bounded; it is not a notation coincidence.

But every frozen Si analytic decay theorem relevant to this transfer has a central/half-density hypothesis. Examples verified directly in the frozen source include:

- sharp resonant phase transition: `s=2n+O(sqrt(n log n))` and `h>=1`;
- logarithmic-oversampling hard decay: `|s-2n|<=L sqrt(n log n)`;
- subdiffusive transfer: `s=2n+O(sqrt n)`;
- primitive bridge decay: `r_bridge=m/2+O(sqrt(m log m))`;
- density-one/fiberwise bridge results: the corresponding half-density form.

The project instead satisfies

\[
T_r=\alpha r+O(1),\qquad\alpha=\log_2 3=1.5849625\ldots,
\]

so

\[
T_r-2r=(\alpha-2)r+O(1),
\]

a linear discrepancy. Thus the project lies outside those analytic hypotheses.

**M6: [PASS]**  
**LT-N5: [PROVED — AUDITED]**  
**F5: TRIGGERED**  
**F6: NOT_TRIGGERED**

## 9. M7 — B3-CT consistency mapping

For a project block `(u,v,k,ell)`, put

\[
m=v-u,
\qquad
B=m+\ell-k
\]

for the total of the shifted positive block variables.

The global row exponent factors as

\[
\frac{2^{u+k-4}}{3^u}
\sum_{p=1}^m\frac{2^{a_{[1,p-1]}}}{3^p}.
\]

Using the local affine-offset identity gives the block modulus `3^v=3^{m+u}` and local frequency

\[
\eta_{\rm block}=2^{v+\ell-4}.
\]

Hence the exact Si block parameters are

\[
h_{\rm block}=u,
\qquad
q_{\rm block}=\eta_{\rm block}2^{-B}=2^{u+k-4}.
\]

For the audited CF-left family,

\[
B=m+\ell-k
=\alpha m-\frac{m(\theta_r+8)}r+O(1),
\]

so

\[
\Delta_{\rm block}
=B/\alpha-m-u
=-u+O(1)\to-\infty.
\]

The frozen Si source itself describes exceptional arithmetic resonances in terms of residues asymptotically congruent to `±2^a` at increasing ternary depth. The exact project block frequency `q_block=2^{u+k-4}` is of that arithmetic type, and `Delta_block->-infinity` is qualitatively nondecaying/supercritical. Thus B3-CT nondecay is genuinely **consistent** with the source's resonance classification.

This is not a theorem transfer: Si's sharp displayed nondecay theorem requires a central bridge and its exact resonant case has normalized `q=1`. Those hypotheses are not satisfied here.

**M7: [PASS — CONSISTENCY CLASSIFICATION ONLY]**  
**F7: NOT_TRIGGERED**

## 10. M8 / LT-CT — direct theorem-transfer obstruction

The exact project fiber is

\[
\boxed{
G_r=\mathbb E\left[
\mathbf e_{3^r}(\eta_rF_r^{\rm aff})
\mid\sum a_i=T_r
\right],
\qquad
\eta_r=2^{T_r-4}\pmod{3^r}.
}
\]

For iid positive `Geom(2)` variables, every composition of total `T_r` has probability `2^{-T_r}`, and there are `C(T_r-1,r-1)` such compositions. Thus exactly

\[
\boxed{
\Pr\left(\sum a_i=T_r\right)
=\binom{T_r-1}{r-1}2^{-T_r}.
}
\]

With `T_r=alpha r+O(1)`, Stirling gives

\[
\log\Pr(\sum a_i=T_r)
=r\left[\alpha H(1/\alpha)-\alpha\log2\right]+o(r),
\]

hence

\[
\boxed{
\Pr(\sum a_i=T_r)=\exp(-I_\alpha r+o(r)),
}
\]

where

\[
I_\alpha
=\alpha\log2-\alpha H(1/\alpha)
=0.05497947281081705\ldots>0.
\]

### What Tao controls

Frozen Tao Proposition 1.17 (`f-decay`) states, uniformly for primitive `xi mod 3^n`,

\[
\mathbb E\exp\left(-2\pi i\xi\,\Syrac(\mathbb Z/3^n\mathbb Z)/3^n\right)
\ll_A n^{-A}.
\]

By Tao's definition, `Syrac(Z/3^nZ)=F_n(Geom(2)^n) mod 3^n`. This is the **unconditioned iid** Fourier coefficient. Section 7 proves the same unconditioned estimate through the white-point/two-dimensional-renewal machinery. It does not state a bound for each individual fixed-total fiber.

The project target is one exponentially rare microcanonical fiber. The direct conditioning inequality used by Si would divide an unconditional bound by `P(S_n=T_r)`, introducing `exp(I_alpha r+o(r))`. Tao's available `n^{-A}` control for every fixed `A` cannot absorb that exponential factor. More fundamentally, an average over all total-sum fibers does not bound one exponentially rare fiber.

### What frozen Si controls

Si gives an exact bridge-reduction identity for the microcanonical coefficient, but its **analytic decay/nondecay theorems** relevant here require central totals or the equivalent half-density Bernoulli bridge. The project total `T_r/r->alpha` is linearly separated from `2`. No sealed Si theorem inspected supplies individual primitive-frequency decay for this off-central fiber.

Therefore the exact load-bearing conclusion is:

> No analytic theorem in the frozen Tao v7 / Si 2026 source set directly controls the exact project microcanonical fiber strongly enough to imply E6-N2.

This closes only the **direct sealed-theorem transfer route**. It does not establish that Tao/Si ideas cannot be adapted by a new theorem, that no new off-central theorem exists, that weighted/operator methods fail, that modified geometry fails, or that E6-N2 is false.

**M8: [PASS — NO DIRECT THEOREM MATCH]**  
**F8: TRIGGERED**  
**LT-CT: [PROVED — AUDITED]**

## 11. Complete adjudication table

### M1–M8

- M1: `[PASS]`
- M2: `[PASS]`
- M3: `[PASS]`
- M4: `[PASS]`
- M5: `[PASS]`
- M6: `[PASS]`
- M7: `[PASS — CONSISTENCY CLASSIFICATION ONLY]`
- M8: `[PASS — NO DIRECT THEOREM MATCH]`

### LT ladder

- LT-N1: `[PROVED — AUDITED]`
- LT-N2: `[PROVED — AUDITED]`
- LT-N3: `[PROVED — AUDITED]`
- LT-N4: `[PROVED — AUDITED]`
- LT-N5: `[PROVED — AUDITED]`
- LT-N6: `[NOT PROVED]`
- LT-N7: `[NOT PROVED]`
- LT-CT: `[PROVED — AUDITED]`

### F1–F8

- F1: `NOT_TRIGGERED`
- F2: `NOT_TRIGGERED`
- F3: `NOT_TRIGGERED`
- F4: `TRIGGERED`
- F5: `TRIGGERED`
- F6: `NOT_TRIGGERED`
- F7: `NOT_TRIGGERED`
- F8: `TRIGGERED`

### Governance / integrity

- Execution integrity: `[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]`
- Package integrity: `[PACKAGE INTEGRITY PASS]`
- Drive package byte read-back: `PASS`
- Stage-1 rerun during this audit: `NO`
- Downstream mathematical work authorized/performed by this audit: `NO`
- Canonical integration performed by this audit: `NO`

## 12. What remains open

`E6-N2` remains **OPEN**.

Also open, within the scope of this audit:

- any new off-central microcanonical Fourier theorem applicable at `T_r/r -> log_2 3`;
- any adaptation of Tao/Si ideas beyond the theorems frozen here;
- weighted/operator approaches;
- modified geometry or different observables;
- E8 and any later research stage.

This audit authorizes none of those next steps; it only adjudicates the returned Stage-1 literature-transfer package.

## FINAL ADJUDICATION

**[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]**

Nothing in this audit proves the Collatz conjecture.
