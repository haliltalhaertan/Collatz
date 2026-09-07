# Team synchronization handoff — 2026-09-07

Status: synchronized exploratory preservation; not canonical B4 acceptance, not a new seal, and not authorization to execute an old seal.

## Preserved evidence

- Prefix package: GitHub branch `codex/prefix-bridge-20260906-persistence`, remote tip `d544bf2d072dd442c3f6528d87d9f7c4f86c23ce`; immutable ZIP SHA-256 `36d0666ec20be4bb7b1341c33166140620c7e8d952c4fb15314c6863b571943f`; Drive raw-byte comparison PASS at file `1gFNtpNvhrTK1ok8UieVfFWrcqj3baaH-`.
- 2026-09-07 team raw archives: `lead_parallel_20260907_RAW.zip` SHA-256 `e7cff5854e6cda42f216c25ec9fcd70676a8d6877bab013f8899f33732ff0443`; interrupted math ZIP SHA-256 `c1d200539009fe7c87d4ccec86071ab69d3bf9143c0721258039436e78848f03`. Both Drive raw-byte comparisons PASS.
- Team GitHub preservation branch: `codex/team-sync-20260907`; first remote preservation commit `458c5e358d66a087c5f2cf2fa053adb2e04b7a6e`. Later commits add byte-preserving attributes, review closure, manifests and receipts.
- Canonical `origin/main` observed at `1a6f924fd86352c11f57a95b0382adaf92d15bcd`. It is stale: it says B4 V2 is authorized/unexecuted, whereas branch `04a66e41864d1d530ead63b1faeaf122048e3069` records the real invocation, authorization consumed and T1-T8 not executed; audit branch `8fb8d68d3c131d6e11721fd629f1ea879102aedc` says DO NOT EXECUTE.

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
5. The fixed-start killed upper bound `|K|=O(1/m)` is CONDITIONAL on a uniform killed positive local-limit estimate `p_m^0(a,b_r)<=C*m^(-3/2)`. That BLL statement was neither proved nor properly matched to the time-dependent irrational-shift lattice in the feasibility note.
6. Claims excluding every finite-state reduction were overbroad. Only a finite stationary quotient preserving the pointwise multiplier was excluded. Fredholm and usual fixed-endpoint Green-kernel language remain heuristic or require reformulation.

## Exactly one next scientific action

Prove or refute the uniform positive killed bridge/local-limit estimate BLL on the actual admissible triangular array:

`p_m^0(a,b_r) <= C*m^(-3/2)` for the fixed starts `a_G` and `a_H`, barrier zero, and the actual endpoints indexed by `theta_r`.

This must explicitly handle the time-dependent integer boundary induced by states `a-beta*t+Z`. Until BLL is closed, do not call the killed term `O(1/m)`. If BLL passes, the next arithmetic gap is the crossing contribution XUB; XUB is sufficient for the split route, not logically necessary for all possible proofs.

No statement here proves E6-N2, B4, a nonzero profile, a polynomial lower bound, cycles, or the Collatz conjecture.
