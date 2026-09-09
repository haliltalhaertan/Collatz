# Exact translated-block baseline and adversarial panel interpretation

2026-09-08. The principal ran the fixed seven-row panel; this note independently interprets its stored exact counts. No duplicate large run, paid call, probabilistic p-value, or asymptotic proof.

## Baseline is an exact translation mean

Fix A=m+t and total parity weight r. Partition the odd starts below2^A into blocks

    x=a*2^m+h, 0<=a<2^t, odd1<=h<2^m.

For a fixed h the first m parities are independent of the block index a, since parity coding to depth m depends only on the starting residue modulo2^m. If their weight is k, the affine identity gives exactly

    H^m(a*2^m+h)=3^k*a+H^m(h).

As a runs over0,...,2^t-1, the right side runs bijectively over all residues modulo2^t because3^k is odd. Its t subsequent parities therefore run over all binary t-bit words, precisely binom(t,j) of weight j. This is a counting identity, not an independent-tail assumption for a=0.

Thus the mean joint count across translated blocks is

    B_k=binom(m-1,k-1)*binom(t,r-k)/2^t,

and its summed mean is

    B=binom(A-1,r-1)/2^t.

Conditioning the complete-period law on total weight r gives the hypergeometric prefix-weight law

    H_k=binom(m-1,k-1)*binom(t,r-k)/binom(A-1,r-1).

Its mean is1+(m-1)(r-1)/(A-1). The initial block a=0 has no automatic privilege in this averaging identity. In particular, an upper bound by the translation mean is false: even this panel has rows with total greater than B.

## Correct exponent diagnostic

Let N be the actual initial-block count. The relevant ratio is R=N/B and its finite exponent diagnostic is log_2(R)/r. On fixed critical bands and m=br+o(r), the baseline exponent is h_*+b-alpha. The desired exponent-only statement is a uniform subexponential upper bound for R, or the previously allowed positive exponential loss. At b1.2 and kappa1.053, the sufficient loss threshold is0.0189197523759952.

This is not the logarithm of the success fraction N/2^(m-1), nor a rate divided by m. Floors in A and m must remain in the exact binomial baseline; replacing them by asymptotic expressions would introduce artificial finite-scale fluctuations.

## What the seven exact rows do and do not show

In every row r10,12,...,22, the observed modal prefix weight is one of the hypergeometric modes. The baseline has a tie at r12 and r20, while the observed mode is a single member of the tie. The mean prefix weights and normalized shapes are close. These are numerical observations, not proofs of conditional independence.

A useful warning is r20,k20: the actual cell is80 versus baseline8855/128, ratio2048/1771, an excess of about15.64 percent. Yet it contributes only80/426962, about0.0187 percent, of the actual total. A maximum cell ratio therefore exaggerates its significance for the weighted total target. A blanket uniform cell-ratio claim is stronger than needed.

Conversely, at r16 every feasible cell is above its unnormalized baseline: the smallest ratio is63052/62985. The total is enriched by approximately0.69 percent while the conditional-shape total variation is only about0.00265. Good agreement of normalized shapes cannot alone certify the needed normalization bound; multiplying all cells by a common large factor would preserve their shape exactly.

The unknown suffix depth t is only3 through7 across this panel. The results are consistent with mild initial-block bias at these small depths. They do not establish behavior when t grows linearly without bound, uniformity over every fixed mass band, or an eventual rate below the allowed loss threshold.

## Concrete research hypothesis and falsification boundaries

The appropriate main hypothesis remains the origin-block upper-bias estimate

    N_(r,A,m)(a=0)<=2^(lambda*r+o(r))*B_(r,A,m),

with uniformity in the relevant fixed critical bands and lambda below the orbit-bridge threshold. The stronger lambda0 version is the original ideal target. This formulation identifies the missing arithmetic fact: why the zero block index cannot be exponentially heavier than the exact translated-block average.

Finite tests can refute explicit stronger guesses, such as N<=B or exact hypergeometric cell equality, but cannot establish an unspecified o(r) bound. The present panel already refutes N<=B. No polynomial prefactor, limiting exponent, or tail-independence assertion should be fitted and promoted to a theorem from these seven points.
