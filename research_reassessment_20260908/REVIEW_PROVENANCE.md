# Review provenance

2026-09-08. One newly created subagent: /root/review01_global. The principal performed the other analysis and executed the bounded diagnostic. Ten distinct agents were requested but could not be dispatched because subsequent root and child spawn attempts returned `agent thread limit reached`. Repeated turns of the same reviewer are not independent agents.

Reviewer pass 1 read the project assessment and variance report. It distinguished exact sufficient targets from an unproved asymptotic covariance estimate, and initially proposed a one-round exponential-gain stop criterion.

Reviewer pass 2 independently checked the count-to-orbit proof, found no mathematical error, emphasized uniformity across fixed mass bands, and proposed the sparse-window sufficient condition recorded in REPORT_TR.md. Its attempt to spawn an independent DP reviewer failed; no such reviewer participated.

Reviewer pass 3 read check_grouped_variance.py and independently checked its algebra, without separately executing the script. It confirmed the group weight squared, ordered-pair factor two, signs, and q-squared normalization. It warned that distinct (k,z) groups need not be distinct acceptance vectors. That qualification is included in the report.

After the principal challenged its initial recommendation with the signed covariance diagnostic, the reviewer withdrew the requirement to control each large family's absolute contribution separately and softened the single-round stop criterion. This is a documented disagreement and revision, not ten-person consensus.

The 22nd-moment sufficient condition was derived and numerically calibrated by the principal. No independent agent confirmation of that extra condition was received. It is an elementary conditional inequality, not an established moment bound.

Code execution by principal: check_grouped_variance.py exited 0, four fixed panels r=5,10,12,14. For each, full period totals, per-signature tail means, and the signed covariance reconstruction were checked with integers. Outputs in GROUPED_VARIANCE.json. No claim of asymptotic validation or full archive re-audit.
