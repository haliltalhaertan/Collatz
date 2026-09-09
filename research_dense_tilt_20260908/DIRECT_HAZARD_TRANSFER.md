# Direct dense hazard transfer and its change of law

2026-09-08. Exploratory analytic result. The dense C/R Laplace upper bound remains open; no sealed stage or numerical depth experiment is executed.

## 1. Predictable opportunities and exact conditional pair law

Let P be the original uniform weak-composition law for a valid R-coordinate suffix of total K. Before pair j+1, let F_j denote the revealed past. A_j in {0,1} is a predictable opportunity indicator. Two choices matter:

- every white entry: A_j=1_{dist(z_j,Z)>=eta}; its mark count is N_white;
- only regular white entries: A_j also requires the remaining length and slope to be in a chosen regular cone; its count N_reg satisfies N_reg<=N_white.

Write X_j=A_j*1_{B_(j+1)=1}, N_A=sum_j X_j, W_A=sum_j A_j. At a remaining state (r,k,z), for r>=3,

p_(r,k)(b)=(b+1)*binom(k-b+r-3,r-3)/binom(k+r-1,r-1), 0<=b<=k.

In particular for k>=1,

p_(r,k)(1)=2k(r-1)(r-2)/[(k+r-1)(k+r-2)(k+r-3)].

For k=0 this probability is zero; for r=2 the single pair has deterministic total k. An odd terminal singleton has no mark. The state update is (r,k,z)->(r-2,k-b,(4/9)*2^b*z).

For r>=4 and 0<a<=k/r<=b_0<infinity, the elementary bound

p_(r,k)(1)>=p_*:=a/[2(b_0+1)^3]>0                     (1)

follows from r-1,r-2>=r/2, k>=ar and each denominator factor at most (b_0+1)r.

## 2. Exact martingale density

Fix t>0. Set p_j=P(B_(j+1)=1|F_j) and

g_j(t)=1-(1-exp(-t))*A_j*p_j.

Then exp(-t)<=g_j(t)<=1 and

E_P[exp(-t X_j)/g_j(t) | F_j]=1.

Consequently D_t=product_j exp(-t X_j)/g_j(t) is the terminal value of a positive mean-one martingale over the finite deterministic number of pairs. It defines a probability law Q_t^A by dQ_t^A=D_t dP. Exactly,

E_P exp(-t N_A)=E_(Q_t^A) product_j g_j(t).             (2)

At an opportunity, the new conditional transition is

Q_t^A(B_(j+1)=b|F_j)
=p_(r,k)(b)*exp(-t A_j*1_{b=1})/g_j(t).                (3)

It remains supported on endpoint-valid compositions. But it is generally NOT the uniform composition law and NOT cyclically invariant. In general it differs from the globally normalized Gibbs tilt exp(-t N_A)P/E_P exp(-t N_A). The two laws coincide if and only if product_j g_j(t) is P-almost surely constant.

For A_j counting every white entry, equation (2) is the exact row-normalization representation of the original dense recursion. For regular-white A_j, the inequality N_white>=N_A gives

E_P exp(-t N_white)<=E_(Q_t^A) product_j g_j(t).

For equations (4)-(5), assume p_j>=p_* whenever A_j=1, as ensured by the regular-cone choice above; no such uniform bound is asserted for every-white A on all states. Using (1), put kappa_t=-log(1-p_*(1-exp(-t))). Then

E_P exp(-t N_white)<=E_(Q_t^A) exp(-kappa_t W_A).        (4)

This direct transfer has no hard logarithmic threshold and no power loss. Its price is the changed opportunity law Q_t^A. An original-law occupation estimate cannot simply be substituted on the right side.

## 3. A finite counterexample to the naive original-law comparison

Take independent Bernoulli(1/2) coins U_1,U_2. Set A_1=1, A_2=U_1, so the second opportunity is predictable. Then

W=1+U_1, N=U_1+U_1 U_2.

The success hazard on every active opportunity is exactly p_*=1/2. With lambda=log 2 and g=1-(1-exp(-lambda))*p_*=3/4,

E 2^(-N)=1/2+(1/4)(1/2)+(1/4)(1/4)=11/16,
E (3/4)^W=(1/2)(3/4)+(1/2)(9/16)=21/32.

Since 11/16>21/32, the hazard condition does NOT imply E exp(-lambda N)<=E_P exp(-kappa W) under the original law. This is an abstract two-step counterexample to a proposed proof principle, not an actual Collatz-array counterexample. Equation (4) avoids the error by using Q instead of P.

## 4. Remaining under P incurs a Holder power loss

Fix t>lambda>0 and alpha=lambda/t. The exact identity

exp(-lambda N_A)=D_t^alpha*(product_j g_j(t))^alpha

and Holder with exponents 1/alpha and 1/(1-alpha), using E_P D_t=1, give

E_P exp(-lambda N_white)
<= [E_P exp(-lambda*kappa_t*W_A/(t-lambda))]^(1-lambda/t). (5)

For t=2lambda this is the square-root bound

E_P exp(-lambda N_white)<=sqrt(E_P exp(-kappa_(2lambda) W_A)).

Thus a C/R opportunity transform under the original law produces only R^(-(1-lambda/t)) via (5) at any fixed t. Taking t to infinity sends the inner Laplace parameter lambda*kappa_t/(t-lambda) to zero, so pointwise fixed-parameter estimates do not justify recovering the desired exponent.

Even assuming a bound of the form E_P exp(-s W_A)<=C/(sR) uniformly for small positive s, the choice t=lambda(1+log R) in (5) yields only O(log R/R): the inner s is kappa_t/log R and the outer exponent is log R/(1+log R). This illustrates the loss of this particular argument, not a theorem that all same-law approaches must fail.

## 5. The normalized kernel changes drift, without useful monotonicity

At a fixed state let mu=E_P B=2k/r, w=A_j and d_t=1-exp(-t), so g=1-d_t p_1 w. Formula (3) gives

E_Q B=(mu-d_t p_1 w)/g,
E_Q B-mu=d_t p_1 w*(mu-1)/g.                          (6)

At an active white state with k/r>1/2, the mean next-pair total weakly increases. Below that slope it weakly decreases. The change is strict when p_1>0. This alone gives no white-occupation estimate. When p_0>0 and P(B>=2)>0 at an active state, both Q(B=0)=P(B=0)/g and Q(B>=2)=P(B>=2)/g increase, so neither first-order stochastic dominance direction holds. Whiteness after z->(4/9)2^b z is itself nonmonotone.

## 6. A remaining-length-only supersolution cannot work

For the killed recursion, a comparison function H must satisfy

H(r,k,z)>=sum_b p_(r,k)(b)*exp(-lambda*w(z)*1_{b=1})
                    *H(r-2,k-b,(4/9)*2^b z).

At any low state z<eta, w(z)=0, so the row has total mass one. The trial H(r,k,z)=C/(r+1) therefore gives right side C/(r-1)>C/(r+1) for r>=3 and fails the supersolution inequality. More generally a strictly decreasing function of remaining length alone has this problem at a row with no killing.

These low states are genuinely reachable within regular remaining slopes: a fixed zero prefix sends z_0<2 below eta, while K/(R-2h)->beta on actual arrays. Thus this is not merely an issue at irrelevant k=0 endpoints. A successful supersolution must retain meaningful state dependence; no such successful function is supplied here.

## Exact remaining problem

Either bound E_(Q_lambda^A) exp(-kappa_lambda W_A) by C/R under the explicit changed law, construct a valid phase/height-dependent supersolution for the original killed recursion, or estimate the original marked transform through another argument. Uniform composition or cyclic-rank formulas cannot be reused under Q without a new comparison. XUB and Collatz remain open.
