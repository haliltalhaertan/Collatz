# Exact joint-count panel and the distinguished-origin question

2026-09-08. Principal with two adversarial reviewers. Fixed bounded panel r=10,12,...,22; A=floor(r log_2 3), m=ceil(1.2r), t=A-m. These are full INITIAL dyadic blocks x<2^m. No new orbit exclusion, paid calls or external publication.

## Design and exact comparison quantity

For odd x<2^m count first-m shortcut parity weight k and following-t weight r-k. Call the joint count J_k and total N=sum J_k. The comparison quantities are

    B_k=binom(m-1,k-1)*binom(t,r-k)/2^t,
    B=binom(A-1,r-1)/2^t.

These do not assume the initial block has independent future bits. They are the EXACT average joint counts over the2^t translated blocks

    x=a*2^m+h, 0<=a<2^t, odd1<=h<2^m.

Proof: the first m bits and their weight k are unchanged by translation. The affine formula gives H^m(h+a*2^m)=H^m(h)+3^k*a. Since3^k is invertible modulo2^t, these endpoints sweep every tail parity word once as a varies. Exactly binom(t,r-k) have the desired tail weight. Summing over binom(m-1,k-1) prefixes proves the joint mean; Vandermonde gives the total mean.

Thus the actual research question is whether the distinguished block a=0 can exceed this translation average by too large an exponential factor. The identity for the average supplies no bound on that distinguished block by itself.

## Results

|r|A|m|t|Exact N|Exact mean B|N/B approximately|
|---|---|---|---|---:|---:|---:|
|10|15|12|3|250|250.25|0.999001|
|12|19|15|4|1967|1989|0.988939|
|14|22|17|5|6360|6359.0625|1.000147|
|16|25|20|5|41142|40859.5|1.006914|
|18|28|22|6|131788|131816.953125|0.999780|
|20|31|24|7|426962|426775.78125|1.000436|
|22|34|27|7|2770062|2772010.3125|0.999297|

The row parameters were fixed before execution. No fitted asymptotic exponent or inferential p-value is reported. run.py/RESULT.json preserve exact rational comparisons, all target cells, deterministic total variation and runtime diagnostics. The largest row represented2^26 odd starts with108580 peak merged states; its local runtime was about0.74seconds. This is a local measurement, not a general speed guarantee.

The normalized comparison shape is the hypergeometric law

    B_k/B=binom(m-1,k-1)*binom(t,r-k)/binom(A-1,r-1),
    mean=1+(m-1)(r-1)/(A-1).

An actual mode is a mode of that law in every row. This supports examining the critical interior weights in this finite panel; it does not prove they dominate all lengths.

## Adversarial findings

1. N<=B is false: r14,r16 andr20 exceed the mean. At r16 EVERY feasible joint cell exceeds its own B_k, so this is not only a rare-bin effect. A universal nonpositive-origin-bias argument is unavailable.
2. Total closeness is not uniform cell closeness. At r20, N/B≈1.000436 but k20 has80 starts versus B_20=8855/128, ratio2048/1771≈1.156409. This is only80/426962≈0.0187% of the total; its large relative discrepancy has a small total weight.
3. Normalized shape closeness does not prove normalization closeness: all cells can be enriched together, as r16 illustrates. The total-variation diagnostic also fluctuates rather than decreasing monotonically.
4. The unknown tails in this panel have only3–7 bits. Despite the large starting counts, this is not evidence of a proved linear-depth asymptotic estimate. The small pointwise discrepancies cannot be extrapolated.

The relevant finite diagnostic is lambda_r=log_2(N/B)/r. All recorded values are small, but the required theorem concerns a uniform asymptotic upper bound over critical mass bands, not these seven values. At b1.2 the existing kappa1.053 bridge allows lambda<approximately0.0189197524; the panel does not certify this inequality beyond its finite rows.

## Independent control

check_blocks.py directly iterates EVERY odd start below2^A for r10 andr12, groups by translated block and both parity weights, and verifies ALL joint mean identities. In the r12 control, the16 block totals range from1929 to2062, their mean is1989, and the initial block has1967. Every identity passed. This confirms normalization through an independent trajectory calculation, not just the new dynamic program.

## Decision

The exact counter now makes joint hypotheses reviewable. This panel finds no growing discrepancy, but provides no new theorem. Preserve the exact translation-average identity as the reference and target a bound on the actual origin block, preferably weighting rare strata by their contribution. Do not replace that task by uniform tail independence, total-shape similarity, or a claim that the origin block is always below average. No larger panel is justified without a new structural hypothesis or an explicit scaling experiment design.
