# A qualified extension to shorter block scales

This is a separate corollary of the weighted-window argument, rechecked by the principal and independently by audit_suffix_law. It does not assert failure at every scale tending to infinity.

Let d_R be an even integer, R=d_R n_R, d_R->infinity, and d_R<=C_0 log R. Use the same actual accessible G suffix K=floor(beta R)-15 and the origin-aligned grid of blocks of d_R/2 pairs. Fix a in (0,beta), eta>0, lambda>0, B>max(0,log_2(2/eta)), integer M>B, and A>1/I_beta(a). Set

k_R=ceil(A log R/d_R), m_R=k_R d_R.

Then A log R<=m_R<A log R+d_R=O(log R), so the exact m_R-coordinate comparison of the main proof is uniform. With G_(k_R) defined by all cyclic windows of k_R groups having mass at least a m_R,

P(G_(k_R)^c)
<=n_R exp[-m_R I_beta(a)+O(m_R^2/R)]
<=R exp[-A I_beta(a)log R+o(1)] ->0.

Moreover k_R/n_R=m_R/R->0. The first-window donor therefore lies strictly before the recipient n_R for large R. The donor and early-height arguments require only d_R->infinity; they do not require k_R to stay fixed. The map has at most k_R preimages, and its weight ratio is bounded below by gamma_(d_R), with gamma_(d_R)->gamma=[a/(1+a)]^M>0. Thus

E exp(-lambda N_C)>=exp(-lambda)gamma/(4k_R n_R)
=exp(-lambda)gamma d_R/(4k_R R).

Since k_R<=A log R/d_R+1<=(A+C_0)log R/d_R,

E exp(-lambda N_C)>=C_1 d_R^2/(R log R),

with C_1>0 independent of R. This contradicts every uniform C/R bound whenever d_R^2/log R->infinity along the divisible actual sequence.

For example, take L_R=floor((log R)^p), d_R=2L_R, with any fixed 1/2<p<1. A divisible sequence is

R_l=2l ceil(exp(l^(1/p))/(2l)).

Its logarithm is l^(1/p)+O(l exp(-l^(1/p))), so (log R_l)^p=l+o(1), from above, and hence L_(R_l)=l eventually. On this actual sequence the lower bound is of order (log R)^(2p-1)/R, which is larger than C/R for every fixed C.

This corollary supplies no contradiction at L_R=O(sqrt(log R)) and does not show that such scales work. Counts using interior pair opportunities or other grids remain separate questions. The complex suffix bound and Collatz are not refuted.
