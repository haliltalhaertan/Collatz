# CP23-salvage report: what the programme owns if Collatz is out of reach

Label key: [PROOF] [EXACT COMPUTATION] [CONJECTURE] [FAIL] [JUDGEMENT].
Scope assumption for this session only: Collatz is out of reach; no claim below touches it.

## Gate
[EXACT COMPUTATION] Ecal(4,3) = 40/3. [EXACT COMPUTATION] Ecal(5,2) = 31/3.
Both reproduced from scratch (`salvage_gate.py`). Gate: PASS.

## Asset novelty assessment (reasoned from the mathematics, no literature search available)
- A1 affine form: (a) certainly known/classical.
- A2 2-adic isometry: (c) unclear — expected reformulation of classical parity-vector isometry.
- A3 collision criterion: (b) plausibly new — exact collision <=> mod-3^k congruence, verified to m=16.
- A4 B never 0 mod 3: (c) leaning (b)-as-lemma — trivial proof, value is in enabling A3's counting use.
- A5 parent identity: (c) — standard first-step conditioning in programme-specific normalisation.
- A6 cap stabilisation: (b) plausibly new — sharp threshold 2^r >= 3^k - 1, verified on 5 (m,k) pairs.
- A7 forced frequency index: (c) — correct method-internal no-go, audience is the programme itself.
- A8 energy identity: (c) — original by construction (Ecal is programme-owned); interest contingent on Ecal.
- A9 91-interval witness: (b) original artifact, narrow audience (delimits the charging approach).
- A10 audit methodology: process asset, not a theorem; case-study value only.

## Strongest standalone theorem (A3 + A4 + count corollary)
Fix m >= 1, H(x) = (3x+1)/2 (x odd), x/2 (x even). For odd h < 2^m let k(h) =
odd-count along m steps, e(h) = H^m(h), B(h) = 2^m e(h) - 3^{k(h)} h.
(i) [PROOF] B(h) is odd and B(h) not = 0 mod 3.
(ii) [PROOF] Same stratum k: e(h) = e(h') => B(h) = B(h') mod 3^k (one line of algebra).
(iii) [EXACT COMPUTATION, programme claims PROOF/T7] Converse holds: verified for all
same-weight pairs to m = 8 plus residue-class scan to m = 16 with zero failures.
Corollary: [EXACT COMPUTATION] per stratum, #distinct endpoints = #occupied B-classes mod 3^k
<= 2*3^{k-1}; saturation 100% observed at (m,k) = (12,4) (54/54).
Status of (iii)'s proof: reduced here to excluding endpoint gaps of exactly +-3^k
(from 2^m | (h-h'+t)); that last exclusion step was NOT re-derived — it is the load-bearing
lemma to check before publication. theorem_verified (computational): true.

## Outside interest
[JUDGEMENT] The B_w object generalises verbatim to (px+q)/2-type maps with p-adic collision
criteria, i.e. itinerary-collision lemmas for piecewise-affine dynamics — that is the real
export market, not Collatz. 2-adic phrasing plugs into the Bernstein-Lagarias conjugacy
audience; Christoffel/Sturmian extremality into combinatorics-on-words. All contingent on a
literature check.

## Methodology
[JUDGEMENT] A10 is a case study (63 killed paths, one caught false [PROOF]), writable for the
ML-for-math / experimental-math workshop audience, but n = 1 programme with no control —
ranked below the theorem note.

## Ranked recommendation
1. Short note: collision criterion + reachability + count corollary (+ A6 as section 2), arXiv
   preprint with dataset; audience: number theory / arithmetic dynamics.
2. Dataset release (239 exact rows + witnesses).
3. Lean formalisation of A1-A4 (trust repair for AI-only provenance; high cost).
4. Methodology case study.
5. Ecal identity paper — only if Ecal gains an audience.
Top pick: item 1, because it is the most surprising, most verified, most narrowly stated claim.

## Soundness note on the intended chain
[JUDGEMENT] The lead's "no measurable progress toward Collatz" reads about right: 239 rows and
an identity are progress toward a mixing lemma, not toward a counterexample constraint, and
chain step 3 (mixing => nowhere to hide) is exactly where B1 bites. B1/B2 stand; neither was
weakened by anything found in this session.
