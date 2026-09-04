# CP20 NOVELTY MATRIX

Status: `[POST-INDEPENDENT-AUDIT REPAIRED PUBLICATION ASSESSMENT]`

| CP20 component | Mathematical status | Closest prior-art family | Novelty assessment | Safe manuscript language |
|---|---|---|---|---|
| Odd-only affine word identity | `[KNOWN]` | Standard accelerated Collatz/Syracuse algebra; Wang; Witteveen | `[NOT NOVEL]` | “Using the standard affine iterate identity…” |
| Sturmian phase word `g_k` and `p_g(r)=r+1` | `[KNOWN]` | Morse–Hedlund/Sturmian theory; López–Stoll in Collatz context | `[NOT NOVEL]` | “The phase word is Sturmian, hence…” |
| Repeated-factor divisibility / separation mechanism | `[PROVED]` | Wang repeated-prefix arithmetic; Witteveen repeated exponent-factor lemma | `[CLOSE PRIOR ART — NOT NOVEL AS A DEVICE]` | “A repeated-factor subtraction argument gives…”; state that Witteveen's `3^r` endpoint divisibility and CP20's `2^{A(W)}` start-value divisibility are dual coprime readings of the same affine subtraction |
| General entropy-threshold architecture | `[KNOWN CLOSE ARCHITECTURE]` | Witteveen 2026 | `[CLOSE PRIOR ART — NOT NOVEL AS AN ARCHITECTURE]` | Do not claim novelty for comparing a constrained-language entropy rate against a Diophantine/discrepancy parameter to obtain a threshold |
| `n_k=O(k^kappa)` from global critical-log law | `[PROVED][AUDITED][FROZEN]` | E-sequence / affine-carry literature | `[NO EXACT MATCH FOUND]` | “Under the critical-log hypothesis we obtain…” |
| Local mass `A(u,r)>=alpha r-O(1)` on Task-6 windows | `[PROVED][AUDITED][FROZEN]` | Standard discrepancy consequence | `[TECHNICAL / LOW NOVELTY]` | State as lemma, no priority claim |
| `liminf log_2 p_a(r)/r >= alpha/kappa` | `[PROVED][AUDITED][FROZEN]` | Dubickas linear parity-complexity bound; Witteveen bounded-amplitude factor counting; docbgm2002 qualitative low-complexity exclusions | `[LIKELY NOVEL QUANTITATIVE THEOREM]` | “We prove an exponential lower factor-complexity rate…” |
| Deterministic zero-critical finite-`B` pressure upper bound `limsup <= h_B` | `[PROVED][AUDITED][FROZEN]` | Lagarias–Weiss stochastic LD/entropy; Witteveen constrained-language entropy; general thermodynamic/Chernoff methods | `[LIKELY NOVEL IN THIS SYRACUSE REGIME]` | “For finite `B>=3`, assuming `1<=a_k<=B` and zero-criticality, we derive a deterministic weighted-pressure upper bound…” |
| Correct Chernoff coefficient inequality | `[KNOWN]` | Standard generating-function/Chernoff bound | `[NOT NOVEL]` | Use without novelty language |
| Finite-B obstruction `kappa>=alpha/h_B` | `[PROVED][AUDITED][FROZEN]` | Consequence of CP20 lower+upper rates | `[LIKELY NOVEL COROLLARY]` | “Under the finite-`B` hypotheses, combining the two rates yields…” |
| B=3 certified `kappa>3.027` | `[CERTIFIED CONSEQUENCE]` | CP20-specific constant | `[LIKELY NOVEL BUT DERIVATIVE]` | Present only under `1<=a_k<=3`, zero-criticality, and the critical-log hypothesis |
| Uniform no-a-priori-B threshold `kappa>2.784` | `[PROVED][AUDITED][FROZEN]` | No exact equivalent located | `[LIKELY NOVEL HEADLINE COROLLARY]` | “Without fixing any finite valuation bound in advance…” |
| Wording “unbounded valuations” | `[INVALID WORDING]` | — | `[DO NOT USE]` | Say “no a priori valuation-alphabet bound” |
| Two-type critical-site feasible region `F` | `[PROVED][AUDITED][FROZEN]` | No exact equivalent located | `[LIKELY NOVEL FORMULATION]` | “We resolve critical sites into two phase-dependent types…” |
| Pressure surface `h(rho_1,rho_2)` | `[PROVED][AUDITED][FROZEN]` | Deterministic LD/pressure methods generally; no matching Collatz theorem found | `[LIKELY NOVEL]` | “We obtain the following critical-density pressure surface…” |
| Scale-family accumulation theorem `h(rho)>=alpha/kappa` | `[PROVED][AUDITED][FROZEN]` | No exact equivalent located | `[LIKELY NOVEL PRINCIPAL THEOREM]` | State exact audited scale-family quantifiers, including `0<epsilon_r<alpha/kappa`, `epsilon_r->0`, `r epsilon_r->infinity` |
| Natural critical-density corollary | `[PROVED][AUDITED][FROZEN]` | Direct corollary | `[LIKELY NOVEL BUT DERIVATIVE]` | Present after main density theorem |
| Zero critical density `o(N)` suffices for `kappa>2.784` | `[PROVED][AUDITED][FROZEN]` | Task 7 pointwise zero-critical result | `[LIKELY NOVEL HYPOTHESIS STRENGTHENING]` | Emphasize density-zero rather than pointwise exclusion |
| `rho_min(kappa)` phase geometry | `[PROVED DEFINITION + CERTIFIED NUM]` | No exact equivalent located | `[LIKELY NOVEL]` | Show exact definition first, decimals second |
| Certified `rho_min(1.06), rho_min(1.5), rho_min(2)` | `[CERTIFIED NUM][FROZEN]` | No exact equivalent located | `[LIKELY NOVEL NUMERICAL COROLLARIES]` | “Interval certification gives…” |
| Maximum of density surface recovers CP19 Task 4 | `[PROVED][AUDITED][FROZEN]` | Internal consistency identity | `[NOT A SEPARATE NOVELTY CLAIM]` | Use as consistency check |
| “strict optimized Sturmian phase cost” | `[FALSE / RETRACTED]` | — | `[DO NOT USE]` | Explicitly absent |
| Full-scale arbitrary-`N` Task-8A extension | `[PROVED — AUDIT EXTENSION CANDIDATE]` | — | `[NOT ADMITTED]` | Exclude from manuscript theorem claims until audited |
| Continued-fraction long-repeat law | `[OBSERVATION / MISSING LEMMA]` | Sturmian continued-fraction theory | `[NOT READY]` | Exclude from theorem body |
| E7R/B4 Fourier cancellation | `[OPEN / ACTIVE]` | Tao/Si microcanonical Fourier line | `[SEPARATE PROJECT]` | Do not mix into this paper |

## Highest-risk novelty conflicts

### Witteveen 2026

Overlap is strongest at both **mechanism** and **architecture** level. The same affine subtraction underlies Witteveen's `3^r` endpoint divisibility and CP20's `2^{A(W)}` start-value divisibility. Witteveen also already has the broad strategy “constrained-language entropy rate versus a Diophantine/discrepancy parameter gives a threshold.” Difference is theorem regime and quantitative output: bounded-amplitude cycles with uniformly bounded zero-budget discrepancy versus global critical-log ordinary Syracuse orbits with an `O(log r)` defect band, together with the CP20 rates `alpha/kappa`, `h_B`, the uniform `2.784` threshold, and the two-type pressure surface.

### docbgm2002/collatz-things, July 2026

Overlap is strongest at the level of **repetition/complexity versus ordinary integrality**. IEF12–IEF21 already exclude several low-complexity or high-repetition balanced residual block languages. Difference is object and conclusion: special repunit-tail `{3,4}` residual language and qualitative no-realizer theorems versus CP20's arbitrary critical-log valuation word and quantitative entropy-pressure rates.

### Abstract non-Collatz subsumption risk

A still-open specialist literature risk is that a general theorem in combinatorics on words or symbolic dynamics, stated outside Collatz terminology, could subsume T4 or T5 after a change of notation. Current status: `[UNCERTAIN — SPECIALIST CHECK REQUIRED BEFORE SUBMISSION]`.

## Publication novelty statement — recommended form

> We do not claim novelty for the underlying affine, Sturmian, repeated-factor, entropy, or general threshold-architecture ingredients. Our contribution is the quantitative combination, in the critical-log ordinary-Syracuse regime, of an exponential factor-complexity lower rate with a deterministic finite-`B` pressure upper rate, its uniform no-a-priori-bound consequence, and the two-type critical-site density pressure extension.

## Confidence labels

- `[KNOWN]`: standard or clearly present in earlier sources.
- `[CLOSE PRIOR ART]`: materially similar theorem device, architecture, or statement exists.
- `[NO EXACT MATCH FOUND]`: targeted search found no equivalent; not a priority certificate.
- `[LIKELY NOVEL]`: no equivalent located and the theorem shape appears materially distinct; specialist confirmation still required.
