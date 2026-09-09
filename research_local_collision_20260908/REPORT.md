# Exact local collision obstruction for valuation words

2026-09-08. Elementary arithmetic deductions and bounded exact checks. No novelty claim, global fiber estimate, or new orbit exclusion.

For a positive valuation word w=(a_1,...,a_r) of total A write S_l=a_1+...+a_l, S_0=0 and

    B(w)=sum_(l=0..r-1) 3^(r-1-l) 2^S_l,
    M(w)=2^(-A) B(w) mod 3^r.

## Single adjacent transfer: exact characterization

Replace (a_i,a_(i+1)) by (a_i+d,a_(i+1)-d), with one-based i in [1,r-1], positive integer d<a_(i+1). Total A is unchanged. Only S_i changes. Therefore

    B(w')-B(w)=3^(r-i-1) 2^S_i (2^d-1).

For odd d the 3-adic valuation of 2^d-1 is zero. For even d=2e, the elementary lifting identity v_3(4^e-1)=1+v_3(e) follows by factoring out the part of e coprime to 3 and repeatedly cubing. Thus

    M(w')=M(w) iff 2*3^i divides d.

The same divisibility uses |d| for negative transfers. This is an iff for ONE adjacent transfer, not for arbitrary word pairs.

Positivity imposes |d|<=A-r. A nontrivial such collision at position i therefore requires 2*3^i<=A-r. In the critical band A=alpha*r+O(1), local residue-preserving transfers are restricted to i<=log_3((A-r)/2)=O(log r). Later positions cannot support a single such transfer. This does not show colliding arbitrary words agree outside their first O(log r) positions: a connecting sequence could pass through different endpoint residues.

## Exact integer numerators are injective at fixed length and mass

If two distinct words of fixed r,A first differ at position i, then i<=r-1. In B(w')-B(w), the first nonzero term has 2-adic valuation min(S_i,S_i'). All later terms have strictly larger 2-adic valuations, because both cumulative sums strictly increase. The first term's odd factor cannot cancel. Hence B(w') != B(w). Modular collisions must be nonzero multiples of 3^r; they are not equality of the exact affine maps at fixed A.

This does not give useful modular injectivity: the numerator range may span many multiples of 3^r.

## Genuine modular collision in the critical band

The bounded check finds at r=11,A=17:

    w =(1,7,1,1,1,1,1,1,1,1,1),
    w'=(7,1,1,1,1,1,1,1,1,1,1).

B(w)=5006191, B(w')=7486249; their difference is 14*3^11. Both canonical endpoints equal 3^11-1=177146. This is the d=6, i=1 resonance. It lies at the TOP of the residue interval, so it is NOT a witness of excess collisions in our small-origin-interval target. It also does not exhibit two positive integer trajectories reaching that endpoint. The construction starts from the two-step residue -1 modulo9 and appends valuation1 branches, which preserve -1 at the lifted moduli in this example.

## Several changes: the remaining arithmetic issue

For arbitrary fixed-mass words,

    Delta B=sum_(l=1..r-1) 3^(r-1-l)(2^S_l'-2^S_l).

For each nonzero term let d_l=S_l'-S_l. Its 3-adic valuation is

    t_l=r-1-l + [0 if d_l odd; 1+v_3(|d_l|/2) if d_l even].

If min t_l<r occurs exactly once, the modular collision is impossible: dividing by 3^min t_l leaves one nonzero unit modulo3. Thus a collision requires either all t_l>=r or at least two terms at the minimal valuation, followed by further cancellation sufficient to reach r. Ties alone are not sufficient. This is a necessary arithmetic condition, not an independent probabilistic saving.

This identifies a narrower next task: bound repeated cancellation among the changed cumulative sums while retaining the small-endpoint condition. Counting local forbidden moves or using the uniqueness of the exact B value cannot substitute for that joint bound. In particular, no uniform distribution or independence between cancellation and endpoint location has been established.

## Verification

check.py enumerates critical totals floor(r log_2 3) for 2<=r<=11, checks uniqueness of exact B for each panel, and checks all 60466 positive adjacent transfers for the exact difference, valuation formula, and collision iff. All pass. RESULT.json records the first modular witness. These finite checks validate the implementation and examples; the all-length local result rests on the algebra above. No paid calls, remote publication, or frozen-artifact edits were made.
