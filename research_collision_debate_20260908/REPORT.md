# Adversarial collision review and a dual interval reduction

2026-09-08. Principal plus two independent adversarial agents. This report supersedes any suggestion that the local-transfer lemma alone controls general collisions. It does not supersede the valid single-transfer formula. No new orbit exclusion or paid calls.

## Objections that survived review

The attack agent found genuine positive trajectories with different words, equal r=7,A=11, and the same small odd endpoint161:

    145 ->109 ->41 ->31 ->47 ->71 ->107 ->161
    147 ->221 ->83 ->125 ->47 ->71 ->107 ->161

The valuation words are (2,3,2,1,1,1,1) and (1,3,1,3,1,1,1). Their B values are12613 and8239, differing by2*3^7. Since161<floor(2^(1.2*7))=337, small endpoints do not forbid coordinated collisions. They merge at47. Removing the common suffix just moves the unknown multiplicity to the merge point; it does not supply a new saving.

An infinite family (r>=4) is

    w=(2,3,1^(r-4),2,1), z=(1,3,1^(r-3),3).

Both have total r+4 and B(w)-B(z)=2*3^r, with B(z)=21*3^(r-2)-2^(r+2). Add d=floor(alpha*r)-r-4 to both final entries when d>=0 (r>=7) to reach the critical band without changing B. The last entries still differ. Therefore arbitrary collision differences are not confined to O(log r) early positions. This family alone does not guarantee small endpoints; its endpoint is at least exponential in r with exponent1 under this adjustment.

## Positivity is automatic; endpoint parity is not

For every positive word and canonical residue n=M(w), n is a unit modulo3, so n>=1. The congruence 2^A n=B mod3^r permits backward reconstruction y=(2^a_r n-1)/3, then the same construction for the preceding word. Inductively all predecessors are positive odd integers: the numerator is positive, odd, and divisible by3. Thus

    x=(2^A n-B)/3^r

is a positive odd integer less than2^A. Requiring x>0 removes NO words. The principal proposed this as a possible filter; the audit agent disproved its usefulness.

If n is odd, all r valuations are exact. If n is even, only the first r-1 are exact and the last prescribed division count is truncated. Calling every canonical word a genuine length-r odd-only itinerary is incorrect. The earlier endpoint177146 witness is even. The relaxed count Q remains a valid upper count for the orbit bridge because genuine odd endpoints are a subset.

For fixed r,A different words give different starts x: the first r-1 exact valuations are determined by x, and their sum plus the fixed A determines the last prescribed valuation. Distinct starts may still share endpoint, as145 and147 demonstrate.

## Exact noncircular description of the start set

Let S_(r,A) contain the odd integers 1<=x<2^A whose actual cumulative odd-only valuations obey

    S_(r-1)(x)<A<=S_r(x).

Equivalently, iterate H(x)=x/2 for even x and H(x)=(3x+1)/2 for odd x. Among H^t(x), t=0,...,A-1, precisely r states are odd. This is a fixed-length parity-weight event, not the exact equality S_r=A.

The canonical starts above are exactly this set. One direction follows from backward reconstruction. Conversely each such start prescribes a unique word with final entry A-S_(r-1). The word imposes a unique residue class modulo2^A; the start and canonical start are both its representatives in [1,2^A), so they coincide. The class uniqueness also follows directly from 3^r x+B divisible2^A, since3 is invertible modulo2^A.

In particular |S_(r,A)|=binom(A-1,r-1). This is the familiar full-period parity coding count; no novelty is claimed for the coding.

## Dual interval sandwich with controlled boundary error

Define q=3^r, c=2^A/q, F(T)=#{x in S_(r,A):x<T}, X=cL. Positivity of each a_i implies A-S_l>=r-l, hence

    B/2^A <= sum_(l=0..r-1)3^(r-1-l)2^(-(r-l))=(3/2)^r-1.

Therefore 0<B/q<=D=2^(A-r)-c. Since n<L iff x<X-B/q,

    F(X-D) <= Q_(r,A)(L) <= F(X),
    0<=F(X)-Q_(r,A)(L)<=ceil(D/2)+1.

The last bound uses distinct odd starts; it does not assume equidistribution.

For A=alpha*r+O(1), alpha=log_2 3, and L=2^(br+o(r)), the error is at most2^((alpha-1)r+O(1)). Thus an upper bound with exponent gamma>alpha-1 for Q is equivalent to the same upper exponent for F(cL), uniformly in every fixed critical mass band. In particular the ideal target gamma=h*+b-alpha is above the error exponent when

    b>2alpha-1-h* = approximately0.6642811135.

This includes b=1.2 and the previously permitted small positive exponent loss. The reduction is an exact interface with a negligible boundary error in that regime; it is NOT an achieved distribution estimate.

## Why the new formulation is still difficult

The full odd period contains2^(A-1) starts and binom(A-1,r-1) selected starts. The target asks for the corresponding rare parity weight among only the initial interval of length X=Theta(2^(br)), exponentially shorter than the full period when b<alpha. Full-period bijectivity does not establish that restriction is representative. Distinctness alone gives F<=X/2+O(1), exponentb, missing the desired saving alpha-h* approximately0.0793186. The attack agent explicitly rejected interpreting the reduction as a saved exponent.

The next well-defined question is a short-initial-interval large-deviation bound for the parity weight of H at depth A. Any proposed theorem must handle this interval length versus coding depth, rather than assuming independent parity bits for a fixed small-integer sample. Merely changing from3-adic to2-adic coordinates does not resolve the dependence.

## A deterministic baseline obtained in the final adversarial exchange

The audit agent objected that the parity reformulation DOES yield a small unconditional improvement over the trivial exponent. Put m=ceil(log_2 X), with m<=A. Cover all x<X by the full residue interval [0,2^m). The first m shortcut parities uniquely encode this interval; for odd starts the first bit is1. If total A-step parity weight is r, the first m bits must contain at least K=r-(A-m) ones, since the remaining A-m steps contribute at most A-m. Hence

    F(X)<=sum_(k=max(1,K)..min(r,m)) binom(m-1,k-1).

This bound uses no random-parity assumption on the incomplete interval: it enlarges that interval to a complete period only at the shorter depth m.

For critical A and X=2^(br+o(r)), write beta=alpha-1. When 2beta<b<alpha, the binomial tail gives exponent f(b)=b H_2(beta/b); for b<=2beta the available bound is exponent b. At b=1.2,

    f=1.199456224042059,
    saving b-f=0.0005437759579409729.

The ideal target at this b is approximately1.1206813872. The valid saving is far too small. Using only this baseline in the existing count-to-orbit bridge gives kappa<b/f(b); maximizing over b<alpha approaches alpha/h*=1.0526808586. Thus it reproduces the previously documented ceiling and does not reach kappa1.053. This is a valid general bound derived through the new interface, not new progress beyond the project's previous asymptotic reach.

## Exact verification and review record

check_dual.py enumerates words and independently iterates EVERY positive odd start below2^A for three cases. It checks canonical positivity, injectivity, set equality, the B bound, and the interval sandwich. All pass:

|r,A,L|Q|odd-endpoint subset|F(X-D)|F(X)|
|---|---|---|---|---|
|7,11,337|33|22|31|34|
|10,15,256|10|7|7|10|
|10,15,4096|140|69|138|140|

The odd subset is reported to demonstrate the parity distinction, not as an asymptotic half-factor claim. The attack agent's r5..14 bounded scan and infinite-family proof are in agent_attack_report.md and its script/JSON. The audit agent independently checked the backward induction and dual reduction; the principal corrected the attack agent's initial exact-total interpretation to the crossing event. Both agents agree that no count exponent has improved. Canonical/frozen files remain unchanged; this package is local.
