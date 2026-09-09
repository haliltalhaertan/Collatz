# Cross-audit: weighted Walsh threshold and centered prefix layers

2026-09-08. Read moments.md, check_centered_prefix.py, and CENTERED_PREFIX.json. No panel enumeration rerun; this is an independent algebra/source audit of the identities and recorded interpretation.

## Weighted Walsh bound: accepted

For mean-zero f, f(0)=sum_{S nonempty} fhat(S). Weighted Cauchy gives exactly

    |f(0)|^2 <= W_w * ((1+1/w)^t-1).

Consequently epsilon+tau log2(1+1/w)<2lambda is a correct sufficient exponential threshold. At w=21 it is weaker than the threshold obtained by routing the same W21 through the 22nd moment. Neither inequality proves a bound for the actual W_w. The mean-zero assumption is essential to omit the empty Fourier coefficient, and is correctly stated.

## Prefix centering: accepted; the large raw cancellation is largely algebraic

For one k layer write w_z=P[k,z], N=sum_z w_z, c=binom(t,r-k), p=c/q and I_z(a) for the tail-weight indicator used by the script. For every a,

    sum_z I_z(a)=c,
    E_a I_z(a)=p.

The first equality uses the parity-word bijection on all q residues; the second also uses invertibility of 3^k modulo q. Therefore

    sum_z (w_z-N/q) I_z(a)
      = sum_z w_z I_z(a)-N p.

Thus the script's cv is exactly the centered layer, not an approximation or a changed observable. The aggregate mean B follows by the stated Vandermonde count. Its V and sum_stratum_variances E satisfy V<=s E pointwise/Cauchy, where s is the number of layers and s=O(r).

The raw diagonal decomposes exactly as

    raw_diag - centered_diag
      = sum_k (N_k^2/q) p_k(1-p_k).

Indeed sum_z w_z^2=sum_z(w_z-N/q)^2+N^2/q. Moreover the covariance matrix of the I_z has zero row sums because sum_z I_z=c deterministically. The entire constant N/q component is therefore a covariance null direction. Large cancellation of this raw baseline is forced algebraically; its numerical magnitude is not evidence of a deep asymptotic cross-layer mechanism.

After centering there can still be substantive within-layer endpoint structure. centered_signature_diagonal is not itself the layer variance: off-diagonal z-covariances remain. A generic bound is E_k<=q*centered_diag_k, since the positive-semidefinite covariance matrix has trace q p(1-p); that q factor is potentially exponential and cannot be discarded.

## Interpretation correction

No code correction is required for the four recorded panels. The current final paragraph of moments.md correctly retracts the inference that every successful exponential-rate proof must preserve negative cancellation across k layers. Because s=O(r), proving a sufficiently strong uniform bound for the CENTERED layer variances loses only a polynomial factor via V<=sE. What remains open is obtaining those actual layer bounds, including within-layer signature covariance.

The saved cross_strata values even have both signs, but no asymptotic conclusion follows from four panels. The earlier phrase 'million-level cancellation' should be presented as a raw decomposition diagnostic with a large exactly removable constant baseline, not as a proved structural obstruction to layerwise estimates.
