# Adversarial target audit and two conditional propositions

2026-09-08. Principal synthesis after separate analytic and deterministic adversarial reviews. Exploratory proofs, not a newly completed frozen stage or a Collatz proof. No paid calls, large experiments, or canonical mutations.

## 1. Accepted objection: the previous target was stronger than necessary

The exact archived E0 interval report asks for

    Q_(r,A)(b) <= 2^((h_*+b-alpha+o(1))*r),
    Q = #{w in W_(r,A): 0 <= M_r(w) < 2^(br)},
    alpha=log_2(3), h_*=alpha log_2(alpha)-(alpha-1)log_2(alpha-1).

Here W is the set of positive compositions of A into r parts, so |W|=binom(A-1,r-1)=2^(h_*r+o(r)) uniformly on any fixed band |A-alpha*r|<=C. E0 does NOT require relative interval discrepancy o(1).

The preceding research_weighted_spectrum_20260908/RESULT.md is algebraically correct, but its persistent-bias example does not obstruct this target. Indeed its density is bounded above by O(1)/q. All its interval probabilities already obey the desired exponent. The earlier final response risked overemphasizing that example as an obstacle for the actual program. That strategic interpretation is corrected here.

Analytic reviewer also constructed a version supported exactly on 3-adic units. Multiplying the old density by (3/2)1_(3 does not divide x) keeps a bounded density relative to uniform units, adds the mandatory conductor-3 baseline, and retains O(r) primitive perturbation coefficients of order 1/r. This stronger example STILL satisfies the exponent target. Further polishing either countermodel is not currently useful.

## 2. Sparse-exception proposition, with explicit permitted loss

Let q=3^r, L=2^(br+o(r)), 0<b<alpha, and lambda>=0 with b+lambda<alpha. Let p be a probability on Z/qZ with characteristic function phi. Partition the nonzero spectrum into:

- B: an exceptional set of size <=2^(lambda*r+o(r));
- A: a remaining low-conductor block with conductor exponent t<=tau*r;
- H: all other frequencies.

Assume tau<=(b+lambda)/alpha and

    sup_(xi in H)|phi(xi)| <= 2^(-(alpha-b-lambda)*r+o(r)).

Then for any cyclic interval I of length L,

    P(I) <= 2^((b-alpha+lambda)*r+o(r)).

All errors and cardinality bounds must be uniform in the required mass parameters. A fixed b is being considered; this is not automatically a theorem for a whole b range.

Proof. Fourier completion is

    P(I)=L/q + (1/q) sum_(xi!=0) phi(xi) D_I(xi).

Since |phi|<=1 and |D_I|<=L, the B contribution is <=|B|L/q, which has the required exponent. For q odd, with d_q(xi)=min(xi,q-xi), the sine bound gives |D_I(xi)|<=q/(2d_q(xi)). Thus

    sum_(xi!=0)|D_I(xi)| <= q H_((q-1)/2) <= q(1+log q),

where log here is natural. The H contribution is at most (1+log q)sup_H|phi| and has the required exponent. For conductor 3^t the normalized locations are a/3^t, 3 does not divide a. Dropping that restriction gives a kernel sum <=3^t(1+log(3^t)). Summing over t<=tau*r and dividing by q bounds A by 2^((alpha*tau-alpha)*r+o(r)), also sufficient. Finally L/q has no larger exponent. This proves the proposition.

For lambda=0 every subexponential-size exceptional set is harmless at this scale. In particular the ENTIRE O(r) power-of-two ladder from the previous report needs no coefficient bound, no location restriction, and no cancellation theorem. Even the boundary complement rate delta=alpha-b suffices; the older strict inequality was a sufficient stronger choice.

What is unproved: the actual endpoint law has not been shown to satisfy the complementary bound or to have only subexponentially many exceptional coefficients. Merely declaring known ladders exceptional does not control other frequencies. This proposition removes an unnecessary universal-supremum requirement; it does not establish endpoint anti-concentration.

## 3. Deterministic count-to-orbit proposition

Let an ordinary positive odd-only Syracuse orbit satisfy

    s_k=floor(alpha*k)-A_k=kappa log_2(k)+O(1), kappa>1,
    A_k=sum_(j<k) v_2(3n_j+1).

If for some fixed 0<b<alpha the above endpoint counts satisfy

    Q_(r,A)(b) <= 2^((gamma+o(1))*r), gamma<b/kappa,

uniformly over every fixed critical mass band needed by the hypothetical orbit, then no such orbit exists.

Proof of state growth. Put D_k=A_k-alpha*k=-s_k-{alpha*k}. The exact CP17 identities are

    U_k=1+(1/(3n_0)) sum_(j<k) 2^(D_j),
    n_k=n_0*2^(-D_k)*U_k.

The sum converges since 2^(D_j)=Theta(j^(-kappa)) and kappa>1. Therefore U tends to a finite positive limit and n_k=Theta(k^kappa). In particular n_k tends to infinity. Determinism then implies injectivity: any repeated state would force eventual periodicity.

Choose epsilon>0 smaller than both b/kappa and b/kappa-gamma, and N=floor(2^((b/kappa-epsilon)*r)). For u in [N,2N], eventually u+r<=3N, so n_(u+r)<=C(3N)^kappa<2^(br)<3^r. Moreover

    A_(u+r)-A_u=alpha*r-kappa log_2((u+r)/u)+O(1)=alpha*r+O(1)

uniformly in u. Hence all these blocks belong to only O(1) critical mass classes.

For each block w its affine identity is

    2^(A(w)) n_(u+r)=3^r n_u+B_w.

Consequently n_(u+r) is congruent to M_r(w)=2^(-A(w))*B_w modulo 3^r, and since the actual endpoint is positive and smaller than 3^r it EQUALS the canonical residue. Two equal words would have equal endpoint residues and hence equal actual endpoints, contradicting injectivity. There are at least N distinct counted words. Summing the proposed count bound over the O(1) masses gives N<=2^((gamma+o(1))*r), contradicting the choice of epsilon.

This proof needs no random-orbit assumption and no repeated-factor spacing lemma. It is a conditional reconstruction using exact identities, not fulfillment of the missing count hypothesis and not a modification of the frozen Task-6 stage.

## 4. The actual quantitative research target

Combining composition entropy with the spectral proposition gives gamma=h_*+b-alpha+lambda. The sufficient strict gap is therefore

    lambda < alpha-h_*-b*(1-1/kappa).

Thus bounded factors, polynomial factors, and even some positive exponential loss can be permissible. Only the origin interval is needed for the deterministic bridge; the Fourier proposition happens to give all translates.

Numerical calibration only: alpha-h_*=0.0793186127748555. At kappa=1.053 and b=1.2 the permitted loss is lambda<0.0189197523759952. These decimals are not proof inputs and do not newly exclude the already-studied controller. They illustrate the exact symbolic inequality.

If b<alpha-h_* and lambda=0, the proposed Q exponent is negative, forcing the integer Q to be zero eventually. That is a strong emptiness theorem, not a mild distribution statement; no claim that it holds for such b is made.

## 5. Debate decisions and next bounded obligation

1. Analytic reviewer: no algebra error in prior note; unit support alone does not force equidistribution. Accepted, but this does not obstruct the actual rate goal.
2. Deterministic reviewer: why demand relative o(1)? The archived target allows subexponential factors. Accepted; research target changed.
3. Principal: could all sparse resonances be ignored at exponent scale? Analytic reviewer checked constants, low conductors, boundary rates and uniformity. Proposition 2 retained with explicit missing assumptions.
4. Principal: can the orbit bridge avoid repeated-factor machinery? Deterministic reviewer checked signs, growth, injectivity and endpoint equality. Proposition 3 retained as conditional only.

Next useful question: using the ACTUAL fixed-mass recurrence, can the coefficients exceeding an admissible exponential threshold be bounded in number, or can their total interval-weighted contribution be bounded directly? We have no such bound yet. A finite spectrum census could falsify proposed rates and suggest a set description, but cannot prove its asymptotic size. More fixed-ladder profile calculations do not address this obligation.

## Sources and review limits

Three exact archived source documents are preserved beside this note with SOURCE_PROVENANCE.json. The E0 target and recurrence and E1 sufficient rate are read directly, not inferred from a summary. CP17 carry identities were checked in research_project_review_20260908/CP17_PROOF_REFERENCE.md; audited critical-log scope in source_037.txt. Both agents independently reviewed the relevant new arguments. This is mathematical peer checking, not a machine-checked proof or a new independent certification of the entire historical project.
