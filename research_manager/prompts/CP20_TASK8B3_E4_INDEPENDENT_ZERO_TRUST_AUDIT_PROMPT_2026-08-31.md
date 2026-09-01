# CP20 TASK 8B3 — E4 INDEPENDENT ZERO-TRUST AUDIT

## Role and hard stop

Act as an independent adversarial mathematical auditor. You did not produce E4. Treat every E4 label, derivation, verifier output, numerical summary, and strategic conclusion as untrusted until independently checked.

This task is audit-only. Do not start E5, do not seek a Collatz proof, do not extend the computation beyond the declared depth, and do not use an E4 claim downstream. If a load-bearing claim fails, stop at the narrowest counterexample or repair.

Nothing in E4 is claimed to prove Collatz.

## Supplied package and provenance gate

Primary input:

- `CP20_TASK8B3_E4_AUDIT_PACKAGE.zip`
- expected SHA-256: `a99185ffc4e9daa527a3ee54b59df8ced02bed65490421ce3f9a028119f8c408`

Reference complete package, if supplied:

- `CP20_TASK8B3_E4_COMPLETE_PACKAGE.zip`
- expected SHA-256: `95190d5cbdb633ad049720897b28c73898be229832549153c1fe9ee03b9c4cb1`

Before reading the conclusions:

1. Extract into a fresh isolated audit directory.
2. Recompute the ZIP hash.
3. Recompute every entry in `CP20_TASK8B3_E4_AUDIT_SHA256SUMS.txt`; the expected package structure is 28 hashed payload entries plus the manifest itself.
4. Check the frozen E3 manifest and verifier provenance. If the full sibling E3 data needed by the E4 verifier are unavailable, separate “theorem audit possible” from “numerical reproduction incomplete”; do not silently call the whole audit passed.
5. Record exact filenames, hashes, runtime, and any missing dependency. Do not modify the supplied artifacts.

## Frozen definitions to re-derive, not assume

Starting from the frozen E3 limit equation, independently verify all conventions and constants:

\[
K_d(\theta)=aK_{d-1}(\theta)
 +bP_{d,C}(\theta)K_{d+\varepsilon(\theta)}(T\theta),
\]

where

\[
\alpha=\log_2 3,\qquad \beta=\alpha-1,\qquad
a=\frac{\beta}{\alpha},\qquad b=\frac1\alpha,
\]

\[
T\theta=\{\theta-\beta\},\qquad
\varepsilon(\theta)=\mathbf 1_{[0,\beta)}(\theta).
\]

Check the half-open phase convention at `0` and `beta`, the signed offset domain, and the exact formula for `P`. Reject any formula that changes a branch convention or rotates a phase during the same-phase unrolling.

## Load-bearing theorem audit

### A. Finite unrolling and boundary condition

Prove or refute by induction, for every finite `J >= 0`,

\[
K_d(\theta)=\sum_{j=0}^{J}ba^jP_{d-j,C}(\theta)
K_{d-j+\varepsilon(\theta),C}(T\theta)
+a^{J+1}K_{d-J-1,C}(\theta).
\]

Then determine exactly what is necessary and sufficient for the displayed remainder to vanish for fixed `(d,theta)`. Distinguish pointwise, essential-supremum, and uniform-in-phase statements. In particular, check whether

\[
a^{-m}K_m(\theta)\to0\qquad(m\to-\infty)
\]

is correctly stated and whether E4 ever uses the infinite expansion without having inherited this condition from finite depth.

### B. Cylinder-to-line conjugacy

Audit the map

\[
x=d-\theta,
\]

as a bijection from `Z x [0,1)` to `R`, including integer endpoints and measure/norm correspondence. Verify directly that the two input states become `x-1` and `x+beta`, and that

\[
p_C(x)=\exp(2\pi i\,2^{x-1-C}).
\]

Decide whether the statement “the dense branch seams are coordinate seams” is exact and what regularity, if any, is still required at integer points.

### C. Centered critical walk

For `q_j=ba^j`, independently check total mass, moment domain, mean, variance, and orientation of

\[
Y=\beta-J.
\]

Separately prove or refute the deterministic identity

\[
\sum_{k=0}^{n-1}\varepsilon(T^k\theta)
=n\beta+T^n\theta-\theta.
\]

Do not model the rotation symbols as iid. State exactly where independent copies of the auxiliary geometric `J` are legitimate when iterating the positive kernel.

### D. Exponential norm and spectral-radius obstruction

This is the most important adversarial check. For

\[
\|f\|_{\infty,s}=\sup_x e^{-sx}|f(x)|,
\]

verify the sign, admissible domain, and exact operator-norm multipliers

\[
m_{\rm LE}(s)=ae^{-s}+be^{\beta s},
\qquad
m_{\rm U}(s)=\frac{be^{\beta s}}{1-ae^{-s}}.
\]

Do not infer spectral radius from a one-step norm. Either establish, for every fixed iterate `n`, a far-left test-function/localization argument whose weighted norm approaches `m(s)^n` despite path collisions and complex phases, or reject/repair the spectral-radius claim. For the unrolled infinite kernel, supply the domination needed to exchange the far-left limit with the geometric sum and then with finite iterates.

Check strict convexity and the claimed unique minimum `1` at `s=0`. Precisely delimit the conclusion:

- pure exponential weights;
- weights asymptotically exponential on the far-left tail;
- patched one-sided and two-sided weights;
- no claim about every conceivable asymmetric or oscillatory weight.

If only the positive majorant is controlled, say so explicitly and mark the complex-operator spectral claim unsupported.

### E. Polynomial, L1, BV, analytic, and truncation claims

For every candidate space, distinguish:

1. operator boundedness/closure;
2. an inherited uniform finite-depth norm bound;
3. compactness or tightness;
4. a canonical spatial boundary condition.

Verify the polynomial geometric jump-tail estimate and confirm that it is not a spatial offset-truncation theorem. Check the scope of the L1, local/global BV, and analytic-strip negative conclusions; repair any wording that purports to exclude more spaces than was proved.

### F. Moving-boundary nontriviality

Starting from the exact `n=0` finite recurrence, verify

\[
|G_{r,0,C}|=1,\qquad x=-\beta r,\qquad |H|=r.
\]

Audit the modular-inverse/finite-initial-range issue and prove or refute convergence of the boundary phase product to a nonzero unit. Then check:

- whether a uniform polynomial allowance with degree `p<1` is indeed impossible;
- whether degree `p=1` is merely admissible rather than proved uniformly bounded;
- whether the moving-boundary asymptotic says anything rigorous about a fixed target such as `(d,C)=(-8,4)`.

No fixed-target nontriviality may be inferred without an explicit uniform transfer estimate.

## Numerical and implementation audit

After the theorem audit, and without changing the frozen artifacts:

1. Run the supplied verifier in an isolated copy or by a read-only wrapper.
2. Recompute CSV dimensions and declared depth/parameter bounds.
3. Independently implement at least one reduced-recurrence checkpoint; report complex error, not only magnitude error.
4. Check selected boundary-sensitivity rows from source data.
5. Confirm that oracle injection is only an implementation control.
6. Verify that the predeclaration predates output inspection and that no E4 computation exceeds `r=8000`.

Profile fits, phase widths, positive-side decay, and boundary sensitivity remain `[NUM]` even if reproduced.

## Required deliverables

Produce:

1. `CP20_TASK8B3_E4_INDEPENDENT_AUDIT_REPORT.md`
2. `CP20_TASK8B3_E4_INDEPENDENT_AUDIT_CHECKS.json`
3. `CP20_TASK8B3_E4_INDEPENDENT_AUDIT_SHA256SUMS.txt`
4. saved verifier/independent-check output
5. one ZIP containing only the audit outputs, not rewritten E4 inputs

For every load-bearing claim, give one status: `[PROVED]`, `[REPAIRABLE]`, `[NUM]`, `[UNSUPPORTED]`, or `[OPEN]`. Cite exact source file and line numbers. Identify the first invalid equality or missing quantifier, not merely a general concern.

## Mandatory final verdict

Return exactly one:

- `[AUDIT PASS — CRITICAL-WALK ROUTE DECISION]`
- `[AUDIT PASS WITH REPAIR — CRITICAL-WALK ROUTE DECISION]`
- `[AUDIT FAIL — LOAD-BEARING ERROR]`
- `[AUDIT OPEN — INSUFFICIENT MATERIAL]`

Then answer, separately and explicitly:

1. Does the exact line conjugacy survive?
2. Does the qualified infinite unrolling survive?
3. Does deterministic zero drift survive without iid assumptions?
4. Does the complex-operator spectral-radius obstruction survive, and on exactly which weights?
5. Does the moving-boundary nonzero asymptotic survive?
6. Was compactness proved?
7. Was a nonzero fixed-target profile proved?
8. May the research manager open the proposed degree-one complex-renewal/local-limit task?

The answer to item 8 is “yes” only after a pass or a fully specified pass-with-repair whose repair does not alter a load-bearing theorem.
