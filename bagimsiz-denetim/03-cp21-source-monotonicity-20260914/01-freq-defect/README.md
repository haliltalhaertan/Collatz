# Per-frequency defect Delta^(a) = M^(a) - L^(a): settlement

All arithmetic is exact: Python `int`, `fractions.Fraction`, and cyclotomic
integers in `Z[zeta_N]` (power basis, relation `zeta^(N/2) = -1`).
**No floating point enters any claimed number.** Signs of non-rational
cyclotomic reals are decided by certified rational enclosures built from
integer-sqrt bounds (`cyclo.sign_of_real`), so every reported sign is a proof.

Collatz is NOT solved. Nothing here bears on that. A finite table is NEVER a
uniform theorem.

## Files (absolute paths)

| file | role |
|---|---|
| `C:\Users\MDP\collatz-analysis\freq_defect\cyclo.py` | exact `Z[zeta_N]`, certified sign/enclosure |
| `C:\Users\MDP\collatz-analysis\freq_defect\source.py` | prefix source, `J_r`, `Ecal`, transfer, `I/F/Out/L/M`, **GATE** |
| `C:\Users\MDP\collatz-analysis\freq_defect\freq.py` | DFT, Parseval checks, mod-N decomposition |
| `C:\Users\MDP\collatz-analysis\freq_defect\grid.py` | mod-N grid run (`grid.json`) |
| `C:\Users\MDP\collatz-analysis\freq_defect\gauges.py` | gauge variants A/B/C at mod-N |
| `C:\Users\MDP\collatz-analysis\freq_defect\forced_index.py` | **the structural proof that mod-q is forced** |
| `C:\Users\MDP\collatz-analysis\freq_defect\gaugeD.py` | forced-index decomposition, reproduces prior 3/2+3/2 |
| `C:\Users\MDP\collatz-analysis\freq_defect\final.py` | 3 gauge variants on the forced index, 41 rows (`final.json`) |
| `C:\Users\MDP\collatz-analysis\freq_defect\minmax.py` | cross-field-safe minima + lift carriers (`minmax.json`) |
| `C:\Users\MDP\collatz-analysis\freq_defect\mandated_min.py` | exact min on the mandated grid (`mandated_min.json`) |
| `C:\Users\MDP\collatz-analysis\freq_defect\witness.py` | exact witness printouts |
| `C:\Users\MDP\collatz-analysis\freq_defect\kill.py` | minimal repro of the mod-N artefact |

Reproduce everything: `python source.py && python forced_index.py && python final.py && python mandated_min.py`

## 1. GATE [EXACT COMPUTATION] — reproduced from scratch

    (m,s)=(4,2): I=40/3  F=16  Out=31/3  L=8/3  M=17/3  defect=3
    (m,s)=(2,1): I=F=Out=4               L=0    M=0     defect=0
    (m,s)=(3,2): I=12  F=12  Out=8       L=0    M=4     defect=4

All match. The merge identity
`M = sum_k J_s(n_{k-1}E_k - n_k O_{k-1})/(n_k n_{k-1}(n_k+n_{k-1}))`
also reproduces `M` exactly on every gate row and every grid row.

## 2. The decomposition [EXACT COMPUTATION + PROOF of the index]

`N = 2^(s+1)`, `q = 2^s`, `c_k = 3^k mod N`, `zeta = zeta_N`.

Split `Phat_k(xi) = A_k(xi) + B_k(xi)` (even / odd `z`). Then

    Ehat_k(xi) = A_k(xi) + zeta^(xi c_k) B_k(xi)
    Ohat_k(xi) = zeta^xi [ B_k(3xi) + zeta^(3 xi c_k) A_k(3xi) ]

Verified exactly on every row:

* Parseval, on **every** array decomposed: `sum_{xi odd mod 2^r} |Xhat(xi)|^2 == J_r(X)` (sibling-difference form).
* `J_s(E_k) == (1/2) sum_{xi odd mod N} |Ehat_k(xi)|^2`, same for `O_k`.
* Round-7 lift law, per `k`: `J_s(E_k)+J_s(O_k)-J_{s+1}(P_k) == sum_{xi odd} cos(2 pi 3^k xi/N)|Phat_k(xi)|^2`.
* Merge spectral form, per `k`: `J_s(n_{k-1}E_k - n_k O_{k-1}) == (1/2) sum_{xi odd} |n_{k-1}Ehat_k(xi) - n_k Ohat_{k-1}(xi)|^2`.
* `3` is invertible mod `2^t`, so `xi -> 3^k xi` is a bijection on odd residues.

### THE INDEX IS FORCED — this is the whole question [PROOF, verified `forced_index.py`]

`E_k, O_k` are functions on `Z/q`. Hence

    Ehat_k(xi) = Ehat_k(xi+q),   Ohat_k(xi) = Ohat_k(xi+q)          (q-PERIODIC)

while the lift weight satisfies

    cos(2 pi c_k (xi+q)/N) = - cos(2 pi c_k xi/N)                   (q-ANTI-periodic)

Both checked exactly on 1294 `(k,xi)` pairs over `s=2..5`, `m<=10`.

Therefore the merge side carries **no** information at the mod-`N` level: a
per-lift split of `M` between `xi` and `xi+q` is an *invention*, not a
decomposition. The unique common index on which both `M^(a)` and `L^(a)` are
well defined is

    a  odd  mod q = 2^s,   lift contributions of xi and xi+q SUMMED.

Final decomposition (`a` odd mod `q`, `lifts(a) = {b, b+q}` per stratum gauge):

    L^(a) = sum_{k=1..m} (1/n_k) sum_{xi in lifts_k(a)} cos(2 pi 3^k xi/N) |Phat_k(xi)|^2
    M^(a) = sum_{k=2..m} sum_{xi in lifts_k(a)} |n_{k-1}Ehat_k(xi) - n_k Ohat_{k-1}(xi)|^2
                                                / (2 n_k n_{k-1} (n_k+n_{k-1}))
    Delta^(a) = M^(a) - L^(a)

`M^(a) >= 0` termwise [PROOF]: each summand is `|.|^2 / positive`.

**Identity check, the correctness criterion:** `sum_a L^(a) == L_lift`,
`sum_a M^(a) == M_merge`, `sum_a Delta^(a) == defect`, exactly as rationals —
**holds on all 41 rows computed**, for all three stratum-gauge variants.

## 3. Grid covered

Mandated: `s in {2,3,4}` x `m in 4..12` with `s <= m-1` → **26 rows, 118 (row,frequency) pairs**.
Extended for free: `s=5, m=6..14` and `m=13,14` for `s=2,3,4` → **41 rows total**.
Wall clock: gate+mod-q grid ≈ 40 s per gauge variant; full suite (all scripts, 3 gauge
variants, mod-N control runs, cross-field certified minima) ≈ 6 min.

## 4. VERDICT: **SURVIVES** on the forced index [EXACT COMPUTATION]

    pairs with Delta^(a) < 0 on the mandated grid : 0 / 118
    pairs with Delta^(a) < 0 on all 41 rows       : 0

Exact minimum on the **mandated** grid:

    (m,s) = (5,4),  a = 3  (and its partner a = 13)
    Delta = 56/15 - (1/2)z^2 - (8/15)z^4 - (9/10)z^6 + (9/10)z^10 + (8/15)z^12 + (1/2)z^14
            in Z[zeta_32]
          ~ 1.366376389...   (certified enclosure, > 0)

Smallest rational value on the grid: `3/2` at `(4,2)`, a=1 and a=3 — exactly the
prior session's reported number, now with a spec behind it.

Extended-grid minimum (41 rows): `~0.201707805...` at `(m,s)=(13,4)`, `a=5`.
Still positive but an order of magnitude smaller — the margin is **shrinking**, so
this is not a robust-looking inequality.

## 5. The prior session's claim is CONFIRMED, and the auditor's doubt was justified

Reproduced exactly: `(4,2)` gives `Delta^(1) = Delta^(3) = 3/2`, sum `3` = defect.
The auditor could not verify it because no index spec existed — and that matters:
**if you refine to mod N and split `M` evenly between the two lifts, `Delta^(a) < 0`
on 26/26 rows** (`grid.json`, first negative already at `(4,2)`, `a=1`,
`Delta = 3/4 - (5/3)sqrt(2)/... ~ -1.6`). That refinement is not a decomposition
of the merge energy (see §2), so it is **not** a counterexample — but it shows the
result is convention-sensitive and must always be quoted with its index.

## 6. Which frequency carries the positive lift — IT MOVES

`L^(a) > 0` carriers (from `minmax.json`):

| s | q | carriers seen |
|---|---|---|
| 2 | 4 | `{1,3}` (m=4,8,10) or `{}` (m=5,6,7,9,11,12,13,14) |
| 3 | 8 | `{3,5}` (most m) or `{}` (m=6) |
| 4 | 16 | `{5,11}`, sometimes `{3,5,11,13}` (m=11), sometimes `{}` (m=9,10) |
| 5 | 32 | `{9,23}`, `{3,9,23,29}`, `{3,7,9,23,25,29}`, `{1,9,13,19,23,31}` |

The carrier is **not** fixed: it moves with `s` (roughly tracking `a ~ q/3`, the
gauge orbit of `3^{-k}`) and fluctuates with `m`, including rows where the lift is
negative at every frequency. Carriers always appear in conjugate pairs `{a, q-a}`.

## 7. Status labels

* [PROOF] `M^(a) >= 0` termwise; `E_k,O_k` spectra are `q`-periodic and the lift
  weight is `q`-anti-periodic, hence mod-`q` is the forced common index.
* [EXACT COMPUTATION] the gate; all Parseval / lift-law / merge-spectral checks;
  `sum_a Delta^(a) = defect` on 41 rows; the sign table; the minima.
* [CONJECTURE] `Delta^(a) >= 0` for all odd `a`, all `m,s`. **Not proved.** 41 rows
  is a finite table, not a uniform theorem — and programme history (`s>=3 => L<=0`)
  shows exactly this kind of evidence collapsing when the grid is extended. The
  shrinking margin at `s=4, m=13` is a live warning.
