# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1 — STAGE 1 INPUT INTEGRITY FAILURE

Status: **[B4 STAGE1 INPUT INTEGRITY FAILURE]**

This is a forensic/provenance record only. It is not a scientific Stage-1 result and must not be integrated as mathematics.

## Authorized inputs

- execution-time canonical main: `0c0e0e55c490278396f0b8f5033000b80725fb6c`
- authorized seal SHA-256: `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`
- canonical contract SHA-256: `3d9fd4c0c029c135b86c43377aa414c87704f5e6c3dd4a008fa621f3b4f1185e`
- canonical authorization prompt Git blob: `d741bc5df165f525c63dccd9426c848f270cb5ce`
- canonical contract Git blob: `94a15beb7573c860e4891048e705c9f13a156f04`

## Passed preflight gates

Authorized seal hash, manifest/member hashes, 16 unique/sorted ZIP members, CRC, canonical base dependency blobs, fresh output absence, and canonical contract bytes all passed before the sealed entrypoint.

## Failure

Contract section B requires the single pre-T1 RUN_WITNESS to contain UTC timestamp, authorized seal SHA, canonical base SHA, process/session identity, and output-absence verdict.

The sealed launcher SHA-256 is `b59db6b20b9144ccf81cc8da5b947950eb2f8d0ce4c17e372da10cae69011fca`.

It created one witness, SHA-256 `2f15a06d765d728706903a17671b25e0b90ee0decb19b9dd2cd1e59294ec7675`, containing timestamp, authorized seal SHA, config SHA, PID, output-absence PASS and execution-count claim, but **not the required canonical base SHA field**. The sealed launcher source contains no write of that field.

The Phase-A repair commit `7042f332378f587b2a8ad839990994f3c0474458` repairs sealed ORDER.md byte preservation only and does not waive this witness requirement.

Therefore A–H was not fully satisfied and the attempted run is invalid/non-acceptable. No rerun is performed or self-authorized.

## Late-detection disclosure

The sealed entrypoint was invoked once before this omission was detected. Formal T1–T8 draft files were also produced before late detection. They are preserved only in the Drive forensic package and are explicitly INVALID/NON-CANONICAL. No B4-N1…B4-N7 or B4-CT claim from those drafts may be integrated or used downstream.

Scientific state therefore remains unchanged from the authorized pre-run state; in particular `E6-N2` remains `[OPEN]`.

## Persistence incident

During forensic persistence, a placeholder was accidentally written to default `main` at commit `c3062952ffb23754f62fd2dd6f6a6237e8b1d22c` and immediately removed at `f5269e5ddbf610b2305fafbd90fe2b1346376103`. GitHub compare from `0c0e0e55...` to `f5269e5d...` reports `files: []`: canonical tree content is unchanged, although main history advanced by two no-net-diff commits. No force-push was used.

## Forensic package

Drive package SHA-256: `71ad925b3d461e4ceb77293736cee75dfea116c012703e1308e00bc118125ab4`.

Drive folder: `1hYTCh3ilo3SfBRPePpNLBGcbQCDrPnsB`.

Raw Drive package read-back: `PASS`, byte-identical.

Nothing in this failed execution proves the Collatz conjecture.
