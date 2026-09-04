# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1 — STAGE 1 EXECUTION INTEGRITY AND OUTPUT CONTRACT

This contract is part of the Stage-0 seal and MUST be canonicalized before any Stage-1 authorization/execution.

## A. Authorization binding

Stage 1 may start only when a manager authorization explicitly quotes the SHA-256 of the exact sealed file
`CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SEAL.zip`.

Authorization applies to that hash only. Any byte change to any sealed member, CONFIG, target, arcs, falsification tests, source, or contract voids authorization.

## B. Required pre-execution checks

Before the first Stage-1 mathematical action, the authorized session MUST:

1. recompute the seal ZIP SHA-256 and compare it to the manager-authorized value;
2. verify `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SHA256SUMS.txt` byte-for-byte;
3. verify every manifested member SHA-256;
4. require ZIP member names unique and sorted, CRC PASS, and exact member count recorded by Stage 0;
5. verify canonical base/dependencies:
   - canonical base `57f670bd531cee8f0f2d6eeb27431243f6e3a479`;
   - CURRENT_RESEARCH_STATE Git blob `5cc2b1ef867017d5aacdd3a3444c012bd2834826`;
   - START_HERE Git blob `87fc5e8c192084ef2bd2f542cbc6e64f22a9bde0`;
   - audited LT integration decision Git blob `60938ad437906bdd4e74a3a4c95c19f632e9fb6f`;
   - LT Stage-1 report Git blob `fae822efd444ad2616fdd004ecadd5b70fe67e1a`;
   - LT zero-trust audit Git blob `caa91d58269a7b98838e6a70ca6a8e5d0bfb6c46`;
6. prove that none of the declared Stage-1 outputs already exists in the fresh execution directory;
7. create exactly one append-only run witness before T1:
   `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RUN_WITNESS.json`;
8. record a UTC timestamp, authorized seal SHA-256, canonical base SHA, process/session identifier, and output-absence verdict in that witness.

On any failure: write `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and STOP without repair/rerun under the same authorization.

## C. Exact execution entrypoint

The exact sealed execution entrypoint is:

`python CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1.py --config CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_CONFIG.json --seal CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SEAL.zip --authorized-seal-sha256 <MANAGER_AUTHORIZED_SHA256> --output CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RESULTS.json`

The sealed Stage-1 launcher is an integrity/ledger orchestrator. It does not itself certify asymptotic mathematics. The authorized proof session must adjudicate T1→T8 in order and append each stage result to the ledger.

## D. One-run discipline

- The entrypoint may be invoked once only.
- Do not modify or rerun after observing output.
- A verifier failure does not authorize repair/rerun.
- Any necessary source change requires a new Stage-0 seal and fresh manager authorization.

## E. Append-only T/M-stage ledger

Create:
`CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_LEDGER.jsonl`.

Before beginning each T-stage append `START`.
After adjudication append exactly one terminal record: `PROVED`, `FAIL`, `OPEN`, `COUNTERTHEOREM`, or `AUDIT_STOP`.
Ledger entries include UTC timestamp and hashes of all evidence artifacts used for that stage.
History must never be rewritten.

## F. Stop-rule enforcement

Immediate independent-audit stop occurs at:
- B4-N5 if genuinely load-bearing;
- B4-N6;
- B4-N7/E6-N2;
- load-bearing B4-CT;
- exact leading-coefficient cancellation/non-cancellation theorem on which downstream proof depends.

When stop fires:
1. append `AUDIT_STOP`;
2. mark every later T-stage `NOT_EXECUTED`;
3. perform no fallback/rescue mathematics;
4. package only result/provenance/persistence artifacts.

The final package MUST contain evidence that downstream post-stop stages were `NOT_EXECUTED`.

## G. Evidence discipline

- Tilting itself is not cancellation.
- Centrality under `p_*` is not Si-theorem applicability.
- Tao Geom(2) results do not automatically transfer to Geom(p_*).
- No qualitative `o(1)` or unspecified polynomial decay may be promoted to `O(1/r)`.
- Moving primitive frequency `eta_r` uniformity is load-bearing.
- No global mod-16 cancellation may be invented.
- B3-CT is a standing falsification constraint.
- T8-A/T8-B are forbidden until direct T7 route adjudication permits them.

## H. Required final integrity/persistence

Before Stage 1 is called operationally complete:
1. create final result files and complete package;
2. compute SHA-256 manifest and package SHA;
3. verify package membership, uniqueness, CRC and manifested hashes;
4. save the complete package to Google Drive;
5. raw Drive read-back and byte/hash verification;
6. persist result records/artifacts to a GitHub result branch;
7. push without force;
8. GitHub read-back of all result records;
9. report exact commit SHA, Drive location, package SHA and manifest SHA.

If Drive or GitHub persistence fails, report failure and do not call Stage 1 operationally complete.
