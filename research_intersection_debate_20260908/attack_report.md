# Exact offset equivalence and audit of progression compression

## Full continuation-law equivalence

Fix odd slope a, positive length N, and lookahead R. The R-step parity-word coding is a bijection on residues modulo q=2^R. Therefore two progressions aj+b and aj+b', j=0,...,N-1, have identical full continuation-word histograms exactly when their residue histograms modulo q agree.

Write N=lq+s,0<=s<q. If s=0, every residue occurs l times, and all offsets are equivalent. If0<s<q, multiplication by a^-1 identifies the residual histogram with a proper consecutive cyclic arc of length s. A proper nonempty cyclic arc has trivial translation stabilizer (its oriented entry boundary is unique). Consequently equivalence holds iff b=b' modq.

Thus q offset classes are generally distinguishable when N is not a full-period multiple. This is a statement about preserving FULL continuation-word laws over arbitrary offsets, not an algorithmic lower bound or a prohibition on compression for a scalar final-weight query.

## Actual equal-weight prefix example

For all j>=0, the classes x=1+16j and x=3+16j have four-step prefix weight2. Their images are

    H^4(1+16j)=1+9j,
    H^4(3+16j)=2+9j.

They have identical slope, length and prefix weight. For lengthN1 their next-step polynomials are z and1. ForN2 their two-step polynomials are2z andz+z^2. Dropping offset therefore changes even the scalar tail-weight count.

## The audit agent's modular compression survives this attack

At depth i>=1, before all m input bits have been exposed, each prefix cylinder has progression3^k*j+b of length2^(m-i). Set A=m+t and R=A-i. Retain the state(k,b mod2^R), with its multiplicity.

If b and b' differ by a multiple of2^R, they have the same parity. Each j-parity child divides its offset by2, after optionally multiplying by3 and adding1. Child offsets therefore remain congruent modulo2^(R-1). Both children have equal prescribed length2^(m-i-1). The transition is well-defined on the quotient states. Merging preserves multiplicity because original prefix cylinders partition the starting interval; coincident future residues do not make those original starts identical.

Initial odd starts require the special first step: (a,b,N)=(2,1,2^(m-1)) maps to(3,2,2^(m-1)), with i1,k1. It does not split into two input branches.

For i<=m the number of reachable states is at most

    min(2^(i-1),(i+1)*2^(A-i)).

After i=m each progression is a singleton, so it follows a single child and state counts cannot increase except through an optional polynomial-sized extra output-weight label. The largest state bound is polynomial(A)*2^(A/2) when t<m. Slopes3^k and integer multiplicities use only polynomial(A)-bit arithmetic, so their manipulation does not introduce a hidden2^m factor.

This is a valid exact finite-computation improvement over enumerating all2^(m-1) odd starts when A<2m. It is not an asymptotic upper bound on the number of selected starts. Nor is a novelty claim made for modular-state dynamic programming.

The generic offset equivalence does not obstruct this method: it retains the required precision and compresses by merging the comparatively few reachable prefixes. In this application N=2^(m-i)<2^(A-i) whenever t>0, so dropping offset entirely is invalid, while reduction modulo2^R is exact.

## Checks and scope

attack_equivalence.py verifies188 slope/length/lookahead parameter cases and200 actual prefix identities. All pass. The audit agent implements the compressed dynamic program independently; this note audits its transitions and complexity proof. No paid calls or new count-exponent claim.
