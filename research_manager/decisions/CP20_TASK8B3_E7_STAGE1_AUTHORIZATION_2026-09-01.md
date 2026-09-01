# CP20 Task 8B3 E7 — Stage 1 Manager Authorization

## Decision

**[MANAGER AUTHORIZED]**

CP20 Task 8B3 E7 Stage 1 is authorized only under pre-run seal ZIP SHA-256:

`0eb3b2d1487ec1d8dfcf0fc200b1082a8e61b7df2e52f9b6f8f1b943f2ad77f0`

Any change to a pre-run manifested byte voids this authorization and requires a
new external seal turn.

## Independently verified seal

Every figure below was recomputed by this manager session from the committed
archive, not accepted from the computation session's report.

- Seal document SHA-256:
  `b97f968d44eeaea8eb4d7c0979b6d6446b6e16a741c7c835d09441809301b8eb`.
- Pre-run manifest SHA-256:
  `3d0321a2b9d2d04efbe7b80a17704f12c6e1ab2e1ee2a9dcbb12f66fee72bb67`.
- Pre-run seal ZIP SHA-256:
  `0eb3b2d1487ec1d8dfcf0fc200b1082a8e61b7df2e52f9b6f8f1b943f2ad77f0`.
- Directory pre-run manifest: 5/5 recomputed and matched.
- ZIP-internal pre-run manifest: 5/5 recomputed and matched; six members,
  exactly the five manifested sources plus the manifest.
- Directory and ZIP-internal manifests are byte-identical to each other.
- E6/manager dependency hashes: 4/4 matched, each resolved to a byte-equal
  archive member — E6 complete package, E6 final manifest, E6 manager
  integration decision, and the E7 manager prompt.
- The repository copies of the E6 integration decision and the E7 prompt are
  byte-identical to the hashes frozen inside the sealed configuration.
- Undeclared E7 pre-run outputs: none. The E7 directory holds exactly the seven
  declared files.
- All nine declared Stage 1 outputs are absent from the archive, confirming the
  seal is outcome-free and Stage 1 has not been executed.
- Journal hash chain: six entries, sequence and `previous_entry_sha256` intact.
- Archive `0dc2284a1d0113bd79fd462db10ee7b0278d9be8c38a42fd8563c389bb7c5902`
  matches its build record in hash, byte size, and member count (834); full CRC
  scan clean.

## Verifier change review

The stage assertion in `tools/verify_handoff.py` was widened from a single
literal to the lifecycle set named in `CONTINUITY_PROTOCOL.md`. The diff was
reviewed adversarially: no hash, manifest, member-count, CRC, or journal check
was weakened or removed.

## Authorized scope

The proof/computation session may:

1. create the declared authorization witness recording `[MANAGER AUTHORIZED]`,
   the accepted seal ZIP hash, this decision path and hash, a timestamp, and
   the voiding rule;
2. recheck every manifested and dependency hash before execution;
3. execute the byte-identical sealed sources exactly once;
4. carry out the sealed E7 program at the frozen block geometry
   `u=floor(r/3)`, `v=r-floor(r/3)`, `r>=12`, window
   `W_r=ceil(8*sqrt(r*log(r+1)))`;
5. write only the declared Stage 1 reports, outputs, verifier material,
   manifests, and packages.

## Restrictions

- No new target depth, no value above `r=8000`, no extension of any target
  sequence.
- No fit, plot, phase bin, frequency grid, precision level, adaptive window,
  rescue run, or post-output model choice.
- No change to the five pre-run manifested files.
- Stop at the first integrity, exact-identity, or schema failure and return
  `[INPUT INTEGRITY FAILURE]` without repair.
- E7-B3 or higher, E6-N2 or higher, a quantitative arithmetic-cancellation
  theorem, a different rigorous scale, or a route-closing countertheorem
  triggers an independent zero-trust audit package and an immediate downstream
  stop.

## Scope this authorization does not grant

E6-N2 through E6-N5 and E7-B2 through E7-B6 remain open. This authorization
grants no asymptotic, no nonzero coefficient, no lower bound, and no Collatz
conclusion.
