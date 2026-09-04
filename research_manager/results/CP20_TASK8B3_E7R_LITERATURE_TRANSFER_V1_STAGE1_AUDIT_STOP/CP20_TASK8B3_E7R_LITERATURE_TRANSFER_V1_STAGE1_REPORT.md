# CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1 — STAGE 1 REPORT

Status: **[MANDATORY AUDIT STOP — LT-CT AT M8]**

Canonical authorization commit: `9119a39957705f53060c380acf3e8f4dd6609565`  
Authorized normalized Stage-0 seal ZIP SHA-256: `403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79`

No unsealed source revision was used. Tao `1909.03562v7` was treated as known literature. Si 2026 theorem statements remain `[LITERATURE CLAIM — UNAUDITED]` unless an identity was rederived independently from frozen definitions.

## Independent finite-phase implementation

The sealed `candidate_m3_project_exponent()` was not used as mathematical evidence.

Independent implementation:
`CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_INDEPENDENT_FINITE_PHASE.py`

SHA-256:
`a6384e10c11b1e7b61183d1009811eaed4837112666c715bfca70f9d8df106b4`

It independently implements both:

1. the negative-exponent modular-inverse plus dyadic-correction formula; and
2. the unified modulus/residue formula
   `M_s=2^max(0,5-s) 3^s`, `R_{s,j}=2^(j+max(0,s-5)) mod M_s`.

Mechanical checks: all six frozen negative-exponent cases agree exactly; 198 wider grid cases agree exactly; 1,715 small weak-composition cases independently corroborate M3. These finite checks are corroboration, not the proof of the identities below.

## M1 — exact microcanonical composition match

**Status: [PROVED]. LT-N1 [PROVED]. F1 NOT_TRIGGERED.**

Set `a_i=A_i=Z_i+1`. Under the project condition `S_r=n_r`,

`sum_i a_i = r+n_r =: T_r = floor(alpha r)-8`.

Every project weak composition `z_1+...+z_r=n_r` has the same conditional probability. The shift `a_i=z_i+1` is a bijection to positive compositions

`a_1+...+a_r=T_r`, `a_i>=1`.

For iid positive `Geom(2)` variables, every tuple with total `T_r` has unconditioned mass `2^{-T_r}`; hence conditioning on the total also gives the uniform positive-composition law. Therefore the project microcanonical law is exactly the same finite law as Si's microcanonical positive-composition ensemble with literature length `n=r` and total `s=T_r`. This is exact equality, not ensemble equivalence.

## M2 — exact Bernoulli-bridge match

**Status: [PROVED]. LT-N2 [PROVED]. F2 NOT_TRIGGERED.**

A positive composition of `T_r` into `r` parts maps by stars-and-bars to a binary string of length

`m=T_r-1`

with exactly

`r-1`

ones. This is exactly Si's `Omega_{m,r'}` convention after renaming Si's bridge count `r'=n-1=r-1`. Si reverses the positive composition before locating separator positions; reversal is a bijection and preserves the uniform microcanonical law. No endpoint, bar-count, or `+1/-1` mismatch remains.

## M3 — exact affine-offset / Fourier-character identity

**Status: [PROVED]. LT-N3 [PROVED]. F3 NOT_TRIGGERED.**

Let `a_i=Z_i+1`, `T=sum_i a_i`, and let `F_r^aff(a)` be the Tao/Si affine offset

`F_r^aff(a)=sum_{m=1}^r 3^(r-m) 2^(-a_[m,r])`.

For row `s>=2`,

`s+S_{s-1}-5 = a_[1,s-1]-4`.

The boundary factor is also the missing `s=1` term because

`1/48 = 2^(-4)/3`.

Hence the total project phase exponent is exactly

`Phi_r = (1/16) sum_{s=1}^r 2^(a_[1,s-1]) / 3^s`.

On the other hand,

`(2^T/(16 3^r)) F_r^aff(a)`

`= (1/16) sum_{m=1}^r 2^(T-a_[m,r]) / 3^m`

`= (1/16) sum_{m=1}^r 2^(a_[1,m-1]) / 3^m`

`= Phi_r`.

Therefore, as an exact rational identity before taking the exponential,

`F_{r,4}^{project} = exp(2 pi i * 2^T F_r^aff(a)/(16 3^r))`.

The independently implemented negative-exponent correction verifies that the early dyadic rows represent this same analytic phase; no silent modular-inverse substitution is used.

## M4 — exact C=4 frequency/depth mapping

**Status: [PROVED]. LT-N4 [PROVED]. F4 TRIGGERED.**

Under the microcanonical condition `T=T_r`, M3 gives

`G_{r,n_r}=E[e_{3^r}(eta_r F_r^aff) | sum a_i=T_r]`,

where

`eta_r = 2^(T_r-4) mod 3^r`.

Thus `eta_r` is primitive: `v_3(eta_r)=0`.

In Si notation the exact global mapping is

- literature iterate length `n=r`;
- modulus `3^(n+k)=3^r`, hence `k=0`;
- `v_3(eta_r)=0`;
- `h=k-v_3(eta_r)=0`;
- effective depth `d(eta_r)=n+h=r`.

The factor `C=4` is the dyadic unit `2^-4` absorbed into the primitive Fourier frequency; it does not create positive ternary oversampling depth. For the bridge-reduction normalization,

`q_r = eta_r 2^(-T_r) = 2^-4 mod 3^r`.

Therefore the exact global target is not in Si's `h>=1` hard-frequency regime. F4 is triggered.

(Tao's Fourier convention uses the opposite sign; replacing Tao's primitive frequency by its negative handles this without changing any hypothesis.)

## M5 — degree-one correction classification

**Status: [PROVED].**

After M3-M4, the project target is literally a single microcanonical Fourier coefficient of the affine offset at a primitive frequency. It is not a frequency derivative, parameter derivative, finite difference, adjacent-frequency difference, or degree-one correction of a Fourier coefficient. The `2^-4` factor changes the frequency by a fixed dyadic unit only.

## M6 — exact entropy/critical-scale classification

**Status: [PROVED]. LT-N5 [PROVED]. F5 TRIGGERED. F6 NOT_TRIGGERED.**

With the exact M4 variables `n=r`, `s=T_r`, `h=0`, Si's formal entropy parameter becomes

`Delta_r = T_r log_3 2 - r`.

Writing `theta_r={alpha r}` and using `log_3 2=1/alpha`,

`Delta_r = -(theta_r+8)/alpha`.

Thus for every `r`,

`-9/alpha < Delta_r <= -8/alpha`.

So the project lies in a bounded `Delta=O(1)` critical-scale strip of the general algebraic parameter; it is neither a `Delta -> +infinity` nor a `Delta -> -infinity` global sequence. This match is exact after M1-M4 and is not a notation coincidence, so F6 is not triggered.

However Si's stated analytic microcanonical decay/phase-transition theorems use central positive-geometric totals `s=2n+O(sqrt(n log n))` (or stronger variants). The project has

`T_r = alpha r + O(1)`, with `alpha=log_2 3 != 2`,

so

`|T_r-2r| = (2-alpha)r + O(1)`,

a linear discrepancy. The project is therefore outside those central-bridge hypotheses. F5 is triggered.

## M7 — B3-CT / resonance consistency

**Status: [PROVED as an exact consistency classification]. F7 NOT_TRIGGERED.**

For a project block `[u,v]` with endpoint states `(k,ell)`, put

`m=v-u`, `B=m+ell-k`.

Conditioned on the endpoints, the block positive variables form a uniform positive composition of total `B` into `m` parts. The block phase equals exactly

`e_{3^v}(eta_block F_m^aff)`

with

`eta_block = 2^(v+ell-4)`,

so in Si depth notation for this block

- length `n_block=m`;
- modulus exponent `N_block=v=m+u`;
- `h_block=u`;
- `v_3(eta_block)=0`;
- normalized bridge frequency
  `q_block = eta_block 2^(-B) = 2^(u+k-4) mod 3^v`.

For the audited CF-left family, write the endpoint rounding errors as `eps_u,eps_v in [0,1)`. Then

`B = alpha m - m(theta_r+8)/r + (eps_v-eps_u)`

and hence the exact block entropy parameter is

`Delta_block = B/alpha - m - u`

`= -u - m(theta_r+8)/(alpha r) + (eps_v-eps_u)/alpha`.

Therefore `Delta_block -> -infinity` because `u=floor(r/3)->infinity`.

This makes the audited `mathcal K^(4)->1` fully consistent with a supercritical/nondecaying hard-depth classification. Moreover `q_block` is an exact power of two for large `r`, matching the power-of-two resonance family discussed in the frozen Si source. This is only a consistency classification: Si's sharp resonant theorem assumes a central bridge and its displayed resonant case has `q=1`; those hypotheses are not silently substituted here. Therefore F7 is not triggered.

## M8 — Tao white-point / renewal transfer

**Status: [NO DIRECT MATCH]. F8 TRIGGERED. LT-CT [PROVED].**

Tao Proposition 1.17 / `f-decay` controls, uniformly over primitive frequency,

the **unconditioned** iid-Geometric coefficient

`E[e_{3^r}(eta F_r^aff)]`.

The exact project target from M3-M4 is instead the single microcanonical fiber

`G_r = E[e_{3^r}(eta_r F_r^aff) | sum a_i=T_r]`,

where `T_r=floor(alpha r)-8`.

The conditioning event has exact iid probability

`P(sum a_i=T_r)=C(T_r-1,r-1) 2^(-T_r)`.

Since `T_r/r -> alpha < 2`, Stirling's formula gives

`P(sum a_i=T_r)=exp(-I_alpha r+o(r))`

with

`I_alpha = alpha log 2 - alpha H(1/alpha) > 0`

(`H(x)=-x log x-(1-x)log(1-x)`). Numerically `I_alpha≈0.0549794728108171`.

Tao's white-point proof gives superpolynomial, but only polynomial-scale-in-`r`, control for every fixed power. The direct conditioning inequality used in Si's central transfer,

`E[e^{-cW}|sum a=T] <= E[e^{-cW}] / P(sum a=T)`,

therefore introduces an exponential factor `exp(I_alpha r+o(r))` here and yields no decay. More fundamentally, Tao's marginal Fourier estimate averages over all total-sum fibers and supplies no bound on this individual exponentially rare fiber.

The sealed Si source does transfer Tao's mechanism to microcanonical laws only under central-total hypotheses such as `s=2n+O(sqrt(n log n))`, and its subexponential bridge theorem uses the equivalent half-density bridge condition. M6 proves that the project violates those hypotheses by a linear amount.

### LT-CT — Direct sealed-theorem transfer obstruction

Let

`T_r=floor(alpha r)-8`, `eta_r=2^(T_r-4) mod 3^r`.

Then the exact project target is the conditional primitive affine-offset Fourier coefficient

`E[e_{3^r}(eta_r F_r^aff) | sum a_i=T_r]`.

Neither Tao Proposition 1.17 / its Section 7 white-point-renewal theorem nor any sealed Si analytic theorem identified in M4-M8 has hypotheses that control this exact fiber: Tao is unconditioned, while the Si microcanonical extensions require a central total/half-density bridge that the project misses linearly. Tao's polynomial white-point estimate cannot be transferred by the sealed conditioning argument because the project conditioning event is exponentially rare.

This closes the **direct theorem-transfer route from the sealed Tao/Si results to E6-N2**. It does not claim that Tao/Si ideas can never be adapted by a new theorem, and it does not close weighted/operator or modified-geometry routes.

This is a load-bearing rigorous no-transfer statement, so the mandatory audit stop fires at M8.

## F1-F8

- F1 `NOT_TRIGGERED`
- F2 `NOT_TRIGGERED`
- F3 `NOT_TRIGGERED`
- F4 `TRIGGERED`
- F5 `TRIGGERED`
- F6 `NOT_TRIGGERED`
- F7 `NOT_TRIGGERED`
- F8 `TRIGGERED`

## LT outcomes

- LT-N1 `[PROVED]`
- LT-N2 `[PROVED]`
- LT-N3 `[PROVED]`
- LT-N4 `[PROVED]`
- LT-N5 `[PROVED]`
- LT-N6 `[NOT PROVED / NOT TRIGGERED]`
- LT-N7 `[NOT PROVED / NOT TRIGGERED]`
- LT-CT `[PROVED — AUDIT STOP]`

E6-N2 remains `[OPEN]`.

## Stop-rule compliance

The audit stop fired at M8, after M1-M8 had been adjudicated in the required order. No weighted-operator work, modified geometry, adaptive search, E8 work, rescue mechanism, or mathematical downstream work was executed after the stop. Only packaging, hashing, persistence, and read-back verification are permitted after this point.

Nothing in this task proves the Collatz conjecture.
