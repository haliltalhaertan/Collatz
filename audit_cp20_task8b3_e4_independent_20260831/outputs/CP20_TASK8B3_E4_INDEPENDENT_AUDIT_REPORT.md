# CP20 TASK 8B3 — E4 INDEPENDENT ZERO-TRUST AUDIT REPORT

## Mandatory verdict

**[AUDIT PASS WITH REPAIR — CRITICAL-WALK ROUTE DECISION]**

The load-bearing route-decision theorem survives. The exact line conjugacy,
qualified infinite unrolling, deterministic zero drift, pure-exponential
complex-operator spectral obstruction, and nonzero moving-boundary asymptotic
are correct. The repairs below are documentary or scope repairs; none changes a
load-bearing equality or theorem.

Nothing audited here proves Collatz, compactness, convergence, or a nonzero
fixed-target profile. E5 was not started and no computation was extended beyond
the declared depth.

## 1. Provenance gate and execution record

### Supplied archives

- `[PROVED]` `CP20_TASK8B3_E4_AUDIT_PACKAGE.zip`: SHA-256
  `a99185ffc4e9daa527a3ee54b59df8ced02bed65490421ce3f9a028119f8c408`.
- `[PROVED]` `CP20_TASK8B3_E4_COMPLETE_PACKAGE.zip`: SHA-256
  `95190d5cbdb633ad049720897b28c73898be229832549153c1fe9ee03b9c4cb1`.
- `[PROVED]` The audit manifest has exactly 28 payload entries and all 28
  independently recomputed hashes match. The manifest itself has SHA-256
  `09632ceba2c4d71934c298cfb79824d80d6534604268a3de2add534489c212fe`.
- `[PROVED]` The full sibling E3 folder was available. All 23 entries in its
  frozen `SHA256SUMS.txt` match; that manifest has SHA-256
  `75d73c9409eff45cd013579bf358e513838da6e354d4c443aee8510103a1e13a`,
  matching the E4 audit package's frozen copy.

The archives were extracted into a fresh audit directory. Supplied artifacts
were not edited. The supplied verifier was run only in an isolated copy beside
a copied, hash-verified full E3 directory.

### Runtime and dependencies

- Supplied verifier: bundled CPython 3.12.13, exit code 0, observed wall time
  9.1515051 seconds, final line `ALL E4 VERIFIER ASSERTIONS: PASS`.
- Independent checker: bundled CPython 3.12.13, standard library only, exit
  code 0, internal elapsed time 1.3274818999925628 seconds.
- Independent checker SHA-256:
  `4000a26ca22ac57ccadfc6b6628521762fae6c73c76a74c4c6f29eed31fca687`.
- The ordinary `python`/`py` WindowsApps launchers were unavailable. This was
  the only missing execution dependency; the bundled runtime resolved it
  without changing any frozen script.

### Predeclaration chronology

`[UNSUPPORTED]` The package states that the design was frozen before output
inspection (`CP20_TASK8B3_E4_PREDECLARATION.md:3-6`), and source/data conform to
that design, but the supplied ZIP entry timestamps are normalized to 1980 and
there is no external pre-output timestamp, commit, or signed seal. Therefore the
temporal ordering itself cannot be independently verified from this package.
The repair is to describe it as a package assertion unless an external seal is
supplied. This affects provenance of the `[NUM]` diagnostics, not the exact
route-decision theorem.

## 2. Frozen definitions and finite unrolling

### Conventions

`[PROVED]` The frozen E3 derivation defines

\[
\alpha=\log_2 3,\quad \beta=\alpha-1,\quad
a=\beta/\alpha,\quad b=1/\alpha,
\]

with `d` in the signed domain `Z`, `theta` in the half-open interval `[0,1)`,
and

\[
T\theta=\theta-\beta+\varepsilon(\theta),\qquad
\varepsilon(\theta)=1_{[0,\beta)}(\theta).
\]

Thus `epsilon(0)=1`, `epsilon(beta)=0`, `T(beta)=0`. E3 explicitly records the
half-open convention at `beta` (`CP20_TASK8B3_E3_LIMIT_EQUATION_DERIVATION.md:94-110`).
The exact eventual real-quotient phase is

\[
P_{d,C}(\theta)=\exp(2\pi i\,2^{d-1-C-\theta}),
\]

while negative finite exponents retain the modular-inverse definition
(`CP20_TASK8B3_E3_LIMIT_EQUATION_DERIVATION.md:29-59`).

### Finite and infinite formulas

`[PROVED]` Repeatedly substitute only the same-phase term
`a K_{d-1}(theta)`. Induction gives, for every finite `J >= 0`,

\[
K_d(\theta)=\sum_{j=0}^{J}ba^jP_{d-j,C}(\theta)
K_{d-j+\varepsilon(\theta),C}(T\theta)
+a^{J+1}K_{d-J-1,C}(\theta).
\]

No branch is rotated during this unrolling. This agrees with
`CP20_TASK8B3_E4_EXACT_UNROLLING_AND_CRITICAL_WALK.md:13-26`.

For fixed `(d,theta)`, put `m=d-J-1`. The remainder is exactly

\[
a^{J+1}K_{d-J-1}(\theta)=a^d a^{-m}K_m(\theta).
\]

Therefore its vanishing is equivalent, not merely implied, by
`a^{-m}K_m(theta) -> 0` as integer `m -> -infinity`.

- Pointwise in phase: the displayed limit is necessary and sufficient for each
  fixed `theta`.
- In cylinder `L-infinity`: necessary and sufficient is
  `ess sup_theta |a^{-m}K_m(theta)| -> 0`.
- Uniform for chosen pointwise representatives: necessary and sufficient is
  `sup_theta |a^{-m}K_m(theta)| -> 0`.

`[REPAIRABLE]` The E4 source says only “the corresponding uniform limit”
(`CP20_TASK8B3_E4_EXACT_UNROLLING_AND_CRITICAL_WALK.md:28-40`). It should state
the essential-supremum and representative-uniform versions separately as
above. E3 proved neither a limit profile nor any of these tail conditions.
E4 correctly labels the infinite expansion as conditional and does not use it
as an inherited finite-depth fact (`ibid.:48-59`).

`[REPAIRABLE]` The first literally invalid displayed equality is in
`CP20_TASK8B3_E4_FALSIFICATION_REPORT.md:19-22`: a `+` is missing immediately
before `a^{J+1}K_{d-J-1}`. The primary derivation contains the correct plus
sign, so this is a transcription repair, not a theorem failure.

## 3. Cylinder-to-line conjugacy

`[PROVED]` For `x=d-theta`, each cylinder strip `{d} x [0,1)` maps to
`(d-1,d]`. These intervals partition the real line. The inverse is

\[
d=\lceil x\rceil,\qquad \theta=d-x,
\]

with the unique integer convention `(d,theta)=(x,0)` when `x` is an integer.
The absolute Jacobian on each strip is one, so counting measure times Lebesgue
measure maps to Lebesgue measure. Consequently all `L^p` norms, including
essential-supremum norms, correspond exactly.

Direct substitution gives

\[
(d-1)-\theta=x-1,
\]

and, using `T theta=theta-beta+epsilon(theta)`,

\[
(d+\varepsilon(\theta))-T\theta=x+\beta.
\]

Also `P_{d,C}(theta)=p_C(x)=exp(2 pi i 2^{x-1-C})`. Thus the full measurable
cylinder equation is exactly

\[
\kappa(x)=a\kappa(x-1)+bp_C(x)\kappa(x+\beta).
\]

The dense branch seams are exactly coordinate seams for measurable functions.
No regularity is needed for the conjugacy. If continuity is requested, the
integer matching condition is the equality of the `theta -> 0+` value in strip
`d` with the `theta -> 1-` limit in strip `d+1`; equivalently `kappa` must be
continuous at that integer. This refines
`CP20_TASK8B3_E4_EXACT_UNROLLING_AND_CRITICAL_WALK.md:61-128` without changing it.

The independent endpoint tests included exact `theta=0`, exact `theta=beta`,
and both adjacent floating-point neighbors; the maximum shift error was zero
and the maximum 256-step telescoping error was `2.842170943040401e-14`.

## 4. Centered critical walk

`[PROVED]` Since `1-a=b`, `q_j=ba^j` is a probability mass on nonnegative
integers. Its probability-generating function gives

\[
EJ=a/b=\beta,\qquad Var(J)=a/b^2=\alpha\beta,
\]

and all polynomial moments exist. For `Y=beta-J`,

\[
EY=0,\qquad Var(Y)=\alpha\beta.
\]

Its exponential moment is finite exactly when

\[
a e^{-s}<1\quad\Longleftrightarrow\quad s>\log a,
\]

and equals `b exp(beta s)/(1-a exp(-s))`.

`[PROVED]` The deterministic identity follows by telescoping
`T^(k+1)theta-T^k theta=-beta+epsilon(T^k theta)`:

\[
\sum_{k=0}^{n-1}\varepsilon(T^k\theta)
=n\beta+T^n\theta-\theta.
\]

No iid model for the rotation symbols is used. Independent copies of `J` are
legitimate only when iterating the positive kernel whose coefficients are the
product measure of the `q_j`; they are not a probabilistic replacement for the
deterministic branch itinerary. The orientation `Y=beta-J` is correct.

## 5. Exponential norm and spectral radius

Let `L_C` be the two-shift complex operator and `U_C` its qualified unrolling.

### Pure exponential weighted `L-infinity`

`[PROVED]` For `||f||_{infinity,s}=ess sup_x e^{-sx}|f(x)|`, direct translation
gives the upper norm bounds

\[
m_{LE}(s)=ae^{-s}+be^{\beta s}
\]

for every real `s`, and

\[
m_U(s)=\frac{be^{\beta s}}{1-ae^{-s}}
\]

exactly for `s>log a`. The latter condition is both the geometric-series
moment domain and the boundedness domain for the pure exponential allowance.

These are also the complex-operator spectral radii, not merely positive
majorant bounds. Take `f_s(x)=e^{sx}`, whose weighted norm is one. If
`g(x)/e^{sx}` is bounded and tends to `c` as `x -> -infinity`, then

\[
\frac{L_Cg(x)}{e^{sx}}\to c\,m_{LE}(s),
\]

because `p_C(x)->1`. Induction gives
`L_C^n f_s(x)/e^{sx}->m_LE(s)^n` for every fixed `n`. Hence the operator-norm
upper bound is attained in the far-left essential supremum, despite path
collisions and complex phases.

For `U_C`, the normalized summands are dominated by the summable sequence
`ba^j exp(s(beta-j))`. Dominated convergence first exchanges the far-left
limit with the geometric sum; the same invariant left-limit argument then
iterates it finitely. Therefore `||U_C^n||=m_U(s)^n`. This supplies the missing
fixed-iterate and domination details requested by the audit prompt.

For `m_LE`, strict convexity and `m_LE'(0)=-a+b beta=0` give the unique global
minimum one at zero. For `m_U`, the logarithm is the cumulant generating
function of nonconstant `Y`, hence is strictly convex on `s>log a`, has
derivative zero at zero, and has unique minimum zero; thus `m_U` has unique
minimum one. Every admissible nonzero pure exponential tilt has spectral
radius strictly above one.

### Scope of the obstruction

`[REPAIRABLE]` The theorem should be stated with these exact limits:

- Pure exponential allowances: proved exactly as above.
- A far-left asymptotically exponential weight inherits the same lower bound
  when its fixed-translation ratios converge to the exponential ratios. For
  `U_C`, a uniform summable domination over the geometric jump index is also
  required.
- For `exp(lambda |x-x0|)`, the far-left slope is `s=-lambda`. `L_C` has the
  strict lower bound `m_LE(-lambda)>1`. `U_C` is bounded only when
  `lambda < -log a`; in that domain its lower bound is `m_U(-lambda)>1`, and
  outside it the unrolled operator is unbounded.
- A one-sided patch with a flat far-left tail retains spectral value at least
  one; a patch with an admissible exponential far-left tail retains the
  corresponding multiplier obstruction.
- No conclusion is established for every conceivable asymmetric, irregular,
  or oscillatory weight.

This is consistent with the intended qualifications at
`CP20_TASK8B3_E4_WEIGHTED_SPACE_DECISION.md:42-79`, but the asymptotically
exponential ratio and domination hypotheses should be written explicitly.

## 6. Polynomial, `L1`, BV, analytic, and truncation claims

- `[PROVED]` Polynomial weighted `L-infinity`: translations and the geometric
  kernel are bounded. The jump-index tail is
  `O(a^J J^p)`. It is only a kernel-jump truncation, not a spatial offset
  truncation uniform in time (`CP20_TASK8B3_E4_WEIGHTED_SPACE_DECISION.md:81-117`).
- `[PROVED]` The moving boundary makes every uniform allowance of degree
  `p<1` impossible. Degree one is merely admissible against this single test;
  no uniform degree-one bound is proved.
- `[PROVED]` Weighted `L1` operator bounds are available under the corresponding
  translation moments, but the constant nonnegative-offset base row is not in
  unweighted `L1`. No inherited finite-depth `L1` state or compactness follows.
- `[REPAIRABLE]` `L_C` preserves `BV_loc`, since it uses finitely many
  translations and smooth local multiplication. Bare `BV_loc` alone does not
  make the infinite `U_C` sum defined or bounded: its terms sample arbitrarily
  far left and require a global growth/moment condition. Therefore
  `CP20_TASK8B3_E4_WEIGHTED_SPACE_DECISION.md:142-162` must restrict “local BV
  is closed” to `L_C` or add such a tail condition. The stated failure of
  ordinary global BV without a right-tail weight is otherwise correct.
- `[PROVED]` `p_C(z)` is entire but is unbounded on ordinary two-sided
  horizontal strips as `Re z -> +infinity`; this rules out the named standard
  global strip-sup setting, not every tailored analytic weight.
- `[NUM]` Boundary sensitivity was reproduced. At `r=8000`, non-oracle complex
  target errors are `5.5179` through `9.4392`; oracle errors are
  `7.59e-15` and `2.20e-14`. Oracle injection is only an implementation
  control, exactly as predeclared. No canonical remote boundary or spatial
  truncation theorem follows.

`[OPEN]` No candidate space audited here supplies all four required pieces:
operator closure, an inherited uniform finite-depth bound, compactness/tightness,
and a canonical spatial boundary condition.

## 7. Moving-boundary nontriviality

`[PROVED]` At `n=0`, the exact recurrence has only the unit phase factor, so
`|G_{r,0,C}|=1`. With `d=-m_r` and `theta_r={beta r}`,

\[
x=d-\theta_r=-\beta r,\qquad |H|=r.
\]

The modular-inverse issue is finite. For `r >= C+1`, the exponent
`r-1-C` is nonnegative and the new phase angle is exactly

\[
2\pi\frac{2^{r-1-C}}{3^r}
=2\pi 2^{-1-C}(2/3)^r.
\]

All earlier modular-inverse factors form one finite unit prefactor. The
absolute sum of the eventual angles converges, so the phase product converges
to a nonzero unit `L_C`. Consequently

\[
H_{r,-m_r,C}/x\to-L_C/\beta.
\]

This proves only a receding-boundary asymptotic. It rules out uniform
polynomial degree `p<1`; it does not prove a degree-one uniform bound, and it
does not imply nontriviality at fixed `(-8,4)`. The first missing quantifier is
a uniform-in-`r` transfer estimate across distance of order `r`, as E4 itself
states (`CP20_TASK8B3_E4_NONTRIVIALITY_ATTEMPTS.md:24-33`).

## 8. Numerical and implementation audit

`[NUM]` The supplied tables contain exactly 970 profile rows and 40 boundary
rows, with only `C in {4,7}`, integer `d in [-64,32]`, and saved depths
`{1000,2000,4000,6000,8000}`. The engine source rejects `rmax != 8000`
(`CP20_TASK8B3_E4_ENGINE.cs:58-61`). No supplied E4 data or log exceeds
`r=8000`; this cannot establish that no undisclosed computation ever occurred.

An independent standard-library implementation recomputed six full complex
checkpoints at `r=1000`, `C in {4,7}`, and `d in {-64,-8,32}`. Maximum complex
error was `2.05788922583097e-14`; the error at the target `d=-8` was below
`8.5e-16` for both `C` values. All 40 boundary error columns were recomputed
from their complex components with zero decimal difference. Detailed real and
imaginary errors are in the JSON checks file.

Profile fits, phase widths, positive-side decay, and boundary sensitivity
remain `[NUM]`. The verifier's green result is an implementation/provenance
control, not a proof of the analytical claims.

## 9. Claim disposition

| Claim | Status | Disposition |
|---|---|---|
| Audit ZIP, 28 payload hashes | `[PROVED]` | Exact match |
| Full sibling E3, 23 hashes and verifier | `[PROVED]` | Complete numerical reproduction possible |
| Predeclaration predates inspection | `[UNSUPPORTED]` | Needs external timestamp/seal; downgrade wording |
| Finite same-phase unrolling | `[PROVED]` | Correct; repair one missing plus sign in falsification report |
| Infinite unrolling | `[PROVED]` | Only under the stated pointwise/norm tail condition |
| Cylinder-to-line conjugacy | `[PROVED]` | Exact measurable and norm correspondence |
| Deterministic zero drift | `[PROVED]` | No iid branch assumption |
| Pure-exponential complex spectral obstruction | `[PROVED]` | Exact on the stated domains |
| Patched/asymptotically exponential scope | `[REPAIRABLE]` | Add ratio and domination hypotheses; no universal-weight claim |
| Polynomial jump tail | `[PROVED]` | Not a spatial truncation theorem |
| Bare `BV_loc` closure for `U_C` | `[REPAIRABLE]` | Restrict to `L_C` or add a global tail condition |
| Nonzero moving boundary | `[PROVED]` | Modular-inverse prefix finite; tail product nonzero |
| Compactness | `[OPEN]` | Not proved |
| Nonzero fixed-target profile | `[OPEN]` | Not proved |
| Fits, phase widths, decay, sensitivity | `[NUM]` | Reproduced within declared scope |

## 10. Mandatory questions

1. **Does the exact line conjugacy survive?** Yes. `[PROVED]`
2. **Does the qualified infinite unrolling survive?** Yes, pointwise or in the
   specified essential-supremum/uniform norm only when the corresponding
   `a^{-m}K_m -> 0` tail condition holds. `[PROVED]`
3. **Does deterministic zero drift survive without iid assumptions?** Yes.
   `[PROVED]`
4. **Does the complex-operator spectral-radius obstruction survive, and on
   exactly which weights?** Yes for pure exponential weighted `L-infinity`:
   all real `s` for `L_C`, and `s>log a` for `U_C`. It extends to patched or
   far-left asymptotically exponential weights only under the ratio and, for
   `U_C`, summable-domination hypotheses stated above. It does not cover every
   asymmetric or oscillatory weight. `[PROVED]` with a `[REPAIRABLE]` scope
   sentence.
5. **Does the moving-boundary nonzero asymptotic survive?** Yes. `[PROVED]`
6. **Was compactness proved?** No. `[OPEN]`
7. **Was a nonzero fixed-target profile proved?** No. `[OPEN]`
8. **May the research manager open the proposed degree-one complex-renewal/
   local-limit task?** **Yes**, because this is a fully specified pass-with-
   repair and the repairs do not alter a load-bearing theorem. The new task
   must remain sealed, must not treat `[NUM]` observations as theorem input,
   and must prove an explicit uniform transfer from the receding boundary to
   the fixed target rather than assume it.
