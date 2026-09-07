# A4 zero-trust package audit — prefix_bridge_20260906

Auditor: independent A4 lane (lead_parallel_20260907). Date: 2026-09-07 (UTC 2026-09-06 ~21:10).
Package under audit: `research_manager/exploratory/prefix_bridge_20260906/` (20 files) plus sibling `prefix_bridge_20260906.zip`.
Nothing inside the package was modified or executed; no tracked file was touched; no commit/push. All artefacts of this audit live in this directory and are hashed in `SHA256SUMS.txt` (this directory).

## VERDICT: [VALID WITH WORDING REPAIR]

The mathematics of `derivation/EXACT_PREFIX_REDUCTION.md` (exact row-phase connection, four-prefix pathwise identity, conditional uniform/independent law, scalar mixture (M), logarithmic prefix-excess cutoff (C)/(T)) was rebuilt from the definitions with exact integer/`Fraction` arithmetic and holds on every tested instance; the proofs were re-read line by line and are correct with the stated domains. Package integrity (hash lists, ZIP, V2 output hash, two-line V1→V2 diff) is confirmed byte-for-byte. The required repairs are all in the *persistence/publication narrative* of `README.md`, which asserts a GitHub preservation branch and publication receipts that do not exist; the science files themselves (`MANAGER_REVIEW.md`, `MANAGER_SCOPE.md`) correctly say no GitHub/Drive publication was performed.

Required wording repairs (none load-bearing for the mathematics):

1. `README.md` "GitHub preservation branch: codex/prefix-bridge-20260906-persistence, based on 1a6f924…": the branch exists **only locally**, points at `1a6f924` = `origin/main` with **zero commits** on top (`git rev-list --count origin/main..HEAD` = 0), and is **absent from origin** (`git ls-remote --heads origin` lists 39 heads, none containing "prefix"). The package directory and ZIP are **untracked** (`git ls-files research_manager/exploratory` → 0 files; `git status` → `?? research_manager/exploratory/`). Replace with: "a local branch name was created; nothing has been committed or pushed."
2. `README.md` "published at the user's explicit request" / "Publication receipts live beside the package and supersede those persistence statements": no receipt file exists beside the package (`research_manager/exploratory/` contains only the package dir, the ZIP and this audit lane). The still-accurate statements are those of `MANAGER_REVIEW.md`/`MANAGER_SCOPE.md` ("No GitHub/Drive push … performed"). Delete the supersession sentence or replace it with the truth.
3. `README.md` Drive folder link: NOT VERIFIABLE from this audit (no Drive access attempted); should be labelled unverified until a read-back receipt exists.
4. Minor precision (optional): `checks/REPORT.md` should say explicitly that the producer checker tests the **three**-prefix split `B_r = 3^(r-3)B_3 + 2^s B_tail` (it does), while the derivation's load-bearing identity is the **four**-prefix split (P); the four-prefix identity is covered only by the package auditor's `independent_row_checks.py` and by this audit.
5. Minor precision (optional): the two JSON result files are CRLF (Python `write_text` on Windows); all other 18 files are LF. The hash lists were computed on the as-stored (CRLF) bytes; an LF-normalised `RESULTS_V2.json` hashes to `8d45373e…`, not `3b6fe2ac…`. The `.gitattributes` `* -text` is therefore genuinely necessary (repo has `core.autocrlf=true`) but is currently inert because nothing is tracked. Worth one sentence in README.

## A. Integrity — PASS (with the CRLF note above)

Evidence: `audit_integrity_stdout.txt`, `audit_integrity_results.json`, `v1_v2_diff.txt`, `git_evidence.txt` (all real redirected stdout).

| Item | Result | Evidence |
|---|---|---|
| SHA256SUMS.txt (16 entries) vs recomputed on-disk SHA-256 | PASS 16/16 match; `sha256sum -c` exit 0 | audit_integrity_stdout.txt |
| PACKAGE_SHA256SUMS.txt (19 entries = 16 + README.md + .gitattributes + SHA256SUMS.txt) | PASS 19/19 match; `sha256sum -c` exit 0; only unlisted file is PACKAGE_SHA256SUMS.txt itself (self-hash impossible; its hash is `1a460a8c53d3ef5c…`) | audit_integrity_stdout.txt |
| CRLF/LF | Only `checks/RESULTS.json` (41426 CRLF) and `checks/RESULTS_V2.json` (248 CRLF) contain CRLF; 18 other files pure LF. Hash lists match the CRLF bytes as stored. | audit_integrity_results.json `files.*.crlf_count`, `sha256_lf_normalised` |
| .gitattributes `* -text` | Correct semantics; `git check-attr text` → `unset` for package paths; repo `core.autocrlf=true`, so without it a fresh non-Windows checkout would break the two JSON hashes. Currently inert (untracked). | git_evidence.txt |
| ZIP members | PASS: 20 members, 20/20 byte-identical to on-disk files, none missing either way. ZIP SHA-256 `36d0666ec20be4bb7b1341c33166140620c7e8d952c4fb15314c6863b571943f` (ZIP itself is untracked and not listed in any package hash list). | audit_integrity_stdout.txt |
| Claim "V2 output hash = 3b6fe2ac8166…ce084c3d" | PASS: exactly one on-disk file has this hash: `checks/RESULTS_V2.json`. `RESULTS_V2.json` internally records `source_sha256 = ed6aced4…` = on-disk V2 source hash and `plan_sha256 = 3a3fb9b5…` = on-disk PLAN.md; `input_hashes_unchanged: true`. V1 JSON likewise records `2efe6a8c…` = on-disk V1 source. | audit_integrity_stdout.txt |
| Claim "V1→V2 diff is exactly two substitutions" | PASS: `diff -u` shows exactly two changed lines (line 36 output filename `RESULTS.json`→`RESULTS_V2.json`; line 68 tail denominator `16*3**(r-3)`→`16*3**r`); reversing the two substitutions with `sed` on V2 gives a byte-identical V1 (`reverse_diff_exit=0`). | v1_v2_diff.txt |
| V1 JSON content | 2935 paths, 23480 checks, 2935 failures, all in `phase_concatenation`; V2 JSON: 2935 paths, 23480 checks, 0 failures. Timestamps V1 20:37:58Z < V2 20:39:29Z consistent with narrative. | audit_integrity_stdout.txt |
| Producer/auditor scripts import no producer module | PASS by static read: V2 imports fractions/itertools/pathlib/datetime/hashlib/json/math/time only; `independent_row_checks.py` imports fractions/math/json only. | package sources (read only) |
| "GitHub preservation branch" | FAIL as worded (see repairs 1–2). Local branch only, 0 commits, package untracked, no remote branch. | git_evidence.txt |
| Drive folder | NOT VERIFIABLE | — |
| INDEPENDENT_ROW_CHECK_OUTPUT.json | NOT VERIFIABLE as raw stdout (honestly labelled "transcribed"); its counts 1161/1161/20/60 are reproduced independently below. | audit_recompute_stdout.txt section F |

## B. Mechanical reproduction without producer code — PASS

Script: `audit_recompute.py` (own code, direct power-sum definition of `B_r`, `fractions.Fraction`/int only; mpmath only for an illustrative margin report). Output: `audit_recompute_stdout.txt`, `audit_recompute_results.json`. Overall `PASS`, 0 failures, 1.9 s.

| Protocol item | What was checked | Result |
|---|---|---|
| B(i) pathwise identity | r=5..9, n=0..5, all 4795 weak compositions: `B_r(a) = 3^m B_4(p) + 2^(4+j) B_m(b)` (integer) and `B_r/(16·3^r) = B_4/1296 + 2^j B_m/3^(m+4)` as **exact rational equality** (hence also mod 1) | PASS 4795/4795 both |
| B(ii) row-phase connection | Sum of analytic row exponents `1/48 + Σ_{s≥2} 2^(s+S_(s-1)-5)/3^s` (negative powers of two kept as rationals) equals `B_r/(16·3^r)` as **exact rational equality**, not only mod 1 | PASS 4795/4795 |
| §2 claims | `B_r` odd; `B_r mod 16` = first four summands mod 16; key `(r mod 4, min(a_1,4), min(a_2,4), min(a_3,4))` determines `B_r mod 16` (176 keys seen, no inconsistency, residues = all 8 odd classes); CRT `B/(16·3^r) = uB/3^r + vB/16` exactly with `16u+3^r v=1`; `v` odd and `e_16(vB) ≠ 1` on every path | PASS 4795/4795 each |
| B(iii) mixture (M) | For each of 30 (r,n): residue-count vector `{B_r(a) mod 16·3^r}` over all a equals the convolution `Σ_j (counts of 3^m B_4(p) mod M, p∈WC(j,4)) * (counts of 2^(4+j) B_m(b) mod M, b∈WC(n−j,m))` — an exact identity in the cyclotomic field (stronger than complex equality). Uniform+independent conditional law: for every j the set of (prefix,tail) pairs realised by compositions with J=j equals the full Cartesian product with cardinality `C(j+3,3)·C(n−j+m−1,m−1)`. `Σ_j w(j) = 1` exactly. Illustrative 50-digit numeric: max |G − Σ w D H| = 1.4e−50. | PASS 30/30 each |
| B(iv) cutoff (C) | r=5..12, n=0..10, L=0..n (528 triples), exact Fractions: `P(J>L) ≤ 4 (n/(n+r−1))^q`, `q=⌊L/4⌋+1`; also each proof step: `P(z_1≥q) = C(n−q+r−1,r−1)/N = Π_{h<q}(n−h)/(n+r−1−h) ≤ (n/(n+r−1))^q` and union bound `P(J>L) ≤ 4P(z_1≥q)`; the J- and z_1-marginals were brute-forced from the uniform law for the 409 triples with N ≤ 20000 | PASS 528/528 every step; 409/409 brute-force agreement |
| Critical target | `n_r = ⌊βr⌋−8` computed exactly as `bit_length(3^r)−1−r−8`; table r=10..17 → −3,−2,−1,−1,0,0,1,1 (so r=12,13 excluded, r=14,15 give n=0, conditional law exists iff r≥14); for r=14..2000: `n_r ≥ 0` and the **exact integer inequality** `2^(n_r+r−1) ≤ 3^(r−1)` (⇔ `n_r ≤ β(r−1)` ⇔ `n_r/(n_r+r−1) ≤ ρ`) hold; 60-digit min margin `β(r−1)−n_r = 7.4151…` (never near 0); cutoff chain `q>L_r/4`, `ρ^q ≤ r^(−1−δ)` confirmed numerically for δ∈{0.1,0.5,1}, r=14..2000 (5961/5961) | PASS |
| E. Producer's 8 checks re-implemented from PLAN.md over its 31 declared cases | 2935 paths, 23480 checks; with the V1 tail denominator `16·3^(r−3)` the phase-concatenation test fails on **all 2935** paths; with `16·3^r` it fails on **0**; the other 7 checks fail on 0; 176 residue keys; residues {1,3,…,15}; r=16 sample reproduced exactly (`B=71613463, u=40356301, v=−15`, project exponent `71613463/688747536`, ternary `28689622/43046721`, mod-16 `7/16`, ternary−project = `9/16`); r=4 witness `65/1296 = 19/432+8/1296` vs V1's wrong `19/432+8/48 = 91/432` | PASS — matches REPORT.md/RESULTS*.json exactly |
| F. Quoted counts | Auditor 1161 paths (r=5..8,n=0..4), 20 pairs, 60 cutoff triples; producer 31 cases, 2935 paths, 23480 checks | PASS |

## C. Mathematical scope review of derivation/EXACT_PREFIX_REDUCTION.md — PASS

- §1 row-phase connection. Cross-checked against the frozen `research_manager/results/CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE0/…_PROJECT_DEFINITIONS.md` (tracked): `ζ_4 = exp(2πi/48)`, rows `exp(2πi·2^(s+j−5)/3^s)` with `j=S_(s−1)`, `n_r=⌊βr⌋−8`, `β=log_2 3 − 1`. With `A_(s−1)=s−1+S_(s−1)` each row exponent is `2^(A_(s−1))/(16·3^s)` including s=1, and the sum is `B_r/(16·3^r)` as a rational number (verified exactly). Negative powers of two are handled analytically, not by modular inverse. Correct.
- Domains. `r≥5 ⇔ m≥1` needed so that the tail is non-empty; r=4 correctly excluded from (P)/(M). `n≥0` arbitrary; `n=0` and `k=0` are covered (`C(m−1,m−1)=1`). Critical target: `n_r ≥ 0 ⇔ r ≥ 14` (exact table above); r=14,15 have n=0 (degenerate single path, identities hold trivially); r=12,13 have n=−1 and are correctly excluded. Correct.
- §2. All statements verified (oddness of `B_r` and of `v`, first-four-summand reduction, 64 labels per r mod 4, CRT split, non-triviality of `e_16(vB)`). The negative statement (no finite tail-frequency closure) is a correctly hedged non-claim.
- §3. Split of the sum is a two-line identity (verified symbolically and on 4795+2935 paths). Conductor `3^(m+4)=3^r` is right; `2^j` is a unit mod 3 so no cancellation; `B_4` depends on `p_1,p_2,p_3` only. Correct.
- §4. Bijection `a ↔ (p,b)` at fixed `J=j` is exact; equal weights `1/N` give uniform × uniform independence; `Σ_j w = 1` is Vandermonde. (M) is the expectation of (P). Offset formula `4β−8−θ_r−j` rechecked. Correct.
- §5 cutoff lemma. Quantifier order is right: δ>0 fixed first, then `L_r` defined, then the bound holds for **every** r≥14 with the uniform constant 4. Steps: translation identity (exact), product with each factor `(n−h)/(n+r−1−h) ≤ n/(n+r−1)` (valid since `h≥0`, `n+r−1−h ≥ r > 0`), `q>n` ⇒ probability 0, pigeonhole `J>L ⇒ some z_i ≥ ⌊L/4⌋+1` (if all four ≤ ⌊L/4⌋ then J ≤ 4⌊L/4⌋ ≤ L), union bound + exchangeability (no independence needed). `n_r ≤ βr−8 ≤ β(r−1)` uses `β<8`; `x ↦ x/(x+r−1)` increasing gives `≤ ρ=β/(1+β)`. With natural logs, `q > L_r/4 ≥ (1+δ)ln r/|ln ρ|` and `ρ<1` give `ρ^q < exp(−(1+δ)ln r) = r^(−1−δ)`; the claimed `4r^(−1−δ)` follows and is `o(1/r)` since `4r^(−δ)→0`. Correct.
- Use of `|D_j H| ≤ 1` in (T): `|G − S_L| = |Σ_{j>L} w_j D_j H_j| ≤ Σ_{j>L} w_j = P(J>L)`, where `|D_j|,|H_j| ≤ 1` because both are averages of unit-modulus numbers. Correctly used (only the tail j>L is bounded; nothing is claimed about the retained terms).
- §6. "Signed truncated-sum bound is logically equivalent to G=O(1/r) up to the remainder": correct — `G = S_L + R`, `|R| ≤ 4r^(−1−δ) = o(1/r)`, so `S_L=O(1/r) ⇔ G=O(1/r)`. Triangle-weighted bound ⇒ signed bound (triangle inequality), and follows from a uniform `|H| ≤ C/r` (since `|D|≤1`, `Σw≤1`); it is sufficient, not necessary; its failure would not refute `G=O(1/r)`. All correctly stated, and no reduction of difficulty is claimed. (OPEN) is honestly labelled.
- Overclaim scan of README/MANAGER_REVIEW/FINAL_AUDIT: mathematical claims are all hedged correctly (no O(1/r), no nonzero coefficient, no Collatz). The only overclaims are the README persistence statements (repairs 1–3). `MANAGER_REVIEW.md`'s claim "Output hash independently checked by manager: 3b6fe2ac…" is TRUE for `checks/RESULTS_V2.json`.

## D. Claims table

| # | Claim (source) | Independent status |
|---|---|---|
| 1 | Row phases multiply to `e_(16·3^r)(B_r)` (derivation §1; FINAL_AUDIT) | PASS — exact rational identity, 4795 paths; definition matches frozen PROJECT_DEFINITIONS |
| 2 | `B_r mod 16` = first four summands; determined by r mod 4 and `min(a_i,4)`, i≤3; ≤64 labels per residue (§2; INITIAL_AUDIT) | PASS |
| 3 | CRT split `e_(16·3^r)(B)=e_(3^r)(uB)e_16(vB)`, second factor never 1 (§2; checker categories bezout/crt_fraction/oddness/nontrivial) | PASS — exact, all paths |
| 4 | Four-prefix identity `B_r = 3^m B_4 + 2^(4+j) B_m`, phase (P) with conductor `3^(m+4)` (§3; FINAL_AUDIT) | PASS — exact, 4795 paths |
| 5 | Conditional law: given J=j, prefix/tail uniform and independent; `Σ w = 1`; mixture (M) (§4) | PASS — Cartesian-product bijection and exact residue-vector identity, 30 (r,n) cases |
| 6 | Cutoff inequality (C) `P(J>L) ≤ 4(n/(n+r−1))^(⌊L/4⌋+1)` (§5) | PASS — exact, 528 triples + brute-force marginals; proof steps re-derived |
| 7 | `n_r ≤ β(r−1)`, ratio ≤ ρ, r≥14 domain, r=14,15 n=0, r=12,13 excluded (§1, §5) | PASS — exact integer inequality r=14..2000, margin ≥ 7.4; table r=10..17 |
| 8 | `P(J>L_r) ≤ 4r^(−1−δ)` and truncation error (T) `= o(1/r)`, natural logs (§5; MANAGER_REVIEW "rigorous elementary lemma") | PASS — proof correct; numerically confirmed r=14..2000, δ∈{0.1,0.5,1} |
| 9 | Signed truncated bound ⇔ G=O(1/r) up to remainder; triangle-weighted bound sufficient, not necessary (§6; FINAL_AUDIT) | PASS (logic correct); the bounds themselves OPEN |
| 10 | G=O(1/r), nonzero coefficient, lower bounds, Collatz: NOT established (all files) | Correctly stated as OPEN |
| 11 | V1 checker: 2935 paths, 23480 checks, 2935 failures all in phase_concatenation, cause = denominator `16·3^(r−3)` (REPORT, PRE_EXECUTION_PROVENANCE, FINAL_AUDIT) | PASS — JSON parsed; failure reproduced on all 2935 paths by independent re-implementation; r=4 witness reproduced |
| 12 | V2: exactly two substitutions; 0 failures; output hash `3b6fe2ac…` (REPORT, V2_REPAIR, MANAGER_REVIEW, README) | PASS — diff produced; hash matches `checks/RESULTS_V2.json`; all checks pass in independent re-implementation |
| 13 | 176 residue keys, all 8 odd residues, r=16 sample values incl. "ternary − project = 9/16" (REPORT) | PASS — reproduced exactly |
| 14 | Auditor counts 1161/1161/20/60 (FINAL_AUDIT, MANAGER_REVIEW) | PASS (counts reproduced; the transcribed output file itself NOT VERIFIABLE as raw stdout, honestly labelled) |
| 15 | Hash lists and ZIP preserve the package byte-for-byte (README) | PASS (16/16, 19/19, ZIP 20/20) |
| 16 | `.gitattributes` byte-preserving (README) | PASS in semantics; inert while untracked |
| 17 | "GitHub preservation branch codex/prefix-bridge-20260906-persistence" (README) | FAIL as worded — local-only branch, 0 commits, package untracked, not on origin |
| 18 | "published … publication receipts live beside the package" (README) | FAIL — no receipts exist; MANAGER_REVIEW's "no push performed" is the true state |
| 19 | Drive folder (README) | NOT VERIFIABLE |
| 20 | Wall times, UTC timestamps, "executed exactly once" (REPORT) | NOT VERIFIABLE beyond internal JSON consistency (timestamps ordered V1<V2, hashes consistent) |

## Files produced by this audit (all in this directory)

- `audit_integrity.py`, `audit_integrity_stdout.txt`, `audit_integrity_results.json` — item A
- `audit_recompute.py`, `audit_recompute_stdout.txt`, `audit_recompute_results.json` — items B/C(E,F)
- `v1_v2_diff.txt` — real `diff -u` plus reverse-substitution check
- `git_evidence.txt` — read-only git commands (remote heads, tracking, status)
- `AUDIT_VERDICT.md` — this file
- `SHA256SUMS.txt` — hashes of all of the above

Nothing in this audit proves the Collatz conjecture; the triangle-weighted bound and G=O(1/r) remain OPEN.
