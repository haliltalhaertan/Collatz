# Two-parent merging and short family rules

2026-09-08. Exploratory exact arithmetic. Forward depth stays16. No OpenRouter call; cumulative spend remains $0.061356 of $2. Prior governed stages unchanged.

## New result and scope

Starting from54556 previously excluded residues of the checkpoint index k modulo65536, search only the10980 remaining classes. At each of the first16 accelerated forward steps (including timezero), allow TWO odd inverse parents, each with exponent1..4, followed by0..4 doublings. A valid target is a positive smaller member of S={20+27k:k>=0} for every nonnegative integer cylinder parameter.

This yields653 additional disjoint certificates:55209 excluded and10327 unresolved classes. These are exclusions only for the smallest exceptional member of S, not convergence proofs for all covered starts. The additional search is richer than before, not an increase in forward depth. No optimality claim.

## General certificate

If a common future value is y, choose

m_1=(2^u y-1)/3,
m_2=(2^v m_1-1)/3,
s=2^w m_2.

Both parents must be positive odd integers for every parameter, and s must be a smaller checkpoint. Starting from s, w halvings reach m_2, then an odd step and v halvings reach m_1, then an odd step and u halvings reach y. Thus s and the original start merge. The program checks all divisibility, parity, and affine coefficient conditions and independently advances the target back to the common value.

## Concrete compressed infinite family

For t>=0 let n=6912t+101 and s=5184t+74, whose checkpoint indices are256t+3 and192t+2. Their difference is64t+1>0 in index units.

Eight accelerated steps from n give:

6912t+101 ->10368t+152 ->5184t+76 ->2592t+38
 ->1296t+19 ->1944t+29 ->2916t+44 ->1458t+22 ->729t+11.

For the target s, one halving gives2592t+37. An odd standard step gives7776t+112; four halvings give486t+7. Another odd step gives1458t+22, and one halving reaches the same729t+11. All required parities are fixed for every t>=0. Therefore this entire family cannot contain the least exceptional checkpoint.

The simple family includes lifts already covered by older rules. It illustrates the new rule set; it must not be counted wholesale as newly excluded residue classes.

## Compression and validation

Each discovered witness was retried with shorter checkpoint-index moduli2^d, d>=its forward step count. Every accepted shorter family was independently checked with its own affine coefficients and base intercept. There are275 distinct resulting witness descriptions. They may overlap, are not a disjoint partition, and are not asserted to be minimal; d>=j is a conservative parity condition.

CERTIFICATES.json records all653 new fixed-modulus certificates. RULES.json records the275 shorter descriptions. RESULT.json contains summary counts. INPUTS.json binds the two input collections by SHA256. The finite symbolic search handles infinitely many starts per certificate; it is not a finite numerical Collatz-range verification.

## Relation to the full research

This step develops the deterministic checkpoint side using exact powersof2, divisibility by3, and shared orbit tails. It does not turn the earlier auxiliary-phase Theta(1/R) low-excursion contribution or compact-height estimate into deterministic convergence. The global dense C/R bound remains open, as does exhaustion of exceptional integer checkpoints.

The smaller marginal gain from this bounded extension is not evidence of a limiting coverage barrier or an impending proof. Continuing to enlarge inverse neighborhoods alone cannot establish exhaustion. The useful next question is whether these short index transformations admit an invariant or a decreasing rank covering the unresolved families. Finite residue graphs must retain actual integer parameter lifts; zero density of unresolved starts would still not exclude an exceptional orbit.
