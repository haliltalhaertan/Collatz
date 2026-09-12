# Principal review — 2026-09-12

Accepted scope: exact all-length tail-shell identity and real-array alignment reduction; exact finite counterexamples to the literal W <= W_flat shortcut. No new asymptotic estimate, orbit exclusion or novelty claim.

I checked the sibling lift, binomial multiplicity, endpoint conventions, unnormalized Parseval factors, zero denominators, and odd translation dilation in PROPOSAL.md. The finest-shell half-mass identity uses total Fourier energy including the constant coefficient; the different centered denominator is explicitly retained. The all-length conjugate-pair estimate A <= 2^(s-2) for s>=2 follows by pairing a with -a; A=1 at s=1,2. That estimate is exponential in precision and is not sufficient by itself.

For an independent implementation check I used integer cyclic autocorrelations rather than the proposal's conditional variance projections. At modulus n=2^s and H=n/2, let C_P(d)=sum_u P(u)P(u+d), and C_F likewise for the aggregated tail. The primitive Ramanujan sum is H at 0, -H at H, and 0 elsewhere. Hence the exact conductor variance is

    V_(k,s) = H/q^2 * sum_d C_P(d)[C_F(d)-C_F(d+H)].

This yields the same 64 stratum/conductor variances and R,D values on the four fixed panels. All sharper real-pair bounds passed, as did equality with flat pairing at s<=2. Four genuine strata exceed flat pairing; the largest observed ratio is 3692/1941. The output is INDEPENDENT_CHECK.json; the source is independent_alignment_check.py. No floating-point DFT was used. These checks do not extend the finite panel scope.

The next question is control of the weighted alignment mean together with W_flat in a growing critical family. Pointwise alignment control is sufficient but not necessary. The failure of the literal constant-one upper bound neither rules out a larger constant nor subexponential control.
