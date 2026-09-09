# Exact residue-stratified join certificates

2026-09-08. Bounded refinement of the previously fixed42-row panel. No new asymptotic claim, paid call, or canonical-stage change.

## Exact cheap information before using covariance bounds

For a nonempty prefix of length j, total mass a and last valuation m_last,

    M_j mod3 =2^(-m_last) mod3 =(-1)^m_last.

Therefore no prefix endpoint lies in residue0 modulo3. For j>=2 its exact class totals are

    C_1(j,a)=sum_(even m=1..a-j+1) binom(a-m-1,j-2),
    C_2(j,a)=sum_(odd m=1..a-j+1) binom(a-m-1,j-2), C_0=0.

For j=1 the only word(a) has residue(-1)^a. These totals require no full prefix-residue enumeration. They follow directly from the endpoint recursion, so this is use of a known arithmetic identity rather than a novelty claim.

For an accepted suffix with lifted residue Z=n+3^k h, the demanded prefix is t=-2^R h mod3^j. If h=0 mod3 it is impossible to join any prefix. Equivalently successful joins require v_3(2^R n-B_v)=k, not a higher valuation. For j=1 the exact demanded high digit is h=-(-1)^A mod3; it depends only on the full mass. No uniformity of demands is inferred.

## A hierarchy of valid centered bounds

For a residue cell E containing m_E coordinates, write n_E=sum_E P, C_E=sum_E D, U_E=sum_E P^2, V_E=sum_E D^2. Define

    B(E)=n_E C_E/m_E
         +sqrt((U_E-n_E^2/m_E)(V_E-C_E^2/m_E)).

Then the exact join in E is <=B(E). Partitioning into classes modulo3^s gives a valid upper bound by summation.

The REAL bounds are monotone under refinement. To prove this, split each parent-centered histogram orthogonally into child-mean deviations and within-child residuals. The refined covariance allowance is the inner product of the child-mean deviations plus the sum of products of residual norms. Cauchy-Schwarz on the residual list and then on the pair(mean norm,residual norm) bounds it by the parent covariance allowance. At singleton cells both residual variances vanish and the join is exact.

Integer rounding is handled explicitly. A node's certified integer bound is the minimum of its own rounded centered bound and the sum of its children's certified bounds. Both are upper bounds; their minimum preserves validity and prevents separate child ceilings from increasing the stored certificate. All calculations use integer square roots.

This partitions EXACT histograms. It does not replace a trajectory representative at successive times, so the earlier ambient-bucket artificial-branching obstruction does not apply.

## Bounded computation

The same42 rows r4..10, critical offsets-1,0,1, b=.8,1.2 were used. Depths s=0,1,2 were compared. Full depth s=j was also checked only as an exactness calibration. The script records the prior data and imported numerator implementation hashes.

All exact formula, enclosure, refinement monotonicity and full-depth exactness checks passed. Depth1 improved41 of42 rows. Depth2 improved24 rows beyond depth1. Only15 rows have j>2 and therefore still hide residue information at depth2; do not label all depth2 recoveries as nontrivial compressed results.

| r,A,L | Prefix length j | Exact Q | Global centered | Mod3 stratified | Mod9 stratified |
|---|---:|---:|---:|---:|---:|
| 10,15,256 | 4 | 10 | 58 | 47 | 36 |
| 10,15,4096 | 2 | 140 | 191 | 162 | 140 |

The second row becomes exact because modulus9 is the FULL prefix modulus. This is calibration, not a new saving theorem. The first row retains9 residue classes each containing9 coordinates, so36 is a genuine non-singleton bound, but the needed moments were still obtained from fully enumerated histograms.

In the first row,56 accepted suffixes demand an impossible nonunit prefix residue. These are suffix words, NOT56 successful full words being removed. Zeroing those demands contributes to the improvement. The remaining36−10=26 units of bound slack are distributed across suffix masses R7..11 as4,8,6,7,1. This locates the finite uncertainty; it does not establish a universal dominant mass regime.

## Why more residue splitting alone is not a solution

For any fixed partition, choose within each allowed unit cell two disjoint subsets of size a (with2a<=cell size M). Put P=1 on the first and D=w on the second for an integer w>0. The true join is zero. Yet the centered bound in that cell is

    wa^2/M+sqrt((a-a^2/M)(w^2 a-w^2 a^2/M))=wa.

Thus exact class totals, integrality, unit support and fixed residue stratification alone can retain the entire demand count as an upper bound despite zero true overlap. This relaxed histogram countermodel is NOT asserted to be a Collatz histogram. It shows the specific arithmetic relationship must still do work.

Refining to all singleton residues only reconstructs the full exact computation. We will not count incremental finite-digit refinements as evidence of an asymptotic theorem or keep expanding this panel without a new structural claim.

## Independent review and next obligation

The analytic reviewer independently proved real-valued monotonicity, checked the rounding repair, and supplied the disjoint-support obstruction. The deterministic reviewer independently derived the mod3 class-count formulas and demanded-high-digit constraint. The principal checked those formulas against every enumerated prefix distribution in the panel.

The useful remaining object is within-class alignment between actual prefix fibers and actual accepted suffix demands. A new lemma should control this alignment across a family of scales, or bound the required class moments without full enumeration. Fixed-class statistics alone do not suffice. The count-to-orbit theorem remains conditional and no genuine Collatz trajectory class was newly excluded.
