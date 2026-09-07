# SUMMARY.md — A3 analytic attack (exploratory; pending manager acceptance gate)

1. [PROVED here] Exact real coordinate: with delta_s := (j+s-1+Y_{s-1}) - alpha(s+4),
   e_{3^{s+4}}(2^{u_s}) = exp(2 pi i 2^{delta_s}) identically, so
   H_{m,k}(j) = Psi(m; j-5alpha, j+k-beta*m-5alpha), Psi a mean-zero bridge functional, and
   G_{r,n_r} = Psi(r; -4-alpha, -12-alpha-theta_r). Verified mechanically (4.7e-16; the four-prefix
   row split is bit-exact, error 0.0).
2. [PROVED here] CIRCULARITY: YES. H and G are the SAME two-parameter family with the SAME right
   endpoint -13.585-theta_r, same tilt, same critical line. No fixed conductor (it is 3^r, exactly
   equivalent to a 4alpha shift of the left endpoint), no fixed offset, no easier line. The j-drift
   the derivation places in the endpoint offset in fact sits entirely in the LEFT endpoint
   a_j = j - 5alpha. j = 0 in uniform-H is already an E6-N2-strength statement.
3. [PROVED here] The centring tilt is rho = beta/alpha, i.e. p* = 1-rho = 1/log_2 3 — the same rho as
   the audited cutoff constant. Under it the conditioning is central ([NUM] sqrt(r) P_rho ->
   1/(sigma sqrt(2pi)) = 0.41432), not off-central; that candidate obstruction dies.
4. [PROVED here] The r^{1/2} loss, exactly. Conditioning contributes prefactor
   P_rho(Y_m=k)^{-1} ~ 2.41 sqrt(m) on the one extra dual variable phi. Even a perfect
   uniform-in-phi unconditioned bound sup_phi|Phi_m| <= A/m gives only O(m^{-1/2}); naive Plancherel
   over phi gives O(m^{1/4}), worse than trivial. A joint (phi, 3-adic) local limit is required —
   precisely the [OPEN] E7R-B4 object.
5. [PROVED here] B3-CT does not apply to this window (it lives at left endpoint -> -infinity; the
   prefix window moves the left endpoint UP). Reusable stop rule: any variant that pushes the left
   endpoint DOWN is refuted in advance by B3-CT.
6. [NUM] UNIFORM-H: supported, C ~ 50. r*max_{j in window}|H_j| flat in [43, 49.3], slope -1.01; the
   maximiser is j = 0 for every tested r in [60,600]; the feared (log r)/r growth is refuted
   (r*max|H|/log r falls 12.8 -> 7.6). Not proved. Hardest step isolated: equidistribution off the
   no-wrap barrier event, |E[prod ; E^c]| = o(1/m)  [OPEN].
7. [PLAUSIBLE, heuristic] The 1/r scale is a barrier probability: a mean-zero bridge with O(1)
   endpoints stays below the wrap threshold with probability ~ 2|a||b|/(sigma^2 m).
8. [PROVED here] D_j exact for j<=40; premise corrected: |D_j| > 0.3 only for j <= 6, and < 0.032 for
   12 <= j <= 40. So (S) needs uniform H control only on j <~ 10; [NUM] j<=5 carries >99.6% of S_r.
9. [NUM] TRIANGLE vs SIGNED: S_r/|G| -> 1.1818, monotone, r-stable. Discarding between-class
   cancellation costs about 18%, nothing more.
10. Verdict on (S): likely TRUE [PLAUSIBLE, heuristic], but NOT a genuine step. It implies E6-N2 and
    is numerically within a factor 1.19 of it; no argument can prove it without proving E6-N2. The
    derivation's claim that the signed truncated bound merely restates the original problem is
    [PROVED here] CORRECT — and the same holds for the triangle version up to that bounded factor.
    Adopting (S) as the next target risks re-running E6-N2 under a new name.
11. [NUM] r|G| and r|H_0| do NOT converge; they are almost-periodic in theta_r = {beta r}
    (correlations 0.828 and 0.9882). Any "r|G| -> c" target is ill-posed; the object is a profile.
12. ONE next lemma (NEXT_LEMMA.md): PREFIX-WINDOW EXTREMALITY (PWE) —
    |H_{r-4,n_r-j}(j)| <= C |H_{r-4,n_r}(0)| for all 0 <= j <= L_r. Contains no rate; provable in
    principle by bridge comparison/coupling without arithmetic equidistribution; falsified by an
    unbounded R(r) = max_j |H_j|/|H_0|; [NUM] R(r) = 1.000000 exactly for all r in [60,600]. It would
    collapse the O(log r) drifting window to ONE family, retiring the audit's "Global offset
    compactness [OPEN]" item for this route, and reduce E6-N2 to |H_{r-4,n_r}(0)| = O(1/r). Violates
    no prohibited_inferences (checked item by item).
13. Nothing here proves Collatz. E6-N2 [OPEN], (S) [OPEN], (U) [OPEN], PWE [OPEN]. No tracked file
    modified, no commit, no push, no canonical state change.
