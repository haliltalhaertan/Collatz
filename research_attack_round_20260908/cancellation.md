# Exact dyadic mean/difference recursion with actual-prefix cancellation

2026-09-08. Independent adversarial derivation. No paid calls or large runs. The identities below hold for actual Collatz prefixes; the required bound on their signed differences remains open.

Fix m>=1. For0<=a<2^t let

    P_t(a;z)=sum_(odd1<=h<2^m) z^[K_(m+t)(h+2^m*a)],
    G_(t,r)(a)=[z^r]P_t(a;z),
    B_(t,r)=binom(m+t-1,r-1)/2^t,
    F_(t,r)=G_(t,r)-B_(t,r).

Out-of-range coefficient indices have value0. The first parity is fixed odd. These functions include all prefix weights with their actual multiplicities.

## 1. A genuine structural cancellation

Pair a and a+2^(t-1), with0<=a<2^(t-1). For each h, the corresponding original starts differ by2^(m+t-1). Their first m+t-1 parities agree. After those steps their states differ by an odd integer3^K, so their next parities are opposite.

Consequently, exactly and coefficientwise,

    P_t(a;z)+P_t(a+2^(t-1);z)=(1+z)P_(t-1)(a;z).

Thus

    G_(t,r)(a)+G_(t,r)(a+2^(t-1))
       =G_(t-1,r)(a)+G_(t-1,r-1)(a).

This is not a mean-field substitution: pairing the actual starting integers cancels the unknown final carry from the sum. Pascal's identity gives the same relation for B, hence the pair mean of F is

    M_(t,r)(a)=[F_(t-1,r)(a)+F_(t-1,r-1)(a)]/2.

More generally, averaging all2^s lifts of a lower block index cancels the final s unknown bits exactly:

    sum_(b=0..2^s-1) P_t(a+2^(t-s)*b;z)
       =(1+z)^s P_(t-s)(a;z).

Proof: each h has a fixed earlier weight K, and the state at depth m+t-s shifts by3^K*b. This odd dilation permutes the2^s tail residues and therefore their parity words. The weight-dependent dilation is retained and causes no loss in the complete lift average.

## 2. The signed difference retains the missing arithmetic

Let K_h be the weight through depth m+t-1 and let e_h be the next parity for the lower member of the pair. Define

    S_(t-1)(a;z)=sum_h (-1)^e_h z^K_h.

Then

    P_t(a;z)-P_t(a+2^(t-1);z)=(1-z)S_(t-1)(a;z).

Writing S_q=[z^q]S, the half-difference is

    D_(t,r)(a)=[S_r(a)-S_(r-1)(a)]/2.

This gives a second exact cancellation: the full signed difference polynomial vanishes at z=1, so sum_r D_(t,r)=0. At z=-1 the pair sum vanishes instead; the total parity-sign polynomial is anti-periodic under a->a+2^(t-1). These are genuine algebraic restrictions, but neither bounds one chosen coefficient r by itself.

## 3. Exact energy recursion

Let average and covariance on the lower-level block index use its uniform finite measure. The elementary pair identity gives

    V_(t,r)=average[M_(t,r)^2]+average[D_(t,r)^2]
      =[V_(t-1,r)+V_(t-1,r-1)
          +2 Cov(F_(t-1,r),F_(t-1,r-1))]/4
        +average[D_(t,r)^2].

The plus sign on the D energy is essential. Orthogonal decomposition preserves energy; it is not automatically a contraction. Bounding the mean term while omitting D would reproduce the invalid diagonal-only variance argument in another form.

Expanding the last term gives

    4 average[D_(t,r)^2]
       =average[S_r^2+S_(r-1)^2-2S_r*S_(r-1)].

Each S is a signed count of actual prefixes classified by their next carry. The off-diagonal products therefore contain precisely the unknown pair correlations, now organized by adjacent weights and the final dyadic scale. Taking absolute values before combining these terms would discard the cancellation the recursion was designed to preserve.

## 4. What is established, and what is not

Established: all dyadic conditional means can be computed from shorter-depth adjacent-weight counts by an exact Pascal smoothing, independent of the final carry signs. Every high-bit pair difference has the factor1-z, and its total coefficient sum vanishes. The variance splits exactly into mean and signed-difference energies.

Open: any uniform bound on the sum of signed-difference energies strong enough for the previously specified variance exponent. The recursions identify where such a bound must enter; they do not furnish it. Constant sign, zero adjacent-weight covariance, independent carries, or a norm contraction would each be an additional unsupported assumption. In particular, a Koopman isometry or a low-degree claim cannot be substituted for the missing energy estimate.

The useful next lemma would estimate the signed counts S_r-S_(r-1) across actual block indices, with prefix multiplicities preserved. Proving only the unsigned Pascal relation again would merely restate the translated-block mean already known.

## Verification

Independent direct shortcut iteration checked699 coefficientwise pair identities across all m1..6,t1..4. Exact rational variances agreed with the mean/difference energy identity for every tested coefficient. All checks passed. These bounded computations validate signs and normalization; the all-length proof is the pairing argument above.

## 5. Principal's correction: remove the exact uniform nullspace first

The principal's centered-prefix diagnostic showed that much of the previously large positive/negative pair accounting was cancellation of an exactly uniform prefix component, rather than evidence of complicated cancellation between weight strata. This correction is mathematically sound.

Use the original prefix histogram P_k(z), q=2^t, N_k=sum_z P_k(z), and define

    E_k(z)=P_k(z)-N_k/q,
    e_k=sum_z E_k(z)^2=sum_z P_k(z)^2-N_k^2/q,
    p_j=binom(t,j)/q.

The uniform component contributes only the mean N_k p_j, because z->z+3^k*a permutes all residues. It is therefore annihilated before forming any centered covariance.

For unnormalized Fourier transforms, let M_j=max_(xi!=0)|hat T_j(xi)| and let V_k be the variance of the k-stratum contribution alone. Exact Parseval gives

    V_k=q^(-2)sum_(xi!=0)|hat E_k(-xi)|^2 |hat T_j(xi)|^2
         <=M_j^2*e_k/q, j=r-k.

The3^k dilation merely permutes frequencies for this individual stratum. The total variance consequently obeys

    V <= (sum_k sqrt(V_k))^2
       <= (sum_k M_j*sqrt(e_k/q))^2
       <= K sum_k M_j^2*e_k/q,

where K is the number of participating weights, at most m. This costs only a polynomial factor and assumes no favorable cross-weight sign. The trivial spectral estimates M_j<=min(qp_j,q(1-p_j)) and M_j^2<=q^2 p_j(1-p_j) are always valid.

Define the centered source diagonal

    D_source=sum_k e_k*p_j*(1-p_j).

Then the weaker but simple sufficient inequality is

    V<=K*q*D_source.

Combined with the sharp origin estimate, this gives |G(0)-B|<=sqrt(K)*q*sqrt(D_source), up to replacing q-1 by q. Thus even the conditional estimate D_source<=poly(r)*B suffices for the IDEAL count exponent when gamma0>=2tau, where tau=alpha-b and gamma0=h_*+b-alpha. Equivalently b>=alpha-h_*/3, approximately1.0830812047, which includes b1.2.

More generally an exponent omega for D_source is sufficient for the kappa bridge if omega<2b/kappa-2tau. At b1.2,kappa1.053 this is approximately1.5092772778. This is an unproved, explicitly quantified weighted L2-prefix-defect target. It shows that sufficiently good centered prefix mixing would make additional off-diagonal cancellation unnecessary; it does not assert that such mixing has been established.

The support-size spectral estimate also gives V<=K*q*D2, where D2=sum_k e_k*p_j^2. For t>=1 every binomial weight probability p_j<=1/2, so D2<=D_source. The same sufficient exponent threshold applies to D2; this may be sharper in rare-tail strata and requires no additional spectral cancellation assumption.

### Independent elementary check via convolution

For the k-stratum, reflection and the permutation a->3^k*a identify its centered function with the circular convolution of E_k and T_j. Young's inequality in unnormalized counting norms gives

    ||E_k*T_j||_2 <= ||E_k||_2 ||T_j||_1 = sqrt(e_k)*q*p_j.

Dividing by sqrt(q) converts to the population L2 norm, so sqrt(V_k)<=sqrt(q)*p_j*sqrt(e_k). Minkowski followed by Cauchy across K strata gives V<=K*q*D2 exactly as above. This proof requires no Fourier coefficient estimate and confirms the normalization.

The origin bound then gives G(0)<=B+sqrt(K)*q*sqrt(D2). If D2 has exponent omega, the resulting count exponent is at most max(gamma0,tau+omega/2). Thus BOTH gamma0<b/kappa and omega<2b/kappa-2tau are needed for the strict orbit bridge. At b1.2,kappa1.053 the first already holds and the second threshold is approximately1.5092772778. Uniform fixed-band control and polynomial K remain required.

The previously fixed direct checks are now reproducible in check_dyadic.py and DYADIC_CHECK.json:699 coefficientwise identities and168 exact variance decompositions, all PASS on the original m1..6,t1..4 grid. No grid expansion was made.
