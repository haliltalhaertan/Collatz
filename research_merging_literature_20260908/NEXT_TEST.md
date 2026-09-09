# A bounded test suggested by the literature review

Proposal only, not executed. No solver success or new exclusions claimed.

Select one small unresolved checkpoint guard family. Retain its initial integer n0 as a reference variable. Specify a finite candidate transition library, each with an exact all-parameter positive-integer merge witness. Intermediate values may increase.

A successful exit is either a separately verified convergent base or a checkpoint in S strictly smaller than n0. Any other terminal state is explicitly unresolved. A termination certificate alone is insufficient.

Seek one fixed small affine or lexicographic ranking template. Verify separately:

1. Initial-state coverage for every nonnegative integer parameter of the selected guard.
2. Sound positive-integer transitions, congruence guards and merge witnesses.
3. Well-founded progress for the selected strategy, including its total availability outside successful exits.
4. Every terminal state allowed by that strategy is a successful exit.

If all obligations hold, the result is a new universally quantified exclusion of a least exceptional checkpoint. If an obligation fails, record the failed template or uncovered parameter constraint. No failure of a bounded solver template establishes mathematical impossibility.

The existing 275 decreasing descriptions alone need no solver to prove termination. They can be used as already verified reductions but cannot replace the four obligations above. In an orbit-graph experiment, never delete all minimum-excluded residue classes as though every exceptional orbit avoided them.

Independent literature cross-check by audit_coarse_identity: final arXiv v3 of Yolcu–Aaronson–Heule, Theorems 2.6, 2.15, 3.17, and official repository source. No independent solver run. The primary string prover is not directly an affine-guard engine; using it requires a proved translation.
