# CP25 C1 — ORIENTED LIFT COHERENCE / PRODUCT BARRIER

**Date:** 2026-09-21
**Status:** `OPEN-NONTRIVIAL`
**Boundary:** Collatz remains open. This is an integrality criterion for rational cycle words, not a proof of convergence or a no-cycle theorem.

## 1. Question under test

Let `w=(epsilon_0,...,epsilon_{m-1})` be a nonzero binary word, `k=sum(epsilon_i)`,

- `M = 2^m`,
- `P = p^k` for odd `p>=3`,
- `D = M-P`, `b=sign(D)`, `A=|D|`,
- `B_r` the exact Böhm–Sontacchi numerator for cyclic rotation `r`,
- `q_r=B_r/A`,
- `h_r in {1,...,M}` the least positive residue satisfying
  `P h_r + b B_r == 0 (mod M)`.

The positive-orientation choice `b=sign(D)` unifies the positive `pn+1` regime (`D>0`) and positive `pn-1` regime (`D<0`). It does not treat `b` as a free second choice for the same word.

The candidate implication is

```text
C1:  q_r >= h_r for every cyclic rotation r
     => A divides B_0.
```

Because `A` is odd and `h_r == A^{-1}B_r (mod M)`, define the signed carry

```text
B_r = A h_r + M t_r.
```

Then `q_r>=h_r` is exactly `t_r>=0`. The proof gap is therefore:

```text
t_r >= 0 for all rotations  =>  A divides t_r (equivalently A divides B_r).
```

## 2. What was proved exactly

The rotation recurrence is

```text
2 B_{r+1} = p^{epsilon_r} B_r + b epsilon_r A,
2 q_{r+1} = p^{epsilon_r} q_r + b epsilon_r.
```

It follows that

```text
product_{r:epsilon_r=1} (p + b/q_r) = M.
```

Divisibility is rotation-invariant because, modulo `A`,

```text
2 B_{r+1} == p^{epsilon_r} B_r (mod A),
```

and both `2` and `p` are invertible modulo `A`.

ChatGPT Web proposed the stronger **Product Barrier**. Put

```text
y_r = h_r + M/A.
```

For every nonintegral primitive word (`A` does not divide `B_0`):

```text
PB+: product_{epsilon_r=1}(p + 1/y_r) < M   when b=+1,
PB-: product_{epsilon_r=1}(p - 1/y_r) > M   when b=-1.
```

Muse 1.3 independently verified, without assuming the conclusion, that `PB => C1`:

1. `t_r>=0` and `A` not dividing `t_r` imply `t_r>=1`.
2. Therefore `q_r>=y_r` for every rotation.
3. Termwise monotonicity plus the exact product identity contradicts PB+ or PB-.
4. Every factor is positive; in particular `p-1/y_r>p-1>=2`, so the `b=-1` comparison is legitimate.

This implication is a proved reduction. **PB itself is not proved.**

## 3. Remaining carry lemma

Muse reduced PB to bounded modular carries. Define integers `u_r` by

```text
2 h_{r+1} = p^{epsilon_r} h_r + b epsilon_r + M u_r.
```

Then

```text
u_r in {0,1}                         if epsilon_r=0,
u_r in {-(p-1),...,1}                if epsilon_r=1.
```

With `delta=M/A`,

```text
2 y_{r+1}
 = p^{epsilon_r} y_r + b epsilon_r
   + delta(2-p^{epsilon_r}+A u_r).
```

After telescoping, PB is equivalent to a product inequality involving only these bounded, correlated carries. The unresolved step is uniform control of the admissible cyclic `u_r` sequence. No argument currently bridges this step without becoming circular.

## 4. Exact local computation

All comparisons used Python integers and `fractions.Fraction`; no floating-point decision was used.

### C1 exhaustive raw-word scan (`m<=22`)

Each `p` scan covers all `2^22-1 = 4,194,303` words beginning with `1`, including repeated/nonprimitive words.

| p | rows with every `q_r>=1` | C1-premise rows | integral premise rows | nonintegral survivors |
|---:|---:|---:|---:|---:|
| 3 | 1,394,653 | 61 | 61 | 0 |
| 5 | 406,630 | 37 | 37 | 0 |
| 7 | 124,259 | 7 | 7 | 0 |

A separate primitive-necklace scan covered all 50 odd `p` values from 3 through 101 at `m<=16`: 439,950 `(p,necklace)` rows and zero nonintegral C1 survivors.

### Product Barrier scan

| scope | primitive necklaces | nonintegral checked | falsifiers |
|---|---:|---:|---:|
| `p=3, m<=22` | 401,427 | 401,423 | 0 |
| `p=3, m<=20` | 111,012 | 111,008 | 0 |
| `p=5, m<=20` | 111,012 | 111,008 | 0 |
| `p=7, m<=20` | 111,012 | 111,011 | 0 |
| odd `p=3..101, m<=16` | 439,950 | 439,934 | 0 |

The `m<=18` convention discrepancy in the ChatGPT/Muse reports was resolved: 31,041 primitive necklaces includes the length-one word; 31,040 is the `2<=m<=18` count. Their nonintegral counts agree after applying the same convention.

These are regression and falsification results only; they are not a proof.

## 5. Independent agents

### ChatGPT Web

The existing theory conversation was reopened automatically. It did not claim a proof or counterexample. It produced the Product Barrier reduction and explicitly classified C1 as `OPEN-NONTRIVIAL`.

### Muse Spark 1.3 — proof audit

Verdict: `OPEN-NONTRIVIAL`.

It verified:

- the `B_r` and `q_r` recurrences,
- positivity of every product factor,
- rotation-invariance of divisibility,
- the non-circular proof `PB => C1`,
- the bounded-carry reduction.

It did not prove PB and did not find a counterexample.

### Muse Spark 1.3 — independent falsifier

Verdict: `BOUNDED-PASS`.

Its independent implementation reported 1,665,552 nonintegral primitive-necklace checks over a staircase reaching `m<=22` for `p in {3,5,7}`, with zero falsifiers. Its ephemeral scratch files were removed when the sandbox ended, so this wider number is retained as agent evidence, not promoted above the reproducible local JSON results. The full Muse event log and reported program hashes are preserved.

### Jev advisory gate

Jev was used only as an `ADVISORY` pre-filter:

- first pass: `promising=0.71`, `proof_ready=0.18`, `circular_risk=0.43`;
- follow-up: `accept=0.33`, `needs_lemma=0.67`, `reject=0.00`.

Its stated bottleneck matched the exact analysis: the carry recurrence/congruence must force divisibility without assuming it.

## 6. Prior art boundary

Böhm–Sontacchi parity-word rational forms and unique parity residue classes are established prior art. Rukhin's immutable arXiv v8 paper presents dual-radix modular division, quotient cylinders, and prefix/suffix tests for integrality of Böhm–Sontacchi numbers:

- https://arxiv.org/abs/1506.07622v8

This is directly relevant and prevents any unsupported novelty claim. The inspected statements do not supply the Product Barrier inequality. A full literature comparison would still be required before claiming that PB or the carry formulation is new.

## 7. Decision

**Do not kill C1 yet. Do not promote it to a theorem.**

The original integrality/realizability split remains killed. The oriented-lift continuation has survived serious exact falsification and now has one sharply stated open core: the bounded-carry Product Barrier lemma.

The next mathematically justified action is one of:

1. prove the bounded-carry product inequality from the cyclic `u_r` constraints;
2. find a counterexample, concentrating first on near-resonance cases `|2^m-p^k|` small;
3. compare the carry lemma explicitly with Rukhin's quotient-cylinder/prefix machinery to determine whether it is already implied by a known integrality test.

Even a proof of C1 would be only an integrality certificate for cycle words. It would not by itself eliminate nontrivial integer cycles, prove convergence, or solve Collatz.

## 8. Reproducibility

Primary files:

- `lift_coherence.py`
- `test_lift_coherence.py`
- `lift_allwords_p{3,5,7}_m22.json`
- `lift_scan_odd_p3_101_m16.json`
- `product_barrier_p{3,5,7}_m20.json`
- `product_barrier_p3_m22.json`
- `product_barrier_odd_p3_101_m16.json`
- `evidence/chatgpt_c1_full_history.json`
- `evidence/muse_pb_prove_full.jsonl`
- `evidence/muse_pb_falsify_full.jsonl`
- `evidence/jev_c1_*.json`

Selected SHA-256 values:

```text
abfa5d93b9a918c76a8982d1ce874f40ae8649f8b24c5f56cfc53562ae50b7fb  lift_coherence.py
689b84f75d56189c67e450307e565621ca9fa63d1381051e422c5fb1b60d82c0  test_lift_coherence.py
169649e1d5e1eb11025dfd038517a5b8dd25fa5708b704bde087ef7eac6a5a0b  lift_allwords_p3_m22.json
72b5eb2c760d901cc30b971f5fe6f30c946168d4ba29669f4f5896fc51cc5282  product_barrier_p3_m22.json
0a871cb64391b33a2d4f218ee513b51bd6486c220fba7fcaa497f514b855361e  product_barrier_odd_p3_101_m16.json
56f98d179f64922a4901706e8e2ef3b032874351e7a9117831fa9100289f1053  evidence/muse_pb_prove_full.jsonl
38c9bd2fe7e08cad9ef461e1e8a802db95c8e0adc54b2ed415ff67635e91c214  evidence/muse_pb_falsify_full.jsonl
8ab46d18ea3d6978a457bc37b05cfbb8e431730d3655316df84ace94f79d1a6b  evidence/chatgpt_c1_full_history.json
```
