# CITATION_AUDIT — CP17 manuscript

Referee: analytic number theory / dynamics.
Date: 2026-09-07.
Targets audited:

- `C:/Users/MDP/Downloads/CP17_MANUSCRIPT.tex` (74 032 bytes, sha256 `42bed9aa…39dab`, 2 844 lines)
- `C:/Users/MDP/Downloads/CP17_JTNB_INITIAL_SUBMISSION_V3.pdf` (38 pages)
- Bibliography database `CP17_REFERENCES.bib` — **not present on the filesystem**; recovered from
  `C:/Users/MDP/Downloads/CP17_EXTERNAL_REFEREE_PACKAGE_V1.zip` → `PRIMARY/CP17_REFERENCES.bib` (4 979 bytes, 16 entries).

Method: every DOI resolved live against the Crossref REST API; the one Zenodo DOI resolved against
DataCite; three arXiv identifiers resolved against the arXiv API. Nothing below is taken from the
prior internal audits, which explicitly left "citation metadata against MathSciNet/Crossref" as an
open human gate (`CP17_EXTERNAL_REFEREE_VERDICT_2026-08-23.md` §6, `CP17_PUBLICATION_BRANCH_V3_AUDIT_2026-08-23.md` line 137).

---

## 0. Headline

| Check | Result |
|---|---|
| `\cite` keys used | 16 (in 12 `\citep` commands, all on lines 47, 59, 61, 63, 65, 67) |
| Bib entries defined | 16 |
| Cited-but-undefined | **0** |
| Defined-but-uncited | **0** |
| DOIs that resolve and match the entry | **15 / 15** (14 Crossref + 1 DataCite) |
| arXiv ids that resolve and match | **3 / 3** |
| Entries requiring correction before submission | **2** (`Rozier2019`, `Sterin2019`) |
| Entries requiring a judgement call | **2** (`MatthewsWatts1984/1985` given names, `Lagarias2003` plurality) |
| Named results used but neither cited nor proved | **3** (Chernoff, Hoeffding, Doob) |
| Missing reference a specialist referee will ask for | **2** (Lagarias 2010 *Ultimate Challenge*; Lagarias' bibliography part II) |

**BLOCKING-1 (logistics, not mathematics).** `CP17_REFERENCES.bib` exists nowhere on disk — a
filesystem-wide `find /c/Users/MDP -iname '*.bib'` returns nothing. The `.tex` ends with
`\bibliography{CP17_REFERENCES}` (line 2842), so the manuscript as it sits in `Downloads/` **cannot
be built by anyone who does not first unzip the referee package.** Extract
`PRIMARY/CP17_REFERENCES.bib` next to the `.tex` and keep the pair together.

---

## 1. Entry-by-entry verification

All fifteen DOIs were resolved live. Format below: **bib field** vs *record of publication*.

### 1.1 Entries that verify clean — no change needed

| Key | DOI | Crossref record | Verdict |
|---|---|---|---|
| `Terras1976` | `10.4064/aa-30-3-241-252` | Riho Terras, "A stopping time problem on the positive integers", Acta Arithmetica **30** (3), 241–252, 1976 | **exact match** |
| `Everett1977` | `10.1016/0001-8708(77)90087-1` | C. J. Everett, "Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2", Advances in Mathematics **25** (1), 42–45, 1977 | **exact match** |
| `Lagarias1985` | `10.1080/00029890.1985.11971528` | J. C. Lagarias, "The 3x+1 Problem and its Generalizations", Amer. Math. Monthly **92** (1), 3–23, 1985 | **exact match** |
| `LagariasWeiss1992` | `10.1214/aoap/1177005779` | Lagarias & Weiss, "The 3x+1 Problem: Two Stochastic Models", Ann. Appl. Probab. **2** (1), 1992 | **exact match** (Crossref omits pages; 229–261 is correct) |
| `ApplegateLagarias1995a` | `10.1090/S0025-5718-1995-1270612-0` | "Density bounds for the 3x+1 problem. I. Tree-search method", Math. Comp. **64** (209), 411–426, 1995 | **exact match** |
| `ApplegateLagarias1995b` | `10.1090/S0025-5718-1995-1270613-2` | "…II. Krasikov inequalities", Math. Comp. **64** (209), 427–438, 1995 | **exact match** |
| `ApplegateLagarias1995trees` | `10.1080/10586458.1995.10504321` | "The Distribution of 3x+1 Trees", Experimental Mathematics **4** (3), 193–209, 1995 | **exact match** |
| `BernsteinLagarias1996` | `10.4153/CJM-1996-060-x` | "The 3x+1 Conjugacy Map", Canad. J. Math. **48** (6), 1154–1169, 1996 | **exact match** |
| `MatthewsWatts1984` | `10.4064/aa-43-2-167-175` | K. Matthews, A. Watts, "A generalization of Hasse's generalization of the Syracuse algorithm", Acta Arith. **43** (2), 167–175, 1984 | match (see §1.3 on given names) |
| `MatthewsWatts1985` | `10.4064/aa-45-1-29-42` | K. Matthews, A. Watts, "A Markov approach to the generalized Syracuse algorithm", Acta Arith. **45** (1), 29–42, 1985 | match (see §1.3) |
| `Lagarias2003` | arXiv `math/0309224` | J. C. Lagarias, "The 3x+1 problem: An annotated bibliography (1963–1999) (sorted by author)", submitted 2003-09-13 | **exact match** |
| `Tao2022` | `10.1017/fmp.2022.8` | Terence Tao, "Almost all orbits of the Collatz map attain almost bounded values", Forum of Mathematics, Pi **10**, 2022 | **exact match**; arXiv journal-ref confirms "Forum Math. Pi 10 (2022), Paper No. e12, 56 pp", so `pages = {e12}` is right |
| `RozierTerracol2026` | `10.1016/j.disc.2026.115167` | Rozier & Terracol, "Paradoxical behavior in Collatz sequences", Discrete Mathematics **349** (10), 115167, 2026 | **exact match** |

`ApplegateLagarias2003` (`10.1090/S0025-5718-02-01425-4`): title, authors, journal, volume 72, issue
242, pages 1035–1049 all verify. Crossref carries `issued = 2002-06-06` (electronic-first) while the
bib says `year = {2003}`. **No change.** Math. Comp. vol. 72, no. 242 is the April 2003 issue and
MathSciNet/AMS cite it as 2003; the Crossref date is the online-first stamp. Recording this here so
that a later automated bibliography checker does not "fix" it wrongly.

### 1.2 Entries requiring correction

#### (a) `Rozier2019` — the `doi` field points at a preprint deposit, not the article of record

Current entry:

```bibtex
@article{Rozier2019,
  author  = {Olivier Rozier},
  title   = {Parity sequences of the $3x+1$ map on the $2$-adic integers and Euclidean embedding},
  journal = {INTEGERS},
  volume  = {19},
  pages   = {A8},
  year    = {2019},
  eprint  = {1805.00133},
  archivePrefix = {arXiv},
  doi     = {10.5281/zenodo.10705023}
}
```

Findings:

1. `10.5281/zenodo.10705023` **returns HTTP 404 from Crossref** but **does resolve on DataCite**:
   title "Parity Sequences of the 3x+1 Map on the 2-adic Integers and Euclidean Embedding",
   creator "Rozier, O.", publicationYear 2019, publisher Zenodo, resourceTypeGeneral `Text`,
   URL `https://zenodo.org/doi/10.5281/zenodo.10705023`.
   So the DOI is real — but it is a **Zenodo deposit of the text**, not the journal's article DOI.
   *Integers* does not mint article DOIs. Putting a Zenodo `Text` DOI in the `doi` field of an
   `@article` makes `plainnat`/JTNB style print it as if it were the publisher's identifier. A
   referee who clicks it lands on a repository record, not on *Integers*. This is the single
   most likely citation query in a referee report.
2. arXiv `1805.00133` verifies: same title, author Olivier Rozier, and — decisively —
   `journal_ref = "Integers 19 (2019), article A8"`. So volume 19 and article A8 are confirmed
   from the author's own arXiv metadata.
3. Journal name: MathSciNet/zbMATH abbreviate the journal **Integers**, not `INTEGERS`. All-caps
   is the website's logotype, not the citation form.
4. `pages = {A8}` should carry the article marker so the style does not typeset "p. A8".

**Proposed replacement:**

```bibtex
@article{Rozier2019,
  author  = {Olivier Rozier},
  title   = {Parity sequences of the $3x+1$ map on the $2$-adic integers and {E}uclidean embedding},
  journal = {Integers},
  volume  = {19},
  pages   = {Paper No. A8},
  year    = {2019},
  eprint  = {1805.00133},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT},
  note    = {Zenodo deposit \texttt{10.5281/zenodo.10705023}}
}
```

#### (b) `Sterin2019` — key/year mismatch, incomplete proceedings metadata

Current entry has `Sterin2019` as key but `year = {2020}`. Crossref
(`10.1007/978-3-030-61739-4_8`) confirms: Tristan Stérin, "Binary Expression of Ancestors in the
Collatz Graph", *Lecture Notes in Computer Science* / *Reachability Problems*, pages 115–130,
**2020**, Springer International Publishing, ISBNs `978-3-030-61738-7` (print) and
`978-3-030-61739-4` (online). arXiv `1907.00775` verifies title and author (posted 2019-07-01),
which is presumably where the `2019` in the key came from.

The `volume = {12448}` is correct (Crossref returns an empty `volume` for chapters, but the LNCS
series number for RP 2020 is 12448 — consistent with the DOI prefix `978-3-030-61739-4`).

Two defects: (i) the key advertises the wrong year — harmless to the compiled output under
`[numbers]` but a trap for anyone maintaining the `.bib`; (ii) no `editor` and no `address`, which
JTNB's alphabetical proceedings style will want.

**Proposed replacement** (rename the key to `Sterin2020` and update the six citation sites — in
fact there is only one, `.tex` line 63):

```bibtex
@incollection{Sterin2020,
  author    = {Tristan St{\'e}rin},
  title     = {Binary Expression of Ancestors in the {C}ollatz Graph},
  booktitle = {Reachability Problems (RP 2020)},
  series    = {Lecture Notes in Computer Science},
  volume    = {12448},
  pages     = {115--130},
  publisher = {Springer},
  address   = {Cham},
  year      = {2020},
  isbn      = {978-3-030-61739-4},
  doi       = {10.1007/978-3-030-61739-4_8},
  eprint    = {1907.00775},
  archivePrefix = {arXiv},
  primaryClass  = {cs.DM}
}
```

*Note:* Crossref returns an **empty editor list** for this chapter, so I am deliberately not
asserting editor names. If JTNB's style demands them, take them from the printed volume's title
page rather than from a secondary source.

### 1.3 Judgement calls (not errors)

**(c) `MatthewsWatts1984` / `MatthewsWatts1985` given names.** The bib expands the authors to
"Keith R. Matthews and Anthony M. Watts". Crossref (i.e. the publisher's own deposited metadata)
carries only **"K. Matthews, A. Watts"**, and Acta Arithmetica prints initials. The expansion to
*Keith R.* is correct and well attested; *Anthony M.* is an expansion I could not confirm from any
record of publication. Under JTNB's rule *"en respectant le style du JTNB"* the safe choice is to
match the source:

> **Proposed:** `author = {K. R. Matthews and A. M. Watts}` in both entries.

Low severity, but an expanded forename that turns out to be wrong is exactly the kind of thing a
copy-editor catches at proof stage and the author then has to explain.

**(d) `Lagarias2003` and the word "bibliographies".** Line 59 reads:

> "Lagarias' survey and bibliographies \citep{Lagarias1985, Lagarias2003} organize much of the early literature."

The plural **bibliographies** is supported by only one bibliography entry. Lagarias published the
annotated bibliography in two parts; part II (2000–2009) is `arXiv:math/0608208`. Either add it or
make the noun singular.

> **Proposed replacement (minimal):** "Lagarias' survey and annotated bibliography
> \citep{Lagarias1985, Lagarias2003} organize much of the early literature."

### 1.4 Missing references a JTNB referee will ask for

Neither is load-bearing; both are the kind of omission that reads as unfamiliarity with the field.

1. **Lagarias (ed.), *The Ultimate Challenge: The 3x+1 Problem*, AMS, 2010.** Verified:
   Crossref DOI `10.1090/mbk/078`, monograph, American Mathematical Society, 2010,
   ISBN 978-0-8218-4940-8. This is *the* standard modern reference volume for the problem; a paper
   whose §2 is titled "Relation to prior work" and which cites four Applegate–Lagarias papers but
   not this book will be asked why.

   ```bibtex
   @book{Lagarias2010,
     editor    = {Jeffrey C. Lagarias},
     title     = {The Ultimate Challenge: The $3x+1$ Problem},
     publisher = {American Mathematical Society},
     address   = {Providence, RI},
     year      = {2010},
     isbn      = {978-0-8218-4940-8},
     doi       = {10.1090/mbk/078}
   }
   ```

2. **Krasikov & Lagarias 2003.** The audit brief names this explicitly. The manuscript cites
   `ApplegateLagarias1995b`, whose *title* contains "Krasikov inequalities", but never cites
   Krasikov–Lagarias itself. Verified: I. Krasikov and J. C. Lagarias, "Bounds for the 3x+1 problem
   using difference inequalities", *Acta Arithmetica* **109** (2003), no. 3, 237–258,
   DOI `10.4064/aa109-3-4`.

   **Verdict: not required.** No statement in the manuscript uses a difference-inequality density
   bound; §2's density-bound sentence is discharged by the Applegate–Lagarias citations. Adding it
   is optional polish, not a correction. I record it so the author can answer a referee who asks.

---

## 2. Do the cited statements match the ones actually used?

### 2.1 Tao 2022 — the only substantive external mathematical attribution

The manuscript refers to Tao by internal number in two places:

- **line 47** (§1): "In Section 6 of Tao \citep{Tao2022}, a collision-energy quantity is controlled
  conditionally on good events and a fixed total valuation; his Lemma 6.2 gives offset injectivity
  and Corollary 6.3 supplies the corresponding 3-adic separation."
- **line 65** (§2): "His Section 6 explicitly identifies a Renyi-2/collision-entropy quantity and
  controls it on good events at fixed total valuation, using Lemma 6.2 (injectivity of offsets)
  together with Corollary 6.3 (3-adic separation)."

Both sentences are **attribution of prior art**, not appeals to authority: nothing downstream
depends on Tao's lemma being true. That is the correct posture and it survives referee scrutiny.

**One concrete risk a referee will raise.** The bib cites the **published** version (Forum Math. Pi
**10** (2022), Paper No. e12). But arXiv `1909.03562` is now at **v7, last revised 16 July 2026** —
after publication — and its own comment field records that revisions "corrected … one medium typo
(affecting the statement of Lemma 7.9)". Internal numbering is therefore not guaranteed stable
between the published article and the current arXiv version, and the manuscript pins four specific
numbers (Remark 6.1, Lemma 6.2, Corollary 6.3, Propositions 1.14/1.17 per the internal novelty
matrix).

> **Proposed addition** at the first Tao reference (`.tex` line 47), immediately after
> `\citep{Tao2022}`:
>
> "(numbering follows the published version, Forum Math. Pi **10** (2022), Paper No. e12)"

Cost: one clause. Benefit: it disarms the entire class of "your Lemma 6.2 is my Lemma 6.3" queries.

**Explicitly out of my scope and still open:** the sentence added in the submission PDF (page 2,
absent from the `.tex`) —

> "More precisely, in Tao's fixed-total-valuation step the relevant atom probability is
> 2^{-l} = n^{O(C_A^2)} 3^{-n}, and the resulting conditional contribution is bounded by
> n^{-2A'+O(C_A^2)} before A' is chosen sufficiently large."

This is a quantitative assertion **about someone else's proof**. The external referee flagged the
`O(C_A^2)` exponent claim `[UNVERIFIED]` for want of access to the primary source. I did not verify
it either. It is the one remaining literature-dependency statement in the paper that has never been
checked against Tao's text by anyone, and it is checkable in an afternoon by a human with the PDF
open. **Recommend: verify it or delete it** — the paper's argument does not need it, and it is the
only sentence in the manuscript that could be *factually wrong about the literature*.

### 2.2 The two simplifications the internal audits identified — were they adopted?

The brief asks specifically about these. Answer: **both adopted, in substance, correctly.**

**(a) Tao's Lemma 6.2 replaced by a self-contained 2-adic valuation argument — ADOPTED.**
`.tex` lines 2563–2582+ carry a subsection literally titled *"Self-contained injectivity of the
offset map"*, followed by

```
\begin{lemma}[Injectivity of the offset map]\label{lem:offset-injectivity}
The map \(G_n:(\mathbb N_{\ge1})^n\to\mathbb Q\) is injective.
\end{lemma}
\begin{proof}
Use the ordinary \(2\)-adic valuation \(v_2\) on nonzero rationals. Since
\[ S_1<S_2<\cdots<S_n, \]
```

This is the three-line argument the 2026-08-22 adversarial audit recommended (its item A-Finding-1,
"the package's only claimed non-trivial literature input is Tao Lemma 6.2. It is not needed").
The remaining citations of Lemma 6.2 at lines 47 and 65 are **priority attribution**, which is
correct and should be kept — deleting them would be the error.

**Consequence for the brief's question "is every remaining literature dependency explicitly
declared?":** yes, and in fact the manuscript now has **zero load-bearing literature dependencies**.
All 12 `\citep` commands sit on lines 47–67, i.e. entirely inside §1 (Introduction) and §2 (Relation
to prior work). Sections 3–16 and Appendices A–C cite nothing. The paper is, by construction,
self-contained; §2 line 61 says so explicitly for the parity-prefix bijection ("treated as
background structure, not as a novelty claim").

**(b) The `(2^m/C(m,s))^2` fixed-weight round-trip — RETAINED, but explicitly declared
non-load-bearing.** `.tex` §10.2 (lines 877–910) still derives

```
\chi^{\rm fw}_{m,s} \le \left(\frac{2^m}{\binom ms}\right)^2 \chi_s^{\rm Syr}.   (FW)
```

and then line 908–910 says:

> "This is an editorial extraction of the frozen fixed-weight transfer: no new estimate is
> introduced. […] The final coefficient proof below uses the sharper pointwise bound directly and
> does not require this Stirling round trip."

So the 2026-08-22 audit's B-Finding-1 ("the binomial round-trip is unnecessary, and removing it
… needs no Stirling and no 'uniformly on compact ρ-subintervals of (0,1)' hypothesis") was honoured
at the level of the *proof* — the main chain uses the pointwise bound — while (FW) survives as an
illustrative corollary. **Mathematically fine.** Two editorial consequences, both handled in
`CLAIMS_WORDING_AUDIT.md` §4: the word "frozen" is internal jargon, and a referee reading a boxed,
tagged, labelled display `(FW)` will assume it is used somewhere.

### 2.3 Named classical results used without citation **or** proof

All citations stop at line 67; four classical results are then invoked by name in the proof body.
Under JTNB's alphabetical-references convention ("seules les références bibliographiques citées dans
le texte sont listées"), naming a theorem and giving no reference is a legitimate referee query.
Severity: **non-blocking**, but each is a one-line fix.

| Line | Invoked as | Status | Assessment |
|---|---|---|---|
| 324 | "The geometric Chernoff bound gives \(p_t(c)\le e^{-I(c)t}\)" | **no citation, no proof** | `I(c)=c\log 2-[c\log c-(c-1)\log(c-1)]` is the Cramér rate function for the sum of geometric gaps. This is a *large-deviation* statement with an explicit rate, not the textbook two-sided Chernoff bound. **Fix:** either add a two-line exponential-Chebyshev derivation, or cite Dembo–Zeitouni. As written, "the geometric Chernoff bound" names no theorem a referee can look up. |
| 464 | "The mean is \(D+r/2\), so Hoeffding yields \(\exp(-r^2/2(J-1))\)" | **no citation, no proof** | Correct: this is Hoeffding's inequality for `Bin(J-1,1/2)` at deviation `r/2`, giving `exp(-2(r/2)^2/(J-1)) = exp(-r^2/(2(J-1)))`. **Fix:** cite Hoeffding, *J. Amer. Statist. Assoc.* **58** (1963), 13–30, DOI `10.1080/01621459.1963.10500830`. |
| 2657 | "Doob's weak \(L^1\) maximal inequality gives \(\Pr(R_n\ge t)\le t^{-1}\)" | **no citation, correctly applied** | I checked this rather than assuming it. `R_n = \max_{0\le j\le n} W_j` is defined at line 2640 as a running **maximum**, and `(W_j)` is a nonnegative martingale with `E(3\cdot 2^{-A_i}) = 3\sum_{a\ge1}4^{-a} = 1`, so `W_0=1` and Doob gives `Pr(R_n\ge t)\le E[W_0]/t = 1/t`. **The attribution is correct** — this is genuinely Doob and not merely Markov. **Fix:** add a textbook pointer (Durrett, *Probability: Theory and Examples*, or Williams, *Probability with Martingales*, §14.6). |
| 604, 2755, 2805 | "Minkowski", "Minkowski and Cauchy-Schwarz" | no citation | Minkowski's **inequality** (triangle inequality in `L^2`) and Cauchy–Schwarz. Standard; **no citation needed**. Note this is *not* Minkowski's lattice-point theorem, which the audit brief's phrasing might suggest — no geometry-of-numbers result is used anywhere in the manuscript. |

Also invoked without citation and correctly needing none: Stieltjes-type summation (lines 49, 528,
2078, 2227) and Abel summation (line 1745).

---

## 3. Bibliography-style compliance (JTNB)

Verified by an actual clean build (see `SELF_CONTAINMENT_CHECK.md`):

- `\usepackage[numbers]{natbib}` + `\bibliographystyle{plainnat}` produces a **numbered** reference
  list, sorted **alphabetically by author** (confirmed from the generated `.bbl`: Applegate ×4,
  Bernstein, Everett, Lagarias ×2, Lagarias–Weiss, Matthews–Watts ×2, Rozier, Rozier–Terracol,
  Stérin, Tao, Terras). Alphabetical ordering therefore already satisfies JTNB's
  *"par ordre alphabétique"*.
- **But** JTNB requires `jT.cls` and forbids replacing the template's bibliography commands
  (*"il est important de ne pas remplacer les commandes du fichier exemple.tex pour … la
  bibliographie par d'autres commandes"*). `natbib` + `plainnat` + `\citep` is exactly such a
  replacement. See `JOURNAL_FIT.md` §2 for the conversion.

---

## 4. Summary of required citation actions

| # | Severity | Action |
|---|---|---|
| C1 | **BLOCKING** | Place `CP17_REFERENCES.bib` alongside `CP17_MANUSCRIPT.tex`. It currently exists only inside `CP17_EXTERNAL_REFEREE_PACKAGE_V1.zip`. |
| C2 | **BLOCKING** | Replace the `Rozier2019` entry (§1.2a): the `doi` field points at a Zenodo deposit, not the article of record. |
| C3 | should-fix | Rename `Sterin2019` → `Sterin2020` and complete the proceedings metadata (§1.2b). |
| C4 | should-fix | Add "(numbering follows the published version, Forum Math. Pi 10 (2022), Paper No. e12)" at `.tex` line 47 — arXiv `1909.03562` is at v7, revised **after** publication. |
| C5 | should-fix | Verify or delete the unverified quantitative claim about Tao's exponent on PDF page 2 (§2.1). It is the only never-checked literature assertion in the paper. |
| C6 | should-fix | Fix the plural at `.tex` line 59: "survey and bibliographies" → "survey and annotated bibliography" (or add `arXiv:math/0608208`). |
| C7 | polish | Cite Hoeffding 1963 (line 464) and a textbook for Doob (line 2657); either cite or prove the geometric large-deviation bound (line 324). |
| C8 | polish | `MatthewsWatts*`: use `K. R. Matthews and A. M. Watts` to match the record of publication. |
| C9 | polish | Add Lagarias (ed.), *The Ultimate Challenge*, AMS 2010 (`10.1090/mbk/078`). Optionally Krasikov–Lagarias, Acta Arith. **109** (2003), 237–258 (`10.4064/aa109-3-4`) — verified, but not needed by any proof. |

**No citation in this manuscript misrepresents its source.** The two defects (C2, C3) are metadata
hygiene; C4 and C5 are about pinning a moving target. That is a good result for a bibliography of
this size.
