# CP21 — Literature Sweep (lead researcher, 2026-09-14)

Method: web search + abstract/HTML extraction. No claim of exhaustiveness. All items below are
NEW relative to the archive's folder-08 literature sweep (2026-08-26) unless marked "known".
Novelty verdicts here are **[NO EXACT MATCH FOUND]**-style at best; nothing is certified.

---

## L1. **Fernández & Ibáñez, "Christoffel words as extremal structures in Collatz dynamics"**
arXiv:2607.24844 [math.DS], 24 Jul 2026, 18 pages. MSC 11B37, 11B83, 37B10, 37B20.

**Claim.** On binary parity words of length N with exactly r ones (set `D_{N,r}`), with `C(d)` the
Terras-style functional giving the explicit iterate and `C_min(d)` its minimum over the rotation
class, **Christoffel words are, up to rotation, the UNIQUE maximizers of `C_min`**. Consequences
claimed: restrictions on nontrivial cycles, and **explicit lower bounds for the minimum element of
an orbit in terms of its length and the proportion of odd iterates**.

**Why this matters to us — three distinct reasons.**

1. **Apparent tension with CP06, which is NOT a contradiction — resolve it explicitly.**
   CP06 (2026-08-14) *falsified* Christoffel/mechanical extremality with exact counterexamples:
   `R_4(1101)=11 > R_4(1110)=7` and `R_5(11110)=15 > R_5(11101)=7`. That was for the **least
   modular realizer** `R_j(v)` — a 2-adic inverse-residue object. This paper's extremal object is
   **`C_min`, an Archimedean functional on the rotation class**. Different functional, different
   extremality. The archive must record this distinction or a future reader will think one of the
   two is wrong. ACTION: add a note to the CP06 findings.

2. **Direct overlap with CP19 Task 3 — novelty risk, must be checked.**
   CP19 T3 (frozen, `[PROVED][AUDITED][FROZEN]`) proves: a positive injective critical block of
   length r forces `N >= 2^{floor(alpha*l)}(r-2l)/(l+1) - 2r/3`, and with `l = floor(log2 r)`,
   `r >= 16`: `N >= r^{1+log_2 3}/(24 log_2 r) - 2r/3`.
   This paper derives "explicit bounds for the minimum element of an orbit in terms of its length
   and the proportion of odd iterates" — the SAME shape of statement.
   ACTION (high priority): obtain the PDF, extract their explicit bound, and compare it
   quantitatively against CP19 T3 at matching (r, density). Three possible outcomes, all
   actionable: (a) theirs is weaker => CP19 T3's novelty strengthened; (b) comparable => CP19 T3 is
   [CLOSE PRIOR ART], the archive's novelty language must be downgraded; (c) theirs is stronger =>
   CP19 T3 is superseded and we should cite rather than re-derive.

3. **Machinery transfer.** Our whole programme leans on Sturmian/Christoffel structure (the phase
   word `g_k = F_{k+1}-F_k` has factor complexity `r+1`). A published uniqueness-of-maximizer
   theorem for balanced words is exactly the kind of rigidity statement the Round-8 charging
   argument lacks. Worth reading for technique even if the bound comparison goes against us.

---

## L2. **The Collatz Conjecture Challenge (ccchallenge.org)** — live Lean formalisation project
375 catalogued literature entries; 4 papers currently being formalised; 6 formalisations ready to
be audited; 0 being audited. Community-run, "formalising the Collatz literature, one paper at a time".

**Why this matters.** This is the concrete answer to the standing methodological gap the archive
itself flags: *"No human or Lean verification anywhere; AI-AI audit loop explicitly flagged as its
own limit."* (independent-audit layer, folder 16 / era-E digest).

The most valuable single action available to this programme is not another research round — it is
formalising the **CP20 Task 6 + Task 7 pressure clamp** (the alphabet-independent factor-complexity
lower bound + thermodynamic upper bound, giving `kappa >= alpha/h_infinity > 2.784`). It is the most
self-contained and most load-bearing frozen result we have. If it is right, we have something
citable; if it is wrong, everything built above it is suspect. A third party's proof assistant
breaks the AI-AI loop in a way no further Muse round can.

Note also: they have **6 formalisations ready to be audited and 0 auditors**. This programme has a
mature zero-trust audit methodology (`DENETCI_PROMPTU.md`, the T-S-U-K-I-O protocol). Offering
audit capacity is a low-cost way to enter the community with credibility before submitting our own.

---

## L3. **Knight, "Collatz high cycles do not exist"**, Discrete Mathematics 349(3), art. 114812 (2026)
Listed on ccchallenge as **being formalised**. Cycle-exclusion result.
**Relevance:** the archive's cycle side (Side B) is untouched and explicitly open everywhere.
ACTION: read; check whether it closes any branch the archive still lists as open, and whether its
method interacts with CP19 T3 / the Christoffel paper's cycle restrictions.

---

## L4. **Chang, "Exploring Collatz Dynamics with Human-LLM Collaboration"**, arXiv:2603.11066 **v5 (Apr 2026)**
The archive scanned an EARLIER version (folder 08: 13,927 lines, 233 pp, 630 results; factor/subword/
return-word/discrepancy/kappa hits all zero). **v5 adds new material the archive has not seen:**
- second independent reduction route via a **"Sturmian obstruction" and a Carry Contamination Theorem**
- exact `(3/4)^D` survivor law, `|C_D| = 2*3^{D-1}` compatible words
- seven-block cross-core alphabet on a two-vertex digraph, **spectral radius `rho = 2 + sqrt(2)`**
- **2-adic expander with unconditional measure shrinkage `mu_2(T_j) <= 0.522^{jD}`**
- `j >= 5` non-descending exhaustion bound; terminates at a "Carry Independence Conjecture" (CIC)

**Relevance:** the phrase "Sturmian obstruction" collides head-on with our Sturmian phase-word
machinery, and an *unconditional* 2-adic measure-shrinkage statement is the kind of thing that could
either (a) duplicate part of our pressure bound, or (b) supply the missing measure-side ingredient.
CAUTION: this is a human-LLM collaboration preprint of unusual length and has not been through the
kind of audit our own material gets; treat every claim as unverified until independently checked.
ACTION: re-scan v5 specifically for the Sturmian obstruction section and the expander bound.

---

## L5. Known / already in the archive (recorded for completeness, no action)
- Tao 2022, *Almost all orbits of the Collatz map attain almost bounded values* (Forum of Math Pi 10 e12) — known; on ccchallenge "ready to be audited"; the archive already closed **direct** Tao/Si transfer negatively (`LT-CT [PROVED][AUDITED]`: Tao controls the unconditioned coefficient, we need the microcanonical fibre at exponentially small conditioning probability).
- Rozier & Terracol, arXiv:2502.00948 (2025); Tong Niu, arXiv:2605.13886 (May 2026) — both already in folder 08/09.
- Eliahou 1993 cycle-length lower bound — known.
- Terras 1976, Everett 1977, Bernstein-Lagarias 1996, Applegate-Lagarias — known, all `[KNOWN]`.

## L6. Screened and rejected (no relevance)
arXiv:2601.04289 (near-conjugacy to a circle rotation by `log_6 3` with bounded error) — the error
term is `O(1/x)` and uniformly bounded but the construction is an Archimedean reparametrisation; it
does not touch the 2-adic/microcanonical structure our lemma lives in. Also several
vixra/researchgate/academia items claiming complete proofs — not engaged with.

---

## Still NOT swept (declared gaps, same as the archive's own list)
RU/CN literature; the 2019-2026 window systematically; return-word axis; Dubickas 2009 primary text;
López-Stoll sequel; MathSciNet priority sweep. **Novelty remains uncertified.**
