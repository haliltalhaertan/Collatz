# Review of all brainstorm directions — 2026-09-08

Exploratory mathematical review, not a new Collatz solution. No OpenRouter requests, no new computation-depth search, no old governed-stage mutation.

## 1. Fixed ending and black-hole basin

The standard positive Collatz cycle is 1->4->2->1. Reaching any member of its backward basin is sufficient to reach1. This is an exact reformulation, not a proof that every component joins it. A known infinite inverse basin need not exhaust all integers.

## 2. Avoiding every known safe orbit

Merging of forward orbits is an equivalence relation. The exceptional set, if nonempty, is forward and valid-predecessor closed. Closure alone allows disjoint components in functional graphs. For odd n, n and4n+1 merge because3(4n+1)+1=4(3n+1). Merging families reduce duplication but do not prove their root converges.

## 3. Minimal exceptions and checkpoints

The least exceptional positive integer must be odd and3mod4, and its entire orbit stays above or equal to its initial value. Separately, if S=20+27N_0 contains exceptional numbers, its least exceptional member cannot return to a smaller member of S. A smaller arbitrary integer is insufficient for this latter minimality argument.

Monks et al. establish interception of exceptional orbits by S; see Theorem6.4 in [primary paper](https://mathematicalgemstones.com/maria/papers/mmmm.pdf). Ordinary sufficient sets mean merging, not necessarily actual visitation. Existing project certificates remove50568 of65536 checkpoint-index residue classes from the least-exceptional-checkpoint search; they do not prove convergence of every member of those classes. Current report read, enumeration not rerun in this review.

## 4. Changed rules must be defined explicitly

Throughout the following examples F(n)=n/p when p divides n, and F(n)=qn+c otherwise. No rounding is used. Hitting1 counts as success; it need not remain at1.

For (p,q,c)=(4,7,1), residues2 and3mod4 alternate under multiplication. Starting2 never divides and grows indefinitely. For(3,4,2), any multiplication enters the even integers and division by3 preserves evenness. Exactly powersof3 ever reach1. For(3,5,1), residue2mod3 is fixed by5r+1, so2 grows forever. For(2,5,1), a different failure occurs:13->66->33->166->83->416->208->104->52->26->13 is a cycle disjoint from1.

The residue-dependent variant for division3, using5n+1 at remainder1 and5n+2 at remainder2, makes a division available after every multiplication but has cycle12->4->21->7->36->12. Thus activating division is not sufficient for global convergence.

## 5. General common-divisor obstruction [elementary derivation]

Suppose p>=2,q>1,c>=1 and there is d>1 dividing both q and c, with gcd(d,p)=1. Every multiplication enters dZ. Division by p preserves dZ whenever valid, since p is coprime to d; multiplication preserves it too. Thus no orbit can hit1 after a multiplication. Before its first multiplication it consists only of divisions by p. Therefore the complete positive basin of1 is exactly {p^k:k>=0}.

This explains the4n+2,/3 example by d=2. It does not apply to standard3n+1 because gcd(3,1)=1. Absence of this obstruction is not convergence.

## 6. What primality actually gives [elementary derivation]

Assume p prime and p does not divide q. While division has not occurred, residues follow r->qr+c modp, a permutation. Every nonzero residue reaches0 under this multiplication-only map if and only if q=1modp and c!=0modp.

Proof: q=1,c!=0 gives a full translation cycle. If q!=1 and c!=0, the unique fixed point r=c/(1-q) is nonzero, so that class never divides; q>1,c>=1 make its positive trajectories strictly increase without bound. If c=0, nonzero residues stay nonzero. These exhaust the cases. No conclusion is claimed when p divides q or p is composite.

For distinct prime multiplier q and divisor p with c=1, q=1modp is therefore necessary to prevent this particular escape mechanism. For p=2 every odd prime q satisfies it, but the5n+1 cycle shows it is far from sufficient. Primality alone does not create a universal attractor.

## 7. Consecutive numbers

The numerical adjacency of1,2,3 does not itself prove anything. The preceding residue and common-divisor conditions distinguish the successful local features of3n+1,/2 from the failure of4n+2,/3. Generalized maps require their full residue rules, not just a list of coefficients; see [Goncalves–Greenfeld–Madrid](https://arxiv.org/abs/2111.06170).

## 8. Odd numbers as even plus one

For n=4k+1>1, the path reaches(3n+1)/4=3k+1<n. For n=4k+3, its next odd value is(3n+1)/2=6k+5>n. This provides exact descending and ascending families.

A further exact constraint: write odd n=2^k u-1, u odd, k=v_2(n+1)>=1. There are exactly k-1 successive odd-to-odd transitions with only one halving. Their values are n_j=3^j*2^(k-j)*u-1 for0<=j<=k-1. For j<k-1 the value is3mod4; at j=k-1 it is1mod4 and the next transition has at least two halvings. Thus an uninterrupted sequence of such upward odd-to-odd steps cannot last forever for a positive integer. Repeated finite upward runs separated by insufficient decreases remain possible under this argument.

## 9. Total multiplication versus total division

For odd-to-odd steps with exponents a_i, A_j=sum a_i and A_0=0,

n_j=(3^j n_0+C_j)/2^A_j,
C_j=sum_{i=0}^{j-1}3^(j-1-i)2^A_i>0.

Numerical descent is equivalent to2^A_j>3^j+C_j/n_0. A fixed positive frequency of extra divisions, or average random drift, does not automatically establish this along every deterministic orbit. The endpoint correction must be retained.

## 10. Relation to earlier dense-transform work

The proved boundary-configured low-excursion contribution Theta(1/R) and compact-height joint exponential bound concern a conditional arithmetic-phase law. Neither counts actual safe Collatz integers. The auxiliary phase z is not the Collatz integer. These estimates and checkpoint descent share parity/valuation word encodings, but a universal transfer theorem is absent. The dense global C/R bound and deterministic checkpoint exhaustion both remain OPEN.

## Resulting priority

Most concrete combination: unavoidable checkpoints + exact parity cylinders + smaller-checkpoint merging/descent certificates. Changed-rule examples serve as counterexamples to overly broad proof principles. A next argument must specifically rule out indefinitely repeated unresolved returns, not merely show that most classes are easy or that a single upward run ends. No global decreasing rank, no exhaustion, and no Collatz proof obtained here.
