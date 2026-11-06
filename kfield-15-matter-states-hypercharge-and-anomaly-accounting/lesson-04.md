# Lesson 4 — Why anomaly sums are bookkeeping constraints

Essential question: What precisely has been checked when a weighted sum vanishes?

Goals: calculate five named sums with declared normalization; preserve sector contributions including failed trials; derive their general dependence on a,b.

Prerequisite bridge: Lesson 3 taught q=ar+bs and mq versus mq³. We now supply the weights for the source's local anomaly tests. An anomaly here names a potential symmetry-consistency obstruction in the reference field-theory interpretation. The core task is to evaluate its supplied finite coefficient, not derive quantum field theory.

Pacing: three 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Period 1: linear and cubic sums. Period 2: mixed and pure-color sums. Period 3: general polynomials and retained failing trials.

## C15.04-E1 — Five different ledgers

The source uses a left-Weyl inventory: all six rows are counted in one declared chirality convention, including the c-labelled sectors. SU3 names the color symmetry; SU2 names the weak symmetry; U1 names the phase/charge symmetry. The superscripts in test names identify which factors participate, not powers to apply to a group name.

For the gravity²–U1 test, sum mq. For U1³, sum mq³. These use all components. For SU3²–U1, the supplied quadratic index T is 1/2 for a color triplet 3 and its dual bar3, zero for a color singlet. Multiply T by q and the number of weak copies. Thus Q contributes 2q/2, u^c and d^c each q/2. Do not multiply by three again: T already describes the color representation. A spectator multiplicity counts copies from the other symmetry factor.

For SU2²–U1, each weak doublet has T=1/2. Q has three color copies and L one: contributions 3q/2 and q/2. The remaining rows are weak singlets and contribute zero. For pure SU3³, a 3 has coefficient +1 and a bar3 has −1, with weak spectator copies. Hence Q,u^c,d^c contribute +2,−1,−1. Notice that bar3 has the SAME quadratic index but the OPPOSITE cubic color coefficient. This distinction is essential.

## C15.04-W1 — Worked primitive ledger

The following uses q, not Y:

|Sector|mq|mq³|SU3²–U1|SU2²–U1|SU3³|
|---|---:|---:|---:|---:|---:|
|nu^c|0|0|0|0|0|
|e^c|6|216|0|0|0|
|Q|6|6|1|3/2|2|
|u^c|−12|−192|−2|0|−1|
|d^c|6|24|1|0|−1|
|L|−6|−54|0|−3/2|0|
|Sum|0|0|0|0|0|

For example, the cubic sum is 216+6−192+24−54=0. The mixed sums are (2×1−4+2)/2=0 and (3×1−3)/2=0. Switching consistently to Y=q/6 divides the linear and mixed sums by 6 and the U1 cubic sum by 216; the pure-color sum is unchanged. Zero remains zero, but nonzero trial coefficients must report their normalization.

## General calculation, with multiplication taught explicitly

In census order the six charges are 0,2b,a+b,2a,2a+2b,3a+b. Adding their multiplicity-weighted values gives 24a+16b=8(3a+2b). The first mixed sum is [2(a+b)+2a+(2a+2b)]/2=3a+2b; the second is [3(a+b)+(3a+b)]/2=3a+2b.

To expand a cube, distribute each factor in (x+y)(x+y)(x+y): the terms are x³, three x²y, three xy², and y³. Therefore (x+y)³=x³+3x²y+3xy²+y³. The cubic ledger is

8b³+6(a+b)³+24a³+24(a+b)³+2(3a+b)³.

The two (a+b) groups combine to 30(a+b)³. Their coefficients are (30,90,90,30), in the order (a³,a²b,ab²,b³). The final group contributes (54,54,18,2); the other two contribute (24,0,0,8). Adding columns gives 108a³+144a²b+108ab²+40b³. Lesson 5 factors this expression.

## C15.04-P1 — Two trials that must remain in the record

Recompute all five sums for synthetic choices (1,0) and (0,1). These are tests of the formula, not measured data or alternatives to be erased.

For (1,0), q=(0,0,1,2,2,3). Linear contributions are (0,0,6,6,6,6), totaling 24. Cubic contributions (0,0,6,24,24,54) total 108. SU3 mixed contributions (Q,u^c,d^c)=(1,1,1) total 3; SU2 contributions (Q,L)=(3/2,3/2) total 3. SU3³ remains 2−1−1=0.

For (0,1), q=(0,2,1,0,2,1). Linear contributions (0,2,6,0,6,2) total 16; cubic (0,8,6,0,24,2) total 40. SU3 mixed contributions (1,0,1) total 2; SU2 (3/2,1/2) total 2; SU3³ stays zero. Neither trial passes all five tests. Keeping the individual contributions lets us locate the obstruction rather than hiding it in a pass/fail label.

## Diagnostic checks

1. **C15.04-D1:** Derive the two general mixed sums and linear sum.
2. Why is Q's color mixed weight 2/2 rather than 6/2?
3. At (a,b)=(1,1), compute the cubic coefficient using the expanded polynomial.
4. Does SU3³=0 certify the remaining four tests? What happens to the (1,0) linear sum in Y units?

Worked answers: (1) Both mixed sums simplify to 3a+2b; the linear sum is 8 times that, as the expanded terms above show. (2) T=1/2 already incorporates the color representation; only its two weak copies multiply it. (3) 108+144+108+40=400. (4) No: (1,0) gives the counterexample retained in P1. Its linear Y sum is 24/6=4.

> Claim scope: These five source perturbative local coefficients are exactly checked for the declared inventory and normalization. They do not substitute for the separate Witten count or a proof for every non-liftable quotient-group bundle. Sources: S02 KFM-X023 /proof_nodes/68/formula and KFM-F035 /proof_nodes/82/formula. The reference-theory weights are supplied; the finite arithmetic is derived here.

Next dependency: [Lesson 5](lesson-05.md) solves the common cancellation condition.
