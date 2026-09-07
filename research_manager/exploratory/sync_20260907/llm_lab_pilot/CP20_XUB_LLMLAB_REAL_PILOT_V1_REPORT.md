# CP20 XUB llm-lab real pilot V1

Date: 2026-09-07  
Classification: `[NON-CANONICAL ADVISORY / PARTIAL INFRASTRUCTURE RESULT / NO SCIENTIFIC RESULT]`

## Frozen identity

- Parent research commit: `b7c77d39ea76e7f74d2666bf2f072fd19fed622d`
- Task: `cp20-xub-marked-occupation-advisory-v1`
- Project: `cp20-xub-llmlab-pilot-20260907`
- Run: `directed-91ab0e82dfc64e4bbc19240f311089b2`
- Contract SHA-256: `b15b3c934c27677789a238d58cab9f4dfd713ad333aa4531e61cf2cbe68e0668`
- Package SHA-256: `0835c5365b1ff2a32dc4b75d2d76c89c613f361be51b6f870f06898aecc2d052`
- Package bytes: `142991`
- Package members: `34`

The user explicitly approved sending the four named exploratory XUB inputs and the frozen task prompt through OpenRouter to the three declared models. The contract forbade canonical writes, sealed-stage execution, invalid B4 V1 drafts, numerical-depth extension, scope expansion, autonomous new tasks, and retries.

## Gate

- Contract validation: `PASS`
- Contract hash check: `PASS`
- Four input SHA-256 checks: `4/4 PASS`
- DAG check: `PASS`
- Preflight status: `FEASIBLE_WITH_LIMITATIONS`
- Model calls before authorization/execution: `0`
- Declared ceilings: 3 calls, 150000 reserved-token units, USD 0.75, 900 seconds, 2 parallel workers, 0 retries

The declared limitation was that model text is not a proof certificate.

## Execution result

Overall run status: `PARTIAL`.

| Lane | Model | Status | Public scientific output | Recorded usage |
| --- | --- | --- | --- | --- |
| `sol-proof-builder` | `openai/gpt-5.6-sol` | `PARTIAL` | none | 4535 prompt, 5000 completion, 5000 reported reasoning tokens; USD 0.061336 |
| `qwen-independent-refuter` | `qwen/qwen3.8-max-0902` | `TIMEOUT` | none | final provider usage unavailable; 300.028 seconds |
| `grok-adversarial-auditor` | `x-ai/grok-4.6` | `BLOCKED_DEPENDENCY` | none | no call and no charge |

Sol consumed the entire 5000-token completion ceiling in provider-visible reasoning and returned no final JSON content. Qwen streamed provider-visible partial reasoning but did not finish within its 300-second lane ceiling. Because the auditor depended on two completed producer results, Grok was correctly blocked and was never dispatched.

The coordinator reports USD `0.061336`, but this is only the known Sol charge. Qwen timed out before a final usage object was received. Under the frozen reservation and declared prices, Qwen's charge cannot exceed USD `0.063562`; therefore the defensible run-cost interval is:

`USD 0.061336 <= actual total <= USD 0.124898`.

No narrower exact total is asserted from the local artifacts.

## Infrastructure defect exposed

The final budget record says `provider_cost_complete: true` even though the timed-out Qwen call has no final usage or cost record. In the current implementation, `DirectedBudget.record()` marks cost incomplete only when it is called with a usage object lacking cost, while a provider timeout exits before `record()` is called. Consequently `provider_cost_complete` is not reliable for timed-out or interrupted provider calls.

This is an infrastructure accounting defect. It does not alter the frozen reservation ceiling and does not create a scientific result.

## Package verification

- Built-in directed-task verifier: `PASS`, `ok=true`
- Independent SHA-256 recomputation: `PASS`
- ZIP CRC/test: `PASS`
- ZIP member count: `34`

The package verifier establishes byte integrity and internal ledger/report consistency only. It does not establish the mathematical claim.

## Scientific verdict

`XUB-MARKED-OCC`: `[OPEN]`.

There is no public proof, refutation, counterexample, or narrower analytic estimate from this run. The pilot does not prove XUB, E6-N2/B4, a nonzero profile, a polynomial lower bound, or the Collatz conjecture. No sealed B4 source was executed and no canonical claim was changed.

## One repaired follow-up

Before a V2 scientific pilot, repair and test timeout-cost completeness, then use a fresh contract with a larger lane wall-time and an output policy that reserves space for a public final answer instead of allowing reasoning to consume the entire completion ceiling. V1 must not be resumed or silently reinterpreted; any V2 requires a new contract hash and a new explicit budget decision.

