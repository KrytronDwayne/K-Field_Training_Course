# Lesson 5 — The primitive hypercharge line

Essential question: Which part of the charge choice is forced by the equations, and which part is a convention?

Goals: factor the cubic and verify a completed square; solve 3a+2b=0 over integers; select a primitive generator and declare its sign.

Prerequisite bridge: Lesson 4 derived the cubic polynomial and two mixed sums. We use ordinary distribution, the fact that a real square is nonnegative, and divisibility of integers. No matrix positivity theorem is assumed.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. First: factorization and positivity. Second: determinant connection, integer solutions and normalization.

## C15.05-E1 — A line of solutions

Factoring means writing an expression as a product that expands to the original. Verify by distribution that the cubic from Lesson 4 equals

(3a+2b)(36a²+24ab+20b²).

The products with 3a are 108a³+72a²b+60ab². The products with 2b are 72a²b+48ab²+40b³. Combining like powers gives exactly (108,144,108,40). No terms disappear.

Now “complete the square”: turn part of a quadratic into a squared expression plus a remainder. Since (a+b/3)²=a²+2ab/3+b²/9, multiplying by 36 gives 36a²+24ab+4b². Our quadratic has 20b², so the remainder is 16b²:

36a²+24ab+20b² = 36(a+b/3)²+16b².

For real a,b, both squares are nonnegative. If their sum is zero, the second term forces b=0 and the first then forces a=0. Thus for any nonzero pair the quadratic is positive. A product can vanish only if one factor is zero; the cubic therefore vanishes precisely on 3a+2b=0 for nonzero real pairs. The zero pair also satisfies the equation but supplies no nonzero charge generator. Mixed and linear tests already impose the same line. Pure SU3³ is zero independently of a,b for this inventory.

Why call this a determinant lock? The top exterior state Ω=c1∧c2∧c3∧w1∧w2 uses all five basis labels. Under a diagonal transformation its multiplier is the product of the five individual multipliers; this product is the diagonal determinant. If the color phase exponent is aθ and the weak exponent is bθ, the top product has exponent (3a+2b)θ. Requiring that top product to stay unchanged for every continuously varying θ requires 3a+2b=0. In this course that volume-preservation contract is declared, then its arithmetic is checked. It agrees with the anomaly line for this particular carrier; we have not classified arbitrary matter assignments.

## C15.05-W1 — Worked primitive solution

Solve 3a=−2b with integers a,b. Because 3 does not supply a factor of 2, a must be even. Write a=−2k; substitution yields b=3k. Conversely every integer k produces a solution. A nonzero pair is primitive when the greatest common divisor gcd(|a|,|b|) is 1: no common positive factor larger than one remains. Here gcd(2|k|,3|k|)=|k|, so k=+1 or −1. We declare color negative and weak positive, choosing (−2,3). This fixes the global sign and gives the basis weights (−2,−2,−2,3,3); Y=q/6 is the normalization already used.

## C15.05-P1 — Practice with worked answers

Classify (−4,6), (2,−3) and (1,1). Independently expand both the completed square and the factored cubic before checking the preceding derivation.

Answers: (−4,6) has 3a+2b=−12+12=0 but gcd=2, so divide both entries by 2 to get (−2,3). (2,−3) is primitive and lies on the line, but reverses the declared sign convention and all charges. At (1,1), the quadratic is 36+24+20=80, the linear factor 5, and the cubic 400, agreeing with Lesson 4. Expanding the square gives 36a²+24ab+4b²+16b². Expanding the product gives a³ coefficient 108, a²b coefficient 72+72=144, ab² coefficient 60+48=108 and b³ coefficient 40. These are the required independent multiplication checks.

## Diagnostic checks

1. **C15.05-D1:** Why is (0,0) excluded from primitive nonzero generators although it cancels every charge sum?
2. Give two further integer solutions and reduce them to a primitive pair.
3. Could the quadratic vanish at a nonzero real pair with b≠0?
4. Does the equation alone choose which block has positive charge? State the determinant-lock hypothesis.

Worked answers: (1) It generates no nonzero weights; primitive here requires a nonzero pair with gcd 1. (2) (−6,9) and (−8,12), dividing by 3 and 4 respectively, give (−2,3). (3) No: 16b² is then strictly positive. (4) No; the chosen sign is declared. The determinant argument preserves the five-label top product for every phase parameter θ, on this color-first carrier.

> Claim scope: Algebra and divisibility establish the line conditional on the stated inventory and weights. S02 KFM-X024 /proof_nodes/69/formula reports primitive central selection. No new physical sign selection or different matter-carrier classification is inferred here.

Next dependency: [Lesson 6](lesson-06.md) checks complement, dual action and the separate parity count.
