# CP20 Task 8B3 E6 — Manager Integration Decision

## Verdict

**[ACCEPTED WITH SCOPE REPAIR — E6-N1 ONLY]**

E6-N1 is accepted: the finite coefficient recurrence, formal/analytic
Hadamard identity, probability-numerator recurrence, and conditioned-geometric
Feynman–Kac representation are exact. E6-N2, E6-N3, E6-N4, and E6-N5 remain
open. Nothing here proves Collatz.

## Integrity and reproduction

- Accepted pre-run seal ZIP SHA-256:
  `83a26e81fc8a96479a6b76fdd33f962a047885115f00ec6a892248a0c07b6c57`.
- Returned complete-package SHA-256:
  `9511dc8c9bbd0485f159bbfdf2b5f1f784813af156db5085d90e4faccf1be849`.
- Final manifest SHA-256:
  `7c0f7ce6de55582cc1e69d12092f1d822cf169d897a0c36e28570e32378731d1`.
- Directory pre-run manifest: 5/5 PASS.
- ZIP-internal pre-run manifest: 5/5 PASS; six declared ZIP members only.
- E5/manager dependency hashes: 5/5 PASS.
- E5 root and ZIP-internal manifests: 20/20 PASS each.
- E6 root and ZIP-internal manifests: 19/19 PASS each; complete ZIP has 20
  members including its manifest.
- The deterministic E6 verifier was rerun read-only and passed every assertion.
- An independent implementation checked 28 small residue-counter cases with
  maximum L1 counter difference zero and independently reproduced the
  `(r,n)=(2,5)` exact-zero case.
- All five fixed E5-to-E6 numerator conversions were recomputed independently;
  maximum absolute binary64 difference was zero.

The run record reports one invocation of the sealed main source. The immutable
seal, authorization witness, fixed output schema, and recorded command support
that chronology. Exact invocation count is not cryptographically enforceable
from the final filesystem alone, so it is retained as provenance rather than
a mathematical theorem.

## Accepted exact statements

For `r>=2`,

\[
A_r(n)=\sum_{k=0}^n p^{\rm fin}_{r,k,4}A_{r-1}(k),
\]

\[
\mathcal A_r(z)=\frac{1}{1-z}
(P^{\rm fin}_{r,4}\odot\mathcal A_{r-1})(z),
\]

formally and analytically for `|z|<1`, and

\[
N_r=b^ra^{n_r}A_r(n_r)
=D_r\,\mathbb E[F_{r,4}\mid S_r=n_r].
\]

The phase multiplier is periodic in the coefficient index with exact period
`2*3^(r-1)`. The cyclotomic residue-counter representation and its three-block
exact-zero criterion are also accepted.

## Scope repairs

1. The M1 obstruction closes only exact endpoint-state coboundaries and
   multiplicative endpoint-state approximations whose defects are uniformly
   summable in feasible-state supremum norm. It does not exclude nonlocal,
   history-dependent, or block martingales.
2. The `H^2` phase multiplier isometry defeats the direct norm-majorant
   argument. It is not a no-go theorem for every anisotropic, ordered-product,
   contour, or spectral method.
3. The exact two-sided bridge decomposition is accepted as a representation,
   not as a contraction theorem.
4. The five order-one values of `r^(3/2)N_r` remain `[NUM]`; they establish no
   power law, coefficient, or nonvanishing theorem.

## Route decision

- **[PARK]** Exact/local state-coboundary M1, direct norm-only M2,
  Brownian/Lipschitz-only M3, and nonquantitative exact-nonzero M4.
- **[OPEN]** A two-sided conditioned Feynman–Kac block kernel coupled to
  quantitative arithmetic residue mixing and a uniform excursion-tail bound.

The audit stop rule did not fire. E6 obtained only E6-N1, and the accepted M1
obstruction closes one ansatz class rather than the complete critical-bridge
route.

## Single authorized next action

Open E7 as a two-stage sealed proof task. Stage 0 must define an exact
two-sided complex block kernel, freeze the block/window geometry and all
falsification criteria, package the pre-run sources, and stop. No E7 Stage 1
calculation or proof search is authorized until the resulting seal hash is
accepted externally.

