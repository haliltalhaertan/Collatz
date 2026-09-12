# Exact accelerated fourth moments: Kronecker substitution

The actual filter can be evaluated substantially beyond the previous quadratic
autocorrelation loop without FFT error or an unproved rounding rule. This is a
computational improvement, not a new uniform bound or a short state recurrence.

## Definitions and output

For `n = 2^s`, `H = n/2`, use the actual shortcut Collatz map
`T(x) = x/2` for even x and `(3*x+1)/2` for odd x. Let `K_s(u)` count odd
steps among the first s steps, and

`v[u] = F(u) = binom(t-s, j-K_s(u))`, with out-of-range binomials zero.

The implementation computes every integer cyclic correlation

`C[d] = sum_u v[u] v[(u+d) mod n]`.

The primitive (odd-frequency) moments, with the unnormalized Fourier transform,
are exactly

```
M2 = H * (C[0] - C[H])
M4 = H * sum_{d=0}^{H-1} (C[d] - C[d+H])^2
C_Y = H * M4 / M2^2.
```

These follow from the power-of-two Ramanujan sum: the sum of odd characters is
H on shift zero, -H on shift H, and zero elsewhere. The first identity applies
it to the Fourier transform of C. For the second, orthogonality on the
H-dimensional anti-periodic quotient gives the displayed square norm. M2=0 is
reported with an undefined concentration, rather than division by zero.

## Certified integer convolution

Let `Q = sum_u v[u]^2`, and choose the byte-aligned base `B = 256^w > Q`.
Form the nonnegative packed integers

```
A = sum_{i=0}^{n-1} v[i] B^i
R = sum_{i=0}^{n-1} v[n-1-i] B^i.
```

Each coefficient of their polynomial product is at most Q: it is an inner
product of two truncated/reordered copies of v, so Cauchy-Schwarz bounds it by
the product of their Euclidean norms, at most Q. Thus ordinary arbitrary-
precision integer multiplication `A*R` has **no carries between base-B
coefficient positions**. Decoding fixed-width little-endian bytes recovers
all linear-convolution coefficients `a[k]` exactly. The cyclic correlations are

```
C[0] = a[n-1]
C[d] = a[n-1+d] + a[d-1]  for 1 <= d < n.
```

This uses Python integer multiplication and byte encoding only. No floating
point enters correlation, moments, or the reported rational concentration;
`C_Y_display` is solely a decimal rendering of that exact rational.

The implementation additionally checks the decoded coefficient bound,
`C[0]=Q`, reversal symmetry, and `sum_d C[d]=(sum_u v[u])^2`. These are
consistency checks alongside the proof, not substitutes for the proof.

## Complexity and scope

Packing/unpacking are linear in the byte representation size. Multiplication
cost is that of the installed arbitrary-precision implementation at roughly
`n * (log_2 Q + O(1))` operand bits. CPython commonly uses Karatsuba for these
sizes; **this code does not claim O(n log n)**. It removes the explicit n²
correlation loop with a certified fast integer multiplication. Filter generation
still enumerates n residues and follows s shortcut steps for each: O(ns) small
integer steps. Enumeration remains exponential in s.

## Executed verification

`exact_moment.py` compared **every correlation shift**, not just moments, to an
independent nested-loop formula for all 28 choices

```
(t,j) in {(10,6), (12,8), (14,9), (60,38)}, s=2,...,8.
```

All 28 passed exactly. Six additional zero, constant, sparse, byte-boundary,
and unequal-entry vectors passed. In particular, the power-of-256 coefficient
bound case verifies that the base is chosen strictly above Q.

The prescribed larger family `(t,j)=(60,38)` gave:

| s | residues | exact-rational C_Y rendered decimal | filter seconds | correlation seconds | moment seconds |
|---:|---:|---:|---:|---:|---:|
| 8 | 256 | 2.5386273911 | 0.00019 | 0.00061 | 0.00003 |
| 10 | 1,024 | 4.6422262938 | 0.00093 | 0.00408 | 0.00013 |
| 12 | 4,096 | 9.3575695436 | 0.00436 | 0.02948 | 0.00039 |
| 14 | 16,384 | 20.2074332331 | 0.01903 | 0.19187 | 0.00130 |

These are single-run wall-clock timings on the current Windows host, not a
controlled benchmark. Exact integer moments and rational values, together with
packing certificates and direct-comparison timings, are in
`algorithm_results.json`. The largest case uses 12 bytes per packed coefficient
and an operand size bounded by 1,572,864 bits.

The rising concentration in this **fixed finite family** argues against calling
the filter approximately flat throughout these precisions. It does not establish
asymptotic unboundedness: t is fixed at 60, only four larger precisions were
evaluated, and the overall research target weights different strata.

## Reproduction

Run `python -X utf8 research_shift_recurrence_20260912/exact_moment.py` from the
repository root. It has no third-party imports and writes only its own
`algorithm_results.json`. It does not call providers, access sealed outcomes,
or alter previous research artifacts.

## Explicit post-hoc extension after the initial result

The parent researcher requested s=16 and s=18 only after inspecting the initial
s<=14 result. The extension is separately labelled `posthoc_followup` in the
JSON; the original measurements and timings were preserved.

| s | residues | exact-rational C_Y rendered decimal | filter seconds | correlation seconds | moment seconds |
|---:|---:|---:|---:|---:|---:|
| 16 | 65,536 | 45.9041969984 | 0.09299 | 1.67338 | 0.00680 |
| 18 | 262,144 | 109.5643577642 | 0.42502 | 15.67177 | 0.02842 |

These are exact integer calculations using the same certified coefficient bound,
not floating-point reconstructions. They continue the same finite `(t,j)=(60,38)`
family and do not prove an asymptotic claim. In particular, t remains fixed.

To reproduce the extension while retaining prior timings, import `exact_moment`,
call `actual_filter(60,38,s)`, `cyclic_correlation_exact(v)`, and
`moments_from_correlation(c)` for s in `(16,18)`, then save to a separate
`posthoc_followup` section. The default script intentionally retains its
initial prescribed grid; rerunning its default entry point regenerates the
original-grid JSON and therefore replaces an existing extension section.

## Review of recurrence closure: explicit missing cross terms

I read `ADVERSARIAL.md` and `RECURRENCE.md`. The affine recursion is consistent
with exact correlation computation. It does **not** imply a scalar fourth-moment
recurrence. Here are explicit terms that such a further argument must control.

Fix current depth s>=2. Write q=2^(s-1), h0=q/2, and keep the parent filter's
weight sequence `g_k=binom(t-s,j-k)` fixed throughout the following contraction.
At depth s-1 define

```
A_e(b) = sum_{u mod q} g_{K_(s-1)(u)+e} g_{K_(s-1)(u+b)+e}
B(b)   = sum_{u mod q} g_{K_(s-1)(u)} g_{K_(s-1)(3u+b)+1}
Delta Z(b) = Z(b)-Z(b+h0), with arguments modulo q.
```

Contraction of the even and odd branch identities gives exactly

```
C_s(2h)   = A_0(h)+A_1(3h)
C_s(2h+1) = B(3h+2)+B(-3h-1).
```

The odd formula uses the variable-swap form of the second affine branch. Adding
the sibling shift q to the parent argument adds h0 to h; multiplication by
either 3 or -3 sends h0 to h0 modulo q. Hence the two sibling differences are

```
D_even(h) = Delta A_0(h)+Delta A_1(3h)
D_odd(h)  = Delta B(3h+2)+Delta B(-3h-1).
```

Their squared sums contain the cross terms

```
2 sum_{h=0}^{h0-1} Delta A_0(h) Delta A_1(3h)
2 sum_{h=0}^{h0-1} Delta B(3h+2) Delta B(-3h-1).
```

These are correlations between distinct weight-shifted channels under dilation
3, and between offset channels related by the reflection b -> 1-b. They are
not specified just by the individual norms. Applying Cauchy-Schwarz bounds them,
but does not furnish exact scalar closure or automatically a useful normalized
bound. Moreover, the sequence g retained here has `t-s` in its binomial; it must
not silently be replaced by the original family's depth-(s-1) weight sequence
with `t-s+1`. That replacement requires Pascal decompositions and creates still
more mixed weight channels.

A further scalar closure is not ruled out in principle, but would need a
specific additional identity for these cross terms. A transfer formulation can
retain them as Gram/cross-channel data; its state growth and weighted norm
control would then be the new mathematical work. The current affine-state
count controls exact computation, not this norm inequality.

An additional independent inline check contracted these explicit A/B formulas
at `(t,j)=(12,8)` for every shift at s=2,...,8. All **508 even/odd identities**
matched the integer-convolution C values exactly. This supplements the symbolic
branch derivation; it does not establish a uniform bound for the cross terms.
