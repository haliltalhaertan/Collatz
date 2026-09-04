# CURRENT HANDOFF — B4 V2

Canonical task: `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2`
Active stage: `STAGE_1_AUTHORIZED_NOT_EXECUTED`

Phase A / canonical_stage0_base_sha: `34ac0dbeb8c0ae2fddab706680f1682412b00786` — read-back PASS.
Phase B / authorization_commit_sha: `f8d778a2113922e3bbb14c86ee2fa5359cee28ea` — read-back PASS.
Authorized seal SHA-256: `11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e`
Contract SHA-256: `7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403`
Manifest SHA-256: `7f48807db5733c85759324d4f94e357aa6941de0ecd911b4180f5bc2101d6dcb`
Scientific diff: `NO SCIENTIFIC CHANGE`
Drive Stage-0 seal folder/file: `1SFvk3A5fSzB4adPFIMxudgMdbooXVi3q` / `1hWN1mdJdx78jnsOlD2ZXF8htkf9e8QGL` — raw read-back PASS.

Stage 1: `NOT EXECUTED`.
T1-T8: `NOT EXECUTED`.
B4-N1...B4-N7: `NOT ESTABLISHED`.
B4-CT: `NOT ESTABLISHED`.
E6-N2: `[OPEN]`.

Blocked seals — NEVER AUTHORIZE:
- `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`
- `2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea`
- `66ac975940abb29a1248079ea6e03643ded966da296cf33deb7c7a0f5fa60eac`
- `06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f`

Authorization JSON binds exactly the seal, contract, Phase-A SHA and `STAGE_1_AUTHORIZED_NOT_EXECUTED`; it does not self-reference Phase B.

Exact next action:
Execute CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 Stage 1 exactly once in a fresh session that has not seen invalid V1 T1-T8 drafts, using canonical_stage0_base_sha=34ac0dbeb8c0ae2fddab706680f1682412b00786, authorization_commit_sha=f8d778a2113922e3bbb14c86ee2fa5359cee28ea, seal=11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e, contract=7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403.

Invalid V1 T1-T8 drafts remain INVALID/NON-CANONICAL/DO NOT USE.
Nothing in this authorization proves the Collatz conjecture.
