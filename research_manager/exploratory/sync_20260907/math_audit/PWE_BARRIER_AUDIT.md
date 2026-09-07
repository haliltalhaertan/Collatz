# Zero-trust bounded audit: PWE and barrier review

Date: 2026-09-07  
Audited object: `math/PWE_BARRIER_INDEPENDENT_REVIEW.md` and its declared
plan, script, and result JSON.  
Scope: static inspection, independent algebra, and a representative
reproduction restricted to producer-predeclared cases. No historical sealed
run, depth extension, Git/Drive operation, or canonical edit was performed.

## Verdict

**`PASS WITH REQUIRED WORDING/SCOPE REPAIRS`.**

The endpoint constants, exact bridge representation, exact barrier
decomposition, telescoping obstruction, and the numerical counterexamples to
literal modulus monotonicity are correct. The finite result JSON is internally
consistent and the representative values reproduced independently.

Two claims require repair before this review is used as a research-direction
authority:

1. PWE itself does **not** logically require a nonzero denominator or a
   positive lower envelope for `H_0`. Written as
   `|H_j| <= C |H_0|`, it remains a defined statement when `H_0=0`; it then
   requires the relevant `H_j` also to vanish. Nonvanishing is needed to form
   the diagnostic ratio `R(r)` and may be needed by a ratio-based proof
   strategy, but it is not an extra hypothesis needed to state or use PWE for
   an upper bound.
2. The proposed fixed-barrier KFB theorem does not cover the full PWE window.
   For `a_j=j-5 alpha` and `h=0`, the killed event is empty at time zero for
   every `j>=8`, while `L_r` grows like `log r`. Thus a KFB theorem uniform on
   a fixed compact starting set can address the fixed-start `G`/`H_0` family,
   but not PWE for all `0<=j<=L_r`. A PWE route needs an additional reduction
   to bounded `j`, a moving barrier, or a different comparison theorem.

No theorem or countertheorem to eventual PWE was found. No audit stop rule
fires. The correct final classification remains exploratory.

## 1. Independent endpoint derivation

Put `alpha=log_2(3)`, `beta=alpha-1`, `m=r-4`, and let
`Y_t=y_1+...+y_t`. The row `s=t+1` in `H` is

```text
exp(2 pi i * 2^(j+s-1+Y_(s-1)) / 3^(s+4)).
```

Its base-two exponent after absorbing the denominator is

```text
j + Y_t + t - alpha(t+5)
= j + Y_t - beta*t - 5*alpha.
```

Therefore the row-phase state is exactly

```text
Delta_t = j + Y_t - beta*t - 5*alpha,
Delta_0 = j-5*alpha.
```

Translating by `beta` gives the pre-increment convention

```text
X_t = Delta_t+beta = j+Y_t-beta*t-(4*alpha+1),
X_0 = j-4*alpha-1,
q_beta(X_t)=exp(2 pi i 2^(X_t-beta)).
```

Since `beta=alpha-1`, the two advertised constants differ exactly by
`beta`; they are consistent only when paired with their corresponding row
function.

For `k=floor(beta*r)-8-j` and `m=r-4`, writing
`theta_r={beta*r}` gives

```text
Delta_m = j+k-beta*m-5*alpha
        = -13-beta-theta_r
        = -12-alpha-theta_r,
X_m     = -13-theta_r.
```

For the full `G` bridge the row-phase start is `-4-alpha` and the endpoint is
the same `-12-alpha-theta_r`. These constants in the reviewed document are
correct.

Conditioning independent geometric increments on `Y_m=k` produces the uniform
law on weak compositions because every composition receives the same factor
`(1-rho)^m rho^k`. This validates use of the tilted conditional bridge.

## 2. PWE and monotonicity adjudication

The producer's literal heuristic that increasing `j` "can only increase
cancellation" predicts non-increase of `|H_j|`. It is false. The independent
reproduction found

```text
r=30: |H_6|=0.5190060 < |H_7|=0.5992852
                    < |H_8|=0.7159153 < |H_9|=1,
r=60: |H_12|=0.00928705 < |H_13|=0.00996632.
```

These are sufficient counterexamples to literal monotonicity and to any proof
that obtains that monotonicity merely from a pathwise endpoint order. Complex
expectations do not have the positive order structure used in ordinary
stochastic domination.

They do **not** refute eventual bounded-ratio PWE. In particular, the small-r
cases reaching `k=0` can be excluded by PWE's eventual threshold. The reviewed
classification `[OPEN / NUMERICALLY SUPPORTED]` is therefore correct.

The review's denominator discussion needs the following precise replacement:

- The ratio diagnostic `R(r)=max_j |H_j|/|H_0|` is undefined when `H_0=0`
  and becomes unstable near small denominators.
- PWE itself should be stated without division as `|H_j|<=C|H_0|`. It is
  meaningful at a zero and imposes simultaneous vanishing there.
- PWE plus the upper bound `|H_0|=O(1/r)` yields the desired upper comparison
  without any lower bound on `|H_0|`.
- A proof based on dividing by `H_0`, compactness of a normalized profile, or
  numerical ratios would require nonvanishing control. That is a limitation of
  those proof mechanisms, not a logical hidden assumption of PWE.

Accordingly, the document's observation about possible small-denominator
difficulty is useful, but "PWE silently imports part of the nontriviality
problem" is too strong as written.

## 3. Barrier decomposition and telescoping obstruction

With `M_m=max_(0<=t<m) Delta_t`, splitting the conditional expectation by the
disjoint events `{M_m<=h}` and `{M_m>h}` gives exactly

```text
Psi = K_m^h + R_m^h.
```

This is an identity. A ballot theorem controls the conditional probability
`Q_m^h`; it does not by itself control the complex killed expectation `K_m^h`.

On `{M_m<=-T}` with `T>0`,

```text
|product_t q(Delta_t)-1|
 <= sum_t |q(Delta_t)-1|
 <= 2*pi*m*2^(-T).
```

Thus `|K_m^(-T)-Q_m^(-T)|<=2*pi*m*2^(-T)`. For this deterministic error to be
`o(1/m)`, one needs `2^(-T)=o(m^-2)`, for example
`T>=(2+epsilon)log_2(m)`. But the start `Delta_0=a` is fixed. Eventually
`-T<a`, and because time zero is included in `M_m`, the event
`{M_m<=-T}` is empty. The reviewed obstruction is correct and decisive
against that particular uniform-closeness argument.

It is not a countertheorem to a barrier/Feynman--Kac mechanism; it only closes
the proposed reduction of the killed functional to an ordinary ballot
probability through a uniformly tiny phase error.

## 4. KFB and crossing gaps

A killed Feynman--Kac local-limit/renewal theorem is a legitimate missing
ingredient for the fixed-start `G` or `H_0` bridge. Its statement needs three
repairs/clarifications:

1. **Admissible lattice family.** Conditional bridges exist only when
   `b-a+beta*m` is a nonnegative integer. Uniformity in a displayed continuum
   `theta in [0,1)` must mean uniformity over the admissible triangular-array
   endpoints generated by the actual integers, not conditioning on arbitrary
   continuum endpoints.
2. **Uniform coefficient control.** To infer `O(1/m)` from
   `K=m^-1(kappa+o(1))`, `kappa` and the remainder must be uniformly bounded on
   the stated endpoint family. Nonzero or positive lower control is needed
   only for a nonzero-profile/lower-bound conclusion.
3. **PWE coverage.** With `h=0`, `a_j=j-5alpha>0` for `j>=8`; hence
   `{M_m<=0}` is empty immediately for that part of the logarithmically growing
   PWE window. "Uniform for `a` in the required compact starting set" cannot
   represent all PWE starts. The theorem should either be explicitly scoped
   to fixed-start `G`/`H_0`, or supplemented by a separate argument for the
   moving-start window.

Even a repaired KFB theorem controls only `K`. The sufficient estimate
`R_m^h=o(1/m)` is a second load-bearing arithmetic gap. A joint asymptotic with
cancellation between `K` and `R` could replace this separate estimate, so the
crossing bound is sufficient, not logically necessary. The review already
acknowledges that alternative and is sound on this point.

Therefore `(U6)` is not presently the only missing statement: the inside term
requires genuine killed Feynman--Kac analysis as well. Calling KFB "the first"
missing lemma is a defensible proposed research order, not a proved uniqueness
or necessity theorem.

## 5. Static and numerical audit

The producer script:

- imports no project module;
- implements the stated modular phases;
- normalizes `H` by `binom(k+m-1,m-1)` and `G` by
  `binom(n+r-1,r-1)`;
- imposes the `G` row barrier on the pre-row state using the correct floor;
- splits `outside=full-inside`, consistent with the exact event decomposition;
- stays inside the cases declared in its plan.

Filesystem timestamps put the plan before the script, result, and report, in
that order. This is useful provenance but not a cryptographic precommitment.

The auditor implementation imports no producer or project code and uses a
direct transition/coefficient recurrence. It reproduced only these declared
representatives: `H` at `(r,j)=(30,6..9),(60,12..13)` and `G` at `r=30`,
barriers `-4,0`. All displayed magnitudes and probabilities agree with the
producer JSON to the printed precision. The unrestricted path count was
`163011640`, exactly the composition count, and the decomposition residual was
zero in binary64 arithmetic. These checks are `[NUM]` only.

## Final classifications

- endpoint-coordinate reconciliation: **`PROVED / AUDIT PASS`**;
- tilted conditional bridge representation: **`PROVED / AUDIT PASS`**;
- exact barrier decomposition: **`PROVED / AUDIT PASS`**;
- growing-depth telescoping reduction: **`REFUTED AS A VIABLE ARGUMENT`**;
- literal modulus monotonicity in `j`: **`REFUTED BY FINITE COUNTEREXAMPLES`**;
- stochastic domination as a proof of that monotonicity:
  **`INVALID GENERAL MECHANISM`**;
- eventual bounded-comparison PWE: **`OPEN / FINITE DATA DO NOT REFUTE`**;
- claim that PWE logically requires nonvanishing: **`OVERSTATED; REPAIR`**;
- fixed-barrier KFB for fixed-start `G`/`H_0`: **`OPEN, PRECISELY
  FORMULABLE`**;
- fixed-barrier KFB as coverage of the entire PWE window:
  **`INSUFFICIENT AS STATED`**;
- crossing-term arithmetic estimate: **`OPEN / LOAD-BEARING FOR THE SEPARATE
  DECOMPOSITION ROUTE`**;
- `G=O(1/r)`, nonzero profile, polynomial lower bound, B4, and Collatz:
  **`OPEN`**.

Nothing audited or reproduced here proves the Collatz conjecture.
