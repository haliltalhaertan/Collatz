# CP20 Task 8B3 — Literature Transfer V1 Stage 0 Acceptance

## Verdict

**[ACCEPT STAGE 0]**

This is a canonical management/intake decision only. No Stage 1 derivation, proof task, weighted-operator work, or E8 work is executed by this decision.

## Canonical intake

- Canonical base: `b3eaaae80a64003f4ee06a43b65fbd3680b8e22b`
- Working branch: `cp20-e7r-literature-transfer-v1-stage0-20260904`
- Accepted Stage-0 working-branch commit: `8ff843722bc9a4901fe72a1594d0fca95ca358b7`
- Accepted normalized Stage-0 seal ZIP SHA-256: `403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79`
- Stage-0 manifest SHA-256: `f486d82365ca77066b328660bf48cd891eacb8aeed7a439d8bfc67b87d5b9276`
- Stage-0 verdict: `[LITERATURE TRANSFER V1 — STAGE 0 FROZEN]`
- Sealed members: `18`
- Manifest verification: `PASS`
- ZIP CRC: `PASS`
- Stage 1 executed: `false`
- M1–M8 adjudicated: `false`
- Stage-0 Drive read-back: `PASS`
- Stage-0 GitHub branch read-back: `PASS`

The Stage-0 sealed artifacts are accepted byte-for-byte and remain immutable.

## Frozen literature

### Tao
- arXiv: `1909.03562v7`
- PDF SHA-256: `62cf49d4d8e8e681c7a4738ebaf56f3dbb7b67de95f37ccbac6e428ef3fc394e`
- source archive SHA-256: `ba81acd6254838251f1ee585256a6f9f223cdc9c73bed0a3c4fd25782d0124ad`

### Si
- Zenodo DOI: `10.5281/zenodo.20027097`
- PDF SHA-256: `0dfad7f22df91c14c36182d7557aee537a462ef0a2a548422c366d21e2bd06c8`
- GitHub commit: `119199e7165505f9535952e272056af912ce59fb`
- `main.tex` SHA-256: `c1ff1f11f442fed1b2f7a37be61fe0e3c0916719549018557446ca01e81e0811`

No unsealed source revision is admitted.

## Binding manager repair for Stage 1

The sealed file `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_EXACT_SYMBOLIC_CHECKS.py` is preserved unchanged for provenance, but its function `candidate_m3_project_exponent()` is **not** accepted as an exact implementation of the project finite phase and its output is **not mathematical evidence for M3**.

For negative exponent rows, any exact M3 computation must implement independently the frozen modular-inverse + dyadic correction / unified-modulus representation in `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_PROJECT_DEFINITIONS.md`, and that independent implementation must be separately hashed.

## Scope

Stage 0 freezes sources, definitions, candidate maps, falsification tests, and permitted exact-comparison discipline only. M1–M8 remain unadjudicated at this checkpoint.

Nothing in this acceptance proves the Collatz conjecture.
