# Independent adversarial interpretation of the fixed joint panel

Reviewed RESULT.json without rerunning or enlarging the experiment. Design: r10,12,...,22; A=floor(alpha*r), m=ceil(1.2*r), t=A-m. This rounding differs from some older floor-m diagnostics; comparisons must retain the actual recorded parameters.

## Exact comparison law

For prefix weight k, write

    J_k=actual origin-block count with prefix weight k and total weight r,
    E_k=binom(m-1,k-1)*binom(t,r-k)/2^t,
    E=sum E_k=binom(A-1,r-1)/2^t.

The E_k are an EXACT average over the2^t translated dyadic input blocks, not expectations obtained by assuming fair tails in the origin block. A fixed m-step prefix of weight k obeys H^m(x+q*2^m)=H^m(x)+3^k*q. As q runs through0,...,2^t-1, the odd multiplier3^k permutes the residues modulo2^t. Thus all tail parity words occur once per fixed prefix, proving the average identity.

Conditional on the full A-step total r over the FULL period, prefix weight has the hypergeometric law

    h_k=E_k/E,
    mean=1+(m-1)*(r-1)/(A-1).

Use this finite center before comparing with the asymptotic approximation m/alpha. A critical-looking mode is already predicted by conditioning on total weight and is not independent evidence of tail randomness.

Three separate descriptive comparisons are useful:

    global enrichment R=sum J_k/E,
    cell enrichment R_k=J_k/E_k,
    conditional shape ratio (J_k/sum J_k)/h_k=R_k/R.

Global closeness is only a weighted average of cell ratios and does not establish uniform control over k.

## Exact falsifiers and positive observations

* A universal origin-block bound R<=1 is false. At r16 the ratio is1.00691393678. Every feasible weight cell is above its baseline; even the smallest cell ratio is63052/62985>1. Thus this failure is not caused only by a negligible extreme cell.
* Total closeness does not mean all cells are comparably close. At r20 the total ratio is1.00043633861, but the k20 ratio is2048/1771=1.1564.... At r14 the total ratio is1.00014742739, while k14 is8/7. The largest ratio in the panel is64/55 at r10,k10; it represents only eight starts, so it must not be described as a large global effect.
* Every observed actual mode belongs to the finite hypergeometric modal set. At r12 that set is{9,10}, with actual mode9; at r20 it is{15,16}, with actual mode15. This is finite compatibility with the comparison law, not proof that a particular stratum controls the asymptotic exponent.
* Conditional total variation is not monotonically decreasing: it is approximately0.000988 at r14,0.002647 at r16, and0.001741 at r18. Do not turn the endpoint values of the panel into a proved decay rate.

## Selection and interpretation controls

The target total r itself selects an unusual prefix-weight distribution. Consequently showing a mode near m/alpha is not a second independent observation supporting equidistribution. Compare J_k/sum J_k with h_k, not with the unconditional Binomial(m-1,1/2) prefix distribution.

The data are exhaustive deterministic counts at seven chosen parameter values, not independent random samples. Statistical p-values or confidence intervals based on random sampling are not warranted. A fixed-width band around a mode can have asymptotically vanishing probability even under the hypergeometric law while still carrying the same exponential growth rate; distinguish fraction dominance from exponent dominance.

Ratios close to one on this panel cannot establish the needed uniform asymptotic condition log2(R)/r<=lambda. This requires a theorem with controlled r-dependence and critical-mass uniformity. Reporting the measured finite ratio is valid; fitting it and treating the fit as that theorem is not.

No additional large runs, paid calls, or new orbit exclusion. The principal independently checks translated-block averages on one small case; the algebra above is the all-length justification.
