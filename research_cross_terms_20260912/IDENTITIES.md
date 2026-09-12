# Cross-term closure: the even cross term is exactly the mixed-channel norm

12 September 2026. Exact identities for real arrays, specialized to the actual
Collatz parity-weight filter. The identities hold at every depth s >= 2;
the computations below are independent finite checks, not the proof.

## Main result

The even-branch cross term is not merely nonnegative. In the notation below,

    sum_(h=0..H-1) Delta A0(h) Delta A1(3h)
      = sum_(b=0..H-1) Delta B(b)^2 = NB >= 0.

Thus one of the apparently independent cross quantities closes exactly.
The remaining odd cross term is the signed reflection quadratic form of the
same mixed channel. For its reflection-even and reflection-odd half-norms
Nplus and Nminus, the parent sibling-difference energy is exactly

    E_parent = N0 + N1 + 6 Nplus + 2 Nminus.

This is an exact positive decomposition. It does not prove a contracting or
uniformly bounded normalized recurrence. In particular, the mixed-channel
norm NB and its reflection split still need scale-dependent arithmetic control.

## Definitions and all normalization conventions

Fix s >= 2, q = 2^(s-1), H = q/2. Arrays and their arguments in this document
are modulo q unless explicitly stated otherwise. Fix the parent's weights
g_k = binom(t-s, j-k), with out-of-range binomials zero, and put

    f0(u) = g_(K_(s-1)(u)),
    f1(u) = g_(K_(s-1)(u)+1),
    Ae(b) = sum_(u mod q) fe(u) fe(u+b),
    B(b)  = sum_(u mod q) f0(u) f1(3u+b),
    Delta Z(b) = Z(b)-Z(b+H).

Write E0 = Delta A0, E1 = Delta A1 and Z = Delta B. Each is anti-periodic:
E(b+H) = -E(b). On real anti-periodic arrays define the half inner product

    <U,V>_half = sum_(b=0..H-1) U(b)V(b)
               = (1/2) sum_(b mod q) U(b)V(b).

Set N0 = ||E0||_half^2, N1 = ||E1||_half^2, NB = ||Z||_half^2.
No child substitution changing binom(t-s,...) to binom(t-s+1,...) is made.

An affine map b -> a b+c with a odd carries b=0,...,H-1 to one representative
from every sibling pair {v,v+H}. Products of two anti-periodic arrays are
H-periodic, so their half sums are invariant under this common permutation.
This explains all changes between half intervals used below.

Use the unnormalized Fourier convention

    hat f(a) = sum_(u mod q) f(u) exp(-2 pi i a u/q).

Then hat(Delta f)(a) is 2 hat f(a) for odd a and zero for even a.

## Proof of the nonnegative even bridge

Autocorrelation gives hat Ae(a) = |hat fe(a)|^2. For the mixed channel,
changing variables v=3u+b yields

    hat B(a) = hat f1(a) conjugate(hat f0(3a)).

The Fourier transform of E1(3h) at a is hat E1(3^(-1)a), with the inverse
taken modulo q. Parseval and half/full normalization therefore give

    <E0, E1(3 .)>_half
      = (2/q) sum_(a odd mod q)
          |hat f0(a)|^2 |hat f1(3^(-1)a)|^2
      = (2/q) sum_(a odd mod q)
          |hat f0(3a)|^2 |hat f1(a)|^2
      = (1/(2q)) sum_(a mod q) |hat Z(a)|^2
      = NB.

This proof works for arbitrary real f0,f1, not only nonnegative filters or
parity-coded arrays. In particular, there is no sign-cancellation gain in the
even cross term. Cauchy gives the valid auxiliary bound

    0 <= NB <= sqrt(N0 N1).

The overlap of the two source spectra under dilation 3 is the exact remaining
quantity in NB. Positive spectra alone do not make this overlap small.

## Odd reflection form, exact split and Fourier phase

From the previous branch identity, the odd cross term without its factor 2 is

    Qodd = sum_(h=0..H-1) Z(3h+2) Z(-3h-1)
         = <Z, RZ>_half,
    (RZ)(b) = Z(1-b).

Indeed, b=3h+2 makes the second argument 1-b, and the preceding sibling-pair
argument justifies changing the summation transversal. R preserves the real
anti-periodic subspace and is a self-adjoint isometric involution: R^2=I.
Consequently

    Zplus  = (Z+RZ)/2,       Zminus = (Z-RZ)/2,
    Nplus  = ||Zplus||_half^2, Nminus = ||Zminus||_half^2,
    NB = Nplus+Nminus,       Qodd = Nplus-Nminus,
    -NB <= Qodd <= NB.

The exact Fourier expression, including the phase from the offset 1, is

    Qodd = (2/q) sum_(a odd mod q)
      Re[exp(2 pi i a/q) * hat B(a)^2].

To verify the phase, hat(RZ)(a)=exp(-2 pi i a/q) hat Z(-a), and real Z obeys
hat Z(-a)=conjugate(hat Z(a)). Thus the reflection form depends on Fourier
phase as well as magnitude. Replacing it by a sum of positive squared Fourier
magnitudes would be incorrect.

## Parent energy and moment identities

Let C_s be the actual parent autocorrelation, on modulus 2q. Define

    E_parent = sum_(d=0..q-1) [C_s(d)-C_s(d+q)]^2.

The established parity branch formulas give

    D_even(h) = E0(h)+E1(3h),
    D_odd(h)  = Z(3h+2)+Z(-3h-1),      0 <= h < H.

Expanding the squares, using the bridge and the reflection form, proves

    E_parent = N0+N1+4 NB+2 Qodd
             = N0+N1+6 Nplus+2 Nminus.

Equivalently the odd-branch energy is exactly 4 Nplus, while the even-branch
energy is N0+N1+2 NB. Thus

    N0+N1+2 NB <= E_parent <= N0+N1+6 NB
                              <= N0+N1+6 sqrt(N0 N1)
                              <= 4(N0+N1).

For unnormalized primitive fourth moments, M4_parent = q E_parent, whereas
the individual child-channel moments are M4_e = H Ne. Therefore

    M4_parent <= 2 [M4_0+M4_1+6 sqrt(M4_0 M4_1)]
              <= 8 (M4_0+M4_1).

This is a general norm bound with explicit constants, not a useful normalized
contraction claim. The two child channels retain the fixed parent g and are
not automatically the previously normalized family at depth s-1.

A more informative comparison isolates the even-branch energy

    E_even = N0+N1+2 NB.

Since N0+N1 >= 2 NB, the odd energy satisfies 4 Nplus <= 4 NB <= E_even.
Consequently there is an exact factor-two comparison

    E_even <= E_parent <= 2 E_even.

This controls the combined branches in terms of the even branch, but the even
branch still includes the mixed norm NB. It is not a scalar scale closure or
a proof of a constant bound after the research target's normalization.

At s=2, q=2 and RZ=-Z for every anti-periodic array, so Qodd=-NB and the odd
branch energy vanishes exactly. At larger depths the reflection form has both
signs even for actual Collatz filters, as the exact checks below show.

## Independent exact finite checks

An inline Python implementation using only `math.comb` and integer nested
loops generated K directly by shortcut iteration. It tested the entire grid

    t in {8,12}, j=0,...,t, s=2,...,min(t,7): 132 cases.

For every case it independently formed all A0,A1,B entries and the full parent
autocorrelation by direct enumeration. All three checks matched exactly:

1. Even half cross term = NB.
2. Odd cross term on the affine transversal = reflection half inner product.
3. Direct parent sibling energy = N0+N1+4 NB+2 Qodd.

Representative actual-filter values:

| t | j | s | N0 | N1 | NB | Qodd | Qodd/NB |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1 | 2 | 625 | 1 | 25 | -25 | -1 |
| 8 | 1 | 3 | 289 | 1 | 17 | 8 | 8/17 |
| 8 | 1 | 7 | 45 | 1 | 5 | 0 | 0 |

The largest reflection ratio in this finite grid was exactly 267120/267241
at (t,j,s)=(12,3,3), with NB=2405169 and Qodd=2404080. This is already very
close to +1, so a generic assumption of substantial negative odd cancellation
fails even on small actual filters. This finite observation does not exclude
special bounds on a narrower prescribed parameter family.

## What has and has not closed

The prior formulation treated both branch cross terms as untracked Gram data.
The even cross term now has an exact norm identity. The odd one reduces to an
explicit reflection split of the same mixed channel. This is more structure
than independent Cauchy bounds on unrelated quantities.

It is not yet a finite-dimensional scale closure: constructing or controlling
the mixed affine channel B and its reflection-even component still requires
additional information. Any claim of a uniform bound for the full W target
must also carry the actual stratum weights and source/filter overlap. None of
these identities establishes Collatz convergence or closes that target.

## Analytic follow-up: scalar iteration is valid but no better than the trivial bound

There is a precise child-family identification if BOTH total length and
precision decrease: f0 is the actual filter (t-1,j,s-1), and f1 is the actual
filter (t-1,j-1,s-1). Their binomial top index is correctly
(t-1)-(s-1)=t-s. This is not the fixed-t depth substitution (t,j,s-1), whose
top index would instead be t-s+1. Allow every integer j; if j<0 or j>t the
actual filter and all its moments are zero by the out-of-range convention.

Thus the preceding generic inequality does give, for s>=3,

    M4(t,j,s) <= 8 [M4(t-1,j,s-1) + M4(t-1,j-1,s-1)].

At s=2, reflection gives Qodd=-NB, hence

    S=N0+N1+2 NB <= 2(N0+N1),
    M4(t,j,2) <= 4 [M4(t-1,j,1)+M4(t-1,j-1,1)].

At s=1 there is exactly one primitive frequency, so the base value is

    M4(t,j,1) = [binom(t-1,j)-binom(t-1,j-1)]^4.

Iterating the two-child recursion and retaining the sharper final factor 4
therefore proves, for t>=s>=2,

    M4(t,j,s) <= U_iter
      = 4 * 8^(s-2) * sum_(h=0..s-1) binom(s-1,h)
          [binom(t-s,j-h)-binom(t-s,j-h-1)]^4.

This valid all-depth formula does not improve the elementary conjugate-pair
bound. To see this exactly, let H=2^(s-1), w_h=binom(s-1,h),

    delta_h = binom(t-s,j-h)-binom(t-s,j-h-1),
    D = sum_h w_h delta_h^2,
    B4 = sum_h w_h delta_h^4.

The actual parity sibling identity gives the primitive second moment M2=H D.
One direct proof is to pair inputs u and u+H. Their first s-1 parities agree,
their last parities are opposite, and the first s-1 parity-word weights h
occur binom(s-1,h) times among these pairs. Their filter-value difference is
delta_h up to sign. Therefore C(0)-C(H)=D and M2=H D.

Since sum_h w_h=H, weighted Cauchy gives D^2 <= H B4. Also
4*8^(s-2)=H^3/2. Consequently

    U_iter = (H^3/2) B4 >= (H^2/2) D^2 = M2^2/2.

For s>=2 each primitive frequency has a distinct conjugate partner with the
same squared modulus. If y_i denotes the common squared modulus in each pair,
then M2=2 sum_i y_i and M4=2 sum_i y_i^2. Positivity gives the elementary bound

    M4 <= M2^2/2.

Thus the iterated bound is ALWAYS at least as large as an already available
trivial bound; combining the two merely returns the trivial one. If D=0,
all delta_h vanish, both bounds are zero, and no division is needed. At s=1
the conjugate-pair formula does not apply, which is why the argument begins
at s=2.

This is an analytic obstruction to a particular relaxation, not to the exact
cross-term approach. The loss comes from repeatedly replacing mixed overlap
NB by sqrt(N0 N1), discarding the reflection split, and then discarding the
relative channel sizes. Progress requires retaining some of that information
or exploiting actual weighted source structure; scalar moments alone with
these worst-case constants cannot supply the hoped-for improvement.
