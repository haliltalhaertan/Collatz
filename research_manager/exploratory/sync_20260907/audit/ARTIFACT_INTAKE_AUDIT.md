# Artifact intake audit — 2026-09-07 exploratory synchronization

Status: **READ-ONLY INTAKE AUDIT / NOT A CANONICAL ACCEPTANCE.**

Scope is limited to the two currently untracked trees
`lead_parallel_20260907/` and `math_20260907/`. This intake did not execute any
producer, checker, launcher, seal, or numerical program; did not modify the source trees; and did
not commit, push, upload, authorize, or consume anything. File hashes quoted below were computed
read-only from the current bytes. The checkout observed during intake was
`d544bf2d072dd442c3f6528d87d9f7c4f86c23ce` on
`codex/prefix-bridge-20260906-persistence`; the remote tracking branch resolved to the same commit.
Canonical `origin/main` remained `1a6f924fd86352c11f57a95b0382adaf92d15bcd`.

## Executive verdict

The intake contains **59 files / 7,380,608 bytes**. The five A-lanes are finished as exploratory
work products, but “complete” does not mean accepted, sealed, reproducible, or ready to execute.
Only A2 and A4 have lane-wide SHA-256 lists. The two math lanes are incomplete interrupted runs:
M1 has only source plus a verification JSON and none of its advertised barrier outputs; M4 began a
run with `rmax 2000`, stopped after the `r=1200` log row, and has neither `PROFILE_DATA.csv` nor its
advertised mpmath result. There are no M2 or M3 directories in the supplied tree.

The A4 mathematical/integrity verdict remains credible at its stated evidence level, but its
publication findings are a historical snapshot and must not be copied as current state. Publication
commit `f5f9d613be10cd22e98097fe5285442819291692` subsequently resolved the missing-remote-branch and
untracked-package complaints. It did **not by itself** satisfy all README repairs. The later remote
commit `d544bf2d072dd442c3f6528d87d9f7c4f86c23ce` adds an accurate Drive failure/read-back receipt,
but that receipt contains a wrong full publication commit ID (`f5f9d616dff...` rather than the real
`f5f9d613be...`). Drive still contained no uploaded ZIP according to that receipt. Accordingly the
updated intake status is **`[VALID WITH PERSISTENCE ADDENDUM REQUIRED]`**, not an unconditional
publication pass.

## Lane classification

| Lane | Files / bytes | Completion | Evidence classes actually supported | Provenance and intake decision |
|---|---:|---|---|---|
| root manager documents | 2 / 24,895 | complete working assessment | mixed `[EXACT]`, `[PROVED]`, `[NUM]`, `[HEURISTIC]`, `[OPEN]`; no new acceptance | `MANAGER_ASSESSMENT_2026-09-07.md` and `CONTROL_AUDIT_2026-09-07.md`; both explicitly noncanonical. Preserve as manager interpretation, not as source evidence. |
| A1 launcher repair | 18 / 143,458 | **design lane complete; operational repair incomplete** | exact source/blob comparisons and synthetic-gate tests; scientific targets remain `[OPEN]`/not executed | Derived from historical B4 commits and a throwaway-clone harness. Patches are unapplied proposals; no V3 seal, CI-integrator update, new authorization, or live Stage-1 run exists. Quarantine execution-capable files. |
| A2 numerical probe | 11 / 6,775,517 | complete finite run | `[NUM]`; integer/residue bookkeeping and weight normalization are exact implementation checks, but complex outputs and asymptotic readings are not `[EXACT]` theorems | Producer was interrupted after data completion; the manager authored `REPORT.md` from existing data. `SHA256SUMS.txt` covers all 10 other lane files and matches current bytes by intake hash comparison. Preserve as a self-contained numerical evidence bundle. |
| A3 analytic attack | 5 / 37,930 | complete exploratory manuscript | exact algebraic identities are candidates for `[PROVED]`; numerical observations `[NUM]`; barrier story `[HEURISTIC]`; PWE, uniform-H, triangle bound and E6-N2 `[OPEN]` | Self-labelled “proved here” arguments have no independent lane-specific proof audit in this intake. Preserve, but downgrade them to **proposed proofs pending independent review** when cited outside the lane. |
| A4 package audit | 10 / 78,429 | complete for its 2026-09-07 snapshot | exact rational recomputations and integrity checks support `[EXACT]`/`[PROVED]` for the prefix identities and cutoff; target bounds remain `[OPEN]` | Independent rebuild against `prefix_bridge_20260906`; `SHA256SUMS.txt` covers all 9 other A4 files and matches current bytes. Its Git/README verdict is time-indexed and partly superseded; see dedicated section below. |
| A5 CP17 publication review | 6 / 87,660 | review complete; **publication package incomplete** | editorial/audit findings; no new mathematical proof class | Manager-verified source/PDF mismatch, missing on-disk bibliography, and journal-fit review. No lane manifest or bundled raw web receipts. Do not label the manuscript reproducible or submission-ready until the actual PDF-producing source is recovered. |
| M1 barrier numeric | 2 / 25,769 | **incomplete** | source declares `[NUM]`; `VERIFICATION.json` supports preflight identity/DP/crosscheck checks only; barrier hypothesis remains `[HEURISTIC]` | `barrier_probe.py` advertises `Q_RESULTS.csv`, `DECOMPOSITION.csv`, `TSTAR.csv`, `BRIDGE_PREDICTION.csv`, a run log, and other generated artifacts, but none are present. No manifest and no captured stdout/exit record. Do not infer that Tasks 2–6 ran. |
| M4 theta profile | 5 / 206,950 | **incomplete interrupted run** | finite partial output `[NUM]`; self-test is implementation evidence only; limiting profile and positive infimum remain `[OPEN]` | `RUN_LOG.txt` says `rmax 2000` but ends at `r=1200`; `run_stdout.txt` likewise ends at 1200. `PROFILE_DATA.csv` and `MPMATH_CROSSCHECK.json` are absent. `__pycache__/theta_profile.cpython-314.pyc` is derived environment noise, not scientific provenance. |

## Complete file inventory

The inventory below names every file present at intake. A2 and A4 hashes are already captured by
their internal `SHA256SUMS.txt`. The remaining lanes require a new external manifest before
packaging.

### Root (2)

- `MANAGER_ASSESSMENT_2026-09-07.md`
- `CONTROL_AUDIT_2026-09-07.md`

### A1 launcher repair (18)

- `derived_v3_files/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_CONFIG.json`
- `derived_v3_files/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md`
- `derived_v3_files/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1.py`
- `DRY_RUN_EXIT.txt`
- `DRY_RUN_INTEGRITY_GATE.py`
- `DRY_RUN_REPORT.json`
- `DRY_RUN_RESULTS.md`
- `DRY_RUN_STDERR.txt`
- `DRY_RUN_STDOUT.txt`
- `JOURNAL_SCHEMA_DRIFT.md`
- `LAUNCHER_DEFECT_ANALYSIS.md`
- `make_v3_patches.py`
- `SUMMARY.md`
- `V3_CONFIG.patch`
- `V3_CONTRACT.patch`
- `V3_PATCH_HASHES.json`
- `V3_RESEAL_REPAIR_PROPOSAL.md`
- `V3_STAGE1.patch`

### A2 numerical probe (11)

- `mpcheck_stdout.txt`
- `MPMATH_CROSSCHECK.json`
- `prefix_probe.py`
- `PROBE_RESULTS.csv`
- `PROBE_RESULTS.json`
- `probe_stdout.txt`
- `REPORT.md`
- `RUN_LOG.txt`
- `SHA256SUMS.txt`
- `VERIFICATION.json`
- `WINDOW_TABLE.csv`

### A3 analytic attack (5)

- `NEXT_LEMMA.md`
- `STRUCTURE.md`
- `SUMMARY.md`
- `TRIANGLE_VS_SIGNED.md`
- `UNIFORM_H_ANALYSIS.md`

### A4 package audit (10)

- `AUDIT_VERDICT.md`
- `audit_integrity.py`
- `audit_integrity_results.json`
- `audit_integrity_stdout.txt`
- `audit_recompute.py`
- `audit_recompute_results.json`
- `audit_recompute_stdout.txt`
- `git_evidence.txt`
- `SHA256SUMS.txt`
- `v1_v2_diff.txt`

### A5 CP17 publication (6)

- `CITATION_AUDIT.md`
- `CLAIMS_WORDING_AUDIT.md`
- `DISCLOSURE_DRAFT.md`
- `JOURNAL_FIT.md`
- `SELF_CONTAINMENT_CHECK.md`
- `SUMMARY.md`

### M1 barrier numeric (2)

- `barrier_probe.py`
- `VERIFICATION.json`

### M4 theta profile (5)

- `theta_profile.py`
- `SELFTEST.json`
- `RUN_LOG.txt`
- `run_stdout.txt`
- `__pycache__/theta_profile.cpython-314.pyc`

## A4 verdict after subsequent publication

A4's `[VALID WITH WORDING REPAIR]` consisted of three required persistence repairs and two optional
precision repairs. Their status is:

| A4 item | Effect of `f5f9d613be...` | Current status at `d544bf2d...` |
|---|---|---|
| Remote GitHub preservation branch, committed package | **Resolved.** The package directory and sibling ZIP were committed, and the remote branch contains the publication commit. | PASS; the preservation branch is not canonical acceptance and `main` is unchanged. |
| “Published” and “receipts live beside the package” | **Partial.** Publication became true, but `f5f9d61` contains no persistence receipt beside the package. | The later `PERSISTENCE_STATUS_2026-09-07.md` is now on the remote branch, so a receipt exists, but its publication SHA is mistyped. Repair the SHA before treating the receipt as exact provenance. |
| Drive link should be unverified until read-back | **Not resolved by f5.** README prints a bare folder link. | Still substantively unresolved: the later receipt says folder creation PASS, ZIP upload BLOCKED, folder read-back 0 files, and raw-byte read-back not complete. README needs that qualification or a pointer to the receipt. |
| Three-prefix producer check versus four-prefix load-bearing identity | Not changed. | Optional wording repair remains useful; no scientific invalidity follows because A4 independently checked the four-prefix identity. |
| CRLF/hash and `.gitattributes` precision note | Tracking made `.gitattributes` effective, but README did not add the CRLF detail. | Optional documentation repair remains. Stored hashes and ZIP were nevertheless verified by A4. |

Therefore A4's **mathematical result is not invalidated**, but the correct present-tense package
verdict is: `[VALID WITH PERSISTENCE ADDENDUM REQUIRED]`; GitHub preservation PASS, Drive ZIP
persistence BLOCKED, canonical B4 acceptance NOT GRANTED.

## Highest-risk blockers and contradictions

1. **Wrong full Git commit in the persistence receipt.**
   `PERSISTENCE_STATUS_2026-09-07.md` records
   `f5f9d616dff06a70477324500560779215165411`; Git resolves the actual publication commit as
   `f5f9d613be10cd22e98097fe5285442819291692`. This is a load-bearing provenance typo and should be
   corrected by an append-only/addendum-style record or an ordinary correction commit, without
   rewriting historical scientific artifacts.
2. **Drive is not synchronized.** Folder existence is not artifact persistence. The authoritative
   receipt says zero uploaded files and no raw-byte verification. Any “everything is synchronized”
   statement is currently false.
3. **M1 and M4 are incomplete.** Their partial bytes must be preserved as interrupted-run evidence,
   not promoted into completed results. M4's declared `rmax=2000` versus last row `r=1200` is the
   clearest termination witness.
4. **A1 is execution-capable but unauthorized.** The derived launcher, patch generator and dry-run
   harness must never be run from the live checkout as part of packaging. A1 explicitly has no V3
   seal or authorization; synthetic PASS does not authorize B4 T1–T8.
5. **A3 proof labels are not independently closed.** Exact coordinate identities appear strong,
   but the broader “restatement/not a reduction”, exact `sqrt(r)`-loss, and difficulty-equivalence
   language mix theorem, asymptotic argument and research interpretation. Cite exact identities
   separately; retain PWE/barrier/rate claims as `[OPEN]` or `[HEURISTIC]` until a second proof audit.
6. **A2 terminology can be misread.** “Exact transfer-matrix DP ... with complex128 accumulation”
   means exact combinatorial/residue state plus floating complex accumulation. The reported complex
   values are `[NUM]`, not exact cyclotomic evaluations or an asymptotic proof.
7. **CP17 is not reproducible.** A5 says the available `.tex` cannot be the source of the recorded
   PDF, and the bibliography is absent outside ZIPs. “Ready after fixes” must not be shortened to
   “ready to submit”; recovering the actual source is the first blocker.
8. **Manifest coverage is fragmented.** A2 and A4 are covered; root, A1, A3, A5, M1 and M4 have no
   complete byte manifest. `V3_PATCH_HASHES.json` covers selected A1 derivatives only. There is no
   top-level inventory, provenance record, or package hash for either tree.

## Exact packaging recommendation

Do not merge these bytes into `prefix_bridge_20260906`, do not amend its historical A4 verdict, and
do not place any of them on canonical `main` as accepted science. Package them as a new dated
**exploratory synchronization batch** with two logical components:

1. `lead_parallel_20260907_raw/`: preserve all 52 files byte-for-byte. Add a generated top-level
   `SHA256SUMS.txt`, a machine-readable inventory (relative path, size, SHA-256, lane, evidence
   class), and a provenance README pinned to source checkout `d544bf2d...`. Retain A2/A4 internal
   manifests as nested evidence. Mark A1 `DO_NOT_EXECUTE / UNAUTHORIZED PROPOSAL`, A3 `PENDING
   INDEPENDENT PROOF AUDIT`, and A5 `PUBLICATION SOURCE BLOCKED`.
2. `math_20260907_interrupted_raw/`: preserve the seven observed files exactly, including the
   `.pyc` only in the raw forensic archive. The curated scientific view should exclude `.pyc` and
   explicitly list the missing advertised outputs. Mark M1 and M4 `INCOMPLETE / DO NOT CITE AS A
   FINISHED RUN`. If work resumes, use a new run ID/output directory; do not append to or silently
   complete these partial logs.
3. Add a persistence addendum that records the correct `f5f9d613be...` publication SHA, the current
   branch tip `d544bf2d...`, ZIP size/hash, Drive object ID, upload result, downloaded-byte hash, and
   verification timestamp. Until Drive returns a file and a raw-byte/download hash matches, record
   Drive as `BLOCKED`, never `PASS`.
4. Commit the synchronization batch to a new `codex/` preservation branch (or a clearly scoped
   continuation branch), push non-forcefully, verify the remote commit/tree, build deterministic
   ZIPs from the committed blobs, upload those exact ZIP bytes to Drive, download/read back, and
   compare SHA-256. The GitHub and Drive receipts must point at one another and at the same manifest.
5. Only after persistence closes should scientific continuation start: first an independent proof
   audit of A3's exact-coordinate/circularity claims and a bounded, separately identified rerun or
   continuation of M1/M4. None of those actions may consume or reuse the expired B4 authorization.

This intake changes no scientific status: E6-N2, uniform-H, PWE, the triangle-weighted bound, the
nonzero phase profile, B4, and Collatz remain `[OPEN]` or not established as stated in their source
documents.
