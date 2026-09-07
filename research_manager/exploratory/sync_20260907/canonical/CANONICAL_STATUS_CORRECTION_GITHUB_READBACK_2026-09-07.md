# Canonical B4 V2 status correction — GitHub read-back

Date: 2026-09-07

Status: **COMPLETE ON GITHUB; GOOGLE DRIVE FULL-ARCHIVE UPLOAD AWAITS EXPLICIT PAYLOAD/DESTINATION APPROVAL**

- Baseline: `1a6f924fd86352c11f57a95b0382adaf92d15bcd`
- Published lock-acquisition Commit A: `26ca3ae9ba3a91a97b85c7116fd31e69cc17af90`
- Published final Commit B: `2461573739147763eb011faf03c344370a184d69`
- Remote `refs/heads/main` after push: `2461573739147763eb011faf03c344370a184d69`
- Remote/local commit equality: `PASS`
- Twelve load-bearing Git blobs, including the archive blob, compared after publication: `12/12 PASS`
- Worktree after publication: clean
- Final active stage: `STAGE_1_INPUT_INTEGRITY_FAILURE_AUTHORIZATION_CONSUMED_CLOSED`
- Final integrator lock: `RELEASED`
- Journal: `22/22`, append-only hash chain `PASS`
- `HANDOFF VERIFICATION: PASS`
- Current archive SHA-256: `f9a501670013f59ae56c3249e7e2daa9ff47d8b7ee1b50ba58acafd769acef12`
- Current archive bytes: `91675738`
- Current archive members: `1008`
- Two consecutive deterministic archive builds: identical SHA-256, `PASS`
- Archive/source byte comparisons for state, handoff, journal, manager decision, and verifier: `5/5 PASS`
- Verifier change: exactly one new closed-stage allowlist literal; no other verifier or scientific-program change.

The canonical record now says the truth: the B4 V2 sealed entrypoint was invoked, its sole authorization was consumed, the run stopped at Phase A before RUN_WITNESS/PRE_T1_GATE/T1/T1–T8, and no V3 execution is authorized.

The Google Drive connector rejected upload of the 91,675,738-byte full research archive because explicit approval for that exact sensitive payload and destination was not present. No workaround was attempted. Proposed destination, only if explicitly approved by Halil: folder `1Tg5P5wfILAgKYg-CiUmJS60kzdRFL2AU`, filename `Collatz_Research_Archive_CURRENT_2026-09-07_B4V2_CLOSED.zip`, exact local SHA-256 above.

This governance correction makes no scientific claim and does not prove Collatz.
