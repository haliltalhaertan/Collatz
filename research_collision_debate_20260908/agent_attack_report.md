# Adversarial collision analysis

## Infinite family invalidating late-coordinate localization

For r>=4 set

    w=(2,3,1 repeated r-4 times,2,1)
    z=(1,3,1 repeated r-3 times,3).

Both have total A=r+4. Geometric summation gives

    B(z)=21*3^(r-2)-2^(r+2),
    B(w)-B(z)=2*3^r.

Thus the endpoint residues coincide, despite the last coordinates differing. Adding the same nonnegative d to both last coordinates leaves BOTH integer numerators unchanged and changes total to A=r+4+d. For r>=7, choose d=floor(r log2 3)-r-4 to land exactly in the critical band. This supplies arbitrarily long critical-band collisions whose changes reach the final coordinate. It disproves a global localization inference from the single-adjacent-transfer lemma, but that inference was already explicitly disclaimed in its report.

The construction does not give subexponential endpoints. Its common canonical M satisfies

    2^(d+2)*M+1 = c*3^(r-1)

for a positive integer c, hence

    M >= (3^(r-1)-1)/2^(d+2) = 2^(r+O(1))

under critical adjustment. No claim that M<2^(1.2r) holds uniformly or infinitely often follows. Modulo 3, c is constrained by the displayed identity; its actual representative can be large.

## Actual positive small-endpoint collision

At r=7,A=11:

    w=(2,3,2,1,1,1,1), B(w)=12613,
    z=(1,3,1,3,1,1,1), B(z)=8239.

Both yield M=161<2^(1.2*7). They are genuine accelerated positive trajectories:

    145 ->109 ->41 ->31 ->47 ->71 ->107 ->161
    147 ->221 ->83 ->125 ->47 ->71 ->107 ->161.

They coalesce at step4. This exposes ordinary synchronized mergers behind some small-endpoint fibers; it is not a Collatz counterexample or an asymptotic lower bound.

## Why this does not produce an automatic exponential fiber

The four-step core words u=(2,3,2,1),v=(1,3,1,3) both have mass8 and B values287,125. They require endpoint residue47mod81. Their inverse starts (256n-287)/81 and (256n-125)/81 differ2, so they cannot both satisfy residue47mod81 for a further copy of the same core. Repeated use cannot simply be counted as independent binary choices. This is a concrete compatibility obstruction, not a proof that every possible branching construction fails.

## Verification scope

agent_attack.py enumerates fixed critical masses for r5..14, recording smallest collision residue and a collision reaching the latest differing coordinate. Its JSON is diagnostic only. The infinite-family proof is algebraic, not an extrapolation from this panel. No paid calls or canonical-file edits.

## Challenge to the canonical-start reduction

The principal's proposed comparison between endpoint counts and initial-segment counts of canonical starts is a useful exact reduction, not itself a distribution theorem. Full-period counts of these parity cylinders are known from the positive compositions; incomplete intervals shorter than 2^A need additional arithmetic distribution control.

For ALL words, the true accelerated valuation sums satisfy S_(r-1)<A<=S_r. The final prescribed valuation can truncate the true last valuation if canonical M is even. Thus the full count must NOT be described as exact total A of the first r true accelerated valuations. Odd M gives the exact-total subevent. Equivalently, the full event prescribes exactly r odd states in A shortcut steps starting from an odd integer.

Injectivity supplies only F(X)<=ceil(X/2) for the positive odd starts. At X=2^(br+O(1)), this has exponent b, exceeding the ideal h_*+b-alpha by alpha-h_*=0.0793186... . Eliminating endpoint collisions from the representation does not eliminate the rare parity-pattern count. A theorem saving that exponent over the incomplete interval remains necessary; no such theorem follows from the reduction alone.
