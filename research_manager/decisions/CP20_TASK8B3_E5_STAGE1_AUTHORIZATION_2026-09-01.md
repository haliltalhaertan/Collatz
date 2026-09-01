# CP20 Task 8B3 E5 — Stage 1 Manager Authorization

## Decision

**[MANAGER AUTHORIZED]**

CP20 Task 8B3 E5 Stage 1 is authorized under the exact pre-run seal ZIP SHA-256:

`ffb2fee60acde00ae894e7b408a817e5b244d8316d6c1f82ead1dab488c689c7`

This authorization applies only to the byte-identical sealed inputs listed below. Any change requires a new seal and a new external authorization turn.

## Independently verified seal

- `CP20_TASK8B3_E5_PRE_RUN_SEAL.md`: `6bdd6cf5e3680687f5ab318d631578d66dbdf7fc3e5246c1b9649224bdd50ed1`.
- `CP20_TASK8B3_E5_PRE_RUN_SHA256SUMS.txt`: `f2cbadd7a20fb3a1105f876ad6573a813be155ffe0527c9b3ba5ed921f508557`.
- `CP20_TASK8B3_E5_PRE_RUN_SEAL.zip`: `ffb2fee60acde00ae894e7b408a817e5b244d8316d6c1f82ead1dab488c689c7`.
- Directory pre-run manifest: 5/5 payload hashes matched.
- ZIP-internal pre-run manifest: 5/5 payload hashes matched; six ZIP entries including the manifest.
- Accepted external E3/E4/audit/manager inputs: 9/9 hashes matched the sealed configuration.
- The sealed diagnostics source parsed successfully.
- The authorization guard rejected execution while the manager witness was absent.
- No undeclared pre-authorization file was present in the E5 directory.

## Authorized scope

The computation/proof session may now:

1. create `CP20_TASK8B3_E5_MANAGER_AUTHORIZATION.md` containing the exact marker `[MANAGER AUTHORIZED]` and the accepted seal ZIP hash above;
2. rerun all sealed integrity gates;
3. execute the byte-identical sealed diagnostics within the declared `r<=8000`, `C=4`, `d=-8`, precision, frequency, bin, and checkpoint ranges;
4. carry out the proof and falsification program P1-P5;
5. create only the declared Stage 1 reports, data, verifier output, manifest, and packages.

## Non-negotiable restrictions

- Do not edit any of the five pre-run manifested files.
- Do not change or extend a range, precision, frequency, bin, fit, plot, boundary rule, theorem target, or stopping threshold.
- Do not rescue a failed check. Stop and report the first failing condition.
- Do not use numerics to certify a theorem or a nonzero transfer coefficient.
- Do not assume the infinite unrolling tail condition, compactness, a degree-one bound, or a fixed-target profile.
- If E5-S3 or higher, or another route-changing theorem/no-go result, is obtained, create the independent-audit package and stop all downstream work.

Nothing in this authorization broadens the task toward a Collatz proof.
