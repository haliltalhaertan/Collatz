# CP24 Scope Audit — what is actually justified

Scope: current workspace only; `inputs/` treated as UNTRUSTED claims (read, never modified).
No web, no literature, no novelty claims. Finite runs corroborate; only proofs prove.
`checks.py` (stdlib, exact integers/`Fraction`) ran: **ALL_OK** (exit 0).

Gate (reproduced exactly): 128 odd `h < 256` (NOT 256); affine identity `2^8·e = 3^k·h + B`
with `B` odd, `B ≢ 0 mod 3`, 0 fails; `Ecal₊(4,3) = 40/3`, `Ecal₊(5,2) = 31/3`;
`Hm: 5 → 7 → 10 → 5` closed.

Conventions: `H_b(x) = (3x+b)/2` (odd `x`), `x/2` (even `x`), `b = ±1`.
Word `w` = parities over `m` steps, `k = |w|`, `B_0 = 0`, `B_{i+1} = 3^{w_i}·B_i + w_i·2^i`
(`B_w ≥ 1` whenever `w_0 = 1`), affine law `2^m·H_b^m(h) = 3^k·h + b·B_w`.
`n_k = C(m-1,k-1)`, `J_r(P) = 2^{r-1}·Σ_{u<2^{r-1}}(P[u]-P[u+2^{r-1}])²`, `Ecal = Σ_k J_r(P_k)/n_k`.

## 1. Reflection `H₋` at `2^m−h` vs `H₊` at `h` — PROVED

Lemma A (negation conjugacy). `H₋(−x) = −H₊(x)` for all integers `x`.
*Proof.* `x` even: both sides `−x/2`. `x` odd: `H₋(−x) = (3(−x)−1)/2 = −(3x+1)/2 = −H₊(x)`. ∎

Lemma B (finite-horizon periodicity). Fix `b`. If `y₁ ≡ y₂ mod 2^m` then their length-`m`
parity words agree. *Proof.* Induction: same residue mod 2 gives same first parity; if
`y₁ ≡ y₂ mod 2^t` with the same parity, then `H_b(y₁) ≡ H_b(y₂) mod 2^{t-1}` (even case:
`(y₁−y₂)/2`; odd case: `3(y₁−y₂)/2`, `3` odd). Holds for all integers, both signs. ∎

Theorem 1 (reflection). Let `m ≥ 1`, `h` odd, `1 ≤ h < 2^m`, `hs = 2^m − h`. Let
`(wp,kp,ep)`, `(wm,km,em)` be the word/weight/endpoint of `H₊` from `h` and `H₋` from `hs`.
With `Bp`, `Bm` the signed offsets (`2^m·e = 3^k·h + b·B_w`, unsigned `B_w` from the word):
`wm = wp`, `km = kp`, `Bm = −Bp`, `em + ep = 3^k`.
*Proof.* By Lemma A inductively, `H₋^i(−h) = −H₊^i(h)`; negation preserves mod-2 parity,
so the word from `−h` under `H₋` equals `wp`. Since `hs ≡ −h mod 2^m`, Lemma B gives
`wm = wp` (hence `km = kp =: k`), with common unsigned `B_w`. The two affine laws read
`2^m·ep = 3^k·h + B_w` and `2^m·em = 3^k·hs − B_w`; adding and using `h + hs = 2^m`
gives `em + ep = 3^k` and signed `Bm = −Bp`. ∎ (`hs` is odd, an involution without
fixed points — the pairing has no fixed `h`.)

Corollary (Ecal blindness, proved — not just observed). Per stratum `k`,
`{em} = {3^k − ep}` as multisets, i.e. `P⁻_{m,k,r}(z) = P⁺_{m,k,r}(c_k − z)` with
`c_k = 3^k mod 2^r` odd. The map `φ(z) = c_k − z mod 2^r` sends complementary pairs
`{u, u+2^{r-1}}` to complementary pairs (adding `2^{r-1}` commutes with `φ`), so the
multiset of half-differences — hence every `J_r` and `Ecal` — is identical for the two
maps at every `(m,r)`. Corroborated: `(4,3) = 40/3`, `(5,2) = 31/3`, `(6,2) = 38/5`,
pairing 0 bad at `m = 4, 6, 8`; e.g. Q1 cross-identity
`S⁻(m) = −2^m·T⁺(m) + S⁺(m)` follows from Theorem 1 by summing over the bijection.

Valid invariant class: functionals of the per-`k` endpoint data invariant under
`z ↦ c_k − z` with `c_k` odd (per-`k` odd translation-reflection), e.g. `Ecal`,
`|B|`-multisets, negated-`B` multisets. A functional is in the blind class only if it
factors through such invariants — check per functional, do not assume.

What this DOES NOT imply (explicit non-claims):
- (a) Nothing about same-`h` behaviour: `k⁺(h) ≠ k⁻(h)` for 110/128 odd `h` at `m = 8`.
  The pairing is cross-`h` (`h ↔ 2^m−h`), not same-`h`.
- (b) Signed functionals separate the maps: Q1/Q2/Q4 values differ (`Q4(6)`: 100640 vs 37920).
  A `3n−1`-true lemma stays usable as an auxiliary lemma inside a `3n+1` argument the
  moment it is combined with sign-sensitive hypotheses (sign of `B`, `D > 0` vs `D < 0`,
  dropping `3^k < 2^m` with `+B`); the filter is a one-sided kill, not a ban on `Ecal`.
- (c) Identical `Ecal` values do NOT prove any monotonicity conjecture, even proved in
  general: equality across maps is orthogonal to growth in `m`/`r`. Finitely many agreeing
  pairs prove nothing in either direction.
- (d) No impossibility theorem for modular methods: only the invariant class is blind.

## 2. Cycle self-consistency — PROVED equivalent (positivity is the only extra)

Setup: abstract word `w`, `w_0 = 1`, `k = |w|`, `B_w` from the recurrence, `D = 2^m − 3^k`
(always nonzero and odd: `2^m` even, `3^k` odd; `gcd(D,6) = 1`). Candidate
`x = b·B_w/D`. Question: does integral positive `x` automatically satisfy
word`(x) = w` and `H_b^m(x) = x`?

Lemma C (parity-vector bijection). Odd residues mod `2^m` are in bijection with words of
length `m` with `w_0 = 1`, via the length-`m` word. *Proof.* Induction on `m` (`m = 1`
trivial). Given the claim at `m`, each realised word lifts to two residues mod `2^{m+1}`
whose first-`m` words agree (Lemma B); their `(m+1)`-st parities differ because the affine
law gives `H_b^m(h+2^m) = e + 3^k` with `3^k` odd. So both one-bit extensions occur,
uniquely. ∎

Theorem 2. Let `w_0 = 1`, `b = ±1`. If `D ∣ b·B_w` so `x = b·B_w/D` is an integer (any
sign), then word`_m(x) = w` and `H_b^m(x) = x` (period dividing `m`).
*Proof.* Let `h` be the unique odd residue with word `w` (Lemma C), `e = H_b^m(h)`:
`2^m·e = 3^k·h + b·B_w`. The candidate satisfies `(2^m − 3^k)·x = b·B_w`. Subtracting:
`2^m·(e−x) = 3^k·(h−x)`, so `2^m ∣ 3^k·(h−x)`; `3^k` odd gives `x ≡ h mod 2^m`.
Lemma B: word`(x) = w` (and `x` is automatically odd). The affine law along `x`'s true
word `w` then gives `2^m·H_b^m(x) = 3^k·x + b·B_w = 2^m·x`. ∎

Verdict on "self-consistency is strictly stronger": REFUTED for its word/endpoint content —
divisibility and full integer self-consistency are equivalent (both signs). The only
strictly-stronger component is the positivity filter `x > 0` (i.e. for `b = +1`, `D > 0`;
for `b = −1`, `D < 0`, since `B_w > 0`). The `task1.json` pattern `div == self_any` in
every row `m ≤ 20` is exactly what Theorem 2 predicts — not independent evidence — and
two agreeing implementations are corroboration, not proof. Exact instances checked:
`Hp`: `(1,0)→x=1`, `(1,0,1,0)→x=1`, `(1,1)→x=−1` (negative fixed point, word matches);
`Hm`: `(1,1,0)→x=5`, `(1,0,1)→x=7` (the `5→7→10→5` cycle), `(1,1,1)→x=1`; exhaustive
`m ≤ 8` both signs: `div == self_any` everywhere, positives a strict subset.

## 3. Ecal normalisation — PROVED identity; growth claims restricted

With `p_k = P_k/n_k` and `π_k = n_k/2^{m-1}` (`Σ_k n_k = 2^{m-1}` over odd residues):
`J_r` is homogeneous of degree 2, so `J_r(P_k) = n_k²·J_r(p_k)` and

`Ecal = Σ_k n_k·J_r(p_k) = 2^{m-1}·Σ_k π_k·J_r(p_k)`.

Verified exactly: `(4,3)`: `Ecal = 40/3`, normalised `5/3`; `(5,2)`: `Ecal = 31/3`,
normalised `31/48`; each `J_r(p_k) ≤ 2^{r-1}` (mass on one residue), so
`Ecal ≤ 2^{m+r-2}` always. Consequences: unnormalised `Ecal` growth in `m` at fixed `r`
may only reflect the `2^{m-1}` prefactor — mixing is a claim about the NORMALISED
mixture `Σ_k π_k J_r(p_k) → 0` per fixed `r`, never about raw `Ecal`. Fixed-`r`
normalised decay says nothing about finer scales; any fixed `m+r` diagonal is a finite
set of pairs from which no convergence theorem follows. No mixing theorem is proved here.

## 4. Target-probe verdict (bounded, finite — nothing infinite established)

Established (exact, reproduced): gate triple; `Hp`, `m ≤ 12`: every `D > 0` odd-`q`
self-consistent pass has `q = 1` (only at even `m`, alternating word — the trivial fixed
point), zero nontrivial; sieve is non-vacuous: `Hm` `m = 3` gives `{1, 5, 7}`,
`F5` witness `(1,1,0,0,0)`, `q = 1`, cycle `1→3→8→4→2→1` closed.
Unfinished: everything else — `m > 12` untouched, no uniform bound, no dropping lemma,
no tail bound, no density limit. Classical stopping-density results (Terras/Everett-type)
are NOT new and may only be reproved with attribution, never claimed.

ONE bounded validation task (only): Terras single-step dropping count at `m = 16`, exact
integers — drop-count `#{odd h < 2^16 : Hp^16(h) < h}` by direct trajectory scan AND by an
independent per-word `B_w`-maxima route, requiring agreement.
Acceptance: both routes output exactly `27823/32768` (observed finite value, not a theorem;
`m = 8` baseline `94/128`). Any density/limit claim from it is explicitly out of scope.

## Corrections table (inputs/ left unchanged)

| # | Location | Claim / defect | Correction |
|---|----------|----------------|------------|
| 1 | brief/gates | "256 odd h below 256" risk | 128 odd residues; all gates use 128 |
| 2 | cycle prior claim | "self-consistency strictly stronger" | Equivalent given integrality (Thm 2); only `x>0` is extra |
| 3 | `task1.json` reading | `div==self` surprises / proves | Predicted by Thm 2; corroboration only |
| 4 | `task1.py` | hardcoded abs path; numpy int64 "exact" | fragility: use repo-relative path, pure-Python big ints |
| 5 | asym finite runs | pairing/Ecal equality at sampled `(m,r)` | upgraded to proofs (Thm 1 + Corollary); samples kept as checks |
| 6 | monotonicity talk | equal Ecal ⇒ trend true/false | orthogonal; neither direction follows |
| 7 | filter talk | blind ⇒ no modular `3n+1` argument | one-sided kill only; sign-sensitive combinations escape |
| 8 | diagonals | finite `m+r` values ⇒ convergence | finite only; mixing needs normalised `m→∞` bounds per fixed `r` |
| 9 | probe | `m≤12` sieve ⇒ cycle claim | bounded observation; `m>12` open; controls only show non-vacuity |
| 10 | my `checks.py` draft | expected `Hm (1,1,1)→−1` | is `+1` (`Hm(1)=1`); fixed, ALL_OK |

Proved: Lemma A, B, C; Thm 1 (reflection + endpoint sum); Ecal-blindness corollary
(all `(m,r)`); Q1 cross-identity (instance of Thm 1); Thm 2 (divisibility ⇔
self-consistency, both signs); normalisation identity + `J_r(p_k)` bound.
Unsupported (explicit gaps): monotonicity of `Ecal`; any mixing/convergence; any
cycle exclusion beyond the bounded sieve; any novelty/attribution claim (no literature).
