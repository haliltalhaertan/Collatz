# Round 7 failed run record

One early extended scan recomputed source histograms separately for every `(m,s)` row and hit the 60-second execution limit.

No values from that interrupted execution are used in the report.

The accepted primary run rebuilt one high-precision histogram table per `m`, then projected it to all required `s`; it completed successfully. The 51-case second implementation also completed successfully.
