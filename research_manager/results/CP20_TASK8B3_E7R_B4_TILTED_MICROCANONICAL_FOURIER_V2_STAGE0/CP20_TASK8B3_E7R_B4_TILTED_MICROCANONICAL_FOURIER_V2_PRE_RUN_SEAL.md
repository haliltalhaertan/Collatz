# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — V2 PRE-RUN SEAL — CANONICAL STATE PATH REPAIR

Status: **STAGE 0 REPAIR FROZEN — AWAITING MANAGER AUTHORIZATION**

Canonical historical Stage-0 source SHA: `8d274095b0e1acbe1fad0a73ef6a5293364902fc`
Literal handoff gate: **HANDOFF VERIFICATION: PASS**
Handoff run/job: `33917015405` / `101166400966`
Scientific diff verdict: **NO SCIENTIFIC CHANGE**

Authoritative Phase-B state path: `CURRENT_RESEARCH_STATE.json["active_task"]["stage"]`.
Required value: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.
No top-level `active_stage` field is required. Optional aliases are consistency checks only; conflicts FAIL before T1.

Authorization semantics: **TWO-COMMIT PHASE A / PHASE B**.
- `canonical_stage0_base_sha` is the future Phase-A canonical Stage-0 commit.
- `authorization_commit_sha` is the later Phase-B authorization/state commit.
- `canonical_base_sha = authorization_commit_sha` in the run witness.
- The Phase-B authorization JSON is NOT required to contain its own commit SHA.

Blocked seals — DO NOT AUTHORIZE:
- V1 consumed seal `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`
- V2 blocked candidate `2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea`
- V2 self-reference-defective candidate `66ac975940abb29a1248079ea6e03643ded966da296cf33deb7c7a0f5fa60eac`
- V2 canonical-state-path-defective candidate `06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f`

Witness/two-commit tests: **SELFTEST PASS** — S1–S11 FAIL as expected; S12 PASS.
Canonical state-path tests: **P1 PASS; P2 FAIL; P3 FAIL; P4 FAIL; P5 FAIL; P6 PASS**, all as expected.
Static control-flow check: **PASS**.
Scientific diff: **NO SCIENTIFIC CHANGE**.
Stage 1: **NOT EXECUTED**.
T1–T8: **NOT EXECUTED**.
Stage-1 authorization: **NOT GRANTED** by this repair.

Contract SHA-256: `7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403`
Config SHA-256: `2fbc7bd09ab2cae89095b537342cf63c85f53f821d4ddf21c7860a2ec53b1f4b`
Launcher SHA-256: `9222d0e0a8079e3560bc880520dd5ead44869f5fd4fa541520e225c841b8a732`
Witness schema SHA-256: `c6e12499f3de2acb7fa34be81a4b54d5d0424abb351ca2fcbbc3ab7808447f01`
PRE_T1 schema SHA-256: `b6d7fe7602c291690d82d2bcde292403712003be1433878b247b22f1b24b55e2`
Validator SHA-256: `59c7c81511602469387160cdd5e737eb862b40fb91950ed599147ad2aa699bdd`
Self-test results SHA-256: `10132ba0a0e52a2ebee658174076824362ffe53f243cb1a44499df6f00477433`
Static-control results SHA-256: `e52c52e572c1382d581278988f3917ee200472bdcb5efab5079bd56e5860aaaf`
Scientific-diff report SHA-256: `f4e2d05554976f898d6fbc943cf79e330d8869007f7ae83bac8858dd15c864a2`

The ZIP SHA-256 and manifest SHA-256 are recorded outside this member after deterministic construction to avoid self-reference.

Nothing in this integrity repair proves the Collatz conjecture.
