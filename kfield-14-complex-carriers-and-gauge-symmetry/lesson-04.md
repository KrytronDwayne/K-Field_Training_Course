# Lesson 4 — Determinants and the top-form lock

Essential question: What extra constraint preserves an ordered volume coefficient as well as lengths?

Goals: Compute small determinants; calculate the three-plus-two phase constraint; distinguish norm preservation from determinant preservation.

Prerequisite bridge: Lessons 2–3 taught unitary matrices and the ordered blocks C₃,W₂. Now attach one scalar to a square matrix. Use two periods: determinant intuition and calculation, then the phase constraint.

## C14.04-E1 — A scalar that records oriented scaling

For a real 2×2 matrix [[a,b],[c,d]], its columns are the transformed unit directions. Their signed parallelogram area is ad−bc, the determinant det A. Swapping columns reverses the sign; equal columns make area zero. For complex entries use the same algebraic formula, although the result is a complex coefficient rather than ordinary real area. For example det [[1,i],[i,1]]=1−i²=2. Multiplying every entry of a 2×2 matrix by s multiplies its determinant by s², since each term has two factors. Therefore Lesson 2's V has determinant (1/√2)²·2=1.

A diagonal matrix has determinant equal to the product of its diagonal entries. For a block diagonal matrix diag(A_c,A_w), determinant equals det A_c times det A_w. These rules suffice for every required calculation. Recognition-only general rule: det(AB)=det A det B.

A top form here is an ordered alternating volume coefficient Ω. “Alternating” means exchanging two input directions reverses its sign and repeating a direction gives zero. Under a transformation A the coefficient scales by det A. We use this transformation rule as the contract; a full construction with exterior algebra belongs to the next course. Preserving Ω means keeping the coefficient itself unchanged, so det A=1, not merely |det A|=1. A phase factor can have modulus one without equaling one.

The source contract preserves the Hermitian structure of each block (the inner products from Lesson 2), the block decomposition, and the top form. Thus A_c and A_w are unitary and det A_c det A_w=1. U(n) names the group of n×n unitary matrices, while SU(n) adds determinant one. The notation S(U(3)×U(2)) means pairs of unitary blocks whose determinant product is one; it does not require each block determinant to equal one separately. The multiplication of pairs is component by component. Lesson 5 teaches the group terminology.

Suppose a unit phase z acts with integer weight a on each color slot and weight b on each weak slot. The matrix is diag(z^a I₃,z^b I₂). Its determinant is z^(3a+2b). To preserve the top form for every phase, require 3a+2b=0. If the integer exponent n were nonzero, taking an angle π/n would yield z^n=−1, so it could not equal one for every phase. Integer solutions are a=−2m,b=3m: 3a=−2b requires a even, then substituting a=−2m gives b=3m. The primitive source choice uses m=1, giving weights (−2,−2,−2,3,3); “primitive” means no common integer factor greater than one in their magnitudes. The opposite choice m=−1 reverses the phase parameter. No physical charge unit is inferred from these integers.

## C14.04-W1 — Worked example

det diag(i,−i)=i(−i)=1. Color block diag(i,−i,1) therefore has determinant 1; weak block I₂ has determinant 1, so their product is 1. Every entry has modulus one, giving unitarity too. For central weights a=−2,b=3, the determinant exponent is 3(−2)+2(3)=0, and z⁰=1 for every unit phase.

## C14.04-P1 — Answered practice

Color diag(−1,−1,1) and weak diag(i,−i) have determinants 1 and 1; they preserve both block norms and Ω. Weights a=2,b=−3 also give 6−6=0. In contrast, a=1,b=0 at z=i gives determinant i³=−i and fails the top-form condition while preserving norms. Finally diag(2,1/2) has determinant 1 but sends (1,0) to (2,0): squared norm changes from 1 to 4. Both conditions must be checked.

> Claim scope: The preserved-block/top-form contract is source-local to S02 M10, with the order correction from S03. The diagonal and integer computations are verified here. Classification of the entire connected group is source-read recognition, not an untaught proof requirement.

## Diagnostics — C14.04-D1

1. Compute det [[2,1],[3,2]].
2. Test weights a=4,b=−6 for all phases. Are they primitive?
3. Why does testing z=1 alone never establish the all-phase lock?
4. Does diag(2,1/2) satisfy both conditions? Does diag(i,1)?

Worked answers: (1) 4−3=1. (2) 12−12=0, so the lock holds; common factor 2 makes them nonprimitive. (3) 1^n=1 for any integer n, including failing weights. (4) The first has determinant 1 but fails norm preservation; the second preserves norm but has determinant i, so fails to preserve Ω.

Next dependency: [Lesson 5](lesson-05.md) expresses these block transformations through a map and calculates precisely which inputs become invisible in its output.
