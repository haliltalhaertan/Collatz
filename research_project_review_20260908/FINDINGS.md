# Findings from the whole-project reassessment

8 September 2026. Existing research files were read without modification. Findings concern specific statements or proposed experiments; none is a blanket rejection of the project.

## F1: Cancel the same-checkpoint/global-minimum comparison

The recent conversational proposal retained S={20+27k} while relaxing the target to any smaller integer under global-minimum reasoning. Every n in S is2 mod3. An even n has smaller equivalent n/2. An odd n has positive odd m=(2n-1)/3<n and T(m)=n. Therefore no member of S can be the global least exception at all. The proposed comparison would be trivially successful and scientifically confounded.

This does not invalidate any smaller-S certificate: the least exceptional member within S need not be the least exceptional integer globally. All current55,210/10,326 counts retain their original minimum-in-S meaning. A separate global-minimum search would need its own complete domain, initially reducible to3 or7 mod12, not merely S.

## F2: Positive Laplace domination is one-way

research_sol_20260908/PRINCIPAL_ANALYSIS.md repairs the earlier 'equivalent' wording: |E W|<=E|W|<=E exp(-lambda N). Failure of the positive majorant does not refute complex cancellation. Old copied XUB input packages retain the older wording and must not override the repair. Even the complex C/R upper bound does not supply a nonzero profile, polynomial lower bound, or Collatz convergence.

## F3: Supplementary D1 audit conflates weak and exact realization

bagimsiz-denetim/13-d1-denetim/DENETIM_RAPORU.md:232–234 and the corresponding BAS_ARASTIRMACI_VERDICT.md supplementary Finding D assert that r_L always equals the least positive exact valuation-word realizer.

Counterexample: w=(1) gives A1=B1=1 and r1=-3^-1 mod2=1. But v2(3*1+1)=2, not1. The least exact start is3, with v2(10)=1. Thus weak divisibility residue r_L cannot always replace the exact terminal-parity lift R_L.

The test in09_realizer_bedeli.py:27–29 rejects only v2(3*x+1)<a_k. It checks weak divisibility, not equality. Its green result does not support the stronger sentence. The same full audit elsewhere distinguishes R_L from r_L, and inspected downstream D1-D/D1-E summaries retain the interior/terminal distinction. No downstream load-bearing failure was established by this review.

## F4: Supplementary plateau typicality and domain overclaims

09_realizer_bedeli.py:40 labels random.choice([1,1,2]) alpha-typical. Its mean is4/3, not log_2(3); the finite table cannot establish the printed alpha-limit. This numerical assertion should not be used as evidence for the separate audited injury-gap identity.

Likewise 'infinite plateau iff divergent noncycling orbit' requires the specified survivor/injectivity conditions. The constant valuation2 schedule realizes the trivial odd fixed orbit1 and eventually constant residues. General stabilization supplies an ordinary orbit; divergence needs additional assumptions.

## F5: Some summary files omit theorem domains

The reconstructed CP17 master summary displays the harmonic theorem without repeating injectivity. The actual CP17_FINAL_STANDALONE_PROOF_V3.md Section1 explicitly requires a positive injective odd-only orbit and explicitly does not exclude nontrivial cycles. Use the original theorem domain, not the abbreviated summary. No defect in that original theorem was established here.

## F6: Archive bytes match, but literal state paths are misencoded

The stock tools/verify_handoff.py stops at the detached-checkout branch mismatch: expected main. No canonical PASS is claimed.

Separate read-only snapshot checks pass archive SHA256, byte size,1008 member count, CRC,85/85 repository hashes and the22-entry journal chain. All81 literal archive dependency paths in the root state fail lookup because of character encoding corruption. A diagnostic cp1252-to-UTF8 decoding locates81/81 entries and their bytes match all81 stored hashes. This diagnoses path metadata, not missing mathematical contents. No root state, archive or validator was repaired.

README's834-member archive/E7-awaiting-authorization summary is stale relative to the actual build and current handoff. B4 V2 is closed after pre-mathematics input-integrity failure; that failure is not a mathematical refutation.

## Review limits

No claim of re-proving all archived theorems, formally checking every proof, exhaustively verifying every local certificate, reading every duplicate/nested artifact, or checking live Drive/GitHub publication. The CP15 recovery DOCX has no text in its document XML; it cannot supply a scientific summary. CP01/CP05 source-status gaps and reconstructed CP14 material remain explicitly marked.
