# Targeted literature triage — 8 September 2026

Exploratory reading, not a new proof or full literature audit. Target: the dense marked Laplace transform under the endpoint-conditioned composition law. No governed stage is reopened. No external model calls or new expenditure.

## Sources checked and relevance

1. **Terence Tao**, Almost all orbits of the Collatz map attain almost bounded values, Forum of Mathematics, Pi (2022), [current v7](https://arxiv.org/html/1909.03562v7). Sections 7.1–7.4 provide the white-point/triangle renewal mechanism. The arXiv record reports a July 2026 correction affecting Lemma 7.9. Earlier v5 was initially inspected; current v7 is the reference to use going forward. Direct unconditioned-to-critical-fiber transfer was already rejected in the project's September 4 audit; this is not a newly discovered obstruction.

2. **Felipe Gonçalves, Rachel Greenfeld, Jose Madrid**, [Generalized Collatz Maps with Almost Bounded Orbits, v2 (2022)](https://arxiv.org/html/2111.06170v2). Theorem 1.9 isolates a renewal theorem with an exponential transform of good visits bounded by every fixed negative power. Hypotheses include iid increments, exponential tails, lattice nondegeneracy, separated triangular bad regions, and strict slope inequality omega > eta (their eta denotes triangle slope). Section 7 explicitly uses this gap in triangle exit and separation estimates. Our critical bridge does not inherit these hypotheses. The geometric decomposition is useful; the theorem is not an available black box.

3. **Francesco Caravenna and Loïc Chaumont**, [An invariance principle for random walk bridges conditioned to stay positive](https://arxiv.org/abs/1204.6148), Electronic Journal of Probability 18 (2013), no. 60. Inspect Proposition 4.1 in the [author PDF](https://fcaraven.github.io/download/papers/carcha2-final.pdf), particularly the local limit kernels near the boundary. In the finite-variance regime, a half-line killed kernel at bounded admissible endpoints has the familiar n^(-3/2) scale, with ladder-renewal factors; dividing by an unconstrained n^(-1/2) bridge denominator produces n^(-1). This motivates boundary-dependent comparison functions. Our arithmetic soft killing is not half-line killing, so the cited theorem does not settle our transform.

4. **Loïc Chaumont and Gerónimo Uribe Bravo**, [Shifting Processes with Cyclically Exchangeable Increments at Random](https://chaumont.pages.math.cnrs.fr/rpdfiles/cu2.pdf), Theorem 2.2 and Corollary 3.1. Cyclic shifts condition minima and connect bridges to excursions. This supplies context for our finite cyclic-rank argument. It requires cyclic invariance; the adaptive normalized Q law has no established such invariance. No transfer to Q is claimed.

5. **Raphaël Chetrite and Hugo Touchette**, [Nonequilibrium Markov processes conditioned on large deviations](https://arxiv.org/html/1405.5157v3), Annales Henri Poincaré (2015), Appendix E. Tilted transition matrices and generalized Doob transforms clarify the distinction between row normalization and global path tilting. Their long-time equivalence statements do not automatically control our finite, endpoint-conditioned, polynomial-scale estimate. Relevant as a method for constructing state-dependent transforms, not as a ready-made C/R bound.

6. **Manuel Inselmann**, [An Approximation of the Collatz Map and a Lower Bound for its Average Total Stopping Time, v3 (2024)](https://arxiv.org/html/2402.03276v3), Theorem 1.1 and abstract. For every fixed epsilon > 0, almost every start in natural density descends below m^epsilon in O(log m) accelerated steps. This is useful contemporary progress but does not control our conditional Fourier/marked observable. Natural-density and arbitrary-diverging-threshold conclusions must not be conflated.

7. **Yuan Si**, [A microcanonical phase transition for the Collatz affine random model](https://zenodo.org/records/20027097), May 2026 preprint; [source at previously frozen commit](https://raw.githubusercontent.com/SamSi0322/collatz-affine-model/119199e7165505f9535952e272056af912ce59fb/main.tex). Closest vocabulary: fixed-total compositions and Bernoulli bridges. The project's prior audit already found the central-total assumptions miss our slope linearly. Theorem-level imports remain UNAUDITED. The preprint is not new to this project and does not repair that mismatch.

Recent search hits claiming stronger density results or formal verification were not adopted without checking their primary proof artifacts. This was a targeted scan, not a claim that no newer theorem exists.

## Concrete synthesis for the present suffix problem

The following is our own elementary reformulation, not a theorem imported from these papers. Write beta=log_2(3)-1 and K=beta R+O(1). For any fixed m>0, iid nonnegative geometric coordinates with law

P_m(Y=y)=(1/(1+m))*(m/(1+m))^y

become exactly uniform weak compositions upon conditioning on sum Y=K: each admissible tuple has the same mass. Choose m=beta, denoting the iid law by P_beta. Its endpoint mass is

d_R=P_beta(sum Y=K)=binom(K+R-1,R-1)*beta^K/(1+beta)^(K+R)

and Stirling's formula, for bounded K-beta R, gives

d_R ~ [2*pi*R*beta*(1+beta)]^(-1/2).

For the same path-defined dense mark count N_white, exactly

F_R=E_composition exp(-lambda N_white)
   =E_beta[exp(-lambda N_white)*1_{sum Y=K}]/d_R.

Thus the desired F_R=O(R^(-1)) is equivalent, up to fixed constants on the stated endpoint strip, to the joint killed endpoint estimate

E_beta[exp(-lambda N_white)*1_{sum Y=K}]=O(R^(-3/2)).

This makes the connection to killed local limit kernels precise at the level of the target. It does NOT prove the numerator bound. Under P_beta, the log-phase increments B-2beta have mean zero. Replacing Tao's original law by this geometric law removes exponential rarity of the endpoint but also removes its fixed drift gap. Nor does this constant-parameter geometric tilt restore iid increments under the separate adaptive law Q from the preceding turn.

The unresolved arithmetic obstacle is explicit: z<eta has no killing, but positive near-integer z also has weak/no killing. A half-line survival theorem controls only the first type. We need a bound on repeated near-integer excursions or a phase-dependent renewal potential before combining the two. Weak convergence to a Brownian bridge alone gives no relative precision for an event/transform of order 1/R.

## Next research priority

Start with the iid centered geometric representation and the joint R^(-3/2) target. Use ladder-renewal functions as candidates for the low-state part of a supersolution; separately test whether the exact B=1 word arithmetic can control positive resonant excursions. Retain the full mark and endpoint law in every comparison. This is a proposed research direction, not an established applicability theorem.

## Local provenance

Read current research_dense_tilt_20260908/NEXT_ACTION.md and research_dense_pairs_20260908/EXACT_B1_WORD_LEMMA.md. Checked the earlier E7R literature-transfer source registry and Stage-1 report, especially M6 and M8. The old mandatory stop remains attached to that closed stage; no files there were edited or computations rerun. This note is local and outside the previously uploaded V1 package.
