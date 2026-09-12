# Exact affine-state recursion for shifted parity weights

12 September 2026. Independent mathematical derivation and bounded checks. No Collatz convergence theorem or uniform concentration bound is claimed.

## Concrete conclusion

The shifted joint parity-weight polynomial does close after adjoining an odd affine slope. A memoized recursion for ONE specified shift has at most O(sqrt(s) 2^(s/2)) distinct states, rather than a full 2^s residue enumeration. Each state carries a bivariate polynomial, so polynomial arithmetic and coefficient bit lengths must also be counted. This is a genuine exact computational reduction, not yet a bound for the fourth moment over ALL shifts.

## Definitions and recursion

Let H(v)=(3v+1)/2 on odd v and v/2 on even v. Let K_n(v) count odd parities during the first n shortcut steps. K_n depends only on v modulo 2^n. Define

    Q_n(a,b;x,y) = sum_(v mod 2^n) x^K_n(v) y^K_n(av+b),

for odd a, and J_n(d)=Q_n(1,d). All affine parameters are residue classes modulo 2^n. Q_0=1.

For n>=1, take integer representatives a,b, put q=2^(n-1), and for e=0,1 set

    f = (a e+b) mod 2,
    a' = 3^(f-e) a mod q,
    b' = [3^f(a e+b)+f]/2 - 2e a' mod q.

The division by 2 in this expression is ordinary integer division of an EVEN numerator. The negative exponent uses the inverse of 3 modulo q. At q=1 both parameters are zero and Q_0=1, so no inverse convention is needed. Then

    Q_n(a,b;x,y) = sum_(e=0,1) x^e y^f Q_(n-1)(a',b';x,y).

Proof: write v=2w+e. Then H(v)=3^e w+2e and H(av+b)=3^f a w+[3^f(ae+b)+f]/2. Change variables z=3^e w+2e modulo q; this is bijective because 3 is odd. The two subsequent trajectories are z and a'z+b', respectively. Their weights gain the initial e and f. The formulas are independent of the selected integer representatives modulo 2^n.

Caution: the alternate rational-looking formula b'=(3^f b+f-e a')/2 is unsafe if a' has ALREADY been reduced modulo q: dividing a changed representative by two can change the result modulo q. The integer formula above avoids this implementation error.

## Where translation-only closure breaks

For d=2c the two first parities coincide:

    J_n(2c) = J_(n-1)(c) + xy J_(n-1)(3c).

For d=2c+1 they differ:

    J_n(2c+1)
      = y Q_(n-1)(3,3c+2;x,y)
        + x Q_(n-1)(3^(-1),c+3^(-1);x,y).

The inverses here are 2-adic residues at the remaining precision. Via the exact variable-swap symmetry

    Q_n(a,b;x,y)=Q_n(a^(-1),-a^(-1)b;y,x),

one may instead write the second term as

    x Q_(n-1)(3,-3c-1;y,x).

Thus an odd shift creates an affine slope 3 or 1/3. For remaining modulus >=4 that affine map is not a translation map. This proves the obstruction to the naive pointwise translation-state recursion; it does NOT rule out some additional nontrivial identity among generating polynomials that could remove slopes.

A useful exact high-valuation formula follows by iterating the even branch. For 0<=ell<=n,

    J_n(2^ell c)
      = sum_(h=0..ell) binom(ell,h) (xy)^h J_(n-ell)(3^h c).

In particular,

    J_n(2^(n-1))=(1+xy)^(n-1)(x+y).

This recovers the sibling-shift binomial identity and extends it to every prescribed 2-adic shift valuation. Odd shifts still need the affine state.

## Rigorous memoization bound for one root shift

Start from a=1. At depth d every slope is congruent to 3^delta, where -d<=delta<=d; this follows because each branch changes delta by f-e in {-1,0,1}. At remaining precision n=s-d, canonical residues b have at most 2^n possibilities. Therefore the number N_d of distinct reachable states satisfies

    N_d <= min(2^d, (2d+1) 2^(s-d)).

Different powers of 3 can coincide modulo 2^n, which only improves this upper bound. Let M=2s+1 and D=ceil((s+log2 M)/2), clipped to s if needed. Summing the tree bound before D and the residue bound after D gives

    sum_d N_d = O(sqrt(s) 2^(s/2)).

A simple derivation uses sum_(d<=D)2^d <2^(D+1) and sum_(d>D) M 2^(s-d) <=M 2^(s-D). This is a worst-case bound uniform in the chosen starting shift d; it is not inferred from measured state counts.

Every Q_n has degrees at most n in each variable, and coefficients are nonnegative integers summing to 2^n. A naive dense representation thus gives at most O(s^2) integer operations per state, each on O(s)-bit integers. Hence an explicit safe arithmetic-operation bound is

    O(s^(5/2) 2^(s/2)),

with another polynomial factor if bit operations rather than integer additions are counted. Memoization must key the remaining precision and BOTH canonical affine residues. No assumption of independent parity bits between the two trajectories is made.

For all 2^s root shifts jointly, the corresponding state bound at depth d is at most (2d+1)2^(s-d), giving fewer than 6*2^s states after summing the geometric series. Thus all-shift memoization is near-linear in the number of shifts up to polynomial factors, not a square-root-exponential computation for the entire fourth moment. Existing FFT autocorrelation for a fixed concrete filter is already O(s2^s) in numerical arithmetic; this recursion is especially meaningful for one/few shifts or joint coefficient information, not an unqualified replacement for FFT.

## Exact checks made independently

A separate inline Python implementation used Counter-valued bivariate coefficients and direct shortcut iteration. For every n=1..7 it checked every b modulo 2^n; for n<=4 it checked every odd slope, and for n>=5 it checked the four slopes 1,3,5,2^n-1. In total 1066 affine polynomial comparisons matched exactly. These checks supplement the proof; the identities above are not restricted to n<=7.

State-only traversal for J_s(1), merging exact canonical (a,b) residues, gave:

| s | Total memo states across all depths | Largest depth | Residues in direct enumeration |
|---|---:|---:|---:|
|8|47|11|256|
|12|214|55|4096|
|16|859|209|65536|
|20|3273|782|1048576|
|24|11499|2475|16777216|

These timings/states do not measure full bivariate polynomial arithmetic. The table is finite evidence only; the preceding state bound is proved separately.

## Connection to the actual filter and what remains open

For the actual filter F(v)=binom(t-s,j-K_s(v)), let g_h=binom(t-s,j-h). If [x^a y^b] J_s(d)=N_(a,b)(d), then its cyclic autocorrelation is exactly

    C(d)=sum_(a,b) g_a g_b N_(a,b)(d).

Thus Q computes the exact object needed for the fourth-moment expression

    Tr(beta^2)=2^(s-1) sum_(0<=d<2^(s-1)) [C(d)-C(d+2^(s-1))]^2.

But coefficient computation and the unweighted state-count bound do not control these weighted squared differences uniformly. A successful analytic continuation would need a weighted transfer inequality, or a rigorously controlled approximation of many shifts, that survives the affine slope/intercept evolution. No fixed-cardinality affine state space, uniform C_Y bound, or bound on the actual source-filter alignment has been proved here.
