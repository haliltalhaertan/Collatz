# Cyclic conductors, source sibling imbalances, and the actual tail filter

2026-09-08. Exact finite identities and their limitations. No large computation or new orbit exclusion. This note uses the corrected m3 example only.

Fix q=2^t. Let P_(k,s)(u) count odd initial h<2^m with prefix weight k and H^m(h)=u mod2^s, for0<=s<=t. Its total is N_k. Let

    R_(k,s-1)=sum_(u<2^(s-1))
       [P_(k,s)(u)-P_(k,s)(u+2^(s-1))]^2, 1<=s<=t.

Fourier transforms below are unnormalized finite cyclic transforms with negative exponential. A frequency xi modulo q has conductor2^s when xi=a*2^(t-s), with a odd modulo2^s.

## 1. Source sibling scale exactly equals cyclic conductor energy

Projection to the smaller residue ring gives

    hat P_(k,t)(a*2^(t-s))=hat P_(k,s)(a).

For odd a, splitting the sum into two siblings gives

    hat P_(k,s)(a)=sum_(u<2^(s-1))
      [P_(k,s)(u)-P_(k,s)(u+2^(s-1))]
      *exp(-2pi*i*a*u/2^s).

The odd-frequency exponentials form a twisted Fourier basis on the2^(s-1) sibling differences. Parseval therefore yields the exact identity

    sum_(a odd mod2^s)|hat P_(k,s)(a)|^2
       =2^(s-1) R_(k,s-1).

Consequently the centered full source energy is

    e_(k,t)=sum_(s=1..t)2^(s-1-t)R_(k,s-1).

Thus the proposed source sibling/Haar decomposition aligns EXACTLY with cyclic Fourier conductor blocks. It is a filtration by the number of low input bits exposed, not Boolean Walsh Hamming degree. Odd dilations3^k preserve conductor, although they permute frequencies within it.

## 2. Exact tail Fourier multiplier from only the first s parity bits

Let T_(t,j)(z) indicate that z has j odd parities among its first t shortcut steps. For a fixed u modulo2^s, those first s parities have weight K_s(u). As z runs over the2^(t-s) lifts of u, the remaining parity words run bijectively through all binary words of length t-s. Therefore

    sum_(z=u mod2^s) T_(t,j)(z)=binom(t-s,j-K_s(u)).

Define F_(s;t,j)(u)=binom(t-s,j-K_s(u)), with out-of-range binomials zero. Then

    hat T_(t,j)(a*2^(t-s))
       =sum_(u<2^s) F_(s;t,j)(u)*exp(-2pi*i*a*u/2^s).

This computes all tail multipliers at conductor2^s using only the2^s residue coding table and binomial coefficients, instead of enumerating2^t tail residues. It is a genuine exact low-conductor computational reduction; the highest conductors still require exponentially many entries.

For odd a the transform can again be written using sibling differences. If w=K_(s-1)(u) and e is the next parity at u, that difference is

    (-1)^e*[binom(t-s,j-w)-binom(t-s,j-w-1)].

The sign is the actual next parity, not a freely assigned independent sign. Binomial cancellation therefore does not remove the nonlinear parity coding at higher conductors.

## 3. Exact per-stratum variance decomposition

Let V_k be the variance of the k-stratum translated-block count, and j=r-k. The exact nonnegative decomposition is

    V_k=sum_(s=1..t) V_(k,s),
    V_(k,s)=q^(-2)sum_(a odd mod2^s)
       |hat P_(k,s)(a)|^2 |hat F_(s;t,j)(a)|^2.

The uniform source baseline is absent at every nonzero conductor. Put L_(s,j) and M_(s,j) equal to the minimum and maximum magnitudes of these tail multipliers on odd a. Then

    [2^(s-1)/q^2]*L_(s,j)^2 R_(k,s-1)
       <=V_(k,s)
       <=[2^(s-1)/q^2]*M_(s,j)^2 R_(k,s-1).

If all tail multipliers on a conductor vanish, that entire source scale is invisible. Otherwise R alone records total energy on the scale, not its frequency allocation relative to the kernel. Exact R scale information is therefore insufficient to determine V_(k,s) unless the relevant multiplier magnitudes agree or an additional alignment estimate is available.

## 4. A useful limitation: the first conductor is visible at the balanced critical split

At s=1 there is only one frequency, and

    hat F_(1;t,j)(1)=binom(t-1,j)-binom(t-1,j-1)
       =binom(t,j)*(1-2j/t).

Writing p_j=binom(t,j)/q, the scale contribution is EXACTLY

    V_(k,1)=p_j^2*(1-2j/t)^2*R_(k,0).

The middle tail j=t/2 is therefore blind to parity imbalance. But at the balanced critical split k~m/alpha, j~t/alpha, the multiplier ratio tends to1-2/alpha, which is nonzero. Its squared magnitude stays a positive constant. Thus first-conductor source imbalance cannot be hidden by this tail filter at that split. No claim that this split dominates every actual count is being made.

The corrected actual null example remains valid away from that observation: m3,k2,q4 gives P=(1,0,1,0), N=2, centered E=(1/2,-1/2,1/2,-1/2), e=1. For t2,j1, the tail indicator is(0,1,1,0), every translated stratum count is1, and V_k=0 despite qD_(2,k)=1. The earlier erroneous histogram(1,0,2,0) and its derived numbers are not used.

More generally, for fixed s and j/t->rho in(0,1),

    binom(t-s,j-K_s(u))/binom(t,j)
       ->rho^K_s(u)*(1-rho)^(s-K_s(u)).

Hence normalized low-conductor multipliers tend to the Fourier transform of the inverse parity-coding image of a biased Bernoulli s-bit law. This is a finite-s limit derived from factorial ratios, not an assertion of independent continuation bits for the actual prefix sample. It supplies explicit limiting multipliers; it does not bound the source R terms.

## Status

Established: exact alignment of low-bit sibling energy with cyclic conductor blocks; exact binomial-lift computation of every low-conductor tail multiplier; exact first-conductor visibility/nullspace criterion. Open: uniform control of actual growing critical source imbalances and their allocation within higher conductor blocks sufficient to bound W=sum_k V_k. The identities identify visible directions but do not prove their size is small.
