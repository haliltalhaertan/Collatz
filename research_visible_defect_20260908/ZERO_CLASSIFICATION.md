# Complete classification of exact cyclic tail-kernel zeros

2026-09-08. Principal's candidate lemma independently audited. Exact all-length algebraic result; no quantitative lower bound on nonzero coefficients, no new orbit exclusion, and no novelty claim.

Let t>=1 and0<=j<=t. Let T_(t,j)(u) be the indicator that the first t shortcut Collatz parities from u have weight j, for u modulo2^t. Use the unnormalized cyclic Fourier transform. Every nonzero frequency has the form xi=a*2^(t-s), with1<=s<=t and a odd modulo2^s.

## Theorem

    hat T_(t,j)(xi)=0

if and only if s=1, t is even, and j=t/2. In particular every tail coefficient of conductor at least4 is nonzero, for every valid weight j.

## Proof

Put n=t-s. The exact parity-lift formula from kernel.md gives

    hat T_(t,j)(a*2^(t-s))
       =sum_(u=0..2^s-1) binom(n,j-K_s(u))*zeta^u,

where zeta=exp(-2pi*i*a/2^s) is a primitive2^s-th root. Define the integer polynomial

    F(X)=sum_(u=0..2^s-1) binom(n,j-K_s(u))*X^u.

The minimal polynomial of zeta over the rationals is Phi_(2^s)(X)=X^(2^(s-1))+1. Since deg F<2^s, F(zeta)=0 is equivalent to the coefficientwise sibling equalities

    binom(n,j-K_s(u))
      =binom(n,j-K_s(u+2^(s-1)))

for every0<=u<2^(s-1). To see the coefficient equivalence directly, divisibility by1+X^H with H=2^(s-1) and degree less than2H means F=(1+X^H)Q with deg Q<H, so the two halves are identical. Conversely identical halves give that factorization.

Sibling residues u and u+2^(s-1) have the same first s-1 parities and opposite last parity. If their first s-1 weight is h, their unordered s-bit weights are h,h+1. Every h in0,...,s-1 occurs because the length-(s-1) parity coding is bijective on those residues. Thus all sibling equalities hold exactly when

    binom(n,j-h)=binom(n,j-h-1), every h=0,...,s-1.

Equivalently the s+1 consecutive extended binomial coefficients at indices j-s,...,j are all equal, with coefficients outside0,...,n defined to be zero.

Since0<=j<=t=n+s, this index interval intersects[0,n]. At least one coefficient is positive, so their common value would have to be positive and every index would have to lie in[0,n]. In a positive binomial row, consecutive equality binom(n,l)=binom(n,l-1) occurs only at l=(n+1)/2. There cannot be two consecutive such equalities. Therefore s+1>=3, namely s>=2, is impossible. This argument also covers n=0 and n=1 through the support observation.

For s=1, the sole equality is binom(t-1,j)=binom(t-1,j-1). At valid endpoints j=0,t one side is1 and the other0. In the interior it holds exactly when2j=t. This proves the classification.

The cyclotomic argument also explains why a zero at any one primitive frequency would force every primitive coefficient on that conductor to vanish. It is not legitimate to infer this for arbitrary real coefficient arrays; here the aggregate coefficients are integers.

## Exact nullspace consequence

On the full real or complex cyclic space modulo q=2^t, convolution with T_(t,j) has rank q and is invertible unless t is even and j=t/2. In that exceptional middle-weight case its kernel is exactly the one-dimensional span of u->(-1)^u and its rank is q-1. The zero-frequency coefficient binom(t,j) is always positive, so no extra constant direction is in the kernel. On the mean-zero domain the same alternating vector is the only possible null direction, again only in the exceptional case.

The odd dilation3^k does not change this statement. For an individual centered prefix stratum, V_k=0 therefore implies E_k=0 except in the middle-tail case, where E_k may be purely alternating. Different k strata can still cancel each other in the total count; the theorem does not preclude that separate phenomenon.

The corrected actual m3,k2,t2,j1 histogram P=(1,0,1,0) realizes the exceptional alternating null direction. It does not exemplify a larger higher-conductor nullspace.

## Quantitative limitation

Nonzero is not a uniform lower bound. The theorem rules out exact invisibility of higher conductors, but those tail multipliers may still be small relative to the binomial mass. It therefore does not justify controlling the full unweighted source defect from visible variance, nor prove the required upper bound on W or the origin count.

The retained open direction is quantitative spectral attenuation and actual source-energy allocation, rather than a search for additional exact higher-conductor zeros of these cyclic tail-weight kernels. This classification says nothing about Boolean Walsh zeros, which are a different transform.

The principal independently checked440 conductor cases at t1..10 using exact binomial-lift coefficients; check_zeros.py and ZERO_CHECK.json preserve those checks. The present audit did not duplicate that computation. The theorem rests on the cyclotomic and binomial-row proof above.
