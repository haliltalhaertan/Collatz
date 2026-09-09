# Directed task findings

Task: cp20-xub-sol-none-v1

| Claim | Status | Statement |
| --- | --- | --- |
| XUB-MARKED-OCC | OPEN | For fixed admissible eta, lambda, bounded positive alphabet cutoff B_0, and a preregistered disjoint block grid with L_R=floor(c log R) below the stated symbolic-supply threshold, there is a constant C such that every sufficiently large actual accessible suffix array satisfies E[exp(-lambda * sum_{q in Q_R} 1_{C_q}) &#124; S_R=K and the exact first-passage data] &lt;= C/R. Here C_q is the event that block q has all pair totals in {1,...,B_0}, its entry state is not low, and it does not satisfy the exact positive amplified-resonance condition recorded in the inputs. |

## Supporting evidence

Shared implementations and shared inputs limit independence. Agreement is not a proof certificate; conflicting evidence requires review, never a vote.

- **XUB-MARKED-OCC**: domain Uniformly over sufficiently large accessible suffix lengths R=2J+epsilon, epsilon in {0,1}, and the actual coupled integer arrays (r,R,tau,K) with K-beta R in (-15-2beta,-13-2beta), beta=log_2(3)-1, z_0=2^(1-{beta tau}) in (1,2), and S_R=K under the uniform weak-composition law; constants may depend only on the preregistered fixed parameters eta, lambda, B_0, c and the fixed grid rule, not on r,R,tau,K.; first missing step: {'name': 'Actual-array joint marked lower-tail inequality', 'inequality': 'There must exist constants a&gt;0 and C_0&lt;infinity, depending only on eta, lambda, B_0, c and the fixed grid rule, such that for every sufficiently large accessible R, every actual coupled (r,R,tau,K) satisfying the stated constraints, and every integer 0&lt;=n&lt;=ceil((2/lambda) log R), P(N_R&lt;=n &#124; S_R=K and the exact first-passage data) &lt;= C_0 e^{lambda n/2}/R, where N_R=sum_{q in Q_R}1_{C_q}.', 'why_narrower_than_target': 'This is required only up to logarithmic n and directly implies the desired Laplace estimate after splitting the expectation at n approximately (2/lambda)log R and summing the lower tail. It does not demand independence, exclusion of all resonances, or occupation control outside the preregistered grid.', 'why_not_proved': 'The exact coefficient formula controls one prescribed block only. No displayed identity or estimate controls simultaneous bounded-positive words together with affine non-low prefix constraints and short-orbit nonresonance marks across many endpoint-conditioned blocks. Rational ties, even-time sampling, and the growing ternary conductor therefore remain unresolved at precisely this joint lower-tail step.'}.
  - Lane sol-none-review: OPEN; independence: SHARED_TRUST_BASE; files: LANES/sol-none-review/EVIDENCE.json, LANES/sol-none-review/RESULT.json.

Downstream claims not established: Execution or use of any sealed B4 Stage 1 source, Invalid or non-canonical B4 V1 drafts, Claims about arbitrary independent endpoints outside the actual coupled array, New numerical depth, fits, plots, adaptive searches, or literature browsing, Promotion of XUB, E6-N2/B4, a nonzero profile, polynomial lower bounds, or Collatz to proved status
