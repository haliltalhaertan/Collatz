# Harmonic block budget: packing audit and exact missing condition

2026-09-08. Bounded independent analytic audit. No numerical search or external model call. The recorded CP17 upper bound is used on its stated positive injective odd-orbit domain; its full proof is not re-audited here.

## 1. Budget is correct

For an actual single orbit, let I=[u,v), ell=v-u, delta_I=A_v-A_u-alpha ell>0, and n_v>=n_u. Iterating the exact odd-step identity gives

    log(n_v/n_u) = -delta_I ln2 + sum_{i in I} log(1+1/(3n_i)).

Consequently delta_I <= sum_{i in I}(1/n_i)/(3 ln2). There is no omitted endpoint term: the sum uses u,...,v-1.

For nonnegative weights theta_I satisfying sum_{I containing i}theta_I<=1 at each i<N, summation gives the stronger fractional-packing form

    sum_I theta_I delta_I <= H_N/(3 ln2)
                            <= (K17+o(1)) ln ln N/(3 ln2).

The report's multiplicity-L_N bound follows by theta_I=1/L_N. The o(1) statement remains valid after that multiplication, with the usual asymptotic interpretation. No application to cycles is justified.

## 2. Exact sufficient packing condition

Let P_N be the maximum total delta over pairwise disjoint selected actual intervals contained in [0,N). Then

    P_N <= (K17+o(1)) ln ln N/(3 ln2).

Thus a contradiction would follow from limsup P_N/(ln ln N)>K17/(3 ln2). It suffices instead to exhibit any feasible fractional weights with a strictly larger limsup load. This condition is quantitative and concerns one actual orbit.

For a finite family of intervals, the fractional packing optimum equals the maximum-weight disjoint packing optimum. One elementary justification is that the incidence matrix has consecutive ones in every column, hence is totally unimodular: for any selected subset of rows, alternating signs in their time order give each column sum in {-1,0,1}. Integer capacities then give integral extreme points. This observation makes fractional packing a certificate format, but produces no additional load from an arbitrary family.

In particular, interval graphs of maximum overlap L can be colored with L colors by assigning each interval, in increasing start order, a color unused by currently active intervals. Each color is disjoint. One color has delta weight at least sum_I delta_I/L. This exactly recovers the existing multiplicity bound; it does not improve its asymptotic content for free.

## 3. Why infinitude cannot supply the missing lower bound

These are abstract interval counterexamples, not realizable Collatz counterexamples.

- Nested intervals [0,j), all of weight one, give infinitely many intervals but maximum disjoint weight one. Any claimed generic greedy extraction of unbounded disjoint load is false.
- Disjoint unit intervals starting at ceil(exp(exp(j))) have weight one each, but only order ln ln N total weight up to N. Infinitely many disjoint positive-weight intervals need not exceed the CP17 scale. Even sparser starts can make their count o(ln ln N).
- Disjoint intervals with weights 2^{-j} have finite total load despite infinitude. Positive delta is not a uniform positive gap when lengths grow.

Therefore one needs all three controls: actual same-orbit realization, enough weighted packing by time N, and a comparison exceeding the explicit CP17 coefficient. Blocks obtained from different scaled starting integers cannot be pooled into this budget without a new orbit-identification theorem.

## 4. Bounded-length greedy selection and its limitation

Suppose M_N distinct starts each supply one selected actual interval of length at most B. Greedily choose the earliest remaining start, keep its interval, and discard starts before its endpoint. Each choice discards at most B integer starts, so at least M_N/B intervals are selected disjointly.

Define g_B=min_{1<=ell<=B}(ceil(alpha ell)-alpha ell)>0, using irrationality of alpha=log_2 3. Every positive delta on such an interval is at least g_B. Hence

    g_B M_N/B <= (K17+o(1)) ln ln N/(3 ln2).

For variable B=B_N the formula remains a sufficient test, but g_B can shrink and the factor B grows. Neither cost may be dropped.

There is a stronger elementary limitation for each FIXED B: only finitely many such paradoxical blocks can occur on a positive injective orbit. Choose Q>B/(3 ln2 g_B). Injectivity implies that eventually every n_i>Q. A subsequent length-at-most-B block would then have

    delta_I <= B/(3 ln2 Q)<g_B,

a contradiction. This does not use CP17. Thus a useful proposed extraction must genuinely handle growing block lengths; promising a fixed bounded length infinitely often would already conflict with elementary injectivity.

## Verdict

The existing harmonic budget is valid on its declared domain. Packing reorganizes it cleanly but does not convert qualitative infinitude into an excessive lower load. A precise open target is a same-orbit family with feasible weighted interval packing whose load beats K17 ln ln N/(3 ln2). No such family is constructed here, and no new orbit exclusion follows.
