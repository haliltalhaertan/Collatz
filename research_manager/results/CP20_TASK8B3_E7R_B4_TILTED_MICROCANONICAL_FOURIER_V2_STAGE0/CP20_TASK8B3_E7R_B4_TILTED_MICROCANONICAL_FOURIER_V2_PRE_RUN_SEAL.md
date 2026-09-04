# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — V2 PRE-RUN SEAL — AUTHORIZATION-BASE SELF-REFERENCE REPAIR

Status: **STAGE 0 REPAIR FROZEN — AWAITING MANAGER AUTHORIZATION**

Canonical historical Stage-0 source SHA: `8d274095b0e1acbe1fad0a73ef6a5293364902fc`
Literal handoff gate: **HANDOFF VERIFICATION: PASS**
Handoff run/job: `33912148126` / `101150791299`
Handoff evidence SHA-256: `93168be2f5ba453387bd7ed42180ce026e4e8da9195373f326b160bf8bb3400c`
Scientific diff verdict: **NO SCIENTIFIC CHANGE**

Authorization semantics: **TWO-COMMIT PHASE A / PHASE B**.
- `canonical_stage0_base_sha` is the future Phase-A canonical Stage-0 commit.
- `authorization_commit_sha` is the later Phase-B authorization/state commit.
- `canonical_base_sha = authorization_commit_sha` in the run witness.
- The Phase-B authorization JSON is NOT required to contain its own commit SHA.

Blocked seals — DO NOT AUTHORIZE:
- V1 consumed seal `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`
- V2 blocked candidate `2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea`
- V2 self-reference-defective candidate `66ac975940abb29a1248079ea6e03643ded966da296cf33deb7c7a0f5fa60eac`

Witness self-test: **SELFTEST PASS** — S1–S11 FAIL as expected; S12 PASS.
Static control-flow check: **PASS**.
Scientific diff: **NO SCIENTIFIC CHANGE**.
Stage 1: **NOT EXECUTED**.
T1–T8: **NOT EXECUTED**.
Stage-1 authorization: **NOT GRANTED** by this repair.

Contract SHA-256: `26dd63e143c9d7a1178b0a99acdeda0f3b9839208c7e2df066706a17f959de9f`
Config SHA-256: `6007a994b04ab1768d8164bdbbc44acdf94a076c1f07ab3d2ea67c0934cfbe67`
Launcher SHA-256: `16cadd29fc6bae7f3255a596267ede57faa30f469b7b70cffb1042f68115f6cc`
Witness schema SHA-256: `c6e12499f3de2acb7fa34be81a4b54d5d0424abb351ca2fcbbc3ab7808447f01`
PRE_T1 schema SHA-256: `b6d7fe7602c291690d82d2bcde292403712003be1433878b247b22f1b24b55e2`
Validator SHA-256: `efeadaa9f838e5b4dd03bec0603b94763709e7101ac83481456dfce7ece8d362`

The ZIP SHA-256 is recorded outside this member after deterministic construction to avoid self-reference. Any future authorization must bind the final fresh seal SHA, this exact contract SHA, and the future Phase-A `canonical_stage0_base_sha`; the computation then receives the later Phase-B `authorization_commit_sha` after that commit exists.

Nothing in this integrity repair proves the Collatz conjecture.
