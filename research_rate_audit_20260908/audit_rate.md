# Explicit one-bootstrap exponent audit

2026-09-08. This is an elementary quantitative reconstruction using Inselmann's neighborhood/bootstrap mechanism, with an upper-only base event and a one-time fractional-moment refinement. It is not a literal extraction of the constants in the paper's full-horizon two-sided proof.

Write alpha=log_2(3), rho=sqrt(3)/2, d=1-alpha/2. A set has exception exponent D when its complement below X is O(X^(1-D)). All claims here are asymptotic with unspecified finite constants. No finite convergence range follows.

## 1. Upper-only base event

On x in [2^n,2^(n+1)), every prefix of length ell<=n is fair under uniform counting. The exact affine identity is

    H^ell(x)=3^P_ell*(x/2^ell+r_ell), 0<=r_ell<1.

Since x/2^ell>=1, this is at most2*3^P_ell*x/2^ell. A union of Hoeffding bounds therefore shows that the event

    H^ell(x)<=rho^ell*x^(1+.05), all ell<=log_2(x),

has any exception exponent strictly below2*(.04/alpha)^2/ln2=0.001837750435029583. Fix D=0.001. The gap between .04 and .05 absorbs the constant2 and floors.

Similarly, using absolute parity deviations .01*n/alpha, the event

    rho^ell*x^(.98)<=H^ell(x)<=rho^ell*x^(1.02), all ell<=log_2(x),

has exception exponent D0=0.0001, since2*(.01/alpha)^2/ln2=0.00011485940218934894. Lower estimates use r>=0. This avoids cubic auxiliary losses from demanding more than the needed upper event.

## 2. One-time offset concentration, independently derived

Let eta>0. At depth n,

    r_n=sum_(i=0)^(n-1) p_i*2^(i-n)*3^(-P_(i+1)).

For0<theta<=1, fractional-power subadditivity and dropping p_i give

    E r_n^theta <= 2^(-theta*n)*a_theta*sum_(i=0)^(n-1)(2^theta*a_theta)^i
                 <=C_theta*a_theta^n,
    a_theta=(1+3^(-theta))/2.

The geometric ratio exceeds1 because a_theta>=(3^(-theta/2)). The geometric constant C_theta can be large as theta approaches0; theta is fixed here, so this does not alter the power exponent or its uniformity in n. Hoeffding's moment estimate gives

    ln(a_theta)<=-theta*ln3/2+theta^2*(ln3)^2/8.

Markov's inequality therefore bounds the proportion with r_n*3^((.5-eta)n)>=1 by

    C_theta*2^[-(theta*alpha*eta-theta^2*alpha^2*ln2/8)n].

Choose theta=2eta/(alpha ln2), valid for the parameters below. The certified offset exponent is3eta^2/(2ln2).

## 3. Explicit neighborhood bootstrap parameters

Take eta_prime=D/4=0.00025 and eta=D/32=0.00003125. They satisfy

    eta_prime<D/(2-D),
    eta<eta_prime/[2(eta_prime+2)].

Following the neighborhood and dilation steps in Lemmas2.13--2.16, the neighborhood exponent is

    D_neigh=D(1+eta_prime)-2eta_prime=0.00050025,

and its dilation pullback has exponent

    D_dilate=alpha(.5-eta)*D_neigh=0.0003964139680712859.

For the representation of H^n(x), impose both the offset event above and prefix weight in[(.5-eta)n,(.5+eta/2)n]. The latter has any exponent below eta^2/(2ln2). The representation is then

    H^n(x)=floor[3^floor((.5-eta)n)*x/2^n]*3^L+i,
    0<=L<=2eta*n, 0<=i<2*3^L,

for sufficiently large n. The two relevant rates are

    D_offset=3eta^2/(2ln2)=2.1133228138021926e-9,
    D_parity=eta^2/(2ln2)=7.044409379340642e-10.

Thus the original base upper event pulled back by x->H^floor(log2x)(x) has the safely smaller exception exponent

    D_cert=5e-10.

This conclusion uses the source's exact neighborhood mechanism; the explicit rates for the input and representation events were proved above instead of being assumed.

## 4. Horizon, accumulated error and application to our count

Intersect that pullback with the initial event of Section1. At n=floor(log2x), write y=H^n(x). We have log2 y>=(alpha/2-.02)log2x+O(1). Thus the second base window covers every total depth up to1.7log2x for sufficiently large x, as1.7<1+alpha/2-.02=1.772481250360578.

For later depth N=n+ell, combine the upper estimates:

    H^N(x)<=rho^N*x^(1+.02)*y^.05
           <=O(1)*rho^N*x^[1+.02+.05(alpha/2+.02)].

The accumulated error exponent .060624062518028904 is less than .1. Therefore the upper trajectory approximation with epsilon=.1 holds through1.7log2x outside O(X^(1-D_cert)) starts below X.

For the Collatz count at b=1.2, discard x<2^(.95r), NOT the earlier full-horizon cutoff2^(.5r). Now A/log2x<=alpha/.95+o(1)=1.6683815797064803+o(1)<1.7. A fixed critical mass band and parity weight r imply H^A(x)/x>=3^r/2^A>=c0>0. The good-set upper estimate instead tends exponentially to0, since -d*alpha+.1b<0. Consequently

    F<=2^(.95r)+O(2^[(1.2*(1-5e-10)+o(1))*r]).

The explicit power exponent5e-10 is far smaller than the orbit-bridge requirement1-1/1.053=0.05033238366571691. It is also much weaker than the project's explicit affine-offset count bound. This reconstruction closes the unspecified-positive-exponent bookkeeping obligation; it does not improve the research's best count exponent or exclude a new trajectory class.

For any fixed band |A-alpha*r|<=C, all source good sets and parameters are independent of A. Only bounded constants in c0 and the endpoint/start scaling depend on C. The displayed asymptotic count bound is therefore uniform on each required fixed critical mass band.

## Source scope

Primary source: Manuel Inselmann, arXiv2402.03276v3, https://arxiv.org/html/2402.03276 . The checked mechanism is the power-density neighborhood expansion and dilation in Lemmas2.13--2.16. Constants above belong to this reconstruction, with the separately derived fractional-moment estimate. No claim that these are optimal constants of the source theorem or a limitation on all alternative arguments is made.
