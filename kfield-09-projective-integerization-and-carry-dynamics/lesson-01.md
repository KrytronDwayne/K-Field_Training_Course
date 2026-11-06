# Lesson 01 — Nearest-integer maps need a tie rule

Essential question: How can two people turn the same number into the same nearest integer, even halfway between integers?

Goals: compute ceiling and floor for signed numbers; apply a deterministic half-tie rule; retain the signed rounding coordinate; distinguish rounding from cell ownership.

Bridge and readiness: From signed arithmetic and course 08, locate 0.5 and −0.5 on a number line. Each lies halfway between two integers. If you cannot name both neighbors, draw the interval and do that before rounding. No geometry from course 08 is needed beyond reading an ordered list of coordinates.

## C09.01-E1 — Defining the operation

An integer is a whole number, including zero and negative whole numbers. The ceiling of t, written ceil(t), is the least integer greater than or equal to t. Thus ceil(2.1)=3, ceil(−2.1)=−2, and ceil(−2)=−2. The floor floor(t) is the greatest integer less than or equal to t; floor(−2.1)=−3. Ceiling does not mean “move away from zero.”

Usually there is one nearest integer. At a half-tie there are two. Throughout this course define

**nint(t)=ceil(t−1/2): choose the lower integer at every exact half-tie.**

Subtract a half first, then take the ceiling. For t=2.4 this gives ceil(1.9)=2; for t=2.6 it gives ceil(2.1)=3. The rule is a function: each input has exactly one output. Define Q=nint(t) and the retained rounding coordinate epsilon=Q−t. This sign matters: a negative epsilon means the integer lies below the input. The original input is t=Q−epsilon.

Why is −1/2 ≤ epsilon < 1/2? If Q=ceil(t−1/2), then Q−1<t−1/2≤Q. Rearranging the right inequality gives Q−t≥−1/2; rearranging the left gives Q−t<1/2. The notation [−1/2,1/2) includes the left endpoint and excludes the right. The residual is an exact coordinate, not something to discard.

## C09.01-W1 — Worked signed ties

For t=1/2, subtracting 1/2 gives 0, so Q=0 and epsilon=0−1/2=−1/2. For t=−1/2, the ceiling input is −1, so Q=−1 and epsilon=−1−(−1/2)=−1/2. Likewise nint(3/2)=1 and nint(−3/2)=−2. These four cases all choose the lower integer. They do not alternate between lower and upper integers.

## C09.01-P1 — Guided practice and answers

Compute Q and epsilon for 49/100 and 51/100. Then add 3 to each input and repeat before reading the answers. After reading E2 below, return here and independently compute Q, epsilon, and the cell owner at both +1/2 and −1/2.

Answers: ceil(−1/100)=0, so the first pair is (0,−49/100). The second gives ceil(1/100)=1, so its pair is (1,49/100). After adding 3 the outputs are 3 and 4, while the residuals stay −49/100 and 49/100. In general, for any integer m, ceil(u+m)=ceil(u)+m because shifting every integer neighbor by m preserves their order. Therefore **nint(t+m)=nint(t)+m**. This translation rule will justify carry calculations in lesson 04, including at ties.

Signed-tie practice answers (use after E2): +1/2 gives Q=0, epsilon=−1/2, owner=1; −1/2 gives Q=−1, epsilon=−1/2, owner=0. In each case Q is the lower neighbor; the owner is the upper neighbor. Record both operations by name.

## C09.01-E2 — A different operation: cell ownership

A cell centered at integer n owns coordinates q with −1/2≤q−n<1/2. The owner is floor(q+1/2). At q=1/2 the owner is 1, with centered coordinate −1/2. The integerizer instead returns 0, with epsilon=0−1/2=−1/2. Both intervals look the same, but their subtractions run in opposite directions: q−owner versus Q−q. Never substitute one operation for the other.

> Scope: S02 M06 supplies the integerization framework, but its half-tie behavior is ambiguous. S03 finding AUD-013 identifies that ambiguity. This explicit lower-tie convention implements course amendment SA-09; it is not attributed to the original archive. All numbers in this lesson are teaching examples, not measurements.

## Diagnostic checks

1. **C09.01-D1:** At q=−1/2 compute the cell owner and integerizer. Explain their difference.
2. **C09.01-D2:** Compute ceil(−7/4), then nint(−7/4).
3. **C09.01-D3:** A program returns 1 at t=1/2. Is it implementing our contract? State the resulting epsilon.
4. **C09.01-D4:** Verify the translation rule at t=−1/2 with m=3. Recover the original t from its pair.

Worked answers: (1) owner=floor(0)=0; nint=ceil(−1)=−1. The owner centers q−owner, while integerization retains Q−q. (2) ceil(−1.75)=−1; nint=ceil(−2.25)=−2. (3) No: epsilon=+1/2 violates the excluded upper endpoint. (4) nint(2.5)=2=−1+3. Original t=−1−(−1/2)=−1/2.

Next: [lesson 02](lesson-02.md) applies this rule separately to three scaled coordinates.
