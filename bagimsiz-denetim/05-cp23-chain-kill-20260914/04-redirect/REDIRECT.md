# CP23 REDIRECT — contrarian strategy report

Gate: `gate_check.py` reproduces **Ecal(4,3) = 40/3** and **Ecal(5,2) = 31/3**
([EXACT COMPUTATION], exact `Fraction` arithmetic). All strategic claims below rest on
computations in `gate_check.py`, `cycle_analysis.py`, `analogue_kill.py` (all passing).

Convention: every substantive statement carries one of
[PROOF] [EXACT COMPUTATION] [CONJECTURE] [FAIL] [JUDGEMENT].
Collatz is NOT solved. A finite table is NEVER a uniform theorem.

## 0. Barrier verdicts (challenging B1, B2, and the lead's self-assessment)

- [JUDGEMENT] B1 (measure-zero escape) STANDS for divergent orbits: no census statistic can
  see a single divergent orbit, and nothing this session weakens that. It is EVADED (not
  refuted) only by the cycle direction: a cycle is a finite exact Diophantine condition,
  not a statistical one.
- [JUDGEMENT] B2 (finite-information wall) STANDS: nothing here writes down an infinite
  object. Cycles evade it for the same reason — a length-m cycle is finitely checkable;
  the infinitude over (m,k) is handled by approximation theory, not by statistics.
- [JUDGEMENT] The lead's "NO measurable progress toward Collatz" is about right as stated
  but mislocated: the position is worse than stalled — the intended chain's step 3
  (mixing => counterexample has nowhere to hide) is REFUTED as stated by the 3n-1 witness
  below — while the assets (A3/A4, audit methodology, failure library) are worth MORE
  than the assessment claims, just not for the stated goal.

## 1. The chain-kill (see `analogue_kill.py`)

- [PROOF] Hp(-x) = -Hm(x) over integers, two-case parity check, where Hp/Hm are the
  3n+1 / 3n-1 shortcut maps.
- [PROOF] The 3n-1 map has the affine form Hm^m(h) = (3^k h - B_w)/2^m with the SAME
  B_w = sum_{odd j} 3^{suf_j} 2^j (sign flips in the unfolding, magnitudes identical).
- [PROOF] (modulo the standard word-periodicity lemma in the granted A1/A2 circle)
  Ecal(3n+1) = Ecal(3n-1) for ALL m,r, per stratum: odd residues pair as h <-> 2^m-h,
  endpoint multisets map by u -> -u+3^k, and J_r is invariant under u -> -u+c
  (sum-of-squares permutation). [EXACT COMPUTATION] 45/45 (m,r) pairs match exactly,
  total and per-stratum.
- [EXACT COMPUTATION] 3n-1 provably has cycles: Hm(1)=1 (fixed point) and
  5 -> 7 -> 10 -> 5. 5n+1 provably has the 5-cycle 1 -> 3 -> 8 -> 4 -> 2 -> 1, yet shows
  zero monotonicity violations on 78+40 exact rows.
- [FAIL] Therefore Ecal-mixing coexists with cycles. The intended chain step 3 is false
  as stated: even a full proof of the open target would prove mixing for maps with known
  cycles. (Finite-table caveat applies only to the 5n+1 rows; the 3n-1 half is proved.)

## 2. Cycles analysis (see `cycle_analysis.py`)

- [EXACT COMPUTATION] A1 + B_w formula + B odd + B%3!=0 re-verified m<=8 from scratch.
- [EXACT COMPUTATION] A3 (endpoint collision <=> B_w=B_w' mod 3^k) re-verified m<=8.
- [PROOF] From A1, a shortcut-map cycle of length m, weight k satisfies
  x = B_w / D, D = 2^m - 3^k, hence D > 0 and D | B_w (3n+1), with the quotient's word
  equal to w (self-consistency, strictly stronger than divisibility).
- [PROOF] gcd(D,6)=1 always (D odd; D = 2^m mod 3 = +/-1, never 0). A2 controls 2-adic
  data, A3 controls 3-adic data: the cycle divisor lives on prime support disjoint from
  both. Structural mismatch, no computation needed.
- [EXACT COMPUTATION] Word-enumeration scan m<=12 and m in {14,16,18,20}: the only
  D-divisible words are trivial-cycle repetitions (x=1); zero nontrivial cycles.
  (Mechanism demo only — NOT a bound; classical bounds live far above m=20.)
- [EXACT COMPUTATION] On small-D strata, D-divisibility runs at/below chance
  (e.g. (8,5): 0/35 vs 1/13; (10,6): 0/126; (13,8): 0/792) and conditioning on A3 class
  never enriches it (cond_max = 0 throughout at n>=6). A3 gives no observed leverage on
  the cycle condition. Finite tables: consistent with independence, proves nothing.
- [PROOF] 3n-1 shares the same B_w combinatorics; its cycles live at D < 0
  (x = B_w/|D|). So ANY future B_w-based cycle attack must be sign-sensitive, and any
  argument symmetric in +/-D is dead on arrival (3n-1 is the witness).
- [JUDGEMENT] The counting view reproduces the classical doorway (D|B_w with B_w >= D
  forces m/k near log_2 3), but walking through it needs Diophantine-approximation
  machinery (lower bounds for |2^m-3^k|) this programme does not own. Verdict: A1+A3
  reformulate cycles but exclude nothing; the honest cycle play is a timeboxed lemma
  hunt with a pre-registered kill condition, aimed below the literature, not above it.

## 3. Ranked directions (EV = value x probability / cost; probabilities [JUDGEMENT])

| rank | id | direction | P | cost | nearest dead path / why this differs |
|---|---|---|---|---|---|
| 1 | D4 | Analogue filter: port every claim to 3n-1/5n+1; nothing ships without analogue tests | 0.9 | days | Lopez-Stoll bridge / used as FALSIFIER, not bridge |
| 2 | D9 | Join ccchallenge.org as auditors (methodology for their 0-auditor queue) | 0.8 | days | none / first outside-eyes move ever |
| 3 | D10 | Preprint negatives + chain-kill; 2-3 outside experts | 0.6 verdict | weeks | none / programme never sought review |
| 4 | D3 | Cycle lemma-or-kill, 2-week timebox, sign-sensitive only | 0.4 scoped / 0.05 full | 2 wks | forward-T7r (circular) / finite Diophantine target, evades B1+B2 |
| 5 | D11 | Stop proving; publish failure library + 239-row dataset | 0.85 | weeks | none / negative results AS the contribution |
| 6 | D8 | Lean the kernel A1-A3,A5,A7,A8 | 0.7 | months | A10 audit / machine-checked instead of human-checked |
| 7 | D7 | Pure parity-word combinatorics paper (A3/A4, zero Collatz claims) | 0.3 | weeks | Christoffel extremality / claims only proved facts |
| 8 | D5 | Terras-type stopping-time density from the census | 0.5 | weeks | Tao/Si transfer / aims BELOW Tao (classical), honestly statistical |
| 9 | D2 | Weakened averaged mixing for almost-all theorem | 0.15 | weeks | naive Fourier decay / needs only averaged decay; BUT fixed-s trend to m=16 shows no decay, and B1 still bites |
| 10 | D6 | 2-adic ergodic theory beyond literature | 0.2 | months | none / statistics IS the goal there, B1 moot |
| 11 | D12 | Full stop + archive | baseline | 0 | beats grinding |
| 12 | D1 | Grind current target to proof | 0.05 | months | all 63 kills / NO structural difference from them; A9 says the needed ingredient is unidentified; chained value ~0 after chain-kill |

Top-three defense. [JUDGEMENT] D4 first: it already produced this session's largest
finding at minutes of compute; institutionalising it costs ~nothing and blocks years of
false-generality work. [JUDGEMENT] D9 second: exact complementary fit (programme owns
audit methodology, zero formalisation; ecosystem owns 375 sources, zero auditors) with
days of cost and near-certain useful output. [JUDGEMENT] D10 third: the crisis is
direction, not effort (63 kills prove effort is abundant); only outside review can
convert that record into a verdict, and the abstract-test (draft it crisply or admit
unreadiness) is free. D3 is the sole technical bet because it alone evades B1+B2.

## 4. Direct recommendation

Freeze the mixing grind immediately and recharter the programme around falsification and
outside contact: make the 3n-1/5n+1 analogue filter mandatory for every existing and
future claim, give one researcher a two-week timeboxed attempt at a sign-sensitive cycle
lemma with a pre-registered kill condition (kill it if the independence computation does
not budge), and put everyone else on writing the failure-library plus chain-kill preprint
and taking it to ccchallenge.org and two outside experts for audit and review, accepting
in advance that if review confirms the chain is dead the programme closes with the
write-up as its contribution.

## 5. Cheap kill

[JUDGEMENT] Attractive direction killed: "Ecal-mixing as a Collatz detector" (prove the
target, or any symmetry-blind mixing statement, as a step toward excluding
counterexamples). [FAIL] Witness: 3n+1 and 3n-1 share Ecal tables exactly (45/45 pairs,
total and per-stratum, plus proof above), yet 3n-1 provably cycles (1 fixed; 5-7-10-5);
5n+1 mixes on 118/118 exact rows yet provably 5-cycles (1-3-8-4-2-1). Mixing, in exactly
this programme's sense, coexists with cycles — so no proof of the target, however
beautiful, can by itself exclude a cycle. Run `analogue_kill.py`.
