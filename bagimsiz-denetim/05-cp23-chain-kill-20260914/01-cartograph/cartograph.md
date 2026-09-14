# CP23 Cartographer report — the real distance from the mixing target to Collatz

Rule for this file: every substantive sentence carries one of
[PROOF] [EXACT COMPUTATION] [CONJECTURE] [FAIL] [JUDGEMENT].
Grades for chain links use a separate vocabulary:
[PROVED] / [CONJECTURED, formulated] / [NOT EVEN FORMULATED] / [KNOWN BARRIER].

Programme assets A1–A10 are taken as reported inputs to this cartography.
[JUDGEMENT] I did not re-verify A1–A8 proofs or re-run the 239-row table in this session; I re-implemented the Ecal definition from scratch and reproduced both gate values exactly (see gate.py), which is the only independence check this session claims.

## 0. Grounding gate

- [EXACT COMPUTATION] Ecal(4,3) = 40/3, reproduced from scratch with Fraction arithmetic (gate.py).
- [EXACT COMPUTATION] Ecal(5,2) = 31/3, reproduced from scratch with Fraction arithmetic (gate.py).
- [EXACT COMPUTATION] Gate detail for Ecal(4,3): stratum tables are k=1:[0,1,0,0,0,0,0,0] Jr=4; k=2:[1,1,1,0,0,0,0,0] Jr=12; k=3:[0,1,0,0,1,1,0,0] Jr=4; k=4:[1,0,0,0,0,0,0,0] Jr=4, with n=(1,3,3,1), giving 4/1+12/3+4/3+4/1 = 40/3.
- [EXACT COMPUTATION] Gate detail for Ecal(5,2): k=1:[0,0,1,0] Jr=2; k=2:[1,2,1,0] Jr=8; k=3:[1,1,4,0] Jr=20; k=4:[2,0,1,1] Jr=4; k=5:[0,0,1,0] Jr=2, with n=(1,4,6,4,1), giving 2+2+10/3+1+2 = 31/3.
- [JUDGEMENT] Gate status is PASS; nothing downstream is blocked on a definition mismatch.

## 1. The complete chain (target proved ⇒ Collatz), link by link

- [CONJECTURE] Link 1 — one-step mixing inequality: for all m,s ≥ 1, Ecal(m,s+1) ≥ Ecal(m+1,s), i.e. M_merge − L_lift ≥ 0. Grade: [CONJECTURED, formulated].
- [JUDGEMENT] Link 1 is the only link the programme has actually written down with quantifiers, and its evidence is 239 exact rows with zero violations — which is support, never a theorem.
- [CONJECTURE] Link 2 — iteration to fixed-resolution decay with a rate: from Link 1, derive an explicit bound of the form Ecal(m,r) ≤ δ(m) for fixed r (or r growing slowly with m), with δ(m) → 0 at a stated rate. Grade: [NOT EVEN FORMULATED].
- [PROOF] Link 2 has no stated corollary because naive iteration does not produce it: assuming Link 1, repeated application gives only Ecal(m,r) ≥ Ecal(m+1,r−1) ≥ … ≥ Ecal(m+r−1,1) ≥ 0 (r−1 steps, lower bound 0) and Ecal(m,r) ≤ Ecal(m−1,r+1) ≤ … ≤ Ecal(1,m+r−1) = 2^(m+r−2) (upper bound exponential, hence trivial).
- [EXACT COMPUTATION] The closed form used above, Ecal(1,R) = 2^(R−1), holds because at m=1 the single odd start h=1 gives H(1)=2, a point mass, so exactly one top-bit difference is 1 and J_R = 2^(R−1).
- [FAIL] The hope "Link 1 implies Ecal(m,r) decreases in m at fixed r" is false as stated: exact values at r=2 are m=1:2, m=2:4, m=3:4, m=4:8, m=5:31/3≈10.33, m=6:38/5=7.6, so fixed-r behaviour oscillates and Link 1 is consistent with growth at fixed resolution.
- [CONJECTURE] Link 3 — upgrade from top-bit control to full mixing: J_r-based bounds imply total-variation (or all-frequency Fourier) uniformity of P_{m,k,r}/n_k over residues mod 2^r, plus the 3-adic control mod 3^k needed for Syracuse offsets. Grade: [KNOWN BARRIER].
- [PROOF] Link 3 as a naive upgrade is blocked by the programme's own proved obstruction (reported asset): some exact Fourier coefficient is ≥ 1/2, so uniform exponential decay at all frequencies is IMPOSSIBLE; J_r sees only the top-bit difference X(u)−X(u+2^{r−1}), which is one projection of the distribution, not the distribution.
- [PROOF] Link 3 is further narrowed by the programme's no-refinement result (reported asset A7): the merge-side spectra are q-periodic while the lift weight is q-antiperiodic, so no mod-N refinement of the merge side exists — the coarseness of Ecal is structural, not a placeholder.
- [CONJECTURE] Link 4 — census uniformity implies typical-orbit control: e.g. a density-one set of starting values ≤ X has typical parity statistics / almost-bounded first passage (the Tao-type "almost all" conclusion). Grade: [NOT EVEN FORMULATED].
- [JUDGEMENT] Link 4 has no programme-side transfer lemma with quantifiers (rate in ⇒ density conclusion out); the literature version of this step exists but uses different, fully quantitative machinery with explicit decay, union bounds over scales, and stopping-time analysis that this programme has not reproduced.
- [CONJECTURE] Link 5 — typical behaviour excludes divergent orbits: no orbit is unbounded without cycling. Grade: [KNOWN BARRIER].
- [JUDGEMENT] Link 5 is barrier B1 (measure-zero escape): a density-one theorem is logically compatible with one unbounded orbit, because one orbit has density zero; ruling out a single orbit needs a per-orbit certificate, which a census average cannot supply.
- [CONJECTURE] Link 6 — typical behaviour (or census uniformity) excludes nontrivial cycles: no p ≥ 1 and x with H^p(x) = x except the known 1–2 loop. Grade: [KNOWN BARRIER].
- [JUDGEMENT] Link 6 fails on method mismatch, not just measure: an exact return equation H^p(x) = x is a Diophantine condition handled in the literature by transcendence/approximation tools, and no statistical-decay hypothesis in this programme constrains exact return; no bridge has been formulated.
- [CONJECTURE] Link 7 — finite windows control one infinite object: bounds uniform over all scales (m → ∞, r → ∞ jointly) trap a single fixed orbit forever. Grade: [KNOWN BARRIER].
- [JUDGEMENT] Link 7 is barrier B2 / the programme's own CP18 wall: finitely much window information cannot separate "each finite pattern occurs for some start" from "one start realises all patterns jointly," so any finite-(m,r) input needs a uniformity-across-scales argument that has not been formulated.
- [PROOF] Link 8 — assembly: (no nontrivial cycles AND no divergent orbits) implies every positive integer reaches 1. Grade: [PROVED].
- [PROOF] Link 8 holds by the classical pigeonhole argument: the forward orbit of any x ∈ N is infinite unless it hits 1; if it is bounded and infinite it repeats a value (hence contains a cycle), and if it never repeats its values are infinitely many distinct positive integers, hence unbounded; so excluding both alternatives leaves reaching 1 as the only option.

## 2. Weakest link (exact statement)

- [JUDGEMENT] The weakest link is the statistical-to-single-orbit passage (Links 5+7 fused; the lead's "step 3"): even perfect mixing would not touch a single counterexample, and this step has never been given quantifiers.
- [CONJECTURE] The exact statement that would be needed — call it the Transfer Thesis — is: there exist a fixed resolution r ≥ 1, a function δ(m) → 0, and a constant c > 0 such that (∀ large m: Ecal(m,r) ≤ δ(m)) implies every H-orbit reaches 1; equivalently, contrapositively, if x0 has an H-orbit that never hits 1 then lim sup_{m→∞} Ecal(m,r) ≥ c(x0) > 0 (or the same with an explicit weighted/stratum-localised variant that names how x0's orbit imprints on the census).
- [FAIL] No implication of that shape — with explicit quantifiers over x0, m, r, δ, c — exists anywhere in this programme; the lead's "mixing implies no counterexample" is a hope, not a conjecture, because a conjecture requires exactly the quantifiers above and they were never written.
- [JUDGEMENT] To my knowledge the literature contains no such implication either, and Tao's work has the opposite quantifiers by design (density-one conclusion from quantitative equidistribution); barriers B1 (one orbit has density zero) and B2 (finite windows vs one infinite joint realisation) explain why no purely statistical hypothesis of Ecal type can yield it without a fundamentally new per-orbit idea.
- [JUDGEMENT] The lead's suspicion is therefore confirmed and, if anything, understated: step 3 is not a theorem, not a conjecture, but an unformulated hope, and it sits behind two further unformulated steps (Links 2 and 4), so the chain has three missing links before the two known ceilings are even reached.

## 3. What a proof of the target actually buys (derivation)

- [PROOF] Assume Link 1 for all m,s; fix (m,r) with r ≥ 2 and apply it r−1 times: Ecal(m,r) ≥ Ecal(m+1,r−1) ≥ … ≥ Ecal(m+r−1,1) ≥ 0, since every Ecal value is a sum of nonnegative terms.
- [PROOF] Apply Link 1 backwards the same way: Ecal(m,r) ≤ Ecal(m−1,r+1) ≤ … ≤ Ecal(1,m+r−1), and the endpoint equals 2^(m+r−2) by the point-mass computation, so the only upper bound Link 1 yields grows exponentially in m+r and is trivially true.
- [PROOF] Hence all Link 1 implies, by itself, is that along each diagonal m+r = const the Ecal values form a bounded monotone sequence, which therefore converges to some limit L ≥ 0; the limit is unidentified and may be large positive, and no rate of approach follows from monotonicity alone.
- [EXACT COMPUTATION] The computed grid (m=1..8, r=1..4: e.g. row m=4 is 8/3, 8, 40/3, 32; column r=2 is 2, 4, 4, 8, 31/3, 38/5, 43/5, 176/21) shows fixed-resolution values oscillating rather than decaying, consistent with the proof above that diagonal monotonicity controls no fixed-r limit.
- [JUDGEMENT] For the target to fund any orbit conclusion it would additionally need: (a) a fixed-resolution decay Ecal(m,r) → 0 with an explicit rate δ(m); (b) an upgrade from top-bit J_r to full-distribution control, against the programme's own ≥1/2 Fourier obstruction; (c) a reweighting from 1/n_k strata to natural density over starts; (d) a Tao-shaped transfer with union bounds over ~log X scales and stopping-time analysis.
- [JUDGEMENT] A bare monotonicity (no δ at all) funds none of (a)–(d): with no rate there is nothing to insert into a union bound, with one-bit projections there is nothing to feed a total-variation argument, and with shifting resolution (r dropping as m grows) there is not even a fixed object whose limit is zero.
- [JUDGEMENT] My assessment of the lead's two barriers: B1 and B2 survive challenge — both are genuine ceilings for any statistical route — but the self-assessment "no measurable progress toward Collatz" is, if anything, slightly too kind, because Links 2–4 show the programme has not even built the road to the ceilings yet: the target as stated does not compound into the input any ceiling-crossing argument would need.

## 4. Endpoint verdict: Collatz or "almost all"?

- [JUDGEMENT] If every link up to Link 4 were somehow completed, the chain would terminate at an "almost all" statement (density-one typical boundedness / typical parity statistics), which is exactly the endpoint Tao (2019/2022, "Almost all orbits of the Collatz map attain almost bounded values") already owns with stronger, published machinery.
- [JUDGEMENT] Links 5–7 show that the road from "almost all" to "all" needs a new per-orbit / infinite-joint idea that equidistribution by itself cannot provide; nothing in A1–A10 proposes one, and A9 (caps+supports+masses+integrality do not suffice) plus the Fourier obstruction actively shrink the space where one could hide.
- [JUDGEMENT] Verdict: the chain terminates at "almost all," not at Collatz, and the programme's best possible outcome without retargeting is a weaker, redundant special case of a result already in the literature — most plausibly a new elementary proof of a coarse one-bit equidistribution lemma, which is a legitimate analytic-combinatorics result but not progress to Collatz and should be published (if at all) under that honest title.
- [JUDGEMENT] "This programme cannot reach its stated goal and should retarget" is a defensible first-class conclusion here: retarget to explicit-rate one-bit equidistribution, or to the reachable-residue programme (A3/A4), or to formalising Links 2–4 as stated open problems — and stop carrying Collatz in the title.

## 5. Honest translation of the current data

- [EXACT COMPUTATION] Concrete instance (m=4): the 8 odd starts 1,3,…,15 run 4 H-steps to endpoints 1,2,1,13,17,20,8,80 with odd-counts 2,2,1,3,3,3,2,4; grouped mod 8 this is exactly the P_{4,k,3} table in section 0, whose weighted top-bit discrepancy is Ecal(4,3)=40/3.
- [EXACT COMPUTATION] Concrete instance (m=5): the 16 odd starts 1,3,…,31 run 5 H-steps to endpoints 2,1,2,20,26,10,4,40,5,17,2,20,22,71,26,242; grouped mod 4 this is the P_{5,k,2} table in section 0, whose weighted top-bit discrepancy is Ecal(5,2)=31/3.
- [EXACT COMPUTATION] The one-step instance pairing the two gates is Ecal(4,3)=40/3 ≥ Ecal(5,2)=31/3: after one more Collatz step and one coarser bit of resolution, the coarse non-uniformity of these two tiny censuses (starts <16 vs <32) did not go up.
- [JUDGEMENT] What "239 rows, 0 violations" literally says: for 239 tested (m,s) pairs at small m (censuses over odd starts below 2^m — hundreds to thousands of starts), the same shifting-resolution non-increase held every time.
- [JUDGEMENT] What it does not say: anything about any integer beyond the tested windows, anything about the 5th/6th/… iterate of a fixed start beyond the window length, anything about uniformity of residues in general (a finite table is never a uniform theorem), and a fortiori anything about whether a divergent orbit or a nontrivial cycle exists.
- [JUDGEMENT] A single counterexample orbit, if one existed, would be one infinite object far outside these small windows, and 239 finite-window inequalities cannot see it — that is just B1+B2 restated for the data, and it is why the table, while genuine evidence for Link 1, carries zero bits of Collatz information on its own.
