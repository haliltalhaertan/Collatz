# XUB multiscale arithmetic-occupation findings

Date: 2026-09-07

Status: `[ROUTE REPAIRED / XUB OPEN]`.

This record continues the exact first-passage, paired-increment, small-`b`, and symbolic-block reductions. Three independent read-only analytic lanes examined the low-state branch, positive amplified resonances, and the suffix/seam remainders. No numerical experiment or sealed E7/B4 source was run.

## 1. Exact actual-array coordinates

For a restarted suffix with `R=2J+epsilon`, `epsilon in {0,1}`, condition the `R` raw geometric increments to have total `K`. On the actual G/H arrays,

`K-beta*R in (-15-2beta,-13-2beta)`.

If `tau` indexes the boundary start, then

`z_0=2^(1-{beta*tau})=2^(tau+floor(beta*tau)+1)/3^tau in (1,2)`.

Writing `H_j=B_1+...+B_j` for the first `j` pair totals,

`z_j=2^(E_j)/3^(D_j)`

with

`E_j=tau+floor(beta*tau)+1+2j+H_j`, `D_j=tau+2j`,

and exactly

`log_2 z_j=1-{beta*tau}+H_j-2beta*j`.

## 2. What is now closed

1. The memorylessly summed overshoot is exactly the fictitious first increment in the restarted suffix. Its compensating phase is `q(a'_s)^(-1)`. No pair crosses the true first-passage seam.
2. The odd singleton is already represented by the exact generating-function factor `(1-z)^(-1)` and has modulus one. Both parities are covered.
3. Under the conditioned uniform-composition law, one raw coordinate satisfies a uniform geometric tail. Consequently

   `P(max_j B_j >= A log R | S_R=K) <= C R rho^(A log R/2)`.

   For natural logarithm and `A>4/|log rho|`, this is `o(1/R)`. Truly logarithmically huge symbols are negligible.
4. Every fixed finite suffix range `R<=R_0` contributes `O_(R_0)(1/m)` to the first-passage convolution by the existing first-passage flux bound.

## 3. What was refuted or repaired

1. **Low-state hit rarity is false.** In the black region, nearest integer zero is exactly `z_j<eta`. At any fixed bulk fraction, its conditional probability tends to `1/2`; even a fixed initial run of zero pair totals enters the low region with a positive limiting probability.
2. **Low steps do not give uniform contraction.** `|A_0|=1`, and an arbitrarily long low `b=1` run can have a product of moduli bounded away from zero.
3. **The complement of a fixed bounded alphabet is not rare.** For fixed `B_0`, `P(B>B_0)>0`. Moderate symbols outside selected useful words are harmless only because all unused factors have modulus at most one; they are not a small-probability error.
4. **Per-start resonance bounds plus a union bound are structurally mismatched.** Useful-word abundance requires an exponent `a<1`; even granting an `O(R^(-1/2))` single-atom estimate, summing over `O(R)` starts gives `R^(1/2-a)`, far above `O(1/R)`.
5. **A fixed-fraction short-suffix range is not an endpoint error.** Absolute values give only `O(sqrt(delta)*m^(-1/2))` for `R<delta*m`, not `O(1/m)`. Every growing suffix scale still needs complex cancellation.

## 4. Exact positive-resonance reduction

For a preregistered bounded-positive word of length `L`, a fully black positive run forces

`|2^(E_j)-h*3^(D_j+2L)| < eta*3^(D_j)`

for some integer `h>=1`. Equivalently,

`dist(2^(E_j)/3^(D_j+2L),Z) < eta/9^L`.

The corresponding endpoint-conditioned probability is an exact finite coefficient sum over the prefix total `H_j` and word total. It is recorded in `AMPLIFIED_RESONANCE_WEIGHTED_COUNT.md`.

This event says that a selected short shift of the binary expansion of `1/3^(D_j+2L)` begins with `Theta(L)` equal bits. The multiplicative order `ord_(3^Q)(2)=2*3^(Q-1)` describes an exponentially longer full orbit and supplies no short-orbit discrepancy estimate on the accessible `E_j=O(m)` window.

## 5. Correct multiscale target

Let `Q_R` be the preregistered disjoint block grid at the intrinsic suffix scale `R`, with `L_R=floor(c log R)` below the audited symbolic threshold. For a block `q`, let:

- `G_q`: every pair total lies in `{1,...,B_0}`;
- `L_q`: its entry is in the low state `z<eta`;
- `R_q`: the exact positive amplified-resonance event;
- `C_q=G_q intersect L_q^c intersect R_q^c`.

Every `C_q` block contains at least one eta-white positive entry and therefore a uniform contraction. The narrow sufficient open estimate is

`E[exp(-lambda sum_(q in Q_R) 1_(C_q)) | S_R=K, exact first-passage data] <= C/R`

uniformly for every sufficiently large accessible `R` and every actual coupled `(r,R,tau)` array. It must not be generalized to arbitrary independent endpoints.

An equivalent target is the actual-array suffix estimate

`|L_R(a'_(m-R+1),b_r)/p_R(a'_(m-R+1),b_r)| <= C/R`.

Together with the fixed finite-suffix bound and the first-passage flux, this gives

`sqrt(m) sum_(s+R=m+1) s^(-3/2) R^(-3/2)=O(1/m)`

and would prove XUB for this route.

## 6. Scientific classification

- exact coordinates, overshoot seam, parity, logarithmically huge-symbol tail, and finite-suffix treatment: `[PROVED]`;
- low-state hit rarity: `[REFUTED]`;
- fixed-alphabet-complement rarity: `[REFUTED]`;
- per-start union-bound route at the useful-word threshold: `[INSUFFICIENT]`;
- exact weighted resonance formula: `[PROVED REDUCTION]`;
- multiscale marked occupation/Laplace estimate: `[OPEN — LOAD-BEARING]`;
- XUB, E6-N2/B4, a nonzero profile, polynomial lower bounds, and Collatz: `[OPEN / NOT PROVED]`.

