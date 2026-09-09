# Literature review tied to the current merging research

8 September 2026. Primary-source review of selected theorem statements and proofs; not a complete audit of every paper or an exhaustive bibliography. No new Collatz theorem, solver run, OpenRouter call, or publication upload in this review.

## Verified local starting point

Read research_double_merge_20260908/REPORT.md, RESULT.json and RULES.json. Current certificate totals are 55,209 excluded checkpoint-index residues modulo 65,536 and 10,327 unresolved. The latest extension has 275 overlapping compressed witness descriptions. These exclude the LEAST exceptional member of S={20+27k:k>=0}; they do not certify convergence of every member of the covered classes. The older conditional analytic target remains open.

## Primary sources and transfer decisions

1. **Kenneth M. Monks (2006), The sufficiency of arithmetic progressions for the 3x+1 conjecture.** [Author PDF](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf), Theorem 1.1 and Section 3. Every positive nonconstant arithmetic progression is sufficient through merging. The construction supplies a merging representative, without requiring it to be smaller than the original start. Application: our checkpoint choice is flexible; sufficiency alone supplies no decreasing certificate.

2. **K. Monks, K. G. Monks, K. M. Monks, M. Monks (2013), Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph.** [Author preprint](https://mathematicalgemstones.com/maria/papers/mmmm.pdf), Sections 6–7. Theorem 6.4 justifies our checkpoint. Proposition 6.5 uses cycle edge proportions to certify sufficient sets; its forward and cycle criteria differ. Theorem 7.3 transfers certain sufficient sets through graph folding, subject to its explicit cycle-length hypothesis. Application: systematic checkpoint selection and graph certificates, not automatic pruning of our minimum-exclusion classes.

3. **Emre Yolcu, Scott Aaronson, Marijn J. H. Heule, An Automated Approach to the Collatz Conjecture.** [Final arXiv v3](https://arxiv.org/abs/2105.14697v3); [conference PDF](https://www.cs.cmu.edu/~mheule/publications/collatz.pdf); [code](https://github.com/emreyolcu/rewriting-collatz). Relative termination supports rule removal, requiring control of the full ambient rewrite system. Matrix interpretations permit SAT-based certificate searches. Their simulation equivalence does not automatically apply to our guarded affine rules. Application: certificate architecture after a sound encoding; not a coverage theorem.

4. **David Applegate and Jeffrey C. Lagarias (2006), The 3x+1 Semigroup.** [Primary full text](https://arxiv.org/html/math/0411140), Theorem 1.1 and Section 2. They prove a weaker semigroup statement, allowing products that need not be actual orbit paths. Their fixed-depth multiplier scheme encounters a persistent -1 modulo 2^j class and handles the larger proof by induction across scales. Application: investigate structural residual families and finite certificates. Their multipliers and obstruction cannot be imported into our merging system without a separate proof.

5. **Daniel J. Bernstein and Jeffrey C. Lagarias (1996), The 3x+1 Conjugacy Map.** [Author PDF](https://websites.umich.edu/~lagarias/doc/bernstein.pdf), Introduction. The parity coding conjugates Collatz on the 2-adic integers to a shift. Application: exact parity-cylinder bookkeeping. A compatible infinite residue sequence is a 2-adic object; positive ordinary-integer realization remains an additional condition. Cycles of the conjugacy map itself must not be mistaken for Collatz cycles.

6. **Ilia Krasikov and Jeffrey C. Lagarias (2003), Bounds for the 3x+1 problem using difference inequalities.** [Author PDF](https://websites.umich.edu/~lagarias/doc/krasikov.pdf), abstract and setup. Computer-assisted inequalities yield at least x^0.84 predecessors below x of any fixed positive a not divisible by 3, for sufficiently large x depending on a. Application: quantitative inverse-basin growth. This is a historical established bound, not a claim to be the latest record, nor an exhaustion theorem.

7. **Mishel Carelli (ICALP 2026), Loop Termination and Generalized Collatz Sequences.** [Publisher full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.175/LIPIcs.ICALP.2026.175.html), Section 4 and Theorem 20. Polynomial-time decidability for one-variable linear-constraint loops is conditional on a reachability conjecture. Its weak Collatz maps have a common multiplier across residue classes. Application: a boundary result; neither ordinary Collatz nor our guarded checkpoint system has been identified with that special class.

8. **Terence Tao, Almost all orbits of the Collatz map attain almost bounded values.** [Current record](https://arxiv.org/abs/1909.03562). Almost-all logarithmic-density control does not exclude a single exceptional orbit. The prior project review of the critical conditioning mismatch remains operative.

9. **Manuel Inselmann, An approximation of the Collatz map and a lower bound for the average total stopping time.** [Primary record](https://arxiv.org/abs/2402.03276). Almost-all descent estimates are relevant to typical trajectories; they do not establish uniform control of our remaining integer families.

10. **Goncalves, Greenfeld, Madrid, Generalized Collatz Maps with Almost Bounded Orbits.** [Primary record](https://arxiv.org/abs/2111.06170). Retain the earlier local review's hypothesis audit before any use of its renewal estimates. This turn refreshed the record, not the complete technical proof.

## Our own synthesis: three obligations, not one

Let B be the set reaching 1, E its complement, and let x~y mean their forward orbits merge. Determinism gives x in E iff y in E whenever x~y.

Suppose S is sufficient. If E is nonempty, E intersects S. Therefore it has a least element s*. A certificate s~m with m in S and m<s excludes s as s*. This proves the logic behind our certificates without proving s in B.

A complete descent-by-merging proof would need:

1. Soundness: every certified edge represents actual merging of positive integers.
2. Coverage: every checkpoint outside a verified convergent base admits a certified reduction.
3. Well-foundedness: chosen reductions cannot continue infinitely.

The current decreasing rules address soundness and already have the integer rank s (equivalently k). Their standalone termination is immediate. Coverage remains missing. Consequently, proving termination of just those rules is not additional Collatz progress: unhandled checkpoints become stuck states, with no evidence that they reach 1.

A second trap is deleting all 55,209 covered classes from an orbit graph. The least exceptional checkpoint cannot be in these classes, but larger exceptional checkpoints along its orbit are not excluded by that argument. For an abstract illustration only, consider a map with 20->74->20 and 47->74, with none reaching 1. Then 74 merges with smaller 47, yet the least exceptional checkpoint 20 visits 74. This is a logical countermodel to the pruning inference, not a Collatz example.

Sound finite graphs may overapproximate actual trajectories. If every path in such a graph is impossible by a certified bound, that can establish exclusion. A surviving graph cycle proves nothing about positive integer realization. Neither graph folding nor a SAT encoding should discard the affine integer parameter or its domain guards.

## Actionable priorities

First audit the uncovered domains and identify repeated symbolic families, including behavior organized by v2(n+1). The semigroup comparison motivates this question; it proves no barrier for our rules. Next compare a few alternative sufficient checkpoints using identical bounded search settings. Finally, attempt guarded reductions with temporary increases only if the complete composite path has verified merging and decrease, or a rigorously defined well-founded rank.

Do not equate a higher excluded percentage with global convergence. Do not assume almost-all estimates hold uniformly after our endpoint conditioning. A useful next outcome is a certified new family or a precise obstruction to a restricted certificate template, even if all global questions remain open.

This report is local and outside the previously uploaded V1 package. No governed files were modified.
