# CLAIMS_WORDING_AUDIT — CP17 manuscript

All line numbers refer to `C:/Users/MDP/Downloads/CP17_MANUSCRIPT.tex` (2 844 lines,
sha256 `42bed9aa…39dab`). Quotations are exact.

---

## 0. Headline

The scope discipline in this manuscript is **unusually good** and I want to say so before the
criticism. An adversarial scan for priority language (`first`, `novel`, `new`, `previously unknown`,
`breakthrough`, `resolves`, `settles`, `best known`, `strongest`, …) over every prose line finds
**zero** priority claims. Every occurrence of "first" is ordinal ("the first \(t\) valuations",
"first fix \(c\)"). The negative-scope disclaimer is stated **four separate times** — abstract
(line 36), introduction (line 55), immediately after the main theorem (line 143), at the end of the
final-contradiction section (line 1370) — and then given its own section, §15 *Scope and limitations*
(line 1372). That is more self-restraint than most published papers show.

The findings below are therefore about **precision**, not about honesty.

| Class | Count | Severity |
|---|---|---|
| Numbered statements missing hypotheses inside the environment | 3 of 8 | **W1 — blocking** |
| Missing uniformity/implied-constant qualifier | 2 | **W2 — blocking** |
| Sentence pointing at a document the referee does not have | 3 | **W3 — blocking** |
| Symbol overloading (`A`) | 6 distinct meanings | **W4 — should fix** |
| Notation inconsistency (`\chi`, `p`) | 2 | W5 — polish |
| Constants stated consistently? | **yes, verified to 21 digits** | — |

---

## 1. Inventory of every numbered statement

Eight numbered environments (2 `theorem`, 6 `lemma`; verified by counting `\begin{}` occurrences —
`theorem: 2`, `lemma: 6`, `proof: 6`).

| # | Line | Environment / label | Statement (abridged) | Hypotheses **inside** the env? |
|---|---|---|---|---|
| T1 | 102–141 | `theorem` `thm:main-additive` — "Harmonic bound and additive constraint" | `limsup H_N/loglog N ≤ K₁₇ < 2.742882 < 3`; `β₀=4(α−1)/(α+2)`, `I(c)=c log2−[c log c−(c−1)log(c−1)]`, `K₁₇=β₀log2/(3I(α))`; hence `∄C,k₀: s_k ≤ log₂k+C`, so `limsup(s_k−log₂k)=+∞` | **NO** |
| T2 | 597–602 | `theorem` `thm:syracuse-collision-energy` — "Polynomial Syracuse collision energy" | `χ_s^Syr = O(s⁴)` | **NO** |
| L1 | 382–390 | `lemma` `lem:parity-prefix-bijection` — "Parity-prefix bijection" | `x mod 2^J ↦ (e₀(x),…,e_{J−1}(x))` is a bijection `Z/2^J Z → {0,1}^J` | yes ("For every `J≥1`") |
| L2 | 682–684 | `lemma` `lem:uniform-polynomial-bookkeeping` — "Uniform polynomial bookkeeping" | rounding/binomial-tail/ceiling/slice factors contribute `O_{ε,ρ}(log(t+1))` | **NO** |
| L3 | 912–921 | `lemma` `lem:endpoint-rectangle` — "Endpoint rectangle; λ=1" | `x < 2^m`, first `m` shortcut steps have exactly `s` odd steps ⟹ `T^m(x) ≤ 3^s−1` | yes |
| L4 | 1784–1795 | `lemma` `lem:bounded-distance-reciprocal-pair-graph` — "Bounded-distance reciprocal pair graph" | for any finite injective positive `x₀,…,x_{M−1}` and `t≥2`, `Σ_{j−i≤t} 1/(x_i x_j) = O((log(t+1))²)` "with an absolute constant" | yes — **model statement, see §2** |
| L5 | 2354–2356 | `lemma` `lem:reachable-representatives` (untitled) | if a class `y mod Q_t` contains one genuinely admissible terminal for `a`, every positive `Y ≡ y` is a terminal of a positive unit length-`t` past with the same valuation word | yes |
| L6 | 2573–2575 | `lemma` `lem:offset-injectivity` — "Injectivity of the offset map" | `G_n : (N_{≥1})^n → Q` is injective | yes |

---

## 2. **W1 (blocking)** — three statements are not self-contained

L4 (line 1784) shows the author can do this properly:

> "For any finite injective sequence of positive integers \(x_0,\ldots,x_{M-1}\) and any integer
> \(t\ge2\), […] with an absolute constant."

Quantifier, hypothesis, uniformity: all inside the environment. T1, T2 and L2 do not meet that bar.

### 2.1 T1 — the main theorem (line 102)

The environment opens directly with a display. Its hypotheses live in unnumbered ambient prose at
lines 71–100, above the environment:

> line 77: "be a \textbf{positive injective odd-only Syracuse orbit}. Put"

A theorem whose hypotheses are in the paragraph above it cannot be quoted, cited, or checked in
isolation. This is the **first** thing a JTNB referee will write down.

> **Proposed replacement.** Insert as the opening sentence of the `theorem` environment at line 103,
> before the existing `\[`:
>
> ```latex
> Let \((n_k)_{k\ge0}\) be a positive injective odd-only Syracuse orbit, that is,
> \(n_{k+1}=(3n_k+1)/2^{a_k}\) with \(a_k=v_2(3n_k+1)\ge1\), all \(n_k\) positive odd and
> pairwise distinct. Put \(\alpha=\log_23\), \(A_k=\sum_{i<k}a_i\),
> \(s_k=\lfloor\alpha k\rfloor-A_k\) and \(H_N=\sum_{k<N}1/n_k\). Then
> ```

### 2.2 T2 — the collision-energy theorem (line 597)

The entire environment is:

```latex
\begin{theorem}[Polynomial Syracuse collision energy]\label{thm:syracuse-collision-energy}
\[
\boxed{\chi_s^{\rm Syr}=O(s^4).}
\tag{7.1}\label{eq:body-7-1}
\]
\end{theorem}
```

Neither `χ_s^Syr` nor its underlying random variable appears in the statement; both are defined at
lines 586–595 outside it. This is the paper's **headline estimate** — the one the abstract leads
with and the one whose novelty §2 argues for. It should be quotable.

> **Proposed replacement** for lines 597–602:
>
> ```latex
> \begin{theorem}[Polynomial Syracuse collision energy]\label{thm:syracuse-collision-energy}
> For \(s\ge1\) let \(A_1,\ldots,A_s\) be independent with \(\Pr(A_i=a)=2^{-a}\) \((a\ge1)\), put
> \(S_j=A_1+\cdots+A_j\), let
> \[ X_s=\sum_{j=1}^s3^{j-1}2^{-S_j}\pmod{3^s},\qquad p_s(y)=\Pr(X_s=y), \]
> and set \(\chi_s^{\rm Syr}=3^s\sum_{y\bmod3^s}p_s(y)^2\). Then
> \[ \boxed{\chi_s^{\rm Syr}=O(s^4)} \tag{7.1}\label{eq:body-7-1} \]
> with an absolute implied constant.
> \end{theorem}
> ```

### 2.3 L2 — the bookkeeping lemma (line 682)

Exact text:

> "All integer rounding, binomial-tail, ceiling, and finite-slice factors used below contribute only
> \(O_{\varepsilon,\rho}(\log(t+1))\) to a logarithmic count, uniformly on this compact parameter set."

Three unresolvable deictics: **"used below"** (which factors? the lemma is unfalsifiable as
written), **"a logarithmic count"** (which one?), **"this compact parameter set"** (never named in
the statement). The proof that follows is perfectly good and enumerates five concrete items; the
*statement* does not.

> **Proposed replacement** for line 683:
>
> "Fix \(\varepsilon,\rho>0\) and let \(\mathcal P_{\varepsilon,\rho}\) be the compact parameter set
> of \eqref{eq:body-10-9}ff. Let \(\Pi(t)\) be any product of at most \(d\) factors, each of which is
> a ratio of binomial coefficients with parameters shifted by \(O(1)\), a binomial tail, a ceiling
> \(\lceil3^s/2^j\rceil\), or a slice count bounded by \(O(t)\), with \(d\) fixed. Then
> \(\log\Pi(t)=O_{\varepsilon,\rho,d}(\log(t+1))\), uniformly over \(\mathcal P_{\varepsilon,\rho}\)."

---

## 3. **W2 (blocking)** — missing uniformity qualifiers on the two `O`-statements

`O(s^4)` (line 599) and `O_{ε,ρ}(log(t+1))` (line 683) are asymptotic claims with **no stated
uniformity**. The manuscript demonstrably knows this matters: line 307 writes "with an absolute
implied constant", line 1794 writes "with an absolute constant", line 2140 writes "The error is
independent of \(N\) and \(c\)". T2 and L2 should carry the same qualifier.

For T2 the correct qualifier is **absolute** (there is no free parameter); it is supplied in the
replacement in §2.2 above. For L2 the qualifier must name the dependence explicitly
(`ε, ρ` and the fixed slice-exponent `d`), as in §2.3.

---

## 4. **W3 (blocking)** — three sentences point at documents the referee will not receive

These are the audit-internal leaks. All three survive into the submission PDF, verified on
PDF pages 2 and 20.

### 4.1 Line 65 (§2) — an appeal to an unavailable audit

> "The publication-level novelty claims are therefore restricted to statements for which the
> **accompanying literature audit** found no exact match, most notably this unconditional explicit
> global bound, the specific fixed-weight/prefix/harmonic synthesis, the certified coefficient
> \(K_{17}<3\), and the resulting additive-slack conclusion."

There is no accompanying literature audit in a JTNB submission. As written, the paper's novelty
claim rests on evidence the referee cannot see — the worst possible rhetorical position, and it
invites the reply "then let me be the judge."

> **Proposed replacement:**
>
> "The novelty claimed here is correspondingly narrow: an unconditional explicit global bound for
> the full distribution modulo \(3^n\), the specific fixed-weight/prefix/harmonic synthesis, the
> certified coefficient \(K_{17}<3\), and the resulting additive-slack conclusion. We are not aware
> of an exact prior statement of these, but we make no priority assertion."

### 4.2 Line 1382 (§16) — the paper disowns itself as the proof

> "**The frozen proof source is** \texttt{CP17\_FINAL\_STANDALONE\_PROOF\_V3.md}. The exact
> coefficient certificate is \texttt{CP17\_FINAL\_RATE\_CERTIFICATE\_V3.py}; […] The frozen package
> includes a SHA256 manifest and a dependency graph. **The publication branch** reran the
> coefficient certificate and verified the frozen package manifest before preparing this manuscript."

Four separate problems in one paragraph: (i) "**the frozen proof source is** [some other file]"
tells the referee that *this manuscript is not the proof* — fatal to a submission that is otherwise
genuinely self-contained; (ii) "frozen" and "publication branch" are internal version-control
jargon; (iii) neither named file is obtainable — no DOI, no URL, no repository; (iv) it reads as an
internal changelog.

> **Proposed replacement** — see `DISCLOSURE_DRAFT.md` §1 for the full paragraph. In outline:
>
> "All proofs in this paper are self-contained. The numerical values quoted in \eqref{eq:body-11-4}
> and \eqref{eq:body-11-5} are certified by a short script using exact rational and interval
> arithmetic, archived at [DOI]. It certifies \(\chi_1^{\rm Syr}=5/3\), \(\chi_2^{\rm Syr}=15/7\),
> \(4.916563<K_{11}<4.916564\) and \(K_{17}<2.742882<3\)."

### 4.3 Line 908 (§10.2) and line 2142 (Appendix A)

> line 908: "This is an editorial extraction of **the frozen fixed-weight transfer**: no new
> estimate is introduced."
>
> line 2142: "Thus the new theorem regresses correctly to **the CP9 fixed-\(t\) statement**."

`CP9` is an internal checkpoint identifier. It appears nowhere else in the manuscript, is defined
nowhere, and has no bibliography entry. A referee reading line 2142 has no way to know what "CP9" is.

> **Proposed replacement, line 908:**
> "No new estimate is introduced here; \eqref{eq:body-fw} is recorded only to exhibit the transfer in
> its most familiar form. The final coefficient proof below uses the pointwise bound directly and
> does not require this Stirling round trip."
>
> **Proposed replacement, line 2142:**
> "For fixed \(t\), \eqref{eq:a-7-1} reduces to the ordinary fixed-depth master inequality with an
> \(O_t(1)\) remainder."

*(A referee-facing note on line 908: the display it comments on, `(FW)` at lines 900–905, is boxed,
tagged and labelled `eq:body-fw` — and then never referenced anywhere in the manuscript. My
cross-reference scan confirms `eq:body-fw` is one of the unreferenced labels. Either reference it or
drop the tag; a boxed, numbered, never-used display reads as a leftover.)*

---

## 5. **W4 (should fix)** — the letter `A` carries six distinct meanings

Enumerated by scanning every `A`-with-subscript token in the source:

| Meaning | Symbol | Lines |
|---|---|---|
| (i) **individual** iid geometric gap | `A_1,…,A_n`, `A_i`, `A_j` | 43, 44, 586, 1622, 2509, 2512, 2515, 2650 |
| (ii) **cumulative sum** of deterministic valuations | `A_k=\sum_{i<k}a_i` | 80, 84, 86, 156 |
| (iii) cumulative sum, orbit form | `A_t(x)=a_0+\cdots+a_{t-1}` | 406, 412, 415 |
| (iv) cumulative sum, windowed | `A_{s,t}=a_s+\cdots+a_{s+t-1}`, `A_{k-t,t}` | 1558, 1564, 1583, 1920 |
| (v) entropy branch function | `A_\beta(x)=\beta H(x/\beta)` | 1094, 1096, 1103, 1162, 1229 |
| (vi) **affine permutation of `Z/3^n Z`** | `A_k(z)=4^kz+\frac{4^k-1}{3}` | 2824, 2831 |

(ii)–(iv) are one coherent family (`A` = accumulated valuation) and are fine.

Two real collisions:

**(a) (i) vs (ii)–(iv) — `A` is both a single gap and a sum of gaps.** In the probabilistic model
(line 586) `A_i` is *one* gap and `S_j=A_1+\cdots+A_j` is the *sum*. In the deterministic orbit
(line 80) `a_i` is one gap and `A_k` is the *sum*. So capital `A` means "gap" on one page and "sum
of gaps" on another, while "sum" is `S` in one convention and `A` in the other. This is exactly the
kind of thing that costs a referee twenty minutes and produces an irritated report.

> **Proposed fix (cheapest that works):** keep `A_i` for the random gaps (it matches Tao's
> convention, which §2 explicitly adopts) and rename the deterministic cumulative sum to `\Sigma_k`
> or `S_k^{\rm det}`. Alternatively add one sentence at line 88:
> "Throughout, lower-case \(a\) denotes a single valuation and upper-case \(A\) a partial sum of
> valuations along a deterministic orbit; in the probabilistic model of §7 the convention is Tao's,
> where \(A_i\) is a single random gap and \(S_j\) the partial sum."
> The sentence is cheaper than the renaming and removes the ambiguity.

**(b) (ii) vs (vi) — identical token `A_k`.** Line 80 defines `A_k` as a nonnegative integer;
line 2824 redefines `A_k(z)` as an affine map on `Z/3^n Z`, and line 2831 then writes `p_n(A_kz)`
**without the parenthesis**, so the token is literally `A_k` applied to `z`. Fix by renaming.

> **Proposed replacement, line 2824:** `\Phi_k(z)=4^kz+\frac{4^k-1}{3}\pmod{3^n}`, and
> correspondingly `C_n(k)=3^n\sum_z p_n(z)p_n(\Phi_k z)\le\chi_n^{\rm Syr}` at lines 2830–2832.

---

## 6. **W5 (polish)** — `\chi` and `p` superscript inconsistency

- **`\chi`.** The manuscript's standard notation is `\chi_n^{\rm Syr}` (15 occurrences). But
  **line 1382** (§16, reproducibility) writes `\(\chi_1=5/3\), \(\chi_2=15/7\)` with the `^{\rm Syr}`
  superscript **dropped**, while equation (11.5) at line 1322 correctly writes
  `\chi_1^{\rm Syr}=\frac53, \chi_2^{\rm Syr}=\frac{15}{7}`. Same quantities, two notations, sixty
  lines apart. Confirmed present in the submission PDF, page 20.
  > **Fix:** restore `^{\rm Syr}` at line 1382.
- **`p`.** Line 590 defines `p_s(y)=\Pr(X_s=y)`; line 893 writes `p_s^{\rm Syr}(y)`; the abstract
  (line 28) and introduction (line 45) write `p_n(y)`. Three spellings of one object.
  > **Fix:** pick `p_s^{\rm Syr}` (it pairs with `χ_s^{\rm Syr}` and with `p^{\rm fw}_{m,s}` at
  > line 882) and use it from line 590 onwards.
- **Index letter.** The abstract and introduction state the collision-energy bound with index `n`
  (`3^n Σ p_n(y)^2 = O(n^4)`, lines 28, 45–46); Theorem 7.1 states it with index `s`
  (`χ_s^{\rm Syr}=O(s^4)`, line 599). Harmless, but a reader checks twice.
  > **Fix:** use `n` in both, or note at line 586 that the index is renamed `s` to match the
  > fixed-weight parameter.

Everything else in the notation checklist is **consistent**: `α=log₂3` (line 80, 69 occurrences,
never redefined); `D_k=A_k−αk` (line 84, 8 occurrences); `s_k=⌊αk⌋−A_k` (line 86, 17 occurrences);
`H_N=Σ_{k<N}1/n_k` (line 99, 33 occurrences); `n_k`, `a_k` (32 / 6 occurrences); `C_n(k)` (lines
2830, 2838 only — defined at point of use). The identity `D_k=−s_k−{αk}` (line 92, boxed as (1.1))
is stated once and used consistently.

---

## 7. Constants — verified, and they check out exactly

I recomputed these independently at 40 decimal digits with `mpmath` rather than trusting the
certificate:

```
alpha    = log2(3)  = 1.58496250072115618145373894394781650876
beta0    = 4(alpha-1)/(alpha+2)
                    = 0.6526846521864418817074710275453727627425
I(alpha) = alpha*log2 - [alpha*log(alpha) - (alpha-1)*log(alpha-1)]
                    = 0.05497947281081707167285039039020556613374
K17      = beta0*log2/(3*I(alpha))
                    = 2.742881438765941863306094837987417771463
K17 < 2.742882      -> True
```

**All occurrences agree.** Every one was located by regex and compared:

| Constant | Lines | Value as printed | Verdict |
|---|---|---|---|
| `K_{17}` symbol | 30, 50, 65, 106, 122, 1305, 1315, 1335, 1349, 1382, 1384, 2245, 2258 (13×) | — | consistent |
| `K_{17}=\frac{\beta_0\log2}{3I(\alpha)}` | 122 (boxed, tag 1.3), 1305 (boxed, tag 11.3) | identical formula both times | **consistent** |
| `K_{17}<2.742882` | 30, 50, 106, 1315, 1382 | `2.742882` | **consistent, and true** |
| `K_{17}=2.742881438765941863306…` | 1335 | 21 significant digits | **matches my computation exactly** |
| `K_{17}` 20-digit form | 2245 | `2.7428814387659418633` | **correct truncation** of the line-1335 value (next digit is 0, so truncation and rounding agree) |
| `\beta_0=\frac{4(\alpha-1)}{\alpha+2}` | 114, 1120 (boxed, tag 10.9) | identical both times | **consistent** |
| `K_{11}=4.916563550949996880846…` | 1331 | — | consistent with the certificate's `4.916563 < K11 < 4.916564` |
| `\chi_1^{\rm Syr}=5/3`, `\chi_2^{\rm Syr}=15/7` | 1322–1324, 1382 | — | values consistent; notation inconsistent (§6) |

**One gap.** `β₀` is defined symbolically at lines 114 and 1120 and used fifteen times, but its
**numerical value `0.65268465…` is never printed anywhere in the manuscript** — a regex for
`0\.65\d*` returns zero hits. Since `K₁₇` is given to 21 digits, a reader who wants to check
`K₁₇=β₀log2/(3I(α))` by hand must first compute `β₀` themselves.

> **Proposed addition** at line 1126, inside the `(10.9)` display block or immediately after it:
>
> "Numerically \(\beta_0=0.6526846521\ldots\), \(\beta_{\rm sw}=0.8842282173\ldots\) and
> \(\beta_*=1.1699250014\ldots\)."
>
> (All three verified: `β_sw = 2α/(α+2) = 0.8842282173954806272…`,
> `β_* = 2(α−1) = 1.16992500144231236290…`.)

---

## 8. Does the abstract/introduction claim more than is proved?

**No.** I checked each claim against what the paper proves.

| Claim | Where | Proved? |
|---|---|---|
| `3^n Σ p_n(y)² = O(n⁴)` | abstract 28, intro 45–46 | yes — T2 (line 597) + Appendix C |
| `limsup H_N/loglog N ≤ K₁₇ < 2.742882 < 3` for every positive injective odd-only Syracuse orbit | abstract 30, intro 50 | yes — T1 (line 102), §13 (line 1305) |
| an eventual `s_k ≤ log₂k+C` forces coefficient 3 | abstract 32, intro 51 | yes — §4 (line 145), used at line 1343 |
| `limsup(s_k−log₂k)=+∞` | abstract 34, intro 52 | yes — §14 (line 1364) |
| does **not** prove Collatz / exclude cycles / exclude divergence / give `limsup s_k/log₂k>1` | 36, 55, 143, 1370, 1374 | correctly disclaimed, 4× |

Two soft observations, neither blocking:

**(a) `K₁₇` is undefined in the abstract.** Line 30 asserts `≤ K_{17}<2.742882<3` with no
indication of what `K₁₇` is. Abstracts are read in isolation (indexing services, MathSciNet).
> **Proposed replacement** for line 30–31:
> ```latex
> \[ \limsup_{N\to\infty}\frac{\sum_{k<N}1/n_k}{\log\log N}\le K_{17}<2.742882<3, \]
> where \(K_{17}=\beta_0\log2/(3I(\alpha))\) is an explicit constant in \(\alpha=\log_23\).
> ```

**(b) Title breadth.** The title is *"…and Additive Constraints on **Injective Collatz Orbits**"*
(line 18). The theorem is about *positive injective odd-only **Syracuse** orbits*. "Collatz orbits"
is the broader object. A hostile referee can read the title as promising more than §3 delivers.
> **Proposed replacement:** "…and Additive Constraints on Injective Syracuse Orbits."
> The running head (line 18, `[Collision Energy and Injective Collatz Orbits]`) would change
> correspondingly. **Judgement call** — "Collatz" is the searchable keyword and the abstract
> corrects the scope in its second sentence. Flagging, not insisting.

---

## 9. Priority-language check — clean

Adversarial scan over all prose lines for `first|novel|novelty|new|previously unknown|breakthrough|
resolves|settles|solves|establishes|unprecedented|best known|improved|strongest|only known`:

- **`first`**: 14 hits, all ordinal ("the first \(t\) valuations", "first fix \(c\)", "first-block
  weight"). **No priority use.**
- **`new`**: 2 hits — line 908 "no **new** estimate is introduced" (a *disclaimer*), line 2142 "the
  **new** theorem" (the paper's own, contrasted with the fixed-depth case). Both fine.
- **`novel`, `novelty`**: 1 hit, line 65, and it is *self-limiting* ("The publication-level novelty
  claims are therefore **restricted to** …"). Reworded in §4.1 above for a different reason.
- **`establish`**: 3 hits, all inside negative disclaimers ("does not establish…", "Nothing in the
  proof establishes that…").

This matches the internal novelty matrix's own rule — *"Do not replace this with 'the first proof,'
'previously unknown,' or 'novel'"* — and the manuscript obeys it. **No change required.**

---

## 10. Fix list, ordered

| # | Severity | Line(s) | Action |
|---|---|---|---|
| W1a | **blocking** | 102 | Put the orbit hypotheses inside `thm:main-additive` (§2.1) |
| W1b | **blocking** | 597 | Put the definition of `χ_s^Syr` inside `thm:syracuse-collision-energy` (§2.2) |
| W1c | **blocking** | 683 | Replace the deictic bookkeeping-lemma statement (§2.3) |
| W2 | **blocking** | 599, 683 | Add uniformity/implied-constant qualifiers (§3) |
| W3a | **blocking** | 65 | Delete the appeal to the "accompanying literature audit" (§4.1) |
| W3b | **blocking** | 1382 | Rewrite §16 so the manuscript is the proof, not a pointer to `*.md` (§4.2) |
| W3c | **blocking** | 908, 2142 | Remove "frozen" and the undefined "CP9" (§4.3) |
| W4a | should fix | 88 | One sentence reconciling the `a`/`A`/`S` conventions (§5a) |
| W4b | should fix | 2824, 2831 | Rename the affine permutation `A_k(z) → Φ_k(z)` (§5b) |
| W5a | polish | 1382 | Restore `^{\rm Syr}` on `χ_1`, `χ_2` (§6) |
| W5b | polish | 590, 893 | Settle on one spelling of `p_s^{\rm Syr}` (§6) |
| W5c | polish | 1126 | Print the numerical values of `β₀`, `β_sw`, `β_*` (§7) |
| W5d | polish | 30 | Say what `K₁₇` is in the abstract (§8a) |
| W5e | judgement | 18 | Consider "Syracuse" for "Collatz" in the title (§8b) |
| W5f | polish | 900–905 | Reference or de-tag the unused display `(FW)` / `eq:body-fw` (§4.3 note) |
