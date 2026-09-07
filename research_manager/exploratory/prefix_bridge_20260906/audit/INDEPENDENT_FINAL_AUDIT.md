# Independent final audit of the exploratory prefix bridge

Verdict: PASS FOR THE STATED EXACT REDUCTION AND PREFIX-CUTOFF LEMMA. No asymptotic cancellation theorem, nonzero profile, canonical B4 acceptance, or Collatz result is established.

## Independence and scope

The preserved INDEPENDENT_INITIAL_AUDIT.md was derived before inspecting the other agents' files. The audit source independent_row_checks.py was independently written from the formulas and executed once before opening EXACT_PREFIX_REDUCTION.md or the checker's source/output. It imports neither producer modules nor old sealed sources. It uses a direct power sum, whereas the checker uses a Horner recurrence. No canonical state, Git branch, or seal was edited by this auditor.

The audit was supplied the analytic row definition: zeta4=e_48(1), with rows s>=2 equal to exp(2 pi i 2^(s+S_(s-1)-5)/3^s). This review verifies its algebraic relation to B; it does not independently certify provenance of that supplied definition from historical seals.

## Audited algebra

For a_i=1+z_i, A_(s-1)=s-1+S_(s-1). Therefore each row exponent is 2^A_(s-1)/(16*3^s), including s=1 giving 1/48. The sum is B_r/(16*3^r) as a rational equality, not merely modulo one. No modular inverse is substituted for analytic negative exponents.

The CRT decomposition, first-three truncated-increment classification for r>=4, and four-prefix identity in producer sections 2-3 are correct. In the latter, m=r-4 and J=sum first four z_i, and the phase is

    e_1296(B4) * e_(3^r)(2^J B_m).

The conductor is 3^r=3^(m+4), not 3^m. The fourth prefix increment changes J although B4 only depends on its first three increments. Finite mod-16 classes do not produce finitely many actual J or a fixed finite-frequency closure.

Counting prefix-tail pairs gives producer section 4 exactly: conditioned on J=j, prefix and tail are independent uniform weak compositions of j into four and n-j into m parts. The binomial weights w sum to one. This validates the scalar mixture G=sum_j w_j D_j H_j. Domains r>=5,n>=0 include m=1 and n=0; critical r14,15 are degenerate but valid. An argument that insists on nondegeneracy must separately restrict r>=16; these exact identities do not need that restriction.

## Audited cutoff proof

For a single coordinate, translation gives the exact composition ratio. The factors (n-h)/(n+r-1-h) decrease as h increases, so their product is bounded by (n/(n+r-1))^q. If J>L, some one of four coordinates is at least floor(L/4)+1. The union bound is valid without independence.

At n=floor(beta*r)-8, beta=log_2(3)-1, we have n<=beta*(r-1), since 8>=beta. Therefore the single-coordinate ratio is at most rho=beta/(1+beta). For delta>0 and L=ceil(4*(1+delta)*log(r)/abs(log(rho))), the claimed tail bound <=4*r^(-1-delta) follows. Cases n=0 and q>n have zero actual probability and are harmless. All logarithms here are explicitly natural.

Since |D_j H_j|<=1, truncating the exact mixture at min(n,L) has absolute error <=4*r^(-1-delta). This is a rigorous uniform prefix-excess truncation lemma. It is not the previously missing global offset compactness/tail lemma: the retained tail observables still have changing endpoint offset and frequency, and the conductor shift remains.

The initially proposed signed truncated-sum O(1/r) bound is logically equivalent to G=O(1/r) up to this already bounded remainder. Producer section 6 was subsequently replaced, before audit finalization, by the stronger triangle-weighted target sum w_j|D_j||H_j|=O(1/r). I reviewed that replacement. Its sufficiency follows from the triangle inequality plus the proved remainder. It retains cancellation inside each H, discards cancellation between distinct prefix contributions, and follows from a uniform O(1/r) estimate for every H in the window. Neither target nor uniform-H bound is proved here. Failure of the triangle-weighted bound would not refute the desired signed bound; no strict separation is proved for this specific family. No nonzero coefficient follows even from the upper bound; coefficient convergence and noncancellation across j remain separate OPEN tasks.

## Independent mechanical checks and failed checker version

Independent exact-integer/Fraction checks on r=5,...,8 and n=0,...,4 passed 1161 literal-row identities, 1161 corrected four-prefix rational identities, 20 prefix-weight normalizations, and 60 cutoff union/marginal inequalities. Their source and transcribed output are retained in this audit folder. Finite checks support the implementation; the proofs above establish the general identities and cutoff, not these tests alone. No floating-phase accuracy assertion is made.

The other checker's V1 source was read statically and its output parsed without rerunning it. Its phase_concatenation assertion incorrectly uses denominator 16*3^(r-3) for the tail, rather than 16*3^r. Because B_tail>0, this yields a strict nonzero rational error on every declared path. Its 2935 phase failures are therefore an implementation/formula error in that assertion, not counterexamples to the correct decomposition. V1 and its failure output must remain unchanged. The remaining seven check categories report 2935 passes each, i.e. 20545 passes and 2935 failures among 23480 assertions; the overall V1 batch must not be called PASS. Composition enumeration counts are separate checks, not included in that eight-category count.

The manager subsequently authorized a separately named V2. A no-index source diff confirms exactly two substitutions: the corrected tail denominator and the output filename. The V2 output reports 2935 paths, eight categories of 2935 checks, zero failures and unchanged input hashes. I parsed that output and checked the source diff without rerunning the checker. This is a corrected finite mechanical run, not retroactive conversion of V1 into a pass. The auditor's independently written row/four-prefix checks provide separate reproduction of the load-bearing algebra.

## Classification and stop boundary

Elementary exact reduction: independently reviewed and valid within this exploratory scope.
Logarithmic prefix-excess truncation: independently reviewed rigorous lemma, valid with the declared domain and cutoff.
Uniform complex cancellation / G=O(1/r): OPEN.
Nonzero 1/r coefficient or polynomial lower bound: OPEN.
Global offset compactness: OPEN.
Historical protocol repair / canonical theorem acceptance: NOT PERFORMED.

This is an exploratory independent-agent audit, not canonical named co-chair acceptance or a formal zero-trust stage package. Stop downstream at the lemma gate pending the manager's classification; canonical integration is outside this working-only batch. No old sealed task was rerun. No downstream asymptotic theorem may be claimed from this audit. Nothing in this exploratory audit proves Collatz.
