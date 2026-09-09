# Independent tail audit: a valid offset bound and its ceiling

2026-09-08. Exploratory theorem and bounded verification. No paid calls. This does not exclude a new orbit class.

Let H be the shortcut Collatz map. For odd 1<=x<2^m, let k be its first-m parity weight and y=H^m(x). Write

    2^m y = 3^k x + C.

For fixed m,k, moving an odd bit one place later past an even bit increases C. Consequently

    0<C<=2^(m-k)(3^k-2^k).

This maximum even allows an initially even word and thus remains an upper bound for odd starts. Canonical inverse positivity gives 1<=y<3^k. The height bound by itself is weak: in the relevant parameter range 2^t-1 fits below3^k and has t consecutive odd parities. But the affine OFFSET bound limits the number of original starts per candidate y without an injectivity assumption.

If the following t parity bits have weight j, their admissible residues modulo2^t number binom(t,j). Each residue has at most ceil(3^k/2^t) representatives in [1,3^k). For fixed y, all possible x belong to an interval of length less than2^(m-k), by the displayed C bound. Thus the number N_(m,t,k,j) of starts obeys

    N <= min{binom(m-1,k-1),
             binom(t,j)*ceil(3^k/2^t)*(2^(m-k)+1)}.

The final factor deliberately counts all integer starts, losing only a bounded parity factor. It covers mergers: many distinct prefixes can lead to the same y, but all their starts must lie in that short interval.

In the critical scaling m=br+o(r), t=(alpha-b)r+o(r), k=sr+o(r), j=(1-s)r+o(r), summing the bound over k gives exponent at most

    G(b)=max_s min{b H_2(s/b),
          b-s+max(alpha*s-(alpha-b),0)
          +(alpha-b) H_2((1-s)/(alpha-b))},

where max(0,1-alpha+b)<=s<=min(b,1). The expression is a rigorous asymptotic upper exponent. Numerical optimization of it is calibration, not a certified decimal optimum.

At b=1.2 the numerical envelope is approximately1.1992471920426042, versus the previous exposed-bits value1.199456224042059. This is a small fixed-b improvement, still far from the ideal exponent1.1206813872 or the kappa1.053 bridge threshold1.1396011396.

## The principal's ceiling objection is correct

Take s=b/alpha, a feasible point. Both the prefix and tail entropy arguments equal1/alpha. Put h=h_* and H=h/alpha. The prefix expression is bH. The second expression minus bH equals

    b(1-1/alpha)+(alpha-2b)H,                    b<=alpha/2,
    3b-b/alpha-alpha+(alpha-2b)H,                b>=alpha/2.

The first is nonnegative. The second is affine in b and positive at both ends: (alpha-1)/2 at alpha/2 and2alpha-1-h at alpha. Therefore G(b)>=b*h/alpha for every0<b<alpha. No choice of b in this offset envelope can raise the old bridge ceiling alpha/h=1.0526808586079717. The decimal fixed-b gain must not be presented as progress past that ceiling.

## Verification and literature boundary

audit_tail.py independently enumerates odd starts for all m<=12 and1<=t<=6, checks the exact affine identity, offset maximum and canonical height, and checks1325 nonempty count cells against the displayed bound. All passed. Its entropy optimization splits at the max-affine kink; each resulting function is concave, so ternary search is appropriate for numerical calibration.

The principal requested a parallel primary-source check of Inselmann, arXiv2402.03276v3. I read Lemmas2.13--2.16 and their proofs: the bootstrap transfers power-density exceptions, but loses exponents through neighborhood expansion and a parity-concentration auxiliary set. The explicit transformations in2.13 and2.14 do not alone give the final usable exception exponent. Theorem-level existence of a positive exponent must not be upgraded to the required exponent above1-1/1.053 without tracing the auxiliary parameters. Source: https://arxiv.org/html/2402.03276 . This is a relevance/quantifier check, not a full independent audit of the paper.

The principal's application of Theorem2.18 is valid, conditional only on that sourced theorem as stated. Put d=1-alpha/2, b=1.2, epsilon=.1. Discard x<2^(.5r). For the remaining x up to2^(br+o(r)), the theorem's horizon log_2(x)/d contains A=alpha*r+O(1), since .5/d>alpha. Its good set gives H^A(x)/x<=2^((-d*alpha+.12+o(1))*r), exponentially tending to0. But parity weight r implies H^A(x)/x>=3^r/2^A>=c0>0 on any fixed critical band. Thus every remaining counted x belongs to the theorem's exceptional set. If its positive exception exponent is D_.1, then

    F <= 2^(.5r)+O(2^((1.2*(1-D_.1)+o(1))*r)).

This provides an existential positive exponent saving at the chosen b. It does not certify D_.1>1-1/1.053, nor show the saving improves the explicit offset estimate.
