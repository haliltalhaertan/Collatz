# The origin-grid obstruction holds for every fixed logarithmic coefficient

2026-09-08. Exploratory analytic continuation of research_sol_gap_20260908/COARSE_GRID_OBSTRUCTION_PROOF.md. No sealed computation or canonical state change.

## Statement

Fix any c>0, eta>0 and lambda>0. Let L_R=floor(c log R), with natural logarithm, and take the origin-aligned disjoint grid of blocks of L_R pairs. There is an unbounded sequence of actual accessible overshoot-summed G suffixes for which R=2L_R n and

E exp(-lambda N_C) >= A(c,eta,lambda) L_R/R,

with A>0 independent of R, whenever N_C assigns at most one mark to each grid block and a mark requires its entry state to satisfy z>=eta. Additional bounded-positive-word or nonresonance requirements only delete marks and preserve the lower bound.

Therefore, for EVERY fixed c>0, this origin-grid marked count cannot satisfy a uniform C/R Laplace upper bound on the actual arrays. In particular, decreasing c within the symbolically admissible range does not repair the original helper lemma. This statement does not assert failure of the complex suffix expectation, XUB, Collatz, or all other counting schemes.

## 1. Exact law, centered bridge, and genuine entries

Use the actual G first crossing s=1, r=R. The source first-passage representation gives tau=2, c_1=7, full total floor(beta R)-8, and restarted total

K=floor(beta R)-15, beta=log_2(3)-1.

The transformed suffix consists of the nonnegative crossing overshoot followed by the true future increments. Summing the overshoot gives a bijection to all weak R-part compositions of K with equal geometric probability weights. The fictitious initial phase is removed by a unit-modulus reciprocal; it puts no further restriction on this positive suffix law. The suffix is accessible for every sufficiently large R since K>=0. These facts were derived from the original first-passage formula and independently audited in the preceding artifact.

For d=2L and R=dn define U_i as the sum of raw coordinates (i-1)d+1,...,id. The exact mass function is

p(u)=Z^(-1) product_i w_d(u_i),
w_d(t)=binom(t+d-1,d-1),
Z=binom(K+R-1,R-1), sum_i u_i=K.

It is invariant under coarse cyclic rotations. Write beta_R=K/R, mu=K/n=d beta_R and

s_j=sum_(i<=j)U_i-j mu, 0<=j<=n,

so s_0=s_n=0. Define

E_0={s_j<=0 for 1<=j<n},
H_B={s_j<-B for 1<=j<n}.

Genuine entries are q=0,...,n-1; the terminal vertex n is not an entry. Let Delta be the largest minus second-largest height among the n vertices s_0,...,s_(n-1), with zero for a tied maximum. On every path exactly one indexed cyclic rotation belongs to H_B if Delta>B, and none otherwise. Thus P(H_B)=P(Delta>B)/n, with no coprimality assumption. Only the simpler maximum-rooting inequality is needed below.

## 2. Local windows replace the global single-block minimum

Choose once and for all a in (0,beta), for example a=1/1000, and define

I_beta(a)=a log(a/beta)+(1+a)log((1+beta)/(1+a))>0.

Fix an integer k with 2ck I_beta(a)>1. This k depends on fixed c, not on R. Eventually n>k. Let

G_k={every cyclic window of k consecutive coarse groups has total >=a k d}.

This event is invariant under cyclic rotation. Each window, including a wrapping window, comprises kd DISTINCT raw coordinates when n>k. Uniform compositions are invariant under every permutation of raw coordinates, so each window has the exact kd-coordinate marginal.

For m=kd and 0<=t<=am the exact marginal is

P(T_m=t)=binom(t+m-1,m-1) (K)_t (R-1)_m / (K+R-1)_(t+m),

where (x)_j denotes a falling factorial. Uniformly in this range, with m=O(log R), comparing each finite product to its leading power gives

P(T_m=t)
=binom(t+m-1,m-1) beta_R^t/(1+beta_R)^(t+m) exp(O(m^2/R)).

The logarithmic error is uniform because there are O(m) factors, each with log correction O(m/R); beta_R stays in a fixed positive compact interval. The comparison distribution is a sum of m geometric variables of mean beta_R. Its negative exponential moment is [(1+beta_R)-beta_R exp(-theta)]^(-m). Optimizing exponential Markov at exp(-theta)=a(1+beta_R)/(beta_R(1+a)) yields

P(T_m<am)<=exp[-m I_beta(a)+O(m^2/R)],

using beta_R=beta+O(1/R). A union bound over the n windows therefore gives

P(G_k^c)<=n exp[-kd I_beta(a)+O((kd)^2/R)] ->0.           (1)

Indeed d/log R->2c, log n~log R, and 2ck I_beta(a)>1. Independence of overlapping windows is neither used nor claimed.

Every zero-sum centered bridge has at least one indexed rotation rooted at a maximum and hence in E_0. Since G_k is invariant,

P(E_0 intersect G_k)>=P(G_k)/n.                         (2)

## 3. Repair with at most k preimages

Fix B>max(0,log_2(2/eta)) and an integer M>B. On E_0 intersect G_k, the first k groups have total at least akd, so some group among them has U_j>=ad. Choose the first such j, necessarily j<=k<n, and map

U_j -> U_j-M,  U_n -> U_n+M,

leaving every other group unchanged. For sufficiently large R, ad>=M, so this map stays in nonnegative compositions and preserves K.

For 1<=i<j, every preceding group has U_i<ad. Therefore

s_i<i(ad-mu)=-i d(beta_R-a)<-B

for large R, since d tends to infinity and beta_R-a tends to beta-a>0. These early heights remain unchanged by the map. Every height with j<=i<n decreases by M from a value <=0 and becomes <=-M<-B. Thus EVERY image lies in H_B.

The recipient factor w_d(U_n+M)/w_d(U_n) is at least one. The donor factor satisfies

w_d(U_j-M)/w_d(U_j)
=product_(r=0)^(M-1)(U_j-r)/(U_j+d-1-r)
>= [(ad-M+1)/(ad+d-1)]^M =gamma_d,

where gamma_d -> gamma=[a/(1+a)]^M>0. Consequently p(F(u))>=gamma_d p(u).

The map need not be injective; its multiplicity is uniformly bounded by k. Given an output v and a possible j in {1,...,k}, its only possible preimage is recovered by adding M at j and subtracting M at n. Failure of the source event or first-donor rule can only reduce the number of valid preimages. Summing exact probability weights gives

gamma_d P(E_0 intersect G_k)
<=sum_(u in E_0 intersect G_k) p(F(u))
<=k P(H_B).

Combining with (1) and (2),

P(H_B)>=gamma_d P(G_k)/(k n).                           (3)

For sufficiently large R, gamma_d>=gamma/2 and P(G_k)>=1/2, giving P(H_B)>=gamma/(4kn). Equivalently, P(Delta>B)>=gamma/(4k)>0. This is precisely the step that removes the prior restriction to large c.

## 4. Actual threshold and divisible accessible sequence

For the G sequence above,

delta=K-beta R=-15-{beta R}<0,
z_0=2^(2-2beta) in (1,2).

At coarse entry q (raw time dq), actual nonlow status is

s_q >= b(q/n), b(t)=log_2(eta/z_0)-delta t.

Our fixed B gives b(t)>-B throughout [0,1]. Thus H_B makes every genuine noninitial entry low. At most the initial block can be marked: N_C<=1 on H_B. From (3),

E exp(-lambda N_C)>=exp(-lambda)P(H_B)
>=exp(-lambda)gamma/(4kn)
=exp(-lambda)gamma L_R/(2kR).                           (4)

To ensure exact divisibility without changing the block rule, for each sufficiently large integer l set

R_l=2l ceil(exp(l/c)/(2l)).

Then exp(l/c)<=R_l<exp(l/c)+2l, so l<=c log R_l<l+1 eventually. Hence L_(R_l)=l and R_l=2L_(R_l)n_l. Selecting r=R_l and s=1 gives actual accessible suffixes, not independently chosen endpoints. The constants in (4) are fixed on this sequence, while L_(R_l) tends to infinity. This disproves a uniform C/R bound for every fixed c>0 on the specified origin grid.

## Interpretation and limits

This replaces the earlier unresolved small-c question: taking a smaller positive constant in a logarithmic block length does not repair this origin-aligned helper lemma. The finite-maximum-gap argument is entirely discrete and handles ties; no Brownian approximation or ballot theorem is assumed. The probability comparison uses exact finite products with a controlled uniform error, not an independence approximation under endpoint conditioning.

For c below a chosen alphabet's symbolic threshold, abundant useful words remain possible; the rare low-entry paths proved here still prevent the desired positive Laplace bound. This does not forbid phase cancellation in the complex kernel. No assertion is made for a separately fixed overshoot, arbitrary adaptive grids, counts that include interior opportunities, or a varying c=c_R tending to zero. Such variants require their own analysis.
