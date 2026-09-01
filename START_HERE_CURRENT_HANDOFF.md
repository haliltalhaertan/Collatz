# START HERE — Current Collatz Research Handoff

This is the single entry point for a new LLM, researcher, or recovery session.
Do not infer the active task from filenames, chat history, or the newest-looking
report. The machine-readable authority is `CURRENT_RESEARCH_STATE.json`.

## Recovery sequence

Run these steps in order:

1. Confirm that the repository branch is `main` and fetch `origin/main` without
   discarding local work.
2. Read `CURRENT_RESEARCH_STATE.json` completely.
3. Run:

   ```text
   python tools/verify_handoff.py
   ```

   Do not continue if it does not end with `HANDOFF VERIFICATION: PASS`.
4. Read, in order:
   - `research_manager/RESEARCH_MANAGEMENT_PROTOCOL.md`
   - `research_manager/CONTINUITY_PROTOCOL.md`
   - the active integration decision named in the state file
   - the active task prompt named in the state file
   - the active authorization prompt named in the state file, if non-null
5. If the extracted archive is absent, run:

   ```text
   python tools/extract_current_archive.py
   ```

   This extracts to `_restored_current/` and refuses to overwrite an existing
   recovery tree.
6. Execute only `next_action` from `CURRENT_RESEARCH_STATE.json`.

## Current active state

- Scientific checkpoint: E6-N1 accepted with explicit scope repairs.
- Active task: CP20 Task 8B3 E7.
- Stage: E7 pre-run seal accepted; explicit Stage 1 authorization is pending.
- Target: `(d,C)=(-8,4)`.
- Accepted E6 seal ZIP SHA-256:
  `83a26e81fc8a96479a6b76fdd33f962a047885115f00ec6a892248a0c07b6c57`.
- Returned complete-package SHA-256:
  `9511dc8c9bbd0485f159bbfdf2b5f1f784813af156db5085d90e4faccf1be849`.
- E6 manager decision SHA-256:
  `d3017c56d3b6a5b6540848f29af29a1a7c1d24122991fee779e1d73ed3b28104`.
- Accepted E7 seal ZIP SHA-256:
  `0eb3b2d1487ec1d8dfcf0fc200b1082a8e61b7df2e52f9b6f8f1b943f2ad77f0`.
- Immediate action: obtain explicit external manager authorization quoting
  this exact hash. A generic continue instruction is insufficient. Stage 1 is
  not authorized.

Do not run E7 Stage 1, rerun E6, expand the depth, or begin a different branch
unless the current integrity check fails or the user explicitly changes the
objective.

## Non-negotiable scientific scope

Accepted:

- E4 critical-walk route decision with audited documentary/scope repairs.
- E5-S1 exact finite Green kernel and conditioned-geometric bridge.
- Positive denominator local-limit scale.
- E6-N1 exact coefficient/Hadamard, numerator, and conditioned-bridge forms.
- The M1 endpoint-state coboundary obstruction only in the repaired uniform
  sup-summable scope.

Not accepted:

- E6-N2 through E6-N5.
- E7-B2 through E7-B6.
- A degree-one inherited cone bound.
- A complex local-limit theorem.
- A nonzero boundary-to-target transfer coefficient.
- A fixed-target asymptotic or polynomial lower bound.
- Any claim that Collatz has been proved.

## Mandatory publication cycle

Every accepted seal, result package, audit verdict, repair, route decision, or
material falsification must be recorded before the turn ends:

1. verify artifacts and mathematical scope;
2. append one record to `research_manager/RESEARCH_JOURNAL.jsonl`;
3. update `CURRENT_RESEARCH_STATE.json` and this handoff if the active action
   changed;
4. rebuild `Collatz_Research_Archive_CURRENT.zip`;
5. run `tools/verify_handoff.py`;
6. commit, rebase on `origin/main` without force, and push;
7. report the Git commit and archive SHA-256 to the user.

Conversation memory is never the only copy of an active decision.

Nothing in the current research state proves the Collatz conjecture.
