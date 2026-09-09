# Reconnecting the Fourier work to its original interval question

8 September 2026. Elementary synthesis from exact Fourier completion and the already recorded frequency normal form. Not a new general anti-concentration theorem or a claim of novelty. No numerical experiment.

## Exact interval budget

Let p be any probability mass function on Z/qZ and define

    phi(xi)=sum_x p(x) exp(2 pi i xi x/q),
    D_I(xi)=sum_{x in I} exp(-2 pi i xi x/q).

For an interval I of L consecutive distinct residues, 1<=L<=q, Fourier inversion gives

    P(X in I) = L/q + (1/q) sum_{xi != 0} phi(xi) D_I(xi).

For any subset B of nonzero frequencies its contribution has absolute value at most

    (1/q) sum_{xi in B} |phi(xi)| |D_I(xi)|.

Relative to the uniform interval mass L/q, its bound is

    (1/L) sum_{xi in B} |phi(xi)| |D_I(xi)|.

The elementary geometric-series identity implies

    |D_I(xi)| <= min(L, 1/|sin(pi xi/q)|).

In particular, large characteristic-function values do not alone determine their importance for an interval. Their locations and total weighted multiplicity matter.

## The specific structured project frequency

Use the accepted normal form in the canonical literature-transfer result:

    alpha=log_2(3), q=3^r,
    T_r=floor(alpha*r)-8,
    xi_r=2^(T_r-4) mod 3^r.

For sufficiently large r the power is a positive integer smaller than q, so no modular reduction is needed. Put theta_r={alpha*r}. Then exactly

    xi_r/q = 2^(-12-theta_r),
    2^-13 < xi_r/q <= 2^-12.

Since sin(pi x)>=2x for 0<=x<=1/2,

    |D_I(xi_r)| <= 4096.

Thus even the trivial bound |phi(xi_r)|<=1 implies that this one Fourier summand has absolute contribution <=4096/q and relative contribution <=4096/L. Including its conjugate frequency gives <=8192/L. This is a bound on these summands only, not on the full interval error. For intervals L growing exponentially in r, these individual relative contributions decay exponentially without any theorem about a 1/r complex profile.

For a fixed nonnegative shift C in place of4, the analogous bound is2^(8+C)/L per frequency at sufficiently large r. Uniformity in growing C is NOT asserted. Frequencies approaching zero, many related frequencies, or the rest of the spectrum can exhaust the budget.

## Strategic interpretation

Archived E1 (source_043.txt) selected a uniform high-conductor exponential majorant as a sufficient route to small-interval control. E2 (source_044.txt) pivoted to a polynomial lower-bound countertheorem for structured resonances, to disprove that majorant. E3–E6 (sources045–048) pursued the profile and its nonzero coefficient. Recent marked-Laplace upper bounds address an intermediate component of that program.

The calculation above shows why a countertheorem against a supremum estimate does not itself defeat the original interval problem. Conversely, it may be unnecessary to finish a difficult nonzero-profile theorem merely to control these individual structured summands in interval completion.

A more directly relevant research target would state explicit sets B_r and prove both:

1. a total interval-weighted estimate on B_r;
2. a complementary estimate on all remaining required frequencies, uniform in the declared mass and interval ranges.

The required error scale must be taken from the particular frozen interval/conjunction theorem; this note does not assume relative o(1) is necessary or sufficient for every downstream goal. It also does not identify B_r or prove the complementary estimate. Known fixed low-conductor obstructions must remain explicitly accounted for.

This is a research-design proposal, not an execution or authorization of a closed canonical stage. It neither resolves ordinary integer realization nor proves Collatz.
