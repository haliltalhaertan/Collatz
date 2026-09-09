# Multiscale literature triage and next structural question

2026-09-08. Exploratory brainstorming, primary-source reading, and elementary deductions. No new orbit exclusion, paid model request, or numerical panel expansion. Earlier geometric tilting is explicitly recognized as existing work.

## What the literature contributes, and what it does not

1. Hochman, On self-similar sets with overlaps and inverse theorems for entropy: https://arxiv.org/abs/1212.1873 . Inverse convolution entropy methods organize failure of smoothing into structure across scales. This motivates asking what persistent prefix/demand alignment forces; it does not establish that our exact join satisfies a convolution-growth hypothesis.
2. Shmerkin, On Furstenberg's intersection conjecture, self-similar measures, and the L^q norms of convolutions: https://arxiv.org/abs/1609.07802 . Author's detailed exposition: https://arxiv.org/html/1907.07121 , Sections 1.1–1.3 and 2. Contracting self-similar measures with exponential separation have explicit L^q dimensions. The separate inverse convolution theorem does not require self-similarity. Therefore lack of contraction blocks the direct self-similar corollary, NOT every inverse-convolution approach. A single large value of a cross-correlation is not by itself a verified hypothesis for that inverse theorem.
3. Eberhard–Varju, Mixing time of the Chung–Diaconis–Graham random process: https://arxiv.org/abs/2003.08117 . Fixed multiplier and iid additive steps; sharp mixing result for almost all odd moduli. Our modulus sequence 3^r cannot be extracted from an almost-all-moduli statement; our increments also retain accumulated valuation dependence. A useful analogy, not an imported bound.
4. Breuillard–Varju, Cut-off phenomenon for the ax+b Markov chain over a finite field: https://arxiv.org/abs/1909.09053 . Finite fields, most parameters, and conditional sharp results do not supply a theorem on the fixed prime-power sequence 3^r.
5. Tao, Almost all orbits of the Collatz map attain almost bounded values: https://arxiv.org/abs/1909.03562 . High-frequency estimates for a skew walk on 3-adic cyclic groups and renewal geometry are the closest structural precedent. Its logarithmic-density conclusion is not a statement about every exceptional orbit. The previously documented critical-tilt drift obstruction remains open.

## Why the critical law matters: reconstruction, not a new method

Let alpha=log_2(3), and choose iid positive geometric valuations with

    Pr_p(a=m)=p(1-p)^(m-1), m>=1.

Every length-r word of total A has probability p^r(1-p)^(A-r). Hence conditioning on total A gives exactly the uniform positive-composition law for EVERY p in (0,1).

At p=1/alpha the mean is alpha. For A=alpha*r+O(1), Stirling's formula in

    Pr_p(sum a_i=A)=binom(A-1,r-1)p^r(1-p)^(A-r)

gives Theta(r^(-1/2)). Consequently any event E obeys

    Pr(E | sum a_i=A) <= O(sqrt(r)) Pr_p(E).

E may itself use the fixed external parameter A. This is only a transfer inequality; its unconditioned right side still needs a bound. Under p=1/2 the critical total instead costs 2^(-(alpha-h*)r+o(r)), h*=alpha log_2 alpha-(alpha-1)log_2(alpha-1).

The same critical geometric-law idea already appears in research_literature_20260908/LITERATURE_TRIAGE.md. It must not be presented as a new discovery.

For the real affine branch T_a(x)=(3x+1)/2^a, the critical tilted law has E log_2 T_a'=alpha-Ea=0. A conditioned critical block has derivative 3^r/2^A=2^O(1); there is no uniform exponential contraction in r. Also T_1 expands. Thus the standard contracting-real-IFS corollary cannot simply be applied. The maps are contracting in the 3-adic metric, but the ordinary interval M<L does not become a single small 3-adic ball. Resolving that metric mismatch remains necessary.

## A precise next question: signed contributions across scales

For each suffix mass R, retain the ACTUAL prefix histogram P and accepted demand histogram D on G=Z/(3^j). No independent-uniform surrogate is introduced. Equip G with uniform probability. Let F_s be the partition into residues modulo 3^s; define P_s=E[P|F_s], D_s=E[D|F_s], and increments Delta P_s=P_s-P_(s-1), similarly for D.

By orthogonality of martingale differences, exactly

    sum_t P(t)D(t) = n*C/m + m*sum_(s=1..j) E[Delta P_s Delta D_s],

where m=3^j, n=sum P and C=sum D. Proof: expand P=P_0+sum Delta P_s and D similarly; all different-level cross terms vanish by conditional expectation. This is standard finite martingale algebra, not a new theorem.

The last finite panel bounded residual correlations by products of norms. The next structural question is whether actual arithmetic forces a bound on the SIGNED aggregate above across many scales and all relevant mass splits. Independence, negativity, or cancellation cannot be assumed. Controlling each scale by Cauchy alone recreates the old obstruction.

A useful inverse statement would infer explicit arithmetic concentration from an excessively large join, and then show that such concentration cannot persist for the actual paired distributions. It must specify a quantitative exponent; saying 'structure exists' is insufficient. The currently sufficient example permits loss lambda<0.01891975237599524 at b=1.2 and kappa=1.053, subject to the existing uniform count-to-orbit assumptions. This number is a target budget, not an achieved bound.

## Decision

Prioritize exact alignment and its multiscale inverse formulation; inspect the inverse L^q theorem's premises before claiming a transfer. Keep critical tilting as an exact representation already in the project. Do not expand residue enumeration merely to lower another finite certificate. Reject a proposed shortcut if it needs unproved iid demands, typical-modulus substitution, contraction at zero drift, or independence between mass and endpoint.
