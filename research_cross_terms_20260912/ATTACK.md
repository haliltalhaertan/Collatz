# Adversarial audit: cross terms, saturation, and sign cancellation

This is a bounded audit of the actual Collatz filter, not a proof of the global
weighted W bound. I used the definitions in the final cross-channel section of
`research_shift_recurrence_20260912/ALGORITHM.md` and independent direct sums.
No provider calls, sealed outcomes, Git mutations, or publication were used.

## Exact notation

Let q=2^(s-1), H=q/2, s>=2, f(u)=g(K_(s-1)(u)),
z(u)=g(K_(s-1)(u)+1), and g(k)=binom(t-s,j-k). Let A0,A1 be their respective
cyclic autocorrelations, B(b)=sum_u f(u)z(3u+b), and Delta V(b)=V(b)-V(b+H).
All arguments below are modulo q. Define half-period vectors

```
a(h)=Delta A0(h), c(h)=Delta A1(3h),
x(h)=Delta B(3h+2), y(h)=Delta B(-3h-1), 0<=h<H.
N0=<a,a>, N1=<c,c>, E=<a,c>, O=<x,y>.
```

## The even cross term is always nonnegative: proven

With unnormalized Fourier transforms, autocorrelation spectra are nonnegative:
A0hat(xi)=|fhat(xi)|^2 and A1hat(xi)=|zhat(xi)|^2. Delta keeps odd frequencies
and multiplies them by two. Products of two anti-periodic sequences have equal
sums on the two half periods. If 3^-1 denotes the inverse modulo q, Parseval gives

```
E = (2/q) sum_(xi odd) |fhat(xi)|^2 |zhat(3^-1 xi)|^2 >= 0.
```

Thus any argument hoping for negative cancellation from the EVEN cross channel
is false. This proof holds for arbitrary real f,z; no positivity assumption on
the weights is needed.

## Stronger exact coupling: E equals each odd-channel squared norm

Directly transforming the mixed affine correlation gives

```
Bhat(xi) = zhat(xi) conjugate(fhat(3xi)).
```

The sampled arguments 3h+2 choose exactly one representative of every antipodal
pair {b,b+H}. Therefore Parseval and a permutation of odd frequencies imply

```
<x,x> = <y,y> = E.
```

This is useful structure missing from a model with unrelated four channels.
Reflection J takes b to 1-b and is an isometric involution on the anti-periodic
space. Thus -E<=O<=E. In particular

```
2E+2O >= 0.
```

The two cross terms TOGETHER cannot give a negative net contribution relative
to the four separate squared norms. The odd cross term can cancel the even
cross term exactly, but cannot overcompensate it.

Writing Delta B_+=(Delta B+J Delta B)/2, with its norm taken on any half-period
representatives, gives

```
E+O=2 ||Delta B_+||^2,
S := ||a+c||^2+||x+y||^2
   = N0+N1+2E+4||Delta B_+||^2.
N0+N1+2E <= S <= N0+N1+6E.
```

This is an identity and a bound, not a useful uniform contraction by itself.
Reflection-symmetric mixed energy can be as large as E.

## Nondegenerate exact Cauchy saturation is present

The exact integer scan includes the following actual filters. The decimal rho
is shown only for interpretation; saturation is decided by ab^2=aa*bb.

| t,j,s | channel | aa | bb | ab | rho |
|---|---|---:|---:|---:|---:|
| 5,3,4 | even | 6 | 6 | 6 | 1 |
| 6,3,4 | even | 24 | 24 | 24 | 1 |
| 11,6,4 | odd | 384160 | 384160 | 384160 | 1 |
| 5,4,4 | odd | 2 | 2 | -2 | -1 |
| 6,2,4 | odd | 20 | 20 | -20 | -1 |

These disprove an unconditional rho<=rho0<1 assertion across all actual t,j,s
for either channel. The t=5,j=3 example is an interior filter, and j is the
nearest integer to alpha*t, alpha=log(2)/log(3). It is still a small finite
example, NOT a refutation of an asymptotic bound with a sufficiently large
threshold and carefully specified near-critical window.

There is also an infinite near-critical interior family with even rho=1 at a
fixed coarse depth: s=3 and j=round(alpha*t), t sufficiently large. Here q=4,
and every real autocorrelation has Delta A(1)=0, so a=(a0,0), c=(c0,0), where
a0,c0>=0. They are nonzero for sufficiently large t: K_2(0)=0,K_2(2)=1, so
nonconstancy across the antipodal pair follows from the unequal consecutive
binomials g0,g1 and g1,g2. These consecutive binomials can be equal only at
the central index, whereas alpha>1/2. Thus rho=1 exactly.
This fixed-depth obstruction does not attack a claim restricted to growing s,
and coarse levels were already known to have special structure.

## Endpoint warning

For j=0, f is a point mass at the all-even residue and z=0. For j=t, f=0 and
z is a point mass at the all-odd residue. Hence E=0, B=0. Cauchy equality is
formally true (0=0), but both normalized cross-channel correlations are
UNDEFINED. Endpoints therefore must NOT be advertised as nondegenerate
rho=1 counterexamples, nor as near-critical examples. Their ordinary cyclic
Fourier magnitudes are flat, but this is a different statement.

## Independently executed finite checks

The companion attack_results.json records all scalar integer results for

```
t=3,...,12; j=0,...,t; s=2,...,min(t,7).
```

There are 460 cases. K is computed by direct shortcut steps. A0,A1,B are each
computed by their defining nested integer sums; no imported recurrence,
convolution packer, FFT, or parent probe functions were used. All 460 satisfy
E>=0, E=||x||^2=||y||^2, and E+O>=0 exactly. Selected full half-period vectors
are included for independent checking. The identities above supply the general
proof; the finite scan is a separate normalization and implementation check.

## Research recommendation

Retain E as a nonnegative mixed spectral energy and the reflection-even part of
Delta B as the additional obstruction. Do not model all cross terms as free
signed errors or rely on universal strict Cauchy slack. A meaningful next lemma
would bound this mixed/reflection-even energy relative to the correctly weighted
parent quantity, or show that layers with near saturation carry small total
weight. None of the finite counterexamples rejects such a weighted statement.

## Parent follow-up: factor-two baseline bound

The parent's notation A=N0+N1 and B=E gives

```
S=A+4B+2O,  |O|<=B,  0<=B<=sqrt(N0*N1)<=A/2.
A+2B <= S <= A+6B <= 2(A+2B).
```

This holds for all real channel arrays f,z in the definitions above, hence for
the actual binomial filters. The denominator A+2B is the squared EVEN combined
channel norm, not the original W_flat and not a parent-to-child normalized
concentration. Claiming a uniform W/W_flat<=2 from this inequality would be a
normalization error.

For arbitrary real nonnegative channel arrays the factor two is sharp: take
q=4, f=(sqrt(2),0,0,0), z=(1,1,0,0). Then Delta A0=Delta A1=(2,0,-2,0),
B=(sqrt(2),sqrt(2),0,0), and Delta B is reflection-even under b->1-b.
Thus N0=N1=B=O=4, S=32, A+2B=16. These arrays are NOT claimed to be an actual
Collatz binomial filter pair. Actual-family sharpness remains unproved.

On the 460-case exact scan, the largest nonzero ratio S/(A+2B) was 667/342
(about 1.95029) at (t,j,s)=(9,5,4). The near-critical rounded index example
(8,5,3) gives 467/242 (about 1.92975). All defined ratios lay in [1,2]
exactly. These finite examples reject small unconditional proposed constants,
not a carefully delimited large-depth bound.
