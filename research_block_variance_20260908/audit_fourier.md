# Exact translated-block Fourier identity and an affordable variance target

2026-09-08. Independent algebraic derivation. No paid calls. The variance bound identified below is an unproved sufficient target, not an established property of Collatz.

Fix m,t,r with A=m+t and Q=2^t. For each k let

    P_k(z)=#{odd1<=h<2^m : K_m(h)=k, H^m(h)=z modQ},
    T_j(z)=1 if the first t parities of H starting at z have weight j, else0.

Set T_j=0 outside0<=j<=t. The target count in translated input block a is exactly

    G(a)=sum_k sum_z P_k(z) T_(r-k)(z+3^k*a),  a in Z/QZ.

This keeps the prefix-weight-dependent dilation3^k. Replacing it by a common shift would change the problem.

## Fourier and variance normalizations

Use hat f(xi)=sum_z f(z) exp(-2pi*i*xi*z/Q), so inversion has factor1/Q. Then

    hat G(eta)=sum_k hat T_(r-k)(3^(-k)*eta)
                     *hat P_k(-3^(-k)*eta).

Here3^(-k) is the modular inverse moduloQ. In particular

    B=average_a G(a)=hat G(0)/Q=binom(A-1,r-1)/Q.

The exact population variance is

    sigma^2=(1/Q)sum_a(G(a)-B)^2
       =(1/Q^2)sum_(eta!=0)
           |sum_k hat T_(r-k)(3^(-k)*eta)
                    *hat P_k(-3^(-k)*eta)|^2.

The sum over k remains inside the squared modulus. Its cross terms are not independent noise. Cauchy across the O(m) strata would cost only a polynomial factor, but obtaining small enough individual energies would remain necessary.

At the origin,

    G(0)-B=(1/Q)sum_(eta!=0)hat G(eta),
    |G(0)-B|<=sqrt(Q-1)*sigma.

## The pointwise loss is sharp, but might be affordable

Mean and variance alone cannot generally remove sqrt(Q-1). An array having G(0)=B+d and every other value B-d/(Q-1) attains equality whenever nonnegative; suitable integral rescalings preserve the exponent. The additional crude range bound G<=2^(m-1) does not by itself fix this when B is exponentially below that range. Actual Collatz arithmetic might preclude coherent Fourier phases, but that requires a new argument.

However, dismissing variance solely because of the sqrt(Q) factor would be a mistake. Put m=br+o(r), t=(alpha-b)r+o(r), gamma0=h_*+b-alpha. If

    sigma^2<=2^((v+o(1))*r),

then

    G(0)<=2^((max(gamma0,(alpha-b+v)/2)+o(1))*r).

Therefore the ideal count exponent follows from v<=2gamma0-(alpha-b). A permitted loss lambda follows from

    v<=2gamma0-(alpha-b)+2lambda.

Equivalently, the normalized requirement is sigma^2/B^2<=2^(-(alpha-b-2lambda)r+o(r)). All inequalities must be uniform on the required fixed critical mass bands.

At b=1.2, the ideal variance threshold is approximately1.8564002741 in exponent per r. For kappa1.053, the strict orbit-bridge requirement is

    v < 2b/kappa-(alpha-b),

approximately1.8942397785. A hypothetical Poisson-sized variance sigma^2=2^((gamma0+o(1))*r), with gamma0 about1.1206813872, would easily suffice even after the sharp pointwise loss. This comparison is a scale calibration only; no Poisson law is assumed or proved.

The trivial estimate sigma^2<=max(G)*B has exponent at most b+gamma0, approximately2.3206813872, so it does not suffice. The variance route needs a substantive correlation estimate, but not necessarily cancellation strong enough to remove every pointwise loss.

## What would be a useful next certificate

Prove a bound on the exact nonzero-frequency energy above, retaining the3^(-k) reindexings. It may suffice to bound the sum of the separate stratum energies and pay O(m), rather than proving cancellation between different k. A finite all-block variance panel can test proposed inequalities and their normalization; it cannot establish the required uniform exponential estimate or justify treating a=0 as a random block.

In particular, the conditional hypothesis sigma^2<=poly(r)*B implies the ideal count exponent whenever gamma0>=alpha-b, equivalently b>=alpha-h_*/2 (approximately0.8321405567). This is comfortably satisfied at b1.2. The exact finite inequality sigma^2<=B is stronger than needed and must not be inferred from a few rows satisfying it.

## Exact pair-correlation form

Define p_j=binom(t,j)/Q and

    C_(j,j')(d,c)=(1/Q)sum_u T_j(u)T_j'(d*u+c).

For prefix endpoints z,z' with weights k,l, change variables u=z+3^k*a. The second endpoint is d*u+c with d=3^(l-k) modQ and c=z'-d*z. Therefore

    sigma^2=sum_(k,l,z,z') P_k(z)P_l(z')
        *[C_(r-k,r-l)(3^(l-k),z'-3^(l-k)*z)-p_(r-k)p_(r-l)].

This is an exact expression averaging over actual prefix offsets. The diagonal contributions from identical starting h are p_j(1-p_j), summing to at most B. The remaining covariances can have either sign; discarding them would not prove sigma^2<=B.

For nonzero integer e, the slope's distance from1 satisfies

    v_2(3^e-1)=1 if e odd,
    v_2(3^e-1)=2+v_2(e) if e even,

with valuation truncated at t moduloQ. Negative exponents have the same valuation because the extra denominator is an odd unit. Since |l-k|<=m=O(r), distinct slopes cannot agree modulo more than O(log r) low bits when t grows linearly. This does not by itself bound correlation of the complete tail-weight sets.

Here is a counterexample to a slope-only decorrelation assertion, respecting j-j'=l-k. Take l=k+1, so d=3, j=t, j'=t-1, and t>=2. The set T_t is the singleton u=-1 modQ. Choose c=2^(t-1)+2. Its image is3u+c=2^(t-1)-1, whose t-step parity weight is t-1: it has t-1 consecutive odd steps, followed by an even state. Thus

    C_(t,t-1)(3,c)=1/Q,
    p_t*p_(t-1)=t/Q^2.

The correlation is enhanced by Q/t despite v_2(3-1)=1. This is a valid abstract affine-offset example, not a claim that the needed offset pair is realized with significant multiplicity in the actual prefix histogram. It demonstrates why the useful next lemma must average over the actual c=z'-3^(l-k)z values, rather than asserting pointwise independence from the slope valuation.
