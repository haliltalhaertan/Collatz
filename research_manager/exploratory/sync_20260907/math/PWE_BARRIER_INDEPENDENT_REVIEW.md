# Independent review: PWE and the barrier-probability mechanism

Date: 2026-09-07  
Scope: bounded exploratory mathematical review. No sealed source, old depth run,
Git/Drive operation, or canonical state was touched.  
Classification: exact algebra below is `[PROVED IN THIS REVIEW]`; finite checks
are `[NUM]`; all asymptotic statements explicitly labelled otherwise remain open.

## Executive verdict

1. The apparent discrepancy `j-5 alpha` versus `j-4 alpha-1` is not an
   algebraic contradiction. They are the same bridge in two time conventions,
   separated by `beta=alpha-1`. The row-phase convention naturally starts at
   `j-5 alpha`; the pre-increment convention naturally starts at
   `j-4 alpha-1`.
2. PWE remains open and is numerically plausible as a bounded-ratio statement.
   Its advertised monotonicity/coupling justification is invalid: modulus of a
   complex Feynman--Kac expectation has no stochastic order, and explicit
   in-window adjacent increases occur. More importantly, the ratio form hides
   a nonvanishing/lower-bound requirement on `H_0`. PWE is not presently a
   purely probabilistic comparison lemma.
3. A barrier mechanism remains plausible, but the published step saying that
   the product is uniformly close to one on a fixed barrier event does not
   yield the claimed scale. Its deterministic error is `O(m 2^{-T})`; making
   this `o(1/m)` requires a barrier depth growing like `2 log_2 m`, which is
   eventually below the fixed starting endpoint and makes the event empty.
4. The first missing theorem for a valid barrier route is a **killed
   Feynman--Kac ballot/local-time theorem**, not an ordinary ballot theorem.
   Even after that, a separate arithmetic estimate is needed for paths that
   cross the barrier. Thus the former statement that off-barrier
   equidistribution `(U6)` was the only missing content was too strong.
5. No load-bearing theorem, countertheorem to PWE, `O(1/r)` estimate, nonzero
   profile, or Collatz result was obtained. No audit stop rule fires.

Throughout,

```text
alpha = log_2 3,  beta = alpha-1,  rho = beta/alpha,
m = r-4,  k = n_r-j,  n_r=floor(beta r)-8.
```

## 1. Exact bridge formulation and the endpoint constant

Let `Y_t=y_1+...+y_t`, where under the `rho`-tilted law the `y_i` are
independent geometric variables with

```text
P_rho(y_i=q)=(1-rho)rho^q,  q>=0,
E_rho[y_i]=beta.
```

Conditioning on `Y_m=k` makes the vector uniform on weak compositions of `k`,
so it is exactly the microcanonical law defining `H`; the choice of tilt does
not change this conditional law.

### Convention A: pre-increment bridge state

For `0<=t<=m`, set

```text
X_t = j + Y_t - beta t - (4 alpha+1).
```

Then

```text
X_0 = j-4 alpha-1,
X_m = j+k-beta m-4 alpha-1,
X_{t+1}-X_t = y_{t+1}-beta.
```

The row with index `s=t+1` is

```text
e_{3^(s+4)}(2^(j+s-1+Y_(s-1)))
 = exp(2 pi i 2^(X_t-beta)).
```

Thus `j-4 alpha-1` is correct when the state is recorded immediately before
the row and the observable is `q_beta(x)=exp(2 pi i 2^(x-beta))`.

### Convention B: row-phase bridge state

Set `Delta_t=X_t-beta`. Then

```text
Delta_0 = j-4 alpha-1-beta = j-5 alpha,
Delta_m = j+k-beta m-5 alpha,
Delta_{t+1}-Delta_t = y_{t+1}-beta,
```

and the functional takes the cleaner form

```text
H_(m,k)(j)
 = E_rho[ product_(t=0)^(m-1) q(Delta_t) | Y_m=k ],
q(x)=exp(2 pi i 2^x).
```

Therefore

```text
j-5 alpha = (j-4 alpha-1)-beta.
```

They are not competing constants. They belong to states that differ by a
deterministic translation and to correspondingly translated row functions.
Mixing an endpoint from one convention with the row function from the other
would be an error.

At the critical target `k=n_r-j`, both endpoints are independent of `j` on the
right:

```text
X_m     = -13-theta_r,
Delta_m = -13-beta-theta_r,
theta_r={beta r}.
```

The analogous exact formula for `G` in Convention B is

```text
G_(r,n_r)
 = E_rho[ product_(t=0)^(r-1) q(Delta_t)
          | Delta_0=-4-alpha,
            Delta_r=-12-alpha-theta_r ].
```

This confirms the substantive A3 observation: the prefix variable moves only
the left endpoint after the frequency is absorbed, while the critical right
endpoint is fixed up to `theta_r`.

## 2. PWE adjudication

PWE asks for a fixed `C` such that

```text
|Psi(m;a_0+j,b_r)| <= C |Psi(m;a_0,b_r)|,
0<=j<=L_r,  a_0=-5 alpha.
```

### What survives

- It is a precise, falsifiable statement and contains no explicit decay rate.
- If it and `|H_(r-4,n_r)(0)|=O(1/r)` both held, the audited prefix truncation
  would reduce the logarithmic prefix window to the `j=0` family.
- Existing data through the declared ranges support a bounded ratio; that is
  `[NUM]` only.

### What does not survive

The proposed proof slogan, "raising the left endpoint can only increase
cancellation", is not a theorem. A pathwise ordering can order barrier events,
but it cannot order

```text
|E[product q(Delta_t)]|,
```

because complex phases have no compatible positive cone. The independent
bounded check found adjacent increases inside the declared prefix window:

- `r=30`: `|H_6|=0.5190 < |H_7|=0.5993 < |H_8|=0.7159`;
- `r=60`: `|H_12|=0.009287 < |H_13|=0.009966`, with several further
  increases before the cutoff.

These do not refute eventual bounded-ratio PWE, but they refute monotonicity as
its general mechanism. At `r=30,40,50`, where the cutoff still contains the
degenerate `k=0` endpoint, the maximizer is `j=n_r` and the ratios to `H_0` are
`1.024`, `1.115`, and `1.263`; the free `r_0` makes these non-counterexamples.

There is a second, more structural issue. A ratio inequality is meaningful only
if the denominator does not vanish. If `H_0=0` for some large `r`, PWE forces
every numerator in the window to vanish at that `r`. More generally, proving a
uniform ratio along the dense phase sequence `theta_r` normally requires
control of small denominators. Current numerics suggest
`r|H_0|` has a positive phase profile, but no rigorous positive lower envelope
or nonzero profile has been proved. Consequently PWE silently imports part of
the nontriviality problem that the earlier E3--E6 work left open.

**Verdict:** PWE is `[OPEN / NUMERICALLY SUPPORTED]`, but it should not be
advertised as accessible by stochastic domination alone or as free of
arithmetic nonvanishing. A ratio-free upper comparison would avoid division by
`H_0`, but any version strong enough to give `O(1/r)` is essentially the
uniform-H/E6-N2 problem again.

## 3. Exact barrier decomposition

Use Convention B and let

```text
M_m=max_(0<=t<m) Delta_t,
Q_m^h(a,b)=P_rho(M_m<=h | Delta_0=a, Delta_m=b),
K_m^h(a,b)=E_rho[product q(Delta_t); M_m<=h
                  | Delta_0=a, Delta_m=b],
R_m^h(a,b)=E_rho[product q(Delta_t); M_m>h
                  | Delta_0=a, Delta_m=b].
```

Then the exact identity is

```text
Psi(m;a,b)=K_m^h(a,b)+R_m^h(a,b).
```

Classical bridge/ballot intuition concerns `Q_m^h`, not `K_m^h`. For fixed
negative endpoints below a fixed barrier, one expects a `1/m` survival scale
under suitable lattice hypotheses. It does not follow that `K_m^h` is close to
`Q_m^h`.

Indeed, on `M_m<=-T`, telescoping only gives

```text
|K_m^(-T)-Q_m^(-T)| <= 2 pi m 2^(-T).
```

To make the right side `o(1/m)` one needs
`T >= (2+epsilon)log_2 m`. But `Delta_0=a=O(1)` is fixed; once `-T<a`, the event
`M_m<=-T` is empty because it already fails at time zero. Hence this uniform
closeness argument cannot convert an ordinary ballot estimate into the desired
Feynman--Kac estimate.

The bounded independent check shows the distinction already at finite size.
For the `G` bridge at barrier `h=0`:

```text
r=30:  Q=0.999953, |K|=0.837342, |Psi|=0.837338
r=60:  Q=0.976856, |K|=0.414905, |Psi|=0.414892
r=100: Q=0.888678, |K|=0.241252, |Psi|=0.241245.
```

Thus the crossing contribution is small in these cases, but the killed complex
expectation is not the survival probability. These are `[NUM]` observations;
they neither establish the asymptotic scale nor a nonzero coefficient.

## 4. The first missing lemma, stated precisely

The first missing result needed to turn the barrier intuition into mathematics
is the following killed Feynman--Kac ballot theorem.

> **KFB (open).** For a fixed barrier `h` (for example `h=0`) and for the
> lattice-compatible endpoints occurring here, prove that, uniformly for
> `a` in the required compact starting set and
> `b=-13-beta-theta`, `theta in [0,1)`,
> ```text
> K_m^h(a,b)=m^(-1)(kappa_h(a,b)+o(1)),
> ```
> with controlled `kappa_h`; for a nonzero-profile result, also prove the
> relevant coefficient is not identically zero (and, where needed, is bounded
> away from zero).

An ordinary ballot/local-limit theorem gives information only about `Q_m^h`.
KFB additionally requires control of the occupation field near the barrier and
the multiplicative functional `product q(Delta_t)`. A plausible route is a
killed renewal theorem with a boundary-layer occupation functional, not the
uniform telescoping estimate above.

Even KFB would not finish the total bridge. The second, arithmetic gap is

```text
R_m^h(a,b)=o(1/m)
```

or a joint asymptotic showing how it combines with `K_m^h`. This is a
microcanonical two-variable Fourier/local-limit problem of B4 type. Existing
finite data at `h=0` suggest suppression of `R`, but do not prove it.

Accordingly `(U6)` is still load-bearing, but it is not the only unproved step:
the inside-barrier term also needs KFB. The clean research order is

1. prove or refute KFB for one fixed barrier and the actual endpoint family;
2. only if KFB survives, attack the crossing term with the joint arithmetic
   estimate.

This order separates the probabilistic renewal content from the arithmetic
equidistribution content and gives an early route-closing test.

## 5. Numerical provenance and scope

The only new computation in this review was predeclared in
`PWE_BARRIER_CHECK_PLAN.md` and implemented independently in
`pwe_barrier_independent_check.py`. It used the fixed cases listed there and
wrote `PWE_BARRIER_CHECK_RESULTS.json`. It imported no producer module and did
not extend the historical depth. All its conclusions are `[NUM]`.

Final classification:

- endpoint-coordinate reconciliation: `[PROVED IN THIS REVIEW]`;
- exact bridge and barrier decomposition: `[PROVED IN THIS REVIEW]`;
- monotonicity rationale for PWE: `[REFUTED AS A GENERAL ARGUMENT]`;
- eventual bounded-ratio PWE: `[OPEN / NUMERICALLY SUPPORTED]`;
- barrier probability as the source of the `1/r` scale: `[PLAUSIBLE BUT
  INCOMPLETE]`;
- KFB: `[OPEN — FIRST MISSING PROBABILISTIC LEMMA]`;
- crossing-term arithmetic cancellation: `[OPEN — SECOND LOAD-BEARING GAP]`;
- `G=O(1/r)`, nonzero profile, polynomial lower bound, Collatz: `[OPEN]`.

Nothing in this review proves the Collatz conjecture.
