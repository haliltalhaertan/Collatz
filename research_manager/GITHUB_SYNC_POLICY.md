# GitHub Research Sync Policy

## Scope

The user authorized GitHub publication of research progress and data as milestones are produced. Accepted seals, manager decisions, prompts, reports, deterministic sources, manifests, verifier outputs, and declared numerical data are publishable.

## Canonical publication form

1. `research_manager/` is tracked directly so prompts and decisions remain browsable.
2. `Collatz_Research_Archive_CURRENT.zip` is the deterministic current archive containing the full extracted research archive, research-manager records, and independent audit outputs.
3. `CURRENT_ARCHIVE_BUILD.json` records the archive hash, member count, source groups, and uncompressed byte count.
4. The original imported archive is retained as provenance.

## Exclusions

The following are working copies, not independent research data, and are not committed directly:

- `_extracted/` after its contents have been included in the current archive;
- `_verification/` temporary checks;
- independent-audit `isolated_run`, `input_audit`, and `input_complete` copies that duplicate hash-identified E3/E4 inputs;
- Python caches and other reproducible runtime residue.

Independent audit reports, check source, machine-readable checks, manifests, saved outputs, and the audit-output ZIP are included in the canonical archive.

## Milestone rule

At each accepted seal, completed result package, independent audit verdict, or manager route decision:

1. verify hashes and manifests;
2. rebuild the deterministic current archive;
3. verify no archive member exceeds GitHub's single-file limit and the generated ZIP is below that limit;
4. commit a concise status update;
5. push the current branch to `origin`;
6. record the commit and archive SHA-256 in the manager handoff.

Failed or partial computations are published only when they are material falsification evidence and carry explicit status labels.
