# Lesson 2 — The sixteen even exterior states

Essential question: How can a census prove that no state was missed or counted twice?

Goals: enumerate the six allowed bidegrees; calculate their multiplicities; list every degree-four state and track a block exchange sign.

Prerequisite bridge: Lesson 1 gave sorted signed subsets and binom(n,k). We now group those subsets without losing labels or signs.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Use period 1 for bidegrees and period 2 for explicit lists and block signs.

## C15.02-E1 — Two counts instead of one

The bidegree (r,s) records r selected color labels and s selected weak labels. Thus 0≤r≤3 and 0≤s≤2. The total exterior degree is r+s. Even requires r+s to be 0,2,or 4. To enumerate systematically, run through r=0,1,2,3 and retain s values with the same parity. No other allowed pair can have an even sum.

A multiplicity is the number of independent basis states in a group. For each choice of r colors, there are binom(2,s) choices of s weak labels. Choices are independent, so multiply: m=binom(3,r)binom(2,s). This multiplication counts pairs of choices.

The source calls a group with common transformation behavior a sector or multiplet. We attach its labels after counting. A superscript c in nu^c, e^c, u^c, d^c is part of the supplied left-Weyl naming convention; it is not a color basis label or an instruction to take a complement. Q and L are sector names. We teach transformation labels in Lesson 6.

## C15.02-W1 — Worked census

|Bidegree (r,s)|Choice calculation|Multiplicity m|Source sector|
|---|---|---:|---|
|(0,0)|1×1|1|nu^c|
|(0,2)|1×1|1|e^c|
|(1,1)|3×2|6|Q|
|(2,0)|3×1|3|u^c|
|(2,2)|3×1|3|d^c|
|(3,1)|1×2|2|L|

Sum: 1+1+6+3+3+2=16. Q has c1∧w1,c1∧w2,c2∧w1,c2∧w2,c3∧w1,c3∧w2. The degree-two groups contain 1+6+3=10, agreeing with Lesson 1. This second route independently checks the count.

Suppose someone writes the weak block before the color block. Passing s weak labels across r colors requires rs neighbor swaps, because each weak label passes every color. Therefore the sign is (−1)^(rs). For (1,1) it is −1; for (2,2) it is +1. Merely renaming a block order does not justify discarding this sign.

## C15.02-P1 — Practice and answers

List all degree-four states by the omitted label. Separate them into bidegrees. Reverse their color/weak blocks and record the signs. Also split the degree-two count into its three groups.

Omitting c1 gives c2∧c3∧w1∧w2; omitting c2 gives c1∧c3∧w1∧w2; omitting c3 gives c1∧c2∧w1∧w2. These are the three (2,2) states, whose block sign is (−1)^4=+1. Omitting w1 gives c1∧c2∧c3∧w2; omitting w2 gives c1∧c2∧c3∧w1. These are the two (3,1) states, whose block sign is (−1)^3=−1. Degree two has three color pairs, six mixed pairs and one weak pair. Together with the empty state, the totals are 1+10+5=16.

These lists use positive coefficients in canonical order. They are not oriented complement formulas; Lesson 6 adds those orientation signs.

## Diagnostic checks

1. **C15.02-D1:** Convert w2∧c3 into color-first order. Is the sign optional?
2. Why is (3,2) excluded even though both counts lie within their bounds?
3. Why does (2,0) have three states rather than six?
4. Does the full exterior algebra contain sixteen or thirty-two basis states?

Worked answers: (1) −c3∧w2, with a required minus sign. (2) Degree 5 is odd. (3) Each pair of colors is an unordered subset: 3×2/2=3. (4) Thirty-two; the source selects sixteen even states. The sixteen odd states remain a separately recorded complementary sector.

> Claim scope: This is finite mathematics for H=C3⊕W2, color first. Sector names follow S02 /backbone_sequence/10/sector_census. Exterior block factorization is KFM-X022 at /proof_nodes/67/formula. Names and dimension alone do not establish a physical realization.

Next dependency: [Lesson 3](lesson-03.md) assigns additive charges to the census.
