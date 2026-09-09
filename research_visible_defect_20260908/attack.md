# Adversarial audit of source scales and tail-visible energy

2026-09-08. Algebraic audit and diagnostic proposal; no new enumeration. Fix one m,k stratum throughout each formula. Use ordered pairs in collision counts, and unnormalized cyclic Fourier transforms.

## 1. Precision is not automatically a monotone raw defect

Write P_s for the same exact-endpoint population reduced modulo 2^s, N=sum P_s, C_s=sum P_s^2, and e_s=C_s-N^2/2^s. For

    R_s=sum_{z<2^s}(P_(s+1)(z)-P_(s+1)(z+2^s))^2,

the recorded identities e_(s+1)=e_s/2+R_s/2 and e_t=sum_{s<t}2^(s-t)R_s are correct. Raw e_s need not increase with resolution: its normalization changes. The monotone quantity is 2^s e_s (or 2^s e_s/N^2 for N>0).

At full q=2^t, the exact source energy at Fourier conductor 2^ell is

    E_ell=(1/q) sum_{ord(xi)=2^ell}|hat E_t(xi)|^2
         =2^(ell-1-t) R_(ell-1),   1<=ell<=t.

These are the legitimate nonnegative additive scale components of e_t. Do not compare unscaled R_s across s as if they were contributions of equal normalization.

## 2. Exact merging versus modular aliasing

Let M_y count starts reaching the SAME INTEGER endpoint y after the SAME m steps with the SAME weight k. Define

    C_exact=sum_y M_y^2,
    A_d=sum_{y!=y', v2(|y-y'|)=d} M_y M_y'.

Then, exactly,

    C_s=C_exact+sum_{d>=s} A_d,
    e_s=C_exact+sum_{d>=s}A_d-N^2/2^s,
    R_(ell-1)=C_exact+sum_{d>=ell}A_d-A_(ell-1).

This gives a useful nonnegative partition of RAW collisions into exact fibers and dyadic alias distances. It does NOT give a nonnegative additive split of centered conductor energy into 'merger energy' and 'alias energy': the last identity contains subtraction. Large C_exact alone cannot identify the responsible conductor or the tail visibility of a defect.

C_exact includes N self-pairs; the genuinely distinct-start exact collisions are C_exact-N. Replacing M_y by one discards multiplicity and changes both the source population and the target observable. General checkpoint merging certificates at different times or weights are not automatically certificates for these exact fibers.

## 3. The right source-versus-visible comparison

For actual tail indicator T_j and full-grid source E_t, define

    V_ell=(1/q^2)sum_{ord(xi)=2^ell}|hat E_t(xi)|^2 |hat T_j(xi)|^2.

Then V_k=sum_ell V_ell. The odd multiplier 3^k permutes frequencies without changing conductor, so it preserves this layerwise energy statement. It still matters for cross-k phases and direct origin values.

When E_ell>0,

    V_ell/E_ell=(1/q)*(source-energy-weighted mean of |hat T_j|^2 on that conductor).

Thus useful diagnostics are the conductor fractions E_ell/e_t and V_ell/V_k, and the attenuation

    V_ell/(q p_j^2 E_ell) in [0,1],

with zero denominators explicitly marked undefined. The upper bound uses |hat T_j|<=q p_j. At total level compare W with q D_2, not unnormalized W with D_2. For this integer-valued tail indicator, primitive Fourier coefficients on a fixed conductor are Galois conjugates: one exact zero therefore annihilates that entire conductor. The earlier generic warning about one zero frequency was too weak for this rational kernel. The exact classification below shows that only conductor two can vanish.

The exact min/max tail multipliers on each conductor also give certified bounds

    (min |hat T_j|^2)/q * E_ell <= V_ell
       <= (max |hat T_j|^2)/q * E_ell.

These are weighted spectral comparisons, not independence claims about endpoints and tails.

## 4. What the fixed panels can establish

The panels can verify the scale/Fourier identities, expose which conductors dominate in each finite stratum, and identify exact zeros or unusually strong attenuation. They cannot establish uniform suppression in the growing critical regime, or even that the dominant finite stratum stays dominant. The relevant weights p_j and full normalizations must accompany every comparison.

Finally, W=sum_k V_k is not the total variance V; cross-stratum covariances remain. The valid V<=K W costs only O(r). The resulting q costs in source-to-origin bounds are not intrinsically fatal: the current sufficient exponent calculation can absorb them if the conjectured source-energy budget holds. Conversely, tail visibility can make that sufficient budget unnecessarily strong. Neither strategy has its needed asymptotic estimate yet.

## 5. Exact tail-zero classification: independently verified

For the actual indicator T_(t,j), 0<=j<=t, all primitive conductor-2^s Fourier coefficients are conjugate algebraic numbers, because the indicator has integer coefficients. Thus one is zero if and only if all are zero.

Aggregate the indicator modulo 2^s. At u the coefficient is F(u)=binom(t-s,j-K_s(u)), with out-of-range binomial coefficients zero. The suffix count is exact: fixing a length-s parity prefix leaves the remaining binary parameter in a bijective affine residue parametrization of the length-(t-s) parity words.

Divisibility by Phi_(2^s)(X)=X^(2^(s-1))+1 is equivalent to F(u)=F(u+2^(s-1)) for every u<2^(s-1). These paired residues have the same first s-1 parity bits and opposite final bit. Their weights are h,h+1, and all h=0,...,s-1 occur. Therefore vanishing requires all s+1 coefficients

    binom(t-s,j), binom(t-s,j-1), ..., binom(t-s,j-s)

to be equal. The index interval intersects [0,t-s], because 0<=j<=t, so at least one coefficient is positive. A binomial row has no positive plateau longer than two. For s>=2, equality is impossible. This includes t-s=0, whose sole positive coefficient is one.

For s=1, adjacent positive binomial coefficients are equal exactly when t is even and j=t/2. This proves that conductor two is the only possible zero conductor, with precisely this central-weight condition. The endpoint weights j=0,t have no nonzero-frequency zeros. The classification is exact algebra; no floating-point positivity test is used. It does not bound the magnitudes of nonzero coefficients away from zero uniformly as t grows.

