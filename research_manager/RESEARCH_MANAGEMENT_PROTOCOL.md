# Collatz Research Management Protocol

## Session roles

### Research-manager session

This session owns research direction. It must:

- preserve the frozen dependency spine and branch-closure decisions;
- select one falsifiable, high-information target at a time;
- write the computation/proof prompt;
- independently inspect returned code, data, hashes, theorem statements, and failure reports;
- distinguish `[EXACT]`, `[PROVED]`, `[CERTIFIED NUM]`, `[NUM]`, `[LEAD]`, `[OPEN]`, `[FAIL]`, and `[PARK]`;
- decide whether to continue, repair, audit, freeze, park, or change branch;
- explain the result to the user without implying that Collatz is solved.

### Computation/proof session

The computation session executes only the authorized prompt. It must not:

- redefine the project objective;
- silently use unfrozen results as dependencies;
- promote numerics to theorems;
- begin downstream work after a load-bearing theorem appears;
- overwrite frozen artifacts.

## Co-chair governance

Two research-manager co-chairs may share this role. Neither can assign work to
the other, and neither is the other's reviewer of record by default. The final
arbiter of any disagreement is the user.

### Role rotation

At each milestone one co-chair writes the primary mathematical and artifact
assessment, and the other writes an independent adversarial review. The roles
swap at the next milestone. No joint decision is recorded until both
assessments exist.

A co-chair who authorized a run must not be the sole judge of that run's
result. Declare the conflict and take the adversarial role instead.

### Active-integrator lock

`CURRENT_RESEARCH_STATE.json` carries an `active_integrator` block with
`holder`, `scope`, `base_commit`, `acquired_at`, and `status`. `status` is
`HELD` or `RELEASED`.

- Only the holder writes to the canonical branch, and only within `scope`.
- The other co-chair prepares its assessment as a separate file or branch and
  never pushes to the canonical branch while the lock is `HELD`.
- `base_commit` records the commit the holder started from, so a stale-base
  commit is detectable.
- The lock is released in the same transaction that finishes the integration.
- Claiming a lock whose `status` is `HELD` by the other co-chair is a protocol
  violation, not a merge to resolve.

### Independent reproduction standard

Rerunning a producer's own verifier is provenance, not reproduction. An
independent check must:

- import no producer module;
- be rebuilt from the definitions rather than the producer's code;
- have its own source and output hashes;
- cover at least one exact edge case and one central case.

### Dissent record

A disagreement is never silently closed. Append one `CO_CHAIR_DISSENT` journal
entry carrying:

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

Ordinary research stops when a new load-bearing theorem, critical lemma, major branch closure, checkpoint freeze, or publication-critical claim appears. The result must then be packaged for an independent zero-trust audit. It cannot be used downstream until the audit verdict is integrated and any wording or artifact repairs are complete.

## Working-artifact rule

New prompts and manager notes remain working artifacts until explicitly accepted for canonical persistence. Historical frozen files are immutable; repairs use a new V2/V3 version. No commit, push, Drive upload, or freeze label is implied merely by creating a local working prompt.

## Continuity requirement

Every accepted seal, returned result, audit verdict, repair, route decision, or material falsification must complete the atomic handoff and GitHub publication cycle in `CONTINUITY_PROTOCOL.md`. The active task, exact next action, accepted hashes, and prohibited inferences must be recoverable from `CURRENT_RESEARCH_STATE.json` without chat history. Conversation memory is never an authoritative project-state store.

## Current authorized task

E6-N1 is accepted with the scope repairs in `decisions/CP20_TASK8B3_E6_INTEGRATION_2026-09-01.md`; E6-N2 through E6-N5 remain open. E7 Stage 0 is complete and its pre-run seal ZIP SHA-256 `0eb3b2d1487ec1d8dfcf0fc200b1082a8e61b7df2e52f9b6f8f1b943f2ad77f0` is accepted. E7 Stage 1 remains unauthorized until an external manager explicitly quotes and authorizes that hash; a generic continue instruction is insufficient. No deeper numerical run is authorized. Research milestones are synchronized to GitHub under `GITHUB_SYNC_POLICY.md`.
