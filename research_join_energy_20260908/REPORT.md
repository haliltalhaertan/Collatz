# Join energy: the correct marginal, centered bounds, and a conditional rate obstruction

2026-09-08. Exploratory exact derivations and the same42 finite rows from the prior exact-join panel. No paid calls, larger enumeration, canonical stage changes, or new Collatz exclusion.

## 1. What the required collision energy actually measures

Keep the exact split notation r=j+k, total mass A=a+R, q=3^r, m=3^j, L<=3^k. For suffix v let

    Z_v=2^(-R)B_v mod3^r = n_v+3^k h_v,
    0<=n_v<3^k, 0<=h_v<m.

Accept v if n_v<L. Its required prefix residue is t_v=-2^R h_v modm. Let c_(h,n) count accepted suffixes with this high/low pair. Because multiplication by -2^R is a permutation modulo m,

    E_D=sum_h (sum_(n<L) c_(h,n))^2.

Ordinary accepted-suffix endpoint collision energy is instead

    E_low=sum_(n<L) (sum_h c_(h,n))^2.

These are different marginals of the same joint arithmetic distribution. Equal low endpoints need not mean equal required prefix residues, and equal demands need not mean equal low endpoints. Prior low-endpoint collision data therefore cannot simply replace E_D.

There ARE safe general comparisons. With E_full=sum_(h,n)c_(h,n)^2,

    E_full<=E_D<=L*E_full,
    E_full<=E_low<=m*E_full,
    E_D<=L*E_low, E_low<=m*E_D.

They follow by Cauchy-Schwarz within rows or columns. One may also bound E_D by L times the unrestricted ordinary suffix energy. But L grows exponentially in the selected regime, so such a factor cannot be silently absorbed as a constant. No assertion that there is 'no mathematical relation' between the energies is intended.

The deterministic reviewer supplied explicit witnesses, subsequently checked by check_witnesses.py. At k=2,j=1,R=9,L=3, suffixes(2,7),(5,4),(8,1) have respective (low endpoint, demand) pairs (2,2),(1,2),(2,1). Thus both nonimplications occur within one accepted set. Other complete two-part enumerations give (E_low,E_D)=(9,25) and(12,8), so neither universal ordering holds. These are algebraic witnesses outside the critical asymptotic regime, not evidence for its rates; details are in WITNESSES.json.

## 2. Center the join before applying Cauchy-Schwarz

For each fixed R let P(t) be prefix multiplicity, D(t) required-prefix multiplicity, n=sumP and C=sumD. The exact join is

    Q_R=nC/m + sum_t (P(t)-n/m)(D(t)-C/m).

Consequently

    Q_R<=nC/m+sqrt((E_P-n^2/m)*(E_D-C^2/m)).

Unlike the raw sqrt(E_P E_D) bound, this explicitly retains the uniform overlap and bounds only its deviation. The centered bound is no larger than the raw bound, by the two-dimensional Cauchy-Schwarz inequality applied to mean and fluctuation norms.

The means are taken over all m residues as an algebraic identity, not an assumption that the actual distribution is uniform or that unit-support bias vanishes. Centered energies may still be large. No sign is assumed for the covariance.

For exact integer arithmetic set X=mE_P-n^2 and Y=mE_D-C^2, both nonnegative. A safe integer ceiling is

    ceil((nC+ceil(sqrt(XY)))/m).

check_centered.py uses integer square roots, verifies the bound separately for every mass term against the recorded exact join, then sums the ceilings.

## 3. Finite results

All42 rows from research_exact_join_20260908/RESULT.json passed.32 rows improved strictly over the raw-energy upper bound. No parameter search or new word enumeration was required; the same stored histogram energies suffice. Source bytes are SHA-256 bound in RESULT.json.

| r,A,L | Exact Q | Raw collision bound | Centered bound |
|---|---:|---:|---:|
| 10,15,256 | 10 | 64 | 58 |
| 10,15,4096 | 140 | 337 | 191 |

These are valid finite upper bounds based on fully computed histograms, not an asymptotic theorem or a demonstrated faster large-r method. The first example's improvement is modest; the second is stronger. Neither proves a uniform exponent.

## 4. A conditional floor for raw Cauchy-Schwarz

This paragraph assumes, rather than proves, the following critical-split scaling. Put h=h_*, beta=k/r, b=alpha*beta+o(1), and suppose for one critical mass split

    n=2^(h(1-beta)r+o(r)), C=2^(h beta r+o(r)),
    m=2^(alpha(1-beta)r+o(r)).

The accepted-demand exponent for C is an ADDITIONAL hypothesis. The fact that L/3^k is bounded below does not prove it for the actual law.

Integrality gives E_P>=n and E_D>=max(C,C^2/m). Thus the raw upper-bound expression itself has exponent at least

    f=[h(1-beta)+max(h beta,2h beta-alpha(1-beta))]/2.

The ideal E0 exponent is e=h-alpha(1-beta). If h beta>=alpha(1-beta), the excess f-e is (alpha-h)(1-beta)/2>0. In the other case f=h/2 and f-e=alpha(1-beta)-h/2>0 throughout that case.

Therefore raw Cauchy-Schwarz cannot attain the IDEAL lossless exponent under these premises, even with optimally low raw energies. This is a limitation of the proof expression, not a lower bound on Q.

Crucial qualification: the actual count-to-orbit route permits a positive loss lambda when

    lambda<alpha-h-b(1-1/kappa).

At b=1.2,kappa=1.053, the conditional raw floor loss is about .00963262, while the permitted loss is about .01891975. Hence the floor does NOT rule out meeting that weaker target. Actual sufficient energy upper bounds still have to be proved. We do not close the raw-energy route on the basis of this ideal-target obstruction.

## 5. What a useful centered-energy theorem would need

For the full mass range R=k,...,A-j, one needs to control both the mean term nC/m and the excess term. If aggregate mean and excess bounds give exponent gamma<b/kappa, the previously established conditional count-to-orbit proposition applies to the stated critical-log class.

In the illustrative critical split above, the mean already has exponent e under the extra C assumption. If E_P is near its diagonal scale n, controlling the centered demand energy more strongly than its raw background could remove the raw-CS mismatch. Neither that near-diagonal prefix estimate nor the required centered-demand estimate has been proved uniformly here. Noncritical split masses must also be bounded; global critical mass does not place every split in a fixed critical band.

This is a quantitative description of the missing theorem, not its solution. Another possible route is to bound the covariance directly without separately making either marginal flat. A negative-correlation claim is unnecessary and unsupported by the finite examples.

## Review and decision

The analytic reviewer independently derived the conditional raw-energy obstruction and the centered alternative. The principal checked the obstruction against the weaker allowed-loss budget rather than rejecting the entire route. The deterministic reviewer was tasked with concrete collision witnesses and the distinct marginals. The42-row centered check was performed by the principal using prior exact data; it is not an independent re-enumeration of every word in this turn.

The deterministic review also emphasized that the centered covariance is an exact re-expression of the original join, with a corresponding cross-spectrum identity. Naming it does not prove cancellation or introduce an independent constraint. That objection is accepted: only a new quantitative bound on this specific arithmetic pairing would close the current gap.

Continue only with a claim about the accepted lifted high/low joint law, its centered demand energy, or the actual covariance. Do not substitute the old low-endpoint energy or assume independent gains. These results sharpen the target and finite certificate; no actual Collatz orbit class has been newly excluded.
