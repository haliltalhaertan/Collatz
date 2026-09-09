# Direct intersection round: exact state merging and a lookahead limitation

2026-09-08. Principal and two adversarial agents. No paid calls or asymptotic orbit exclusion.

## A genuine finite algorithm improvement

For the shortcut map H, count odd starts in an initial interval whose first A parity bits have weight r. After i>=1 steps, a prefix cylinder is represented by an arithmetic progression

    3^k*j+b, 0<=j<N,

where k is its already observed parity weight. Its next R=A-i bits depend only on these values modulo2^R. Hence states with identical

    (k, b mod2^R, N)

may be merged, adding their multiplicities. The slope is determined by k. Distinct original cylinders are disjoint, so coinciding future states do not create double counting. The residue representative need not be an actual positive intermediate value; only its remaining parity behavior is used.

Transition proof: the slope a=3^k is odd. Split j=2h+e with e in{0,1}; the child lengths are ceil(N/2), floor(N/2). Put v=b+a*e. If v is even, the child progression is a*h+v/2 with unchanged k. If v is odd, it is3a*h+(3v+1)/2 with k increased by1. Reduce the child offset modulo2^(R-1). Changing b by a multiple of2^R changes its child offset by a multiple of2^(R-1), so the merge is exact. Zero-length children are discarded. N=1 naturally has just one child.

Initially the odd starts form2j+1 with length N0; the forced odd step gives3j+2, k=1. For a full dyadic initial interval x<2^m, lengths at depth i<=m are2^(m-i). For arbitrary initial intervals, there are at most two possible lengths at each depth (floor/ceiling of N0/2^(i-1)), so N must be retained in the state key.

The number of states at depth i is bounded by

    min(2^(i-1), 2(i+1)*2^(A-i)),

and also by N0. Thus the total arithmetic work is at most polynomial(A,log X)*min(N0,2^(A/2)), with a corresponding peak-state bound. This is a provable improvement over scanning all2^m starts when A<2m; it remains exponential. It is not a bound on the value of the counted coefficient and therefore does not prove the research target.

The attack agent independently checked every transition and the multiplicity interpretation. Its separate2^t-offset distinguishability result is consistent: that statement concerns fixed-length full-tail distributions before using the simultaneous decline in remaining precision. It is not an impossibility theorem for this dynamic program.

## Exact short lookahead cannot improve the old exponent

Let m=ceil(log_2 X), t=A-m. A certificate that evaluates h actual tail steps and treats the remaining t-h bits as arbitrary accepts exactly those starts with

    r-(t-h)<=K_(m+h)(x)<=r.

Call its count C_h(X). It is an upper bound for the exact parity-weight count and decreases with h. Nevertheless, for full dyadic x<2^m every prefix weight

    r-t+h<=k<=r-h

is accepted regardless of the observed h bits. Thus

    C_h(2^m)>=sum_(k=max(1,r-t+h)..min(m,r-h)) binom(m-1,k-1).

The audit agent strengthened the argument to arbitrary INITIAL X: the half interval x<2^(m-1) lies inside x<X. Expose its m-1 bits and then h+1 additional bits. This gives

    C_h(X)>=sum_(k=max(1,r-t+h)..min(m-1,r-h-1)) binom(m-2,k-1).

For A=alpha*r+O(1), m=br+o(r),0<b<alpha, and h=o(r), this lower bound and the exposed-prefix upper bound have the SAME exponent:

    b,                                  b<=2(alpha-1),
    b H2((alpha-1)/b),                   b>2(alpha-1).

Thus bounded or sublinear exact lookahead cannot improve this certificate's asymptotic exponent, regardless of the actual observed arithmetic. This is a limitation of exact-lookahead followed by arbitrary continuation, not a universal computational lower bound.

For b1.2,kappa1.053, solving H2(p)=1/kappa with p>.5 gives p≈.63130137836. The forced-acceptance lower bound implies that this particular strategy needs

    h/r> b*p-(1-alpha+b)≈.14252415475

before it could meet the strict desired exponent. This is approximately37.02% of the tail length(alpha-b)r. It is a necessary condition, not a guarantee of success. The exact merged-state algorithm above preserves the whole remaining continuation and is not restricted to this lookahead certificate.

## Checks and limits

check_lookahead.py checks monotonicity and the forced-acceptance inequality on three complete dyadic panels. For r16,A25,m20, successive lookahead certificates are260984,212925,167012,123519,81900,41142; the last is the exact count. These are counts on x<2^20, not the original smaller canonical endpoint interval. Finite decreases do not contradict the sublinear-lookahead exponent theorem.

The necessary-lookahead root is a numerical diagnostic with a symbolic inequality behind it.

The implemented modular dynamic program in audit_dp.py passed60 full-interval and215 partial-interval comparisons against direct iteration. It also reproduced F=10 and F=140 for the prior rational canonical-start thresholds at r10,A15,L256 and4096. These are F counts; equality to Q in these two examples must not be assumed in general.

The principal independently compared the ENTIRE joint distribution for m20,t5 with direct iteration over524288 odd starts. All105 nonempty joint cells agreed, including weight16 count41142. The dynamic program used5617 peak states and26357 summed prefix states. Measured in that single local run: dynamic program0.0382868 seconds, direct iteration2.1320156 seconds, about56 times faster. This is a reproducible local diagnostic, not a hardware-independent speed claim. PRINCIPAL_CHECK.json records it. At depth m the implementation evaluates each merged residue's remaining tail directly, which contributes a polynomial time factor and preserves the stated complexity bound.

No large search is justified solely by availability of this algorithm.

## Research consequence

This round produces a practical exact intersection verifier and a precise reason that a few extra observed bits cannot supply the missing exponent. It does not establish a distribution theorem. Future count certificates must exploit structure in the merged states rather than their total number, or otherwise control actual intersections without discarding the needed offset information.
