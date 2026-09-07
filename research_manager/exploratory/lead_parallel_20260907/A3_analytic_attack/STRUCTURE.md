# STRUCTURE.md — exact structure of H_{m,k}(j) and the circularity verdict

Date: 2026-09-07. Status: EXPLORATORY WORKING ARTIFACT, pending the manager's acceptance gate.
Not a canonical result. Nothing here proves the Collatz conjecture. No sealed task was run,
no tracked file was modified, no canonical state was edited.

Constants: `beta = log_2(3) - 1 = 0.5849625007`, `alpha = 1 + beta = log_2 3 = 1.5849625007`,
`rho = beta/alpha = 0.3690702464`, `theta_r = {beta r}`, `n_r = floor(beta r) - 8`, `m = r - 4`.

---

## 1. Row form of H  [PROVED here] [verified numerically]

**Claim 1.** For all `m >= 1, k >= 0, j >= 0`, with `Y_0 = 0`, `Y_s = y_1 + ... + y_s`,

```
H_{m,k}(j) = E[ prod_{s=1}^{m} e_{3^{s+4}}( 2^{ j + s - 1 + Y_{s-1} } )  |  Y_m = k ],
```

`y` uniform on weak compositions of `k` into `m` parts.

*Proof.* `2^j B_m(y+1) = sum_{s=1}^m 3^{m-s} 2^{j + A'_{s-1}}` with `A'_{s-1} = (s-1) + Y_{s-1}`,
and `3^{m-s}/3^{m+4} = 1/3^{s+4}`. The modulus of row `s` is therefore `3^{s+4}`, not `3^{m+4}`.
The product form is a rational identity, not a congruence. QED

`[NUM]` Mechanical check against the frozen definition of `H`: `max |H_def - H_rowform| = 4.7e-16`
over `m <= 5, k <= 5, j <= 9` (180 cases).

## 2. Exact self-similarity of the four-prefix split  [PROVED here] [verified numerically]

**Claim 2.** For every admissible `a = z+1` of length `r >= 5`, with `j = S_4 = sum_{i<=4} z_i`,

```
F_r(a) = [ prod_{s=1}^{4} e_{16*3^s}(2^{A_{s-1}}) ] * [ prod_{s=1}^{m} e_{3^{s+4}}(2^{ j+s-1+Y_{s-1} }) ],
```

where `Y` is the suffix walk `(z_5,...,z_r)`. The second bracket is exactly the row form of Claim 1,
and for `s >= 5` the row `e_{16*3^s}(2^{A_{s-1}})` of `F_r` equals `e_{3^s}(2^{s-5+S_{s-1}})`.

*Proof.* `2^{A}/(16*3^s) = 2^{A-4}/3^s`; re-index `s' = s+4` and use `j + Y_{s'-5} = S_{s'-1}`. QED

`[NUM]` Mechanical check: `max |F_full - F_split| = 0.0` (exact, bit-identical) over `r = 5,6,7`,
all `z_i <= 2` (3^5 + 3^6 + 3^7 = 3159 paths).

**Consequence.** The tail factor `H` is *literally the last `m` rows of the same phase product*.
The four-prefix reduction is a self-similar splitting of `G`, not a passage to a different object.

## 3. The exact real coordinate: `H` and `G` are one two-parameter family  [PROVED here]

Because the row modulus and the row numerator are both powers, the modular reduction can be
removed entirely. Put `u_s = j + s - 1 + Y_{s-1}` and

```
delta_s := u_s - alpha (s+4).
```

Then, EXACTLY (real identity, no congruence),

```
e_{3^{s+4}}( 2^{u_s} ) = exp( 2 pi i * 2^{u_s} / 3^{s+4} ) = exp( 2 pi i * 2^{ delta_s } ),
```

and `delta_{s+1} - delta_s = y_s - beta` is a MEAN-ZERO increment under the `rho`-tilted law
(section 5). Hence

> **[EXACT] `H_{m,k}(j) = E[ prod_{s=1}^{m} exp(2 pi i * 2^{delta_s}) ]`, the expectation over a
> mean-zero random-walk BRIDGE `delta` of length `m` with**
> ```
> delta_1     = j - 5*alpha              (left endpoint)
> delta_{m+1} = j + k - beta*m - 5*alpha (right endpoint).
> ```

Define `Psi(m; a, b) :=` this bridge functional with endpoints `a, b`. Then, with the same algebra
applied to `F_r` itself (`delta'_s = A_{s-1} - 4 - alpha s`):

```
G_{r,n_r}            = Psi( r  ; -4 - alpha ,          -12 - alpha - theta_r )
                     = Psi( r  ; -5.5850   ,          -13.5850 - theta_r )

H_{r-4, n_r-j}(j)    = Psi( r-4; j - 5*alpha ,         -13 - beta - theta_r )
                     = Psi( r-4; j - 7.9248 ,          -13.5850 - theta_r ).
```

Three exact consequences.

* **(3a) The right endpoint of the H-family does NOT drift with `j`.** `j + k - beta m - 5 alpha
  = 4beta - 8 - theta_r - 5 alpha`, independent of `j`. The derivation's "endpoint-offset drift
  `4beta - 8 - theta_r - j`" is real in the `(k, m)` parametrization but is an artifact of it: once
  the frequency `2^j` is absorbed, ALL of the `j`-drift sits in the LEFT endpoint `a_j = j - 5alpha`,
  and the right endpoint coincides with that of `G` itself. `[PROVED here]`
* **(3b) The conductor `3^{m+4} = 3^r` (not `3^{r-4}`) is exactly equivalent to a shift of the left
  endpoint by `4 alpha = 6.3399`.** It is not an independent obstruction and carries no extra
  arithmetic content. `[PROVED here]`
* **(3c) `G` is the `w`-mixture of the `H` family, and its own left endpoint `-4-alpha` is recovered
  at `j = 4 beta = 2.3399`**, which is exactly `lim_r E[J | S_r = n_r] = 4 beta`. `[NUM]` the probe
  gives `E[J] = 2.0000, 2.1600, 2.2267, 2.2500, 2.2720, 2.2800` at `r = 100..600`, increasing to
  `4 beta = 2.3399`.

## 4. Transfer operator and coefficient extraction  [PROVED here]

Let `N = ord_{3^{m+4}}(2) = 2 * 3^{m+3}`; the residue `2^{u} mod 3^{m+4}` is determined by
`u mod N`, and it determines every row modulus `3^{s+4}, s <= m`. On `C[Z/N]` define, for a formal
variable `x` marking the composition weight,

```
( M_s(x) f )(u) = e_{3^{s+4}}(2^u) * sum_{y>=0} x^y f(u + 1 + y).
```

Then `sum_{k>=0} binom(k+m-1,m-1) H_{m,k}(j) x^k = ( M_1(x) M_2(x) ... M_m(x) 1 )(j)`, and

```
H_{m,k}(j) = binom(k+m-1,m-1)^{-1} * [x^k] ( M_1(x)...M_m(x) 1 )(j).
```

The operator sequence is **non-stationary**: `M_s` depends on `s` through the conductor `3^{s+4}`.
In the `delta` coordinate of section 3 the family becomes **stationary**: the row multiplier is
`exp(2 pi i 2^{delta})` on the real line and the increment law is `s`-independent. This is the
correct spectral coordinate; the growing conductor is an artefact of the integer parametrization.

Order remark: `ord_{3^t}(2) = 2 * 3^{t-1}` grows geometrically, so no finite quotient of the state
space is preserved and no finite-rank stationary operator exists in the residue coordinate.

## 5. The natural tilt is `rho = beta/alpha`, and it is exactly the cutoff constant  [PROVED here]

Under the canonical law `Z_i ~ Geom(1/2)` (`P(Z=j)=2^{-(j+1)}`), `E[S_r] = r` while `n_r ~ beta r`.
So the microcanonical conditioning is a LARGE DEVIATION, not a central one:
`[NUM] P_{iid}(S_r = n_r) = exp(-39.85)` at `r = 600` (`~ e^{-c r}`).

Conditioning on `S_r = n` is tilt-invariant (all tilts induce the same uniform law on weak
compositions). The tilt that centres the constraint is the geometric with ratio `q` solving
`q/(1-q) = beta`, i.e. `q = beta/(1+beta) = beta/alpha = rho`. Then `1-rho = 1/alpha`, so the
success parameter is `p* = 1/alpha = 1/log_2 3` — **the `p*` named in the E7R-B4 direction is exactly
`1 - rho`, and `rho` is exactly the constant `beta/alpha` already appearing in the audited
prefix-cutoff lemma.** Variance: `sigma^2 = rho/(1-rho)^2 = 0.927144`.

`[NUM]` local-CLT confirmation under the tilt: `sqrt(r) * P_rho(S_r = n_r) =`
0.30288 (r=100), 0.38074 (400), 0.40077 (1000), 0.41370 (20000) → `1/(sigma sqrt(2 pi)) = 0.414321`.

Fourier inversion over the sum constraint (the ONE extra dual variable `phi`):

```
H_{m,k}(j) = P_rho(Y_m=k)^{-1} * INT_0^1 Phi_m(j, phi) e(-phi k) d phi ,
Phi_m(j,phi) = E_rho[ prod_{s=1}^m e_{3^{s+4}}(2^{j+s-1+Y_{s-1}}) e(phi Y_m) ]   (unconditioned).
```

`P_rho(Y_m=k)^{-1} ~ sigma sqrt(2 pi m) ~ 2.41 sqrt(m)`. This `m^{1/2}` prefactor is the entire
cost of the microcanonical conditioning; see UNIFORM_H_ANALYSIS.md §4.

---

## 6. CIRCULARITY VERDICT

**`H_{m,k}(j)` is NOT a genuinely simpler object. The four-prefix reduction is exactly circular in
species.** `[PROVED here]`

Itemised against the three hoped-for gains:

| hoped-for gain | verdict |
|---|---|
| fixed endpoint offset | **NO** in the `(k,m)` coordinates (offset `4beta-8-theta_r-j` drifts); **YES but useless** in `delta` coordinates — the right endpoint is fixed AND equal to `G`'s own, while the drift moves to the left endpoint `a_j = j - 5alpha`. Either way one endpoint drifts over an `O(log r)` range. |
| fixed conductor | **NO.** Conductor is `3^{m+4} = 3^r`, the same as `G`'s; §3b shows it is exactly a `4alpha` shift of the left endpoint, carrying no independent content. The `16` in `G`'s conductor `16*3^s` is likewise only a `-4` shift of the dyadic exponent, consistent with the audited LT statement that no independent mod-16 cocycle survives. |
| shifted / easier critical line | **NO.** Both `G` and every `H_j` are bridges with the SAME mean-zero increment law under the SAME tilt `rho`, the SAME right endpoint `-13.585 - theta_r`, and lengths `r` vs `r-4`. The critical line is identical. |

Sharpest form of the circularity: **taking `j = 0` in the proposed uniform-H bound gives
`|Psi(r-4; -7.9248, -13.5850-theta_r)| = O(1/r)`, which is a statement of exactly the same strength
and species as E6-N2 `|Psi(r; -5.5850, -13.5850-theta_r)| = O(1/r)`** — same family, same endpoints
up to an `O(1)` shift of `a`, same length up to 4. Proving uniform-H is therefore at least as hard
as E6-N2, and in fact strictly harder, since it demands the estimate simultaneously for an
`O(log r)`-long segment of the `a`-axis rather than at one point. `[PROVED here]`

The only thing the reduction genuinely buys is **explicitness of the left endpoint as a summation
parameter `j`**, which is what makes the comparison lemma of NEXT_LEMMA.md formulable.

`[OPEN]` Everything about the size of `Psi(m; a, b)`.
`[OPEN]` E6-N2. `[OPEN]` `|E[F_{r,4}|S_r=n_r]| = O(1/r)`.
