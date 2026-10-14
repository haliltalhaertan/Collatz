# CP25-PB-PROVE report (read-only; Collatz is OPEN)

**Verdict: OPEN-NONTRIVIAL**

PB is well-formed and `PB => C1` is valid, but PB itself is neither proved nor refuted here. It is genuinely stronger than C1, not algebraically equivalent, and not trivial. Finite searches below are evidence only.

Scratch used: `/tmp/cp25-pb-prove` (`pb_search.py`, `pb_search2.py`, `pb_gap.py`, `pb_target.py`, `pb_exh.py`, `pb_reduce_check.py`, `pb_instances.py`). No workspace writes.

## 1. Definitions and elementary checks

Assume `m>=1`, `p>=3` odd, `w` length `m` with `k` ones. `M=2^m`, `P=p^k`, `D=M-P`, `b=sign(D)`, `A=|D|`.

- `D!=0`: `M` even, `P` odd, so `D` odd nonzero. Hence `b=+-1` defined, `A>=1` odd, `gcd(A,M)=1`, `gcd(P,M)=1`, `gcd(p,A)=1` (a divisor of `p,A` divides `M`, hence 1), `gcd(2,A)=1`.
- `k=0` edge: `B_r=0`, empty product convention needed; assume `k>=1` below. Then each `B_r>=1` (sum of `k` terms each `2^j p^e>=1`), so `q_r=B_r/A>0`.
- `A=1` edge: `A|B_0` always; PB hypothesis `A∤B_0` vacuous, PB and C1 both vacuous. Assume `A>1` when testing PB.
- `B_r`: for rotation `rot_j=eps_{r+j}`, `B_r=sum_{j:rot_j=1} 2^j p^{#later ones}`. Well-defined integer `>=0`.
- `h_r`: `P` invertible mod `M`; `-b B_r P^{-1}` has exactly one residue mod `M`, represented in `{1,...,M}` (`M` stands for `0`). Existence/uniqueness OK.
- `h_r==A^{-1}B_r (mod M)`: `D=bA=M-P`, so `P==-bA (mod M)`. Since `(-b)^{-1}=-b`, `P^{-1}==-bA^{-1}`, so `-bBP^{-1}==BA^{-1}`. Uses `A` odd (invertible mod `M`). Verified numerically on all tested words.
- `B_r=Ah_r+Mt_r`: holds with `t_r=(B_r-Ah_r)/M∈Z` since congruence gives `M|(B_r-Ah_r)`. `t_r` may be negative. `M/A>0` so `y_r=h_r+M/A>0`, `q_r=h_r+(M/A)t_r`.

## 2. Exact identity and positivity; rotation invariance

B-recurrence (proved, not assumed). With `D=M-P=bA`:

```text
2B_{r+1} = p^{eps_r} B_r + eps_r D = p^{eps_r} B_r + b eps_r A.
```

Proof: if `eps_r=0`, dropping a leading `0` halves `B`. If `eps_r=1`, the leading `1` moves to the end: intermediate `p`-exponents rise by 1 (the moved `1` goes from before them to after them), giving `B_r=p^{k-1}+(2/p)(B_{r+1}-2^{m-1})`, i.e. `pB_r=P+2B_{r+1}-M`. Rearranged is the claim. Checked exactly on ~30k words.

Dividing by `A`, with `q_r=B_r/A`:

```text
2q_{r+1} = p^{eps_r} q_r + b eps_r.   (1)
```

Hence `q_{r+1}/q_r=1/2` if `eps_r=0`, and `=(p+b/q_r)/2` if `eps_r=1` (valid since `q_r>0`). Cyclic telescoping `∏q_{r+1}/q_r=1` gives:

```text
∏_{r:eps_r=1}(p+b/q_r) = 2^m = M.   (2)
```

Positivity of factors:

- `q`-factors: `p+b/q_r=2q_{r+1}/q_r>0` exactly. No extra hypothesis.
- `y`-factors: `y_r>=1+M/A`, so `1/y_r<=A/(A+M)<1`, hence `p+b/y_r>=p-1/y_r>p-1>=2>0` for both `b`. In particular `b=-1` factors are strictly positive; termwise monotonicity below is legitimate. This answers the `b=-1` concern affirmatively (both families positive).

Rotation invariance of `A|B`: mod `A`, `2B_{r+1}==p^{eps_r}B_r`. Since `2,p` invertible mod `A`, `A|B_r⇔A|B_{r+1}`. Also `B_r=Ah_r+Mt_r` with `gcd(A,M)=1` gives `A|B_r⇔A|t_r`. So `A|B_0⇔A|B_r∀r⇔A|t_r∀r`.

## 3. `PB => C1` is valid (non-circular)

Assume all `t_r>=0` and, for contradiction, `A∤B_0`. Then `A>1` and by invariance `A∤B_r∀r`, i.e. `A∤t_r∀r`. Since `0` is divisible by `A`, `t_r>=0,A∤t_r⇒t_r>=1∀r`. Thus `q_r=h_r+(M/A)t_r>=h_r+M/A=y_r>0`.

- `b=+1`: `q>=y⇒p+1/q<=p+1/y` (all `>0`), so `M=∏(p+1/q)<=∏(p+1/y)<M` by PB. Contradiction.
- `b=-1`: `q>=y⇒p-1/q>=p-1/y>0`, so `M=∏(p-1/q)>=∏(p-1/y)>M` by PB. Contradiction (equality on support still contradicts strict `>M`).

No step assumes C1 or `A|B`. The only inputs are (1)-(2), invariance, positivity. So the implication is proved and non-circular.

## 4. PB status: no proof, no counterexample

Exact-arithmetic searches (Fractions, independent implementation of `B,h,t`, asserting (1)-(2) each time):

- `p=3,m<=8`, primitive, `k>=1`: 465 non-divisible words, 0 violations.
- `p=5,7,m<=10`: 3906 words, 0 violations.
- Random `p∈{3,5,7,9,11},m∈9..25`: 2983 words, 0 violations.
- Random nontrivial core `m∈10..40` (see §6): 5376 words, 0 violations.
- Exhaustive `p=3,m=15` (32763) and `m=16` (65532): 0 violations.
- Targeted: `t_r==1` on all `1`-support with `A>1,A∤B_0` (which would give `∏_y=M`, killing strict PB): 24052 words `m<=12`, 0 occurrences.

Evidence only; no theorem.

Two exact instances for audit:

```text
p=5,m=7,w=(1,0,0,0,1,1,0): M=128,P=125,b=+1,A=3
B=(137,344,172,86,43,109,274), h=(3,72,100,114,57,79,6), t=(1,1,-1,-2,-1,-1,2)
prod_y=1883980672/14951495≈126.006<128.  Trivial bound (p+1)^k=216>M, useless.
p=3,m=4,w=(1,1,1,0): M=16,P=27,b=-1,A=11
B=(19,23,29,38), h=(9,5,7,2), t=(-5,-2,-3,1)
prod_y=18081424/759345≈23.812>16.  Trivial bound (p-1)^k=8<M, useless.
```

Both have mixed-sign `t`, i.e. lie outside C1's hypothesis yet PB constrains them — PB is broader than C1.

## 5. Reduction to one precise lemma (h/y recurrence + telescoping)

From `B_r=Ah_r+Mt_r` and `2B_{r+1}=p^{eps}B_r+beps A`, put `δ=M/A`, `s_r=p^{eps_r}t_r-2t_{r+1}`. Then `δs_r=2h_{r+1}-p^{eps_r}h_r-beps_r∈Z`, so `A|s_r` (as `gcd(M,A)=1`); write `s_r=Au_r`. Hence for every `r`, with `h∈[1,M]`:

```text
2h_{r+1} = p^{eps_r} h_r + b eps_r + M u_r,   (3)
2y_{r+1} = p^{eps_r} y_r + b eps_r + δ(2-p^{eps_r}+A u_r),  y_r=h_r+δ. (4)
u_r=(2h_{r+1}-p^{eps_r}h_r-b eps_r)/M ∈ Z,
u_r∈{0,1} if eps_r=0; u_r∈{-(p-1),..,1} if eps_r=1.   (5)
```

Bounds: `eps=0`: `(2-M)/M<u_r<(2M-1)/M`, i.e. `>-1,<2`. `eps=1`: `(2-b)/M-p<u_r<2-(p+b)/M`, i.e. `>-p,<2` using `p+b>=2`. Verified on 1943 random words.

Let `S={eps=1}`, `Z={eps=0}`, `R_r=2y_{r+1}/y_r>0`. Then `∏_{all r}R_r=2^m=M` telescopes. With `g_r=p+b/y_r` and `c_r=g_r/R_r=1-δ(2-p+Au_r)/(2y_{r+1})` (`r∈S`), and `R_r=1+δ(1+Au_r)/y_r` (`r∈Z`), exact algebra gives:

```text
(∏_{r∈S} g_r)/M = (∏_{r∈S} c_r)/(∏_{r∈Z} R_r).   (6)
```

Identity (6) verified exactly on the same 1943 words. PB is therefore exactly this carry lemma:

**Lemma (remaining):** under `A∤B_0` (`A>1`), with `u_r,y_r` from (3)-(5), `∏_S c_r<∏_Z R_r` if `b=+1`, and `>` if `b=-1` (empty `Z` product `=1`; `S` nonempty as `A∤B_0⇒k>=1`).

This is not a restatement: it replaces `q,t` by the bounded carries `u_r` and a telescoped ratio. Proving it still requires uniform control of the `u_r` sequence (correlated modular carries), which is the open core.

## 6. Stronger vs circular vs trivial

- Not `TRIVIAL`: `h>=1` alone gives `∏_y>(p-1)^k` (`b=-1`) and `∏_y<(p+1)^k` (`b=+1`, since `1/y<1`). The §4 examples have `(p-1)^k<M` resp. `(p+1)^k>M`, so these bounds do not decide PB, yet PB holds. A trivial regime exists (`(p-1)^k>M` resp. `(p+1)^k<M`, e.g. `p=3,m=5,w=(1,0,1,0,0)` with `(p+1)^k=16<32`), but the core above is nontrivial.
- Not `CIRCULAR`/equivalent: C1 constrains only all-`t>=0` words; PB constrains all non-divisible words including mixed-sign `t` (both §4 instances). C1 cannot imply PB. The `PB=>C1` proof uses no hidden divisibility assumption. A proof attempt via "`t_r>=1` hence `q>=y`" without the C1 hypothesis would be circular, but the statement itself is strictly stronger (it in particular forbids `t==1` on support with `A>1`, observed 0 times in 24052 words but unproved).
- Hence `OPEN-NONTRIVIAL`: well-formed, implication valid, universal residue inequality unproved, no counterexample, reduction to the carry lemma (3)-(6).

Collatz remains open; nothing here claims a cycle theorem.
