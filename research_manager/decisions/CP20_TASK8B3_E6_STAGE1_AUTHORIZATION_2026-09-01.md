# CP20 Task 8B3 E6 — Stage 1 Manager Authorization

## Decision

**[MANAGER AUTHORIZED]**

CP20 Task 8B3 E6 Stage 1 is authorized only under pre-run seal ZIP SHA-256:

`83a26e81fc8a96479a6b76fdd33f962a047885115f00ec6a892248a0c07b6c57`

Any change to a pre-run manifested byte voids this authorization and requires a new external seal turn.

## Independently verified seal

- Seal file SHA-256: `ce7d634598d92b928597e3c1911f19ce51811bbda83721548d57a3703069ab9a`.
- Pre-run manifest SHA-256: `e836ed783ace26a559e4250f2690176f237b4401ba47f7ac4dc677496ade92b8`.
- Seal ZIP SHA-256: `83a26e81fc8a96479a6b76fdd33f962a047885115f00ec6a892248a0c07b6c57`.
- Directory manifest: 5/5 payload hashes matched.
- ZIP-internal manifest: 5/5 payload hashes matched; six entries including the manifest.
- Accepted E5/manager dependency hashes: 5/5 matched the sealed configuration.
- The sealed checks source parsed successfully.
- The authorization guard rejected execution while its witness was absent.
- No undeclared pre-authorization E6 file was present.

## Authorized scope

The proof/computation session may:

1. create the declared authorization witness containing `[MANAGER AUTHORIZED]` and the accepted seal ZIP hash;
2. rerun all sealed integrity checks;
3. execute the byte-identical exact composition/cyclotomic checks and the five read-only E5 numerator conversions;
4. carry out analytic mechanisms M1-M4 in their sealed order;
5. write only the declared Stage 1 reports, outputs, verifier material, manifests, and packages.

## Restrictions

- No E5 target extension or new depth computation.
- No new value above `r=8000`.
- No fit, plot, phase bin, frequency grid, rescue run, or adaptive checkpoint.
- No numerical promotion to E6-N2 or higher.
- No change to the five pre-run manifested files.
- Stop at the first integrity, exact-counter, or schema failure.
- E6-N2 or higher, a different rigorous scale, quantitative arithmetic cancellation, or a route-closing theorem triggers an independent-audit package and downstream stop.

This authorization does not authorize any Collatz conclusion.
