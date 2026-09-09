# Smaller-checkpoint merging: synthesis and exact extension

2026-09-08. Exploratory. No old governed-stage changes. No external model calls; cumulative OpenRouter spending $0.061356 of $2.

## What changed

Previous certificates required the starting orbit to visit a smaller checkpoint in S={20+27k:k>=0}. The user's basin observation allows a larger certificate class: two orbits may merge at a common future value, even if the original orbit never visits the smaller checkpoint itself.

If any exceptional positive orbit exists, the interception theorem of Monks et al. supplies an exceptional member of S; choose its minimum s*. If s* merges with a smaller member of S, that member is exceptional too, contradicting minimality. This argument uses minimum within S, not an unjustified assumption that all smaller arbitrary integers converge. The external premise is Theorem6.4 of [Monks et al.](https://mathematicalgemstones.com/maria/papers/mmmm.pdf), already checked in the basin work.

## Exact sibling construction

At any forward value y, choose u>=1 such that m=(2^u y-1)/3 is a positive odd integer. Then m->2^u y->...->y under the standard rule. For v>=0, s=2^v m also reaches y. Thus the start and s merge.

For an affine family y=a t+b, all t>=0, require both coefficients in (2^u y-1)/3 to be integers, its t coefficient even and its intercept odd. The target s must have coefficient0mod27, intercept20mod27, and be strictly below the original start for every t>=0. These are exact arithmetic conditions; invalid integer inverse edges are rejected.

## A simple infinite family

Let n=6912t+128 and s=864t+20 for any integer t>=0. Both are checkpoints, with indices256t+4 and32t. Starting n, seven halvings give54t+1, then one accelerated odd step gives81t+2. Starting s:

864t+20 ->432t+10 ->216t+5 ->648t+16 ->324t+8 ->162t+4 ->81t+2.

The paths meet, and s<n. Hence no member of n=6912t+128 can be the least exceptional checkpoint. This is an exact infinite-family certificate, not a finite numerical sample. At t=0 the start128 reaches1 without ever visiting20, illustrating why merging is more general than a smaller-checkpoint forward return.

## Bounded enumeration and validation

Input: previously saved50568 certified residues modulo65536 for k in20+27k. Only the14968 unresolved residues were searched. Forward depth stayed16. At each forward state, allowed1<=u<=6 and0<=v<=6. The recorded new3988 certificates are disjoint from the old set.

- Previous certified classes:50568.
- Additional smaller-checkpoint MERGING certificates:3988.
- Combined:54556 of65536.
- Unresolved under these bounded rules:10980.

run.py verifies both affine paths for every certificate, including parity invariance for every t, exact common endpoint, positivity, target checkpoint congruence, and strict decrease. Complete new certificates are in CERTIFICATES.json; summary in RESULT.json. Forward prefixes were not lengthened, but the search rule set was enlarged by the bounded inverse construction. No claim that this is an optimal or exhaustive merging search.

Covered classes are excluded only as possible least exceptional checkpoint classes. A certificate may lead to a smaller unresolved checkpoint; convergence of all covered classes is not established. Unresolved classes are not claimed to contain exceptions. Counts refer to this fixed residue partition, not probability of Collatz being true.

## Incorporating the older analytical route and the new questions

The common encoding is exact affine evolution of parity/valuation words. The powersof2 and3 in the sibling formula connect the user's prime/divisibility questions to actual valid inverse edges. Changed-rule counterexamples taught us to preserve integer divisibility and not infer global attraction merely because a division eventually occurs.

Our previous dense phase-transform results remain unchanged: a boundary-configured low excursion contributes Theta(1/R), and compact-height block-start paths have a joint exponential upper bound. They concern an auxiliary conditional law, not the number of exceptional integers. No theorem transfers these averages to deterministic exhaustion of checkpoint cylinders. Nor does the additional merging coverage prove the open global dense C/R bound.

This turn advances the deterministic side of the synthesis: more exact certificates describe which parity cylinders cannot contain a minimal exception. A future analytic estimate could be targeted at the remaining cylinders, but their conditioned weights and the implication from average control to exclusion would have to be proved explicitly.

## Next bounded objective

Compress the new merge certificates into short residue-family rules and inspect how their target indices enter the10980 unresolved classes. Seek a well-founded decreasing rank or an integer-valid contradiction for any indefinitely unresolved component. Do not infer exhaustion from coverage percentages, zero density, or cycles of a residue-only projection. Collatz and both main open estimates remain unresolved.
