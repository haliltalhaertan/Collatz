# Tail-selected spectral peeling: exact residual bound and transfer limits

12 September 2026. Analytic subtask; no paid models, publication, Git mutation, or new asymptotic theorem. Read together with the exact cyclic conductor identities and the W shell-budget continuation. The main experiment, not this note, freezes and computes the r=5..20 panels with L=1,2,4.

## What this reduction actually buys

It is legitimate to isolate a fixed number of the largest **tail** multipliers and measure the actual source energy at those frequencies. The remaining variance has an exact, deterministic upper bound using the next tail multiplier and the remaining source energy. This interpolates monotonically between the maximum-multiplier bound and the exact variance. It does not establish that a fixed number of peaks suffices uniformly as the conductor grows. Neither a tail trace budget nor successful finite panels implies that conclusion.

The selected frequencies must depend only on the tail `(t,j,s)`, with a fixed tie convention. Ranking source-tail products, or choosing frequencies because they capture the observed variance, is a different source-adaptive diagnostic and must not be described as this tail-selected bound.

## Pair conventions and exact theorem

Fix one stratum k and conductor 2^s, and let q=2^t. Write H_s=2^(s-1). Source and tail arrays are real. For s>=2 collapse the odd frequencies into conjugate pairs `{a,-a}` modulo 2^s; there are n_s=2^(s-2) pairs, each of multiplicity d_s=2. For s=1 there is one self-conjugate frequency, so n_s=d_s=1. One representative convention for s>=2 is odd `1<=a<2^(s-1)`.

For a pair i define

    y_i = |hat T_(t,j)(a*2^(t-s))|^2,
    e_i = sum_{b in pair i} |hat P_(k,s)(b)|^2.

The tail squared magnitude is the same at the two conjugate frequencies. Thus e_i includes the factor two and y_i does not. In the s=1 case use the single frequency once. Sort by descending y_i, breaking exact ties by the smaller representative; move the associated e_i with its pair. This sorting does not consult e_i.

The preceding exact identities give

    S := sum_i e_i = H_s R_(k,s-1),
    sum_i y_i = n_s D(t,j,s),
    V_(k,s) = q^(-2) sum_i y_i e_i.

Here D is the proved binomial shell budget. Neither S nor D alone determines the products. For G(a)=sum_z P_k(z) T(z+3^k a), Fourier transformation reindexes the count frequency by the odd factor 3^k. The matched source and tail frequencies in the formula above are the same original tail frequency. If a computation works in count-frequency coordinates, it must apply the inverse odd dilation consistently before attaching source energies to the tail-selected pairs.

Let ell=min(L,n_s),

    B_ell = q^(-2) sum_{i<=ell} y_i e_i,
    S_res = S-sum_{i<=ell} e_i.

When ell<n_s, the EXACT decomposition and deterministic enclosure are

    V_(k,s) = B_ell + q^(-2) sum_{i>ell} y_i e_i,
    B_ell + q^(-2) y_(n_s) S_res
        <= V_(k,s)
        <= U_ell := B_ell + q^(-2) y_(ell+1) S_res.

For ell=n_s the residual is empty and U_ell=B_ell=V_(k,s). The proof is termwise positivity: every residual multiplier lies between y_(n_s) and y_(ell+1). In particular the upper bound does not assume independence, random phases, or small alignment.

The upper-bound slack is exactly

    U_ell-V_(k,s)
       = q^(-2) sum_{i>ell} [y_(ell+1)-y_i] e_i.

Consequently equality holds precisely when every residual source-energy-bearing pair has multiplier y_(ell+1), or the residual source energy is zero. This also explains why tail plateaus can make peeling produce no improvement.

Set U_0=q^(-2)y_1 S. For 1<=ell<n_s,

    U_(ell-1)-U_ell
        = q^(-2)[y_ell-y_(ell+1)] S_res >=0.

Thus the certified bounds are nonincreasing with L; the last-pair bound is already exact. For one-pair shells (s=1 and s=2), L>=1 is exact immediately. The distinction between individual frequencies and conjugate pairs matters: L=1 here means up to two frequencies, not one.

Summing U_ell over (k,s) bounds W exactly under the same normalization. When all quantities needed for the bound are known, it is a rigorous finite bound; it is not necessarily computationally cheaper than evaluating W, because identifying the largest multipliers can still require all high-conductor tail frequencies. Its research value is to isolate a potentially provable small exceptional set and a bulk operator norm.

## Why trace control and fixed L do not settle the growing problem

Put T_pair=sum_i y_i=n_s D. Positivity and ordering give

    y_(ell+1) <= T_pair/(ell+1),
    y_(ell+1) <= T_pair-sum_{i<=ell} y_i.

The second right side is the residual trace, **not** the residual trace divided by its number of entries: the residual maximum is at least its average, not at most its average. Replacing the next multiplier by that average would reproduce the unproved averaging shortcut already falsified by actual source panels.

The first bound retains the factor n_s/(ell+1) relative to the shell mean D. For fixed L and growing s this is exponential, so it does not establish a uniform O(1) bulk-to-mean multiplier ratio. Trace information alone permits ell+1 equal peaks, each near T_pair/(ell+1), with all other multipliers arbitrarily small positive numbers. After peeling ell peaks, another large peak remains; an abstract source can place its energy there. Allowing small positive values means the no-exact-zero theorem does not remove this information-theoretic obstruction.

This is an obstruction to a deduction from trace and positivity alone, **not** a claim that those engineered spectra are the actual Collatz indicator spectrum or that the actual prefix histogram realizes the adverse source. Realizing an adverse family under the actual arithmetic constraints would require additional work. Conversely, observing a small fixed-L bound on finitely many true panels cannot prove a uniform statement for that family either.

A useful sufficient research target would control both (i) the summed, source-weighted selected-peak contribution and (ii) the summed product y_(ell+1) S_res/q^2. A uniform bound on y_(ell+1)/D would simplify (ii), but leaves (i) to be controlled. Large tail peaks are not harmless merely because their number is fixed: their actual source weights may dominate. It is enough to bound these weighted sums; demanding a uniform ratio for every shell is stronger than necessary.

If the numerical experiment uses floating-point DFT values, exact rational W from direct counts does not itself certify the ordering or rounded peeling bounds. Near ties need certified separation, interval enclosures, or an explicit designation of those ratios as numerical diagnostics. A valid conservative bound may replace y_(ell+1) by any verified upper bound for every unselected multiplier, so an uncertain exact ranking can be handled by enlarging the selected set or retaining a conservative residual maximum. No special theoretical gain should be inferred from a rounding-dependent tie choice.

## Walsh and cyclic Fourier do not transfer coefficientwise

Let b(u)=(b_0,...,b_(t-1)) be the shortcut parity word, and f(b)=1_{|b|=j}. Parity coding is a bijection, so T(u)=f(b(u)). It preserves counting and norms as a coordinate permutation. It is not a group isomorphism from cyclic residues under addition to Boolean words under XOR; these groups already have different exponents for t>=2. Hence it does not carry the cyclic translation characters to the Walsh characters by relabeling.

The concrete t=4,j=2 support is

    {u mod 16 : K_4(u)=2} = {1,2,3,6,12,13}.

At the alternating cyclic character xi=8,

    hat T(8)=sum_{u in support} (-1)^u=0

because the support has three odd and three even elements. On the parity-word cube, the Walsh coefficient at the all-four-bit character is

    sum_{|b|=2} (-1)^(b_0+b_1+b_2+b_3) = binom(4,2)=6.

These are two explicitly different characters, not two normalizations of one coefficient. In fact the cyclic alternating character corresponds to the *first-bit* Walsh character because b_0=u mod 2; it does not correspond to the all-bit character. This example obstructs identifying an alternating cyclic coefficient with parity-word alternation or transporting a Walsh-degree classification directly into cyclic conductor estimates. It does not prohibit proving a separate quantitative change-of-basis theorem; none is available or assumed in this reduction. No Krawtchouk bound is imported.

One can see the translation mismatch without any transform calculation: at t=4, b(0)=0000, b(1)=1010 and b(2)=0101, with bits in time order. The parity-word XOR increment caused by u->u+1 is 1010 from 0 to 1 and 1111 from 1 to 2. It is not a fixed Boolean translation.

## The sibling sign that cannot be dropped

For n=t-s, let w=K_(s-1)(u) and e be the s-th shortcut parity of u. The aggregate difference is exactly

    F(u)-F(u+2^(s-1))
      = (-1)^e [binom(n,j-w)-binom(n,j-w-1)].

The sign is the actual next parity at that residue; the spatial ordering of w and e is also fixed by parity coding. Squaring and summing permits the shell-trace formula to discard that sign. Individual Fourier coefficients, their maxima, and their ranking retain it.

For t=s=4,j=2, the actual sibling difference vector for u=0,...,7 is

    (0,1,1,1,-1,-1,1,0).

Dropping (-1)^e instead gives

    (0,1,-1,1,-1,-1,1,0).

At u=2 the first three parities have weight w=1 and the fourth parity is e=1. The bracket is -1 but the actual difference T(2)-T(10) is +1. Both vectors have squared norm 6, so a shell-energy test alone would fail to detect the erroneous sign removal; their individual Fourier transforms need not agree. This is precisely why a correct binomial trace does not supply the peak spectrum needed by peeling.

## Audit outcome

The tail-selected conjugate-pair residual bound is valid with the factors and normalization above. Its monotonic refinement and exact slack are proved. The missing asymptotic inputs are explicit: actual source weights on selected peaks and a usable remaining multiplier bound, in weighted aggregate over growing critical strata. The Walsh/cyclic coefficient mismatch and sibling sign error are concrete obstructions to bypassing those inputs. The two displayed t4 arrays were checked by direct four-step integer iteration; no new broad experiment was run in this subtask.

## Addendum: an exact weighted exceedance reformulation

This final analytic check concerns the principal's proposed aggregate layer-cake route; no new numerical or literature check is performed here.

Index the contributing strata/conductors by b=(k,s). Write D_b=D(t,r-k,s), S_b=sum_i e_(b,i), and

    f_b = S_b D_b/q^2 = flat_(k,s),
    W_flat = sum_b f_b.

All quantities are nonnegative. If S_b=0 then every e_(b,i)=0 and V_b=0. If D_b=0, the exact tail trace identity sum_i y_(b,i)=n_s D_b forces every y_(b,i)=0 and again V_b=0. Thus strata with f_b=0 contribute neither to W nor to W_flat and must simply be omitted from normalized expressions; do not assign a ratio 0/0. If W_flat=0, every stratum has zero variance and W=0. The ratio W/W_flat and the following probability distribution are undefined in that entirely zero case, though any inequality W<=constant*W_flat holds trivially.

Assume W_flat>0. On every retained stratum define

    z_(b,i) = y_(b,i)/D_b,
    p_(b,i) = e_(b,i)/S_b.

The p values sum to one within the stratum. Direct substitution, including the conjugate-pair multiplicities already absorbed in e, gives

    V_b/f_b = sum_i p_(b,i) z_(b,i).

Hence the joint weights `mu_(b,i)=(f_b/W_flat) p_(b,i)` form a probability measure, and the source-weighted aggregate tail function is

    M(u) = sum_(b,i) mu_(b,i) 1[z_(b,i)>u],  u>=0.

In particular 0<=M(u)<=1 and M is nonincreasing. Its expectation identity is exact:

    W/W_flat = sum_(b,i) mu_(b,i) z_(b,i)
             = integral_0^infinity M(u) du.

For each finite panel this follows by summing the elementary identity `z=integral_0^infinity 1[z>u]du` for nonnegative z. The strict inequality at finitely many jump locations does not affect the integral. The same identity extends to countable nonnegative mixtures by Tonelli, possibly with both sides infinite, but no such extension is needed for the frozen panels.

If there are fixed constants C>=0 and epsilon>0 such that

    M(u)<=C*u^(-1-epsilon) for every u>=1

uniformly over the intended growing family of panels, then

    W/W_flat <= integral_0^1 1 du
                 + C integral_1^infinity u^(-1-epsilon) du
              = 1+C/epsilon.

The assumptions must quantify over all thresholds u>=1 and all panels in the claimed family. A finite grid of thresholds or a fitted finite-panel constant is not that hypothesis. A growing prefactor would need its own quantitative bound; finiteness on each panel alone supplies no uniform estimate.

This aggregate condition is weaker than imposing the same C,epsilon tail bound in every stratum separately: a convex mixture preserves a common per-stratum bound, whereas the aggregate inequality can hold even when a stratum violates it because that stratum has small weight f_b/W_flat. Here the aggregate weights depend on the actual arithmetic source energies; they are not uniform weights over strata or over frequencies. A condition expressed only in unweighted tail-frequency counts would omit the essential source alignment and is not interchangeable with M.

The condition is sufficient, not necessary, for a bounded ratio W/W_flat. Even a uniform first-moment bound alone yields only the generally nonintegrable estimate M(u)<=constant/u by Markov; it does not imply an epsilon>0 power margin. Thus this route also makes a substantive extra regularity demand, albeit an aggregated one rather than a worst-stratum demand.

The principal reports that a post-hoc diagnostic of the stronger per-stratum epsilon=1 version needs C to grow to about 20 by r=20. This is reported context, not a separately checked result of this analytic subtask; it neither proves failure of a uniform bound at larger scales nor supplies encouragement for asserting that stronger hypothesis. In particular it should not be used to choose and then advertise a favorable exponent as independently supported.

The reduction itself is proved, but no arithmetic exceedance bound for M is proved here. It reformulates exactly the missing joint control of actual prefix source energy and actual cyclic tail multipliers. Establishing its tail envelope and bounding W_flat sufficiently in the growing critical regime remain separate open tasks; the layer-cake identity alone yields no new asymptotic W exponent or orbit exclusion.
