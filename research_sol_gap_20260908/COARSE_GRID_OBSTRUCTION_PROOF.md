# Analytic obstruction for one admissible fixed grid

Date: 2026-09-08. Exploratory mathematical result; no canonical promotion or sealed execution.

## Claim and precise scope

Let beta=log_2(3)-1. Choose the bounded-positive alphabet cutoff B_0=2 and block length L_R=floor(c log R), where c=6/5 and log is natural. Use the origin-aligned disjoint grid of blocks of L_R pairs, with genuine entry indices j=qL_R, q=0,...,floor(R/(2L_R))-1. Fix eta>0 and lambda>0 independently of R.

There is a sequence of actual accessible G suffixes with R=2L_R n, K=floor(beta R)-15, and z_0=2^(2-2beta), such that every marked count N_C assigning at most one mark to each grid block and requiring a nonlow entry z_j>=eta satisfies

E[exp(-lambda N_C) | the restarted suffix total K] >= c_*(eta,lambda) L_R/R

for all sufficiently large members of this sequence, with c_*>0. In particular no finite uniform C can give E exp(-lambda N_C)<=C/R on this grid. The useful-positive-word and nonresonance requirements may delete more marked blocks and cannot invalidate this lower bound.

The choice c=6/5 is strictly BELOW the symbolic-supply threshold for B_0=2. This theorem therefore refutes a C/R marked-block claim that includes this admissible parameter choice. It does not refute an existential claim that some smaller c may work; nor does it refute other grids, the complex suffix bound, XUB, or Collatz.

## 1. Exact actual suffix law and accessibility

In the first-crossing representation, fix a crossing time s and any allowed pre-crossing prefix of total J. If c_s=floor(beta s-a)+1, the crossing increment is Y_s=c_s-J+e, e>=0. At fixed full total N, the transformed continuation

(e,Y_(s+1),...,Y_m)

is in bijection with ALL weak compositions of K=N-c_s into R=m-s+1 parts. Each continuation has the same geometric probability weight. The pre-crossing condition puts no later path restriction on this transformed suffix. The fictitious initial phase is removed by q(a'_s)^(-1), a unit-modulus factor. Thus the positive law bounding the normalized free suffix kernel is exactly the endpoint-only uniform composition law. This statement sums overshoot e; it would not hold for a separately fixed e.

For the actual G family, choose the accessible first crossing s=1 and r=R. The recorded exact formulas give N=floor(beta R)-8, c_1=6+floor(2beta)=7, tau=s+1=2, and

K=floor(beta R)-15,
a'=beta+1-{2beta}=2-beta,
z_0=2^(a'-beta)=2^(2-2beta).

For large R, K>=0, so this suffix is accessible: there is no pre-crossing increment to restrict, and a crossing increment 7+e followed by any remaining composition realizes it. Its endpoint defect is delta=K-beta R=-15-{beta R}, and also equals the general formula -14-2beta+{2beta}-{beta R}. It lies in the recorded actual interval (-15-2beta,-13-2beta).

## 2. Exact equal-block law and cyclic maximum identity

Set d=2L and R=dn. Let U_i be the total in raw coordinates (i-1)d+1,...,id. Under uniform compositions the mass of a coarse vector is

P(U=u)= product_(i=1)^n w_d(u_i) / binom(K+R-1,R-1),
w_d(t)=binom(t+d-1,d-1), sum_i u_i=K.

It is invariant under cyclic rotation. Put mu=K/n and s_j=sum_(i<=j)u_i-j mu for j=0,...,n, with s_0=s_n=0. Let Delta be the largest minus second-largest value among s_0,...,s_(n-1), with Delta=0 for a tied maximum. For B>0 let

H_B={s_j<-B for every 1<=j<n}.

For any fixed vector, exactly one cyclic rotation satisfies H_B if Delta>B, and none otherwise. Indeed the rotated vertex heights are precisely s_l-s_k, and the base must be the unique maximum separated by more than B. Consequently

P(H_B)=P(Delta>B)/n.                                      (1)

This requires no distinctness or coprimality hypothesis.

## 3. A weighted injection creating a separated maximum

Fix a=1/1000 and an integer M>B. Define the invariant event G={min_i U_i>=ad}, and E_0={s_j<=0 for all 1<=j<n}. Rotating at a maximum always gives E_0, so

P(E_0 intersect G)>=P(G)/n.                              (2)

For every vector in E_0 intersect G, for sufficiently large d apply

u_1 -> u_1-M,   u_n -> u_n+M,

leaving all other coordinates fixed. The transformation is injective on these rooted vectors. Each genuine interior height decreases exactly M, so its image belongs to H_B. The recipient weight does not decrease, and the donor weight ratio is

w_d(u_1-M)/w_d(u_1)
= product_(r=0)^(M-1) (u_1-r)/(u_1+d-1-r)
>= [(ad-M+1)/(ad+d-1)]^M =: gamma_d.

For the last inequality use (u_1-r)/(u_1+d-1-r)>= (u_1-M+1)/(u_1+d-1), followed by monotonicity in u_1>=ad. Since M is fixed, gamma_d -> [a/(1+a)]^M>0. Therefore (1) and (2) give

P(Delta>B)=nP(H_B)>=gamma_d P(G).                        (3)

## 4. The all-block lower bound event has probability tending to one

The exact one-group marginal, with falling factorial notation (x)_k, is

P(U_1=t)=w_d(t) (K)_t (R-1)_d / (K+R-1)_(t+d).

For t<=ad and d=O(log R), K/R=beta+O(1/R), taking logarithms of these finite products shows, uniformly in t,

P(U_1=t)=w_d(t) beta_R^t/(1+beta_R)^(t+d) * exp(O(d^2/R)),
beta_R=K/R.

This follows by expanding each log(1-j/K), log(1-j/R), and log(1-j/(K+R)) with j=O(d); sums of errors are O(d^2/R). The displayed comparison is to a sum of d independent geometric variables of mean beta_R, used only as an exact comparison distribution.

For a<beta_R, exponential Markov applied to that negative-binomial comparison gives

P(U_1<ad)<= exp[-d I_(beta_R)(a)+O(d^2/R)],
I_b(a)=a log(a/b)+(1+a)log((1+b)/(1+a)).

Indeed its negative exponential moment is [(1+b)-b exp(-theta)]^(-d); optimizing at exp(-theta)=a(1+b)/(b(1+a)) yields the rate above. Continuity and beta_R=beta+O(1/R) give I_(beta_R)(a)=I_beta(a)+O(1/R).

No independence of the conditioned blocks is needed for the union bound

P(G^c)<= n exp[-d I_beta(a)+O(d^2/R)].                   (4)

When d=2 floor(c log R), log n~log R and d/log n->2c. For our constants, 2c I_beta(a)>1, proved below. Thus the right hand side in (4) tends to zero. Combining with (3) gives a fixed p_*>0 such that P(Delta>B)>=p_* for all sufficiently large members of the divisible sequence.

## 5. Certified constant inequalities; no fitted or simulated input

We use only 58/100<beta<59/100, equivalent to the exact integer inequalities 2^158<3^100<2^159. For a=1/1000,

a log(a/beta)>-7/1000,
log(1+beta)>58/129,
log(1+a)<=1/1000.

The first follows from beta/a<590<exp(7); the middle follows from log(1+x)>=2x/(2+x) and beta>58/100. Therefore

I_beta(a)>-7/1000+(1001/1000)(58/129-1/1000)>11/25>5/12.

Hence 2c I_beta(a)>(12/5)(11/25)=132/125>1.

For the symbolic supply, rho=beta/(1+beta) lies between 29/79 and 59/159. With B_0=2,

pi_2=(1-rho)^2(2rho+3rho^2)
> (100/159)^2 [2(29/79)+3(29/79)^2] >4/9.

The positive exponential series gives

exp(5/6)>1+5/6+(5/6)^2/2+(5/6)^3/6>9/4.

Thus log(1/pi_2)<log(9/4)<5/6, and c log(1/pi_2)<1. Our c is strictly admissible for the recorded symbolic theorem, even though the marked occupation claim fails on this grid.

## 6. Divisibility and transfer to the actual low threshold

For positive integers l tending to infinity set

R_l=2l ceil(exp(l/c)/(2l)).

Then exp(l/c)<=R_l<exp(l/c)+2l, so l<=c log R_l<l+1 for all sufficiently large l. Hence L_(R_l)=l and R_l=2L_(R_l)n_l exactly. Choose the actual G suffix of section 1 for each R_l. This supplies a genuine accessible subsequence, not independently selected continuum endpoints.

At the block entry j=qL (raw time dq), actual nonlow status is

s_q >= b(q/n),
b(t)=log_2(eta/z_0)-delta t.

Since delta<0 and z_0<2, choose fixed B>max(0,log_2(2/eta)); then b(t)>-B for every t in [0,1]. The event H_B makes all genuine noninitial entries q=1,...,n-1 low. Only q=0 may be marked, so N_C<=1 on H_B. Using (1) and the gap lower bound,

E exp(-lambda N_C)>= exp(-lambda) P(H_B)
>= exp(-lambda) p_*/n
=2 exp(-lambda) p_* L_R/R.

As L_R tends to infinity, this contradicts any fixed C/R upper bound for this parameter choice. The terminal q=n is not a genuine block entry and has not been included in H_B.

## Scientific interpretation

The proof establishes a parameter-qualified counterexample sequence for the coarse marked-block sufficient condition. It does not assert that sparse symbolic blocks do not occur: their unconditional abundance remains compatible with rare paths of probability order L_R/R having at most one NONLOW entry. It also does not assert failure of the absolute complex expectation. Taking absolute values before expectation discards phase cancellation, so failure of this Laplace certificate is not a converse theorem about the complex kernel.

The next decision is whether to reformulate the helper lemma using a smaller c or a different counting scheme, or return to direct complex cancellation. This artifact does not dispatch a sealed stage or change canonical research state.
