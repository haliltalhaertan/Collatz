# Adversarial rate audit of the Inselmann bootstrap

Primary source inspected: https://arxiv.org/html/2402.03276 (v3), especially Lemmas2.13-2.16 and Theorem2.18, equations2.7,2.14-2.19. This is a rate audit of one proof construction, not an upper bound on what the actual exceptional set can achieve.

Write a=log2(3), c=a/2, and I(u)=1-H2(1/2+u).

## A conditional certificate-rate ceiling

Suppose the input good set P in Lemma2.16 has density exponent D. Its parameters obey

    eta_prime < D/(2-D),
    eta < eta_prime/[2(eta_prime+2)].

Eliminating eta_prime gives eta<D/[2(4-D)]. Lemma2.15 establishes its good set via intersection with a complete-prefix parity concentration set Q whose upper tolerance is some eta_second<eta. Over each full dyadic shell, parity coding is exactly uniform. Hence the complement of Q has size 2^(n(1-I(eta_second))+o(n)).

Consequently the SPECIFIC good subset retained by this intersection cannot have complement exponent greater than

    I(D/[2(4-D)]).

This is not an impossibility theorem for the larger good set asserted by Lemma2.15 or the actual preimage of P: points discarded by Q may still satisfy them. Recovering such points requires an argument outside this retained-subset accounting.

## Bounding the allowable input D

If P imposes the usual upper orbit approximation with tolerance zeta through depth floor(log2 x), then any admissible density exponent D obeys

    D <= I(zeta/a), provided0<zeta/a<1/2.

Proof: on x in[2^n,2^(n+1)), the n-step parity word is uniform over all n-bit words. If its number of ones s exceeds n/2+zeta*(n+1)/a, the exact affine formula gives

    T^n(x) >= (x/2^n)*3^s > (sqrt(3)/2)^n*x^(1+zeta).

This binomial upper tail lies in the actual complement of P and has logarithmic exponent1-I(zeta/a), by Stirling's formula. Thus this input-rate ceiling is an actual necessary constraint, unlike a mere lower estimate obtained from Hoeffding.

## Numerical scope for the present target

The limiting admissible approximation tolerance for the target horizon is

    E=(1-a/2)*a/1.2=0.2740911969791881.

Literal Theorem2.18 remainder bookkeeping in equation2.19 chooses

    (1+delta)*zeta+delta*a<E,

so zeta<E. Even permitting equality in the limiting upper envelope gives

    D <=0.08809762970004353,
    eta <=0.011260203011314977,
    retained-subset rate <=0.00036587580557323474.

Audit agent correctly challenged treating zeta<E as intrinsic: if only the orbit upper estimate is carried and the contraction factor is retained, one may allow zeta>E. The more generous one-step upper-composition condition is

    delta+(c+delta)*zeta<E,

which permits zeta up to E/c=0.3458645827323699. Repeating the same calculation yields

    D <=0.1421300830904766,
    eta <=0.018420797765562644,
    retained-subset rate <=0.0009793088765915892.

Both bounds are below the needed D>1-1/1.053=0.05033238366571691. They quantify why merely optimizing these parameters and retaining the same parity-concentration intersection will not hit that target. They do not close altered proofs, alternative preimage estimates, shorter tailored blocks, or the actual exceptional count.

No paid calls, asymptotic orbit exclusion, or claim that the paper's qualitative theorem is false. Calculations use standard real logarithms for displayed diagnostics; the proof inequalities are symbolic and have a wide numerical margin.
