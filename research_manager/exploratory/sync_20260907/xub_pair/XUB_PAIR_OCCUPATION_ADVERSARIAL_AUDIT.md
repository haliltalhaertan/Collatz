# Adversarial audit of the XUB pair-occupation route

Date: 2026-09-07

Verdict: `[PASS WITH MATERIAL SCOPE REPAIR; BROAD UNIFORM LEMMA REFUTED]`.

## 1. Exact counterexample to arbitrary-endpoint uniformity

If the proposed occupation estimate is asserted uniformly over arbitrary compatible endpoint data, take `J` complete pairs and condition on total `K=0`. The support then contains only `B_1=...=B_J=0`. Hence `N_eta=0` and

`E[exp(-c_eta N_eta) | K=0]=1`,

which cannot be bounded by `C/J` as `J` grows. This does not refute the actual G/H central arrays. It refutes the broader statement. The theorem domain must be restricted to the coupled accessible central regime, approximately `K-2 beta J=O(1)`, with short suffixes and both parity alignments treated separately.

## 2. Raw B=1 abundance does not imply white occupation

At pair entry write `z=2^(x-beta)`. The exact update after total `B=b` is

`z' = 2^(b+2) z / 9`.

Thus a run of `B=1` symbols gives `z_j=(8/9)^j z_0`. For every fixed `eta>0`, only `O_eta(1)` initial terms can stay at distance at least `eta` from the integer zero; the remainder are black. Therefore even a linear number of raw `B=1` symbols does not by itself produce linear or logarithmic white occupation.

The endpoint fixes only the total product. Early `B=0` or `B=1` blocks can drive the state deep into a low black region and later large totals can compensate. Such paths may be rare, but neither an endpoint local-limit theorem nor a raw-symbol law excludes them.

## 3. Exact central marginal

For `J` pair totals conditioned on sum `K`, a vector has weight proportional to `prod_j(B_j+1)`, and

`P(B_1=1 | sum B_j=K) = 2 binom(K+2J-4,2J-3) / binom(K+2J-1,2J-1)`.

If `K/J -> kappa>0`, this tends to `8 kappa/(kappa+2)^3>0`. This independently confirms that the obstruction is phase quality, not the raw availability of `B=1`.

## 4. Domain and seam repairs

- Do not condition uniformly on arbitrary leftover or overshoot values. Sum them with their exact weights, or split into a central window plus a controlled tail.
- A pair must not straddle the first-passage seam. Isolate one increment when parity requires it.
- Separate finite/short suffixes before invoking an asymptotic central-cone estimate.
- State every ratio only on the actual accessible array where its denominator is positive.

## 5. Ternary resonance

On the actual boundary start, pair-entry phases have the form `2^E_j/3^D_j`, with both exponents evolving along the conditioned path. The order of `2 modulo 3^D` and the deterministic rotation of `x mod 1` are not enough: whiteness depends also on the integer part of `x`, and the estimate is an occupation lower tail under endpoint and first-passage conditioning.

The useful repaired route is:

1. retain the proved raw-symbol and regular-cone estimates;
2. isolate low-state black excursions;
3. prove a positive-state ternary-resonance occupation estimate;
4. combine them only on the actual central arrays.

It may be advantageous to exploit contraction from the full operators `A_b(x)` for several small `b`, rather than only `b=1`; this is a candidate improvement, not a theorem.

## Final classification

- broad arbitrary-endpoint uniform occupation lemma: `[REFUTED]`;
- exact pair dynamics and long-black-run mechanism: `[PROVED]`;
- central raw `B=1` abundance: `[PROVED]`;
- inference from raw abundance to white occupation: `[INVALID]`;
- repaired actual-central-array logarithmic-white-opportunity estimate: `[OPEN]`;
- XUB and all downstream Collatz claims: `[OPEN / NOT PROVED]`.

