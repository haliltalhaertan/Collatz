# Adversarial tail control: valid bound, exact ceiling, literature alternative

2026-09-08. Principal, audit_cancellation and attack_local. All computations local; no paid calls or new orbit exclusion. This round tests whether coupling an exposed shortcut prefix to its remaining tail surpasses the earlier exponent ceiling.

## 1. Pointwise tail shortcuts fail

The attack agent supplied critical examples with entirely odd unexposed tails. In shortcut notation H(x)=x/2 if even and (3x+1)/2 if odd:

* r12,A19,m14,t5: x231 has prefix weight7 and H^14(x)=31; all next5 states are odd.
* r16,A25,m19,t6: x2805 has prefix weight10 and H^19(x)=319=-1 mod64; all next6 states are odd.

Thus one cannot demand even a single zero in every such tail. Its separate infinite inverse-tree construction gives linear all-odd tails under the small-start condition, but does NOT enforce the critical mass band; that limitation is retained. Neither observation disproves a statistical upper count.

## 2. A genuinely coupled finite bound

Let x be positive odd below2^m, y=H^m(x), and k the number of odd states in the first m steps. The affine identity is

    2^m y=3^k x+C.

Canonical residue reconstruction gives 1<=y<3^k. Swapping adjacent parity bits10 to01 increases the affine offset. Moving all k ones to the end therefore gives

    0<=C<=Cmax=2^(m-k)(3^k-2^k).

For a fixed y, possible x values lie in an interval of width Cmax/3^k<2^(m-k). There are at most2^(m-k)+1 positive odd starts in that interval (a deliberately conservative bound). This does not assert x->y is injective.

Let t=A-m and j=r-k. Exactly binom(t,j) residue classes modulo2^t give a length-t tail of parity weight j. Each has at most ceil(3^k/2^t) representatives in [1,3^k). Thus the count with prefix weight k satisfies

    N_k <= min{binom(m-1,k-1),
               binom(t,r-k)*ceil(3^k/2^t)*(2^(m-k)+1)}.

Sum over max(1,r-t)<=k<=min(m,r). The factors come from covering integer endpoints and bounding their fibers, not from treating prefix and suffix as independent. The audit agent proposed this bound and the principal verified it on all4095 odd starts for m1..12, using t=max(1,floor(m/3)). Every affine, height and counting inequality passed; see check_height.py and HEIGHT_RESULT.json.

## 3. Exact obstruction to surpassing the old ceiling with THIS bound

Write alpha=log_2 3, b=m/r, t0=alpha-b, and s=k/r, with A=alpha*r+O(1). Up to subexponential factors the upper-bound expression has exponent

    Gamma(b)=max_s min{b H2(s/b),
                 b-s+max(alpha*s-t0,0)+t0 H2((1-s)/t0)},

where max(0,1-t0)<=s<=min(b,1). This expression can improve the exposed-prefix bound at some fixed b. But the feasible value s=b/alpha forces

    Gamma(b)>=b H2(1/alpha)=b h*/alpha.

Proof: at s=b/alpha the first term is bH, H=H2(1/alpha). The second minus first is

    b(1-1/alpha)+(alpha-2b)H >=0, if b<=alpha/2;
    3b-b/alpha-alpha+(alpha-2b)H, if b>=alpha/2.

The second expression is affine in b and positive at both endpoints: (alpha-1)/2 at b=alpha/2 and 2alpha-1-h* at b=alpha. Hence it stays positive. Feasibility follows from s-(1-t0)=(alpha-1)(1-b/alpha)>=0. The audit agent independently checked all signs and endpoints.

Consequently the existing orbit criterion Gamma(b)<b/kappa cannot be achieved by this certificate for kappa>=alpha/h*=1.0526808586. In particular it cannot reach1.053. This is an obstruction to the upper-bound METHOD, not a lower bound for the actual number of paths. No grid optimization is needed for this ceiling proof.

## 4. A directly relevant literature alternative, with a rate obligation

Primary source: Manuel Inselmann, An Approximation of the Collatz Map and a Lower Bound for its Average Total Stopping Time, v3 (2024), https://arxiv.org/html/2402.03276 . Definition2.6 defines *-density by a power bound on the exceptional count. Theorem2.18 gives such density for simultaneous trajectory approximation throughout the stated logarithmic horizon; Lemma2.16 supplies a pullback step. This is stronger than using only the density-one wording of the introduction. We have not extracted a sufficiently large numerical exceptional exponent from its proof.

Our deduction from that theorem: write d0=1-alpha/2, take epsilon=.1, b=1.2. The theorem provides some D_epsilon>0 outside an exceptional set of count O(X^(1-D_epsilon)), with H^A(x)<=2^(-d0 A)x^(1+epsilon) whenever A<=log_2(x)/d0. For our selected starts, H^A(x)>=2^(-O(1))*x because total shortcut parity weight is r and A=alpha*r+O(1).

Split off x<2^(.5r). Above this threshold the time horizon is valid, since .5/d0>alpha. Also x<=2^(br+o(r)) implies 2^(-d0 A)x^epsilon tends exponentially to zero because d0*alpha>.1b. Hence selected starts in that range must be exceptional. Therefore

    F(X)<=2^(.5r)+O(2^(b(1-D_epsilon)r+o(r))).

This supplies an existential positive power saving without an independence assumption. It does not certify that it is stronger than our prior explicit bounds. To reach kappa1.053 by this route at b1.2 requires a verified D_epsilon>1-1/1.053, approximately0.0503324; no such rate was obtained this round. Extracting the actual constants, rather than reading 'almost all' as sufficient, is the next specific literature task.

## Decision and scope

Do not keep tuning the exposed-prefix/height certificate: its exact exponent ceiling is now proved. Preserve it as a valid baseline. The surviving option examined here is the quantitative pullback mechanism from the cited source; continue only with explicit error-exponent accounting. The critical infinite orbit class remains unexcluded, and neither finite all-odd tails nor certificate ceilings imply it exists.
