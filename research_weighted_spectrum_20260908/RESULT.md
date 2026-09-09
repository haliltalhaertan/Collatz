# Weighted spectral budget: a proved extension and an obstruction

2026-09-08. Exploratory mathematical deductions, outside frozen stages. No paid model calls or canonical changes. These are elementary results, with no priority claim.

Subsequent adversarial target audit: the algebra below remains valid, but its relative-o(1) target is stronger than the archived E0 exponent-only requirement. The countermodel satisfies that original requirement. The entire O(r) ladder can be absorbed at exponent scale without coefficient decay. See ../research_spectral_target_audit_20260908/RESULT.md for the corrected research priority, sparse-exception proposition, and explicit conditional count-to-orbit bridge.

## 1. A growing structured window can be discarded

Let q=3^r, alpha=log_2(3), T=floor(alpha*r)-8, and let I be any cyclic interval of L distinct residues. For a probability law p define phi(xi)=sum_x p(x)e_q(xi*x). Relative to L/q, the absolute contribution of a set B is at most sum_B |phi(xi)||D_I(xi)|/L.

For integers 0<=C<=Cmax<=T, put xi_C=2^(T-C). These are distinct, smaller than q/2, and xi_C/q=2^(-8-C-theta), theta={alpha*r}. The sine bound gives |D_I(xi_C)|<=2^(8+C). Consequently the ENTIRE set of these frequencies and their negatives contributes at most

    2^(9) (2^(Cmax+1)-1)/L < 2^(Cmax+10)/L.

This uses only |phi|<=1, uniformly over all probability laws and interval locations. If L=floor(2^(b*r)), 0<b<alpha, and Cmax<= (b-epsilon)*r for fixed 0<epsilon<b, this tends to zero exponentially. Unlike a fixed-C observation, this removes a linearly growing window. It removes only these exact frequencies, not neighborhoods, multiplicative translates, or the complementary spectrum.

The transition is C approximately log_2(L): farther down this ladder, frequencies lie within order q/L of zero and the interval kernel no longer supplies smallness. This is a sufficient cutoff, not a sharp necessity statement for the actual law.

## 2. Sparse primitive coefficients of size 1/r do NOT suffice

Fix any 0<b<alpha. Set L=floor(2^(b*r)) and, for sufficiently large r, J=floor(log_2(q/(6L))), M=J+1. Define a probability law on Z/qZ by

    p_r(x) = (1/q) [1 + (1/(2r)) sum_(j=0)^J cos(2*pi*2^j*x/q)].

Proof of validity: each frequency 2^j is a nonzero integer at most q/(6L), so each cosine has zero sum over the group. Also M/(2r)<1 eventually, since M/r -> alpha-b<2; hence p_r(x)>0. Frequencies and their negatives are all distinct.

Its only nonzero nonconstant Fourier coefficients occur at +/-2^j and equal 1/(4r). Every such frequency has full conductor 3^r, since 3 does not divide 2^j. There are only 2M=O(r) coefficients. Thus every nonconstant coefficient tends to zero, and all low-conductor coefficients vanish exactly.

Nevertheless, for I={0,...,L-1}, every phase 2*pi*2^j*x/q is between 0 and pi/3. Each cosine is at least 1/2. Therefore

    P_r(I)/(L/q) - 1 >= M/(4r),
    liminf [P_r(I)/(L/q)-1] >= (alpha-b)/4 > 0.

This is a rigorous counterexample to the GENERIC implication that O(r) primitive resonances, each O(1/r), guarantee relative o(1) interval discrepancy. It also shows that conjugate pairing can reinforce a bias. It does not refute any weaker upper-bound-only target, nor any claim using additional structure of the actual endpoint law.

This law is deliberately relaxed: it is not asserted to be a Collatz endpoint law, a valuation bridge, an ordinary orbit, or a Collatz counterexample. In particular it does not impose the exact endpoint support or recursion. Its function is to show that sparsity, primitivity, and coefficient decay alone cannot replace those missing properties.

## 3. Revised research obligation

The growing structured window in section 1 needs no profile theorem for its interval contribution. The potentially consequential part is the long-wavelength end of that family and the remaining spectrum.

For any specified family B, a sufficient phase-free target is

    sum_(xi in B) |phi(xi)| min(1, q/(2L*d_q(xi))) = o(1),
    d_q(xi)=min(xi,q-xi), 1<=xi<q.

The inequality follows from |D_I|/L<=min(1,q/(2L*d_q)). Alternatively one can control the exact complex sum, but phase cancellation must be proved uniformly in the required interval locations; the example above shows it cannot be assumed.

For the ladder's low-frequency portion, uniform o(1/r) coefficients would suffice when it has O(r) members. Uniform O(1/r) alone would not. A smaller summed bound could suffice without any uniform estimate. Neither is established for the actual endpoint law here.

The archived E2 recursion controls fixed structured parameters; it does not automatically give bounds when C grows proportionally to r. Extending fixed-C asymptotics to this range would be a new uniformity theorem. Before pursuing it, the exact downstream Task-6 requirement must be recovered: relative o(1), a fixed-factor upper bound, and an exponential-rate upper bound are different goals. This note proves no transfer from a distributional estimate to a single ordinary orbit.

## Verification

The proofs above use Fourier orthogonality, a finite geometric sum, and sin(pi*u)>=2u for 0<=u<=1/2. The accompanying small numerical sanity check verifies normalization, positivity, Fourier support, and the claimed interval lower bound at r=8, b=0.8. Floating point verification supports implementation only; the displayed proofs establish the claims.

Prior project sources: research_project_review_20260908/WEIGHTED_SPECTRAL_BUDGET.md and source_043.txt (E1), source_044.txt (E2). Existing E7/E4 failure and tail-condition boundaries remain unchanged.
