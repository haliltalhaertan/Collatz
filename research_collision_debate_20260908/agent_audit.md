# Independent arithmetic audit and binary stopping-time reformulation

2026-09-08. Read-only audit of prior research, with this separate note. No paid calls. No global counting estimate established.

## Local formulas

The single-adjacent-transfer difference, its 3-adic valuation, and the iff divisibility by 2*3^i are correct. The exact integer numerator injectivity proof at fixed length and total is also correct: the first unequal cumulative sum gives the unique least 2-adic valuation in the difference. Neither fact bounds the sizes of modular fibers. The minimum-3-adic-valuation tie criterion is necessary, not sufficient; repeated higher cancellation remains the full modular equation.

## Positivity is automatic, final oddness is not

Write q=3^r, A=sum a_i, B_r=3 B_(r-1)+2^S_(r-1), and n=M(w) in [0,q). Since M is a 3-adic unit, n>=1. The congruence 2^A n-B_r=0 mod q gives

    y=(2^a_r n-1)/3 in Z,
    2^S_(r-1)y-B_(r-1)=(2^A n-B_r)/3 =0 mod 3^(r-1).

Starting from positive n, y is a positive integer. Repeat backwards: all predecessor values are positive odd integers. Thus x=(2^A n-B_r)/q is always positive and odd. It is also less than 2^A. Requiring a positive start removes no words.

The canonical n can be even. In that case the first r-1 valuations are exact, but a_r is only a partial division in the last odd step. If n is odd all r valuations are exact. This distinction affects interpretation of genuine odd-only trajectories, not the original upper count Q over all words.

For fixed r,A distinct words have distinct x: the first r-1 genuine valuations are determined by x, and their sum together with A determines the last a_r. In particular Q(L)<=#{positive odd x < 2^A L/q}; this has exponent b on a critical mass band and misses the desired saving alpha-h_*.

## Quantitative dual interval reduction

Let S_(r,A) be the canonical start set, F(T)=#{x in S_(r,A):x<T}, c=2^A/q, X=cL. For A>=r,

    B <= 3^(r-1)*(1+2^(A-r+1))-2^A,
    B/q <= 2^(A-r)-c = D.

The first inequality follows by maximizing every positive cumulative sum: S_i<=A-r+i for i>=1. Since x=cM-B/q,

    F(X-D) <= Q(L) <= F(X),
    0 <= F(X)-Q(L) <= ceil(D/2)+1.

On any fixed band A=alpha*r+O(1), the additive error has exponent alpha-1. Consequently a target exponent gamma>alpha-1 is equivalent for these two counts, uniformly on the required band. For gamma=h_*+b-alpha this requires b>2alpha-1-h_*. The constants c vary only by bounded factors on a fixed band; the threshold is exactly X=cL, not silently L.

## Noncircular description of the start set

For an ordinary positive odd x, let S_j(x) be the accumulated genuine odd-only valuations through j steps, with S_0=0. Then

    S_(r,A) = {odd 1<=x<2^A : S_(r-1)(x)<A<=S_r(x)}.

The right side assigns the first r-1 exact valuations and last partial valuation A-S_(r-1). Its residue class modulo 2^A is the word's canonical start; both representatives lie in [1,2^A), so they are equal.

Equivalently define the shortcut map H(x)=x/2 for even x, and H(x)=(3x+1)/2 for odd x. The set consists of odd x<2^A for which the states x,H(x),...,H^(A-1)(x) contain exactly r odd values. Indeed the odd occurrence times are 0,S_1,S_2,... . The full-period count is binom(A-1,r-1), but the proposed research bound is a short-initial-interval large-deviation count for this binary coding. Full-period binomial uniformity does not establish the required short-interval estimate.

## Merger objection

Removing a shared tail of two genuinely merging trajectories produces prefix pairs with equal time, mass, and actual endpoint. Counting those prefixes still requires an inverse-tree multiplicity bound jointly with endpoint location; treating prefix multiplicity and the allowed tail as independent would discard their compatibility. The supplied r4 merger core has inverse starting points differing by 2, so one cannot simply concatenate it into a binary tree: both inverse points cannot occupy its same required residue class modulo81. Neither exponential multiplicity nor subexponential multiplicity follows from that example alone.

The useful surviving result is the exact dual interval reformulation. It exposes rather than solves the missing quantitative estimate.

## A quantitative baseline from exposed parity bits

Let m=ceil(log2 X)<A. Enlarge the start interval to all odd x<2^m. The first m parity bits run bijectively over binary words beginning with1. If the first A bits contain r ones, the first m must contain at least r-(A-m) ones (and at most r). Therefore

    F(X) <= sum_(k=max(1,r-A+m))^min(m,r) binom(m-1,k-1).

On a critical band, m=br+O(1). For b>2(alpha-1), this gives exponent

    gamma_exposed(b)=b H_2((alpha-1)/b).

For smaller b the bound has the trivial exponent b. At b=1.2, gamma_exposed=1.199456224042059: only a saving 0.000543775957941 from the trivial start count. At b approaching alpha the bound approaches h_*, giving the familiar ceiling alpha/h_*=1.0526808586079717 for the critical-log orbit bridge. Since H_2((alpha-1)/b) decreases on this b range, no intermediate b improves that ceiling. This elementary reduction does not reach kappa=1.053; the hard information lies in parity bits beyond the precision already exposed by the starting interval.

Independent finite verification: all A=1..12 and all r=1..A, totaling4095 valuation words, gave canonical start sets exactly equal to sets obtained by independently iterating the shortcut map over all odd residues below2^A. Checked positivity, oddness, range and injectivity. These checks corroborate the exact induction, not its asymptotic consequences.
