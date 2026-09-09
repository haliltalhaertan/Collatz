# Dense pair counts: lower scale and failure of the stronger opportunity tail

2026-09-08. Exploratory analytic continuation. This document concerns the exact overshoot-summed suffix law, not a separately fixed overshoot. No sealed computation or numerical depth experiment is used.

## Definitions and actual domain

Let beta=log_2(3)-1, R=2J+epsilon, epsilon in {0,1}. The raw increments are a uniform weak composition of K into R nonnegative parts. Pair totals are B_j=Y_(2j-1)+Y_(2j), and the phase at pair entry j, indexed from zero, is

z_j=z_0*2^(S_(2j)-2beta*j).

Assume the actual domain z_0 in (1,2) and delta=K-beta R in (-15-2beta,-13-2beta). Fix 0<eta<1/2. Define N_white to count pair entries with B_(j+1)=1 AND dist(z_j,Z)>=eta. Define W to count all white pair entries, regardless of the next pair total. A regular/central opportunity count W_reg may be any subset of those entries, so W_reg<=W.

The direct target F=E exp(-lambda N_white)<=C/R remains OPEN. Two rigorous lower bounds below clarify which stronger statements are impossible.

## 1. A positive-probability boundary configuration

Choose fixed integers h>=1 and M>=2 such that

2(4/9)^h<eta,    2^(-11-M)<eta.

Force the first 2h raw increments to be zero, the final complete pair to have total M, and the terminal singleton to be zero if epsilon=1. Call this event D. The middle has

R'=R-2h-2-epsilon=2n,    K'=K-M.

For sufficiently large R, n>=1 and K'>=0. Conditional on D, the middle is exactly uniform over all R'-part compositions of K'. The last pair has M+1 splits. Therefore

P(D)=(M+1)*binom(K-M+R'-1,R'-1)/binom(K+R-1,R-1).       (1)

Since h,M,epsilon are fixed and K/R->beta uniformly on the actual domain, finite-factorial ratios give

P(D)->(M+1)*beta^M/(1+beta)^(M+2h+2+epsilon)>0.          (2)

The smaller of the two parity limits gives a uniform positive lower bound for all sufficiently large actual arrays.

Let x_start and x_end denote the logarithms base two of the actual phase at the beginning and end of the middle. They satisfy

x_start=log_2 z_0-2beta h<log_2 eta,
x_end=log_2 z_0+delta+beta(2+epsilon)-M
     <-12+beta epsilon-M<-11-M<log_2 eta.                (3)

Write the middle pair totals as U_i and define the endpoint-centered bridge

s_q=sum_(i=1)^q U_i-qK'/n, 0<=q<=n.

The actual middle log-state at entry q is exactly

x_q=(1-q/n)x_start+(q/n)x_end+s_q.                     (4)

The middle law is cyclically invariant. At least one indexed rotation of every centered bridge is rooted at a maximum and has all interior s_q<=0. Thus this nonpositive-excursion event has conditional probability at least 1/n, with ties allowed.

## 2. No-mark paths have probability at least constant/R

On that nonpositive middle excursion, (3)-(4) show every middle pair entry is low: z<eta. Such entries cannot be white. The forced prefix has pair totals 0; the last pair has total M>=2; neither can contribute to N_white. The singleton is not a pair. Therefore N_white=0 on this entire event and

P(N_white=0)>=P(D)/n>=c_eta/R.                         (5)

This holds for all sufficiently large actual arrays and both parities, with c_eta>0. For every fixed lambda>0,

E exp(-lambda N_white)>=P(N_white=0)>=c_eta/R.           (6)

This rules out an o(1/R) uniform upper bound. It is compatible with, and does not prove or refute, the candidate O(1/R) upper bound.

## 3. Exact middle ranks on an actual prime subsequence

Specialize to the actual G first crossing s=1, so r=R, tau=2, z_0=16/9 and K=floor(beta R)-15. Let n run through unbounded primes and choose

R=2n+2h+2,
K'=floor(beta(2n+2h+2))-15-M.

These are actual accessible suffixes for sufficiently large n. They have even parity and exactly n middle pairs after imposing D. Because K'/n->2beta in (1,2), eventually n<K'<2n. Primality gives gcd(K',n)=1.

The n heights s_0,...,s_(n-1) are then distinct: an equality between indices separated by 0<j<n would require jK'/n to be an integer. Define

N_mid=#{0<=q<n:s_q>=0}.

For a fixed path, rotation at vertex k translates all vertex heights by -s_k. Its nonnegative occupation is therefore the descending rank of s_k. The n indexed rotations give exactly the counts 1,...,n. Under the invariant conditional middle law,

P(N_mid=j | D)=1/n,   1<=j<=n.                       (7)

Since the affine term in (4) is strictly below log_2 eta, every actual nonlow middle entry requires s_q>0. In particular every white middle entry requires s_q>0. As s_0=0 is the unique zero height, there are N_mid-1 strictly positive heights. The initial h pair entries can give at most h white opportunities; the last full pair's entry equals the low middle endpoint. Thus, on D,

N_white<=N_mid-1,
W_reg<=W<=h+N_mid-1.                                  (8)

## 4. The stronger logarithmic opportunity-tail target is false

For every integer 0<=m<=n-1, (7)-(8) imply

P(N_white<=m)>=P(D)*(m+1)/n.                           (9)

Fix ANY A>0 and set m_R=floor(A log R-h). Eventually 1<=m_R<=n. On D intersect {N_mid<=m_R},

W_reg<=h+m_R-1<A log R.

Consequently, along this actual prime subsequence,

P(W_reg<A log R)>=P(D)*m_R/n>=c_(eta,A)*log R/R.        (10)

No finite C can make this probability <=C/R uniformly for any fixed A>0. This refutes the stronger helper target in the earlier paired-occupation reduction when W_reg counts a subset of predictable white pair entries with the fixed eta and the stated alignment. Restricting to a regular cone or central region can only reduce W_reg and cannot remove the obstruction. Here R=m=r for the G s=1 suffix, so the original full-length formulation has no scale mismatch.

The direct dense Laplace target is NOT contradicted. Indeed the same rank comparison gives the compatible bound

E exp(-lambda N_white)
>=P(D)*(1-exp(-lambda n))/(n*(1-exp(-lambda))).          (11)

The cumulative mass of the first O(log R) occupation values can be of order log R/R while their exponentially weighted contribution is only of order 1/R. A hard logarithmic threshold loses this distinction.

## Conclusion

Do not try to prove the refuted hard-threshold opportunity estimate. Retain the direct dense exponential-moment question or exploit complex cancellation directly. Positive arithmetic near-resonances remain unresolved. These results do not prove or refute XUB or Collatz and do not authorize canonical state changes.
