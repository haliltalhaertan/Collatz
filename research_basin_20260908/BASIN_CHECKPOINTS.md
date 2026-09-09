# Basin avoidance and unavoidable checkpoints — 2026-09-08

Exploratory conceptual research prompted by the user's observation: a nonconvergent orbit must avoid every number already connected to 1. No new Collatz theorem is claimed, no previous governed stage is reopened, and no external model spending is incurred.

## Exact elementary formulation

For the standard Collatz map C, let B be the set of positive integers reaching 1, and E its complement. Membership satisfies n in E iff C(n) in E. Thus E, if nonempty, is both forward closed and closed under every valid predecessor. In particular n and 2n have the same basin membership. The claim E is empty is precisely Collatz; closure alone does not prove emptiness.

Define two starts to merge when some forward iterate of one equals some forward iterate of the other. Because the map is deterministic, merging is an equivalence relation. Each entire equivalence class has the same basin membership. For odd n, 3(4n+1)+1=4(3n+1), hence n and 4n+1 merge. Iterating gives the family 4^j n+(4^j-1)/3, j>=0. This family relation does not imply that its representative reaches 1.

If E is nonempty, its minimum m cannot be even. It cannot be 1 modulo 4: writing m=4k+1>1, after the odd step and two halvings the orbit reaches 3k+1<m. Therefore m=3 mod 4. Every later term in its orbit is at least m. These are familiar elementary necessary conditions, not evidence that E exists or a new classification of all exceptional numbers.

## Primary literature found

Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, Maria Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, arXiv:1204.3904v2 (2012), journal publication 2013. [Record](https://arxiv.org/abs/1204.3904), [author PDF](https://mathematicalgemstones.com/maria/papers/mmmm.pdf).

The paper distinguishes sufficient sets (every orbit merges with an orbit starting in the set) from direct orbit interception. It states that every positive forward orbit for the accelerated map T meets 2 modulo 9, and every nontrivial cycle or divergent orbit meets 20 modulo 27. Standard Collatz trajectories contain their accelerated T trajectories, so these interception statements also apply to standard trajectories. General arithmetic-progression sufficiency must not be misstated as every orbit visiting every progression.

Consequently, proving every positive integer 2 mod 9 converges would prove Collatz. Proving convergence for all positive integers 20 mod 27 would also exclude every exceptional component. Neither convergence assertion is established here. In particular a finite verification of members of either progression leaves its infinite remainder open.

Ilia Krasikov and Jeffrey C. Lagarias, *Bounds for the 3x+1 Problem using Difference Inequalities*, Acta Arithmetica 109 (2003), 237–258. [Primary paper](https://websites.umich.edu/~lagarias/doc/krasikov.pdf), [arXiv](https://arxiv.org/abs/math/0205002). Their computer-assisted result gives at least x^0.84 integers up to x reaching 1 for sufficiently large x. This is cited as an established historical bound, not asserted to be the latest record. A large inverse basin is not by itself an unavoidable basin: counting its members does not establish intersection with every orbit.

## Concrete possible research direction, still open

The useful target is a checkpoint set S with TWO separately proved properties: (1) every exceptional orbit must hit S; (2) every member of S reaches 1. The cited work supplies examples for (1), leaving (2). Alternatively one could prove that each member of S merges with a smaller member of S, with an explicitly resolved finite base. Well-ordering then proves convergence of all S, and interception proves convergence globally. No such decreasing merge rule is supplied here; finding one may be as difficult as the original problem.

Why this differs from raw inverse enumeration: merging with a known safe orbit suffices, even at a large common value. It need not occur by immediate numerical descent. But an infinite growing inverse tree, or a finite congruence graph with no apparent escape, is not a completeness proof. Finite residue projections must retain actual integer-lift validity before ruling out infinite trajectories.

Recommended next discussion: focus on an unavoidable class such as 20+27k and ask what additional arithmetic relation could connect all its members to the known basin. Keep ordinary sufficiency, actual interception, finite evidence, and a universal convergence proof distinct.
