# JOURNAL_FIT — CP17 manuscript vs. JTNB

Target journal per the filename `CP17_JTNB_INITIAL_SUBMISSION_V3.pdf`:
**Journal de Théorie des Nombres de Bordeaux** (ISSN 1246-7405), published by the Institut de
Mathématiques de Bordeaux / Université de Bordeaux, hosted on Centre Mersenne.

---

## 1. Source of the requirements

The journal's Centre Mersenne pages (`jtnb.centre-mersenne.org/page/instructions-aux-auteurs/`,
`…/page/submissions/`) are JavaScript-rendered and return **no content** to a plain fetch — worth
knowing, because it means the real rules live elsewhere. They are on the Bordeaux site:

- **Submission:** `https://jtnb.math.u-bordeaux.fr/jtnbsubmit.html` (last updated 24 July 2023)
- **Preparation of the final version:** `https://jtnb.math.u-bordeaux.fr/preparation.html`

Both fetched and quoted verbatim below. **Note the split:** `jtnbsubmit.html` governs what you send
**now**; `preparation.html` opens with *"La version finale doit être préparée en tenant compte des
instructions suivantes"* — i.e. it governs the **accepted** version. I have graded each requirement
by which stage it binds, because that changes what is blocking today.

---

## 2. Requirement-by-requirement gap analysis

| # | JTNB requirement (verbatim) | Binds at | Manuscript status | Gap |
|---|---|---|---|---|
| J1 | *"Les manuscrits proposés doivent obligatoirement être soumis via le site web: `https://jtnb.math.cnrs.fr/`"* | **submission** | — | **Process gap.** Submission is via the web platform only; there is no submission email. (`managing@jtnb.math.u-bordeaux.fr` is the managing contact, not a submission address.) |
| J2 | *"Les auteurs doivent choisir un membre du comité éditorial (celui ou celle ayant la plus grande proximité scientifique avec leur sujet) pour lui soumettre leurs travaux."* | **submission** | not recorded anywhere in the package | **Action required.** The author must nominate a specific editorial-board member. For a paper that is 3-adic/2-adic distribution + large deviations + arithmetic dynamics (MSC 11B83, 11K36, 37A50), pick the board member closest to arithmetic dynamics or probabilistic number theory. |
| J3 | *"Aucun produit issu de l'IA ne peut être considéré comme auteur ou co-auteur… Les auteurs doivent déclarer explicitement **dans un paragraphe dédié du manuscrit soumis** toute utilisation d'un outil d'IA ou LLM lors du processus de rédaction et expliquer les spécificités et la nature de ce recours (vérification orthographique, syntaxe, mise en page et, plus important encore, **toute intervention de l'IA dans les arguments scientifiques ou les citations**)."* | **submission** | **Satisfied in the PDF, absent from the `.tex`** | See §3. In `CP17_MANUSCRIPT.tex` the disclosure exists only as a `%` comment (line 1386) — invisible in output. The submission PDF **does** carry a dedicated section. |
| J4 | *"La première page du manuscrit doit contenir le titre, le nom des auteurs et un résumé court mais suffisamment explicite sur le contenu de l'article."* | **submission** | PDF: title ✓, author "HALIL TALHA ERTAN" ✓, abstract ✓. `.tex`: `\author{}` empty | **Blocking for the `.tex`** (see `SELF_CONTAINMENT_CHECK.md` §4.1). Satisfied in the PDF. |
| J5 | *"L'article est composé dans un fichier source (latex) en prenant pour modèle le fichier `exemple.tex`. Les auteurs doivent télécharger au préalable le fichier spécifique **`jT.cls`** des documents JTNB, qui s'appuie sur le fichier de style de base `amsart.cls`."* | **final version** | uses `\documentclass[11pt]{amsart}` | **Gap, but cheap.** JTNB states `jT.cls` *is built on* `amsart.cls`, and this manuscript is already an amsart document with no exotic packages. Conversion is mostly mechanical. Not blocking for initial submission; do it now anyway to avoid a second round. |
| J6 | *"Le fichier source contient un **résumé en français et en anglais**."* | **final version** | English abstract only | **Gap.** A French abstract must be written. ~150 words. This is the single item most likely to be forgotten. |
| J7 | *"Le fichier source inclut les **adresses postales et électroniques** de tous les auteurs."* | **final version** | absent from both `.tex` and PDF | **Gap.** The PDF shows a bare name with no affiliation or email. |
| J8 | *"Il est important de ne pas remplacer les commandes du fichier `exemple.tex` pour les résumés, les mots-clefs, la classification AMS par matières et la bibliographie par d'autres commandes."* | **final version** | uses `natbib` + `\citep` + `\bibliographystyle{plainnat}` | **Gap.** `natbib`/`plainnat` is exactly such a replacement. Under `jT.cls` use the template's bibliography commands and plain `\cite`. MSC (`\subjclass[2020]`) and `\keywords` are already present at lines 23–24 in amsart form and will map across. |
| J9 | *"Seules les références bibliographiques citées dans le texte sont listées en fin d'article, et cela par **ordre alphabétique**, et en respectant le style du JTNB."* | **final version** | 16/16 cited, 16/16 defined, and `plainnat` already sorts alphabetically (verified from the generated `.bbl`) | **Substantially satisfied.** Only the style file changes. |
| J10 | *"Les cadres colorés dans les hyperliens doivent être supprimés."* | **final version** | `\usepackage[hidelinks]{hyperref}` at line 6 | **Already satisfied.** Do not undo this during the `jT.cls` conversion. |
| J11 | *"La version finale des articles acceptés devra être envoyée sous la forme d'un fichier TeX, avec une préférence pour le format LaTeX2e."* | **final version** | LaTeX2e ✓ | satisfied |
| J12 | figures *"encapsulées au format postscript ou pdf (éviter le plus possible les fichiers de style personnels)"* | final version | no figures; no custom `.sty` | satisfied |

### Not specified by JTNB

- **Length limit.** Neither page states one. At **38 pages** the manuscript is long but not
  out of range for JTNB, which regularly publishes 25–40 page papers. **No action**, but note that
  Appendices A–C occupy pages 21–38, i.e. **45% of the paper**, and a referee may ask whether
  Appendix A (the growing-depth master inequality, 17 pages of the source) belongs in the body.
- **Language.** Not restricted on either page; JTNB publishes in both French and English. English is
  fine. (The French *abstract* requirement, J6, is separate and does stand.)
- **Data & code availability.** JTNB states **no** data/code policy. This is a gap in the *journal's*
  rules, not the manuscript's — but see §4: the manuscript's §16 currently points at files nobody
  can obtain, which is worse than having no statement at all.
- **Conflict of interest.** No JTNB policy found. A one-line statement is harmless and conventional.
- **Copyright / licence.** Not stated on either page. Centre Mersenne journals are diamond
  open-access; check the licence terms at acceptance.

---

## 3. The AI/LLM declaration — status and assessment

JTNB has an **explicit, mandatory, unusually specific** AI policy (J3). It is one of the stricter
ones in number theory, and it asks for exactly the thing most declarations omit: *"toute
intervention de l'IA dans les **arguments scientifiques** ou les **citations**"*.

**The submission PDF already carries a dedicated section** (page 20, `section*.58`, "Declaration on
the use of AI/LLM tools"):

> "During the development and preparation of this manuscript, the author used large language model
> tools for exploratory mathematical reasoning, assistance with the generation and checking of
> computational experiments, drafting and editing, literature triage and citation cross-checking,
> and adversarial proof review. The mathematical claims retained in the manuscript were subjected to
> exact or symbolic checks, reproducible computations where applicable, and repeated adversarial
> review. No AI system is listed as an author. The human author takes responsibility for the
> submitted mathematical content, citations, and disclosures."

**Assessment: this satisfies J3 and does so well.** It names scientific-argument involvement
("exploratory mathematical reasoning", "adversarial proof review") and citation involvement
("literature triage and citation cross-checking") rather than hiding behind "language polishing" —
which is precisely what the policy is written to catch. It also states the no-AI-author rule and the
human responsibility statement.

Two refinements are proposed in `DISCLOSURE_DRAFT.md` §2: (i) it does not say which *specific*
results were machine-checked and by what method, and (ii) "assistance with the generation… of
computational experiments" is vaguer than the exact-arithmetic certification actually performed.

**However — it is not in the `.tex` under audit.** `CP17_MANUSCRIPT.tex` has only a `%` comment at
line 1386, which produces nothing. See `SELF_CONTAINMENT_CHECK.md` §6.

---

## 4. Data & code availability — the real weakness

JTNB does not require a statement, so this is not a compliance gap. It is a **credibility** gap.

§16 (line 1382 / PDF page 20) currently says the certificate is `CP17_FINAL_RATE_CERTIFICATE_V3.py`
and the proof source is `CP17_FINAL_STANDALONE_PROOF_V3.md`. **Neither file is obtainable by a
referee**: no DOI, no URL, no repository, no supplementary-material upload. A section titled
"Reproducibility and certificates" that names two unreachable files reads worse than no section.

> **Recommendation.** Deposit the certificate script and its output on **Zenodo** (mints a DOI, no
> cost, permanent) or attach them as supplementary material, and cite the DOI in §16. Draft text in
> `DISCLOSURE_DRAFT.md` §1. The scripts to deposit are named there.

---

## 5. Is JTNB the right venue?

**Yes, with one caveat.** JTNB publishes arithmetic dynamics and probabilistic number theory; the
MSC codes (11B83 primary; 11K36, 37A50 secondary) are in scope; the length is acceptable; the
journal is diamond open-access and well indexed.

**The caveat is the referee pool.** This paper is a Collatz paper. Every number theory journal
receives a steady stream of claimed Collatz proofs, and editors triage them hard. This manuscript's
best defence is exactly the thing it already does well — the abstract's final sentence
("The result does not prove the Collatz conjecture, rule out divergent orbits or nontrivial cycles,
or establish `limsup s_k/log₂k > 1`") — and the cover letter should lead with it, not bury it. The
blocking items in `CLAIMS_WORDING_AUDIT.md` §4 matter disproportionately here: a paper that cites an
"accompanying literature audit" the editor does not have, and whose §16 says the *real* proof is in
a `.md` file, looks like exactly the kind of submission the triage filter is designed to catch —
regardless of the mathematics being sound.

---

## 6. Alternative venues

| Venue | Rationale | Notes |
|---|---|---|
| **Acta Arithmetica** | Closest peer of JTNB in scope and level; already publishes four of this paper's own references (Terras 1976; Matthews–Watts 1984, 1985; Krasikov–Lagarias 2003), so the referee pool demonstrably exists. English, LaTeX, no French abstract needed. | Strongest alternative if JTNB declines. Slower turnaround. |
| **INTEGERS: Electronic Journal of Combinatorial Number Theory** | Publishes 3x+1 work routinely — including this paper's own `Rozier2019` (Integers 19, #A8). Fast, open access, receptive to explicit-constant results of exactly this shape. | Lower prestige than JTNB/Acta, but the *fit* is arguably the best of any journal on this list. |
| **Experimental Mathematics** | Publishes `ApplegateLagarias1995trees`. A natural home given the certified-constant / exact-interval-arithmetic component and the reproducibility material. | Would want the code deposit (§4) done properly — which is a good discipline regardless. |
| **International Journal of Number Theory (IJNT)** | Broad scope, explicitly welcomes analytic/probabilistic number theory, faster than Acta. | Commercial (World Scientific), not open access. |
| **Journal of Number Theory** | Broad and well known. | Elsevier; heavily loaded with Collatz submissions, so triage risk is highest here. |

**Recommendation:** keep JTNB as first choice — the AI declaration is already written to its policy
and the conversion cost is low — with **Acta Arithmetica** and **INTEGERS** as second and third.

---

## 7. Concrete pre-submission checklist for JTNB

**Blocking (must be done before uploading):**

1. Locate the `.tex` that produced `CP17_JTNB_INITIAL_SUBMISSION_V3.pdf`; do not edit the stale one
   (`SELF_CONTAINMENT_CHECK.md` §6).
2. Ship `CP17_REFERENCES.bib` with the `.tex` (`CITATION_AUDIT.md` C1).
3. Add affiliation, postal address and email to `\author` (J4/J7).
4. Remove the four jargon leaks — "accompanying literature audit", "frozen" ×3, "publication
   branch", "CP9" (`CLAIMS_WORDING_AUDIT.md` §4).
5. Rewrite §16 around a citable DOI deposit, or delete it (§4 above).
6. Fix the `Rozier2019` bibliography entry (`CITATION_AUDIT.md` C2).
7. Make T1, T2 and L2 self-contained (`CLAIMS_WORDING_AUDIT.md` §2).
8. Nominate the editorial-board member (J2).

**Do now, cheaply, to avoid a second round:**

9. Convert to `jT.cls` from `exemple.tex` (J5, J8) — it is amsart-based, so the diff is small.
10. Write the French abstract (J6).
11. Verify or delete the unverified sentence about Tao's exponent (`CITATION_AUDIT.md` C5).
