# Collatz Research Continuity Protocol

## Purpose

The project must remain recoverable when the active LLM, desktop session,
machine, or conversation context disappears. No active state may exist only in
chat memory.

## Authorities

In descending order:

1. byte-verified sealed inputs and independent audit packages;
2. `CURRENT_RESEARCH_STATE.json` for the active task and next action;
3. manager integration/authorization decisions;
4. `RESEARCH_JOURNAL.jsonl` for chronological transitions;
5. `START_HERE_CURRENT_HANDOFF.md` for human-readable recovery;
6. chat summaries and recollection.

If two sources disagree, stop and repair the higher-level handoff files from
the verified artifacts. Do not guess.

## Atomic milestone transaction

Every meaningful state transition is one transaction:

1. **Intake:** locate the exact returned files and preserve their paths.
2. **Integrity:** verify ZIP hashes, manifests, package membership, and sealed
   source hashes.
3. **Reproduction:** rerun the deterministic verifier read-only and reproduce
   at least one independent checkpoint when appropriate.
4. **Scope:** classify exact, proved, certified numerical, numerical, open,
   failed, and parked statements.
5. **Decision:** write a manager decision naming exactly one next action.
6. **Journal:** append one JSON line; never rewrite earlier journal lines.
7. **State:** update `CURRENT_RESEARCH_STATE.json` so it names the new active
   prompt, decision, seal, status, and next action.
8. **Handoff:** update `START_HERE_CURRENT_HANDOFF.md` when the active task or
   stage changes.
9. **Package:** rebuild the deterministic current archive.
10. **Verify:** run `tools/verify_handoff.py` and require a pass.
11. **Publish:** fetch, preserve remote work, commit, rebase without force,
    push `main`, and confirm local HEAD equals `origin/main`.
12. **Report:** give the user the commit, current-archive SHA-256, active stage,
    and exact next action.

A turn is not operationally complete until steps 6–12 are done, unless an
integrity failure or user stop prevents publication.

## Journal hash chain

`RESEARCH_JOURNAL.jsonl` is append-only UTF-8/LF JSONL.

- `sequence` increases by one.
- `previous_entry_sha256` is the SHA-256 of the previous line's exact UTF-8
  bytes, excluding its newline.
- The first entry uses `null`.
- A correction is a new event; old entries are never edited.

## Active computation rules

- Record `AUTHORIZED_NOT_EXECUTED`, `RUNNING`, `RESULT_RETURNED_UNVERIFIED`,
  `ACCEPTED`, or `AUDIT_PENDING` explicitly.
- Record exact seal and authorization hashes.
- A new LLM must not create a replacement seal when an accepted seal already
  exists.
- Returned results are not accepted until manager intake completes.
- Audit stop rules override the temptation to continue downstream.

## GitHub continuity rules

- The root handoff, state, journal, manager documents, audit outputs, tooling,
  and deterministic current archive are committed.
- Temporary verification trees and duplicated isolated audit inputs remain
  ignored after their unique evidence is packaged.
- Never force-push research history.
- Preserve unrelated remote commits through fetch/rebase or a non-destructive
  merge.
- If the current archive reaches GitHub's hard single-file limit, split it into
  hash-manifested volumes or migrate the archive artifact to Git LFS before the
  next milestone; never silently omit data.

## Recovery success criterion

A fresh clone with no chat history is sufficient when a new agent can:

1. run `tools/verify_handoff.py` successfully;
2. identify the accepted scientific checkpoint;
3. identify prohibited claims;
4. locate and verify the active seal and prompt;
5. state the one next action without asking the previous agent;
6. restore the complete archive with `tools/extract_current_archive.py`.
