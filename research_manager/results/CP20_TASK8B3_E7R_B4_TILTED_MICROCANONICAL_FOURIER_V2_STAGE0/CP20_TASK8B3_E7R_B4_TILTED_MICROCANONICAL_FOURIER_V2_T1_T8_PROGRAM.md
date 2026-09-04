# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — T1–T8 STAGE-1 PROGRAM

Stage 0 status: **PROGRAM FROZEN; NOT ADJUDICATED AS STAGE-1 THEOREMS**

## T1 — Conditional-law invariance
Prove exactly that iid Geom(p), conditioned on total `T`, is uniform on positive compositions of `T` into `r` parts, and therefore the project conditional law is unchanged at `p_*`.

Stage-0 permission used: finite pure-algebra checks only.

## T2 — Centrality under the tilt
Prove `E_(p_*)[sum A_i]=alpha r` and `-9<delta_r<=-8`.
Mandatory guardrail: this does not alter `T_r/r -> alpha != 2` and does not place the project in Si's frozen `s~2n` theorem regime.

Stage-0 permission used: pure algebra/tiny fixed numerical sanity only.

## T3 — Exact denominator
Establish
`D_r=binom(T_r-1,r-1)p_*^r q_*^(T_r-r)`
and rigorously prove the local limit
`D_r ~ 1/sqrt(2*pi*alpha(alpha-1)r)`
with an error sufficient for the later quotient.

Stage 0 verifies only the exact formula on preregistered tiny cases. The asymptotic is not Stage-0 evidence.

## T4 — Exact numerator reduction
With `chi_r=e_(3^r)(eta_r F_r^aff)`, establish exactly
`N_r=E_(p_*)[chi_r 1_(sum A_i=T_r)]`
and `G_r=N_r/D_r`.

Stage 0 checks only definition-level finite algebra.

## T5 — Required numerator scale
Use the denominator theorem to justify that `N_r=O(r^(-3/2))` suffices for `G_r=O(1/r)`.
Reject `O(r^-1/2)` and unspecified `o(r^-1/2)` as insufficient.

## T6 — Total-sum Fourier inversion
Use the frozen convention
`H_r(t)=E_(p_*)[chi_r exp(i t(sum A_i-alpha r))]`
and
`N_r=(1/(2*pi)) integral exp(-it(T_r-alpha r))H_r(t)dt`.
Derive the sign/index convention exactly.

Stage 0 mechanically tests the convention only on fixed finite surrogates.

## T7 — New joint Fourier / renewal theorem
Develop, rather than import, a theorem strong enough to bound the integral of `H_r(t)` by `O(r^-3/2)`, uniformly at the moving primitive frequency `eta_r`.

Frozen deterministic arcs:
`L_r=(ln(r+1))^(1/4)`.
- major: `|t|<=L_r/sqrt(r)`
- intermediate: `L_r/sqrt(r)<|t|<=r^-1/4`
- minor: `r^-1/4<|t|<=pi`

Mandatory internal falsification:
- T7-F1: load-bearing p=1/2 identity without p_* analogue;
- T7-F2: unit-modulus tilted resonance/eigenvalue;
- T7-F3: `H_r(0)` too large;
- T7-F4: nonzero central leading term of order `r^-1/2`;
- T7-F5: cancellation is numerical rather than exact algebra.

No leading-coefficient cancellation may be claimed without exact derivation.

## T8 — Preregistered fallbacks; DO NOT EXECUTE before direct route adjudication
T8-A: saddlepoint/Edgeworth expansion of the joint tilted transform.
Primary question: does the leading coefficient vanish exactly?

T8-B: endpoint-weighted/cotransition block decomposition.
Primary question: can actual endpoint weights control the global conditional expectation despite B3-CT?

No T8 fallback may begin until the direct tilted joint-transform route has been adjudicated according to the sealed stop/failure logic.

## Global guardrails
G1–G8 from the Stage-0 order are binding:
tilt changes proof measure only; no Si/Tao auto-transfer; no qualitative-decay overclaim; moving-frequency uniformity is mandatory; no global mod-16 cancellation; B3-CT constrains every block mechanism.
