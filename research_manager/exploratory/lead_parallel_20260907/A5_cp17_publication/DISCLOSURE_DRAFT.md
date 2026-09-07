# DISCLOSURE_DRAFT — code/data availability and AI-assistance statements

**These are drafts. Nothing here has been inserted into the manuscript.** The manuscript was not
modified in any way during this audit.

Everything below is factual as far as I could verify it from the files on this machine. Where I
could **not** verify something, it is marked `[AUTHOR TO CONFIRM]` — please do not ship those
brackets, and do not ship a claim the author cannot personally stand behind. Two of them concern
whether specific scripts were written by the author or by the independent auditors; that
distinction matters and must not be blurred.

---

## 1. Code and data availability — replacement for §16

### 1.1 What §16 says now, and why it must change

Current text (`.tex` line 1382, submission PDF page 20):

> "The frozen proof source is `CP17_FINAL_STANDALONE_PROOF_V3.md`. The exact coefficient certificate
> is `CP17_FINAL_RATE_CERTIFICATE_V3.py`; it certifies \(\chi_1=5/3\), \(\chi_2=15/7\),
> \(4.916563<K_{11}<4.916564\), and \(K_{17}<2.742882<3\). The frozen package includes a SHA256
> manifest and a dependency graph. The publication branch reran the coefficient certificate and
> verified the frozen package manifest before preparing this manuscript."

Three problems, in order of severity:

1. **"The frozen proof source is [another file]."** For a journal submission the manuscript *is* the
   proof. This sentence tells the referee the paper is a derivative of something else — which is
   both untrue (the proof is complete in the manuscript; the external referee verified exactly that)
   and self-defeating.
2. **Neither named file is obtainable.** No DOI, no URL, no repository, no supplementary upload.
3. **"frozen", "publication branch"** are internal version-control jargon.

### 1.2 Draft replacement

> ## Code and data availability
>
> All proofs in this paper are self-contained; no step depends on external computation.
>
> The numerical values quoted in (13.4) and (13.5) are certified by a short Python script using
> exact rational arithmetic (`fractions.Fraction`) and interval arithmetic in extended precision
> (`mpmath`). The script certifies
> \(\chi_1^{\rm Syr}=5/3\) and \(\chi_2^{\rm Syr}=15/7\) as exact rationals, and brackets
> \(4.916563<K_{11}<4.916564\) and \(K_{17}<2.742882<3\) by an interval enclosure of
> \(K_{17}=\beta_0\log 2/(3I(\alpha))\); the enclosure obtained is
> \[ 2.7428814387659418633060948379874177714629\ldots < K_{17} < 2.7428814387659418633060948379874177714629\ldots \]
> The script, its recorded output, and a SHA-256 manifest are archived at
> `[DOI — AUTHOR TO CONFIRM AFTER DEPOSIT]`.
>
> The finite enumerations reported in the course of the proof are **regression checks only**: no
> numerical experiment is used as a premise in any argument. In particular the polynomial
> collision-energy bound of Theorem 9.1 is proved analytically in Appendix C, and the finite values
> of \(\chi_n^{\rm Syr}\) are computed only to confirm the analytic bound on small cases.

### 1.3 What to deposit

The deposit is one Zenodo record (free, mints a DOI, permanent). Suggested contents:

| File | Provenance | Purpose |
|---|---|---|
| `CP17_FINAL_RATE_CERTIFICATE_V3.py` (4 287 B) | **author's** | the certificate referenced in §16; certifies `χ₁=5/3`, `χ₂=15/7`, `4.916563<K₁₁<4.916564`, `K₁₇<2.742882<3` |
| `CP17_FINAL_RATE_CERTIFICATE_V3_OUTPUT.txt` (1 607 B) | **author's** | recorded output, including the two 109-digit interval endpoints for `K₁₇` |
| `SHA256SUMS.txt` | **author's** | manifest |

Both author files are present in
`C:/Users/MDP/Downloads/CP17_EXTERNAL_REFEREE_PACKAGE_V1.zip` → `PRIMARY/`.

**Ship the deposit with an LF-normalised output file.** The independent replay found the shipped
output reproduces *content-identically* but that a Windows rerun emits CRLF where the shipped file
is LF (23 lines affected). That is a platform artefact, not a discrepancy — but a referee who runs
`diff` will see 23 changed lines and wonder. A one-line note in the deposit README pre-empts it.

---

## 2. AI-assistance declaration

### 2.1 Status

JTNB's policy (`jtnbsubmit.html`) is mandatory and specific: no AI as author, and

> *"Les auteurs doivent déclarer explicitement dans un paragraphe dédié du manuscrit soumis toute
> utilisation d'un outil d'IA ou LLM lors du processus de rédaction et expliquer les spécificités et
> la nature de ce recours (vérification orthographique, syntaxe, mise en page et, plus important
> encore, toute intervention de l'IA dans les arguments scientifiques ou les citations)."*

**The submission PDF already satisfies this** (page 20, dedicated section "Declaration on the use of
AI/LLM tools"). It is a good declaration: it names scientific-argument and citation involvement
rather than hiding behind "language editing". `CP17_MANUSCRIPT.tex` does **not** contain it — only a
`%` comment at line 1386 that produces no output. Whatever source produced the submission PDF is the
one to keep.

The draft below **strengthens** the existing text rather than replacing it, by saying *which*
results were machine-checked and *by what method* — because the honest answer here is unusually
strong evidence of diligence, and burying it wastes it.

### 2.2 Draft replacement for the existing declaration

> ## Declaration on the use of AI/LLM tools
>
> No AI system is an author or co-author of this work, and the human author takes full
> responsibility for the mathematical content, the citations, and the disclosures in this paper.
>
> Large language model tools were used throughout the development and preparation of the
> manuscript, and the use was not confined to language editing. Specifically, such tools were used
> for: exploratory mathematical reasoning and the search for candidate arguments; drafting,
> reorganisation and LaTeX preparation of the text; generation and checking of the finite
> enumerations and the exact-arithmetic certificate; literature triage and cross-checking of
> bibliographic metadata; and repeated adversarial review of the proof, in which the argument was
> re-derived from scratch and attacked for errors.
>
> Every claim retained in the paper was subsequently verified by at least one of the following: an
> exact or symbolic computation; an independent re-derivation from scratch that did not reuse the
> original derivation; or explicit hand checking. In particular:
>
> - the constant \(K_{17}=\beta_0\log2/(3I(\alpha))\) and the inequality \(K_{17}<2.742882<3\) were
>   certified with exact rational and extended-precision interval arithmetic, and recomputed
>   independently;
> - the exact values \(\chi_1^{\rm Syr}=5/3\) and \(\chi_2^{\rm Syr}=15/7\) were confirmed by direct
>   enumeration over gap tuples, by a method that does not reuse the recursion used to derive them;
> - the parity-prefix bijection (Lemma 7.1), the endpoint rectangle (Lemma 12.1), the reverse-gap
>   and prefix-cylinder inequalities, and the reachable-terminal package of Appendix B were checked
>   exhaustively on all small parameter ranges for which exhaustive checking is feasible;
> - all bibliographic entries were verified against the publishers' records of publication.
>
> These computations are regression checks and verifications; **no numerical experiment is used as a
> premise in any proof in this paper.** `[AUTHOR TO CONFIRM the four bullets above match what the
> author personally ran or personally reviewed.]`

### 2.3 Optional: acknowledging independent review

If the author wishes to state that the manuscript was independently audited before submission — and
it is a genuinely strong thing to be able to say — the accurate and modest form is:

> Before submission, the argument was independently re-derived and attacked in several adversarial
> review passes, in which no step was accepted on the basis of a prior verdict, a certificate, or a
> claim of correctness, and every load-bearing estimate was recomputed from scratch.

**Do not** name internal audit documents, verdict labels (`[VALID]`, `[PROOF VALID]`), checkpoint
identifiers, or package filenames in the manuscript. They mean nothing to a referee and read as
substitutes for the referee's own judgement. `[AUTHOR TO CONFIRM whether to include §2.3 at all —
it is optional and some editors read it as pre-emptive defensiveness.]`

---

## 3. Which parts were machine-assisted — the factual record

Recorded here **for the author's own use in answering editor questions**. This is not proposed
manuscript text.

### 3.1 The author's own certificate

| Script | Lines | What it does |
|---|---|---|
| `CP17_FINAL_RATE_CERTIFICATE_V3.py` | 4 287 B | Certifies `χ₁=5/3`, `χ₂=15/7`, `4.916563<K₁₁<4.916564`, `K₁₇<2.742882<3`. Output records `K₁₇` to 109 digits as a two-sided enclosure. |

### 3.2 Independent verification scripts — **written by the auditors, not the author**

Located at `C:/Users/MDP/collatz/repro/cp17-referee-v1/` and `C:/Users/MDP/collatz/repro/cp17/`.
Stdlib + `mpmath`/`numpy` only. **These must not be described in the manuscript as the author's
work.** If the author wants to cite them, the correct framing is "independent verification scripts
produced during pre-submission review", and they should be deposited separately or not at all.

| Script | What it checks |
|---|---|
| `cp17-referee-v1/verify1.py` | `χ_n` by direct truncated enumeration over all gap tuples with `S_n ≤ cap`. Deliberately **does not** use the certificate's periodized residue law, so it is a genuinely independent confirmation of `χ₁=5/3`, `χ₂=15/7`. Brackets both to ~1e−9. |
| `cp17-referee-v1/verify2.py` | Parity-prefix bijection (`J≤14`); endpoint rectangle (`m≤14`); first-block affine identity (`m≤11`); reverse-gap identity (`m≤10`); prefix-cylinder bound (`s≤6, R≤8`). All PASS. |
| `cp17-referee-v1/verify3.py` | Appendix B reachable-terminal package for `t≤4` over ~100k unit starts; `M(y) ≤ 2^m p_s^Syr(y)` for `m≤9, s≤4`; prefix count bound for `t≤4`. 0 failures. |
| `cp17-referee-v1/rate.py`, `rate4.py` | Saving band: brute-force grid over `γ` (conservative envelope) vs closed-form `γ`-infimum (faithful envelope). Agree to 2.2e−16; gap ≡ 0 for `β ≤ β₀`, > 0 above — i.e. `β₀` is exactly the threshold the proof claims. |
| `cp17-referee-v1/fidelity.py`, `prose.py` | Display-math and word-level diff of the manuscript against the standalone proof. 132/132 tagged displays identical. |
| `cp17/chi_exact.py` | From-scratch `χ_n = 3ⁿ Σ p_n(y)²` for `n ≤ 12` via the recursion `X_n = 2^{-A}(1+3X_{n-1}) mod 3ⁿ`, plus the autocorrelations `C_n(1), C_n(2), C_n(3)`. |
| `cp17/exhaustive.py` | Exhaustive audit of every internal inequality of the collision-energy theorem for `n ≤ 6`, including the injectivity test and the martingale class decomposition. |
| `cp17/partB.py` | The fixed-weight pointwise bound `M(y) ≤ (2^m/C(m,s)) p_s^Syr(y)` for `(m,s) ∈ {(6,3),(8,4),(10,5),(9,4),(12,6)}`, checking **both** the aligned and the naive unaligned residue labelling. |
| `cp17/verify_K.py` | `α`, `I(α)`, `β₀`, `β_sw`, `β_*`, `K₁₇` at `mp.dps = 60`. |
| `cp17/sweep2d.py` | Two-dimensional sweep of the prefix envelope over `(c, β)`. |

### 3.3 What I verified myself in this audit

For the record, independently of the above:

- Recomputed `α`, `β₀`, `I(α)`, `K₁₇` at 40 digits with `mpmath`: `K₁₇ = 2.742881438765941863306094837987417771463`, matching the manuscript's 21-digit display at line 1335 exactly and its 20-digit display at line 2245 as a correct truncation. `K₁₇ < 2.742882` is **True**.
- Compiled the manuscript from source (`pdflatex` → `bibtex` → `pdflatex` ×2): 38 pages, 0 errors, 0 warnings, 0 undefined references or citations, 0 over/underfull boxes.
- Resolved all 15 DOIs live against Crossref/DataCite and all 3 arXiv identifiers against the arXiv API.

---

## 4. Conflict of interest

JTNB publishes no conflict-of-interest policy that I could find. A one-line statement is
conventional and costs nothing:

> ## Conflict of interest
>
> The author declares no conflict of interest.

## 5. Funding

The submission PDF already carries:

> ## Funding
>
> This work received no external funding.

**Correct as it stands.** No change proposed. `[AUTHOR TO CONFIRM this is still accurate.]`
