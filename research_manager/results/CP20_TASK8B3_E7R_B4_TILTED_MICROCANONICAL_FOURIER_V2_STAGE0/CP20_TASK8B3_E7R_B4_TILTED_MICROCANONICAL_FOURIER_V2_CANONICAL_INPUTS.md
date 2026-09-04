# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — CANONICAL INPUTS

Canonical repository: `haliltalhaertan/Collatz`
Stage-0 source base SHA: `8d274095b0e1acbe1fad0a73ef6a5293364902fc`
Canonical V1 Stage-0 scientific-source commit: `c83d22f9e3ac8bdc4ec955d14b3d7dca11c3fee1`
Working branch: `cp20-e7r-b4-tilted-microcanonical-fourier-v2-stage0-reseal-20260904`

Canonical closeout status:
- V1 old seal `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`: **[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]**
- V1 Stage 1: **[INPUT INTEGRITY FAILURE — INVALID / NON-CANONICAL]**
- B4-N1…B4-N7: NOT ESTABLISHED
- B4-CT: NOT ESTABLISHED
- E6-N2: **[OPEN]**

The sole known repair target is the mechanical witness/launcher integrity defect. No invalid V1 Stage-1 mathematics is imported.

## Base-SHA semantics
`stage0_source_base_sha` is permanently `8d274095b0e1acbe1fad0a73ef6a5293364902fc` for this reseal.

`authorized_execution_base_sha` is deliberately NOT frozen now. It is a future manager-supplied canonical commit/ref that must already contain canonicalized V2 Stage-0 artifacts, the canonicalized V2 execution contract, and the manager's Stage-1 authorization binding the exact V2 seal and contract.

For every future RUN_WITNESS:
`canonical_base_sha = authorized_execution_base_sha`.

The older Stage-0 source base must never be substituted for the future authorization base.
