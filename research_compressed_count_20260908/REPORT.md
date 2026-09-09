# Compressed endpoint counting: two distinct obstructions and an exact quotient

2026-09-08. Exploratory exact arithmetic, 48 finite parameter cases and adversarial mathematical checking. This is a test of specific compression templates, not a general impossibility theorem or a Collatz theorem. No paid calls or canonical file changes.

## 1. Target and notation

The actual event is M_r(w)<L for positive r-part compositions w of total A. q=3^r, N=binom(A-1,r-1), and Q is the exact successful-word count. The relevant asymptotic target requires Q/N<=2^(-delta*r+o(r)) for a positive delta=alpha-b-lambda. Merely obtaining an upper bound a little below N is insufficient.

The prefix numerator evolves B_(j+1)=3B_j+2^a where a is the current prefix mass. The earlier count-certificate formulation used (j,a,B_j modq).

## 2. Exact future-equivalence quotient

With k=r-j steps remaining and a fixed suffix u,

    B_r=3^k B_j+2^a B(u).

Thus B_j only matters modulo3^j for the final residue modulo3^r. At depth j, the exact state (j,a,c=B_j mod3^j) suffices; its transition is c'=(3c+2^a) mod3^(j+1). Every common suffix gives the same endpoint from equivalent prefix states.

This is an exact arithmetic quotient, not an approximate distributional claim. It is a direct consequence of the affine block identity, related to the already recorded suffix/conductor structure; no novelty claim is made. It removes unnecessary early precision but still reaches full modulus at the terminal depth. It does not provide a small asymptotic state space or a new count bound.

## 3. Fixed low-digit model: exact blindness threshold

Retain only c=B_j mod3^t and use terminal cost

    g_t(c)=1 iff some x in [0,L) satisfies x=2^(-A)c mod3^t.

If L>=3^t, every residue class intersects the interval, so g_t is identically1. Backward counting gives exactly N at the root. Every supersolution of this ambient terminal majorant has root at least N.

If L<3^t, precisely L ambient classes are accepted. Thus the sharp threshold for even distinguishing success from failure is 3^t>L. For L=2^(br+o(r)), one needs t of order (b/alpha)r. This is not sufficient for a useful bound and not a state-complexity lower bound for arbitrary symbolic or reachability-sensitive methods.

An adaptive schedule t_j=max(0,t-r+j) is exact for this projected terminal event, but cannot repair its terminal blindness.

## 4. High-digit bucket model and sound Bellman upper bound

Normalize the state as x=2^(-A)B_j modq. Its transition is

    x'=(3x+c_a) modq, c_a=2^(a-A) modq.

Fix 1<=t<r, H=3^t buckets, and W=q/H. Bucket b represents all integers [bW,(b+1)W). Let S(a,b) be the EXACT set of successor buckets for its integer representatives. Define

    F(r,A,b)=1_(bW<L),
    F(j,a,b)=sum_(feasible m) max_(b' in S(a,b)) F(j+1,a+m,b').

The root's first transition from x=0 is kept exact, giving x_1=2^(-A) modq; the root bound is sum_m F(1,m,bucket(x_1)).

Soundness: every concrete child lies in S(a,b); each child's true count is bounded by the maximum displayed above. Sum over the feasible next letters and induct backward. The terminal bucket-intersection predicate majorizes the exact event. Hence Q<=F_root<=N.

### A real quantifier error caught during debate

One reviewer initially argued this model always returns N because every fixed full word has some abstract path ending in bucket0. The principal objected: this chooses bucket representatives with knowledge of ALL future letters. In the sum/max Bellman recurrence a choice at one level cannot be separately optimized for every later word. These are different quantifier orders.

Independent counterexamples, with r=4,t=3,q=81,W=3,L=9:

| A | Exact Q | Bellman upper F | Total N |
|---:|---:|---:|---:|
| 6 | 0 | 9 | 10 |
| 7 | 3 | 17 | 20 |

The reviewer independently reproduced these using explicit enumeration of EVERY integer representative in a bucket, separately from the principal's interval-arithmetic successor calculation. The universal Bellman-collapse claim was retracted. It is not a result of this report.

The spurious-path diagnosis itself remains valid: r=2,A=3,q=9,t=1,L=3, word(1,2) has exact normalized path 0->8->4. After the first step, replacing8 by7 inside bucket[6,9) creates 7->1, an artificial success. Exact propagation of initial uncertainty would eventually erase it because3^r=0 modq; repeated projection instead reinjects incompatible representatives.

## 5. Corrected obstruction: a randomized-policy floor

The correct general statement is a LOWER bound on this UPPER-bound algorithm, not exact equality with N:

    F_root/N >= ceil(L/W)/H >= 3^(-t),
    for 1<=t<=r-1 and 1<=L<=q.

Proof. Write c_a=d_a W+e_a, 0<=e_a<W. For x=bW+u, 0<=u<W,

    next bucket=(3b+d_a+floor((3u+e_a)/W)) modH.

Since W>=3 is a power of3, the floor term attains each of0,1,2 as u ranges over integer representatives. Thus choosing any successor 3b+d_a+v modH with v in{0,1,2} is legal.

Use a randomized admissible policy choosing independent uniform v's. Draw the letters from the exact uniform-composition bridge; their distribution depends on remaining length and mass, NOT on the bucket or the v's. Condition on the full valuation word: the offsets d_a are fixed. In the final t transitions, the sum of independent ternary digits with weights1,3,...,3^(t-1) is uniform modulo H; all earlier bucket information vanishes modulo H. Therefore the final bucket is uniform, and it hits the ceil(L/W) accepted buckets with probability ceil(L/W)/H. There are r-1>=t abstract transitions after the exact first step.

After dividing each F state by its remaining composition count, the Bellman recursion is the optimal value over such admissible bucket choices under the exact composition bridge. Its max is at least the average for the legal randomized policy. Multiplying by N proves the floor. No future-dependent control choice is used.

The deterministic reviewer independently audited this corrected proof and returned PASS, specifically checking control/word independence, integer representatives, exact-first-step timing, and the sum/max quantifiers.

Consequences: fixed t, or even t=o(r), cannot give the required exponential decrease for this template. For a target exponent delta>0, a necessary condition is asymptotically alpha*t>=delta*r-o(r). This does NOT prove that linearly growing t succeeds, or rule out richer relational states, symbolic compression, or exact carry information. It is a precision barrier for this explicitly defined bucket relaxation.

## 6. Bounded experiment and actual gain

check_models.py used r=3..10, A=floor(alpha*r)+d for d=-1,0,1, b=.8 or1.2, L=floor(2^(br)). All 48 exact counts were checked by independent positive-composition enumeration with the closed affine numerator formula. 138 bucket bounds were computed for t=1,2,3 where t<r. At r<=5, the full-precision t=r variant also matched exact Q.

All Q<=F<=N checks passed. 32 of 138 bucket bounds improved strictly on N; in this panel all such improvements used t=3. The randomized-policy floor was checked in every row as an exact integer inequality. No asymptotic fit was made.

Illustration at r=10,A=15,b=.8,L=256: N=2002, actual Q=10, but the t=3 bucket bound is1827. The model retains a little discrimination while losing most of the required information. This is a poor bound, not evidence of useful exponential decay.

## Decision

Do not scale up fixed low-digit or fixed high-digit models expecting the missing exponent to appear. Their limitations are now explicit. Preserve the exact depth-dependent quotient for any later computation. A further candidate must retain an actual relation between interval location, low digits/carry, and remaining mass; it should first be tested on the explicit spurious splice and against the quantitative floor above.

This turn produced no new endpoint decay theorem and no new exclusion of actual Collatz trajectories. It did establish why two natural compressed certificate designs fail to supply the required scale, while correcting an overstrong negative assertion. The count-to-orbit proposition and the sparse-exception spectral proposition remain conditional and unchanged.
