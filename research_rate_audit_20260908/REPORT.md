# Quantitative audit: explicit positive rate and a retained-subset bottleneck

2026-09-08. Two adversarial agents plus principal. Fixed target b=1.2, kappa=1.053. No new orbit class excluded; no paid model calls or remote publication.

## Outcome

An upper-only, one-pullback implementation gives a valid explicit exceptional exponent d_cert=5e-10, with unspecified finite asymptotic constants. This is NOT an optimized rate or a practical finite verification threshold. Separately, a necessary rate ceiling for the retained-subset construction is approximately0.000979308877 under the generous upper-only tolerance budget. Both are below the required0.050332383666. The ceiling concerns this proof construction at the stated parameters, not the true exceptional set or every possible parameter regime.

## Source and modification boundary

Primary source: Manuel Inselmann, https://arxiv.org/html/2402.03276 (v3). The relevant architecture is in Lemmas2.13–2.16; Theorem2.18 carries both orbit and remainder estimates. We retain its affine pullback construction, replace the base approximation by a direct upper-only estimate, and replace a remainder estimate at a single time by the elementary fractional-moment calculation below. These modifications and explicit constants are our deductions, not numerical exponents quoted from the paper. The independent adversarial note records the original retained-set bottleneck.

## Explicit parameter chain

Use a=log_2 3, c=a/2, rho=sqrt(3)/2, and n=floor(log_2 x). Full dyadic shells have uniform n-bit shortcut parity coding.

1. Base upper approximation: the affine identity is H^ell(y)=3^K(y/2^ell+r_ell), with0<=r_ell<1. For ell<=floor(log_2 y), y/2^ell>=1. A parity excess bounded by(.04/a)floor(log_2 y) yields H^ell(y)<=rho^ell*y^1.05 for sufficiently large y. A union of Hoeffding bounds permits every exception exponent below2(.04/a)^2/ln2=0.0018377504. Choose input D=.001.
2. Initial stage: prefix parity margin .01/a yields rho^n*x^.98<=H^n(x)<=rho^n*x^1.02, outside a set with exponent .0001 (below2(.01/a)^2/ln2=0.0001148594).
3. Pullback parameters: eta_prime=D/4=.00025; eta=D/32=.00003125. These satisfy eta_prime<D/(2-D) and eta<eta_prime/[2(eta_prime+2)]. The enlarged affine-good set followed by the scaling step has rate

       (D(1+eta_prime)-2eta_prime)*a*(.5-eta)=0.000396413968...

4. Retain prefix parity weight between(.5-eta)n and(.5+eta/2)n. Its complement has an upper-count exponent at least eta^2/(2ln2)=7.044409379e-10 by Hoeffding, with harmless fixed factors.
5. The remainder representation has a better rate than this parity restriction, as proved next. Thus d_cert=5e-10 is strictly below every relevant rate. Intersections preserve this smaller rate.

All tolerances have strict margins, absorbing floors and finite factors after a finite initial segment. We do not claim an explicit value for that segment or the multiplicative big-O constant.

## Fractional-moment remainder estimate

Let p_i be the first n shortcut parity bits on a full dyadic shell, S_(i+1)=sum_(j<=i)p_j, and

    r_n=sum_(i=0..n-1) p_i*2^(i-n)*3^(-S_(i+1)).

For fixed0<theta<=1, subadditivity (sum z_i)^theta<=sum z_i^theta and independent fair parity bits within this COMPLETE shell give

    E r_n^theta <= (3^(-theta)/2)*2^(-theta*n)
                     *sum_(i=0..n-1)(2^theta*a_theta)^i
                 <= C_theta*a_theta^n,
    a_theta=(1+3^(-theta))/2.

The geometric ratio exceeds1 because2^theta*a_theta>=(2/sqrt3)^theta>1. C_theta may be large but is fixed independently of n. This does not assume independent bits for an incomplete starting interval or after the exposed prefix.

Markov's inequality and log cosh u<=u^2/2 give

    Pr[r_n*3^((.5-eta)n)>=1]
      <=C_theta*2^(-n[theta*a*eta-theta^2*a^2*ln2/8]).

Taking theta=2eta/(a ln2)<1 yields rate3eta^2/(2ln2)=2.113322814e-9. Together with the prefix parity window, this gives the required single-time affine representation with remainder below one. This avoids the much smaller cubic rate from a conservative direct use of the source's uniform remainder lemma.

## Time horizon and transfer back to the count

One pullback only covers a horizon approaching(1+c-.02)log_2 x, NOT the full horizon in the source theorem. The principal caught the need to change the earlier small-start cutoff accordingly.

For our count at A=a*r+O(1), discard x<2^(.95r). For all remaining x, A/log_2 x<=a/.95+o(1)<1+c-.02, so the one-step horizon suffices. Put y=H^n(x), ell=A-n. The retained set obeys

    H^A(x)<=rho^ell*y^1.05
           <=constant*rho^A*x^[1+.02+.05(c+.02)]
           <=rho^A*x^1.1

eventually. But the exact total parity weight r forces H^A(x)>=3^r*x/2^A>=constant*x uniformly on fixed critical mass bands. Since (1-c)*a>.1*1.2, the upper approximation contradicts this for large r and x<=2^(1.2r+o(r)). Therefore

    F(X)<=2^(.95r)+O(X^(1-d_cert)), X=2^(1.2r+o(r)).

The previous dual-interval reduction transfers this bound to Q. This certified rate is weaker than prior explicit counting bounds and does not extend the established orbit exclusions.

## Why parameter tuning alone does not meet the target

Let I(u)=1-H2(.5+u). An input good set imposing upper orbit tolerance zeta through log_2 x has density exponent at most I(zeta/a): the complementary binomial upper tail actually violates the approximation. Eliminating the affine pullback parameters gives eta<D/[2(4-D)]. The retained prefix-concentration subset itself discards a binomial tail, so its achievable complement exponent is at most I(D/[2(4-D)]).

At b1.2 the limiting tolerance for a contraction contradiction is E=(1-c)*a/1.2. The literal remainder bookkeeping allows zeta<E; a more generous upper-only composition allows zeta<E/c. Substitution gives:

| Certificate accounting | Necessary rate ceiling |
|---|---:|
| Literal remainder-carrying construction |0.000365875806|
| Generous upper-only construction retaining the same concentration subset |0.000979308877|
| Required by kappa1.053 |greater than0.050332383666|

The attack agent initially treated zeta<E as intrinsic. The audit agent objected, and the larger upper-only allowance was incorporated. Even that does not meet the target. This is NOT an upper bound on the possible exponent for the actual preimage exceptional set: many discarded prefix-outlier points could still behave well. Recovering them needs additional control outside this particular retained-subset argument.

## Verification and next obligation

check_parameters.py evaluates all displayed parameter inequalities and caps at60-digit decimal precision; every check passes, with substantial strict margins. This is numerical verification of constants, not a formal proof assistant audit or a finite bound on all starting integers. The all-length reasoning is recorded above and independently checked by the audit agent.

Further work should not optimize this narrow-window certificate. A new argument must control the actual continuation of the discarded prefix-weight outliers, for example through a joint count that does not classify every outlier as exceptional. No such estimate has been proved here. The true critical-orbit question remains open.
