# START HERE — Current Collatz Research Handoff

This is the single recovery entry point. `CURRENT_RESEARCH_STATE.json` is the machine-readable authority for the active task, stage, accepted hashes, prohibitions, and exact next action.

## Recovery sequence

1. Confirm branch `main` and fetch `origin/main` without discarding local work.
2. Read `CURRENT_RESEARCH_STATE.json` completely.
3. Run `python tools/verify_handoff.py` and require `HANDOFF VERIFICATION: PASS`.
4. Read:
   - `research_manager/RESEARCH_MANAGEMENT_PROTOCOL.md`
   - `research_manager/CONTINUITY_PROTOCOL.md`
   - `research_manager/decisions/CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE0_ACCEPTANCE_2026-09-04.md`
   - `research_manager/decisions/CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_AUTHORIZATION_2026-09-04.md`
   - `research_manager/prompts/CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_MANAGER_AUTHORIZATION_PROMPT_2026-09-04.md`
5. Execute only `next_action` from `CURRENT_RESEARCH_STATE.json`.

## Current accepted scientific checkpoint

- `E6-N1 [PROVED][AUDITED/ACCEPTED WITH SCOPE REPAIR]`
- `E7R-B1 [PROVED][AUDITED]`
- `E7R-B2 [PROVED][AUDITED]`
- `E7R-B3 frozen pointwise contraction [FALSE][CLOSED]`
- `B3-CT [PROVED][AUDITED]`
- `E7R-B4 / E6-N2 [OPEN]`
- `E7R-B5 [OPEN]`
- `E7R-B6 [OPEN]`
- `|E[F_{r,4}|S_r=n_r]|=O(1/r) [OPEN]`

Historical/lost pre-recovery E7 conclusions remain `[UNVERIFIED — ARTIFACTS LOST]`.

Nothing here proves the Collatz conjecture.

## Literature Transfer V1 — frozen Stage 0

Canonical task: `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1`

Stage-0 verdict: `[LITERATURE TRANSFER V1 — STAGE 0 FROZEN]`

Accepted normalized Stage-0 seal ZIP SHA-256:

`403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79`

Stage-0 manifest SHA-256:

`f486d82365ca77066b328660bf48cd891eacb8aeed7a439d8bfc67b87d5b9276`

Accepted working-branch commit:

`8ff843722bc9a4901fe72a1594d0fca95ca358b7`

Integrity at acceptance:
- manifest verification `PASS`
- ZIP CRC `PASS`
- 18 sealed members
- Stage 1 not executed
- M1–M8 not adjudicated
- Drive read-back `PASS`
- GitHub branch read-back `PASS`

Frozen literature:
- Tao arXiv `1909.03562v7`; PDF `62cf49d4d8e8e681c7a4738ebaf56f3dbb7b67de95f37ccbac6e428ef3fc394e`; source archive `ba81acd6254838251f1ee585256a6f9f223cdc9c73bed0a3c4fd25782d0124ad`
- Si Zenodo DOI `10.5281/zenodo.20027097`; PDF `0dfad7f22df91c14c36182d7557aee537a462ef0a2a548422c366d21e2bd06c8`; GitHub commit `119199e7165505f9535952e272056af912ce59fb`; `main.tex` `c1ff1f11f442fed1b2f7a37be61fe0e3c0916719549018557446ca01e81e0811`

No unsealed source revision may be substituted.

## Canonical stage

`STAGE_1_AUTHORIZED_NOT_EXECUTED`

Stage 1 is authorized **only** under seal `403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79` and has not been executed by the authorization transaction.

Required M1–M8 order:
M1 microcanonical composition → M2 Bernoulli bridge → M3 affine-offset/Fourier character → M4 C=4 frequency/depth → M5 degree-one correction → M6 entropy line → M7 B3-CT/resonance → M8 Tao white-point/renewal applicability.

### Binding M3 manager repair

The frozen helper `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_EXACT_SYMBOLIC_CHECKS.py` remains unchanged for provenance, but `candidate_m3_project_exponent()` is not accepted as exact project-phase evidence. Negative exponent rows require an independent implementation of the modular-inverse + dyadic-correction / unified-modulus representation frozen in `PROJECT_DEFINITIONS.md`, with a separate hash.

## Stage-1 evidence and stop discipline

- Tao theorem statements may be treated as known literature.
- Si theorem statements remain `[LITERATURE CLAIM — UNAUDITED]`.
- No Si theorem becomes a project dependency without independent proof or separate zero-trust audit.
- Exact law equality is not interchangeable with asymptotic equivalence.
- No analogy-only mapping is accepted.

Stop immediately for independent audit on LT-N6, LT-N7, or LT-CT as defined in the Stage-1 authorization decision. If no stop fires, LT-N1–LT-N5 may be completed in the same run. `[NO DIRECT MATCH]` and F1–F8 falsifications are permitted outcomes.

No weighted-operator work, modified geometry, adaptive frequency/endpoint rescue, new literature-source search, or E8 is authorized by this handoff.

## Exact next action

> Execute Stage 1 once under seal `403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79`, adjudicating M1–M8 in order and obeying the binding M3 repair and the LT-N6/LT-N7/LT-CT audit stop rule. Do not begin weighted-operator work or E8.

## Mandatory persistence cycle

Every completed computation, audit, or manager milestone closes with:

`result → hashes/manifests → Drive save → Drive read-back → GitHub save/push → GitHub read-back → report`

Nothing in the current research state proves the Collatz conjecture.
