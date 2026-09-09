# Compact-height contraction and endpoint-resolved resonance expansion

2026-09-08. Exploratory analytic continuation. Fix beta=log_2(3)-1, lambda>0, and 0<eta<=1/17. No governed stage is reopened.

## 1. Fixed geometric law and endpoint conditioning

Use iid nonnegative geometric raw coordinates with mean beta. The pair distribution is

p_b=(b+1)*beta^b/(1+beta)^(b+2), b>=0.

Its mean is 2beta, variance 2beta(1+beta), and p_1=2beta/(1+beta)^3. Pair state update: z'=(4/9)*2^b*z. Given raw total K over R coordinates, this is exactly the uniform weak-composition law. For K-beta R in a fixed bounded interval, its endpoint probability d_R is asymptotic to [2*pi*R*beta(1+beta)]^(-1/2). Endpoint conditioning must be applied globally; iid independence is not asserted inside the bridge.

## 2. Compact-height contraction [PROVED]

Fix a finite H>=eta. Choose integer L>=1 with 9^(L-1)>=H+eta. The exact word lemma from research_dense_pairs_20260908/EXACT_B1_WORD_LEMMA.md says that an L-long B=1 word has all entries black iff dist(z,9^(L-1)Z)<eta. Therefore every z in [eta,H] has at least one white entry on this word. The inclusive endpoints are valid because blackness is strict.

The word has iid probability p_1^L. Consequently the L-step survival expectation, allowing the path to leave the compact interval inside the block, obeys

E_z exp(-lambda N_[0,L)) <= q_H:=1-(1-exp(-lambda))*p_1^L <1.

Let E_C specify that z_(aL) belongs to [eta,H] at every complete block start a=0,...,m-1. Iterating the positive operator 1_[eta,H] K^L gives

E_z[exp(-lambda N_[0,mL))*1_E_C] <= q_H^m.

This is a JOINT weighted estimate, not an expectation normalized by P(E_C). For R raw steps, m=floor(R/(2L)), discarding leftover killing and applying the single endpoint denominator yields

E_composition[exp(-lambda N_white)*1_E_C]
 <= d_R^(-1) q_H^m
 <= C sqrt(R) exp(-(1-exp(-lambda))*p_1^L floor(R/(2L))).

For fixed H this is exponentially small up to the displayed polynomial factor. This controls even positive near-integer states within that height range; it does not bound the contribution of paths whose block starts leave it.

For H>=1 and the smallest admissible L, L=1+ceil(log_9(H+eta)), and p_1^L is comparable to H^(-gamma), gamma=log(1/p_1)/log 9>0. Thus this particular estimate deteriorates with height. It gives no uniform global contraction independent of H.

## 3. Why unrestricted-height block contraction is false

For arbitrary state z_0=9^m and any nonnegative pair totals, z_j=4^j*2^(B_1+...+B_j)*9^(m-j) is an integer for 0<=j<=m. Hence the first m+1 pair entries are all black, and there is no killing at all through that many pairs. No fixed block length contracts uniformly over all positive starting heights.

This is a statement about the enlarged state space. It is NOT an actual-array counterexample: our starts are in (1,2), and these integer states have not been shown reachable from them. An admissible proof must exploit actual phase structure or retain height-dependent weights.

## 4. Exact resonance expansion [PROVED]

Use x=log_2 z. Define the actual kernel K and a reference kernel T by

K(x;b)=p_b exp(-lambda*1_{b=1}*1_{dist(2^x,Z)>=eta}),
T(x;b)=p_b exp(-lambda*1_{b=1}*1_{2^x>=eta}).

Both change x to x+b-2beta. T kills every nonlow B=1 transition; K omits that killing at positive resonances. Exactly K=T+V, where V permits only b=1 with coefficient

v(x)=(1-exp(-lambda))*p_1*1_{2^x>=eta, dist(2^x,Z)<eta}.

In particular K>=T. A bound on T alone has the wrong inequality direction to upper-bound K. Also T is a SOFT killed kernel, not the hard half-line kernel from the literature.

Let K_n(x,k) and T_n(x,k) be unnormalized masses at pair time n and accumulated total k; K_0=T_0=1_{k=0}. For n>=1, expansion at the first V transition gives the finite identity

K_n(x,k)=T_n(x,k)
 + sum_{j=0}^{n-1} sum_{h=0}^{k-1}
   T_j(x,h) v(x+h-2beta*j)
   K_(n-1-j)(x+h-2beta*j+1-2beta,k-h-1).

Empty sums vanish. This preserves the additive endpoint coordinate exactly.

## 5. A sufficient weighted renewal criterion [CONDITIONAL]

On a domain closed under the intermediate states above, suppose positive weights W_n satisfy T_n<=A W_n, and replacing K on the right of the perturbation sum by W gives a value at most theta W_n, uniformly, for a fixed theta<1. Induction on n gives

K_n <= A/(1-theta) W_n.

Weights O(n^(-3/2)) on target endpoints would deliver the desired joint estimate. Neither the reference bound nor the perturbation condition is proved here. Weights are required at all intermediate heights and endpoint deficits, not just the original starts. An odd terminal singleton requires an additional un-killed geometric convolution with compatible weights.

A small one-step resonance coefficient is insufficient. In the scalar example T=h, V=1-h with 0<h<1, T^n decays exponentially and V<1, but K^n=1. The accumulated mass sum_{j>=0}T^j V equals one. This is an abstract proof-principle counterexample, not an actual phase-law claim.

## Outcome

Compact block-start paths are controlled. Positive resonances can be isolated in an exact endpoint-resolved expansion. Global dense C/R, the reference soft-kernel estimate, and the strict weighted resonance condition remain OPEN. The earlier no-mark lower bound rules out any global o(1/R) claim.
