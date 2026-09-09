# COLLATZ CP17 — FINAL STANDALONE PROOF
## Expository closure after V3.1

**Status:** `[PROVED — final expository patch; submit to one fresh zero-trust audit]` on the stated positive injective odd-only Syracuse-orbit domain.

This document changes **no mathematical mechanism and no constant** from CP17-V3.1.  Its sole purpose is to make every load-bearing lemma locally readable.  Historical CP9/CP10/CP11/CP12/CP13/CP17 sources remain in the final ZIP only as provenance; no inference below is justified merely by saying “see CP10/CP11/CP13”.

All logarithms are natural unless a base is displayed explicitly.

---

# 1. Domain, notation, and exact final theorem

Let

\[
n_{k+1}=\frac{3n_k+1}{2^{a_k}},\qquad a_k=v_2(3n_k+1)\ge1,
\]

be a **positive injective odd-only Syracuse orbit**.  Put

\[
A_k=\sum_{i<k}a_i,\qquad \alpha=\log_2 3,
\]

\[
D_k=A_k-\alpha k,
\qquad
s_k=\lfloor \alpha k\rfloor-A_k.
\]

Then exactly

\[
\boxed{D_k=-s_k-\{\alpha k\}.}
\tag{1.1}
\]

Define

\[
H_N=\sum_{k<N}\frac1{n_k}.
\]

The theorem proved below is

\[
\boxed{
\limsup_{N\to\infty}\frac{H_N}{\log\log N}
\le K_{17}<2.742882<3,
}
\tag{1.2}
\]

where

\[
\beta_0=\frac{4(\alpha-1)}{\alpha+2},
\qquad
I(c)=c\log2-[c\log c-(c-1)\log(c-1)],
\]

and

\[
\boxed{K_{17}=\frac{\beta_0\log2}{3I(\alpha)}.}
\tag{1.3}
\]

Consequently there are no constants \(C,k_0\) such that

\[
s_k\le \log_2 k+C\qquad(k\ge k_0),
\]

and therefore

\[
\boxed{
\limsup_{k\to\infty}(s_k-\log_2k)=+\infty.
}
\tag{1.4}
\]

No multiplicative conclusion \(\limsup s_k/\log_2k>1\) is asserted.  The theorem does not exclude general divergence or nontrivial cycles and is not a proof of the Collatz conjecture.

---

# 2. Exact carry identity and the coefficient-3 lower bound

Define

\[
U_N=\prod_{k<N}\left(1+\frac1{3n_k}\right).
\]

Multiplying the orbit relations gives

\[
n_k=n_0\frac{3^k}{2^{A_k}}U_k.
\]

Hence

\[
U_{k+1}-U_k=\frac{U_k}{3n_k}=\frac{2^{D_k}}{3n_0}.
\]

If

\[
X_N=\sum_{k<N}2^{D_k},
\]

then

\[
\boxed{U_N=1+\frac{X_N}{3n_0}.}
\tag{2.1}
\]

For \(x\ge0\), \(0\le x-\log(1+x)\le x^2/2\).  Taking \(x=1/(3n_k)\) gives

\[
0\le \frac1{n_k}-3\log\left(1+\frac1{3n_k}\right)
\le \frac1{6n_k^2}.
\]

Because the orbit is injective and positive odd,

\[
\sum_k\frac1{n_k^2}\le\sum_{m\ge1,\ m\text{ odd}}\frac1{m^2}=\frac{\pi^2}{8}.
\]

Therefore

\[
\boxed{
0\le H_N-3\log U_N\le\frac{\pi^2}{48}.
}
\tag{2.2}
\]

Now suppose, for contradiction, that for some fixed \(C,k_0\),

\[
s_k\le\log_2k+C\qquad(k\ge k_0).
\tag{2.3}
\]

Using (1.1),

\[
D_k\ge-\log_2k-C-1,
\]

so

\[
2^{D_k}\ge 2^{-C-1}k^{-1}.
\]

Thus

\[
X_N\ge 2^{-C-1}\log N+O_C(1),
\]

and (2.1) implies

\[
\log U_N\ge\log\log N+O_{n_0,C}(1).
\]

By (2.2),

\[
\boxed{
H_N\ge3\log\log N+O_{n_0,C}(1).
}
\tag{2.4}
\]

This is the exact lower side of the final contradiction.

---

# 3. Reachable terminals and canonical starts

The following lemma is used in the growing-depth decomposition and the harmonic ledger.

**Reachable-terminal lemma.** For a length-\(t\) positive valuation word \(\mathbf a=(a_0,\ldots,a_{t-1})\), exact iteration has the affine form

\[
2^A n_t=3^t n_0+B_{\mathbf a},\qquad A=\sum a_j,\quad B_{\mathbf a}>0.
\]

With terminal modulus \(Q_t=2\cdot3^{t+1}\), if one positive terminal representative of a class is genuinely reachable by \(\mathbf a\), then every positive representative of that class is reachable by the same word.  Hence the least reachable positive terminal \(r_y\) exists and equals the least positive representative of its admissible class.  If \(\mu_t(y)\) is the minimum total valuation among words reaching class \(y\), a minimum-valuation word reaches \(r_y\).  Define \(\xi_t(y)\) to be the least positive start obtained from \(r_y\) among minimum-valuation words.  Then

\[
\xi_t(y)\in\mathbb Z_{>0},\qquad (\xi_t(y),6)=1,
\]

canonical starts from distinct terminal classes are distinct, and with

\[
w_t(y)=\frac{3^t}{2^{\mu_t(y)}}
\]

one has

\[
\boxed{
\frac{w_t(y)}{r_y}<\frac1{\xi_t(y)}.
}
\tag{3.1}
\]

A complete proof is reproduced verbatim in **Appendix B**; thus no external terminal-representative convention is being assumed.

---

# 4. Growing-depth master inequality

Fix \(c\in(\alpha,2)\), put

\[
L=\lfloor ct\rfloor,
\qquad
p_t(c)=\Pr(G_1+\cdots+G_t\le L),\quad \Pr(G=a)=2^{-a},
\]

\[
\eta_t=\frac{3^t}{2^{L+1}},
\]

and

\[
B_t(c)=\sum_{\mu_t(y)\le L}\frac{w_t(y)}{r_y}.
\tag{4.1}
\]

The fully reindexed V3.1 reciprocal-composition proof is reproduced in **Appendix A**.  Its exact output is

\[
\boxed{
(1-\eta_t)H_N
\le
\frac{p_t(c)}3(\log N+1)+B_t(c)+O(\log^2(t+1)),
}
\tag{4.2}
\]

with an absolute implied constant.  The proof explicitly separates

\[
H_N=\frac1{n_0}+\sum_{1\le s<N}\frac1{n_s},
\]

runs unit-class blocks only from \(s\ge1\), derives terminal indices \(t+1\le k<N+t\), first bounds the raw bad contribution by \(\eta_tH_{N+t}\), and only then replaces it by \(\eta_tH_N+o(1)\).  The accumulated composition error is uniformly \(O(\log^2(t+1))\).

For fixed \(c\), choose

\[
\boxed{
t=t(N,c)=\left\lceil\frac{\log\log N+2\log\log\log N}{I(c)}\right\rceil.
}
\tag{4.3}
\]

The geometric Chernoff bound gives \(p_t(c)\le e^{-I(c)t}\), while

\[
\eta_t\le 2^{-(c-\alpha)t}.
\]

Thus

\[
p_t(c)\log N=o(1),\qquad \eta_t\to0,
\qquad \log^2t=o(t),
\]

and

\[
\frac{t}{\log\log N}\to\frac1{I(c)}.
\tag{4.4}
\]

Consequently, if

\[
b(c)=\limsup_{t\to\infty}\frac{B_t(c)}t,
\]

then for every fixed \(c>\alpha\),

\[
\boxed{
\limsup_{N\to\infty}\frac{H_N}{\log\log N}
\le\frac{b(c)}{I(c)}.
}
\tag{4.5}
\]

---

# 5. The parity-prefix theorem, proved inline

We now prove the exact deterministic theorem used to locate the active harmonic right edge.  No CP11 citation is needed for the inference.

## 5.1 Shortcut parity-vector bijection

Let the shortcut map be

\[
\mathcal T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For \(x\in\mathbb Z_{\ge0}\), let

\[
e_i(x)=\mathcal T^i(x)\pmod2\in\{0,1\}.
\]

**Lemma 5.1 (parity-prefix bijection).** For every \(J\ge1\), the map

\[
x\pmod{2^J}\longmapsto(e_0(x),\ldots,e_{J-1}(x))
\]

is a bijection between \(\mathbb Z/2^J\mathbb Z\) and \(\{0,1\}^J\).

**Proof.** For \(J=1\), the first bit is exactly \(x\bmod2\).  Inductively suppose a length-\(J\) vector determines a unique class \(x\equiv r\pmod{2^J}\).  Along that vector,

\[
\mathcal T^J(x)=\frac{3^q x+C}{2^J}
\]

for an integer \(C\) and \(q\) equal to the number of odd bits.  The two lifts modulo \(2^{J+1}\) are \(r\) and \(r+2^J\); their \(J\)-th iterates differ by \(3^q\), which is odd.  Hence the next parity bit is opposite on the two lifts, so exactly one realizes each prescribed value of \(e_J\).  This proves the induction. ∎

## 5.2 Low total valuation forces few zeros

Start from an odd integer \(x\).  If its first \(t\) odd-only valuations are \(a_0,\ldots,a_{t-1}\), set

\[
A_t(x)=a_0+\cdots+a_{t-1}.
\]

In the shortcut parity word, the odd states occur at times

\[
0,\,a_0,\,a_0+a_1,\ldots,A_t(x).
\]

Thus among the first \(A_t(x)+1\) parity bits there are exactly \(t+1\) displayed odd bits.  If \(A_t(x)\le L\), then among the first \(L+1\) bits there are at least \(t+1\) ones, hence at most

\[
D=L-t
\]

zeros.  Every shorter prefix of length \(J\le L+1\) also contains at most \(D\) zeros.

Let

\[
N_t(M,c)=\#\{y:\mu_t(y)\le L,\ \xi_t(y)\le M\}.
\]

Every canonical start counted here is odd.  For \(1\le J\le L+1\), Lemma 5.1 and the preceding zero bound give

\[
\boxed{
N_t(2^J-1,c)
\le
\sum_{z=0}^{\min(D,J-1)}\binom{J-1}{z}.
}
\tag{5.1}
\]

This includes all endpoint cases: for \(J=1\) the right side is \(1\); if \(D\ge J-1\) it equals \(2^{J-1}\), the full set of odd prefixes; and \(J=L+1\) is allowed.

## 5.3 Exact tail inequality and \(\theta_{\max}\)

The reciprocal mass in the dyadic shell \(2^{J-1}\le\xi<2^J\) is at most

\[
2^{-(J-1)}N_t(2^J-1,c).
\]

For \(J\le L+1\), write

\[
J-1=2D+r,\qquad r\ge0.
\]

Then (5.1) gives exactly

\[
2^{-(J-1)}N_t(2^J-1,c)
\le
\Pr\{\operatorname{Bin}(J-1,1/2)\le D\}.
\]

The mean is \(D+r/2\), so Hoeffding yields

\[
\boxed{
2^{-(J-1)}N_t(2^J-1,c)
\le
\exp\!\left(-\frac{r^2}{2(J-1)}\right).
}
\tag{5.2}
\]

Summing over \(r\) gives \(O_c(\sqrt t)\).  For completeness, the support bound used here follows immediately from the canonical affine identity: if

\[
2^{\mu}r_y=3^t\xi_t(y)+B_y,
\qquad B_y>0,
\qquad r_y\le Q_t=2\cdot3^{t+1},
\qquad \mu\le L,
\]

then

\[
3^t\xi_t(y)<2^{\mu}r_y\le2^LQ_t,
\qquad\boxed{\xi_t(y)<6\,2^L.}
\tag{5.S}
\]

The support bound (5.S) leaves only \(O(1)\) dyadic shells with \(J>L+1\); the unit packing bound makes their total reciprocal mass \(O(1)\).  Hence all shells beyond

\[
J=2D+O(1)
\]

contribute only \(o(t)\).  With \(J\log2=\theta t\), the active right edge is therefore

\[
\boxed{\theta_{\max}(c)=2(c-1)\log2.}
\tag{5.3}
\]

---

# 6. Standalone harmonic ledger and exact saving-width subtraction

The canonical starts are distinct positive units modulo \(6\), hence

\[
\#\{n\le M:(n,6)=1\}=\frac M3+O(1)
\]

and therefore

\[
N_t(M,c)\le\frac M3+O(1).
\tag{6.1}
\]

This arithmetic packing is the exact source of the factor \(1/3\).

By (3.1), with \(X\ge\max_y\xi_t(y)\),

\[
B_t(c)<S_t(c):=\sum_y\frac1{\xi_t(y)}.
\]

Stieltjes summation gives exactly

\[
S_t(c)=\frac{N_t(X,c)}X+
\int_1^X\frac{N_t(u,c)}{u^2}\,du.
\tag{6.2}
\]

Since \(X<6\,2^L\), putting \(u=e^{\theta t}\) yields

\[
\frac{S_t(c)}t
=o(1)+
\int\frac{N_t(e^{\theta t},c)}{e^{\theta t}}\,d\theta.
\tag{6.3}
\]

Let \(E_c\subset(0,\theta_{\max}(c))\) be an open saving set with the property that for every compact \(F\subset E_c\) there are \(\delta_F>0,t_F\) such that

\[
N_t(e^{\theta t},c)\le e^{(\theta-\delta_F)t}
\qquad(t\ge t_F,\ \theta\in F).
\tag{6.4}
\]

On \(F\), the integrand in (6.3) is exponentially small.  On the complement below \(\theta_{\max}\), (6.1) makes it at most \(1/3+O(e^{-\theta t})\).  Above \(\theta_{\max}\), Section 5 gives \(o(t)\) total reciprocal mass.  Hence for every compact finite union \(F\subset E_c\),

\[
\limsup_{t\to\infty}\frac{B_t(c)}t
\le\frac{\theta_{\max}(c)-|F|}{3}.
\]

Inner regularity of Lebesgue measure lets \(|F|\uparrow|E_c|\).  Thus

\[
\boxed{
b(c)\le\frac{\theta_{\max}(c)-|E_c|}{3}.}
\tag{6.5}
\]

With \(E_c=\varnothing\), (5.3) gives

\[
b(c)\le\frac{2(c-1)\log2}{3},
\]

and the boundary value \(c\downarrow\alpha\) gives the no-new-saving regression

\[
\boxed{
K_{11}=\frac{2(\alpha-1)\log2}{3I(\alpha)}
=4.916563550949996880846\ldots.
}
\tag{6.6}
\]

---

# 7. Syracuse polynomial collision energy

Let \(A_1,\ldots,A_s\) be iid with \(\Pr(A_i=a)=2^{-a}\), put \(S_j=A_1+\cdots+A_j\), and define

\[
X_s=\sum_{j=1}^s3^{j-1}2^{-S_j}\pmod{3^s},
\qquad p_s(y)=\Pr(X_s=y),
\]

\[
\chi_s^{\rm Syr}=3^s\sum_yp_s(y)^2.
\]

The self-contained theorem is

\[
\boxed{\chi_s^{\rm Syr}=O(s^4).}
\tag{7.1}
\]

Its complete proof, including the 2-adic injectivity argument, integer encoding, martingale classes, cross-class Minkowski estimate, and large-gap tail, is reproduced in **Appendix C**.  In particular

\[
\log\chi_s^{\rm Syr}=O(\log(s+1))=o(s).
\tag{7.2}
\]

---

# 8. Prefix-cylinder theorem, proved inline

We next prove the exact CP13 counting lemma directly.

Let \(I\) be an interval of \(3^s\) consecutive integer suffix-start values.  Let \(R\ge0\) be a suffix length and require at least \(r\) ones in its length-\(R\) shortcut parity word.  Write \(\mathcal Y(R,s,r)\) for the number of values in \(I\) satisfying this success condition.

Fix \(0\le j\le R\).  By Lemma 5.1, every length-\(j\) parity prefix is exactly one residue class modulo \(2^j\).  Any interval of \(M\) consecutive integers meets one residue class modulo \(2^j\) either \(\lfloor M/2^j\rfloor\) or \(\lceil M/2^j\rceil\) times.  With \(M=3^s\), each prefix cylinder therefore contains at most

\[
\left\lceil\frac{3^s}{2^j}\right\rceil
\]

points of \(I\).

If the first \(j\) bits contain \(a\) ones, the remaining \(R-j\) bits can contribute at most \(R-j\) ones.  A necessary condition for eventual success is

\[
a\ge r-(R-j).
\]

Thus the number of potentially successful length-\(j\) prefixes is exactly bounded by the binomial tail

\[
\sum_{a\ge r-(R-j)}\binom ja,
\]

with the convention that a threshold \(\le0\) gives all \(2^j\) prefixes and a threshold \(>j\) gives zero.  Multiplying by cylinder occupancy gives, for every \(j\),

\[
\boxed{
\mathcal Y(R,s,r)
\le
\left\lceil\frac{3^s}{2^j}\right\rceil
\sum_{a\ge r-(R-j)}\binom ja.
}
\tag{8.1}
\]

Therefore

\[
\boxed{
\mathcal Y(R,s,r)
\le
\min_{0\le j\le R}
\left\lceil\frac{3^s}{2^j}\right\rceil
\sum_{a\ge r-(R-j)}\binom ja.
}
\tag{8.2}
\]

The endpoints are included: \(j=0\) is the empty-prefix bound, and \(j=R\) is the full Hamming-tail bound.

---

# 9. Uniform logarithmic bookkeeping lemma

The rate proof uses proportional integer parameters

\[
m=\beta t+O(1),\quad s=xt+O(1),\quad
R=(c-\beta)t+O(1),\quad j=\gamma t+O(1).
\]

Fix \(\varepsilon>0\) and restrict \(\beta\) to the compact saving band

\[
K_\varepsilon=[\beta_0+\varepsilon,\beta_*-\varepsilon],
\qquad \beta_*=2(\alpha-1),
\]

with \(c\in[\alpha,\alpha+\rho]\) for fixed small \(\rho\), and parameterize every moving feasible \(x\)-interval by a fixed \(u\in[0,1]\).  All proportional lengths are then \(O(t)\) uniformly.

**Lemma 9.1 (uniform polynomial bookkeeping).** All integer rounding, binomial-tail, ceiling, and finite-slice factors used below contribute only \(O_{\varepsilon,\rho}(\log(t+1))\) to a logarithmic count, uniformly on this compact parameter set.

**Proof.**

1. **Uniform binomial/type error.** For \(0\le k\le n\), with \(H(p)=-p\log p-(1-p)\log(1-p)\),
   \[
   \frac1{n+1}e^{nH(k/n)}\le\binom nk\le e^{nH(k/n)}.
   \tag{9.1}
   \]
   The upper bound follows by optimizing the corresponding term in \((p+(1-p))^n\).  For the lower bound take \(p=k/n\): the \(k\)-term is a mode of the binomial law, so its probability is at least \(1/(n+1)\).  Hence every Stirling/type replacement has log-error at most \(\log(n+1)=O(\log t)\), uniformly even at endpoints.

2. **Binomial tails.** A tail has at most \(n+1\) terms.  Combining this with (9.1) adds at most another \(\log(n+1)=O(\log t)\).  In the saturated half of the binomial cube we simply use \(2^n\), with no asymptotic error.

3. **Floors and ceilings in integer parameters.** Changing any of \(m,s,R,j,r,L\) by \(O(1)\) changes a binomial coefficient or a finite product of adjacent coefficients by at most a fixed power of \(t+1\); equivalently its log changes by \(O(\log t)\).  This follows from the adjacent ratios \(\binom{n+1}{k}/\binom nk=(n+1)/(n+1-k)\) and \(\binom n{k+1}/\binom nk=(n-k)/(k+1)\), with endpoint cases bounded directly by \((n+1)^{O(1)}\).

4. **Cylinder ceiling.** For every \(X>0\),
   \[
   \lceil X\rceil\le2\max(1,X).
   \tag{9.2}
   \]
   Hence
   \[
   \log\left\lceil\frac{3^s}{2^j}\right\rceil
   \le [s\log3-j\log2]_++\log2.
   \tag{9.3}
   \]
   The ceiling costs \(O(1)\) uniformly.  In the active branch \(\gamma=\alpha x\), \(s=xt+O(1)\) and \(j=\alpha xt+O(1)\), so \(3^s/2^j=2^{O(1)}\) and the entire occupancy factor itself is bounded by a constant depending only on the fixed rounding convention.

5. **Number of slices.** The first-block weight has at most \(m+1=O(t)\) possibilities; a prefix length has at most \(R+1=O(t)\) possibilities; all remaining case splits are finite.  Even if all such discrete indices are union-bounded simultaneously, their number is at most \(C_{\varepsilon,\rho}(t+1)^d\) for a fixed integer \(d\).  Its logarithm is \(O_{\varepsilon,\rho}(\log(t+1))\).

Multiplying any fixed number of these polynomial factors remains polynomial in \(t\), so the total logarithmic bookkeeping error is \(O_{\varepsilon,\rho}(\log(t+1))=o(t)\), uniformly on the compact band. ∎

---

# 10. Direct Syracuse bound and the strict saving band

## 10.0 Local counting chain from canonical starts to first-block slices

Fix \(t\ge1\), \(c>\alpha\), and

\[
L=\lfloor ct\rfloor.
\]

Recall the canonical-start counting function

\[
N_t(M,c)=\#\{y:\mu_t(y)\le L,\ \xi_t(y)\le M\},
\]

and define the ambient low-valuation unit-start count

\[
C_t(M,c)=\#\{1\le x\le M:(x,6)=1,\ A_t(x)\le L\}.
\]

Every canonical start counted by \(N_t\) is a positive unit start satisfying the same low-total-valuation condition, hence

\[
N_t(M,c)\le C_t(M,c).
\]

For odd shortcut starts, \(A_t(x)\le L\) is equivalent to saying that the first

\[
J=L+1
\]

shortcut parity bits contain at least

\[
q=t+1
\]

ones.  For a dyadic initial segment \(M=2^m-1\), let

\[
F(J,m,q)
\]

denote the number of integers \(0\le x<2^m\) whose first \(J\) shortcut parity bits contain at least \(q\) ones.  Since \(C_t\) has the additional unit restriction,

\[
C_t(2^m-1,c)\le F(L+1,m,t+1).
\]

Finally decompose \(F(L+1,m,t+1)\) according to the number \(s\in\{0,\ldots,m\}\) of odd steps in the first block of length \(m\).  Let \(W_s\) be the number of starts in that slice that satisfy the required suffix success condition.  The slices are disjoint and exhaustive, so

\[
\boxed{
N_t(2^m-1,c)
\le
C_t(2^m-1,c)
\le
F(L+1,m,t+1)
=
\sum_{s=0}^{m}W_s.
}
\tag{10.A}
\]

There are exactly \(m+1=O(t)\) possible values of \(s\) in the proportional regime \(m=\beta t+O(1)\).  Therefore replacing a uniform slice bound by the sum in (10.A) multiplies the count by at most \(m+1\), changing its logarithm by

\[
\log(m+1)=O(\log t)=o(t),
\]

uniformly on every compact saving band, in agreement with Lemma 9.1.

Split the first shortcut block into length \(m\) and weight \(s\).  Let its one positions be

\[
0\le i_1<\cdots<i_s<m.
\]

The fixed-word affine offset is

\[
C=\sum_{k=1}^s3^{s-k}2^{i_k},
\qquad
y\equiv2^{-m}C\pmod{3^s}.
\]

The alignment here is deliberately \(y\equiv2^{-m}C\pmod{3^s}\), not \(C\pmod{3^s}\).

Define the reverse partial gaps

\[
S_j:=m-i_{s+1-j},\qquad 1\le j\le s,
\qquad S_0:=0.
\]

Since \(i_s\le m-1\),

\[
S_1=m-i_s\ge1.
\]

Moreover, if \(1\le j<s\), then \(i_{s-j}<i_{s+1-j}\), and hence

\[
S_{j+1}=m-i_{s-j}>m-i_{s+1-j}=S_j.
\]

Thus

\[
1\le S_1<S_2<\cdots<S_s,
\qquad
S_s=m-i_1\le m.
\]

Now

\[
2^{-m}C
=\sum_{k=1}^s3^{s-k}2^{i_k-m}.
\]

With the substitution \(j=s+1-k\), one has \(i_k-m=-S_j\) and \(s-k=j-1\), so

\[
\boxed{
2^{-m}C
=\sum_{j=1}^s3^{j-1}2^{-S_j}.
}
\tag{10.RG}
\]

Define the positive gap tuple

\[
A_j:=S_j-S_{j-1},\qquad 1\le j\le s.
\]

Then \(A_j\in\mathbb Z_{>0}\), its partial sums are exactly the \(S_j\), and (10.RG) is precisely the canonical Syracuse offset associated with this admissible gap tuple.  Under the independent \(\operatorname{Geom}(2)\) gap law, the tuple has probability

\[
\prod_{j=1}^s2^{-A_j}=2^{-S_s}\ge2^{-m}.
\]

Consequently, if \(M(y)\) fixed-weight words have aligned endpoint residue \(y\), their distinct reverse-gap tuples all contribute to the Syracuse probability \(p_s^{\rm Syr}(y)\).  Summing their weights gives

\[
M(y)2^{-m}\le p_s^{\rm Syr}(y),
\]

and therefore

\[
\boxed{M(y)\le2^m p_s^{\rm Syr}(y).}
\tag{10.RG2}
\]

This is the reverse-gap alignment used below; it is a pointwise statement in the aligned residue \(y\equiv2^{-m}C\pmod{3^s}\).

**Lemma 10.1 (endpoint rectangle; only the \(\lambda=1\) case).**  Let \(x\) be a positive integer with \(x<2^m\).  Suppose the first \(m\) shortcut steps contain exactly \(s\) odd steps.  Then

\[
\boxed{\mathcal T^m(x)\le3^s-1.}
\tag{10.B}
\]

Equivalently, every first-block endpoint lies in the integer interval \([0,3^s)\).

**Proof.**  Put

\[
z_i=\mathcal T^i(x),\qquad
q_i=\#\{0\le h<i:z_h\text{ is odd}\}
\]

for \(0\le i\le m\).  We prove by induction on \(i\) the invariant

\[
z_i\le 3^{q_i}2^{m-i}-1.
\tag{10.C}
\]

At \(i=0\), \(x<2^m\) gives \(z_0=x\le2^m-1\), which is (10.C) with \(q_0=0\).

Assume (10.C) at some \(i<m\).

* If \(z_i\) is even, then the right side of (10.C) is odd, so the even integer \(z_i\) actually satisfies
  \[
  z_i\le3^{q_i}2^{m-i}-2.
  \]
  Hence
  \[
  z_{i+1}=\frac{z_i}{2}
  \le3^{q_i}2^{m-i-1}-1,
  \]
  while \(q_{i+1}=q_i\).

* If \(z_i\) is odd, then
  \[
  z_{i+1}=\frac{3z_i+1}{2}
  \le
  \frac{3(3^{q_i}2^{m-i}-1)+1}{2}
  =3^{q_i+1}2^{m-i-1}-1,
  \]
  while \(q_{i+1}=q_i+1\).

Thus (10.C) propagates.  At \(i=m\), \(q_m=s\), so \(z_m\le3^s-1\).  This proves the lemma.  (The omitted start \(x=0\), when present in the ambient dyadic count, is trivial.) ∎

The fixed-word affine identity has the form

\[
2^m\mathcal T^m(x)=3^s x+C,
\]

so the endpoint residue satisfies

\[
\mathcal T^m(x)\equiv2^{-m}C\pmod{3^s}.
\]

By Lemma 10.1 the actual integer endpoint belongs to \([0,3^s)\).  Consequently every residue class modulo \(3^s\) appearing in this first-block problem has exactly one representative in that interval, and the successful-residue set is exactly the successful integer set in the interval

\[
I=[0,3^s)
\]

to which the prefix-cylinder theorem of Section 8 applies.  Therefore, for suffix length \(R\), required suffix weight \(r\), and every \(0\le j\le R\),

\[
Y
\le
\left\lceil\frac{3^s}{2^j}\right\rceil
\sum_{a\ge r-(R-j)}\binom ja,
\]

and hence

\[
\boxed{
Y
\le
\min_{0\le j\le R}
\left\lceil\frac{3^s}{2^j}\right\rceil
\sum_{a\ge r-(R-j)}\binom ja.
}
\tag{10.D}
\]

This is the exact value-to-residue bridge needed before the rate estimate.

Therefore, for the fixed-word endpoint multiplicity \(M(y)\), the reverse-gap inequality (10.RG2) gives, in the same aligned residue coordinate,

\[
\boxed{M(y)\le2^m p_s^{\rm Syr}(y).}
\tag{10.1}
\]

If \(\mathcal Y\) is the set of suffix-success residues and \(Y=|\mathcal Y|\), then

\[
W=\sum_{y\in\mathcal Y}M(y)
\le2^m\sum_{y\in\mathcal Y}p_s(y)
\le
\boxed{2^m\sqrt{\frac{Y\chi_s^{\rm Syr}}{3^s}}}.
\tag{10.2}
\]

This is the canonical direct bound; no fixed-weight Stirling round trip is used.

For \(x\le1\), set

\[
m=\beta t+O(1),\quad s=xt+O(1),\quad R=(c-\beta)t+O(1),\quad r=(1-x)t+O(1).
\]

Applying (8.2) with \(j=\gamma t+O(1)\), let

\[
d=c-1-\beta+x.
\]

The successful prefix condition is equivalent to at most \(dt+O(1)\) zeros in the first \(j\) bits.  Lemma 9.1 gives uniformly

\[
\log Y
\le
P(c,\beta,x;\gamma)t+O(\log t),
\tag{10.3}
\]

where

\[
P(c,\beta,x;\gamma)
=[\alpha x-\gamma]_+\log2
+\gamma\Psi(d/\gamma),
\tag{10.4}
\]

and

\[
\Psi(z)=
\begin{cases}
H(z),&0\le z\le1/2,\\
\log2,&z\ge1/2.
\end{cases}
\]

If \(d<0\), the success set is empty and the desired saving is automatic.  Define

\[
Y_{\rm pref}(c,\beta,x)=
\inf_{0\le\gamma\le c-\beta}P(c,\beta,x;\gamma).
\tag{10.5}
\]

Using (7.2), (10.2), and Lemma 9.1,

\[
\boxed{
\frac1t\log W
\le
\beta\log2+
\frac12\bigl(Y_{\rm pref}(c,\beta,x)-x\log3\bigr)
+O\!\left(\frac{\log t}{t}\right).
}
\tag{10.6}
\]

Independently,

\[
W\le\binom ms
\]

and Lemma 9.1 gives

\[
\frac1t\log W
\le A_\beta(x)+O\!\left(\frac{\log t}{t}\right),
\qquad
A_\beta(x)=\beta H(x/\beta).
\tag{10.7}
\]

For \(x>1\), suffix success is automatic.  Since throughout the saving band \(\beta\le\beta_*<2\),

\[
A_\beta(x)\le A_\beta(1)=\beta H(1/\beta)<\beta\log2,
\tag{10.8}
\]

so this whole branch already has strict saving.

At \(c=\alpha\) and the entropy center \(x=\beta/2\), put

\[
R=\alpha-\beta,
\qquad
d=\alpha-1-\beta/2.
\]

Define

\[
\boxed{\beta_0=\frac{4(\alpha-1)}{\alpha+2}},
\qquad
\beta_{\rm sw}=\frac{2\alpha}{\alpha+2},
\qquad
\beta_*=2(\alpha-1).
\tag{10.9}
\]

For \(\beta_0<\beta\le\beta_{\rm sw}\), choose

\[
\gamma=\alpha x=\alpha\beta/2.
\]

The equality \(\gamma=2d\) is exactly \(\beta=\beta_0\); hence for \(\beta>\beta_0\), \(0\le d/\gamma<1/2\), and

\[
Y_{\rm pref}\le\gamma H(d/\gamma)<\gamma\log2=x\log3.
\tag{10.10}
\]

For \(\beta_{\rm sw}\le\beta\le\beta_*\), choose \(\gamma=R\).  Then \(0\le d/R<1/2\) in the open nontrivial range and

\[
x\log3-Y_{\rm pref}
\ge R[\log2-H(d/R)]>0.
\tag{10.11}
\]

At \(\beta=\beta_*\), \(d=0\) and the same inequality remains strict.  Thus

\[
\boxed{
Y_{\rm pref}(\alpha,\beta,\beta/2)<\frac\beta2\log3
\quad(\beta_0<\beta\le\beta_*).
}
\tag{10.12}
\]

To pass from the entropy centre to the full feasible \(x\)-domain, define

\[
A_\beta(x)=\beta H(x/\beta)
\]

as in (10.7), and on the nonempty-success branch define

\[
B_\beta(x)
=
\beta\log2+
\frac12\bigl(Y_{\rm pref}(\alpha,\beta,x)-x\log3\bigr).
\]

When the success set is empty, the corresponding slice count is zero and may be discarded.  The asymptotic slice rate is bounded by

\[
R_{17}(\alpha,\beta,x)
\le
\min\{A_\beta(x),B_\beta(x)\}
\]

on the nonempty branch, and by \(A_\beta(x)\) on the automatic-success branch \(x>1\).

For every feasible \(x\ne\beta/2\), strict concavity of binary entropy and the uniqueness of its maximum at \(1/2\) give

\[
A_\beta(x)<\beta\log2.
\]

At the unique entropy centre \(x=\beta/2\), (10.12) gives

\[
B_\beta(\beta/2)<\beta\log2
\qquad(\beta_0<\beta\le\beta_*).
\]

Thus for **every** feasible \(x\), at least one of the two available branches is strictly below \(\beta\log2\).  We now make the compactness upgrade explicit.  Let \(K\) denote the feasible compact \(x\)-domain and put

\[
x_0:=\beta/2.
\]

At \(x_0\), the prefix/Cauchy branch satisfies

\[
B_\beta(x_0)<\beta\log2.
\]

By continuity of \(B_\beta\) on the nonempty-success branch, and because \(x_0\) lies in that branch, there exist a neighbourhood \(U\subset K\) of \(x_0\) and \(\delta_1>0\) such that

\[
B_\beta(x)\le\beta\log2-\delta_1
\qquad(x\in U).
\]

On the compact complement \(K\setminus U\), one has \(x\ne\beta/2\).  Since

\[
A_\beta(x)=\beta H(x/\beta)
\]

has its unique maximum \(\beta\log2\) at \(x=\beta/2\), continuity and compactness give \(\delta_2>0\) such that

\[
A_\beta(x)\le\beta\log2-\delta_2
\qquad(x\in K\setminus U).
\]

For \(x\in U\), the nonempty-branch envelope satisfies \(R_{17}\le\min\{A_\beta,B_\beta\}\le B_\beta\), so it is at most \(\beta\log2-\delta_1\).  For \(x\in K\setminus U\), every slice is bounded by the entropy branch \(A_\beta\) (and empty-success slices are zero), so it is at most \(\beta\log2-\delta_2\).  Therefore uniformly on the whole feasible compact domain,

\[
R_{17}(\alpha,\beta,x)
\le
\beta\log2-\min(\delta_1,\delta_2).
\]

Hence

\[
\boxed{
\sup_xR_{17}(\alpha,\beta,x)<\beta\log2
\qquad(\beta_0<\beta\le\beta_*).
}
\tag{10.13}
\]

No claim is made that the maximizing \(x\) is the entropy centre; indeed the argument does not locate the maximizer at all.  The centre is used only to cover the unique point where the entropy branch itself is not strict.

For a fixed compact \(K_\varepsilon=[\beta_0+\varepsilon,\beta_*-\varepsilon]\), parameterize each feasible \(x\)-interval by \(u\in[0,1]\).  The finite branch functions, the infimum (10.5) over the compact \(\gamma\)-interval, and their minimum are continuous in \((c,\beta,u)\).  The strict gap at \(c=\alpha\) is therefore uniformly positive on the compact set \(K_\varepsilon\times[0,1]\).  Uniform continuity supplies \(\rho_\varepsilon>0\) such that the same strict exponential saving holds for every fixed

\[
\alpha<c<\alpha+\rho_\varepsilon,
\qquad \beta\in K_\varepsilon.
\tag{10.14}
\]

Finally, the total initial-segment count is the sum over at most \(m+1=O(t)\) first-block weights.  Lemma 9.1 shows that this polynomial number of slices changes the logarithm only by \(O(\log t)\), so (10.14) is exactly the compact saving property (6.4) in harmonic coordinate \(\theta=\beta\log2\).

---

# 11. Safe \(c\downarrow\alpha\) order and the final coefficient

This section deliberately avoids any statement such as \(\limsup_{c\downarrow\alpha}b(c)\le\cdots\) unless it is actually needed.  The proved quantifier order is the following.

Fix \(\varepsilon>0\).  Section 10 gives \(\rho_\varepsilon>0\) such that for every **fixed**

\[
c\in(\alpha,\alpha+\rho_\varepsilon)
\]

the saving set in the harmonic coordinate contains the image of

\[
[\beta_0+\varepsilon,\beta_*-\varepsilon],
\]

whose width is

\[
(\beta_*-\beta_0-2\varepsilon)\log2.
\]

For that fixed \(c\), first let \(N\to\infty\) in (4.5).  Sections 5–6 then give directly

\[
\limsup_{N\to\infty}\frac{H_N}{\log\log N}
\le
\frac{[2(c-1)-(\beta_*-\beta_0-2\varepsilon)]\log2}{3I(c)}.
\tag{11.1}
\]

The left side is independent of \(c\).  Now choose any sequence of fixed values \(c\downarrow\alpha\) inside that interval.  Since \(I(c)\to I(\alpha)>0\) and \(\beta_*=2(\alpha-1)\), (11.1) yields

\[
\limsup_{N\to\infty}\frac{H_N}{\log\log N}
\le
\frac{(\beta_0+2\varepsilon)\log2}{3I(\alpha)}.
\tag{11.2}
\]

Finally let \(\varepsilon\downarrow0\):

\[
\boxed{
\limsup_{N\to\infty}\frac{H_N}{\log\log N}
\le
K_{17}:=\frac{\beta_0\log2}{3I(\alpha)}.
}
\tag{11.3}
\]

No continuity or upper-semicontinuity property of the unknown function \(b(c)\) is asserted or required.

The final interval certificate proves

\[
\boxed{K_{17}<2.742882<3.}
\tag{11.4}
\]

It also reproduces

\[
\chi_1^{\rm Syr}=\frac53,
\qquad
\chi_2^{\rm Syr}=\frac{15}{7},
\tag{11.5}
\]

and the no-saving regression (6.6), with decimal displays

\[
K_{11}=4.916563550949996880846\ldots,
\]

\[
K_{17}=2.742881438765941863306\ldots.
\]

---

# 12. Final contradiction and exact scope

If an eventual additive upper slack existed, Section 2 would give

\[
\liminf_{N\to\infty}\frac{H_N}{\log\log N}\ge3.
\]

Section 11 gives

\[
\limsup_{N\to\infty}\frac{H_N}{\log\log N}\le K_{17}<3,
\]

a contradiction.  Hence

\[
\boxed{
\nexists C,k_0:\ s_k\le\log_2k+C\quad\forall k\ge k_0.
}
\]

Equivalently,

\[
\boxed{
\limsup_{k\to\infty}(s_k-\log_2k)=+\infty.
}
\]

Again, this does not imply \(\limsup s_k/\log_2k>1\), does not exclude a general divergent orbit, does not exclude nontrivial cycles, and does not prove the Collatz conjecture.

---

# Appendix A — Complete growing-depth master-inequality proof

# COLLATZ CP17-V3.1 — Growing-depth master inequality

## Standalone closure of the inherited fixed-depth bridge

**Status:** `[PROVED]` on the stated positive injective odd-only Syracuse-orbit domain, with the exceptional initial term \(1/n_0\) removed explicitly before every unit-class argument.

The purpose of this note is only to prove the growing-depth inequality

\[
\boxed{
(1-\eta_t)H_N
\le
\frac{p_t(c)}3(\log N+1)+B_t(c)+E(N,t,c)
}
\tag{M}
\]

with an error bound uniform in \(N\) and growing \(t\), namely

\[
\boxed{E(N,t,c)=O((\log(t+1))^2)=o(t)}
\tag{E}
\]

for the coefficient-extraction schedule used below. No appeal to “CP10 already proved this” is made.

---

# 1. Quantifiers and the exact growing-depth schedule

Let \((n_k)_{k\ge0}\) be a positive injective orbit of the odd-only Syracuse map

\[
n_{k+1}=\frac{3n_k+1}{2^{a_k}},
\qquad
 a_k=v_2(3n_k+1)\ge1,
\]

No unit assumption is imposed on the initial value \(n_0\).  However, for every \(k\ge1\),

\[
n_k=\frac{3n_{k-1}+1}{2^{a_{k-1}}}
\]

is odd and is nonzero modulo \(3\), because \(3n_{k-1}+1\equiv1\pmod3\) and \(2^{a_{k-1}}\) is a unit modulo \(3\).  Hence

\[
\boxed{\gcd(n_k,6)=1\qquad(k\ge1).}
\tag{1.0}
\]

Accordingly, every canonical residue-class, domination, and length-\(t\) block argument below is run only from starting indices \(s\ge1\).  The exceptional initial reciprocal is kept outside the block decomposition:

\[
\boxed{
H_N=\frac1{n_0}+\sum_{1\le s<N}\frac1{n_s},
\qquad \frac1{n_0}\le1.
}
\tag{1.0a}
\]

Define

\[
\alpha=\log_2 3.
\]

Fix first

\[
\boxed{c\in(\alpha,2).}
\]

All limits in \(N\) below are taken with this \(c\) fixed. Put

\[
h(c)=c\log c-(c-1)\log(c-1),
\]

\[
I(c)=c\log2-h(c)>0.
\tag{1.1}
\]

For sufficiently large \(N\), write

\[
L_N=\log\log N,
\qquad
\ell_N=\log L_N,
\]

and choose exactly

\[
\boxed{
t=t(N,c)=\left\lceil\frac{L_N+2\ell_N}{I(c)}\right\rceil.
}
\tag{1.2}
\]

Then

\[
t\to\infty,
\qquad
\frac{t}{\log\log N}\to\frac1{I(c)},
\qquad
t=O_c(\log\log N)=o(\log N).
\tag{1.3}
\]

The limit \(c\downarrow\alpha\) is **not** taken simultaneously with \(N\to\infty\): first fix \(c\), then let \(N\to\infty\), and only afterwards send \(c\downarrow\alpha\). This removes the need for uniform constants all the way to the endpoint \(c=\alpha\).

The error estimate (E) below has an absolute implied constant, independent of \(N,t,c\) and the particular injective orbit. Bounds involving \(I(c)\) or \(c-\alpha\) are for fixed \(c\); they are uniform on every compact subinterval of \((\alpha,2)\).

---

# 2. One-step and t-step reciprocal identities

The one-step recurrence gives exactly

\[
\frac1{n_k}
=
\frac3{2^{a_k}}\frac1{n_{k+1}}
+\varepsilon_k,
\tag{2.1}
\]

where

\[
\boxed{
\varepsilon_k
=
\frac1{n_k(3n_k+1)}
=
\frac1{2^{a_k}n_kn_{k+1}}>0.
}
\tag{2.2}
\]

For \(s\le i\), define

\[
Q_{s,i}=\prod_{h=s}^{i-1}\frac3{2^{a_h}},
\qquad Q_{s,s}=1.
\tag{2.3}
\]

Iterating (2.1) exactly \(t\) times yields

\[
\boxed{
\frac1{n_s}
=
\frac{Q_{s,s+t}}{n_{s+t}}
+R_{s,t},
}
\tag{2.4}
\]

with

\[
\boxed{
R_{s,t}
=
\sum_{i=s}^{s+t-1}Q_{s,i}\varepsilon_i.
}
\tag{2.5}
\]

If

\[
A_{s,t}=a_s+\cdots+a_{s+t-1},
\]

then

\[
Q_{s,s+t}=\frac{3^t}{2^{A_{s,t}}}.
\tag{2.6}
\]

Now sum (2.4) over exactly the unit-tail starting indices

\[
1\le s<N.
\]

Using (1.0a), one obtains the exact shifted identity

\[
\boxed{
H_N
=
\frac1{n_0}
+
\sum_{k=t+1}^{N+t-1}
\frac{3^t}{2^{A_{k-t,t}}}\frac1{n_k}
+R_+(N,t),
}
\tag{2.7}
\]

where

\[
\boxed{
R_+(N,t)=\sum_{s=1}^{N-1}R_{s,t}.
}
\tag{2.8}
\]

Thus there is no hidden use of the possibly non-unit initial point inside a canonical block: all composed blocks begin at \(s\ge1\), and their terminal indices are exactly

\[
k=s+t\in\{t+1,\ldots,N+t-1\}.
\tag{2.9}
\]

The isolated term \(1/n_0\le1\) is an absolute \(O(1)\) remainder.  The only potentially dangerous growing-depth composition error is \(R_+(N,t)\); the shifted terminal range in (2.9) will be treated explicitly in the good/bad split below.

---

# 3. The accumulated error in D- and U-notation

Define cumulative valuations and slack

\[
A_k=\sum_{j<k}a_j,
\qquad
D_k=A_k-\alpha k.
\tag{3.1}
\]

Then

\[
Q_{s,i}
=\frac{3^{i-s}}{2^{A_i-A_s}}
=2^{D_s-D_i}.
\tag{3.2}
\]

Therefore (2.8) can be reindexed exactly as

\[
\boxed{
R_+(N,t)
=
\sum_{i=1}^{N+t-2}\varepsilon_i
\sum_{s=\max(1,i-t+1)}^{\min(i,N-1)}
2^{D_s-D_i}.
}
\tag{3.3}
\]

The range follows from the simultaneous conditions \(1\le s<N\) and \(s\le i\le s+t-1\).  In the interior, where neither endpoint truncates the interval, this is precisely

\[
\varepsilon_i\sum_{j=0}^{t-1}2^{D_{i-j}-D_i}.
\]

Now define the exact carry product

\[
U_k=\prod_{j<k}\left(1+\frac1{3n_j}\right).
\tag{3.4}
\]

The orbit product gives

\[
U_{k+1}-U_k=\frac{2^{D_k}}{3n_0}.
\tag{3.5}
\]

Write

\[
\Delta U_k=U_{k+1}-U_k.
\]

Since

\[
\frac1{n_k}=\frac{3\Delta U_k}{U_k},
\qquad
\frac1{3n_k+1}=\frac{\Delta U_k}{U_{k+1}},
\]

we have the exact identity

\[
\boxed{
\varepsilon_k
=\frac{3(\Delta U_k)^2}{U_kU_{k+1}}.
}
\tag{3.6}
\]

Also (3.5) gives

\[
2^{D_s-D_i}=\frac{\Delta U_s}{\Delta U_i}.
\]

Thus the exact truncated version of (3.3) is

\[
\boxed{
R_+(N,t)
=
3\sum_{i=1}^{N+t-2}
\frac{\Delta U_i}{U_iU_{i+1}}
\left(
U_{b_i+1}-U_{a_i}
\right),
}
\tag{3.7}
\]

where

\[
a_i=\max(1,i-t+1),
\qquad
b_i=\min(i,N-1),
\]

with an empty inner interval contributing zero.  In particular, by monotonicity of \(U\),

\[
R_+(N,t)
\le
3\sum_{i=1}^{N+t-2}
\frac{\Delta U_i}{U_iU_{i+1}}
\bigl(U_{i+1}-U_{\max(1,i+1-t)}\bigr)
\tag{3.8}
\]

and hence

\[
R_+(N,t)
\le
3\sum_{i=1}^{N+t-2}
\frac{\Delta U_i}{U_i^2}
\bigl(U_{i+1}-U_{\max(1,i+1-t)}\bigr).
\tag{3.9}
\]

This reproduces the expected \(U\)-increment structure with all factors and indices explicit.

There is also an exact telescoping kernel

\[
\frac{\Delta U_i}{U_iU_{i+1}}
=\frac1{U_i}-\frac1{U_{i+1}}.
\tag{3.10}
\]

Pure monotonicity/Abel summation applied to (3.7) gives useful qualitative bounds, but by itself can retain an unwanted dependence on the long-range size of \(U\). The next section gives the required uniform-in-\(N\) estimate by exploiting injectivity.

---

# 4. Uniform composition-error theorem

The forward affine iteration has positive offset, so for \(s\le i\)

\[
n_i>Q_{s,i}n_s.
\tag{4.1}
\]

By (2.2), \(2^{a_i}\ge2\), and (4.1),

\[
Q_{s,i}\varepsilon_i
=
\frac{Q_{s,i}}{2^{a_i}n_in_{i+1}}
\le
\frac1{2n_sn_{i+1}}.
\tag{4.2}
\]

Hence, putting \(j=i+1\),

\[
R_+(N,t)
\le
\frac12
\sum_{\substack{1\le s<N,\ s<j\le N+t-1\\1\le j-s\le t}}
\frac1{n_sn_j}
\le
\frac12
\sum_{\substack{1\le s<j<N+t\\1\le j-s\le t}}
\frac1{n_sn_j}.
\tag{4.3}
\]

We now prove a purely combinatorial packing lemma.

### Lemma 4.1 — bounded-distance reciprocal pair graph

For any finite injective sequence of positive integers \(x_0,\ldots,x_{M-1}\) and any integer \(t\ge2\),

\[
\sum_{\substack{0\le i<j<M\\j-i\le t}}
\frac1{x_ix_j}
=O((\log(t+1))^2)
\tag{4.4}
\]

with an absolute constant.

### Proof

Set \(T=t^2\) and split vertices into

\[
S=\{i:x_i\le T\},
\qquad
L=\{i:x_i>T\}.
\]

The graph in (4.4) has undirected degree at most \(2t\).

**Small-small edges.** Ignoring the edge restriction only enlarges the sum:

\[
\sum_{SS}\frac1{x_ix_j}
\le
\frac12\left(\sum_{i\in S}\frac1{x_i}\right)^2.
\]

Injectivity gives

\[
\sum_{i\in S}\frac1{x_i}
\le\sum_{n\le T}\frac1n
\le1+\log T,
\]

so the small-small part is \(O((\log t)^2)\).

**Large-large edges.** Use

\[
\frac1{xy}\le\frac12\left(\frac1{x^2}+\frac1{y^2}\right).
\]

The degree bound and injectivity give

\[
\sum_{LL}\frac1{x_ix_j}
\le
 t\sum_{i\in L}\frac1{x_i^2}
\le
 t\sum_{n>T}\frac1{n^2}
=O(t/T)=O(1/t).
\]

**Small-large edges.** Fix a small vertex \(i\). It has at most \(2t\) large neighbors, and every large neighbor has value \(>T\). Therefore

\[
\sum_{j:\,ij\text{ cross edge}}\frac1{x_j}
\le\frac{2t}{T}.
\]

Summing over small vertices,

\[
\sum_{SL}\frac1{x_ix_j}
\le
\frac{2t}{T}\sum_{i\in S}\frac1{x_i}
=O\left(\frac{\log t}{t}\right).
\]

Adding the three pieces proves (4.4). ∎

Apply Lemma 4.1 to the finite injective sequence \(n_1,\ldots,n_{N+t-1}\) in (4.3). Therefore

\[
\boxed{
R_+(N,t)=O((\log(t+1))^2)
}
\tag{4.5}
\]

uniformly in \(N\), in the orbit, and in \(c\).

Together with the isolated initial reciprocal \(1/n_0\le1\), all reciprocal-composition losses are

\[
\boxed{O((\log(t+1))^2).}
\tag{4.6}
\]

The only remaining shifted-range issue is the terminal tail \(N\le k<N+t\) inside the bad-class contribution; it is handled explicitly in Section 5 rather than hidden in (4.6).

---

# 5. Canonical terminal classes and good/bad split

Set

\[
L=\lfloor ct\rfloor,
\qquad
Q_t=2\cdot3^{t+1}.
\tag{5.1}
\]

For each admissible terminal class \(y\pmod{Q_t}\), let \(\mu_t(y)\) be the minimum total valuation of an admissible length-\(t\) history ending in that class. Define

\[
w_t(y)=\frac{3^t}{2^{\mu_t(y)}}.
\tag{5.2}
\]

Let

\[
\mathcal G_t(c)=\{y:\mu_t(y)\le L\}
\]

be the good classes, and define the boundary quantity

\[
\boxed{
B_t(c)=\sum_{y\in\mathcal G_t(c)}\frac{w_t(y)}{r_y},
}
\tag{5.3}
\]

where \(r_y\) is the least genuinely reachable positive terminal defined and proved in Appendix B below.

For an actual block ending in terminal class \(y\), its total valuation is at least \(\mu_t(y)\). Therefore if \(y\notin\mathcal G_t(c)\), then its weight satisfies

\[
\frac{3^t}{2^{A_{k-t,t}}}
\le
\frac{3^t}{2^{L+1}}
=:\eta_t.
\tag{5.4}
\]

Thus

\[
\boxed{
\eta_t=2^{\alpha t-L-1}
\le2^{-(c-\alpha)t}.
}
\tag{5.5}
\]

Because the terminal indices in (2.7) run through \(t+1\le k<N+t\), the raw bad-class contribution is bounded first by

\[
\boxed{
\eta_t\sum_{k=t+1}^{N+t-1}\frac1{n_k}
\le \eta_t H_{N+t}.
}
\tag{5.6}
\]

This is the exact shifted index range; it is not replaced prematurely by \(\eta_t H_N\).  Now

\[
H_{N+t}
=
H_N+\sum_{N\le k<N+t}\frac1{n_k}.
\tag{5.7}
\]

The \(t\) tail values are distinct positive integers, so injectivity gives the uniform bound

\[
0\le H_{N+t}-H_N
\le \sum_{m=1}^{t}\frac1m
\le 1+\log(t+1).
\tag{5.8}
\]

Consequently

\[
\boxed{
\text{bad contribution}
\le
\eta_tH_N+O(\eta_t\log(t+1)).
}
\tag{5.9}
\]

Since \(L=\lfloor ct\rfloor\) and \(c>\alpha\), one has \(\lfloor ct\rfloor+1>ct>\alpha t\), hence \(0<\eta_t<1\) for every \(t\).  Thus the extra tail in (5.9) is already \(O(\log(t+1))\) with an absolute constant.  Moreover, for fixed \(c>\alpha\),

\[
\eta_t t
\le t\,2^{-(c-\alpha)t}\longrightarrow0,
\qquad
\eta_t\log(t+1)
\le2^{-(c-\alpha)t}\log(t+1)\longrightarrow0.
\tag{5.10}
\]

In particular the shifted bad-class tail costs no linear-in-\(t\) term on the coefficient-extraction schedule.

---

# 6. Arithmetic-progression packing for good terminal classes

For a fixed terminal class \(y\pmod{Q_t}\), all actual orbit terminals in that class are distinct positive elements of the progression

\[
r_y+qQ_t,\qquad q\ge0.
\]

The shifted terminal list in (2.7) contains exactly \(N-1\) entries, so there are at most \(N-1\) visits to any such progression. Therefore

\[
\sum_{\substack{t+1\le k<N+t\\n_k\equiv y\;(Q_t)}}\frac1{n_k}
\le
\frac1{r_y}+\sum_{q=1}^{N-1}\frac1{qQ_t}
\le
\frac1{r_y}+\frac{\log N+1}{Q_t}.
\tag{6.1}
\]

Multiplying by \(w_t(y)\) and summing over good classes gives

\[
\text{good contribution}
\le
B_t(c)
+\frac{\log N+1}{Q_t}
\sum_{y\in\mathcal G_t(c)}w_t(y).
\tag{6.2}
\]

It remains to bound the total good weight.

A positive length-\(t\) valuation word of total valuation \(A\) is a composition of \(A\) into \(t\) positive parts, hence there are

\[
\binom{A-1}{t-1}
\]

such words. Each word yields at most two terminal unit classes (the two initial unit residues modulo \(3\)). Therefore

\[
\#\{y:\mu_t(y)=A\}
\le2\binom{A-1}{t-1}.
\tag{6.3}
\]

Let \(G_1,\ldots,G_t\) be iid positive geometric variables with

\[
\Pr(G_j=a)=2^{-a},\qquad a\ge1,
\]

and put \(S_t=G_1+\cdots+G_t\). Then

\[
\Pr(S_t=A)=\binom{A-1}{t-1}2^{-A}.
\]

Define the exact finite lower-tail probability

\[
\boxed{
p_t(c)=\Pr(S_t\le L).
}
\tag{6.4}
\]

Using (6.3),

\[
\sum_{y\in\mathcal G_t(c)}w_t(y)
\le
2\,3^t
\sum_{A=t}^{L}\binom{A-1}{t-1}2^{-A}
=
2\,3^t p_t(c).
\tag{6.5}
\]

Since \(Q_t=2\cdot3^{t+1}\),

\[
\boxed{
\frac1{Q_t}\sum_{y\in\mathcal G_t(c)}w_t(y)
\le\frac{p_t(c)}3.
}
\tag{6.6}
\]

This is the exact origin of the \(1/3\) in the growing-depth master inequality. It is consistent with, but logically distinct from, the \(1/3\) unit-density factor in the later Stieltjes boundary ledger.

---

# 7. Master inequality

Combine:

- the exact unit-tail decomposition (2.7), including \(1/n_0\le1\);
- the composition-error bound (4.5);
- the exact shifted bad-class estimate (5.6)--(5.10);
- and the good-class packing (6.2), (6.6).

Before moving the bad term, the inequality has the explicit form

\[
H_N
\le
\frac{p_t(c)}3(\log N+1)
+B_t(c)
+\eta_tH_{N+t}
+C_0(1+\log^2(t+1)).
\tag{7.0}
\]

Using (5.7)--(5.9) gives

\[
H_N
\le
\frac{p_t(c)}3(\log N+1)
+B_t(c)
+\eta_tH_N
+C_1(1+\log^2(t+1)),
\]

because \(0<\eta_t<1\) and the extra \(O(\eta_t\log(t+1))\) term is absorbed into \(O(\log^2(t+1))\).  Therefore there is an absolute constant \(C\) such that, for all \(N>1\) and \(t\ge2\),

\[
\boxed{
(1-\eta_t)H_N
\le
\frac{p_t(c)}3(\log N+1)
+B_t(c)
+C(1+\log^2(t+1)).
}
\tag{7.1}
\]

Thus one may take

\[
\boxed{
E(N,t,c)=C(1+\log^2(t+1)).
}
\tag{7.2}
\]

The error is independent of \(N\) and \(c\), apart from the requirement that the canonical good/bad split be defined.

For fixed \(t\), (7.1) is the ordinary fixed-depth master inequality with an \(O_t(1)\) remainder. Thus the new theorem regresses correctly to the CP9 fixed-\(t\) statement.

---

# 8. Growing-depth asymptotics

The geometric moment generating function gives, for \(c\in(1,2)\),

\[
p_t(c)\le e^{-I(c)t},
\qquad
I(c)=c\log2-h(c)>0.
\tag{8.1}
\]

With the exact schedule (1.2),

\[
e^{-I(c)t}\log N
\le
(\log\log N)^{-2}.
\tag{8.2}
\]

Hence

\[
\frac{p_t(c)}3(\log N+1)=o(1)=o(t).
\tag{8.3}
\]

Also, from (5.5), with \(\kappa(c)=(c-\alpha)\log2>0\),

\[
\eta_t\le e^{-\kappa(c)t}\to0.
\tag{8.4}
\]

The index-shift repair has already produced the stronger pre-move form (7.0) with \(\eta_tH_{N+t}\).  By (5.8)--(5.10),

\[
\eta_t(H_{N+t}-H_N)
=O(\eta_t\log(t+1))=o(1)=o(t)
\]

for fixed \(c>\alpha\).  Hence moving only \(\eta_tH_N\) to the left in (7.1) is legitimate without presupposing any upper bound on \(H_N\). Eventually \(\eta_t<1/2\), so division by \(1-\eta_t\) changes any \(O(t)\) right side by a factor \(1+o(1)\). After (7.1) itself yields \(H_N=O(t)\), one may additionally note \(\eta_tH_N=o(t)\).

Finally,

\[
\frac{E(N,t,c)}t
=O\left(\frac{\log^2 t}{t}\right)
\to0.
\tag{8.5}
\]

Thus the audited growing-depth requirement is proved:

\[
\boxed{E(N,t,c)=o(t)}
\]

uniformly along the coefficient-extraction schedule for every fixed \(c>\alpha\).

---

# 9. The boundary quantity is the same canonical quantity used by the ledger

Equation (5.3) defines

\[
B_t(c)=\sum_{\mu_t(y)\le\lfloor ct\rfloor}\frac{w_t(y)}{r_y}.
\]

This is exactly the boundary term appearing in Section 6 of this standalone proof; no second object with the same notation is introduced.

Define

\[
b(c)=\limsup_{t\to\infty}\frac{B_t(c)}t.
\tag{9.1}
\]

Then tautologically, for each fixed \(c\) and every \(\varepsilon>0\),

\[
B_t(c)\le(b(c)+\varepsilon)t
\]

for all sufficiently large \(t\). The repaired Stieltjes ledger provides the theorem-level upper envelope for \(b(c)\).

---

# 10. Initial segment is harmless

No separate CP9 rate such as \(H_t=O((\log t)^{1-\delta})\) is required. Injectivity alone gives for any block of \(t\) orbit values

\[
\sum_{j=1}^{t}\frac1{2j-1}=O(\log t)=o(t).
\tag{10.1}
\]

This controls the initial/final segment loss in passing between \(H_N\) and the range on which the composed identity is summed.

---

# 11. Error-margin sanity

At \(c\downarrow\alpha\), CP17 gives

\[
K_{17}=2.7428814387659418633\ldots
\]

and

\[
I(\alpha)=0.05497947281081707167\ldots.
\]

An additional asymptotic boundary error \(e\,t\) would increase the final harmonic coefficient by \(e/I(\alpha)\). Therefore the exact available per-\(t\) error budget before reaching coefficient \(3\) is

\[
\boxed{
e_*=(3-K_{17})I(\alpha)
=0.01413624294652430366\ldots.
}
\tag{11.1}
\]

The theorem above is much stronger: its extra error satisfies

\[
E(N,t,c)/t\to0,
\]

so it consumes zero limiting budget.

---

# 12. Finite growing-depth stress test (non-proof)

A separate reproducibility script, `CP17_V3_GROWING_DEPTH_STRESS.py`, evaluates the exact composed reciprocal error on a long injective prefix of the odd-only orbit starting at \(670617279\). It tests depths of order \(\log\log N/I(c)\) and a deliberately faster \(2\times\) depth. The resulting file `CP17_V3_GROWING_DEPTH_STRESS.csv` gives, for example,

| N | c | t | composition error / t |
|---:|---:|---:|---:|
| 80 | 1.60 | 30 | \(1.42\times10^{-17}\) |
| 180 | 1.60 | 33 | \(1.31\times10^{-17}\) |
| 350 | 1.60 | 35 | \(1.46\times10^{-8}\) |
| 350 | 1.60 | 70 | \(1.25\times10^{-10}\) |

These values are not used in the proof. Their only role is to stress the indexing/factor conventions in (2.5), (3.3), and (4.3); no contradiction with the uniform \(O(\log^2 t)\) theorem appears.

---

# 13. Verdict

1. standalone master inequality (7.1): `[PROVED]`;
2. growing-\(t\) quantifiers and schedule: `[PROVED]`;
3. exact accumulated-error formula in \(D\)-notation: `[PROVED]`;
4. exact \(U\)-increment identity: `[PROVED]`;
5. uniform composition error \(O(\log^2t)\): `[PROVED]`;
6. explicit \(n_0\) exception and shifted terminal-tail control: `[PROVED]`;
7. \(\eta_t\) control: `[PROVED]`;
8. same canonical \(B_t(c)\) as ledger: `[PROVED]`;
9. fixed-\(t\) regression: `[PROVED]`.

No load-bearing growing-depth error remains in this bridge.


---

# 12. V3.1 formal-patch verification

The two audit repairs are explicit in the proof, not merely stated in prose:

1. **Initial exception.** Equation (1.0a) writes
   \[
   H_N=1/n_0+\sum_{1\le s<N}1/n_s,
   \]
   and every canonical block begins at \(s\ge1\).  Equation (1.0) proves \(3\nmid n_k\) for every \(k\ge1\), so the complete block decomposition lies in the unit domain.  The term \(1/n_0\le1\) is absorbed only after it has been displayed.

2. **Bad-class shifted range.** Equation (2.9) gives the exact terminal range \(t+1\le k<N+t\); equation (5.6) therefore bounds the raw bad term by \(\eta_tH_{N+t}\).  Equations (5.7)--(5.10) control the extra \(N\le k<N+t\) tail and prove both \(\eta_t t\to0\) and \(\eta_t\log t\to0\) for the exact growing-depth schedule.  Only then is \(\eta_tH_N\) moved to the left in Section 7.

Neither repair changes \(p_t(c)/3\), \(B_t(c)\), the composition estimate \(O(\log^2t)\), or the depth normalization \(t/\log\log N\to1/I(c)\).


---

# Appendix B — Complete reachable-terminal proof

# CP17-V3 — Reachable terminal and canonical reconstruction lemma

**Status:** `[PROVED]`.

This note fixes the terminal-representative ambiguity needed by the growing-depth master inequality. No generic least residue is silently substituted for a genuinely reachable terminal value.

## 1. Odd-only words and affine identity

Let

\[
T(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers. A length-\(t\) valuation word is

\[
\mathbf a=(a_0,\ldots,a_{t-1}),\qquad a_j\ge1.
\]

Put

\[
A_j=\sum_{h<j}a_h,\qquad A=A_t,
\]

and

\[
B_{\mathbf a}=\sum_{j=0}^{t-1}3^{t-1-j}2^{A_j}>0.
\]

Exact iteration gives

\[
\boxed{2^A n_t=3^t n_0+B_{\mathbf a}.}
\tag{1.1}
\]

Throughout the canonical decomposition, starts and terminals are positive odd integers coprime to \(3\).

## 2. Terminal classes

Set

\[
Q_t=2\cdot3^{t+1}.
\]

For a fixed valuation word \(\mathbf a\), call a positive terminal \(Y\) **genuinely admissible** if the successive inverse steps

\[
x_j=\frac{2^{a_j}x_{j+1}-1}{3},\qquad j=t-1,\ldots,0,
\]

with \(x_t=Y\), are all positive odd integers coprime to \(3\). This is an operational definition; no congruence criterion is assumed in advance.

Suppose \(Y,Y'\) are two genuinely admissible terminals for the same word and their corresponding initial starts satisfy

\[
x_0\equiv x'_0\pmod3.
\]

Subtracting the affine identities (1.1) gives

\[
2^A(Y-Y')=3^t(x_0-x'_0).
\]

Since \(x_0-x'_0\) is divisible by \(3\) and \(2^A\) is a unit modulo powers of \(3\),

\[
3^{t+1}\mid(Y-Y').
\]

Both terminals are odd, so also \(2\mid(Y-Y')\). Hence

\[
\boxed{Y\equiv Y'\pmod{Q_t}.}
\tag{2.1}
\]

There are only two possible initial unit residues modulo \(3\), namely \(1\) and \(2\). Therefore a fixed valuation word produces at most two terminal classes modulo \(Q_t\). We call any class containing at least one genuinely admissible terminal an **admissible terminal class for the word**.

## 3. Every positive representative of an admissible class is reachable

### Lemma 3.1

If a class \(y\pmod{Q_t}\) contains one genuinely admissible terminal for \(\mathbf a\), then every positive integer \(Y\equiv y\pmod{Q_t}\) is the terminal value of a positive unit length-\(t\) past with the same valuation word \(\mathbf a\).

### Proof

Let \(Y_0\) be one genuinely admissible terminal in the class and write

\[
Y-Y_0=qQ_t=2q3^{t+1}.
\]

Run the inverse recurrence simultaneously from \(Y\) and \(Y_0\). After the last inverse step the difference of the predecessors is

\[
\frac{2^{a_{t-1}}(Y-Y_0)}3
=2^{a_{t-1}+1}q3^t,
\]

which is divisible by \(2\cdot3^t\). After the next inverse step the difference is divisible by \(2\cdot3^{t-1}\), and so on. Inductively, at every inverse level the new predecessor for \(Y\) is an integer having the same parity and the same residue modulo \(3\) as the corresponding genuinely admissible predecessor for \(Y_0\). Thus it is odd and coprime to \(3\).

Positivity does not require comparison with \(Y_0\). At each inverse step the current terminal is a positive integer and \(a_j\ge1\), so

\[
2^{a_j}x_{j+1}-1\ge1,
\]

hence the integral predecessor is positive.

Finally, because each reconstructed successor \(x_{j+1}\) is odd,

\[
3x_j+1=2^{a_j}x_{j+1}
\]

has exact \(2\)-adic valuation \(a_j\). Therefore the reconstructed past is genuinely admissible and has valuation word \(\mathbf a\). ∎

## 4. Least reachable terminal

For an admissible terminal class \(y\pmod{Q_t}\), define

\[
\mathcal R_t(y)=\{Y>0:Y\equiv y\pmod{Q_t},\ Y\text{ is reached by an admissible length-}t\text{ past}\}.
\]

This set is nonempty. By well-ordering it has a minimum:

\[
\boxed{r_y:=\min\mathcal R_t(y).}
\tag{4.1}
\]

Lemma 3.1 shows more: once the class is admissible, every positive representative is reachable. Therefore

\[
\boxed{r_y=\text{the least positive representative of the admissible class }y\pmod{Q_t}.}
\tag{4.2}
\]

Equation (4.2) is a theorem following from reachability; it is not used as the definition.

## 5. Minimum total valuation is attained at \(r_y\)

Let

\[
\mu_t(y)=\min\left\{\sum_{j=0}^{t-1}a_j:\mathbf a\text{ is admissible for terminal class }y\right\}.
\tag{5.1}
\]

The minimum exists because the set is a nonempty subset of the positive integers and every word has total valuation at least \(t\).

Choose a word \(\mathbf a\) with total valuation \(A=\mu_t(y)\). By Lemma 3.1, this same word reaches the least reachable terminal \(r_y\). Hence:

\[
\boxed{r_y\text{ is realized by a minimum-total-valuation history}.}
\tag{5.2}
\]

This closes the distinction requested by the audit: a higher-valuation history is not needed to reach the least terminal.

## 6. Canonical reconstruction \(\xi_t(y)\)

There may be several minimum-total-valuation words for the same terminal class. For each such word, invert from \(r_y\) and obtain its positive unit start. Define

\[
\boxed{
\xi_t(y)=\min\{x_0:\ x_0\text{ is obtained from }r_y\text{ by a word of total valuation }\mu_t(y)\}.
}
\tag{6.1}
\]

Then:

1. the set in (6.1) is nonempty by (5.2);
2. \(\xi_t(y)\in\mathbb Z_{>0}\) by the inverse construction;
3. \(\xi_t(y)\) is odd;
4. \(3\nmid\xi_t(y)\);
5. therefore
   \[
   \boxed{\gcd(\xi_t(y),6)=1.}
   \tag{6.2}
   \]

Different terminal classes have different canonical starts. Indeed a positive start has one deterministic first \(t\) valuation history and one deterministic terminal class, so the same start cannot reconstruct two distinct terminal classes.

## 7. Boundary inequality

Let \(\mathbf a_y\) be a minimum-total-valuation word realizing \(\xi_t(y)\). Its affine identity is

\[
2^{\mu_t(y)}r_y=3^t\xi_t(y)+B_y,
\qquad B_y=B_{\mathbf a_y}>0.
\tag{7.1}
\]

Define

\[
w_t(y)=\frac{3^t}{2^{\mu_t(y)}}.
\]

Then

\[
\frac{w_t(y)}{r_y}
=\frac{3^t}{2^{\mu_t(y)}r_y}
=\frac{1}{\xi_t(y)+B_y/3^t}
<\frac1{\xi_t(y)}.
\]

Thus the exact canonical inequality is

\[
\boxed{
\frac{w_t(y)}{r_y}<\frac1{\xi_t(y)}.
}
\tag{7.2}
\]

No least-residue/reachable-terminal ambiguity remains.

## 8. Status

- existence of \(r_y\): `[PROVED]`;
- minimum-valuation realization of \(r_y\): `[PROVED]`;
- positivity/integrality/unit property of \(\xi_t(y)\): `[PROVED]`;
- distinctness across terminal classes: `[PROVED]`;
- boundary inequality (7.2): `[PROVED]`.


---

# Appendix C — Complete Syracuse polynomial-energy proof

# CP17-REPAIR — Self-contained Syracuse polynomial collision-energy theorem

**Status:** `[PROVED]`.

This version removes the external injectivity dependency. The proof is fully self-contained at the structural step previously attributed to Tao's Lemma 6.2.

## 1. Statement

Let \(A_1,\dots,A_n\) be iid positive geometric random variables

\[
\Pr(A_i=a)=2^{-a},\qquad a\ge1,
\]

with partial sums \(S_j=A_1+\cdots+A_j\). Define

\[
X_n=\sum_{j=1}^n3^{j-1}2^{-S_j}\pmod{3^n},
\qquad p_n(y)=\Pr(X_n=y),
\]

and

\[
\chi_n^{\rm Syr}=3^n\sum_{y\bmod3^n}p_n(y)^2.
\]

Then there is an absolute constant \(C\) such that

\[
\boxed{\chi_n^{\rm Syr}\le Cn^4.}
\]

More explicitly, with

\[
J_n=(4n+1)\left(\left\lfloor n\log_2\frac32\right\rfloor+1\right),
\]

\[
B_n=1+\frac{2n}{3}\left(1+n\log\frac32\right),
\]

and

\[
\eta=3\left(\frac{3125}{8192}\right)^2
=\frac{29296875}{67108864}<1,
\]

one has

\[
\boxed{
\chi_n^{\rm Syr}
\le
\left(\sqrt{J_nB_n}+\eta^{n/2}\right)^2.
}
\]

Hence \(\log\chi_n^{\rm Syr}=o(n)\).

---

## 2. Self-contained injectivity of the offset map

For a positive gap tuple \(a=(a_1,\dots,a_n)\), put

\[
S_j=a_1+\cdots+a_j,
\qquad
G_n(a)=\sum_{j=1}^n3^{j-1}2^{-S_j}\in\mathbb Q.
\]

### Lemma 2.1 — injectivity

The map \(G_n:(\mathbb N_{\ge1})^n\to\mathbb Q\) is injective.

### Proof

Use the ordinary \(2\)-adic valuation \(v_2\) on nonzero rationals. Since

\[
S_1<S_2<\cdots<S_n,
\]

the terms of \(G_n(a)\) have pairwise distinct \(2\)-adic valuations

\[
v_2\!\left(3^{j-1}2^{-S_j}\right)=-S_j.
\]

The unique smallest valuation is therefore \(-S_n\), attained by the last term. For a finite sum with a unique term of minimal \(2\)-adic valuation, the valuation of the sum equals that minimum. Hence

\[
v_2(G_n(a))=-S_n.
\]

Thus \(G_n(a)\) determines \(S_n\). It then determines

\[
G_n(a)-3^{n-1}2^{-S_n}
=G_{n-1}(a_1,\dots,a_{n-1}).
\]

Applying the same argument recursively recovers

\[
S_{n-1},S_{n-2},\dots,S_1.
\]

Finally

\[
a_1=S_1,\qquad a_j=S_j-S_{j-1}\quad(j\ge2),
\]

so the entire tuple is recovered uniquely. ∎

This proof removes the former Tao-Lemma dependency.

---

## 3. Integer encoding at fixed total gap

Fix \(l=S_n\). Define

\[
I(a)=2^lG_n(a)
=\sum_{j=1}^n3^{j-1}2^{l-S_j}.
\]

Every term is a positive integer, so \(I(a)\in\mathbb N\). By Lemma 2.1, for fixed \(l\), distinct tuples have distinct \(I(a)\).

---

## 4. Critical martingale

Define

\[
W_j=3^j2^{-S_j},\qquad W_0=1,
\]

and

\[
R_n=\max_{0\le j\le n}W_j.
\]

Since

\[
\mathbb E(3\,2^{-A_i})
=3\sum_{a\ge1}4^{-a}=1,
\]

\((W_j)\) is a nonnegative martingale. Also \(A_i\ge1\), hence

\[
W_j\le(3/2)^j,
\qquad R_n\le(3/2)^n.
\]

Doob's weak \(L^1\) maximal inequality gives

\[
\Pr(R_n\ge t)\le t^{-1}\qquad(t\ge1).
\]

Therefore

\[
\mathbb ER_n
\le1+\int_1^{(3/2)^n}\frac{dt}{t}
=1+n\log\frac32.
\tag{4.1}
\]

---

## 5. Dyadic martingale classes and residue multiplicity

For \(h\ge0\), let

\[
\mathcal T_{l,h}
=
\{a:S_n=l,\ 2^h\le R_n<2^{h+1}\}.
\]

Write

\[
N_{l,h}=|\mathcal T_{l,h}|,
\qquad
P_{l,h}=N_{l,h}2^{-l}.
\]

For \(a\in\mathcal T_{l,h}\),

\[
I(a)=\frac{2^l}{3}\sum_{j=1}^nW_j
<\frac{2^ln}{3}2^{h+1}.
\tag{5.1}
\]

The \(I(a)\) are distinct positive integers. Hence after reduction modulo \(3^n\), a fixed residue can occur at most

\[
1+\frac{2^ln2^{h+1}}{3^{n+1}}
\tag{5.2}
\]

times: distinct representatives of the same residue differ by at least \(3^n\).

Let \(p_{l,h}\) be the sub-probability distribution modulo \(3^n\) contributed by this class. Each tuple has mass \(2^{-l}\). From (5.2),

\[
3^n\|p_{l,h}\|_2^2
\le
3^n4^{-l}N_{l,h}
+\frac{2n}{3}2^hP_{l,h}.
\tag{5.3}
\]

---

## 6. Sum of class energies

Summing the first term in (5.3) over all tuples,

\[
3^n\sum_a4^{-S_n(a)}
=3^n\left(\sum_{a\ge1}4^{-a}\right)^n
=1.
\]

For the second term,

\[
\sum_{l,h}2^hP_{l,h}\le\mathbb ER_n.
\]

Using (4.1),

\[
\boxed{
\sum_{l,h}3^n\|p_{l,h}\|_2^2
\le
1+\frac{2n}{3}\left(1+n\log\frac32\right)
=B_n.
}
\tag{6.1}
\]

---

## 7. Good total-gap range and cross-class terms

Call a tuple good if \(S_n\le5n\). Then \(n\le l\le5n\), so there are at most \(4n+1\) possible total gaps. Also \(R_n\le(3/2)^n\), so the dyadic index has at most

\[
\left\lfloor n\log_2\frac32\right\rfloor+1
\]

values. Thus at most \(J_n\) good classes occur.

If \(p_{\rm good}\) is their sum, Minkowski and Cauchy-Schwarz give

\[
\sqrt{3^n}\|p_{\rm good}\|_2
\le
\sum_{(l,h)\rm\ good}\sqrt{3^n}\|p_{l,h}\|_2
\le
\sqrt{J_nB_n}.
\]

Hence

\[
3^n\|p_{\rm good}\|_2^2\le J_nB_n.
\tag{7.1}
\]

---

## 8. Large-total-gap tail

Let \(\beta_n=\Pr(S_n>5n)\). With \(x=8/5\),

\[
\mathbb E x^A=\frac{x}{2-x}=4,
\]

so Markov gives

\[
\beta_n
\le
\frac{4^n}{(8/5)^{5n}}
=
\left(\frac{3125}{8192}\right)^n.
\]

For the corresponding sub-probability \(p_{\rm bad}\),

\[
\|p_{\rm bad}\|_2\le\|p_{\rm bad}\|_1=\beta_n,
\]

and therefore

\[
3^n\|p_{\rm bad}\|_2^2\le\eta^n.
\tag{8.1}
\]

---

## 9. Completion

Since \(p_n=p_{\rm good}+p_{\rm bad}\), Minkowski, (7.1) and (8.1) yield

\[
\sqrt{\chi_n^{\rm Syr}}
\le
\sqrt{J_nB_n}+\eta^{n/2}.
\]

Since \(J_n=O(n^2)\) and \(B_n=O(n^2)\),

\[
\boxed{\chi_n^{\rm Syr}=O(n^4).}
\]

---

## 10. Fixed-shift autocorrelations

For every affine permutation

\[
A_k(z)=4^kz+\frac{4^k-1}{3}\pmod{3^n},
\]

Cauchy-Schwarz gives

\[
C_n(k)
=3^n\sum_zp_n(z)p_n(A_kz)
\le\chi_n^{\rm Syr}.
\]

Thus every fixed \(k\), in particular \(k=1,2,3\), satisfies

\[
C_n(k)=O(n^4)=e^{o(n)}.
\]

---

## 11. Reproducibility note

The analytic proof does not depend on finite enumeration. A separate exact helper in the repaired package checks the classwise injectivity/range/multiplicity inequalities exhaustively for

\[
\boxed{n\le6,\quad S_n\le5n.}
\]

The earlier package said \(n\le5\); the repaired package records the actually rerun \(n\le6\) check.
