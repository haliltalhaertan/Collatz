# CP20 SPECIALIST LITERATURE SCREEN V1

Date: 2026-09-04

Scope: residual publication risk identified by the independent zero-trust audit — possible abstract subsumption of T4/T5 by general combinatorics-on-words, symbolic-dynamics, recurrence, discrepancy, or thermodynamic-formalism results stated outside Collatz terminology.

Status:

`[LLM TARGETED SCREEN — RISK NARROWED, HUMAN SPECIALIST PRIORITY CHECK STILL REQUIRED]`

This note is not a priority certificate and does not replace the independent audit's requirement for a specialist human literature pass before submission.

## 1. Non-repetitive complexity is established terminology

Nicholson and Rampersad, *Initial Non-Repetitive Complexity of Infinite Words*, Discrete Applied Mathematics 208 (2016), 114–122, DOI `10.1016/j.dam.2016.03.010`, study the initial non-repetitive complexity introduced by Moothathu and also discuss the shifted/non-repetitive version: the maximum length of a consecutive run of starting positions whose length-`n` factors are pairwise distinct.

This is conceptually very close to the Task-6 counting window. CP20 proves, for each admissible `epsilon`, that all length-`r` valuation factors beginning in

`[N_r,2N_r-r]`,

`N_r=floor(2^((alpha/kappa-epsilon)r))`,

are pairwise distinct. In standard word-combinatorics language this is an exponential lower bound on a shifted non-repetitive-complexity quantity, and the factor-complexity lower bound follows because total factor complexity dominates any such pairwise-distinct run.

### Novelty effect

`[CLOSE GENERAL COMBINATORIAL LANGUAGE — NO SUBSUMPTION]`.

The generic notion is prior art and should be acknowledged if the manuscript discusses the proof as a non-repetition window. The arithmetic theorem that forces this exponential window — polynomial Syracuse state growth plus `2^{A(W)}` repeated-factor separation plus critical-log local mass — is not supplied by Nicholson–Rampersad.

The manuscript therefore must not suggest that “counting consecutive distinct factors before a repeat” is a new complexity concept.

## 2. Recurrence-function literature does not by itself imply T4

Classical combinatorics on words relates factor complexity `p(n)` and recurrence functions. A standard general inequality is of the form

`p(n) <= R(n)`

for a recurrence function `R(n)` large enough to contain every length-`n` factor in every sufficiently long window. This is useful for deriving upper complexity bounds from linear recurrence, but it runs in the wrong direction to imply the CP20 exponential lower factor-complexity theorem from recurrence data alone.

Task 6 instead proves directly that one explicit exponentially long window contains no repeated length-`r` factor. That yields a lower bound on `p_a(r)` by exhibiting exponentially many distinct factors, not by invoking a generic recurrence-function theorem.

### Novelty effect

`[NO ABSTRACT RECURRENCE-THEOREM SUBSUMPTION FOUND]`.

The general vocabulary should be cited as background if useful, but the arithmetic separation step remains the load-bearing Syracuse-specific input.

## 3. Balancedness does not generally force low factor complexity

Espinoza, Popoli and Stipulanti, *Factor-balancedness, linear recurrence, and factor complexity*, arXiv:2602.03746 (2026), study relations between balancedness and factor complexity and explicitly construct a factor-balanced word with exponential factor complexity.

This matters for the interpretation of Task 7. The CP20 pressure upper theorem is not a generic consequence of “balancedness” or “small discrepancy” alone. Its exponential rate comes from the exact phase-dependent allowed defect supports under finite `B`, pointwise zero-criticality, and the `O(log r)` total-defect band, evaluated through the explicit weighted partition functions.

### Novelty effect

`[SUPPORTS DISTINCTNESS OF T5 FROM GENERIC BALANCEDNESS]`.

This source is not an exact antecedent of the CP20 theorem, but it is a warning against vague rhetoric such as “balanced words have low entropy.” CP20 should never use such a statement.

## 4. Pressure/Legendre-transform machinery is classical

The use of topological pressure, exponential generating functions, Birkhoff-average constraints, and Legendre-type optimization is standard thermodynamic formalism. Pesin and Weiss, *The Multifractal Analysis of Birkhoff Averages and Large Deviations* (2001), is one classical reference; much broader formulations exist for finite and countable symbolic systems.

Accordingly, the Chernoff/pressure mechanism in T5 is not itself a novelty claim. The specific CP20 content is the phase-conditioned defect language obtained from the Syracuse critical-log law and the explicit rate

`h_B = inf_lambda [(2-alpha) log_2 P_1(lambda) + (alpha-1) log_2 P_2(lambda)]`,

together with its combination with the independently obtained Syracuse lower rate `alpha/kappa`.

### Novelty effect

`[GENERAL METHOD KNOWN — SPECIFIC SYRACUSE APPLICATION/CONSTANT NOT SUBSUMED IN THIS SCREEN]`.

The final manuscript should cite general pressure/Birkhoff-average literature near the introduction of `h_B`, not only Collatz-specific stochastic work.

## 5. 2026 search for direct abstract substitutes

Targeted queries were run for combinations of:

- factor complexity + recurrence function;
- non-repetitive complexity;
- bounded/factor discrepancy + exponential factor complexity;
- Sturmian environments + weighted pressure;
- constrained Birkhoff sums + pressure/Legendre transforms;
- 2025–2026 combinatorics-on-words papers involving discrepancy and complexity.

No theorem was located with either of the following complete shapes:

### T4 abstract substitute sought

A theorem that, from polynomial growth of an external state observable plus an exponential divisibility/separation rule for repeated factors, directly yields the CP20 rate `alpha/kappa` without the Syracuse-specific arithmetic proof.

**Result:** `[NO EXACT MATCH FOUND]`.

### T5 abstract substitute sought

A theorem whose hypotheses specialize verbatim to the Sturmian phase-conditioned finite-`B` zero-critical defect language and whose conclusion is exactly the CP20 `h_B` formula, so that T5 would be only a change of notation.

**Result:** `[NO EXACT MATCH FOUND]`.

General thermodynamic-formalism results can explain why a pressure/Legendre optimization is natural, but this screen found no source that states the exact CP20 phase-dependent language or constant.

## 6. Updated novelty discipline

After this screen, the safest claim remains:

`[LIKELY NOVEL AS A QUANTITATIVE SYRACUSE SYNTHESIS — HUMAN SPECIALIST PRIORITY CHECK REQUIRED]`.

Do not claim novelty for:

- non-repetitive complexity as a concept;
- recurrence/factor-complexity theory;
- Sturmian/mechanical language theory;
- repeated-factor divisibility as a device;
- pressure, Chernoff, Legendre transforms, or Birkhoff-average multifractal machinery;
- the general architecture of obtaining a threshold by comparing language entropy with a Diophantine/discrepancy parameter.

The defensible contribution remains the exact critical-log Syracuse chain:

`Syracuse arithmetic separation -> exponential lower factor-complexity rate alpha/kappa -> phase-conditioned deterministic pressure h_B -> uniform kappa>2.784 -> two-type critical-density pressure surface`.

## 7. Remaining human-specialist question

A human specialist in combinatorics on words / symbolic dynamics should still be asked one precise question before submission:

> Is there a published theorem, possibly phrased in terms of non-repetitive complexity, return/recurrence functions, constrained Birkhoff sums, relative/fiber entropy, or pressure over a Sturmian base, which after direct specialization makes either CP20 T4 or T5 a formally immediate corollary with the same quantitative constant/rate?

Until that check is answered, priority status remains open even though the targeted screen found no exact substitute.
