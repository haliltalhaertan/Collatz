# Directed task findings

Task: xub-maximum-gap-local-question

| Claim | Status | Statement |
| --- | --- | --- |
| GAP-LOWER-BOUND | OPEN | Find a rigorous bounded-step advance on the maximum-gap probability under the endpoint-only uniform composition law. |

## Supporting evidence

Shared implementations and shared inputs limit independence. Agreement is not a proof certificate; conflicting evidence requires review, never a vote.

- **GAP-LOWER-BOUND**: domain R=dn, n&gt;=2, d grows like a fixed positive constant times log R, K/R approaches beta=log2(3)-1. B&gt;0 fixed. No first-passage transfer claimed.; first missing step: Prove that for the least maximizing vertex M of the exact weighted bridge, its adjacent donor satisfies P(D≥ρd+h &#124; Δ≤B)≥q for some fixed ρ,q&gt;0 uniformly as R=dn→∞ and d is a fixed positive constant times log R. A marginal block lower-tail estimate alone is insufficient because M is path-dependent; a union bound over n can fail for small logarithmic constants..
  - Lane gap: OPEN; independence: SHARED_TRUST_BASE; files: LANES/gap/EVIDENCE.json, LANES/gap/RESULT.json.

Downstream claims not established: Canonical research state changes, Numerical searches, External tools, General proof claims beyond supplied assumptions
