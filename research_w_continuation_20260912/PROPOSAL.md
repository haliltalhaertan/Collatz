# W continuation: an exact shell budget and a failed averaging shortcut

12 September 2026. Bounded independent research. No paid models, no Git mutations, no new convergence or orbit-exclusion claim. The identities below build on `research_visible_defect_20260908/kernel.md`; no priority/novelty claim is made.

## Plain-language result

We can compute exactly how much tail-filter energy lies at every residue precision, using a short sum of binomial coefficients. In particular, **exactly half of its total squared Fourier mass always lies at the finest precision**. The filter is therefore not concentrated solely on coarse residue information.

But knowing that energy budget does not let us replace the actual source/filter pairing by an average pairing. The actual Collatz panels already disprove the literal upper-bound shortcut `W <= W_flat`: at r=12 the true value is approximately 1.400 times the proposed flat-pairing value. The remaining problem has become more explicit: bound the alignment inside each conductor as well as the source energy on that conductor.

## Exact tail-shell lemma

Let `q=2^t`, `0<=j<=t`, and `T(u)=1_{K_t(u)=j}` for the shortcut map. Write `M=binom(t,j)` and use the unnormalized cyclic Fourier transform. For conductor `2^s`, set `h_s=2^(s-1)`, `n=t-s`, and

    D(t,j,s) = sum_{h=0}^{s-1} binom(s-1,h)
                  [binom(n,j-h)-binom(n,j-h-1)]^2.

Out-of-support binomial coefficients are zero. Then

    sum_{a odd mod 2^s} |hat T(a*2^(t-s))|^2 = h_s D(t,j,s).

The right side costs only O(s) binomial terms and does not require building the nonlinear parity-coding table.

Proof: aggregate T modulo `2^s`. The previous exact lift identity gives `F(u)=binom(t-s,j-K_s(u))`. Sibling residues `u` and `u+2^(s-1)` have the same first `s-1` parities and opposite final parities. If the shared prefix weight is h, their aggregate difference is, up to sign, `binom(n,j-h)-binom(n,j-h-1)`. The first `s-1` parity coding is bijective, so exactly `binom(s-1,h)` sibling pairs have weight h. Thus the squared sibling-difference norm is D. Twisted Parseval on the odd characters multiplies that norm by `h_s`. This proves the identity independently of the signs and ordering of those sibling differences.

In particular, when s=t the only nonzero binomial differences come from h=j and h=j-1, with support endpoints handled by the zero convention. Pascal's identity gives

    D(t,j,t) = binom(t-1,j)+binom(t-1,j-1) = M,
    finest-shell Fourier mass = (q/2) M.

Full Parseval gives `sum_xi |hat T(xi)|^2=qM`. Thus exactly one half is on the finest shell, for all valid j, including endpoints. The fraction of **nonconstant** Fourier mass there is `1/[2(1-M/q)]`; the half statement uses total mass including the constant coefficient. Do not confuse these two denominators.

The finite sum rule across nonzero shells is

    sum_{s=1}^t h_s D(t,j,s) = qM-M^2.

This is a spectral budget, not an upper bound on each individual multiplier. In particular it does not contradict small normalized multipliers: the finest-shell mean squared multiplier is M, while the squared zero-frequency multiplier is M^2.

## An explicit alignment reduction for the actual source

Use the existing true prefix histogram P_k modulo q, with sibling energy `R_(k,s-1)`. Let

    X_a = |hat P_(k,s)(a)|^2,
    Y_a = |hat T(a*2^(t-s))|^2,   a odd mod 2^s.

There are h_s such frequencies, and exact Parseval gives `sum X=h_s R` and `sum Y=h_s D`. Define, only when R D>0,

    A_(k,s) = h_s sum_a X_a Y_a / [(sum_a X_a)(sum_a Y_a)].

The stratum's conductor variance is then exactly

    V_(k,s) = A_(k,s) h_s R_(k,s-1) D(t,r-k,s) / q^2.

Odd dilation by 3^k only reindexes the relevant translation frequencies and preserves this identity. If R D=0 then V=0 and A need not be defined. Positivity alone gives `0<=A<=h_s`, but the principal identified the sharper real-array bound:

    A=1 at s=1 and s=2 whenever defined;
    0<=A<=2^(s-2) for every s>=2.

Indeed real P and T have equal squared Fourier magnitudes at a and -a. For s>=2 no odd frequency is self-conjugate, so collapse them into `h_s/2` conjugate pairs. The alignment expression becomes the same normalized pairing expression on only `h_s/2` nonnegative entries, whose upper bound is that number. For s=2 there is just one pair, giving equality A=1; s=1 has only one frequency to begin with. This also gives the exact reduction `W-W_flat=sum_{k,s>=3}(V_(k,s)-flat_(k,s))`: excess pairing can start only at conductor 8. The upper bound is still generally exponential in s, so it does not solve the target. A=1 describes flat spectral pairing on that shell; independence is not assumed or established.

Define the explicitly computable reference quantity

    W_flat = sum_{k,s} h_s R_(k,s-1) D(t,r-k,s) / q^2.

Then `W/W_flat` is exactly a weighted mean of the A values. **W_flat is not in general an upper bound.** If one could prove a subexponential upper bound on all contributing A values and an adequate exponential bound on W_flat in the growing critical regime, that would imply the corresponding bound on W. Both are still open; the reduction separates them rather than solving them. Uniform pointwise control of A is sufficient, not necessary, because only the weighted mean is required.

## Exact finite obstruction to unproved averaging

The script independently rebuilds the true prefix histograms from all odd h<2^m, applies direct translated tail counts, and extracts conductor variances by exact conditional projections. It does not use a floating-point DFT or copy the prior JSON values. The panel rule is the existing fixed rule `A=floor(log2(3^r))`, `m=ceil(1.2r)`, `t=A-m`, for r=5,10,12,14.

| r | W | W_flat | W/W_flat |
|---:|---:|---:|---:|
| 5 | 37/4 | 37/4 | 1 |
| 10 | 819/32 | 779/32 | 819/779 |
| 12 | 2795/4 | 7987/16 | 11180/7987 |
| 14 | 274211/256 | 374259/256 | 274211/374259 |

An especially concrete violating shell is r=12, A=19, m=15, t=s=4, k=10, j=2. Here q=16, h_s=8, R=1294, D=6. Its flat value is `h_s R D/q^2=1941/8`, while its true variance is `923/2`. Thus `A=3692/1941`, approximately 1.902. This is an actual source histogram, not an arbitrary engineered array. The smaller r=10 panel already violates the summed shortcut.

The last panel instead has W below W_flat. Neither a monotone alignment trend nor a uniform constant bound follows from these four finite panels. In particular, the observed maximum below 2 is not evidence of an established `A<=2` theorem.

## Verification and scope

`check_shell_alignment.py` verifies the exact D formula for all 440 (t,j,s) triples with 1<=t<=10, compares against direct residue aggregation, checks the finest-shell identity and total Parseval budget, and recomputes the four true-source panels with integer/Fraction arithmetic. It also checks the sharper conjugate-pair bound and exact equality at s<=2. Output is `RESULTS.json`. All assertions passed. These are bounded implementation checks; the all-length identity rests on the proof above.

The previous correction remains essential: the large old cancellation mostly removed the uniform prefix baseline, and Cauchy's polynomial loss across k is acceptable for the existing exponential target. The present work concerns the already centered source and its actual weighted energy; it does not revive the discarded raw-cancellation interpretation. The inherited sufficient exponent near 1.89423978 for W is not improved or proved here.

Next useful attack: seek a deterministic bound on the **weighted shell alignment** relative to W_flat, or refute such a bound in a relevant growing critical family. Do not assume independence because the individual shell budgets now have a closed formula. The phase/sign placement removed by the D sum is precisely the information that survives in A.
