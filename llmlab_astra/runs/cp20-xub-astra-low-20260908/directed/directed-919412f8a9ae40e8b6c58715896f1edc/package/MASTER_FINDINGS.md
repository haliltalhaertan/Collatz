# Directed task findings

Task: cp20-xub-astra-low-v1

| Claim | Status | Statement |
| --- | --- | --- |
| XUB-MARKED-OCC | OPEN | For fixed admissible eta, lambda, bounded positive alphabet cutoff B_0, and a preregistered disjoint block grid with L_R=floor(c log R) below the stated symbolic-supply threshold, there is a constant C such that every sufficiently large actual accessible suffix array satisfies E[exp(-lambda * sum_{q in Q_R} 1_{C_q}) &#124; S_R=K and the exact first-passage data] &lt;= C/R. Here C_q is the event that block q has all pair totals in {1,...,B_0}, its entry state is not low, and it does not satisfy the exact positive amplified-resonance condition recorded in the inputs. |

## Supporting evidence

Shared implementations and shared inputs limit independence. Agreement is not a proof certificate; conflicting evidence requires review, never a vote.

- **XUB-MARKED-OCC**: domain Uniformly over sufficiently large accessible suffix lengths R=2J+epsilon, epsilon in {0,1}, and the actual coupled integer arrays (r,R,tau,K) with K-beta R in (-15-2beta,-13-2beta), beta=log_2(3)-1, z_0=2^(1-{beta tau}) in (1,2), and S_R=K under the uniform weak-composition law; constants may depend only on the preregistered fixed parameters eta, lambda, B_0, c and the fixed grid rule, not on r,R,tau,K.; first missing step: {'name': 'Necessary unmarked even-time occupation-Laplace inequality', 'inequality': 'E_A[exp(-lambda * sum_{j=0}^{floor(R/2)-1} 1{1-{beta*tau}+H_j-2*beta*j &gt;= log_2 eta})] &lt;= C_low/R', 'quantifiers': 'For the frozen admissible eta and lambda, there must exist finite C_low and R_0, independent of r,R,tau,K, such that the inequality holds for every actual accessible array with R&gt;=R_0, R=2J+epsilon, epsilon in {0,1}, and K-beta*R in (-15-2*beta,-13-2*beta), under the stipulated uniform-composition law with the exact first-passage conditioning. No extension to arbitrary independently chosen endpoints is asserted.', 'relation_to_target': 'Strictly narrower necessary subproblem: all non-low pair-time entries are counted, without requiring grid membership, bounded-positive words, or nonresonance. Its proof would not establish the frozen marked estimate.', 'missing_evidence': 'A uniform joint occupation bound, rather than single-time counting or low-hit rarity.'}.
  - Lane astra-low-review: OPEN; independence: SHARED_TRUST_BASE; files: LANES/astra-low-review/EVIDENCE.json, LANES/astra-low-review/RESULT.json.

Downstream claims not established: Execution or use of any sealed B4 Stage 1 source, Invalid or non-canonical B4 V1 drafts, Claims about arbitrary independent endpoints outside the actual coupled array, New numerical depth, fits, plots, adaptive searches, or literature browsing, Promotion of XUB, E6-N2/B4, a nonzero profile, polynomial lower bounds, or Collatz to proved status
