# Collatz Research Management Protocol

## Session roles

### Research-manager session

This session owns research direction. It must:

- preserve the frozen dependency spine and branch-closure decisions;
- select one falsifiable, high-information target at a time;
- write the computation/proof prompt;
- independently inspect returned code, data, hashes, theorem statements, and failure reports;
- distinguish `[EXACT]`, `[PROVED]`, `[CERTIFIED NUM]`, `[NUM]`, `[LEAD]`, `[OPEN]`, `[FAIL]`, `[FALSE]`, `[CLOSED]`, and `[PARK]`;
- decide whether to continue, repair, audit, freeze, park, close, or change branch;
- explain the result to the user without implying that Collatz is solved.

### Computation/proof session

The computation session executes only the authorized prompt. It must not:

- redefine the project objective;
- silently use unfrozen results as dependencies;
- promote numerics to theorems;
- begin downstream work after a load-bearing theorem or countertheorem appears;
- overwrite frozen artifacts.

## Co-chair and head-researcher governance

Research-manager co-chairs and additional head-researcher sessions may coexist. Historical named role assignments remain authoritative for their recorded milestones. Additional sessions do not automatically become co-chairs, signatories, reviewers of record, or holders of any historical assignment.

Where a milestone has two named co-chairs assigned, neither can assign work to the other, neither is the other's reviewer of record by default, and the user is the final arbiter of any disagreement. The existing two-assessment rule applies to those named assignments. A co-chair who authorized a run must not be the sole judge of that run's result.

Session-count or cardinality differences alone do not block an otherwise valid integration. Do not invent identities, assignments, or signatures to reconcile them.

### Active-integrator lock

`CURRENT_RESEARCH_STATE.json` carries an `active_integrator` block with `holder`, `scope`, `base_commit`, `acquired_at`, and `status`. `status` is `HELD` or `RELEASED`.

- Only the holder writes to the canonical branch, and only within `scope`.
- A session not holding the lock may prepare an assessment separately but does not write canonical state while the lock is `HELD`.
- `base_commit` records the actual canonical commit the holder started from, so stale-base integration is detectable.
- The lock is released in the same milestone transaction that finishes the integration.
- Claiming a lock already `HELD` by another holder is a protocol violation, not a merge to resolve.
- A generic integration-session label may be used as `holder`; it is an operational lock label and does not create a co-chair identity or signature.

### Independent reproduction standard

Rerunning a producer's own verifier is provenance, not reproduction. An independent check must:

- import no producer module;
- be rebuilt from the definitions rather than the producer's code;
- have its own source and output hashes;
- cover at least one exact edge case and one central case.

### Dissent record

A disagreement is never silently closed. Append one `CO_CHAIR_DISSENT` journal entry carrying:

- the SHA-256 of both assessment files;
- the exact mathematical subject of the disagreement;
- whether it affects a load-bearing claim;
- `status`: `OPEN`, `RESOLVED`, or `REFERRED_TO_HALIL`;
- whether any downstream work was stopped.

An unresolved dissent on a load-bearing claim blocks acceptance.

## Result intake gate

Every returned package is reviewed in this order:

1. **Artifact integrity** — required files, SHA-256 manifest, provenance, deterministic paths, and package membership.
2. **Mechanical reproduction** — rerun verifier/certificates and reproduce a representative computation from source.
3. **Mathematical scope** — definitions, domains, quantifiers, edge cases, asymptotic uniformity, and dependency graph.
4. **Adversarial interpretation** — search for counterexamples, overbroad wording, post-selection, precision artifacts, and dependence between claimed savings.
5. **Evidence classification** — label each conclusion at its actual confidence level.
6. **Branch decision** — choose exactly one next action and record what remains open.

The computation session's verdict is an input, not the manager's final verdict.

## Audit and freeze gate

Ordinary research stops when a new load-bearing theorem, countertheorem, critical lemma, major branch closure, checkpoint freeze, or publication-critical claim appears. The result must then be packaged for an independent zero-trust audit. It cannot be used downstream until the audit verdict is integrated and any wording or artifact repairs are complete.

## Working-artifact rule

New prompts and manager notes remain working artifacts until accepted for a milestone. Historical frozen files are immutable; repairs use a new V2/V3 version. Mere local creation does not itself imply acceptance or canonical publication.

Once a computation, audit, or manager milestone is completed/accepted, however, the dual-persistence completion rule below applies automatically; the user does not need to separately request saving.

## Dual-persistence completion rule

Every completed computation, audit, or manager milestone closes with this exact operational chain:

`result → hashes/manifests → Drive save → Drive read-back → GitHub save/push → GitHub read-back → report`

A subordinate operation is not operationally complete until both the Drive and GitHub persistence/read-back legs succeed. If a connector, service, or permission failure prevents one leg, report that failure explicitly, preserve the recoverable artifacts, and do not label dual persistence as complete.

This rule changes persistence/governance only. It does not alter the scientific evidence class of any claim.

## Continuity requirement

Every accepted seal, returned result, audit verdict, repair, route decision, or material falsification must complete the atomic handoff and publication cycle in `CONTINUITY_PROTOCOL.md`. The active task, exact next action, accepted hashes, prohibited inferences, and persistence status must be recoverable from `CURRENT_RESEARCH_STATE.json` without chat history. Conversation memory is never an authoritative project-state store.

## Current authorized task

The E7 Recovery and E7R-B3 audit milestone is integrated:

- `E6-N1 [PROVED][AUDITED/ACCEPTED WITH SCOPE REPAIR]`;
- `E7R-B1 [PROVED][AUDITED]`;
- `E7R-B2 [PROVED][AUDITED]`;
- frozen full-window pointwise `E7R-B3 [FALSE][CLOSED]`;
- `B3-CT [PROVED][AUDITED]`;
- `E7R-B4 / E6-N2`, `E7R-B5`, and `E7R-B6` remain `[OPEN]`.

Historical/lost pre-recovery E7 conclusions remain `[UNVERIFIED — ARTIFACTS LOST]`. The global conditional bound `|E[F_{r,4}|S_r=n_r]|=O(1/r)` remains `[OPEN]`.

The only next scientific action is Stage 0 for `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1` as stated in `CURRENT_RESEARCH_STATE.json`. No weighted-operator or E8 work is authorized.
