# CP20 TASK 8B3 — E7 STAGE 1 MANAGER AUTHORIZATION

**[MANAGER AUTHORIZED]** E7 Stage 1 under seal ZIP SHA-256:

`0eb3b2d1487ec1d8dfcf0fc200b1082a8e61b7df2e52f9b6f8f1b943f2ad77f0`

This is the explicit external authorization required by the Stage 0 acceptance
gate. It is not a generic continue instruction.

Manager decision:

- `research_manager/decisions/CP20_TASK8B3_E7_STAGE1_AUTHORIZATION_2026-09-01.md`
- SHA-256: `e653e6e9d627e8793eb8661c14063d463e7ffc5877dbfc3bdd0245b55b152dc1`

## Authorization witness

First create `CP20_TASK8B3_E7_MANAGER_AUTHORIZATION.md` containing:

1. `[MANAGER AUTHORIZED]`;
2. the accepted seal ZIP hash above;
3. the manager-decision path and hash above;
4. the current timestamp;
5. a statement that any pre-run manifested byte change voids authorization.

Do not alter any pre-run manifested file.

## Mandatory gates

Before using any new result, recompute and report:

- seal document, pre-run manifest, and seal-ZIP hashes;
- directory pre-run manifest 5/5;
- ZIP-internal pre-run manifest 5/5, six members only;
- all four E6/manager dependency hashes;
- absence of undeclared pre-run outputs.

On any mismatch return `[INPUT INTEGRITY FAILURE]` and stop without repair.

## Authorized work

After all gates pass:

1. Run the byte-identical sealed sources exactly once.
2. Prove or repair the exact block kernels and the candidate concatenation law
   before any asymptotic step.
3. Keep the frozen geometry: primary block `u=floor(r/3)`,
   `v=r-floor(r/3)` for `r>=12`; window `W_r=ceil(8*sqrt(r*log(r+1)))`;
   tail target `o(1/r)`; central block target `sup|Kcal| <= C_B/(v-u)`.
4. Do not add a depth, target extension, fit, plot, phase bin, frequency grid,
   precision level, adaptive window, rescue run, or post-output model choice.
5. Treat every computed value as `[NUM]` or `[CERTIFIED NUM]`; numerics cannot
   establish B2 through B6.
6. Complete all declared reports, verifier, manifests, and packages.

The depth ceiling remains the existing `r=8000` data.

## Stop rule

E7-B3 or higher, E6-N2 or higher, a quantitative arithmetic-cancellation
theorem, a different rigorous scale, or a route-closing countertheorem triggers
an independent zero-trust audit package and an immediate downstream stop. If
only E7-B1 survives, identify the first missing operator, contour, bridge, or
arithmetic estimate and recommend exactly one repaired follow-up, or park the
route.

Return the required Stage 1 answers, package paths, manifest counts, and
SHA-256 hashes. End with the exact disclaimer required by the E7 prompt.
