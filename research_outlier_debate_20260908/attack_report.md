# Adversarial audit of conditional parity recovery

## Exact polynomial recursion retaining the missing information

Define P(a,b,N;m,t;z,w) as the sum over j=0,...,N-1 of z to the number of odd states in the first m shortcut steps starting from aj+b, times w to the number of odd states in the following t steps. P at zero total depth equals N.

At a positive depth, let v=z if m>0, otherwise v=w, and decrement the corresponding depth.

If a is even, every start has parity e=b mod2. The recursion has one child with factor v^e and progression

    (a/2,b/2,N) if e=0,
    (3a/2,(3b+1)/2,N) if e=1.

If a is odd, split j=2l+h, h=0,1, with N_h=floor((N+1-h)/2) and c_h=b+ah. The child has factor v^(c_h mod2) and progression

    (a,c_h/2,N_h) if c_h even,
    (3a,(3c_h+1)/2,N_h) if c_h odd.

This identity follows directly from H; it is exact and nonprobabilistic. The desired odd-start polynomial is P(2,1,2^(m-1);m,t;z,w). Coefficients [z^k w^l] are genuine joint counts. A scalar weight histogram cannot evaluate the recursion because the progression offset controls the next parity. This is an exact interface, not a complexity improvement: the recursion may branch to singleton progressions.

## Finite complete bias after uniformly coded prefixes

For m2,t1, the polynomial is z*w+z^2: x1 has prefixweight1 and odd tail; x3 has prefixweight2 and even tail.

For m3,t1, it is z+2z^2+z^3: starts1,3,5,7 reach2,4,2,26 after three steps, respectively, all even. The prefix counts still have precisely the expected binomial weights. Conditional tail uniformity therefore does not follow from prefix coding.

## Infinite exact family showing an exponential correction may be necessary

For every m>=1, the prefixweight-one stratum has one odd start:

    x=(2^m*u-1)/3,
    u=1 if m even, u=2 if m odd.

It obeys x<2^m, and the first step is odd followed by m-1 even steps, so H^m(x)=u. Thereafter the orbit is the1,2 cycle. Conditional on this weight stratum, the entire t-bit tail is the corresponding alternating word with probability1. A fair-tail-word model would assign2^-t, so a uniform multiplicative correction valid over every stratum and every word must be at least2^t.

This is not a global exceptional-count lower bound: the stratum has only one start and is exponentially sparse among the2^(m-1) odd starts. It does not refute an estimate restricted to interior weights or only upper parity-tail events. It does refute blanket conditional independence with subexponential error over all strata.

## Audit of the proposed conditional-offset moment

For a uniform ALL binary m-bit word of weight k, let p=k/m and E=C/2^m=sum_i p_i*2^(i-m)*3^(k-S_(i+1)). For0<theta<=1, subadditivity and dropping p_i<=1 yield

    E[E^theta] <= 2^-theta *sum_(j=0..m-1)q_theta^j,
    q_theta=2^-theta*(1-p+p*3^theta).

The sampling-without-replacement product bound (equivalently the elementary symmetric mean inequality) justifies the moment of each suffix product. This is valid on the full weight stratum. For odd starts, use bad_odd<=bad_all with binom(m,k), as the audit agent explicitly confirmed; do not silently treat the first bit as unconditioned. Comparing to binom(m-1,k-1) costs the factor m/k, harmless in the exponent but relevant to a finite formula.

No independent tail law is used by this moment bound. It only controls the affine offset; the actual continuation still requires the height/residue counting step. Therefore improvement in this moment alone does not establish a better final count exponent.

## Checks

attack_polynomial.py verifies the progression recursion against direct trajectory iteration for45 cases m1..9,t1..5. All pass. The all-length weight-one identity is algebraic. No paid calls, frozen changes, or new orbit exclusion.
