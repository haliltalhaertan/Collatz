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

E5-S1 is accepted as the exact finite conditioned-geometric bridge; E5-S2 through E5-S5 remain open. CP20 Task 8B3 E6 Stage 1 authorization has been dispatched to the existing computation/proof session and is running only under pre-run seal ZIP SHA-256 `83a26e81fc8a96479a6b76fdd33f962a047885115f00ec6a892248a0c07b6c57`. Do not send a duplicate authorization. No deeper numerical run is authorized. Any sealed-source or configuration change voids authorization. Research milestones are synchronized to GitHub under `GITHUB_SYNC_POLICY.md`. The simple full high-conductor exponential theorem is not an authorized next target.
