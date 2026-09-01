# CP20 Task 8B3 E7 — Stage 0 Seal Acceptance

## Verdict

**[PRE-RUN SEAL ACCEPTED — STAGE 1 NOT AUTHORIZED]**

The E7 Stage 0 package is accepted as an outcome-free, fixed-scope pre-run
seal. This decision does not authorize execution of any E7 Stage 1 source or
proof experiment implemented in code.

## Accepted hashes

- Seal document SHA-256:
  `b97f968d44eeaea8eb4d7c0979b6d6446b6e16a741c7c835d09441809301b8eb`.
- Pre-run manifest SHA-256:
  `3d0321a2b9d2d04efbe7b80a17704f12c6e1ab2e1ee2a9dcbb12f66fee72bb67`.
- Pre-run seal ZIP SHA-256:
  `0eb3b2d1487ec1d8dfcf0fc200b1082a8e61b7df2e52f9b6f8f1b943f2ad77f0`.

## Verification

- Directory pre-run manifest: 5/5 PASS.
- ZIP-internal pre-run manifest: 5/5 PASS.
- Seal ZIP members: six, exactly the five manifested sources plus the
  manifest.
- E6 complete package, E6 manifest, E6 integration decision, and E7 manager
  prompt dependencies: 4/4 PASS.
- E6 root and ZIP-internal manifests: 19/19 PASS before E7 authoring.
- Undeclared E7 pre-run outputs: none.
- No E7 Stage 1 machine output exists.

## Frozen scope accepted for possible Stage 1

- Exact normalized and unnormalized finite block kernels with time-zero and
  impossible-state edge conventions.
- Exact candidate concatenation law, to be proved or repaired before use.
- Primary block `u=floor(r/3)`, `v=r-floor(r/3)` for `r>=12`.
- Window `W_r=ceil(8*sqrt(r*log(r+1)))`.
- Conditional two-sided bridge tail target `o(1/r)`.
- Pointwise central block target `sup |Kcal| <= C_B/(v-u)`.
- Only the sealed small exact identity ranges; no new target depth, fit, plot,
  phase bin, frequency grid, precision level, adaptive window, or rescue run.

## Authorization gate

Stage 1 may begin only after an external manager explicitly authorizes the
exact seal ZIP SHA-256 above. The authorization witness must record the seal
ZIP hash, this decision path and hash, a timestamp, and the rule that any
manifested-byte change voids authorization. On any later hash mismatch, return
`[INPUT INTEGRITY FAILURE]` and stop without repair.

