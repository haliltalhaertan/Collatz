# SELF_CONTAINMENT_CHECK — CP17 manuscript

Source: `C:/Users/MDP/Downloads/CP17_MANUSCRIPT.tex` (2 844 lines, sha256 `42bed9aa…39dab`).
Comparison target: `C:/Users/MDP/Downloads/CP17_JTNB_INITIAL_SUBMISSION_V3.pdf` (38 pages).

---

## 1. Compilation — **PASS**, and this is the first time it has actually been done

A LaTeX toolchain **is** available on this machine (MiKTeX, at
`C:/Users/MDP/AppData/Local/Programs/MiKTeX/miktex/bin/x64/`: `pdflatex`, `latexmk`, `xelatex`).
This matters, because the prior external referee recorded:

> "No TeX toolchain was available on this machine, so the manuscript was **not recompiled**. The
> supplied PDF/AUX were checked for internal consistency instead."
> — `CP17_EXTERNAL_REFEREE_VERDICT_2026-08-23.md`

So the build below is, as far as the audit trail shows, **the first independent compilation of this
manuscript from source by anyone other than the author.**

### 1.1 Blocker hit first: the bibliography database is missing

`CP17_MANUSCRIPT.tex` line 2842 reads `\bibliography{CP17_REFERENCES}`. A filesystem-wide search

```
find /c/Users/MDP -maxdepth 6 -iname '*.bib'     ->  (no output)
```

returns **nothing**. `CP17_REFERENCES.bib` exists only inside archives:

- `CP17_EXTERNAL_REFEREE_PACKAGE_V1.zip` → `PRIMARY/CP17_REFERENCES.bib` (4 979 bytes) — the copy
  that pairs with this exact `.tex` (both 2026-08-23 14:03, and the `.tex` inside the zip is
  byte-identical to the one in `Downloads/`, sha256 verified)
- `CP17_PUBLICATION_BRANCH.zip` → `CP17_PUBLICATION_BRANCH/CP17_REFERENCES.bib` (4 655 bytes — an
  **older** version, paired with a 69 917-byte `.tex`)

**As it sits in `Downloads/`, the manuscript cannot be built by anyone.** This is a packaging
defect, not a mathematical one, but it would waste a referee's afternoon.

### 1.2 Build, after extracting the .bib

```
pdflatex -interaction=nonstopmode CP17_MANUSCRIPT.tex     exit=0
bibtex   CP17_MANUSCRIPT                                  exit=0
pdflatex -interaction=nonstopmode CP17_MANUSCRIPT.tex     exit=0
pdflatex -interaction=nonstopmode CP17_MANUSCRIPT.tex     exit=0
```

| Check | Result |
|---|---|
| Fatal errors (`^!`, `Emergency`, `Fatal`) | **0** |
| Output | `CP17_MANUSCRIPT.pdf`, **38 pages**, 517 994 bytes |
| BibTeX warnings/errors (`.blg`) | **0**; "You've used 16 entries" |
| `LaTeX Warning:` of any kind on the final pass | **0** |
| Undefined citations | **0** |
| Undefined references | **0** |
| Multiply-defined labels | **0** |
| Overfull boxes | **0** |
| Underfull boxes | **0** |

A zero-warning, zero-badbox 38-page amsart build is a genuinely clean result. Note the manuscript
also compiles under **pdfTeX** (MiKTeX pdfTeX-1.40.28), whereas the shipped PDFs were produced by
**LuaTeX-1.18.0** — so the source is not engine-locked.

---

## 2. Cross-references — **PASS**

Checked statically against the source *and* confirmed by the warning-free build.

| Check | Count | Result |
|---|---|---|
| `\label{}` definitions | 193 | — |
| Distinct targets of `\cref`/`\Cref`/`\eqref` | 79 | — |
| **Dangling references** (target with no label) | **0** | **PASS** |
| **Duplicate labels** | **0** | **PASS** |
| Manual `\tag{}` displays | 133 | — |
| **Duplicate `\tag` values** | **0** | **PASS** |
| `\ref` / `\autoref` (raw, un-cleverefed) | 0 / 0 | clean — everything goes through `cleveref` |
| Unreferenced labels | 114 | see below |

**On the 114 unreferenced labels:** these are almost entirely `\label{eq:...}` on tagged displays
and `\label{section-name}` on sections, auto-emitted by whatever converted the source. They are
harmless (LaTeX does not warn), but two are worth a second look:

- `eq:body-fw` (line 905) labels the boxed, tagged fixed-weight transfer `(FW)` — and line 910
  states outright that the final proof "does not require this Stirling round trip". A boxed,
  numbered, labelled, **never-referenced** display invites the referee question "where is this
  used?" (See `CLAIMS_WORDING_AUDIT.md` §4.3.)
- All 16 `\label` on section headings are unreferenced. Harmless.

---

## 3. Figures and tables — **N/A**

Zero `\begin{figure}`, `\begin{table}`, `\begin{tabular}`, `\includegraphics`, `\caption`.
The paper is pure text and display math. **Nothing to check, and nothing missing.** (JTNB's rule
about encapsulated PostScript/PDF figures does not apply.)

---

## 4. Placeholders and leftovers

| Pattern | Hits | Verdict |
|---|---|---|
| `\todo`, `TODO`, `XXX`, `FIXME`, `TBD`, `N/A` | **0** | **PASS** |
| `??` (unresolved reference marker) | **0** in source; **0** in the built PDF (zero undefined refs) | **PASS** |
| Non-ASCII characters | 1 line (63) — the `é` in "Stérin", correctly encoded | fine |

### 4.1 **BLOCKING** — author metadata is empty

```latex
19: % Insert author name(s), affiliation(s), and correspondence metadata before submission.
20: \author{}
21: \date{}
```

Confirmed downstream: the submission PDF's document-information dictionary has
`/Author ()`, `/Title ()`, `/Subject ()`, `/Keywords ()` — all empty.

JTNB requires (`preparation.html`): *"Le fichier source inclut les adresses postales et
électroniques de tous les auteurs"*, and (`jtnbsubmit.html`): *"La première page du manuscrit doit
contenir le titre, le nom des auteurs et un résumé"*. See `JOURNAL_FIT.md` §3.

**Note the divergence:** the submission PDF *does* print an author on page 1 —
**HALIL TALHA ERTAN** — with no affiliation, no postal address, no email. So the author was added
in a source revision that is **not the `.tex` under audit** (see §6).

---

## 5. Audit-internal jargon leaking into reader-facing text — **4 sites, all BLOCKING**

Full-text scan for `CP\d+`, `checkpoint`, `frozen`, `audit`, `package`, `publication branch`, `gate`,
`zero-trust`, `regression`. Results after excluding legitimate mathematical uses of "regression"
(lines 574, 1328, 2142 use it in the sense "the estimate regresses to…", which is normal
mathematical English):

| Line | Exact text | Problem |
|---|---|---|
| 65 | "…for which the **accompanying literature audit** found no exact match…" | Refers to a document the referee will not receive. |
| 908 | "This is an editorial extraction of the **frozen** fixed-weight transfer…" | `frozen` = internal version-control state. |
| 1382 | "**The frozen proof source is** `CP17_FINAL_STANDALONE_PROOF_V3.md`. The exact coefficient certificate is `CP17_FINAL_RATE_CERTIFICATE_V3.py`… The **frozen package** includes a SHA256 manifest and a dependency graph. **The publication branch** reran the coefficient certificate and verified the **frozen package manifest** before preparing this manuscript." | Four leaks in one paragraph; also names two files the referee cannot obtain; also asserts that the *real* proof lives elsewhere. |
| 2142 | "Thus the new theorem regresses correctly to the **CP9** fixed-\(t\) statement." | `CP9` is undefined, uncited, and appears nowhere else. |

All four are present in the submission PDF (verified on PDF pages 2 and 20). Exact proposed
replacements are in `CLAIMS_WORDING_AUDIT.md` §4.

---

## 6. **The `.tex` under audit is NOT the source of the submission PDF**

This is the most consequential logistics finding in this report, so it gets its own section.

| Evidence | `CP17_MANUSCRIPT.tex` (audited) | `CP17_JTNB_INITIAL_SUBMISSION_V3.pdf` |
|---|---|---|
| Timestamp | 2026-08-23 **14:01** | 2026-08-23 **15:52** |
| Engine | builds under pdfTeX; shipped `CP17_MANUSCRIPT.pdf` is LuaTeX | LuaTeX-1.18.0 |
| Pages | 38 | 38 |
| Author on page 1 | **none** (`\author{}`) | **"HALIL TALHA ERTAN"** |
| §2 Tao paragraph | ends "…with an explicit exponent \(4\); Tao only requires a conditional polynomial factor…" | **adds** "More precisely, in Tao's fixed-total-valuation step the relevant atom probability is \(2^{-l}=n^{O(C_A^2)}3^{-n}\), and the resulting conditional contribution is bounded by \(n^{-2A'+O(C_A^2)}\) before \(A'\) is chosen sufficiently large." |
| Unnumbered sections after §16 | **none** (only `%`-commented note at line 1386) | **two**: "Declaration on the use of AI/LLM tools" (`section*.58`) and "Funding" (`section*.59`) |
| Hyperref destination for References | `section*.134` | `section*.136` (= +2 sectioning units, consistent with the two extra sections) |

I confirmed the bookmark comparison mechanically: my build's `.out` file contains 36 bookmarks,
16 numbered sections plus one unnumbered ("References"), and **zero** hits for
`Declaration|Funding|AI/LLM`. The submission PDF's decompressed destination table contains
`DeclarationontheuseofAI/LLMtools` and `Funding`.

**Consequence.** Every finding in this audit set is against a `.tex` that is at least one revision
behind the submitted PDF, and **the newer `.tex` is nowhere on this filesystem** — not in
`Downloads/`, not in `collatz/`, not in any of the seven zips. Before any of these fixes are
applied, **locate the source that produced `CP17_JTNB_INITIAL_SUBMISSION_V3.pdf`.** Editing the
stale `.tex` would silently revert the author name, the AI/LLM declaration, the funding statement,
and the Tao clarification.

Two of the divergences are *improvements already made* — the AI/LLM declaration and the funding
statement are exactly what `JOURNAL_FIT.md` §3 would otherwise demand. One of them (the Tao
exponent sentence) is the single unverified literature claim in the paper
(`CITATION_AUDIT.md` §2.1).

---

## 7. Minor presentation defects

**7.1 Two PDF bookmarks display raw LaTeX.** Decoding my build's `.out`:

```
subsection.7.3 -> '7.3. Exact tail inequality and \theta_{\max}'
section.13     -> '13. Safe c\downarrow\alpha order and the final coefficient'
```

These come from the `\texorpdfstring` fallbacks at `.tex` lines 442 and 1259, whose PDF-string
argument literally contains `\textbackslash theta\_\{\textbackslash max\}` and
`Safe c\textbackslash downarrow\textbackslash alpha order…`. The outline pane therefore shows LaTeX
source to the reader.

> **Proposed replacement, line 442:**
> `\subsection{\texorpdfstring{Exact tail inequality and \(\theta_{\max}\)}{Exact tail inequality and theta-max}}\label{exact-tail-inequality-and-theta_max}`
>
> **Proposed replacement, line 1259:**
> `\section{\texorpdfstring{Safe \(c\downarrow\alpha\) order and the final coefficient}{Safe c to alpha order and the final coefficient}}\label{safe-cdownarrowalpha-order-and-the-final-coefficient}`

The same fallback style is used at lines 2415 and 2435 (`Minimum total valuation is attained at
r\_y`, `Canonical reconstruction \textbackslash xi\_t(y)`) and should be corrected the same way.

**7.2 `hidelinks` vs JTNB.** Line 6 already loads `\usepackage[hidelinks]{hyperref}`, which
satisfies JTNB's *"Les cadres colorés dans les hyperliens doivent être supprimés"*. **No action** —
recording it so it is not "fixed" during the `jT.cls` conversion.

---

## 8. Verdict

| Item | Status |
|---|---|
| Compiles from source | **PASS** (38 pp, 0 errors, 0 warnings, 0 bad boxes) |
| `.bib` shipped alongside `.tex` | **FAIL — blocking** (§1.1) |
| All `\ref`/`\cref`/`\eqref` resolve | **PASS** (0 dangling, 0 duplicate labels, 0 duplicate tags) |
| Figures/tables referenced exist | **N/A** (none) |
| No `\todo`/`TODO`/`XXX`/`??` | **PASS** |
| Author/affiliation present | **FAIL — blocking** (§4.1) |
| No audit-internal jargon in reader-facing text | **FAIL — blocking**, 4 sites (§5) |
| Audited `.tex` == submission source | **FAIL — blocking** (§6) |
| PDF bookmarks clean | minor, 2 sites (§7.1) |
