# Residual diagnosis with unchanged search bounds

8 September 2026. Exploratory exact arithmetic. No external model cost or publication upload.

## Question and outcome

The previous rules required a smaller target for every cylinder parameter t>=0. Could the unresolved set largely be an artifact of that requirement, with contraction valid after a finite initial prefix?

Answer within the unchanged witness library: no. Among the 10,327 previously unresolved classes:

- 1 admits a contracting checkpoint target after a finite prefix;
- 10,323 have at least one valid checkpoint target but none with contracting affine coefficient;
- 3 have no valid checkpoint target in the enumerated library.

The library consists of direct forward endpoints through 16 accelerated steps, single inverse-parent exponents 1..6 followed by 0..6 doublings, and double inverse-parent exponents 1..4 each followed by 0..4 doublings. Time zero is allowed for inverse candidates. These are the previous bounds, not an enlarged search. No conclusion about arbitrary inverse depth or later forward times follows.

## Exact threshold principle

For an initial cylinder n(t)=A*t+B and a valid merging checkpoint s(t)=a*t+b with 0<a<A, strict decrease holds exactly when

    t > (b-B)/(A-a).

For nonnegative integer parameters the first permitted value is

    t0=max(0, floor((b-B)/(A-a))+1).

If all finitely many starts with 0<=t<t0 reach 1, and the tail targets remain positive checkpoints, no member of the cylinder can be the least exceptional checkpoint. This does not assert convergence of every cylinder member: a smaller merging target in the tail still needs the minimum-exception argument.

If a>A, the difference s(t)-n(t) is eventually positive; no finite-prefix removal creates a universally descending tail for that fixed witness. If a=A, strict decrease is equivalent to b<B. These elementary facts make this diagnostic exhaustive for the enumerated witnesses. This is a template-level diagnosis, not an impossibility theorem for Collatz.

## One explicit infinite family

The newly found certificate compresses to n=3456*t+20 and s=2592*t+20. For t>=1, both lie in S={20+27k:k>=0}, and n-s=864*t>0.

With T(n)=n/2 for even n and (3n+1)/2 for odd n:

    n -> 1728t+10 -> 864t+5 -> 1296t+8 -> 648t+4
      -> 324t+2 -> 162t+1 -> 243t+2.

The target reaches that same endpoint:

    s -> 1296t+10 -> 648t+5 -> 972t+8 -> 486t+4 -> 243t+2.

All displayed parities are independent of t. At t=0 the two starts coincide at20, so strict descent fails, but20->10->5->8->4->2->1 verifies the base directly.

Thus this family cannot contain the least exceptional checkpoint. Its checkpoint-index form is128t ->96t, with a separately verified zero base. Most of its fixed-modulus lifts were already covered. Only the residue k=0 modulo65536 is newly excluded in the current partition.

The cumulative count becomes55,210 excluded minimum-candidate classes and10,326 unresolved, modulo65536. These are not counts of proved-convergent residue classes.

## What this changes about research priority

The small gain is not itself a reason to abandon merging. The informative result is that relaxing the initial-prefix condition does not remove the dominant obstruction in this fixed library. More cleanup of affine intercepts cannot fix the10,323 classes with no contracting coefficient. They require different witnesses, a different checkpoint representation, or a different argument.

This turn does not justify unlimited deeper enumeration or a large automatic-ranking search. Any next template should first explain how it can change the missing coefficient contraction or prove a successful exit for residual families. The earlier analytic conditional estimate remains open and is unaffected.

## Reproduction and scope

Run run.py with Python3. It reads prior certificate files without importing their executable modules, records their SHA256 hashes in INPUTS.json, exhausts the stated finite library, verifies both affine paths for accepted certificates in the forward direction, and directly checks finite bases. RESULT.json, CERTIFICATES.json and OBSTRUCTED.json are generated outputs. The compressed family above was additionally checked through the separately written verifier.
