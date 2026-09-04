# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1 — PRE-RUN SEAL

Status: **STAGE 0 FROZEN — STAGE 1 NOT AUTHORIZED**

Canonical base: `57f670bd531cee8f0f2d6eeb27431243f6e3a479`
Working branch: `cp20-e7r-b4-tilted-microcanonical-fourier-v1-stage0-20260904`

Canonical handoff: `HANDOFF VERIFICATION: PASS` via GitHub Actions run `33853874663`.

Order source SHA-256: `90dbb1b229a6f5d7677251ce250ef377dba36b369a566d9cc0207aff420a333a`.

## Frozen scientific target

`alpha=log_2(3)`,
`T_r=floor(alpha*r)-8`,
`eta_r=2^(T_r-4) mod 3^r`,

`G_r=E[e_(3^r)(eta_r F_r^aff) | sum A_i=T_r]`.

Target: `|G_r|=O(1/r)`.

## Frozen tilted law

`P_p(A=m)=p(1-p)^(m-1)`.

`p_*=1/alpha`, `q_*=1-p_*`,
`sigma_*^2=alpha(alpha-1)`.

Tilting changes only the unconditioned proof measure. It supplies zero cancellation by itself.

## Frozen Stage-1 program

T1 conditional-law invariance.
T2 centrality under the tilt.
T3 exact denominator + rigorous LLT.
T4 exact numerator/quotient reduction.
T5 required numerator scale.
T6 exact total-sum Fourier inversion.
T7 new joint Fourier/renewal theorem at moving primitive frequency.
T8 preregistered fallbacks only after direct route adjudication.

Frozen deterministic arcs:
`L_r=(ln(r+1))^(1/4)`;
major `|t|<=L_r/sqrt(r)`;
intermediate `L_r/sqrt(r)<|t|<=r^-1/4`;
minor `r^-1/4<|t|<=pi`.

## Frozen falsification inventory

F1–F10 and T7-F1–T7-F5 are frozen exactly in the sealed falsification/program files.

## Frozen outcome ladder

B4-N1 through B4-N7 and B4-CT exactly as recorded in the sealed outcome ladder.

## Guardrails

- no Tao/Si theorem auto-transfer after tilting;
- Si's deterministic ratio `s/n` is not changed by proof measure;
- no qualitative-decay overclaim;
- no adaptive r/t search;
- no weighted/operator calculations;
- no E8;
- B3-CT remains a binding falsification constraint;
- no independent global mod-16 cancellation exists.

## Stage-1 execution-integrity contract

Present: **YES**

Contract SHA-256:
`3d9fd4c0c029c135b86c43377aa414c87704f5e6c3dd4a008fa621f3b4f1185e`

The future canonical integrator MUST canonicalize this contract before any manager authorization/execution.

## Stage-0 permitted checks

Result: **PASS**
Result SHA-256: `070297c3e11b4589b1a935395f43d90f201cd2af8176e68b621e416f5a47ac8c`.

These checks verify only finite algebra/indexing:
conditional composition weights, exact negative-binomial formula, exact quotient identity, frozen Fourier sign/index convention on finite surrogates, and arc ordering. They prove no asymptotic decay.

## Stage-1 execution state

**NOT EXECUTED.**
No Stage-1 witness, ledger, result, theorem, fallback, weighted/operator work or E8 work was created/executed in Stage 0.
