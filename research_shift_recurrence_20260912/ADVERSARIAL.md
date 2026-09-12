# Independent adversarial audit of the shift recurrence

2026-09-12. This audit derives the identities from the shortcut map, checks modular carries, and separates a single-shift computational reduction from the still-open uniform moment bound. No publication or paid calls were made by this auditor.

## 1. The affine recurrence passes the carry audit

Let H(v)=v/2 for even v and (3v+1)/2 for odd v. Write K_n(v) for the number of odd entries during its first n steps, and

    Q_n(a,b;x,y) = sum_(v mod 2^n) x^K_n(v) y^K_n(av+b),

where a is odd. The second argument of K is interpreted modulo 2^n. First n parity bits depend only on this residue, so this is well defined. Q_0=1.

Choose integer representatives a,b modulo 2^n, set v=2u+e, e in {0,1}, and put

    f = (a e+b) mod 2,
    c = (a e+b-f)/2,
    q = 2^(n-1),
    a' = 3^(f-e) a mod q,
    b' = 3^f c+2f-2e a' mod q.

Negative powers of 3 mean modular inverses. The exact identity is

    Q_n(a,b;x,y) = sum_(e=0,1) x^e y^f Q_(n-1)(a',b';x,y).

Indeed H(2u+e)=3^e u+2e and H(a(2u+e)+b)=3^f(au+c)+2f. Substitute z=3^e u+2e; this is a bijection modulo q. The second endpoint is then a'z+b'. Nothing about independence, equidistribution, or bounded carries is assumed.

The main agent's equivalent formula

    b' = (3^f(ae+b)+f)/2 - 2e a' mod q

is correct: its numerator is even, and it equals 3^f c+2f. Integer division must be applied before reduction to q. Reducing a or b modulo 2^n first is safe: changing representatives adds a multiple of q after the division. Reducing them prematurely modulo q is NOT safe. For example Q_2(1,2)=(x+y)(1+xy), while Q_2(1,0)=(1+xy)^2.

Independent scalar enumeration against an independently written recursive implementation checked every odd a and every b for n=1,...,6: 2,730 affine states, all coefficients exactly equal. This confirms implementation cases; the derivation above establishes the identity for general n.

## 2. Translation states alone do not close

Writing J_n(d)=Q_n(1,d), an even shift gives the particularly simple exact recurrence

    J_n(2h)=J_(n-1)(h)+xy J_(n-1)(3h).

For an odd shift,

    J_n(2h+1;x,y)
      = y Q_(n-1)(3,3h+2;x,y)
        + x Q_(n-1)(3,-3h-1;y,x).

The mixed-parity branches create relative slope 3. They cannot generally be relabelled as ordinary translations. For example Q_2(3,2) differs as a polynomial from every J_2(d), d=0,1,2,3. The same nonmatch was checked for Q_n(3,2), n=3,...,6. A bijective change of variable in one coordinate must also be made in the other; treating two marginal bijections as independent changes the joint distribution.

Why retain affine slope? Because odd and even shortcut branches have different slopes. Why retain the full offset modulo the current ring? Because the removed carry changes the next parity word. These are necessary state information, not cosmetic generalizations.

## 3. A useful exact collapse for shifts divisible by powers of two

Repeatedly applying the even recurrence gives, for 0<=ell<=n and any integer h,

    J_n(2^ell h)
      = sum_(k=0,...,ell) binom(ell,k) (xy)^k J_(n-ell)(3^k h).

The proof is induction: multiplication by 3 commutes with the shift-halving branch and the binomial coefficients combine by Pascal's identity. In particular,

    J_n(0)=(1+xy)^n,
    J_n(2^(n-1))=(x+y)(1+xy)^(n-1).

This recovers the exact sibling relation, and costs only ell+1 terminal shift states rather than the 2^ell unmerged recursion branches. It does not handle all odd shifts by itself; half of all shifts are odd.

## 4. The proposed single-shift square-root exponential reduction is rigorous

For a root (a,b)=(1,d), after depth ell every slope is 3^delta modulo 2^(n-ell), with |delta|<=ell. This follows directly from multiplying a by 3^(f-e) at each step. Thus there are at most 2ell+1 possible slopes and 2^(n-ell) offsets at that depth. There are also only 2^ell paths in the unmerged binary recursion tree. The number of distinct cached states at depth ell is therefore at most

    min(2^ell, (2ell+1) 2^(n-ell)).

Summing this bound gives O(sqrt(n) 2^(n/2)) states. For a direct proof, replace 2ell+1 by 2n+1 and split the sum at ell0=floor((n+log2(2n+1))/2). The initial geometric sum is O(2^ell0), and the terminal sum is O((2n+1)2^(n-ell0)); both are O(sqrt(n)2^(n/2)). Finitely many small n are absorbed into the constant.

This is a genuine worst-case state-count improvement for ONE shift, without any unproved bounded-carry assumption. It is not polynomial in n. The state bound alone is not the arithmetic cost: a dense Q_m polynomial has at most (m+1)^2 coefficients, and coefficients have O(n) bits. Shift-and-add polynomial assembly and modular arithmetic add polynomial factors. A safe description is poly(n) 2^(n/2) bit complexity, not O(sqrt(n)2^(n/2)) total runtime. Cache both variable orderings correctly if using the swapped-variable odd formula; the general affine recurrence avoids that issue.

If ALL root shifts d modulo 2^n share one cache, their union has at most (2ell+1)2^(n-ell) states at depth ell. Hence the total affine state count over every shift is less than or equal to

    2^n sum_(ell>=0) (2ell+1)/2^ell = 6 * 2^n.

This is a useful exact shared-cache bound, with polynomial factors for coefficient storage/assembly. It remains exponential; there are already 2^n requested output polynomials. Computing each shift separately and multiplying the single-shift bound would miss this sharing.

## 5. What the recurrence does not prove

The filter autocorrelation follows by coefficient contraction:

    C(d) = sum_(i,j) [x^i y^j] J_n(d) * B(i) B(j),
    B(i)=binom(t-n, target_weight-i).

The primitive fourth moment is (2^(n-1)) times sum_(0<=d<2^(n-1)) [C(d)-C(d+2^(n-1))]^2. Every Q coefficient is nonnegative, but this last expression involves signed differences BEFORE squaring. Bounding its two C terms independently can lose the essential cancellation. The recurrence gives exact computation and a structured object for further estimates; no uniform C_Y bound or bound on source/filter alignment follows just from nonnegativity or state compression.

A compact scalar recurrence for the global fourth moment would be a further result: squaring couples different recursion branches and usually requires a higher-order joint state. A proof must explicitly show closure for those cross terms. The present audit supports the affine recurrence and its single-shift complexity improvement, while rejecting any automatic claim that the filter moment or Collatz problem is now controlled.

## 6. Cross-audit of exact_moment.py and ALGORITHM.md

The Kronecker substitution implementation passes the independent mathematical/code audit. For nonnegative integer entries v[i], every linear product coefficient of v and its reversal is an inner product between two subsequences, each using every original index at most once. Cauchy-Schwarz therefore bounds each coefficient by Q=sum(v[i]^2), including the central coefficient, which equals Q. Selecting B=256^width strictly greater than Q prevents every positional carry. The code's width=max(1,ceil(bit_length(Q)/8)) correctly gives strict inequality, including Q=0 and Q an exact power of 256. Input entries themselves fit in a digit, since an integer v[i]>=1 satisfies v[i]<=v[i]^2<=Q. Thus the fixed-width little-endian input packing and output decoding are sound. The product fits in exactly 2n-1 base-B positions; zero padding via to_bytes is safe.

The cyclic fold is also correct: a[n-1+d] sums nonwrapping pairs separated by d, while a[d-1] sums the wrapping pairs. Their sum is C[d]. No FFT, approximate reconstruction, or unproved prime/rounding assumption is used.

For n=2H, the sum of odd characters is H at displacement zero, -H at displacement H, and zero otherwise. Hence M2=H(C[0]-C[H]). Applied to the squared Fourier transform of the real cyclic correlation sequence, this gives

    M4 = H sum_(d=0,...,n-1) C[d](C[d]-C[d+H])
       = H sum_(d=0,...,H-1) (C[d]-C[d+H])^2.

This confirms the signed cancellation and the absence of a factor-of-two error in code. The concentration H*M4/M2^2 has the intended odd-frequency normalization; M2=0 is correctly represented by an undefined concentration. The public helper moments_from_correlation assumes its argument is a valid autocorrelation; arbitrary input sequences are outside its mathematical contract. All actual calls supply the certified autocorrelation.

Scope remains as stated in ALGORITHM.md: this is exact faster finite computation, still involving 2^s filter entries. The multiplication cost is not asserted to be quasi-linear, and the displayed decimals are conversions of exact rational results. I did not rerun the other agent's complete comparison suite during this final cross-audit; the independent contribution here is the carry, fold, normalization, and byte-representation proof review.
