# Sharp limitation of variance-to-origin transfer

Let B be the number of translated blocks, G_j their nonnegative integer target counts, mu=(sum G_j)/B, and V=(1/B)sum(G_j-mu)^2. Write C2=V/mu^2 for the normalized population variance.

## Sharp deterministic inequality

Because sum_(j>0)(G_j-mu)=-(G_0-mu), Cauchy gives

    sum_(j>0)(G_j-mu)^2 >= (G_0-mu)^2/(B-1).

Consequently

    (G_0/mu-1)^2 <= (B-1)*C2,
    G_0/mu <= 1+sqrt((B-1)*C2).

Equality holds over real-valued histograms when all non-origin blocks have equal count. Thus replacing B by a constant is not possible without further structural information. This is a worst-case guarantee from mean and variance, not a necessary description of actual Collatz counts.

## Exponent threshold for the present application

At b1.2, B=2^(tau*r+O(1)) with tau=alpha-b=0.384962500721156.... If C2<=2^(-v*r+o(r)), this argument gives origin enrichment exponent at most

    max(0,(tau-v)/2).

To certify the allowed loss lambda=0.01891975237599524 via this worst-case argument requires

    v >= tau-2lambda = 0.3471229959691655...

with the usual strict margins when needed by the orbit bridge. Merely C2->0, or merely a positive power decay, does not suffice. Chebyshev says few translated blocks are bad; the origin is a fixed block and can be among them. Forcing the number of bad blocks below one yields the same exponent threshold.

## Integer countermodel with exact mean and block capacities

Use the actual parameter shapes

    A=floor(alpha*r), m=ceil(1.2*r), t=A-m,
    B=2^t, T=binom(A-1,r-1), mu=T/B.

Define a SYNTHETIC histogram by

    G_0=floor(mu)*2^floor(r/16),

and distribute T-G_0 as evenly as possible among the remaining B-1 blocks: values q and q+1, with q and the remainder determined by Euclidean division.

It has exactly the correct full-period total T, integer nonnegative entries, and, eventually, each entry is at most the actual number2^(m-1) of odd starts per block. The latter follows because mu has exponent b-(alpha-h*), and1/16<alpha-h*; the spike exponent stays below b. Nonnegativity of the remainder follows from1/16<tau.

Its origin loss tends to1/16=0.0625, above the allowed0.01891975. Nevertheless

    C2 = 2^(-(tau-1/8)*r+o(r)),
    tau-1/8 =0.259962500721156... >0.

Thus normalized variance decays exponentially despite an exponentially excessive origin spike. This is NOT a claim that any such histogram is realizable by Collatz. It demonstrates that exact mean, integrality, block capacity, and a substantial but insufficient variance rate do not by themselves establish the needed origin bound.

For the balanced integer construction, writing Delta=G_0-mu gives

    V=Delta^2/(B-1)+rounding_error,
    0<=rounding_error<=1/4.

The rounding term is exponentially negligible relative to mu^2 in the displayed regime.

## Verification

attack_countermodel.py verifies exact totals, nonnegativity, block capacities, and the sharp variance inequality using rational arithmetic at r16,32,64,128,256. These are synthetic histograms; no Collatz enumeration was performed. All checks pass. No paid calls or orbit exclusion.
