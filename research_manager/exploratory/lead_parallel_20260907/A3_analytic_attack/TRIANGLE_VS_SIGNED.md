# TRIANGLE_VS_SIGNED.md — is the triangle-weighted lemma TRUE, FALSE, or undecidable?

Date: 2026-09-07. EXPLORATORY WORKING ARTIFACT, pending the manager's acceptance gate.
Nothing here proves the Collatz conjecture. No E6-N2 claim.

Target `(S)`: `S_r := sum_{j<=min(n_r,L_r)} w_{r,n_r}(j) |D_j| |H_{r-4,n_r-j}(j)| <= C/r`.

---

## 1. `D_j` computed exactly for `j <= 40`  [PROVED here] [NUM]

Independent computation (own code, sum over all `binom(j+3,3)` weak compositions of `j` into 4 parts,
`B_4 = 27 + 9*2^{a_1} + 3*2^{a_1+a_2} + 2^{a_1+a_2+a_3}` reduced mod 1296; composition counts asserted
against `binom(j+3,3)`). Agrees with `A2_numeric_probe/WINDOW_TABLE.csv` `abs_D` to printed precision.

```
 j : |D_j|      arg D_j      j : |D_j|      arg D_j
 0 : 1.000000  +0.31513     20 : 0.012068  +2.09395
 1 : 0.997595  +0.39510     21 : 0.013856  +2.37541
 2 : 0.987483  +0.52407     22 : 0.006908  +2.19975
 3 : 0.950645  +0.73352     23 : 0.004264  +3.09649
 4 : 0.835182  +1.05543     24 : 0.005005  +2.49772
 5 : 0.596803  +1.43339     25 : 0.008047  +2.32802
 6 : 0.339342  +1.65101     26 : 0.010103  +2.58622
 7 : 0.253537  +1.23949     27 : 0.008553  +2.85381
 8 : 0.143172  +0.81156     28 : 0.008693  +2.68014
 9 : 0.114711  +1.21007     29 : 0.008510  +2.45378
10 : 0.065235  +1.39732     30 : 0.007858  +2.18490
11 : 0.042420  +0.85187     31 : 0.006530  +1.91389
12 : 0.031596  +1.63505     32 : 0.004723  +1.74951
13 : 0.011119  +2.55306     33 : 0.003332  +1.81287
14 : 0.020175  +1.82731     34 : 0.004245  +1.78308
15 : 0.024114  +2.08723     35 : 0.004702  +1.94698
16 : 0.021168  +2.54873     36 : 0.003743  +1.82996
17 : 0.015980  +2.09864     37 : 0.003181  +1.86363
18 : 0.018280  +1.93965     38 : 0.003345  +1.98814
19 : 0.017450  +2.00043     39 : 0.002272  +1.98496
                            40 : 0.002269  +2.45412
```

**Correction to the working premise.** `|D_j|` is **not** bounded away from `0` for many `j`:
`|D_j| > 0.3` only for `j <= 6`; `|D_j| < 0.032` for every `12 <= j <= 40`; `min = 0.00227` at `j=40`.
`D_j` itself exhibits the same wrapping collapse as `H_j`, and for the same reason (STRUCTURE §3):
`D_j` is the 4-row prefix bridge whose height rises with `j`.

**Consequence.** `(S)` does **not** "essentially require" uniform `|H_j| = O(1/r)` over the whole
window. It requires it only where `w(j)|D_j|` is non-negligible. `[NUM]` at `r = 600` the window sum
`S_r` is carried by `j <= 5` to better than `99.6%`, with per-`j` shares
`j=0: 31.8%, j=1: 34.3%, j=2: 21.3%, j=3: 9.2%, j=4: 2.8%, j=5: 0.53%`.
The `argmax_j` of the term `w|D_j||H_j|` is `j = 1` for 572 of the 587 tested `r` (`j = 0` for the
other 15). The logarithmic cutoff `L_r = 39` at `r = 600` is enormously conservative for this sum;
it is needed only because the audited proof of (T) bounds `|D_j H_j| <= 1`.

`[NUM]` `weight_in_window = 1.000000` to double precision for every tested `r`: the truncation
remainder is numerically invisible, consistent with (T).

## 2. How much does the triangle inequality actually cost?  [NUM] — the decisive measurement

```
 r      |G_{r,n_r}|      S_r         S_r/|G|      r|G|      r S_r
 50     5.1613e-01    6.1066e-01     1.1832      25.81     30.53
100     2.4124e-01    2.8760e-01     1.1922      24.12     28.76
200     1.1585e-01    1.3751e-01     1.1870      23.17     27.50
300     6.9505e-02    8.2338e-02     1.1846      20.85     24.70
400     5.4150e-02    6.4071e-02     1.1832      21.66     25.63
500     4.0111e-02    4.7427e-02     1.1824      20.06     23.71
600     3.5185e-02    4.1582e-02     1.1818      21.11     24.95
```

**`S_r / |G_{r,n_r}| -> 1.1818`, monotonically decreasing and evidently convergent.** `[NUM]`
Log-log slopes over `r = 50..600`: `|G|: -1.081`, `S_r: -1.081` — identical to three digits.

So **discarding all cancellation between prefix classes costs a bounded factor of about 18%,
and that factor is `r`-stable.** The reason is visible in `arg(D_j H_j)`: at `r = 600` the four
dominant classes have arguments `+1.335, +1.651, +2.135, +2.894` — a spread of ~1.6 rad, which is
partial misalignment, not equidistribution, and the spread does not grow with `r`.

## 3. Verdict

**`(S)` is `[PLAUSIBLE, heuristic]` TRUE — and simultaneously it is NOT a genuine step.** More
precisely:

1. **Likely TRUE.** `r S_r` is flat in `[22.1, 27.5]` for `r >= 200`; the log-log slope is `-1.08`;
   the sum is dominated by `j <= 5`, where `|H_j| <= |H_0| ~ 46/r` `[NUM]`. Nothing in the data or in
   the barrier mechanism suggests failure.
2. **But `(S)` is equivalent to E6-N2 up to a factor that `[NUM]` converges to 1.1818.** Since
   `|G| <= S_r + 4r^{-1-delta}` (audited (T) + triangle inequality) and `[NUM] S_r <= 1.20 |G|` for
   all tested `r >= 50`, the two statements are numerically interchangeable. The derivation's
   logical point — that `(S)` is *strictly stronger* as a sufficient condition, and that its failure
   would not refute E6-N2 — is **correct and is not disputed**; but the separation it buys is at most
   a factor `~1.19` on this family, so **`(S)` is not a reduction in difficulty.** It is the same
   problem with the cancellation-between-classes discarded, and that cancellation was worth 18%.
3. **Undecidable without new ideas?** Yes, in the operative sense: *no argument can establish `(S)`
   without also establishing E6-N2*, because `(S)` implies E6-N2 outright (triangle + (T)), and the
   data show it is not weaker by more than a constant. The genuinely new input required is (U6) of
   UNIFORM_H_ANALYSIS.md — the joint arithmetic equidistribution off the barrier event.

## 4. Could between-`j` cancellation rescue `G = O(1/r)` if `(S)` fails?

`[NUM]` **No, not at any tested scale.** The rescue factor available is exactly `S_r/|G|`, measured
at `1.18` and *decreasing*. If `S_r` were to fail the `C/r` bound by more than that bounded factor,
`|G|` would fail too, unless the phase alignment changes character at `r` far beyond 600 — for which
there is no evidence, since `arg(D_j H_j)` for the dominant classes is `r`-stable to two decimals
between `r = 300` and `r = 600`. `[OPEN]` that this persists as `r -> infinity`; it is asserted here
only as a numerical observation on `14 <= r <= 600`.

## 5. Is the derivation's own claim correct?

> "the signed truncated-sum bound ... (up to the `o(1/r)` error) simply restates the original
> upper-bound problem"

**`[PROVED here]` CORRECT.** By (T), `| |G| - |signed truncated sum| | <= 4r^{-1-delta} = o(1/r)`,
so the two are equivalent as `O(1/r)` statements. `[NUM]` confirms: `abs_signed_trunc_minus_G` is at
the `1e-17` level for every tested `r`.

**Addendum this analysis contributes:** the same is true of the *triangle* version up to a bounded
factor. The derivation's and the audit's framing of `(S)` as "a stronger sufficient requirement" is
logically exact but, on this family, empirically almost vacuous. Recommending `(S)` as *the* next
target therefore carries a real risk of re-running E6-N2 under a new name.

`[OPEN]` `(S)`. `[OPEN]` E6-N2. `[OPEN]` any nonzero lower bound or profile coefficient — note
`[NUM]` that `r|G|` does not converge but oscillates almost-periodically in `theta_r = {beta r}`
(range `[18.73, 23.17]` for `r >= 200`, correlation with `theta_r` = 0.828), so a limit-form
coefficient claim would be ill-posed as usually written.
