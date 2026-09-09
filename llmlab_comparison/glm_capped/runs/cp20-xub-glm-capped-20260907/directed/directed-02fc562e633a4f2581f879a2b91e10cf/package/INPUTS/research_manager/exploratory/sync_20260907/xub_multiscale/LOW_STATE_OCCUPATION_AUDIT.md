# Low-state occupation audit

Date: 2026-09-07

Verdict: `[NAIVE RARITY REFUTED / OCCUPATION-LAPLACE ROUTE OPEN]`.

## Exact state and marginal law

At pair time `j`, with `h=2j`,

`z_j=z_0*2^(S_h-beta*h)`, `z_0 in (1,2)`.

Conditional on `S_R=K`, the partial sum has the exact beta-binomial law

`P(S_h=a | S_R=K) = binom(a+h-1,h-1) binom(K-a+R-h-1,R-h-1) / binom(K+R-1,R-1)`.

Its mean and variance are

`E[S_h | S_R=K]=hK/R`,

`Var(S_h | S_R=K)=K*h*(R-h)*(K+R)/(R^2*(R+1))`.

For actual central arrays `K=beta*R+O(1)` and bulk `h/R`, the variance is `Theta(R)`. The low threshold

`S_h-beta*h < log_2(eta/z_0)`

is only `O(1)` from the conditional mean. Uniform beta-binomial Stirling/CLT therefore gives

`P(z_j<eta | S_R=K) -> 1/2`

at every fixed bulk fraction. Low-state visits are not rare.

## Exact positive-probability entrance mechanism

Choose fixed `L_eta` with `2*(4/9)^(L_eta)<eta`. If the first `2L_eta` raw increments vanish, then `z_(L_eta)<eta`. Exactly,

`P(Y_1=...=Y_(2L_eta)=0 | S_R=K) = binom(K+R-2L_eta-1,R-2L_eta-1)/binom(K+R-1,R-1)`.

As `K/R -> beta`, this tends to `(1+beta)^(-2L_eta)>0`.

## Why step counting fails

For `b=0`, `|A_0|=1` and `z` is multiplied by `4/9`. For a low `b=1` run, `z_j=z_0(8/9)^j` and

`product_j |A_1(z_j)| = product_j |cos(pi*z_0(8/9)^j)|`

can converge to a positive limit because `sum_j z_j^2<infinity`. Hence neither low-state hits nor low-step count supplies deterministic exponential contraction.

## Correct open target

Let

`M_eta=#{0<=j<J: log_2 z_j >= log_2 eta}`.

The direct occupation target is

`E[exp(-lambda*M_eta) | S_R=K] <= C/R`.

A closer-to-application marked version counts only regular entries whose next symbol is positive and bounded. A cycle-lemma/Chung-Feller mechanism is plausible, but three exact issues remain:

1. chord-centering `S_h-hK/R` can have rational ties;
2. the actual threshold is an affine bounded shift, not zero;
3. only even raw times are sampled, with a possible final singleton.

Thus the Laplace estimate is a precise open lemma, not a consequence already available from an off-the-shelf occupation identity.

