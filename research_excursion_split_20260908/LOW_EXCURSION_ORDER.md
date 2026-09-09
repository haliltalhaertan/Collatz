# The boundary-configured low excursion has exact order 1/R

2026-09-08. PROVED using a specified literature theorem and the earlier elementary lower bound. This result concerns one explicit no-mark class, not all no-mark paths.

## Domain and boundary event

Use the actual suffix domain from research_dense_pairs_20260908/DENSE_LOWER_TAIL_PROOF.md:

beta=log_2(3)-1, R=2J+epsilon, epsilon in {0,1}, z_0 in (1,2), delta=K-beta R in (-15-2beta,-13-2beta).

Fix eta in (0,1/2). Choose fixed integers h>=1 and M>=2 with 2(4/9)^h<eta and 2^(-11-M)<eta. Let D prescribe first 2h raw coordinates zero, final complete pair total M, and terminal singleton zero when epsilon=1. The remaining middle has 2n=R-2h-2-epsilon raw coordinates and total K'=K-M. Conditional on D it is uniform on these weak compositions, and

P(D)=(M+1) binom(K-M+2n-1,2n-1)/binom(K+R-1,R-1)

converges, for each parity, to (M+1)*beta^M/(1+beta)^(M+2h+2+epsilon)>0.

The middle's initial and terminal log phases are

x_start=log_2 z_0-2beta h,
x_end=log_2 z_0+delta+beta(2+epsilon)-M.

Both are strictly below log_2 eta by a fixed margin and are bounded uniformly over the actual domain. Let A_low mean that every middle vertex (including its endpoints) has phase below eta. On D intersect A_low there are no white B=1 marks: prefix B=0, middle low, final B=M>=2, singleton unmarked.

## Exact centered iid representation

Realize the middle as iid pairs U_i of geometric raw coordinates of mean beta, conditioned on sum U_i=K'. The reflected increment V_i=2beta-U_i has mean zero, variance sigma^2=2beta(1+beta), and maximal lattice span one. A valid shift is c_lat=2beta-1 in (0,1).

Put x=log_2 eta-x_start, y=log_2 eta-x_end. They stay in a fixed positive bounded interval. The reflected path is x+sum_{i<=q}V_i, and its endpoint compatibility is exact:

y-x=2beta n-K'=n*c_lat+(n-K') in n*c_lat+Z.

No integer rounding of x,y is permissible or necessary.

## Applied external theorem and upper bound

Caravenna–Chaumont, *An invariance principle for random walk bridges conditioned to stay positive*, Electronic Journal of Probability 18 (2013), no. 60, [author PDF](https://fcaraven.github.io/download/papers/carcha2-final.pdf): Hypotheses 2.1–2.2 allow this centered finite-variance shifted lattice; Proposition 4.1, equation (4.5), gives the killed local limit estimate uniformly at endpoints x,y=o(a_n). Here a_n=sigma sqrt(n), and bounded endpoints give bounded ladder-renewal factors. Consequently the weak nonnegative kernel is at most C n^(-3/2). The strict-positive event needed here is a subset, so the same upper bound applies without identifying strict renewal factors.

The free endpoint probability is at least c n^(-1/2), uniformly, by the negative-binomial formula/Stirling (also consistent with source equation (4.1)), because

K'-2beta n=delta+beta(2h+2+epsilon)-M

is bounded. Dividing the strict-positive endpoint mass by this free mass gives

P(A_low | D) <= C'/n.

## Matching lower bound and conclusion

Center the middle at its own chord: s_q=sum_{i<=q}U_i-qK'/n. Cyclic invariance implies that the event s_q<=0 at every interior vertex has probability at least 1/n. Its actual log phase equals the line segment between x_start and x_end plus s_q, so this event lies in A_low. Therefore

1/n <= P(A_low | D) <= C'/n.

Since P(D) is bounded below and n is comparable to R, for all sufficiently large actual arrays, both parities,

c/R <= P(D intersect A_low) <= C/R.

Its contribution to E exp(-lambda N_white) is exactly this probability for every lambda>0, since N_white=0 throughout this event.

This upgrades the earlier lower-bound construction to a TWO-SIDED estimate for the full low-middle event with the specified boundary data. It does not establish P(N_white=0)<=C/R: other boundary configurations, repeated low excursions, and positive near-integer phases remain outside this result. In particular it does not establish the full dense Laplace upper bound, XUB, or Collatz.
