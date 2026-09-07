# CP20 exploratory team synchronization — 2026-09-07

Status: preservation and review batch, not canonical scientific acceptance and not a Stage-1 authorization.

This batch synchronizes the work visible from several research sessions without pretending that incomplete runs are complete. `RAW_INVENTORY_SHA256.txt` covers all 59 source-tree files observed at intake (7,380,608 bytes).

## Source lanes

- `lead_parallel_20260907/`: 52 raw files. A1 is an unauthorized launcher/reseal proposal and MUST NOT be executed; A2 is finite numerical evidence; A3 is exploratory mathematics; A4 is an independent package audit; A5 reports that the CP17 submitted PDF is not reproducible from the currently available source.
- `math_20260907/`: seven raw files and two interrupted lanes. M1 lacks its advertised results. M4 was configured for rmax=2000 but its log ends at r=1200 and required output files are absent. Cite neither as a completed run. The generated `.pyc` is preserved only inside the forensic raw ZIP and is excluded from the loose curated Git view.
- `audit/ARTIFACT_INTAKE_AUDIT.md`: bounded intake and evidence classification.
- `git/GIT_SYNC_MAP.md`: branch map and safe additive integration topology.
- `math/PWE_BARRIER_INDEPENDENT_REVIEW.md`: independent continuation of PWE/barrier analysis.
- `math_audit/PWE_BARRIER_AUDIT.md`: completed independent scope audit of the PWE/barrier continuation.
- `kfb/KFB_FEASIBILITY.md`: feasibility reduction for the killed Feynman--Kac bridge; its `O(1/m)` conclusion is conditional.
- `kfb_audit/KFB_FEASIBILITY_AUDIT.md`: independent audit identifying the missing uniform killed positive local-limit estimate (BLL).
- `canonical/CANONICAL_STATUS_CORRECTION_PLAN.md`: plan-only repair for stale canonical status; it is not authorization and has not changed `main`.
- `TEAM_SYNC_HANDOFF_2026-09-07.md`: compact cross-session continuation point and the single selected next scientific action.

## Raw archives

- `lead_parallel_20260907_RAW.zip`: SHA-256 `e7cff5854e6cda42f216c25ec9fcd70676a8d6877bab013f8899f33732ff0443`, 2,403,892 bytes.
- `math_20260907_INTERRUPTED_RAW.zip`: SHA-256 `c1d200539009fe7c87d4ccec86071ab69d3bf9143c0721258039436e78848f03`, 79,988 bytes.

The raw ZIPs contain the source directories byte-for-byte as observed. They are evidence preservation, not permission to resume or execute a program. Resume incomplete numerical work under a new run identifier and frozen plan; do not append silently to interrupted logs.

Drive byte persistence/read-back is recorded in `DRIVE_RAW_READBACK_2026-09-07.md`: both ZIP hashes match after complete raw retrieval. Folder: https://drive.google.com/drive/folders/1Tg5P5wfILAgKYg-CiUmJS60kzdRFL2AU.

## Scientific checkpoint

The exact prefix mixture and logarithmic prefix-excess cutoff remain valid exploratory results. The triangle-weighted bound, PWE, killed Feynman-Kac ballot theorem, crossing-term cancellation, E6-N2/B4, a nonzero profile, polynomial lower bounds and Collatz remain OPEN unless a later audited record explicitly says otherwise.

The remote canonical `main` at intake was `1a6f924fd86352c11f57a95b0382adaf92d15bcd`; its B4 V2 instruction is stale because later branches record authorization consumption and no T1-T8 execution. Do not execute the old B4 V2 seal.

No force push or wholesale merge of divergent evidence/publication branches is authorized by this preservation package.
