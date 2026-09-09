# Checkpoint descent combined with the existing conditional research

2026-09-08. Exploratory continuation. The old governed stages remain closed. No OpenRouter calls; cumulative spending unchanged at $0.061356.

## Deterministic checkpoint layer

Use T(n)=n/2 for even n and (3n+1)/2 for odd n. Let S={20+27k:k>=0}. Monks et al., Theorem 6.4, establishes that every exceptional cycle or divergent orbit meets S: [primary paper](https://mathematicalgemstones.com/maria/papers/mmmm.pdf). Thus if any nonconvergent positive integer exists, the nonconvergent members of S have a least element s*. A certified forward return from s* to a smaller member of S is impossible. This is stronger bookkeeping than merely reaching a smaller arbitrary integer: minimality here is within S only.

An explicit infinite family admits such a certificate. For t>=0,

432t+371 -> 648t+557 -> 972t+836 -> 486t+418 -> 243t+209.

Both endpoints belong to S; their checkpoint indices are 16t+13 and 9t+7. The latter is smaller by 7t+6, so this entire class is excluded as the least exceptional checkpoint. This does not prove the whole class converges unless the destinations are already known to converge.

## Exact finite-cylinder coverage

The script check_return.py fixes depth16, partitions checkpoint indices k modulo65536, and represents each infinite class as n=27*65536*t+(20+27r), t>=0. Each of the first16 parities is fixed within the class. Affine integer iteration gives exact coefficients a_j,b_j. A certificate is accepted only if a_j is divisible by27, b_j=20 mod27, a_j<=27*65536, and b_j<20+27r. These conditions prove a strictly smaller S-return for every t>=0.

RESULT.json records 50568 certified classes and14968 unresolved classes out of65536. An independent rational-affine representation checks every accepted certificate's endpoint coefficients. This is exhaustive arithmetic for a finite family of symbolic certificates, not sampling trajectories or evidence that an individual unresolved class contains a counterexample. Certified classes can lead to unresolved classes, so the covered proportion is NOT a proportion whose convergence has been proved.

## How the earlier work enters, and the missing bridge

The existing dense transform measures weighted arithmetic phases under an endpoint-conditioned composition law. Its small variable z is NOT the Collatz integer n. A white-point mark is NOT a visit to S, nor a certificate of numerical descent. Our proved Theta(1/R) contribution of a boundary-configured low excursion and exponential compact-height block bound must not be presented as probabilities of actual nonconvergence.

Nevertheless both analyses organize paths by exact valuation/parity words. For odd-to-odd Syracuse steps n_(j+1)=(3n_j+1)/2^a_(j+1), define A_j=sum_(i=1)^j a_i, A_0=0 and

C_j=sum_(i=0)^(j-1) 3^(j-1-i)*2^A_i.

Then exactly n_j=(3^j*n_0+C_j)/2^A_j. A descent condition must keep the positive affine correction: n_j<n_0 iff 2^A_j>3^j+C_j/n_0. Dropping C_j and using mean drift alone is invalid. This identity gives a common encoding, not a theorem transporting the previous conditional Fourier bounds to all actual integer orbits.

The useful combined program is therefore:

1. Use exact smaller-checkpoint returns to remove impossible minimal-exception cylinders.
2. Keep the unresolved cylinders and their endpoint residues explicitly, rather than replacing them by unconstrained iid words.
3. Seek a theorem that these unresolved integer cylinders cannot nest forever into a positive-integer orbit avoiding the known basin. Existing average weighted estimates may suggest which words matter, but do not supply this deterministic exclusion.

Even zero limiting density of unresolved starts would not exclude one exceptional orbit. Likewise a sequence of compatible residue cylinders may describe a 2-adic integer without describing a positive ordinary integer. Either an integer-valid well-founded descent argument or a rigorously proved avoidance-to-estimate contradiction is still needed.

## Next bounded target

Study the return graph of the14968 unresolved classes with symbolic merging rules, retaining size comparison and integer-lift validity. Prefer deriving short families like k=16t+13 ->9t+7 over blindly increasing computation depth. Check whether an explicit rank decreases under every unresolved transition; no such global rank or contradiction is established here. The earlier dense C/R estimate and the checkpoint-completeness problem both remain OPEN.
