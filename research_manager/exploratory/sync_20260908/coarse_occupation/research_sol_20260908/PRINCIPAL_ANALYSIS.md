# Exploratory analytic audit, 2026-09-08

No sealed stage or numerical depth experiment is executed. XUB and Collatz remain open.

## 1. The displayed domination is sufficient, not an established equivalence

Let W be the product of complex factors, each of modulus at most one. If each disjoint marked block contributes a modulus bound exp(-lambda), pointwise

|W| <= exp(-lambda N_C).

For any fixed conditioning event/law for which these objects are defined,

|E W| <= E |W| <= E exp(-lambda N_C).

The converse is not a general implication. On two equally likely outcomes set W=+1 and W=-1, N_C=0. All conditions above hold (the marked-block implication is vacuous). Then |E W|=0 but E exp(-lambda N_C)=1. This is a logical counterexample, not an actual Collatz-array counterexample.

Consequently the 'equivalent target' wording in the exploratory master findings is unsupported by this domination. Failure of this marked-block sufficient condition would invalidate this certificate of decay, but would not establish failure of the complex kernel estimate or close all critical-bridge approaches. An additional reverse comparison theorem would be needed for equivalence.

## 2. Exact coarse chord occupation identity

Let x_1,...,x_n sum to zero and s_0=0,s_i=sum_(j<=i)x_j. Suppose s_0,...,s_(n-1) are distinct. For the cyclic rotation starting just after vertex k, the partial sums at times 1,...,n correspond exactly to s_l-s_k for all vertices l, with l=k giving the terminal zero. Thus the weak nonnegative occupation N_k is the number of vertices with s_l>=s_k. As k varies it takes each value 1,...,n exactly once. For fixed lambda>0,

(1/n) sum_k exp(-lambda N_k)
= exp(-lambda)*(1-exp(-lambda*n))/(n*(1-exp(-lambda))).

If ties occur, each tie group is assigned its upper rank (in descending order); hence the average is at most this expression. Ties do not automatically preserve the matching lower bound. If entries at times 0,...,n-1 are counted instead, the count is unchanged because both the initial and terminal value are zero.

Application under the endpoint-only composition law: take R=dn, group d raw coordinates, and set x_i=(group total)-K/n. Rotation by d raw coordinates preserves the uniform composition law. If gcd(K,n)=1, partial sums of the centered coarse bridge cannot tie: a tie separated by 0<m<n would require mK/n to be an integer. Averaging the preceding pathwise identity over the invariant law proves the same exact Laplace identity for weak nonnegative coarse chord occupation.

For d=2L and L asymptotic to c log R this identity is of order 1/n=2L/R. This rigorously demonstrates a logarithmic loss for this chord-centered coarse occupation statistic. It is not yet a lower bound for the actual nonlow count.

## 3. Exact transfer gap

At raw time h, write delta=K-beta R and t=h/R. The actual nonlow condition is

S_h-hK/R >= log_2(eta/z0)-delta*t.

The right hand side is a bounded affine function of t, not identically zero. Changing that threshold can change the number of sampled points; the zero-chord rank identity by itself does not bound this change uniformly. In particular, a lower threshold increases occupation and decreases its Laplace transform, so a lower bound for zero-chord occupation cannot simply be transferred. Remainders when 2L does not divide R, rational ties, actual accessible parameter subsequences, and the exact first-passage conditional law also need separate treatment.

Next bounded analytic question: obtain an explicit lower bound for the probability that a composition bridge stays below this affine barrier at every coarse entry except a bounded number. A lower bound c*L/R along an actual accessible sequence, with bounded entry count and the correct conditioning, would contradict the proposed C/R marked-block bound since N_C cannot exceed the nonlow coarse entry count. Such a bound is not established here.

## 4. Independent native-agent audit and stronger exact reductions

The native audit checked sections 2–3 and supplied two strengthenings, rechecked by the principal.

First, write g=gcd(K,n). A tie between vertices separated by m requires n/g to divide m, so every tie group has at most g vertices. Assign ordinary descending ranks 1,...,n inside each tied group. Its weak occupation count is its upper rank, at most g-1 above each assigned rank. If A_n denotes the exact distinct-rank Laplace average in section 2, then pathwise

exp(-lambda*(g-1))*A_n <= rotation average <= A_n.

Thus bounded gcd suffices for the same order 1/n; coprimality is needed only for the exact equality.

Second, for R=2Ln with no remainder, let Delta_top be the gap between the largest and second-largest values among s_0,...,s_(n-1) of the chord-centered coarse bridge (n>=2). Fix B>max(0,log_2(2/eta)). Since delta<0 and z0<2, the actual affine threshold b(t)=log_2(eta/z0)-delta*t is greater than -B throughout [0,1]. On Delta_top>B, rotate to the unique largest vertex. Every other vertex of this rotated bridge is below -B, hence every genuine block entry q=1,...,n-1 is actually low. The initial entry q=0 is left unrestricted.

The gap event is invariant under coarse cyclic rotation. There is at least one successful rotation on it, so cyclic invariance of the endpoint-only composition law gives

P(all genuine noninitial entries low) >= P(Delta_top>B)/n.

Therefore, for any marked count bounded by the number of actual nonlow entries,

E exp(-lambda N_C) >= exp(-lambda)*P(Delta_top>B)/n.

This is a proved reduction, not a proved asymptotic obstruction. A positive uniform lower bound for P(Delta_top>B) on a sufficiently large actual accessible divisible subsequence, together with the correct conditional law, would give an L/R obstruction. No such gap-probability bound or accessible-subsequence/conditioning transfer is established here. This gap question is more focused than the full affine-barrier ballot question.

## 5. Audit of Sol outputs

- rank: finite rank identity correct; native/principal tie bounds strengthen it.
- logic: direction of domination and cancellation counterexample correct.
- grid: missing-law/remainder caveats useful, but its event at q=1,...,n does not constrain q=0. For a grid starting at zero it implies at most one marked block, not zero. Use exp(-lambda) times event probability. Requiring q=n is also unnecessarily restrictive: it is a terminal point, not the start of a full block when R=2Ln. Use genuine starts 1,...,n-1.
- The grid output's uniform-in-all-parameters proposed lower bound is stronger than necessary to refute a uniform upper bound; one actual accessible subsequence would suffice. First-passage law compatibility remains essential.
- rank and logic returned claim-status labels rejected by the runner schema (INVALID_CLAIM_STATUS); the runner retained OPEN. Their public mathematical arguments were manually audited; package byte verification alone does not validate their mathematics.
