# Hybrid interval/residue certificate: bounded test and precision barrier

2026-09-08. Exploratory continuation of the count-certificate test. No paid calls, new canonical stage, or Collatz theorem. The bounded panel was fixed in PLAN.md before running; source results are identified by SHA-256 in RESULT.json.

## Outcome

The joint model is sound and can improve finite upper bounds, but fixed extra low digits do not remove its asymptotic precision barrier. On a representative deeper panel row it costs more states while giving exactly the old poor bound. Do not scale this design up on the expectation that a positive exponential saving will appear.

## Exact model and soundness

For r positive valuation letters of total A, q=3^r, normalized prefix state x=2^(-A)B_j modq evolves by x'=(3x+c_a) modq, c_a=2^(a-A) modq. Choose high precision t and low precision ell, t+ell<=r. Put H=3^t, W=q/H, P=3^ell. Cell(b,s) contains

    x=bW+s+Pv, 0<=v<W/P, 0<=b<H, 0<=s<P.

At a step the low child residue is exactly (3s+c_a) modP. The possible high child buckets are computed from the integer representatives of this SAME cell; no continuous relaxation replaces modular feasibility. The count majorant is the sum over the next feasible letter m of the maximum child value over these buckets. Terminal cost is1 iff bW+s<L. The first step from x=0 remains exact.

Backward induction proves Q<=F_root<=N, where N=binom(A-1,r-1). Every actual successor is included, and terminal intersection majorizes actual success. Refining ell yields nested cells, so the bound cannot increase. At t+ell=r the cells are singletons and the bound equals Q; these rows are calibrations, not evidence of useful compressed counting.

## Experiment

Reuse all48 rows: r=3..10, A=floor(log_2(3)*r)+d with d=-1,0,1, and L=floor(2^(br)) for b=.8,1.2. Set t=min(3,r-1), and test ell=0..min(3,r-t). This gives162 bounds, including baseline and full-precision calibrations. There are90 genuinely compressed low-digit refinements;29 improve strictly over their high-only baseline. No asymptotic curve was fitted.

All bounds enclose the previously independently enumerated exact Q. High-only baselines match the previous implementation. Refinement monotonicity, singleton exactness, the explicit splices, and the structural lower bound below pass exact integer checks.

Representative row: r=10,A=15,L=256,N=2002,Q=10, high precision t=3:

| Low digits ell | Upper bound F | Memoized Bellman states |
|---:|---:|---:|
| 0 | 1827 | 1215 |
| 1 | 1827 | 2169 |
| 2 | 1827 | 4764 |
| 3 | 1827 | 10170 |

The earlier exact future-equivalence recursion used6646 memoized states on this row. These counts describe these implementations, not a general complexity lower bound. They show that an abstraction may introduce more reachable abstract states than the exact quotient has reachable states, while still losing accuracy.

There are genuine finite improvements: at r=7,A=11,L=48, N=210,Q=1, the upper bound drops203 ->192 ->166 ->148 as ell goes0,1,2,3. This remains far from the exact count, and the algebraic barrier below rules out treating fixed precision as an exponential-rate strategy.

## The original splice is repaired, but a compressed splice survives

For r=2,A=3,L=3,t=1, adding ell=1 blocks the8->7 substitution and changes the count bound2 to exact1. Here t+ell=r, so this is only a singleton calibration.

A genuinely compressed example uses r=4,A=6,t=2,ell=1,L=9 and word(1,1,1,3). The actual normalized path is

    0 ->19 ->14 ->37 ->20,

which is unsuccessful. The hybrid relaxation can instead splice

    0 ->19 ->14, replace14 by11, then11 ->28,
    replace28 by31, then31 ->2.

The first replacement preserves interval[9,18) and residue2 modulo3; the second preserves interval[27,36) and residue1 modulo3. Every chosen single step is arithmetically valid, but the concatenated path is not the original word's path. Endpoint2 is falsely admitted into[0,9).

This is an offline witness of information loss, not a claim that the Bellman strategy optimizes independently for every future word. That quantifier distinction from the previous audit is preserved.

## The hybrid precision barrier

Assume 1<=t<r, t+ell<=r-1, and L>=P=3^ell. Then

    F_root/N >=3^(-t).

Proof. Because W>=3P, the images of cell representatives have high labels

    3b+floor((3s+c_a+3Pv)/W) modH.

The floor increases by at most1 per representative and spans at least three consecutive integer values. Thus each cell has three consecutive legal high child buckets. Their starting offset depends on (a,s), not on b. The low state evolves deterministically independently of the high choice.

Select these three child buckets with equal probabilities at each step, independently of a uniformly sampled positive-composition word. The composition bridge depends only on remaining length/mass, so this independence is legal. Conditional on the complete word, the low states and additive high offsets are fixed. The final t independent ternary choices make the terminal high bucket uniform modulo3^t. There are r-1>=t abstract transitions after the exact first step.

For every low terminal residue s, bucket0 has the representative x=s<P<=L. Thus the legal randomized policy succeeds with probability at least1/H. The normalized Bellman maximum dominates this policy's average, proving the bound. This is a fictitious branching process INSIDE the relaxation, not a randomness assertion about actual Collatz.

Consequently, to certify F_root/N<=2^(-delta*r+o(r)) with delta>0, this template requires at least

    alpha*t >=delta*r-o(r), alpha=log_2(3),

while the hypotheses hold. Fixed or sublinear high precision cannot work merely by adding fixed low digits. If ell grows so P>L, if the cells reach full precision, or if additional relational/reachability restrictions remove the artificial choices, this proof no longer applies. No general impossibility claim about compact symbolic certificates is made.

## Independent review and decision

Both analytic and deterministic reviewers independently derived the hybrid floor, including the three-consecutive-successor property and conditioning/independence requirements. The deterministic reviewer inspected run.py and separately enumerated all cell representatives on four small calibration/compressed cases without importing the principal's implementation. The full48-row panel was run by the principal; it was not independently rerun in full.

The planned question is answered: simply placing high and low digits side by side is insufficient. It repairs a local example but leaves the lost relation between consecutive representatives. Do not enlarge this fixed-precision panel or present singleton recovery as progress toward the exponent.

Retain the exact future-equivalence quotient. Any next certificate proposal must first state what enforces consistency through time and why it does not recreate the artificial ternary branching used in this proof. The current Fourier/count target and count-to-orbit implication remain open/conditional as previously recorded. No new class of genuine Collatz trajectories was excluded in this turn.
