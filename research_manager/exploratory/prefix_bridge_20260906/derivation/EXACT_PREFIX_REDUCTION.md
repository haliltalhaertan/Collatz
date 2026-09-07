# Exact prefix reduction and logarithmic prefix cutoff

Date: 2026-09-06. Status: NEW EXPLORATORY DERIVATION, submitted for independent audit; not canonical acceptance and not a B4 theorem. No sealed source was run. All statements below are proved algebraically from the analytic observable and uniform-composition law; no numerical cancellation is used.

## 1. Domains and connection to the analytic observable

Write e_M(x)=exp(2 pi i x/M). Let r>=5 and n>=0 be integers. Let z=(z_1,...,z_r) be uniform on weak compositions of n into r parts, a_i=z_i+1, and T=r+n. Define A_0=0, A_j=sum_{i<=j} a_i and

    B_r(a)=sum_{s=1}^r 3^(r-s) 2^(A_(s-1)).

The frozen PROJECT_DEFINITIONS analytic observable is zeta_4 times the row phases exp(2 pi i 2^(s+S_(s-1)-5)/3^s) for s>=2, with zeta_4=e_48(1). Since A_(s-1)=s-1+S_(s-1), every row phase including s=1 is exp(2 pi i 2^(A_(s-1))/(16*3^s)). Multiplying gives EXACTLY

    F_r(a)=e_(16*3^r)(B_r(a)),     G_(r,n)=E[F_r | sum z=n].

No replacement of an analytic negative power of two by a modular inverse occurs here. For r<5 the original finite expression remains defined, but the four-prefix/tail formulas below are not asserted: r=4 would require an empty-tail convention. On the critical target n=floor(beta*r)-8, beta=log_2(3)-1, the conditional law exists for r>=14; r=14,15 have n=0 and are covered by the identities despite being degenerate. r=12,13 are not in the domain.

## 2. Finite mod-16 information is not finite tail-frequency closure

For r>=4, B_r mod16 equals the first four summands mod16. All later terms contain 2^(A_(s-1)) with A_(s-1)>=4. Therefore B_r mod16 is determined by r mod4 and the truncated values min(a_1,4), min(a_2,4), min(a_3,4). This gives at most 4^3 prefix classes for each r mod4; no minimality is claimed. The fourth summand depends on the first three increments, not the fourth.

For any integers u,v with 16u+3^r v=1, CRT gives

    e_(16*3^r)(B_r)=e_(3^r)(u B_r) e_16(v B_r).

B_r and v are odd, so the second factor is never 1. It is determined by the stated finite prefix data and r mod4 (v is the inverse of 3^r modulo16). This does not imply that the rest of the observable can be represented by a fixed finite collection of tail frequencies independent of r.

## 3. Four-prefix decomposition: exact pathwise identity

Put m=r-4>=1. Fix the first four positive increments p=(a_1,a_2,a_3,a_4), let A=sum p_i=4+j and j=sum_{i<=4} z_i. Let b=(a_5,...,a_r). Define B_4(p) by the same formula as B_r. Directly splitting the sum gives

    B_r(a)=3^m B_4(p)+2^A B_m(b).

Consequently,

    F_r(a)=e_1296(B_4(p)) e_(3^(m+4))(2^j B_m(b)).                 (P)

The second factor has no dyadic denominator because A>=4. Its modulus is 3^(m+4), NOT 3^m. The coefficient 2^j is a unit modulo this modulus; the factor 3^4 in the conductor cannot be cancelled. The first factor depends only on p_1,p_2,p_3; p_4 nevertheless affects j and the conditional tail law.

## 4. Conditional law and normalized scalar mixture

Let J=sum_{i<=4} z_i. For 0<=j<=n, define

    C4(j)=binom(j+3,3),    Cm(n-j)=binom(n-j+m-1,m-1),
    N(r,n)=binom(n+r-1,r-1),
    w_(r,n)(j)=C4(j) Cm(n-j)/N(r,n).

Given J=j, the first four excess increments are uniform weak compositions of j, the remaining m are uniform weak compositions of n-j, and the two vectors are independent. This follows by counting pairs: each pair corresponds to exactly one full composition, all of equal weight 1/N. In particular sum_j w_(r,n)(j)=1.

Define

    D_j = (1/C4(j)) sum_(x_1+...+x_4=j) e_1296(B_4(x+1)),

    H_(m,k)(j) = (1/binom(k+m-1,m-1))
                 sum_(y_1+...+y_m=k) e_(3^(m+4))(2^j B_m(y+1)).

All summation variables are nonnegative integers. These definitions include m=1 and k=0. Both D and H have modulus <=1. Taking expectations in (P) yields the exact identity

    G_(r,n)=sum_(j=0)^n w_(r,n)(j) D_j H_(r-4,n-j)(j).           (M)

Thus averaging the entire prefix at fixed J leaves only the scalar j. No unconditioned independence approximation was used. The tail endpoint is n-j, its length r-4, its conductor 3^r, and its frequency 2^j. At the critical target its excess offset relative to beta*(r-4) is 4*beta-8-theta_r-j, where theta_r={beta*r}; it drifts with j and is not a fixed-offset family.

## 5. Proposed rigorous logarithmic prefix-cutoff lemma

For r>=5, n>=0 and an integer q>=0 with q<=n, translation of z_1 by q gives

    P(z_1>=q | sum z=n)
      = binom(n-q+r-1,r-1)/binom(n+r-1,r-1)
      = product_(h=0)^(q-1) (n-h)/(n+r-1-h)
      <= (n/(n+r-1))^q.

For q>n the probability is zero. For n=0 and q>=1 it is also zero. Each fraction in the product is <= n/(n+r-1), since r-1>0. By exchangeability and a union bound, for any integer L>=0, setting q=floor(L/4)+1 gives

    P(J>L | sum z=n) <= 4 (n/(n+r-1))^q.                       (C)

Indeed J>L forces at least one of its four nonnegative summands to exceed floor(L/4). If q>n use the zero-probability case; the displayed upper bound still holds.

Now n=n_r=floor(beta*r)-8, r>=14, alpha=1+beta, and rho=beta/alpha in (0,1). Since n_r<=beta*r-8<=beta*(r-1),

    n_r/(n_r+r-1) <= rho.

For a fixed delta>0 define the integer cutoff

    L_r=ceil(4*(1+delta)*log(r)/abs(log(rho))),

where log is the natural logarithm. Then q=floor(L_r/4)+1>L_r/4, and

    P(J>L_r | sum z=n_r) <= 4*r^(-1-delta).

Using |D_j H|<=1 in (M) proves the finite complex-sum error bound

    |G_(r,n_r) - sum_(j=0)^min(n_r,L_r) w_(r,n_r)(j) D_j H_(r-4,n_r-j)(j)|
       <= 4*r^(-1-delta) = o(1/r).                             (T)

This is ONLY a prefix-excess truncation bound. It is not a spatial-offset truncation theorem, not uniform compactness of a profile, not arithmetic cancellation, and not an upper or lower estimate of order 1/r for G. It concerns a new analytic cutoff and does not change any historical sealed numerical window. No numerical run under this cutoff is requested.

## 6. Exactly one next candidate lemma

The one proposed next estimate for the upper-scale question is the TRIANGLE-WEIGHTED LOGARITHMIC-PREFIX CANCELLATION LEMMA: for one fixed delta>0 and the cutoff above, prove or refute existence of C and r0 such that, for all r>=r0,

    sum_(j=0)^min(n_r,L_r) w_(r,n_r)(j) |D_j| |H_(r-4,n_r-j)(j)| <= C/r. (OPEN)

This weighted bound follows from a uniform C/r bound on every H in the window, but does not require that stronger assertion. By the triangle inequality and (T), it would imply G=O(1/r). It discards cancellation BETWEEN prefix classes while retaining cancellation WITHIN each tail average. It is therefore a stronger sufficient requirement than the signed truncated-sum bound, which (up to the o(1/r) error) simply restates the original upper-bound problem. No strict separation between these conditions for THIS particular family has been proved. The triangle-weighted requirement could fail even if the desired signed bound holds; such a failure would reject this sufficient route, not the original conjectural scale. This is not a claim that prefix reduction has substantially reduced the difficulty. A nonzero 1/r asymptotic needs additional convergence and nonvanishing and is NOT implied. Finite mod-16 classification alone supplies none of these estimates.

Nothing in this exploratory derivation proves Collatz. No E6-N2 or B4 acceptance is claimed. Independent audit is required before any downstream use.
