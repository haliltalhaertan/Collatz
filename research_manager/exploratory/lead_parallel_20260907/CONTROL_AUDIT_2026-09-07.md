# Control audit — every control against the failure it prevents

Status: **WORKING ARTIFACT / PROPOSAL.** No protocol file was modified. No integrator lock was
held or claimed. No commit, no push. This is the manager's recommendation for the user to accept,
reject, or amend.

## The test applied to each control

For every control in `RESEARCH_MANAGEMENT_PROTOCOL.md`, `CONTINUITY_PROTOCOL.md`,
`GITHUB_SYNC_POLICY.md`, the B4 V2 sealed execution contract and `tools/verify_handoff.py`,
four questions:

1. **Which failure does it prevent?** Name it, not a category.
2. **Did that failure actually occur in this project?** Evidence from the record, or "never".
3. **Would the control have caught it?** Not "is it satisfied" — would it fire on the real case.
4. **Does it fire on cases carrying no risk?**

A control that cannot answer 1 is deleted. A control that answers 1 but fails 3 or 4 is retargeted
rather than deleted, because the failure is real and something must cover it.

## Failures this project has actually suffered

| id | Failure | Evidence |
|---|---|---|
| F1 | Artifacts lost | `pre-recovery E7 conclusions [UNVERIFIED — ARTIFACTS LOST]`, still in the checkpoint |
| F2 | A producer's own checker was wrong and its verdict would have been believed | V1 prefix checker used denominator `16*3^(r-3)`; caught only by an independent rebuild |
| F3 | A session sees an invalid draft and cannot unsee it | invalid V1 T1–T8 drafts, quarantined |
| F4 | Overclaiming; numerics promoted, wording broader than the proof | recurring "ACCEPTED WITH SCOPE REPAIR" verdicts |
| F5 | Stale-base or concurrent canonical writes | the reason `active_integrator` exists |
| F6 | History rewritten or force-pushed | never occurred; the rule is prophylactic |
| F7 | An artifact recorded as verified that does not do its job | **three instances found 2026-09-07**: B4 config froze a file against a commit where it cannot match; prefix README asserts a branch and receipts that do not exist; CP17 source does not produce the submitted PDF |
| F8 | Our own defect burns a once-only authorization | **twice**, V1 2026-09-04 and V2 2026-09-05, zero mathematics either time |

F7 and F8 are the two the current protocol does not cover. Everything below turns on them.

## Verdicts

### KEEP — real failure, control catches it, no misfire

| Control | Prevents | Note |
|---|---|---|
| Independent reproduction standard (no producer imports, rebuilt from definitions, own hashes, edge + central case) | F2 | **The single most valuable control in the protocol.** It caught the V1 denominator bug, and on 2026-09-07 it caught a wrong premise in my own task prompt. Do not touch it. |
| Evidence classification labels | F4 | Cheap, works, used constantly |
| Result intake gate, step 4 (adversarial interpretation) | F2, F4 | This is what found the prefix-bridge circularity |
| Audit-and-freeze gate on load-bearing results | F2, F4 | Works |
| Journal hash chain, append-only, corrections as new entries | F1 | Verified intact 20/20 today, including across a schema change. Cheap, cannot misfire |
| Never force-push; preserve unrelated remote commits | F6 | Cheap, prophylactic, keep |
| Continuity requirement and the recovery success criterion | F1 | This is the memory prosthesis for sessions that cannot remember. The real justification for most of the paperwork |
| Role separation; a new session must not replace an accepted seal | F3 | Cheap |
| Scientific firewall (a mechanics repair may not change the mathematics) | F4 | Worked: the V3 patch proved no scientific change three independent ways |

### RETARGET — real failure, but the control is attached to the wrong event

**One-run discipline.** Prevents F3, retrying until a pleasing answer appears. But it is attached
to *entrypoint invocation*, not to *mathematical execution*. A crash before T1 has read no
mathematics and produced none, so it carries zero contamination risk — yet it consumes the
authorization. This is F8, and it cost the project two authorizations and four days.
**Fix:** consume the authorization when `T1 START` is appended to the ledger, not when the process
starts. The contract already defines `PRE_T1_GATE PASS` as exactly this boundary and the ledger
already records it, so no new mechanism is needed. A pre-T1 failure attributable to the sealed
contract itself becomes recoverable; any failure attributable to input tampering stays terminal,
and the existing ledger distinguishes them. **This is the one item that needs the user's decision,
because it is a contract change, not a code change.**

**Frozen-dependency check at Phase A.** Prevents silent dependency drift. But it froze a governance
file that the authorization process is required to rewrite — a contradiction compiled into the
config. **Fix:** the two-tier semantics already designed and dry-run in lane A1: scientific inputs
bound at seal time, governance files bound at Phase A, via a declared list rather than a hard-coded
exception. The declared-list form also closes the same latent defect sitting in
`START_HERE_CURRENT_HANDOFF.md`.

**Repository and archive hash checks in `verify_handoff.py`.** Prevent F1. But they verify each
artifact against its own recorded hash, never against what the artifact is for. They passed
continuously while all three F7 instances accumulated. **Fix:** every artifact whose hash is
recorded must also record the question that hash answers, and the transaction must answer it. For
CP17 the question was "does this source compile to the submitted PDF"; nobody asked, so nobody
noticed the source was gone. That is a build check, not a hash check.

**Dual-persistence read-back.** Prevents F1, a genuine need. But it compares bytes, and it is
demanded unconditionally on every milestone including working notes. **Fix:** make the read-back
leg assert the recovery criterion that already exists in the continuity protocol — a fresh clone
can identify the checkpoint, the next action and the prohibited claims — instead of asserting byte
equality alone. The recovery criterion is written down and has, as far as the record shows, never
been executed as part of a transaction.

### DELETE or MERGE — protects another control, or has never fired on a real risk

**Blocked-seal firewall.** Four seals permanently blacklisted. Reading the contract's own reasons:
one consumed, one unstated, one for an "authorization-base self-reference defect", one for a
"canonical-state-path mismatch". The V2 seal is now a fifth. **Every one was blocked because of a
defect in our own configuration or process. Not one was blocked because of tampering.** The list
exists only because the one-run discipline makes a burned seal permanent. Fix that discipline and
this list is a scar registry, not a control. Retain it as history; stop treating it as a firewall.

**Two-commit Phase A / Phase B authorization semantics.** Exists to stop an authorization record
from having to reference the commit that contains it. That chicken-and-egg exists only because the
authorization must live inside the same repository whose hashes it binds. It is machinery
protecting machinery, and it is the most expensive control in the protocol per unit of risk
covered. An authorization record naming the seal, the contract and the scope does the same work
without needing a commit-ancestry ritual.

**Witness semantics, fourteen mandatory fields.** Exists to prove the run happened as declared. But
the witness is checked by a validator that the launcher loads from the working tree and executes
with no hash verification, although the seal carries its SHA-256 (launcher lines 120-121). A
fourteen-field apparatus behind an unlocked door. Either verify the validator or keep three fields.

**Authoritative-canonical-state-path clause,** with its no-silent-fallback rule and legacy-alias
consistency requirements. This clause exists because an earlier seal candidate had a
canonical-state-path mismatch — it is a control written to prevent the recurrence of a bug in a
previous control. It survives only as long as the JSON schema stays unstable.

**Three overlapping specifications of one process.** The milestone chain is written three times: a
six-step milestone rule in the sync policy, a fourteen-step atomic transaction in the continuity
protocol, and a seven-link completion chain repeated in both other documents. Merge to one.

**The branch check in `verify_handoff.py`.** It asserts the current branch is `main` and raises
otherwise. It failed today for no reason but that I was standing on a working branch, which is a
normal and riskless state. It prevents no failure; it prevents *running the verifier* anywhere but
`main`. Make it a printed warning.

**Deterministic 91 MB archive rebuilt on every transaction.** Guarantees recoverability that git
already provides for everything except the one imported original. Rebuild at checkpoints, not at
every state transition.

### Untested

The dissent record has never been used: twenty-one journal entries, no `CO_CHAIR_DISSENT` among
them. It is cheap and covers a real risk, so keep it, but it is unexercised and should not be
counted as working. Related: the rule that a co-chair who authorized a run must not be its sole
judge deserves a check against the B4 sequence, where the same automated integrator both created
the authorization and wrote the records that confirmed it.

## What the audit shows structurally

Nine controls earn their place. Four are aimed at real failures but attached to the wrong event.
Seven exist mainly to protect other controls. The heaviest machinery in the project clusters
entirely in that third group, and every one of the five blocked seals was produced by it rather
than caught by it.

The common defect in the retarget and delete groups is uniform: each control was specified in terms
of **artifacts** — this file, this hash, this commit, this field — rather than in terms of the
**failure** it prevents. A control written that way can be perfectly satisfied while the failure it
was meant to stop walks past, and it will also fire on cases that carry no risk at all. Both
happened here, in the same week.

## Recommended sequence

1. Decide the one-run discipline question. It is a contract decision and it is yours. Nothing else
   should be built until it is settled, because a third authorization under the present rule is
   likely to burn the same way.
2. Apply the two-tier frozen-dependency semantics; the patches and a passing two-directional dry
   run already exist.
3. Add the "what question does this hash answer" requirement, and run the recovery criterion as
   part of the read-back leg.
4. Merge the three milestone specifications into one, and demote the branch assertion to a warning.
5. Leave the nine KEEP controls untouched. In particular the independent reproduction standard is
   what has been catching real errors, including mine.

Nothing in this audit changes any scientific claim. E6-N2 remains `[OPEN]`, and nothing here
proves the Collatz conjecture.
