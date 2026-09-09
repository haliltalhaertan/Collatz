# V2 principal review notes — completed run

This is a new non-canonical advisory run. No sealed B4/E7 source was run, no canonical claim was updated, and V1 was not resumed.

## Preparation evidence

- Current repair record: llm-lab/docs/REAL_PILOT_V1_REPAIRS.md.
- Independently rerun focused offline regression suite: 40 passed in 2.96 seconds.
- Initial pytest attempt: 33 passed, 7 fixture setup errors caused by the default temporary-directory environment. The complete rerun with an explicit fresh workspace temporary directory passed.
- Current OpenRouter model catalog confirmed low effort for Sol, Qwen, and Grok. It did not advertise numeric reasoning-budget support for these models. No numeric cap or guaranteed final-answer reservation is claimed.
- New contract hash: f76c2a284286815f5cb21e53d1be06caa0c61bb85bde0d4674b84b6612e3e56e.
- Same four V1 scientific input files, hashes verified 4/4.
- Calls <= 3, total declared cost ceiling USD 0.75, no retries, two simultaneous producers followed by one dependent auditor.
- Low effort on all lanes; completion ceilings 12000/12000/8000; each lane 600 seconds; total 1200 seconds.

## Sol public-answer review

Sol returned COMPLETED with an OPEN primary claim. This is execution completion, not a proof of XUB.

The stated weak-composition marginal follows by independently counting a prefix of total a and a suffix of total K-a, then dividing by the full composition count. Its range 1 <= h < R avoids zero-coordinate boundary conventions. It is valid under the displayed uniform weak-composition law. Additional first-passage conditioning must preserve that law before transferring the formula to any differently conditioned distribution.

For a fixed run of m zero raw increments, the ratio of composition counts has the stated finite product and tends to (1+beta)^(-m) when K/R tends to beta. For m=2L the pair state is z_L=z_0(4/9)^L, so a sufficiently long fixed run forces a low state. This checks the displayed obstruction, already present in the supplied research record; it is not new evidence that XUB is false.

Define N0 as the count of useful, non-low blocks without excluding positive resonances. Since N_C <= N0, exp(-lambda N0) <= exp(-lambda N_C). Thus the proposed N0 Laplace estimate is a necessary weaker target. This implication is correct. It does not prove the N0 estimate, demonstrate a tractable route to it, or establish that solving it will resolve the resonance exclusion. The model's phrase 'strictly easier' should be read as dropping a condition, not a proved computational or analytic difficulty comparison.

Provider reasoning was not used as scientific evidence. The final run was PARTIAL: Sol completed, Qwen timed out, Grok was blocked by dependency. Package verification and independent ZIP CRC/hash checks passed. XUB remains OPEN.

## Provider read-back after local timeout

The Qwen generation metadata GET returned total_cost USD 0.052800 and finish_reason stop, cancelled false. The local client timed out after 600.557 seconds without public final content. The provider-side completion status does not recover the missing answer or make the local lane completed. It does show that model latency alone is not an established explanation for the local timeout. Investigate stream consumption and callback persistence before paying for another repetition.

The callback currently rewrites the full PARTIAL.json and appends TRACE.jsonl on every fragment. This is an observed implementation detail and a candidate bottleneck, not a diagnosed cause. No fix or performance benchmark was performed in this run.

The request/stream model label was qwen/qwen3.8-max-0902, while generation metadata reports qwen/qwen3.8-max-20260902. Record this provenance discrepancy without assuming either a verified alias or a different model.

The immutable coordinator package correctly retains provider_cost_complete=false and its initial interval USD 0.028816–0.135422. Separate PROVIDER_COST_READBACK.json reconciles the known Sol charge with Qwen's provider-reported charge: USD 0.081616 total. This receipt was not retroactively inserted into or used to rewrite the completed run.
