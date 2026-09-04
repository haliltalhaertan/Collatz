# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1 — TARGET NORMAL FORM

Frozen exact object:

`G_r = E[e_(3^r)(eta_r F_r^aff) | sum_i A_i=T_r]`

where

`alpha=log_2(3)`,
`T_r=floor(alpha*r)-8`,
`eta_r=2^(T_r-4) mod 3^r`.

Change of proof measure:

`P_p(A=m)=p(1-p)^(m-1)`.

Candidate centralizing choice:

`p_*=1/alpha`.

Exact conditional-law candidate:

For every positive composition `a_1+...+a_r=T`,

`P_p(A_1=a_1,...,A_r=a_r)=p^r(1-p)^(T-r)`,

which depends only on `T`. Hence the conditional law at fixed total is uniform and independent of `p`.

Frozen tilted quotient normal form:

`G_r=N_r/D_r`,

`D_r=P_(p_*)(sum A_i=T_r)`,

`N_r=E_(p_*)[e_(3^r)(eta_r F_r^aff) 1_(sum A_i=T_r)]`.

Future quantitative implication to prove, not a Stage-0 result:

`D_r ~ c_* r^(-1/2)` and `N_r=O(r^(-3/2))` would imply `G_r=O(1/r)`.

Guardrail:
- tilting alone gives no cancellation;
- the deterministic ratio `T_r/r -> alpha != 2` is unchanged;
- Si's frozen central `s~2n` theorem is not made applicable by this change of reference law;
- Tao's Geom(2) theorem does not automatically transfer to Geom(p_*).
