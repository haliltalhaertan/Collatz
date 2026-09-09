# Joint outlier review: valid recovery inequality and a stronger obstruction

2026-09-08. Principal plus two adversarial agents. No paid calls, remote publication, or new orbit exclusion.

## What changed

The previous retained-set argument discarded entire prefix-weight outlier classes. This round produced a valid inequality retaining EVERY weight class, with a conditional offset moment and an explicit good/bad offset split. The independent attack then established that even this stronger certificate cannot improve the existing kappa ceiling. The detailed finite inequality, proof and all-parameter obstruction are in audit_stratified.md.

This is not a negative conclusion based on failed numerical optimization. The obstruction evaluates the formula at the feasible critical prefix density k/m=1/log_2 3, and survives even granting perfect offset information. Hence refining the global offset moment further cannot repair this particular endpoint-cardinality method.

## The substantive proposal and correction

For each exact prefix weight k, the offset moment is bounded by a sampling-without-replacement argument inside the exposed block. The tail bits are never declared independent. The attack agent flagged an important normalization issue: fixing an odd start forces the first parity bit to1. The all-word fixed-weight moment cannot be silently used as the odd-conditioned moment. The accepted correction bounds odd bad words by all bad words, equivalently paying m/k. This has been incorporated.

The principal separately verified the theta=1 specialization using rational arithmetic on2047 actual odd starts and66 weight cells, including the Markov bounds at four thresholds. All checks pass. This finite check does not validate every fractional theta by enumeration; the general range is justified by subadditivity and the symmetric-mean inequality in the proof.

## Why the improved formula still loses the required information

At the critical prefix density, the actual prefix endpoints occupy a sparse part of their allowed range. The tail condition selects another subset of that range. Even if every possible endpoint admitted at most one start, counting every tail-compatible endpoint as if it were attained still overcounts the intersection.

Writing alpha=log_2 3, H=H2(1/alpha), prefix depth br and tail depth(alpha-b)r, the idealized endpoint-cardinality term has exponent at least

    (alpha-b)H+max(2b-alpha,0).

This is >=bH: their difference is (alpha-2b)H for b<=alpha/2 and (2b-alpha)(1-H) for b>=alpha/2. Combining this with the marginal prefix count therefore leaves the certificate's exponent at least bH. The bridge ceiling remains1/H=alpha/h*=1.0526808586, below1.053. This does not imply the actual intersection is large.

## Exact alternative representation, with its cost made explicit

The attack agent supplied an exact recursion for the joint parity-count polynomial over an arithmetic progression. Its state retains the progression slope, offset, length, remaining prefix steps and tail steps. Splitting a progression by parity gives affine child progressions; each odd step contributes a prefix or tail variable. Forty-five cases agreed with independent direct iteration.

It preserves precisely the arithmetic information lost by the marginal counts. But it can split all the way to singleton progressions, so it is currently an exact verifier, not a compressed algorithm or an asymptotic estimate. Do not launch a large enumeration merely because this recursion is available.

## Counterexamples with their correct scope

For odd starts below8, the three-step prefix weights have the full binomial counts1,2,1, yet every next state is even. Thus even the next bit is not conditionally fair in every weight class.

There is an infinite version at prefix weight1: the unique start is (2^m u-1)/3, with u=1 for even m and u=2 for odd m. Its continuation is the deterministic1,2 cycle. Any all-strata fair-word model would require an exponential correction in tail length. However this class contains only ONE start; it cannot disprove a useful theorem on the interior critical weights. The principal retains this limitation explicitly.

## Decision

No new exponent gain beyond prior work was established. Retain the all-strata moment inequality as a valid tool and the progression recursion as an exact verifier. Stop spending effort solely on offset size, height, or separate marginal counts: the displayed ceiling applies even with perfect offset control in that architecture. The unresolved task is a genuine arithmetic intersection estimate for the actual fixed-weight prefix image and the selected tail residue classes. The recursion states that information explicitly; it does not yet bound it.
