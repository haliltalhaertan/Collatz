# Round 5 failed/timed-out runs

These runs are provenance only and are **not** used as accepted scientific evidence.

1. `phase_quotient_round5.py` broad monolithic run including an s=20 extension: timed out at 180 s. No accepted result.
2. A narrowed monolithic rerun still timed out at 180 s. No accepted result.
3. `extended_probe.py` printed an s=17 row and then timed out on the next case. The printed s=17 row was **not accepted from this run**; `extended_s17.py` was later run separately and passed.
4. `extended_s19.py` timed out at 120 s. No s=19 result is reported.

The accepted state-count table uses successful isolated runs only through s=18.
