# Independent initial audit: finite-prefix phase bridge

Status: exploratory analytic audit, not a sealed-stage result. This report was derived solely from the definitions supplied in the assignment, before inspecting other agents' sources or outputs. No old sealed source was run.

## Definitions and exact statements

Let a_1,...,a_r be positive integers, T their sum, A_j=sum_{i<=j}a_i and A_0=0. Put B_r(a)=sum_{j=1}^r 3^(r-j) 2^A_{j-1}; the project phase is exp(2 pi i B_r/(16*3^r)). Let e_m(z)=exp(2 pi i z/m).

For r>=4, modulo 16 only j<=4 contribute: every j>=5 has A_{j-1}>=4. Consequently B_r mod 16 is determined by r mod 4 and (min(a_1,4),min(a_2,4),min(a_3,4)). This gives at most 64 prefix labels for each r residue, not necessarily 64 distinct phase values. B_r is odd.

Choose integers u,v with 16u+3^r v=1. Then exactly

    e_(16*3^r)(B_r) = e_(3^r)(u B_r) e_16(v B_r).

The second factor is constant on each truncated-prefix label at fixed r. It is not generically 1. Its dependence on r is through r mod 4. These are equalities of complex numbers; integer representatives u,v need not be unique.

## What finite classification does not accomplish

A finite prefix label does NOT fix the actual sum P=a_1+a_2+a_3. A label containing 4 stands for any integer >=4. Therefore conditioning on a label leaves an unbounded set of possible P as T grows. It also leaves corresponding powers 2^P in the ternary phase and a varying tail total T-P. A claim that this classification alone closes a fixed finite-dimensional transfer state is unsupported.

For a fixed exact prefix b=(a_1,...,a_h), set P=sum b, R=r-h, and let c=(a_(h+1),...,a_r). Algebraically,

    B_r(a) = 3^R B_h(b) + 2^P B_R(c).

Thus the original phase factors as

    e_(16*3^h)(B_h(b)) * e_(16*3^r)(2^P B_R(c)).

For h=4, P>=4, so the tail factor becomes e_(3^r)(2^(P-4) B_R(c)). Its modulus is still 3^r, not 3^R. Since 2^(P-4) is a unit modulo 3, the extra 3^h conductor cannot generally be cancelled. Calling this tail the same natural depth-R observable without an additional frequency/conductor parameter would be incorrect.

## Correct conditional law

For T>=r, the positive compositions of T into r parts are uniformly distributed under IID positive geometric variables conditioned on their total, for every admissible geometric parameter. There are binom(T-1,r-1) compositions.

For h<r and a specified positive prefix b with P<=T-R, its conditional probability is

    w_b = binom(T-P-1,R-1) / binom(T-1,r-1).

Conditioned on that prefix, the remaining vector is uniformly distributed over positive compositions of T-P into R parts. Summing the preceding exact phase factorization against these weights gives an exact prefix-mixture identity. Impossible prefixes have probability zero; do not assign a conditional normalized kernel to a zero-probability event without an explicit convention. The R=0 case is separate and deterministic.

If X is the ternary factor e_(3^r)(uB_r), and c ranges over the at most 64 labels, then

    E[project phase | total T] = sum_c z_c Pr(c | T) E[X | c,T],

where z_c=e_16(vB_r) on that label. Labels with probability zero can instead be handled safely by unnormalized terms E[X 1_c | T].

## Missing estimates and verdict

The finite mixture is exact but supplies neither an O(1/r) estimate nor a nonzero asymptotic coefficient. For an upper bound it suffices to bound each unnormalized class contribution by O(1/r), uniformly over the finite labels and r. If estimates instead condition on exact prefixes, their constants and errors must be summable against w_b uniformly; pointwise-in-prefix results do not suffice.

Even if every class has a uniform 1/r asymptotic, summing their complex coefficients can give zero. Nonzero per-class coefficients alone do not establish a nonzero total coefficient. A polynomial lower bound requires additional noncancellation information.

Verdict: the finite-prefix CRT classification and exact prefix-mixture identity are valid elementary algebra. A closed finite-state long-block problem, a uniform cancellation estimate, and nontriviality of its recombined coefficient remain OPEN. This audit is intentionally independent of any implementation and any pending producer output.
