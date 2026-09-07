# CP17 referee pass — SUMMARY

Written by the research-manager session from the A5 referee lane's findings (the lane could not
write this file itself), with the manager's own verification of the blocking items marked below.
The manuscript was not modified. Nothing was committed or pushed.

Verdict: **ready to submit after the listed fixes.** Every blocking item is editorial or
packaging; none touches the mathematics.

## Blocking — must be fixed before submission

1. **The audited `.tex` is not the submission source.** [VERIFIED by the manager.]
   `CP17_JTNB_INITIAL_SUBMISSION_V3.pdf` page 1 prints the author name "Halil Talha Ertan", while
   every `.tex` available on this machine has `\author{}` empty (line 20, with a comment at line 19
   saying to insert it before submission). The PDF also carries an AI/LLM declaration and a Funding
   section; the `.tex` has only a `%`-commented disclosure note at line 1386, which does not render.
   All three copies of the source are byte-identical — `Downloads/CP17_MANUSCRIPT.tex`, the copy in
   `CP17_PUBLICATION_BRANCH_V3.zip`, and the copy in `CP17_EXTERNAL_REFEREE_PACKAGE_V1.zip` all
   hash to `42bed9aa997a771f…`, 74032 bytes. The source that actually produced the submitted PDF is
   not on this machine.
   Consequence beyond the fix: **the publication branch is not reproducible.** The project cannot
   currently rebuild its own submission PDF from its own recorded source. Find the real source
   before editing anything, or all three additions are silently reverted.
2. **`CP17_REFERENCES.bib` is not on disk.** [VERIFIED.] It exists only inside the two zips
   (16 entries: Terras1976 … RozierTerracol2026). As shipped on disk the manuscript cannot be built
   by anyone.
3. **`\author{}` and `\date{}` are empty** (lines 20-21); the PDF prints a bare name with no
   affiliation, postal address or email. JTNB requires postal and electronic addresses.
4. **Four audit-jargon leaks reach the reader**: "the accompanying literature audit" (l.65),
   "frozen" (l.908, l.1382), "publication branch" (l.1382), "CP9" (l.2142). Section 16 currently
   tells the reader that the real proof is a `.md` file and names two files no referee can obtain.
5. **Three of eight numbered statements are not self-contained**: Theorem 3.1 (l.102),
   Theorem 9.1 (l.597), Lemma 11.1 (l.683) place hypotheses outside the environment; the last is
   unfalsifiable as written ("used below", "this compact parameter set"). Both `O(.)` claims lack a
   uniformity qualifier.
6. **`Rozier2019`'s `doi` field points at a Zenodo deposit**, not the article of record.
7. **JTNB template gaps**: `jT.cls` not used, no French abstract, `natbib`/`plainnat` replaces the
   mandated bibliography commands. JTNB's AI declaration is mandatory and binds at submission.

## Non-blocking

The letter `A` carries six meanings (`A_k` is both a valuation sum at l.80 and an affine
permutation at l.2824). The `chi`/`p` superscripts drift (l.1382, l.590/893). `beta_0 = 0.65268465…`
is never printed numerically. `Sterin2019` has key-year 2020. Consider adding Lagarias, *The
Ultimate Challenge* (AMS 2010). Cite Hoeffding/Doob and either prove or cite the geometric
large-deviation bound. Two PDF bookmarks display raw LaTeX. Verify or delete the one never-checked
literature claim (Tao's `O(C_A^2)` exponent, PDF p.2).

## Already good

First independent compile in the project's history — the prior external referee had no TeX
toolchain. 38 pages, 0 errors, 0 warnings, 0 undefined references or citations, 0 bad boxes.
All 15 DOIs and 3 arXiv identifiers verify against Crossref, DataCite and arXiv; 16 of 16
bibliography entries are both cited and defined. `K_17 = 2.742881438765941863306…` reproduced
exactly at 40 digits, and every `K_17` and `beta_0` occurrence is consistent.

Zero priority overclaims: the scope disclaimer appears four times plus a dedicated section, and the
abstract states plainly that the result does not prove Collatz, does not rule out divergent orbits
or nontrivial cycles, and does not establish `limsup s_k / log_2 k > 1`.

Both simplifications the internal audits requested were adopted: Tao's Lemma 6.2 is replaced by a
self-contained 2-adic argument (l.2573), and the binomial round-trip is explicitly declared
non-load-bearing (l.910). The paper therefore now has **zero load-bearing literature dependencies**;
all 12 citations sit in sections 1-2.

## Effort

About one day for items 1-6, a second day for the `jT.cls` conversion and the French abstract.
Item 1 is a discovery rather than a repair and must be resolved first.
