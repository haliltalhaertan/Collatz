# Symbolic logarithmic-block theorem for the XUB suffix bridge

Date: 2026-09-07

Status: `[PROVED]` for the exact microcanonical suffix law and long central suffix regime. It does not establish arithmetic whiteness.

## Exact law

Let `R=2J+epsilon`, `epsilon in {0,1}`, be the number of suffix increments and condition their total to be `K`. Pair totals are `B_j=Y_(2j-1)+Y_(2j)`; if `epsilon=1`, let `V` be the final singleton. For any tilt `0<t<1`,

`P_t(B=b)=(b+1)(1-t)^2 t^b`, `P_t(V=v)=(1-t)t^v`.

Conditioning on the total removes the tilt factor exactly and recovers the uniform-composition law. Choose the saddle `t=K/(K+R)`. The asymptotic central-cone statement below assumes `K>=1`; this is automatic for sufficiently long accessible actual suffixes.

Fix `B_0>=1` and define

`W(z)=(1-z)^(-2)`, `U_(B_0)(z)=sum_(b=1)^(B_0)(b+1)z^b`.

Partition a fixed initial set of pairs into `N=floor(J/ell)` disjoint blocks of length `ell`, and let `G` count blocks whose every symbol lies in `{1,...,B_0}`. Then the exact conditional probability generating function is

`E[y^G | T_R=K] = [z^K](W(z)^ell+(y-1)U_(B_0)(z)^ell)^N W(z)^(J-Nell)(1-z)^(-epsilon) / binom(K+R-1,R-1)`.

Under the unconditioned saddle tilt the disjoint block indicators are independent Bernoulli variables with success probability

`pi_(B_0)(t)^ell`, where `pi_(B_0)(t)=sum_(b=1)^(B_0)(b+1)(1-t)^2t^b`.

Writing `mu=N*pi_(B_0)(t)^ell`, Chernoff and the exact tilted endpoint mass give, whenever `K/R` remains in a compact subset of `(0,infinity)`,

`P(G<=mu/2 | T_R=K) <= C sqrt(R) exp(-mu/8)`.

The denominator lower bound is obtained directly from uniform Stirling estimates for

`P_t(T_R=K)=binom(K+R-1,R-1)(1-t)^R t^K`.

## Logarithmic blocks and the sharp fixed-grid threshold

On the actual central arrays, `K=beta R+O(1)` and hence `t=rho+O(1/R)`, with `rho=beta/(1+beta)`. Throughout this section `log` is the natural logarithm, `m` is sufficiently large, `ell=floor(c log m)>=1`, and `delta*m<=R<=C_R*m` for fixed positive `delta,C_R`. Set

`pi_0=pi_(B_0)(rho)>0`.

If

`0<c<c_crit:=1/log(1/pi_0)`,

then `theta=1-c log(1/pi_0)>0`,

`mu asymp m^theta/log m`,

and there exist positive constants `a_1,a_2,a_3`, depending only on the fixed central cone, `B_0,c,delta,C_R`, such that

`P(G<a_1*m^theta/log m | T_R=K) <= a_2 sqrt(m) exp(-a_3*m^theta/log m)`.

The failure probability is smaller than every fixed inverse power of `m`. In particular, the bridge contains more than any fixed multiple of `log m` such disjoint useful blocks with superpolynomially high probability.

If `c>=c_crit`, the probability of even one such block on the fixed disjoint grid tends to zero. After fixing a useful block, its total lies between `ell` and `B_0*ell`, so the remaining endpoint differs from its saddle mean by only `O(log m)=o(sqrt(R))`. Uniform Stirling/local-mass ratios therefore bound the remaining endpoint mass divided by the original endpoint mass by a constant. A union bound gives

`P(G>=1 | T_R=K) <= C*N*pi_(B_0)(t)^ell`.

This tends to zero for `c>c_crit` and is `O(1/log m)` at equality.

## Actual G/H centrality

For the common suffix coordinates,

`R=ell_suffix+1`,

`K=floor(beta*r)-floor(beta*(r+1-ell_suffix))-14`,

and exactly

`-15-2beta < K-beta R < -13-2beta`.

Thus every accessible long suffix automatically lies in the required central regime. Both parities are covered by the singleton factor. Short suffixes, inaccessible `K<0` terms, and a separately fixed overshoot require the seam and endpoint treatments already specified in the first-passage audit.

## Consequence and limit

Every useful block has only positive bounded symbols. For a useful block of length `ell`, either at least one of its `ell` pair-entry states is eta-white, in which case the associated positive symbol gives the common contraction, or all `ell` entry states are eta-black. In the second case the first `ell-1` transitions form a black-to-black run and force `9^(ell-1)` divisibility and the corresponding conductor amplification. The final exit is not silently counted; this is the seam-safe dichotomy.

This theorem proves the symbolic supply of candidate blocks. It does not show that amplified positive resonances or low-state black blocks have total probability `O(1/m)`. XUB remains open.
