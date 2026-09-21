# CP25-PB-FALSIFY report (read-only; independent rebuild)

## Independent derivation used (no import of `lift_coherence.py`)

Map `H(x) = x/2` (even), `(p·x+b)/2` (odd), `p` odd ≥ 3. Composing along
`w = (e_0..e_{m-1})` gives `H_w(x) = (p^k·x + b·B_w)/M` with `M = 2^m`,
`k = Σe_j`, and `B_w = Σ_{j:e_j=1} 2^j·p^{#{i>j:e_i=1}}`.
Validated two ways: hand cases (`(1,0)→1`, `(0,1)→2`, `(1,1),p=3→5`) and
rational simulation of `H_w` from `x=0` on 3000 random words — exact match.
`h_r ∈ {1..M}` solves `p^k·h_r + b·B_r ≡ 0 (mod M)` via `pow(p**k, -1, M)`;
`y_r = h_r + M/A`, factors `p + b/y_r` over first-bit-1 rotations, exact
`Fraction` arithmetic only, compared against `M` by exact comparison.
One primitive necklace (min-rotation canonical) per rotation class.

## Reproduction: p = 3, 5, 7 through m ≤ 18

No falsifier. Conventions agree.

| p | primitive necklaces (m≤18) | nonintegral checked | integral skipped |
|---|---|---|---|
| 3 | 31041 | 31037 | 4 |
| 5 | 31041 | 31037 | 4 |
| 7 | 31041 | 31040 | 1 |

Primitive count cross-checks the necklace formula exactly
(e.g. m=19: 27594, m=20: 52377, matching the repo's m≤20 total of 111012).

## Broadened sweep (m-major staircase, lexicographic `(m, p, necklace)`)

Frozen completed bounds (all primitive necklaces, nonintegral checked):

- m = 1–14: every odd p = 3..101 (50 values) — 126,834 checks
- m = 15–18: every odd p = 3..31 (15 values) — 427,560 checks
- m = 19–22: p = 3, 5, 7 — 1,111,158 checks

Total: **1,665,552** nonintegral necklaces, **zero falsifiers**.
Congruence `p^k·h_r + b·B_r ≡ 0 (mod M)` re-verified on samples; no
`D = 0` encountered (impossible for odd p).

## Audit: the `h = M when residue is 0` convention

Dead code for every word in scope — it cannot occur. Proof: factor
`B_r = 2^{j_min}·(odd)`, where `j_min` is the rotation's leading-zero count
(the lowest set bit contributes an odd term, all higher terms are even).
Hence `v_2(B_r) = j_min < m`, so `M = 2^m ∤ B_r` and, `p^k` being invertible
mod `M`, the residue `-b·B_r·(p^k)^{-1} mod M` is never 0 when `k ≥ 1`.
Empirically: 0 occurrences over the full sweep (~20M rotations).
It would trigger only for the excluded all-zero word (`B = 0`).
Integrality was also empirically rotation-invariant (0 mismatches), so
skipping on `A | B_0` is equivalent to skipping on any rotation.

## Program identity

- [pb_falsify.py](/tmp/cp25-pb-falsify/pb_falsify.py) SHA-256:
  `04348601…cd55ba56` (full: `043486014b7a66bc8ac6c39d45d5c3060f0b3ebfc0ce3f934b9403e2cd55ba56`)
- [pb_stair.py](/tmp/cp25-pb-falsify/pb_stair.py) SHA-256:
  `1c5dc4579f91546b23fbd9735425627d4c51abe8d493c6a9901df1ac0d9420c9`
- Raw outputs: `/tmp/cp25-pb-falsify/stair18.json`, `/tmp/cp25-pb-falsify/stair22.json`
  (228.5 s for the full staircase).

No falsifier exists to print; hence no `B_r, h_r, y_r` table or product
fraction is owed. Spot examples behaved with wide margins
(e.g. p=3, `(0,0,0,1)`: product 256/81 < 16; p=101, `(0,1)`: 10104/101 > 4).

Finite verification is not proof: this exhausts only the stated staircase
(m≤14 for p≤101, m≤18 for p≤31, m≤22 for p∈{3,5,7}) and says nothing about
larger words, where near-misses `p^k ≈ 2^m` (small `A`) remain the
most plausible place for a violation.

## Verdict

**BOUNDED-PASS**
