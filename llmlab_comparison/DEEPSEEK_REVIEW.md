# DeepSeek V4 Pro 0813 pilot: interrupted operational comparison

Four calls dispatched; fifth not dispatched. Same five-route plan, frozen scientific inputs, high effort, and 8000 completion-token allowance as Luna. The principal requested a graceful stop at approximately 588.6 seconds after discovering a provider-price ceiling violation and provider/local completion divergence. Status STOPPED is intentional, not a completed five-call mathematical comparison.

No public final text was captured by llm-lab in any of the four lanes before this stop. Hidden reasoning is not treated as research evidence. No assessment of mathematical model quality follows from the absence of captured final text.

Provider generation readback matches the user's Activity screenshot:

| Lane | Provider | Completion / reasoning tokens | Finish | Recorded USD |
|---|---|---:|---|---:|
| counting | StreamLake | 2608 / 2608 | null | 0 |
| cycles | unknown | unavailable | GET 404 | unresolved |
| low-state | Phala | 8000 / 8000 | length | 0.04182115 |
| resonance | CoreWeave | 8000 / 5388 | length | 0.0379549 |

Known recorded subtotal is USD 0.07977605; full billing remains unresolved. The StreamLake record has no terminal finish reason, so its zero charge should not be generalized to a reliable final total. The immutable local ledger reports zero known stream cost and an estimated upper reservation of 0.10959564, but catalog rate ceilings were not enforced in routing and were exceeded. That estimated upper reservation must NOT be presented as a certified billing cap.

Phala used the entire allowance on reasoning, producing no final-answer tokens. CoreWeave's usage reports 2612 non-reasoning completion tokens, but the local app had captured no final text by the stop. Both returned length rather than stop. Provider generation_time fields are 121512 and 252093 respectively, while local streams remained unfinished at about 588 seconds. This is evidence of provider/local stream-state divergence, not proof of a particular local bottleneck.

The current directed engine writes the complete growing PARTIAL.json plus a TRACE entry on every reasoning, reasoning_details, and content callback. This is a plausible throughput bottleneck, not a measured causal diagnosis. No production source was modified.

The catalog snapshot listed USD 0.66/M input and 1.98/M output. Actual Phala charge exceeded the per-lane USD 0.04 declared budget. The default adapter did not send provider.max_price. Subsequent GLM dispatch was held before it began, and a separate adapter copy was created in glm_capped with provider.max_price prompt=0.075 and completion=0.25, sort=price. This isolated routing change is an explicit comparability difference, recorded in BINDING.json with contract and adapter hashes. Original DeepSeek artifacts and the unexecuted original GLM plan were preserved.

DeepSeek package byte verification and independent ZIP CRC passed (45 members). SHA256: 3a3ef6a2e2656a6030050ca6f7c584f91cfbb20af68e65124cfed3ea7c8a8792. Package integrity does not certify its price estimate or mathematical truth.
