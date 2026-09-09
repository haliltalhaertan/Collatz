# A finite-horizon control certificate for the actual endpoint event

2026-09-08. Elementary reformulation motivated by stochastic control and backward value functions. No novelty claim, no asymptotic estimate yet. It does not invoke an infinite-time ensemble-equivalence theorem.

Fix integers r>=1, A>=r, q=3^r, and 1<=L<=q. A word consists of r positive integers with total A. Define a prefix state (j,a,z), where j is the number of letters used, a their sum, and z=B_j modulo q, with B_0=0. Appending m gives

    (j,a,z) -> (j+1,a+m, (3z+2^a) mod q).

When k=r-j>=2 letters remain and R=A-a, the feasible next letters are 1<=m<=R-k+1. When k=1, the sole feasible letter is m=R. Only feasible states reachable from (0,0,0) need be considered.

Define terminal cost at (r,A,z) by

    g(z)=1 if (2^(-A)z mod q)<L, otherwise 0.

The exact number of successful continuations obeys

    V(r,A,z)=g(z),
    V(j,a,z)=sum_(feasible m) V(j+1,a+m,3z+2^a mod q).

Then V(0,0,0)=Q_(r,A)(L). Prefixes leading to a common state are NOT discarded as words: every parent sums over its letters, and reused values count continuations per prefix. Dynamic-programming memoization therefore preserves multiplicities.

Certificate proposition. Any nonnegative function F on these states satisfying F_terminal>=g and F_parent>=sum_m F_child gives Q<=F(0,0,0). Proof: backward induction on the number of remaining letters. For asymptotic usefulness one must exhibit a uniform family with root value <=2^((h_*+b-alpha+lambda+o(1))*r), not merely solve each finite graph.

Normalized form. With C(k,R)=binom(R-1,k-1), the next-letter bridge probability for k>=2 is

    P(m | k,R)=C(k-1,R-m)/C(k,R).

For k=1 it is deterministic. A nonnegative probability supersolution f with f_terminal>=g and f_parent>=sum_m P(m)f_child gives P(event)<=f(root). F=C(k,R)f gives the count formulation. These are the exact conditioned composition weights, not independent unconditioned geometric weights.

If h is the EXACT success-probability value function and h(parent)>0, then P^h(parent,child)=P(parent,child)h(child)/h(parent) defines the exact event-conditioned transition law. For an approximate positive h, that formula need not sum to one. It must be explicitly normalized, with likelihood corrections retained if used for estimation. A good sampler is not automatically a supersolution certificate.

## What makes this different from merely renaming the open problem?

The exact recurrence is already implicit in the archived endpoint identities; writing it does not improve the bound. Its purpose is to specify a checkable interface: candidate construction can be heuristic, but the terminal and local inequalities must be verified for ALL represented states. This permits a counterexample-guided refinement loop to reject a coarse candidate at the first failing state.

The unresolved issue is a compact arithmetic representation of F that preserves enough residue information. State space grows with q. A function depending only on (j,a), in a case Q>0, cannot improve on the total word count: the one successful terminal state forces its common terminal value >=1, and recursive inequalities along reachable prefixes force F(root)>=binom(A-1,r-1). Thus deleting z completely loses the desired event discrimination.

A sound abstraction may keep exact remaining mass and selected residue/interval information. If it takes a worst-case representative independently for different outgoing edges, it can introduce incompatible continuations and lose all gain. Any proposed refinement must improve a verified root upper bound or explain an actual inconsistent path; finite-state fit alone is insufficient.

## Small diagnostic, not asymptotic research evidence

check_count.py compares the exact recurrence with independent composition enumeration using the closed B formula, for r=2..7 and three feasible nearby critical masses, with L=floor(2^(0.8r)). It checks integer equality only. No new decay, sparsity, or Collatz theorem follows.

Motivating primary literature: Chetrite–Touchette, https://arxiv.org/abs/1405.5157 and https://arxiv.org/abs/1506.05291. Their long-time driven-process results have additional hypotheses not verified here. The finite backward induction above is proved directly.
