# Team synchronization handoff — 2026-09-07

Status: synchronized exploratory preservation; not canonical B4 acceptance, not a new seal, and not authorization to execute an old seal.

## Preserved evidence

- Prefix package: GitHub branch `codex/prefix-bridge-20260906-persistence`, remote tip `d544bf2d072dd442c3f6528d87d9f7c4f86c23ce`; immutable ZIP SHA-256 `36d0666ec20be4bb7b1341c33166140620c7e8d952c4fb15314c6863b571943f`; Drive raw-byte comparison PASS at file `1gFNtpNvhrTK1ok8UieVfFWrcqj3baaH-`.
- 2026-09-07 team raw archives: `lead_parallel_20260907_RAW.zip` SHA-256 `e7cff5854e6cda42f216c25ec9fcd70676a8d6877bab013f8899f33732ff0443`; interrupted math ZIP SHA-256 `c1d200539009fe7c87d4ccec86071ab69d3bf9143c0721258039436e78848f03`. Both Drive raw-byte comparisons PASS.
- Team GitHub preservation branch: `codex/team-sync-20260907`; first remote preservation commit `458c5e358d66a087c5f2cf2fa053adb2e04b7a6e`. Later commits add byte-preserving attributes, review closure, manifests and receipts.
- Canonical `main` was corrected through the independently audited two-commit lock protocol. Final remote commit: `2461573739147763eb011faf03c344370a184d69`; it records the real invocation, consumed authorization, pre-mathematics stop, no V3 authority, and a released lock. GitHub load-bearing blob read-back: 12/12 PASS. See `canonical/CANONICAL_STATUS_CORRECTION_GITHUB_READBACK_2026-09-07.md`.

## Artifact classification

- A1: proposed V3 mechanical repair only; unauthorized, unsealed, DO NOT EXECUTE.
- A2: complete finite numerical probe, `[NUM]`; complex values are not exact asymptotics.
- A3: exploratory analytic attack; exact identities require the later independent scope repairs below.
- A4: package audit; historical persistence objections are superseded by the receipts, but mathematical scope remains exploratory.
- A5: editorial review; CP17 submitted PDF is not reproducible from the currently held TeX source, so submission remains source-blocked.
- M1 and M4: interrupted/incomplete. M1 advertised outputs are missing. M4 configured rmax=2000 but ends at r=1200 and lacks required outputs. Preserve; do not cite as completed or silently resume in place.

## Audited mathematical checkpoint

1. The exact four-prefix mixture and logarithmic prefix-excess cutoff remain valid. The cutoff error is at most `4*r^(-1-delta)`; this does not prove `G=O(1/r)`.
2. The endpoint constants `j-5*alpha` and `j-4*alpha-1` are compatible row-phase and pre-increment coordinates.
3. Literal monotonicity of `|H_j|` in `j` is refuted by finite counterexamples. Eventual PWE remains OPEN and finite data do not refute it.
4. Exact barrier splitting `Psi=K+R` and exact domination `|K|<=Q` are valid.
5. The post-package theorem application in `bll_closure/` matches the actual reflected walk to Caravenna--Chaumont, Proposition 4.1, equation (4.5). Its general `(h,c)`-lattice hypothesis includes the moving coset `m*beta+Z`. Consequently `p_m^0(a,b_r)=O(m^(-3/2))` and `|K_m^0(a,b_r)|=O(1/m)` are now PROVED for the two fixed starts and barrier zero.
6. This BLL/KUB result does not cover the full `j`-dependent PWE window and does not control the crossing contribution.
7. Claims excluding every finite-state reduction were overbroad. Only a finite stationary quotient preserving the pointwise multiplier was excluded. Fredholm and usual fixed-endpoint Green-kernel language remain heuristic or require reformulation.
8. The crossing term has now been reduced exactly at its first passage. With `c_s(a)=floor(beta*s-a)+1`, `a'_s=a+c_s(a)-beta*(s-1)`, and the exact seam correction, its numerator is a sum of first-passage fluxes times `q(a'_s)^(-1)L_(m-s+1)(a'_s,b)`. The independently audited formula is recorded in `xub/`.
9. This reduction leaves a genuinely new arithmetic input: a uniform `O(1/ell)` bound for the complex boundary-start bridge ratio on the coupled accessible endpoint array. It is not supplied by the positive killed local-limit theorem and is still OPEN.
10. Pairing the post-crossing increments proves that raw `B=1` blocks are exponentially abundant in the central microcanonical bridge and gives an exact positive hazard in a regular remaining-slope cone. An adversarial audit refutes uniformity over arbitrary endpoints (`K=0` is an exact counterexample) and shows that long `B=1` runs may remain black because the phase is multiplied by `8/9` each time.
11. The repaired sufficient target is only logarithmic white occupation: at least `A log m` regular pair entries with `dist(2^(x_j-beta),Z)>=eta`, except on an `O(1/m)` event, restricted to the actual coupled accessible central arrays and with parity/overshoot seams handled exactly.

## Exactly one next scientific action

Prove or refute the repaired first-passage-conditioned arithmetic estimate on the actual admissible triangular arrays:

`P(W_eta^reg < A log m | endpoint and exact first-passage data) <= C/m`.

Overshoot and odd leftovers must be summed with exact weights or split into a central window and a controlled tail; they are not arbitrary uniform parameters. The proved hazard/supermartingale reduction then yields the needed white-block exponential moment and would imply the target crossing estimate

`|E_a[product_(t=0)^(m-1) q(X_t); tau_0<=m | X_m=b_r]| <= C/m`

The killed half is already `O(1/m)` by BLL/KUB. The exact first-passage representation is proved, but XUB is still a complex/arithmetic cancellation problem, not a positive-probability ballot bound: crossing probability itself may approach one. XUB is sufficient for this split route, not logically necessary for all possible proof routes.

No statement here proves E6-N2, B4, a nonzero profile, a polynomial lower bound, cycles, or the Collatz conjecture.
