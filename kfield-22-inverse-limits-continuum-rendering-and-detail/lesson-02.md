# Lesson 02 — A different meaning of closeness

Essential question: Can two addresses be close while their integer representatives are far apart?

Goals: Compute two explicitly named distances; compare triple address distances; distinguish an exact shared prefix from incomplete knowledge.

Bridge and pacing: Lesson 01 taught remainders and reduction. A shared depth-k residue means the first k low-order digits agree. One 55-minute period: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15 minutes.

## C22.02-E1 — What does the distance measure?

Ordinary real distance between integers a and b is |a−b|. Absolute value removes the sign of the difference, so both |−9| and |9| equal 9. This measures separation on a number line.

Address distance measures a different feature. If two distinct complete addresses share exactly k low-order balanced digits before they differ, define δ=3^(−k)=1/3^k. If they are identical at every depth, define δ=0. With no shared digit k=0 and δ=1. More shared digits make δ smaller. For ordinary integers, divide their nonzero difference by 3 repeatedly until it is no longer divisible by 3. The number of successful divisions is k: equality modulo 3^k is exactly divisibility of the difference by 3^k. Integers here specify complete compatible histories through all of their residues.

For triples take the **maximum** of the three coordinate address distances. A triple agrees to depth k only if every coordinate does. For a finite pair of records agreeing through depth N, you can only say δ≤3^(−N) for their possible infinite extensions; equality requires the next digit to differ. Do not assume a missing tail is zero.

## C22.02-W1 — Worked comparison

Integers 1 and 28 differ by 27. Divide 27 by 3 to get 9, then 3, then 1: three divisions. They agree modulo3, modulo9 and modulo27, but not modulo81. Their address distance is 1/27 while their real distance is 27. By contrast, 1 and 2 differ by 1, which has no factor of 3: δ=1 and real distance=1. Thus the pair with the larger number-line separation has the smaller address distance.

> Claim scope: This distance is a mathematical definition for the ternary histories of S02 M18. No experimental metric or physical length is being inferred. Later, the real renderer will give another real-valued representation, distinct from the integer number line used here.

## C22.02-P1 — Practice, then check

Compare 4 and 13 in both distances. Then find the address distance between (1,4,0) and (28,13,0).

Answer: 13−4=9=3², so k=2, δ=1/9, real distance=9. The triple coordinate address distances are 1/27,1/9,0; their maximum is 1/9. The zero coordinate is retained and contributes distance zero.

## Diagnostics — C22.02-D1

1. Find both distances for 0 and 81.
2. Two finite histories agree through depth 3, with no tail rule. Is their distance exactly 1/27?
3. What is the address distance between a complete history and itself?
4. Histories begin (1,−1,−1,…) and (0,1,1,…), with every displayed tail continuing constantly. Do they share their first residue?

Worked answers: (1) Real distance 81; address distance 1/81, since 81=3⁴. (2) Only the bound δ≤1/27 is known. They might agree farther or forever. (3) Zero by definition; no finite first-difference depth exists. (4) No, their first residues are 1 and 0, so δ=1. Lesson 04 will calculate that these distinct histories render the same real coordinate. A renderer cannot be assumed to recover every history.

Next dependency: [Lesson 03](lesson-03.md) constructs complete histories from compatible finite levels.
