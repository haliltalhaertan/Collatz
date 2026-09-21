# CP25 — Sign-Sensitive Cycle-Word Pilot

**Date:** 2026-09-20
**Status:** KILL (planned sign + integrality + realizability route)
**Collatz status:** OPEN / NOT PROVED

> **2026-09-21 continuation:** The original route remains `KILL`. A separate continuation, oriented lift coherence / Product Barrier, is documented in [`CP25_C1_LIFT_COHERENCE_REPORT.md`](CP25_C1_LIFT_COHERENCE_REPORT.md) with status `OPEN-NONTRIVIAL`; it is not part of the killed claim and is not a theorem.

## 1. Question

For

\[
H_{p,b}(x)=\begin{cases}
x/2,&x\equiv0\pmod2,\\
(px+b)/2,&x\equiv1\pmod2,
\end{cases}
\qquad p\ge3\text{ odd},\ b\in\{-1,+1\},
\]

can the sign of the cycle denominator, its divisibility, and separate parity-word realizability supply a nontrivial sign-sensitive obstruction that survives the CP23/CP24 energy kill?

## 2. Definitions

Let `w=(eps_0,...,eps_{m-1})` be a nonempty binary word with `eps_0=1`, let

\[
k=\sum_{j=0}^{m-1}\varepsilon_j,
\qquad
B_w=\sum_{j:\varepsilon_j=1}2^j p^{\sum_{i>j}\varepsilon_i},
\qquad
D=2^m-p^k.
\]

Formal composition along `w` gives

\[
H_w(x)=\frac{p^k x+bB_w}{2^m}.
\]

Since `m>0`, `k>0`, and `p` is odd, `D` cannot vanish. A formal cycle candidate is

\[
x=\frac{bB_w}{D}.
\]

This is the standard parity-vector/cycle setup rather than a new representation: the classical literature assigns each length-`m` vector a unique residue class, and Böhm–Sontacchi already use the finite enumeration of binary vectors to decide fixed cycle lengths.[1][2][3]

## 3. Exact lemma: integrality already forces realizability

### Lemma

If `D` divides `b B_w`, then the integer `x=bB_w/D` follows the parity word `w` under the actual piecewise map `H_{p,b}` and returns to `x` after `m` steps. This remains true when `x<0`.

### Proof

For the prefix `w_{<j}` let `k_j` be its number of ones and `B_j` its affine numerator. Write

\[
N_j=p^{k_j}x+bB_j.
\]

Splitting the full numerator into prefix and suffix gives, for an integer suffix numerator `C_j`,

\[
p^kx+bB_w=p^{k-k_j}N_j+b2^jC_j.
\]

The cycle equation is

\[
p^kx+bB_w=2^m x.
\]

Reducing the split identity modulo `2^j` and using that `p` is odd shows `2^j | N_j`. Hence

\[
y_j=N_j/2^j
\]

is an integer for every prefix.

If `eps_j=0`, divisibility of `N_{j+1}=N_j` by `2^{j+1}` makes `y_j` even. If `eps_j=1`, divisibility of

\[
N_{j+1}=pN_j+b2^j
\]

by `2^{j+1}` makes `p y_j+b` even; since both `p` and `b` are odd, `y_j` is odd. Thus every formal branch is the branch selected by the actual parity of the current integer. Finally, `N_m/2^m=x`, so the actual trajectory returns after `m` steps. The argument is over the integers and does not assume `x>0`. ∎

### Corollaries

1. `D | bB_w` is equivalent to `D | B_w`; divisibility is independent of the sign `b`.
2. `B_w>0`, so `x>0` exactly when `sign(D)=b`.
3. Parity-word realizability is not a second filter after divisibility. It is automatic.
4. For `p=3`, the same divisible words are split by the denominator sign: the `+1` map keeps `D>0`, while the `-1` map keeps `D<0`.

## 4. Exhaustive finite computation

`cycle_word_sign_pilot.py` enumerates every word beginning with `1`, computes exact integer `B_w`, `D`, and `x`, verifies the actual trajectory, and canonicalizes primitive positive cycles. `results_m22.json` covers

\[
\sum_{m=1}^{22}2^{m-1}=4,194,303
\]

words for each map, or 12,582,909 map/word rows in total.

| Map | Divisible rows | Positive rows | Realized positive rows | Distinct primitive positive cycles |
|---|---:|---:|---:|---:|
| `3n+1` | 61 | 11 | 11 | 1 |
| `3n-1` | 61 | 50 | 50 | 3 |
| `5n+1` | 37 | 26 | 26 | 3 |

The positive `3n-1` primitive cycles found are:

- `(1)`;
- `(5,7,10)`;
- `(17,25,37,55,82,41,61,91,136,68,34)`.

Under sign reflection these agree with the classical negative `3n+1` cycles based at `-1`, `-5`, and `-17`, whose periods are reported as 1, 3, and 11.[3]

The counts are **word rows**, so repetitions of a primitive cycle at lengths `2m`, `3m`, and so on are counted again. They are not counts of distinct cycles.

## 5. Verdict

**KILL** for the planned CP25 route.

The sign is genuinely visible, but only through the classical positivity condition

\[
2^m>3^k\quad(b=+1),
\qquad
2^m<3^k\quad(b=-1).
\]

Divisibility does not see `b`, and realizability contributes no additional constraint once divisibility holds. Therefore the proposed combination does not advance beyond the classical parity-vector cycle equation. The exact scan is a regression check and a finite census, not a proof of the Collatz conjecture or of global cycle exclusion.

## 6. Safe redirect

Do not extend the same scan to larger `m` and call that theoretical progress. A next lemma must use information absent from the scalar equation `D x=bB_w`.

Candidate pilot:

> **Rotation-gap divisibility.** For cyclic rotations `rho^i(w)`, derive exact differences `B_{rho^i(w)}-B_{rho^j(w)}` and test whether `D` dividing every rotation numerator forces forbidden local word structure in the `D>0` regime.

Fast kill conditions:

1. the claimed restriction reduces to `D|B_w` or `D>0`;
2. it also falsely excludes one of the known `3n-1` cycles above;
3. exhaustive word tests find a nontrivial `D>0` counterexample;
4. the argument is sign-blind and supplies no condition beyond an already-classical circuit class.

A literature/novelty check must precede any `[PROOF]` label.

## 7. Reproduction

```bash
python -B -m unittest research_track/CP25_SIGN_SENSITIVE_CYCLE_PILOT/test_cycle_word_sign_pilot.py
python -B research_track/CP25_SIGN_SENSITIVE_CYCLE_PILOT/cycle_word_sign_pilot.py \
  --max-m 22 \
  --output research_track/CP25_SIGN_SENSITIVE_CYCLE_PILOT/results_m22.json
```

## Sources

[1] https://eudml.org/doc/290184 — Böhm and Sontacchi (1978): cycles of given length
    > "Böhm, Corrado, and Sontacchi, Giovanna. "On the existence of cycles of given length in integer sequences like $x_{n+1} = x_{n}/2$ if $x_{n}$ even, and $x_{n+1} = 3 x_{n} + 1$.""
[2] https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/node4-an.shtml — Lagarias survey: parity vectors and residue classes
    > "Theorem B allows one to associate with each vector of length k a unique congruence class."
[3] https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/node8-an.shtml — Lagarias survey: non-trivial cycles
    > "Böhm and Sontacchi also noted that this gives an (inefficient) finite procedure for deciding if there are any cycles of a given length k."
