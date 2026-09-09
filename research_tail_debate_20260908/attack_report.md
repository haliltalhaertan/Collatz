# Attack on a pointwise tail-oddness cap

## Critical finite witnesses

Let H be the shortcut map, m=floor(1.2r), A=floor(r log2 3), t=A-m and K=r-t. Exhaustive odd-start checks below2^m give actual all-odd tails with exactly K prefix odd states for every r8..16 in this bounded panel.

In particular r12,A19,m14,t5,K7 has x231, H^14(x)=31, and all five following states are odd. There are48 such starts at this row. At r16,A25,m19,t6,K10, x2805 gives H^19(x)=319, whose six following states are odd;774 starts satisfy that row's critical event. Thus even the exposed-bits threshold K can be attained by genuine critical trajectories. A universal requirement that the remaining tail contain at least one zero is false. These finite witnesses do not disprove a positive-density-zero assertion holding only asymptotically, nor any useful counting bound.

## All-length noncritical construction

For any positive odd t, let y=2^t-1, so y is odd and not divisible by3. Let k be the least integer with3^k>y. Starting from y, repeatedly construct an odd predecessor x=(2^a y-1)/3, choosing a in{1,2,3,4} so x is integral and not divisible by3.

This is always possible: choose the parity of a to ensure integrality, then compare a and a+2. If the first resulting predecessor vanishes mod3, the second does not, because multiplication by4 changes 2^a*y from1mod9 to4mod9. Positivity and oddness are automatic.

After k inverse steps, write m=sum a_i, so k<=m<=4k. The resulting start satisfies

    0<x<2^m*y/3^k<2^m,
    H^m(x)=2^t-1.

Consequently the following t shortcut parity bits are all odd. Since k=t/log2(3)+O(1), t>=log2(3)*m/4-O(1): the all-odd tail can have length proportional to the number of exposed bits even under the small-start condition x<2^m.

This construction is NOT uniformly in the required critical mass band: A=m+t and r=k+t need not obey A=alpha*r+O(1). It defeats a tail cap based on the small-start condition alone; it does not settle the critical conditional distribution. The one-start-per-t constructed subset is sparse, but no upper bound for ALL such starts follows.

## Remaining arithmetic obligation

For a fixed prefix with k odd states, write 2^m*y=3^k*x+C. An all-odd tail of length t is exactly

    3^k*x+C+2^m = 0 mod2^(m+t).

The actual x<2^m is the canonical representative of the prefix cylinder. Testing the displayed congruence asks about its unexposed high bits, equivalently about extension to the full parity cylinder. A height estimate for y neither establishes uniformity of this test nor bounds its conditional frequency by2^-t. Treating it as an independent factor would assume the desired missing distribution.

Scripts attack_tail.py and attack_family.py use exact integer arithmetic. Their JSON outputs record the finite panel and t1..39 odd construction checks. No asymptotic statistical claim, paid call, or new orbit exclusion.
