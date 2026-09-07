# XUB small-b contraction and resonance propagation

Date: 2026-09-07

Status: exact exploratory algebra derived from the audited XUB pair operator. The identities below passed a separate read-only audit with minor domain and wording repairs, which are incorporated here. XUB and all downstream claims remain open.

## 1. Exact lacunary form

Let

`beta=log_2(3)-1`, `q(x)=exp(2*pi*i*2^x)`, and `z=2^(x-beta)>0`.

Since `2^beta=3/2`, the audited pair operator

`A_b(x)=q(x)/(b+1) sum_(u=0)^b q(x+u-beta)`

becomes

`A_b(x)=exp(3*pi*i*z)/(b+1) sum_(u=0)^b exp(2*pi*i*2^u*z)`.

Thus, with `e(t)=exp(2*pi*i*t)`,

`|A_b(x)|=|S_b(z)|`, where `S_b(z)=(b+1)^(-1) sum_(u=0)^b e(2^u z)`.

For `b>=1`, exact expansion of the square gives

`1-|A_b(x)|^2 = 4/(b+1)^2 sum_(0<=u<v<=b) sin^2(pi*(2^v-2^u)*z)`.

In particular, all terms vanish exactly if and only if the `u=0, v=1` term vanishes, so

`|A_b(x)|=1 iff z is a positive integer`, for every `b>=1`, because the present domain is `z>0`.

For `b=0`, `|A_0(x)|=1` identically.

## 2. Small-b formulas

The contraction deficits are:

`b=1:`

`1-|A_1|^2 = sin^2(pi*z)`.

`b=2:`

`1-|A_2|^2 = 4/9 * (sin^2(pi*z)+sin^2(2*pi*z)+sin^2(3*pi*z))`.

`b=3:`

`1-|A_3|^2 = 1/4 * sum_(d in {1,2,3,4,6,7}) sin^2(pi*d*z)`.

`b=4:`

`1-|A_4|^2 = 4/25 * sum_(d in {1,2,3,4,6,7,8,12,14,15}) sin^2(pi*d*z)`.

These are lacunary exponential sums, not ordinary fixed-ratio geometric sums once `b>=2`.

## 3. Uniform contraction away from the integers

Let `0<eta<=1/2` and `dist(z,Z)>=eta`. The pair `u=0,v=1` alone implies

`1-|A_b(x)|^2 >= 4 sin^2(pi*eta)/(b+1)^2`.

Consequently, for every fixed `B>=1` and `1<=b<=B`,

`|A_b(x)| <= exp(-c_(eta,B))`,

where one valid choice is

`c_(eta,B)=2 sin^2(pi*eta)/(B+1)^2`.

Using several small positive symbols therefore gives a common white-region contraction. It does not remove the resonance set: every `b>=1` still has exact modulus one at every integer `z`.

## 4. Exact black-to-black propagation lemma

The pair-state dynamics is

`z' = (2^(b+2)/9) z`.

Fix `B>=0` and choose

`0<eta<1/(9+2^(B+2))`.

Suppose `0<=b<=B`, `dist(z,Z)<eta`, and `dist(z',Z)<eta`. Let `n,n'` be the unique nearest integers to `z,z'`. Write `z=n+delta`, `z'=n'+delta'`, with `|delta|,|delta'|<eta`. Then

`2^(b+2)n-9n' = 9delta'-2^(b+2)delta`.

The left side is an integer, while the chosen eta makes the absolute value of the right side strictly less than one. Hence both sides vanish:

`2^(b+2)n=9n'`.

Since powers of two are coprime to nine,

`9 divides n`, and `n'=2^(b+2)*(n/9)`.

This proves the black-to-black propagation lemma exactly.

## 5. Consecutive black runs force high 3-adic divisibility

Consider `L` consecutive transitions with `0<=b_j<=B`, and suppose every entry state and the final exit state lies in the eta-black set. Applying the previous lemma repeatedly gives

`9^L divides n_0`

and

`n_L = 2^(sum_j(b_j+2)) n_0 / 9^L`,

where `n_j` is the nearest integer to `z_j`.

The low-state case `n_0=0` is exceptional and must be handled by a killed/low-excursion estimate. For an eta-black run whose initial nearest integer satisfies `n_0>=1`, a long bounded-symbol black run requires a correspondingly large 3-adic valuation of that nearest integer.

## 6. Conductor amplification on the actual ternary starts

On the actual boundary-start arrays, write

`z_0=2^E/3^D`, with `E,D` nonnegative integers. More precisely, at the original boundary start indexed by `t`,

`E=t+floor(beta*t)+1`, `D=t`, and `z_0=2^(1-{beta*t})` lies strictly between one and two.

If an `L`-step bounded-symbol positive-black run occurs, the preceding result gives `n_0=9^L h` for an integer `h>=1` and

`|2^E/3^D-9^L h|<eta`.

Equivalently,

`|2^E-h*3^(D+2L)|<eta*3^D`,

or

`dist(2^E/3^(D+2L),Z)<eta/9^L`.

Thus a length-`L` positive-black run at conductor `3^D` forces an exponentially sharper near-integer resonance at the amplified conductor `3^(D+2L)`.

This is a deterministic implication. It is not yet a probability estimate for the conditioned bridge.

It also gives the exact size obstruction `n_0>=9^L`. At the original boundary start the nearest integer is one or two, so even one bounded-symbol black-to-black transition is impossible. This initial gain does not apply automatically to later run starts after a large pair total has increased the state.

## 7. What the small-b extension does and does not solve

Using `b=1,2,3,4` rather than only `b=1` has two rigorous benefits:

1. every positive symbol in this set contracts on the same eta-white region;
2. a consecutive black run made of bounded symbols forces the exact `9^L` divisibility and conductor-amplification condition above.

It does not prove that enough such bounded-symbol blocks occur in a useful arrangement, nor that the amplified resonance event is sufficiently rare under the actual microcanonical endpoint and first-passage conditioning. Large `b`, low-state excursions, parity seams, and short suffixes remain separate cases.

## 8. Repaired next load-bearing estimate

A promising sufficient route is to combine two estimates on the actual accessible central arrays:

1. the now-proved conditioned symbolic-block theorem producing polynomially many disjoint bounded-positive words of logarithmic length in every long central suffix; and
2. an arithmetic estimate showing that the conductor-amplification event

   `dist(2^E/3^(D+2L),Z)<eta/9^L`

   has total conditioned probability `O(1/m)` for `L` proportional to `log m`, after separating the low-state event `n=0`.

For the predeclared family in which every symbol lies in `{1,...,B}`, endpoint-compatible abundance is proved below the explicit logarithmic-length threshold recorded in `XUB_SYMBOL_BLOCK_THEOREM.md`. The required arithmetic counting estimate remains open. Any alternative word family must be selected before a numerical probe so that post-output word selection does not enter the evidence.

## Classification

- exact lacunary form and deficit identity: `[PROVED ALGEBRAICALLY]`;
- equality set for every fixed `b>=1`: `[PROVED ALGEBRAICALLY]`;
- uniform contraction for `1<=b<=B` away from integers: `[PROVED ALGEBRAICALLY]`;
- black-to-black divisibility and conductor amplification: `[PROVED ALGEBRAICALLY]`;
- conditioned abundance of bounded-positive logarithmic words in long central suffixes: `[PROVED]`;
- conditioned rarity of amplified positive resonances: `[OPEN — ARITHMETIC LOAD-BEARING STEP]`;
- low-state contribution at the needed scale: `[OPEN IN THIS DECOMPOSITION]`;
- XUB, E6-N2/B4, nonzero profile, polynomial lower bound, and Collatz: `[OPEN / NOT PROVED]`.
