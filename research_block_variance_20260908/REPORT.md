# Block variance: exact identities, a sufficient target, and failed shortcuts

2026-09-08. Principal and two adversarial agents. No paid calls, publication, or new orbit exclusion.

## Main mathematical output

Let q=2^t translated blocks have exact target counts G(a), mean B, and population variance V=q^(-1)sum_a(G(a)-B)^2. The sharp deterministic estimate is

    |G(0)-B|<=sqrt((q-1)V).

Proof: the other q-1 deviations sum to minus the origin deviation. Their squared sum is at least the origin squared deviation divided by q-1. Equality occurs when all non-origin deviations are equal.

For critical A=alpha*r+O(1), m=br+o(r), write tau=alpha-b and gamma0=h*+b-alpha. Then B=2^(gamma0*r+o(r)), q=2^(tau*r+o(r)). A variance bound with exponent nu gives an origin count exponent at most max(gamma0,(tau+nu)/2). At b1.2,kappa1.053, a sufficient strict target is

    nu < 2b/kappa-tau = approximately1.89423978.

Equivalently normalized variance V/B^2 must decay at a rate greater than tau-2lambda≈0.347122996 for the previously permitted loss lambda. Merely tending to zero is insufficient. On the other hand V<=poly(r)*B would already give the IDEAL count exponent for b>=alpha-h*/2≈0.83214056. Therefore the pointwise square-root loss is not by itself a reason to reject this route. None of these variance estimates has been proved for actual growing Collatz panels.

## Exact finite measurements and a validation example

The first panel fixed r10,12,14 before execution, and evaluated ALL translated blocks. An additional r16 case was used to check the candidate V<=B. Exact results:

|r|blocks|mean B|variance V|V/B approximately|origin G0|max block|
|---|---:|---:|---:|---:|---:|---:|
|10|8|250.25|19.1875|0.07667|250|258|
|12|16|1989|1598.75|0.80380|1967|2062|
|14|32|6359.0625|1616.87109375|0.25426|6360|6438|
|16|32|40859.5|18903.3125|0.46264|41142|41203|

run.py/RESULT.json preserve the fixed panel; HOLDOUT.json preserves the extra check. The first two rows exactly reproduce the prior independent direct-iteration block controls. The sharp inequality also yields integer uniform certificates262,2144,6583 for the first three rows. These are finite bounds, not a new asymptotic count estimate. Normalized variance is not monotone in these examples.

## The simplest variance conjecture is false

The attack agent searched the bounded grid A2..14,1<=m<A,1<=r<=A (910 cases) and found71 violations of V<=B. A counterexample lies on the intended critical parameter rule itself:

    r=5, A=7=floor(alpha*r), m=6=ceil(1.2*r), t=1,
    G=(4,11), B=15/2, V=49/4, V/B=49/30>1.

The principal independently reproduced these two counts by ordinary shortcut iteration. This disproves the literal all-r constant-one inequality. It does NOT disprove an eventual version, V<=C B, a subexponential factor, or the much weaker sufficient exponent target above. We do not introduce a new numerical constant merely to repair the finite failure.

The attack agent also constructed synthetic nonnegative integer block counts with the exact total and block capacity, a large origin spike, and exponentially vanishing relative variance. These are not asserted to be Collatz-realizable. They show that the quantitative rate in the variance-to-origin step is necessary for an argument using only that information.

## What must actually be estimated

Let P_k(z) count actual odd prefixes h<2^m with first-m parity weight k and H^m(h)=z moduloq. Let T_j(z) indicate that z has tail parity weight j over t steps. For unnormalized Fourier transforms,

    hat G(eta)=sum_k hat T_(r-k)(3^(-k)eta)*hat P_k(-3^(-k)eta),
    V=q^(-2)*sum_(eta!=0)|hat G(eta)|^2.

The principal checked this identity independently against the r10 block counts: maximum floating-point discrepancy was below9e-13 and spectral variance agreed with the exact rational307/16. This numerical check validates normalization and signs; the all-length identity follows by a finite change of variable and Parseval. The k-dependent frequency permutations and cross terms must remain in the expression.

Equivalently V is the sum of covariances of the tail-acceptance indicators associated to actual prefixes. Same-prefix diagonal terms sum to at most B. The uncontrolled part consists of DIFFERENT prefixes. Ignoring those off-diagonal terms is precisely the invalid step that would purport to prove V<=B.

For prefix weights k,l and endpoints z,z', their pair correlation is the average of

    T_(r-k)(u)*T_(r-l)(3^(l-k)u+z'-3^(l-k)z)

over u moduloq. The audit agent showed that the 2-adic valuation of the slope difference alone cannot give pointwise independence: explicit affine pairs can have much larger correlations than the product baseline. Their frequency among the ACTUAL prefix offsets remains to be controlled. The precise missing statement is an averaged bound over those real prefix pairs, not a bound for every arbitrary affine offset.

## Decision

Retain variance as a potentially sufficient route: its required exponent is explicit and is weaker than exact Poisson-scale behavior. Reject the universal constant-one guess and any argument dropping coherent pair terms. Further work must address actual off-diagonal correlations with multiplicities preserved. Additional finite rows alone will not certify their asymptotic bound.
