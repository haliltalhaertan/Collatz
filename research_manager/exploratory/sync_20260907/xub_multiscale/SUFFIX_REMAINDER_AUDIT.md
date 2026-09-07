# XUB suffix and interruption remainder audit

Date: 2026-09-07

Verdict: `[PARTIAL CLOSURE / GROWING SHORT SUFFIXES REMAIN LOAD-BEARING]`.

## Closed pieces

- The exact memoryless restart incorporates overshoot as the first fictitious suffix increment and removes its initial phase with `q(a'_s)^(-1)`.
- The odd singleton is covered by the exact conditional generating function and has modulus one.
- For a uniform weak composition of `K` into `R` parts,

  `P(Y_1>=h | S_R=K)=binom(K-h+R-1,R-1)/binom(K+R-1,R-1)`

  and, on the actual central arrays, this is at most `C*rho^h`.
- Hence `P(B>=q | S_R=K)<=2C*rho^(ceil(q/2))`, and a union bound makes `B>=A log R` an `o(1/R)` event for `A>4/|log rho|`.
- For every fixed `R_0`, suffixes `R<=R_0` contribute `O_(R_0)(1/m)` after division by the full endpoint mass.

## Necessary distinctions

For fixed `B_0`, the event `B>B_0` has positive limiting density and is not a remainder. The audited useful-block theorem only selects many bounded-positive words; every other factor is discarded by modulus one. Divisibility propagation must never cross a moderate `B>B_0` interruption.

For `R<delta*m`, absolute values, first-passage flux, and positive local limits yield at best

`sqrt(m) sum_(R<delta*m) (m-R)^(-3/2) R^(-1/2) = O(sqrt(delta)*m^(-1/2))`.

This is too large by a factor of order `sqrt(m)`. Thus the whole growing short-suffix range cannot be labeled an endpoint error.

## Multiscale repair

Every accessible suffix, including `R=o(m)`, still satisfies `K-beta R=O(1)`. The symbolic theorem can therefore be reparameterized at its intrinsic scale `R`. The eventual complex estimate must be uniform over all sufficiently large accessible `R`, while the fixed finite range is handled positively.

The sufficient actual-array estimate is

`|L_R(a'_(m-R+1),b_r)/p_R(a'_(m-R+1),b_r)| <= C/R`.

It implies the summable convolution

`sqrt(m) sum_(s+R=m+1) s^(-3/2)R^(-3/2)=O(1/m)`.

This multiscale suffix cancellation remains open.

