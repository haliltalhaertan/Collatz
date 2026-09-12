# Independent integration audit — 2026-09-12

Scope: Muse remediation changes relative to full-research commit `b49f630`, as merged at `c10ac750910a2b4736424bd1528c8321f18c8289`. This is a bounded source review and selected regression rerun, not a fresh proof audit of all historical mathematics. The integrator was editing the archive builder concurrently; this report reviews the merged committed builder and does not certify the final rebuilt archive or publication.

## Verdict

The principal remediation is reproducible and suitable for integration, provided the new canonical archive/state publication checks are completed. No tested arithmetic regression failed. There are two remaining wording issues below that should be corrected in the accepted version. No result here establishes Collatz or the missing asymptotic W/D2 bound.

## Freshly executed checks

Interpreter: `C:/Users/MDP/Documents/Default Project/llm-lab/.venv/Scripts/python.exe -X utf8`.

- `test_verify_handoff_git_context.py`: PASS. Ancestor accepted, unrelated commit rejected, absent shallow RELEASED base warned, absent HELD base rejected, detached expected branch tip accepted. This regression does not itself test every archive or dirty-tree branch.
- `verify_madde07.py`: 100000 symbols; alphabet {1,2,3}; zero-critical true; raw-byte SHA256 `31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2`; digit-string SHA256 differs as expected; observed tracking range [-2,1]. This is a finite reconstruction, not an asymptotic controller theorem.
- `interval_pressure_certificate.py`: exact Fraction certificate PASS. Both reported h3/h-infinity intervals and alpha/pressure intervals reproduced at all displayed 36 decimals.
- `dogrulama.py`: stdlib-only pressure and finite DP table run completed. h3 rounds to 0.523466681; B=4 pressure rounds to 0.561900734; all listed B values and finite r values executed.
- Portable GOREV001 `panel(r)` called for r=5,10,12,14 without its output-writing main. All internal exact integer/Fraction identities, direct G0, conductor decomposition, W<=qD2, V<=L W and origin bounds passed. W=(37/4,819/32,2795/4,274211/256); qD2=(37/4,2915/32,21195/8,4612387/256).
- GOREV001 boundary recomputed: P=[1,0,1,0], T=[0,1,1,0], G=[1,1,1,1], e=1, V=0, qD2=1.
- `deney.py`: ordinary trajectory 27 gives (111 steps, 9232 peak). Independently substituted a synthetic 2<->3 transition in memory; both direct trajectory and cached main path raised RuntimeError. The full million-start census was not rerun in this audit.

## Mathematical assumptions checked in the source

The rational log remainder `2 |z|^(2N+1)/((2N+1)(1-|z|^2))`, z=(y-1)/(y+1), is a valid bound for y>0. Fraction endpoints and interval division decisions are exact. Positive derivative at the right endpoint and negative at the left locate a stationary point; to call that point the global minimizer one also needs convexity. That justification can be supplied explicitly: with u=log x, the finite pressure is a positive combination of log(exp(u)+exp(2u)) and log(exp(-u)+exp(u)). Each is strictly convex by the positive tilted variance formula. The infinite pressure replaces these by log(sum_{n>=1} exp(nu)) and log(exp(-u)+sum_{n>=1} exp(nu)), on u<0; the same variance argument applies by convergent differentiation. Since 1<alpha<2, the positive combination is strictly convex. Thus the sign bracket identifies the unique global minimum; this analytic argument is needed in addition to the numerical script.

The h3 interval evaluator uses x+1/x decreasing in its bracket below 1. The h-infinity B(x)=1/x+x/(1-x) is decreasing below 1/2; its bracket is approximately 0.20254. Both endpoint choices are valid on these actual brackets, though the evaluators are not general-purpose global interval routines.

The exact-q identity `((m**1053).bit_length()-1)//1000` is valid for positive integer m because floor(floor(log2 n)/1000)=floor(log2 n/1000). The separate floor(k log2 3) array still uses high-precision Decimal in these scripts; byte reproduction checks this finite array against the archival reference, not an all-k arithmetic theorem.

The D0 lift argument is sound after completing a skipped sentence: if r_k=r_* eventually, either possible R_(k+1) is congruent to r_* modulo 2^(A_k+1), since A_(k+1)>=A_k+1. Nesting then forces R_k=r_* for every sufficiently late k, including the mixed-branch case. A last-four plateau alone cannot supply that hypothesis.

## Remaining issues to fix or label

1. `04-cp20-task6-denetim/madde08_karsi_ornek_disiplini.py` still prints `LINEER DRIFT; H1 FAIL` whenever a finite ratio exceeds 0.01, and concludes the finite greedy controller fails H1 from this observation. A finite ratio does not prove asymptotic drift. For periodic constructions one can prove the nonzero mean algebraically; for independent random choices an almost-sure argument is available but does not automatically certify the one finite seeded sample. For the greedy controller either supply a genuine analytic drift proof or label this as finite evidence against H1, not a verdict. The same caution applies to the remediation report's corresponding finite-controller inference.

2. `13-d1-denetim/01_cekirdek_A_B_C.py` and `02_madde10_liminf.py` say the tail script 'shows ... tends to 0'. Replace with 'finite tail observations decrease / are consistent with the independently proved asymptotic statement'. Their main corrected outputs correctly avoid equating a finite infimum with liminf; retain that discipline in the last sentence too.

## Publication gates, not mathematical counterexamples

The committed builder reviewed here overlays management, audits, tools and continuity, but not the root research_* directories or RESEARCH_INDEX_20260908.md. An unmodified invocation therefore would not create a comprehensive current research archive. The integrator is already editing the builder; require explicit membership coverage for accepted root research results and retain secret/caches exclusions.

Run final handoff verification only after updated state hashes, branch context, rebuilt archive/member root, journal, and accepted commit are mutually consistent. Its expected failure on an in-progress dirty integration tree is not a mathematical failure. Full-ZIP SHA and all-member root certify bytes, not equality to every working-tree result; membership coverage must be checked separately. Historical sealed records must retain historical status and must not be silently promoted by integration.

The external Drive anchor provides an independent-medium snapshot; it is not immutable timestamping. No Drive/GitHub upload or remote anchor was performed or revalidated by this sub-audit.

## Post-review correction and validation — 2026-09-12

At the integrator's request, the two wording findings above were repaired in the three affected scripts and the Round2 remediation report. The original finding descriptions are retained as review history. The generic finite-profile output no longer labels H1 as failed; constant/periodic cases keep their separate exact-mean arguments; the proposed kappa=0.5 keeps its H2 parameter violation. Both D1 endings now explicitly distinguish finite observations from a limit proof.

A fresh full execution revealed a further factual correction to the historical remediation description: the greedy kappa=0.5 controller actually yields s_N=6 at N=60000 (s_N/N=0.0001), not visible linear drift. The report now records that value and withdraws the old description. The seeded random example remains s_N=-37289, a finite observation only.

All three edited scripts completed successfully. D1 core reported 9688 integer/range/injury checks with zero failures, 5999 plateau-point checks with zero failures, and 1480 monotonicity/minimum checks with zero failures. Both D1 scripts reported 3728 injuries at N=6000 and printed the narrowed conclusion. Each script passed compilation and an AST comparison against merge commit c10ac750: after removing print statements and docstrings, the computation AST is identical. Thus calculations, random seed, loops, thresholds, return values and numerical data paths were not changed. These checks close the two wording findings; the integration/publication gates remain the integrator's responsibility.
