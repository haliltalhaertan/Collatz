# Exact split join: preserving the missing relation

2026-09-08. Exploratory exact arithmetic and adversarial review. No new asymptotic bound, no paid calls, and no canonical stage changes.

## Purpose

Fixed interval/residue abstractions lose compatibility between successive representatives. This turn instead keeps complete prefix and suffix residue histograms and joins them by an exact affine condition. It diagnoses the mathematical information needed for a useful bound. It is not presented as a compact algorithm or a new independent restriction.

## Exact join theorem

Split w=uv, with lengths j,k and masses a,R, where j+k=r and a+R=A. The affine identity is

    B_w=3^k B_u+2^a B_v.

Writing M_j(u)=2^(-a)B_u mod3^j gives

    2^R M_r(w)=B_v+3^k M_j(u) mod3^r.

Assume L<=3^k. Define m_v=2^(-R)B_v mod3^k in its canonical range. A successful full endpoint n<L, if it exists, must equal m_v. Thus reject the suffix if m_v>=L. Otherwise its REQUIRED prefix residue is

    t_v=((2^R m_v-B_v)/3^k) mod3^j.

The quotient is an integer. Define P_(j,a)(t) as the number of prefix words of mass a with endpoint residue t, and D_(k,R)(t) as the number of accepted suffixes requiring residue t. Then exactly

    Q_(r,A)(L)=sum_(R=k)^(A-j) sum_t P_(j,A-R)(t) D_(k,R)(t).

This retains word multiplicities and all compatibility. There are no independent marginal losses being multiplied.

An equivalent computational form uses the suffix LIFTED to the full modulus:

    Z_v=2^(-R)B_v mod3^r=m_v+3^k h_v,
    t_v=-2^R h_v mod3^j.

Thus the small endpoint condition reads the low k ternary digits, while the high j digits specify the prefix demand. This is the relevant high/low relation; separately knowing the two marginal distributions is not enough.

## Safe bounds and their missing input

With C_R=sum_t D_R(t), one has

    Q<=sum_R max_t(P_R(t))*C_R,

and by Cauchy-Schwarz

    Q<=sum_R sqrt(E_P(R)*E_D(R)),
    E_P=sum_t P_R(t)^2, E_D=sum_t D_R(t)^2.

The demand energy E_D is NOT the collision energy of ordinary suffix endpoints modulo3^k. It concerns the lifted required-prefix residues after accepting the low-endpoint event. Substituting the ordinary marginal energy is unjustified.

Although prefix and suffix words are independent conditional on their masses in the original uniform-composition model, their residue histograms need not be uniform. The join is a correlation. For m=3^j, its exact centered decomposition is

    sum_t P(t)D(t) = (sum P)(sum D)/m
                         +sum_t (P(t)-meanP)(D(t)-meanD).

Neither sign of the centered term is assumed. A negative-correlation theorem is not necessary: the permitted exponent budget can tolerate bounded or subexponential bias. But large alignment cannot simply be discarded.

All split masses R=k,...,A-j occur. A globally critical A does not force every R to be critical for k; existing fixed-critical-band estimates cannot silently be inserted for every term.

## Bounded exact check

Use the previous panel's42 rows with r=4..10, offsets d=-1,0,1 and b=.8,1.2. Choose k as the smallest integer with3^k>=L and j=r-k. No split search or tuning is performed. Enumerate exact numerator distributions for each part and compare the join to unsplit endpoint enumeration and the previously verified Q.

All42 comparisons pass. Both safe bounds exceed or equal Q. Cauchy-Schwarz is evaluated with an integer ceiling for each mass term. The lifted-high-digit target identity is checked for every accepted suffix. RESULT.json records all mass-specific energies and counts.

| Parameters | Total N | Exact Q | Max-prefix-fiber bound | Collision bound | Uniform-target baseline |
|---|---:|---:|---:|---:|---:|
| r10,A15,L256,j4,k6 | 2002 | 10 | 157 | 64 | 647/81 |
| r10,A15,L4096,j2,k8 | 2002 | 140 | 805 | 337 | 424/3 |

The older fixed hybrid model gave1827 for both rows. The exact split bound is tighter because it retains real compatibility, but it uses fully computed histograms. This comparison is about information and tightness, NOT equal computational resources or a demonstrated asymptotic speedup.

The centered deviations in these two rows are respectively163/81>0 and-4/3<0. Thus even these small cases do not support a blanket sign assumption. Their finite size says nothing decisive about an exponential asymptotic correlation rate.

## An optimistic shortcut already fails the rate test

If one discards suffix acceptance and bounds the maximum prefix fiber by1, the critical mass split alone contributes about2^(h_*k). With k~br/alpha this has exponent h_*b/alpha. The ideal target exponent is h_*+b-alpha, smaller by

    (alpha-h_*)*(1-b/alpha)>0.

Therefore even perfect prefix injectivity cannot make THAT crude upper-bound expression reach the ideal target. For the count-to-orbit inequality gamma<b/kappa, its optimistic exponent can help only when kappa<alpha/h_*, approximately1.05268. It does not cover the calibrated kappa1.053 regime. This is a limitation of the bound, not a lower bound on actual Q.

## Prior-work check and review

The analytic reviewer independently derived the exact join, lifted target, and collision bound. The deterministic reviewer checked the E0 counterexample report and CP8/CP12 summaries: near-injective small prefix distributions and the danger of counting the same compatibility condition twice were already present. This construction does not claim to create a second independent constraint.

The decisive open question is now explicit: bound the required-prefix target histogram jointly with the prefix fibers at the necessary exponent, over the full mass split. Merely repeating old endpoint collision estimates will not suffice. The exact join is a useful interface for that question, but the theorem needed to control it remains unproved.

Keep this as a bounded diagnostic. Do not enlarge enumeration or assert a new convergence consequence from the64 vs1827 comparison. A next mathematical claim must address the lifted target distribution or the centered join term, with its rate and mass uniformity stated in advance.
