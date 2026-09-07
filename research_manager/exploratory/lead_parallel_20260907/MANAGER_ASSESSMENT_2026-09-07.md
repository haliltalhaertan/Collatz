# Research-manager assessment — parallel lane round, 2026-09-07

Status: **WORKING ARTIFACT.** Not a canonical decision, not a milestone, not an acceptance.
No integrator lock was held or claimed. No tracked file was modified, no commit, no push, no
seal executed, no Stage-1 authorization created or consumed. Canonical `main` is untouched at
`1a6f924`. This document records the manager's own reading of four exploratory lanes and names
one recommended next action for the user to accept or reject.

## Lanes and their state

| Lane | Subject | State |
|---|---|---|
| A1 | B4 V2 launcher defect / V3 reseal design | complete; root cause confirmed from source, dry run PASS both directions |
| A2 | Exact numerical probe of the prefix bridge, r = 14..600 | complete; REPORT.md written by the manager from the agent's finished data after a rate-limit interruption |
| A3 | Analytic attack on the triangle-weighted lemma | complete |
| A4 | Zero-trust audit of the prefix_bridge_20260906 package | complete; verdict `[VALID WITH WORDING REPAIR]` |
| A5 | CP17 manuscript referee pass | complete; ready to submit after editorial fixes, but the submission source is missing |

## The load-bearing finding: the prefix bridge is a restatement, not a reduction

A3's central observation is that the modular reduction can be removed exactly. Since
`3^t = 2^(alpha t)` with `alpha = log_2 3`, every row phase is a real power of two:

```
e_{16*3^s}(2^(A_(s-1)))  =  exp(2 pi i * 2^(A_(s-1) - 4 - alpha s))
e_{3^(s+4)}(2^(j+A'_(s-1)))  =  exp(2 pi i * 2^(j + A'_(s-1) - alpha(s+4)))
```

Both are identities of real numbers, not congruences. I re-derived both exponents myself from
the definitions and confirmed the identity numerically at 60-digit precision (max deviation
2.67e-51). A float64 evaluation of the same identity deviates by 2.3e-05 for large exponents;
that is precision loss in the check, not a defect — noted so a later reader does not repeat it.

Consequently `G_{r,n}` and `H_{m,k}(j)` are the **same two-parameter family**: expectations of
`prod_s exp(2 pi i 2^(delta_s))` over the same mean-zero random-walk bridge, differing only in
length (r versus r-4) and in a constant shift of the left endpoint. [VERIFIED here, by
independent re-derivation.]

The consequence for the research plan is negative and should not be softened. The four-prefix
decomposition does not reduce the problem; it re-expresses `G` as a mixture of shorter instances
of itself. Controlling `|H_j|` at `j = 0` is already an E6-N2-strength statement at length r-4,
so the uniform-H hypothesis that the triangle-weighted lemma needs is **strictly harder** than
E6-N2 itself. [PLAUSIBLE, argued; not a formal proof of equivalence.]

A3 also reports that the "endpoint-offset drift `4beta-8-theta_r-j`" named in the derivation is
an artifact of the (k,m) parametrization: once `2^j` is absorbed into the walk, the right endpoint
is j-free and the whole drift sits in the left endpoint. I have not independently re-derived that
claim; it is consistent with the exponent algebra above. Flagged for a later check: A3 writes the
left endpoint as `j - 5*alpha`, while my own reduction of the same rows gives `j - 4*alpha - 1`
(7.34 versus 7.92). Not load-bearing for circularity, but the constant should be settled before
anything is built on it.

## Independent verification of A3's claims against A2's data

I checked A3's numerical assertions myself against the A2 tables rather than accepting them.

| A3 claim | My independent check | Result |
|---|---|---|
| `argmax_j |H_j| = 0` for every r | 541 values of r in [60,600], within the cutoff window | CONFIRMED, 0 exceptions |
| `S_r/|G_r| -> 1.1818` | r >= 300: min 1.181804, max 1.184684 | value CONFIRMED; A3's added word "monotone" NOT verified (spread 2.9e-03, not strictly decreasing) |
| `corr(theta_r, r|H_0|) = 0.988` | r >= 200 | CONFIRMED, 0.9882 |
| `corr(theta_r, r|G_r|) = 0.828` | r >= 200 | CONFIRMED, 0.8278 |
| `j <= 5` carries > 99.6% of S_r | r = 600 | CONFIRMED, 99.93% |
| `|D_j|` is NOT bounded away from 0 for many j | exact table at r = 600 | CONFIRMED: 1.000, 0.998, 0.988, 0.951, 0.835, 0.597, 0.339, 0.254, 0.143, ... < 0.032 beyond j = 12 |
| central power-of-two identity | 60-digit mpmath | CONFIRMED, 2.67e-51 |

The last row corrects a premise in my own task prompt: I had suggested `|D_j|` stays bounded
away from zero for many j. It does not. A3 pushed back correctly, and the correction narrows the
window that needs H-control to roughly `j <= 10`.

One caution on an apparent conflict: the all-j argmax column of PROBE_RESULTS.csv points at
`j = n_r`, not `j = 0`. That is a degenerate artifact — at `j = n_r` the tail length is zero, one
composition, so `|H| = 1` exactly — and those j lie outside the cutoff window. Inside the window
A3's statement holds. Recorded so the two tables are not read as contradictory.

## Evidence classification

- Exact four-prefix mixture, conditional law, logarithmic prefix-excess cutoff: `[EXACT]` /
  `[PROVED]`, independently re-derived by A4 from definitions with exact rational arithmetic.
- `|G_r|` of order 1/r on 14 <= r <= 600, constant near 20: `[NUM]`.
- `sup_j |H_j|` of order 1/r on the window, constant near 46, maximised at j = 0: `[NUM]`.
- Circularity of the prefix reduction: `[PLAUSIBLE, argued]`, structurally re-derived here.
- Almost-periodic dependence on `theta_r = frac(beta r)`: `[NUM]`, correlation 0.988 for `r|H_0|`.
- `|G_r| = O(1/r)` (E6-N2), the triangle-weighted lemma, uniform-H, and PWE: all `[OPEN]`.
- Collatz: untouched. Nothing here bears on it.

## Two items that change how targets should be phrased

1. **`r|G_r| -> c` is ill-posed.** Both `r|G_r|` and `r|H_0|` are almost-periodic in `theta_r`,
   not convergent. The right object is a profile `Phi(theta)`. Any upper-bound constant must be
   uniform in theta; any future nonzero-coefficient or lower-bound claim must be a function of
   theta, since beta is irrational and theta_r equidistributes. This applies to the frozen B4
   program item T5 as well and should be checked against its wording before B4 is ever run.
2. **A3 reads the 1/r scale as a bridge-barrier probability**, not as arithmetic cancellation:
   a walk with O(1) endpoints staying below the wrap threshold has survival probability of order
   `2|a||b|/(sigma^2 m)`. `[PLAUSIBLE, heuristic]` — I have not verified it. If it survives
   scrutiny it reframes the whole route: the difficulty would be a barrier estimate for a
   conditioned walk rather than an equidistribution estimate, which is a different literature.

## Recommended next action — exactly one

**Do not open a new sealed task on the triangle-weighted lemma.** The evidence says it is
numerically interchangeable with E6-N2 (factor 1.185) and that its natural sufficient condition
is strictly harder than E6-N2. Opening it would spend an authorization on a restatement.

**Recommended instead: adjudicate A3's PREFIX-WINDOW EXTREMALITY (PWE) proposal**,
`|H_{r-4,n_r-j}(j)| <= C |H_{r-4,n_r}(0)|` for `0 <= j <= L_r`, as an ordinary manager review
before any seal. Its merits: it states no rate, so it is not a restatement; it is a
bridge-comparison statement; it is falsifiable by an unbounded `R(r) = max_j|H_j| / |H_0|`, and
`R(r) = 1.000000` on every r in [60,600] that I checked. Its honest limit: it does not make the
remaining core estimate easier, it removes the uniformity-over-a-drifting-window complication,
which is the audit's "global offset compactness [OPEN]" item for this route.

Before that review, three cheap prerequisites, none needing an authorization:
1. Settle the left-endpoint constant (`j - 5 alpha` versus `j - 4 alpha - 1`).
2. Have the barrier-probability heuristic checked by a second reader; it is the only idea in this
   round that could change the method rather than the bookkeeping.
3. Apply A4's wording repairs to `prefix_bridge_20260906/README.md`, whose publication narrative
   is false as written (no remote branch, no receipts, package untracked).

## Lane A1 — the governance defect is worse than the config defect

A1 confirmed the config root cause from the launcher source and, more importantly, found why the
project burned two authorizations for zero mathematics. I verified both findings directly.

**C3 — a defect in our own seal consumes the authorization exactly like a tamper.**
`..._V2_STAGE1.py:28-29` defines `fail(msg)` with `'authorization_consumed': True` hard-coded into
the failure record, with no distinction of cause. Line 81 calls that same `fail()` for the
frozen-dependency mismatch. So a self-contradictory sealed config — our bug, caught before any
mathematics starts — is recorded identically to a malicious modification of a scientific input.
[CONFIRMED, read from source.] This, not the blob mismatch itself, is why V1 and V2 both ended
with a spent authorization and nothing to show. **A policy decision is required before a third
authorization is issued:** a pre-T1 gate failure attributable to the sealed contract itself should
be recoverable, while any failure attributable to input tampering must stay terminal. Distinguishing
the two is a contract question, not a code question, and it is not addressed by A1's patches.

**C4 — the launcher executes unverified code inside the trust boundary.** Lines 120-121 load the
witness validator from the working tree via `spec_from_file_location` and `exec_module` with no
hash check, although the seal carries its SHA-256. [CONFIRMED, read from source.] Also not
addressed by the patches.

**A latent third instance of the same class:** `START_HERE_CURRENT_HANDOFF.md` carries the identical
frozen-at-the-wrong-commit defect and is dormant only because the CI integrator happens to write it
one commit after Phase A. A repair that hard-codes an exception for the state file alone would leave
this one armed; A1's recommended two-tier semantics, with a declared list of Phase-A-bound governance
files, closes both.

**Dry run.** A1 ran the patched integrity gate in a throwaway clone: PASS on a correctly built
Phase-A/Phase-B pair, and correct refusal on four tamper cases, including one the agent added
itself that corrupts a scientific definitions file inside Phase A. Four harness bugs were fixed to
get there (Windows path length, sealed members absent outside the real ZIP, an `eol=lf` attribute
making disk hashes differ from blob hashes, and a T1-start detector that false-matched the
legitimate pre-T1 gate event); none were in the patches. T1 was never invoked.

**Journal hash chain: INTACT.** I recomputed it myself — 20 of 20 links verify, including across the
schema change at entries 20-21, chain tip `f00f80b4…`. The drift is real (three renames, two dropped
fields, eleven additions, entries 20 and 21 not even uniform with each other) and the `schema` tag
still reads `COLLATZ_RESEARCH_JOURNAL_V1`, so nothing in the record signals it. A1's proposed
sequence-22 CORRECTION entry, rewriting no earlier line, is the right shape.

Nothing in lane A1 authorizes a Stage-1 run. No V3 seal exists. The consumed seals remain consumed.

## Lane A5 — CP17 is submittable, but the publication branch is not reproducible

The referee pass produced the first independent compile in the project's history: 38 pages, zero
errors, zero warnings, zero undefined references, zero bad boxes. All 15 DOIs and 3 arXiv ids
verify against the real bibliographic record. `K_17` reproduces exactly at 40 digits and is
consistent at every occurrence. There are no priority overclaims; the scope disclaimer appears five
times. Both simplifications the internal audits asked for were adopted, so the paper now carries
**zero load-bearing literature dependencies**. Verdict: ready to submit after editorial fixes,
roughly two days of work, none of it mathematical.

One finding deserves separate weight because it is a process failure of the same family as the B4
defects. **The submitted PDF cannot be rebuilt from any source the project holds.**
[VERIFIED by the manager.] Page 1 of `CP17_JTNB_INITIAL_SUBMISSION_V3.pdf` prints the author name;
every available `.tex` has `\author{}` empty. The PDF also carries an AI declaration and a Funding
section that exist in the source only as a `%`-comment, which does not render. All three copies of
the source — the loose file and the copies inside `CP17_PUBLICATION_BRANCH_V3.zip` and
`CP17_EXTERNAL_REFEREE_PACKAGE_V1.zip` — are byte-identical at `42bed9aa997a771f…`, 74032 bytes.
The bibliography file is not on disk at all, only inside those zips.

So the publication branch, which the project recorded as mechanically clean with only human gates
remaining, does not in fact reproduce its own artifact. The prior audits verified hashes of the
files that were present; nobody compiled the source and compared it to the PDF, because no TeX
toolchain was available then. Recovering the true submission source should precede any editing —
otherwise the author name, the AI declaration and the Funding section are silently reverted.

## Cross-lane observation

Three of the four completed lanes found the same class of defect: an artifact recorded as verified
whose verification never actually closed the loop. B4's sealed config froze a file against a commit
where it could not match. The prefix-bridge README asserted a GitHub branch and receipts that do not
exist. The CP17 publication branch cannot rebuild its own PDF. In each case hashes were computed and
checked, and in each case the thing the hashes were supposed to guarantee was not the thing anyone
needed. The protocol's read-back discipline is verifying artifacts against themselves rather than
against their purpose. That is worth one governance fix, not three.

Nothing in this assessment proves the Collatz conjecture. E6-N2 remains `[OPEN]`.
