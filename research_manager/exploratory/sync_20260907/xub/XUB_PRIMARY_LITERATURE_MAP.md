# XUB primary-literature map and Tao-style pair mechanism

Date: 2026-09-07

Verdict: no reviewed black-box theorem found that directly supplies XUB `O(1/m)` for this endpoint-conditioned, first-crossing, state-dependent complex product.

## Nearby results and mismatches

- Caravenna, *A Local Limit Theorem for Random Walks Conditioned to Stay Positive*: <https://arxiv.org/abs/math/0406182>. Positive killed/local probabilities; no state-dependent complex cancellation.
- Caravenna--Chaumont, *An invariance principle for random walk bridges conditioned to stay positive*: <https://arxiv.org/abs/1204.6148>. Closes BLL/KUB, not crossing XUB.
- Grama--Lauvergnat--Le Page, finite-Markov-chain conditioned LLT: <https://arxiv.org/abs/1707.06129>. Finite positive driver; the project state is infinite/dense and the multiplier does not descend to a finite quotient.
- Hervé--Ledoux, finite Markov-additive LLT: <https://arxiv.org/abs/1306.5353>. Finite-state spectral assumptions do not match.
- Diaconis--Saloff-Coste, complex convolution powers on `Z`: <https://arxiv.org/abs/1205.6490>. Translation-invariant, finitely supported convolution; the project kernel is state-dependent and has unbounded geometric jumps.
- Dolgopyat--Sarig, inhomogeneous Markov-chain LLTs: <https://arxiv.org/abs/2109.05560>. Uniform ellipticity/mixing and real additive-functional hypotheses do not match this null-recurrent killed bridge with `q(x)`.

The closest proof architecture is Tao, *Almost All Orbits of the Collatz Map Attain Almost Bounded Values*, Proposition 1.17 and Section 7: <https://arxiv.org/abs/1909.03562>. Tao's theorem does not directly apply, but its pair conditioning and white/black renewal mechanism suggests a concrete new lemma.

## Exact pair-total reduction

For a post-crossing pair, condition on `B=Y_1+Y_2=b`. Since

```text
p(u)p(b-u)=(1-rho)^2 rho^b,
```

the split `u` is uniform on `0,...,b`. Entering the pair at state `x`, the exact two-step phase average is

```text
A_b(x)=q(x)/(b+1) * sum_(u=0)^b q(x+u-beta),
x'=x+b-2*beta.
```

The exit state depends only on `b`, not on the split. For `b=1`,

```text
|A_1(x)|=|cos(pi*2^(x-beta))|.
```

Hence, whenever `dist(2^(x-beta),Z)>=eta`, a `B=1` block contracts by at most `cos(pi*eta)<1`.

For many pairs, the totals have

```text
P(B=b)=(b+1)(1-rho)^2 rho^b.
```

Conditioning on their global sum weights a totals vector proportionally to `product_j(B_j+1)`, while splits remain conditionally independent and uniform.

The crossing indicator cannot be factorized blindly inside a pair because it may depend on the split. The safe route is to cut at the exact first-passage/overshoot time, isolate a possible one-step parity alignment, and use pair contraction only on complete post-crossing pairs; equivalently one can introduce a crossed/not-crossed `2x2` block operator.

## Next load-bearing lemma

For complete post-crossing pairs define

```text
N_eta=#{j:B_j=1 and dist(2^(x_j-beta),Z)>=eta}.
```

Split averaging gives the exact domination

```text
modulus <= exp(-c_eta*N_eta).
```

A sufficient quantitative target is therefore a uniform/summably weighted bound of the form

```text
E[exp(-c_eta*N_eta) | endpoint and first-passage/overshoot data] <= C/m.
```

This turns the vague phrase “arithmetic cancellation” into a precise white-block occupation problem for the conditioned negative-binomial pair-total bridge. The load-bearing issue is to exclude quantitatively long ternary high-conductor black regions. This lemma, and therefore XUB, remains **`[OPEN]`**.
