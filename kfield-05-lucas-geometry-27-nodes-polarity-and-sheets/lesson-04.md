# Lesson 4 — Parity and directed signs

**Essential question:** Which information survives when a sheet number becomes a class label?

**Goals:** Compute node polarity for positive and negative sheet numbers; compute remainder classes modulo 3; distinguish both labels from directed orientation and reconcile their populations.

**Prerequisite bridge:** Lesson 3 supplied the integer λ and its seven populations. We now group those integers in two ways. Budget: explanation/work 20 minutes (10 parity, 10 remainder), practice 15 (7 parity, 8 remainder), checks/feedback 15, transition 5.

## C05.04-E1 — Even and odd include negative integers

An integer is even when it equals 2k for some integer k. It is odd when it equals 2k+1. Thus −2=2(−1) is even and −3=2(−2)+1 is odd. Define the node polarity χ(L)=(-1)^λ, pronounced chi. Operationally χ is +1 for even λ and −1 for odd λ. For nonnegative powers, pairs of factors (−1)(−1) multiply to +1. Negative powers are reciprocals: (−1)⁻³=1/(−1)³=−1, giving the same even/odd rule. Zero is even and (−1)⁰=1.

Negating L changes λ to −λ. If λ=2k, then −λ=2(−k) remains even. If λ is odd, its negative remains odd. Therefore χ(−L)=χ(L), even though p(−L)−O=−(p(L)−O). A number giving even/odd class cannot tell us which direction a displacement points.

## C05.04-W1 — Worked polarity

For L=(1,−1,1), λ=1−1+1=1, odd, so χ=−1. For L=(1,1,0), λ=2, even, so χ=+1. Their negatives have sums −1 and −2 and retain those respective χ values. A negative λ does not automatically mean negative χ.

## C05.04-P1 — Guided polarity practice, with answer

Find χ for (−1,−1,−1) and the center, then count both polarities from the seven sheets. Answer: sums −3 and 0 give −1 and +1. Even sheets −2,0,2 contain 3+7+3=13 nodes. Odd sheets −3,−1,1,3 contain 1+6+6+1=14. Keep all 27 rows; these totals are an additional summary.

## C05.04-E2 — Remainders modulo 3

The notation r₃=λ mod 3 means the unique remainder in {0,1,2} when λ=3k+r₃ with integer k. For negative λ, choose k so the remainder is nonnegative and less than 3. This groups integers three steps apart; parity instead groups integers two steps apart. Do not give these fields the same column name.

## C05.04-W2 — Worked distinction

At λ=−2, write −2=3(−1)+1, so r₃=1 and χ=+1. At λ=1, write 1=3(0)+1, so r₃=1 but χ=−1. The shared remainder has not preserved parity. Conversely λ=0 and λ=2 both have χ=+1 but have remainders 0 and 2, so polarity does not preserve remainder either.

## C05.04-P2 — Guided remainder practice, with answer

Find r₃ and χ at −1 and 2. Then group the seven populations by r₃. Answer: −1=3(−1)+2, giving r₃=2, χ=−1; 2=3(0)+2 gives r₃=2, χ=+1. The full accounting is:

|r₃|Sheets contributing|Population|
|---|---|---|
|0|−3,0,3|1+7+1=9|
|1|−2,1|3+6=9|
|2|−1,2|6+3=9|

These equal populations describe the same 27 nodes whose seven-sheet populations are unequal and whose polarity populations are 13 and 14. A different grouping answers a different question.

> **Claim scope:** χ is the node-polarity definition in S02 /backbone_sequence/2/definitions/2. The remainder counts are our finite derivation. χ, r₃, directed vector signs, and the orientation sign introduced next are separate fields. Detector parity, A1 carry parity, chirality, family labels, and primitive lifts are other source concepts, not synonyms for χ. Their calculations are outside this course. No complex phase formula is required; any such extension would also require the same affine origin convention.

## Diagnostic checks

1. **C05.04-D1:** Compare λ, χ and displacement for L=(1,−1,1) and −L. Can χ recover orientation?
2. **C05.04-D2:** Reconcile populations 9,9,9 with 13,14. Does either label determine L?
3. **C05.04-D3:** A learner reports −2 mod 3=−2. Repair the result and show λ=3k+r₃.
4. **C05.04-D4:** Compute λ,r₃,χ for (0,−1,0) and (1,1,1).

**Worked answers:** 1. λ changes from 1 to −1; χ stays −1; displacement reverses from (0,−1,−3/2) to (0,1,3/2) U. χ cannot choose a direction. 2. Remainders partition by steps of three, polarity by steps of two; both totals are 27. Neither label identifies a triple: (1,0,0) and (0,1,0) share both labels. 3. −2=3(−1)+1, so the allowed remainder is 1. 4. The first has λ=−1,r₃=2,χ=−1; the second λ=3,r₃=0,χ=−1.

**Next dependency:** [Lesson 5](lesson-05.md) explicitly stores the direction that polarity cannot recover.
