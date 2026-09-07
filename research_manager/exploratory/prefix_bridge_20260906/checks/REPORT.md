# Exact finite checks — V1 failure preserved, V2 narrow repair passes

## Scope and provenance

This was new exploratory arithmetic, not any old sealed source execution. No producer modules, sealed results, or canonical state were used or modified. Fixed cases: r=4,...,8 with n=0,...,5, plus r=16,n=1, all positive compositions a_i=1+z_i with sum z_i=n. This gives 31 (r,n) pairs and 2,935 paths. Each version was executed exactly once by this agent; the visible earlier trace contained no source execution. Input SHA-256 values were printed before each execution. This is local tool-order provenance, not external time attestation.

## V1 outcome

V1 performed 23,480 checks, with 2,935 failures, all in phase_concatenation. The error was the test's tail denominator 16*3^(r-3), which omitted a factor 27. The defect was explicitly recorded before execution in PRE_EXECUTION_PROVENANCE.md. All seven other checks passed, including the integer concatenation identity, CRT exponent identity, and residue formula. The original source and output are preserved.

The first failure is r=4,n=0,a=(1,1,1,1). B_4=65, B_3=19, B_tail=1 and s=3. The correct exponent is 65/1296=19/432+8/1296. V1 incorrectly compares against 19/432+8/48. This is a test formula defect, not a counterexample to correct concatenation.

## V2 outcome

After explicit manager authorization, V2 changed only that denominator and the output filename. It used identical cases and checks. All 23,480 checks pass on 2,935 paths; zero failures. It is transparently a post-output harness repair, not a claim that V1 originally passed. Wall times: V1 0.0959096 seconds; V2 0.0678415 seconds.

The exact identity tested is B_r=3^(r-3)B_3+2^s B_tail, and hence B_r/(16*3^r)=B_3/(16*27)+2^s B_tail/(16*3^r). The tail conductor retains r: cancellation of a factor 3^3 in that tail term is not permitted.

176 capped-prefix/r-mod-4 keys occurred. Observed B mod16 residues were all eight odd classes {1,3,5,7,9,11,13,15}. Every tested correction e16(vB) was nontrivial. These are finite computations, not a uniform asymptotic theorem. The direct literal analytic row-product crosscheck was not included; it was assigned separately to the auditor.

At r=16,n=1,a=(2,1,...,1): B=71613463, m=43046721, u=40356301, v=-15. The project exponent is 71613463/688747536; the ternary exponent modulo 1 is 28689622/43046721; the correction exponent modulo 1 is 7/16. Equivalently, ternary minus project is 9/16 modulo 1. The pure ternary phase therefore differs from the project phase.

## Domain limitation

At most sixteen residue classes (indeed only odd B here) does not mean sixteen exact-prefix classes. Exact positive prefixes range over infinitely many values as r,n increase. Their exact sum changes the remaining composition budget and phase multiplier. Nothing in these checks proves a finite-dimensional closed renewal system, uniform tail asymptotics, nonzero limiting coefficient, or O(1/r).

## SHA-256

- PLAN.md: 3a3fb9b5d9a8023370b9d1fdcb9dfc2bb798f756f436db10145b30637224992c
- exact_prefix_checks.py: 2efe6a8ce8c9c59da02f9ac058515a371d5467831066384af986fb93bacc3886
- RESULTS.json: 5bb9778ad1d2b1585d8bba3dcea7bc5fd76049c44420866a2409b6cf59e6b66e
- exact_prefix_checks_v2.py: ed6aced4569dccb91821845669488ba399cff0fb5cd471ecbe0b5ebc860bb979
- V2_REPAIR.md: bdc15c97f5a220ea60aadf7b07037e4db709028c3fe72d5ab9f65e77e481d194
- RESULTS_V2.json: 3b6fe2ac8166cee1f7891d4f3abfc4b70a847c3085e4d7c44fde8e12ce084c3d

Nothing in this bounded check proves Collatz.
