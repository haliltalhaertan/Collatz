# Actual bounded counterexample to V<=mean

The proposed all-parameter constant-one bound is false even with the intended critical parameter prescription.

Take r5, A=floor(5 log2 3)=7, m=ceil(1.2*5)=6, and t1. Count odd starts in each translated block of length64 whose first seven shortcut states contain exactly five odd states.

Origin block[0,64): 9,39,47,55, giving G_0=4.

Second block[64,128): 71,79,83,91,95,97,105,107,121,123,125, giving G_1=11.

The total15 agrees with binom(6,4). Thus

    mean=15/2,
    population variance=((4-15/2)^2+(11-15/2)^2)/2=49/4,
    variance/mean=49/30>1.

This is an actual Collatz parity count, not the earlier synthetic histogram. It refutes V<=mean asserted for every r under this parameter prescription. It does NOT refute an eventual inequality, V<=C*mean with a fixed larger C, or V<=2^o(r)*mean; those would have the same relevant exponential strength and require separate evidence/proof.

## Bounded scan scope

actual_variance_scan.py enumerated all odd starts below2^A for each A2..14, all m1..A-1, and all target weights r1..A. There are910 parameter cases. Exact totals were checked against binom(A-1,r-1). Seventy-one cases violate V<=mean. Two violations satisfy A=floor(r log2 3): the witness above and r6,A9,m6 with V/mean=15/14. The latter uses a different m from the intendedceil(1.2r)=8.

Among the six scanned intended critical rows with t>0, only r5 violates the bound. No extension beyond the preset A14 limit was run. This absence in other small rows does not establish eventual validity.
