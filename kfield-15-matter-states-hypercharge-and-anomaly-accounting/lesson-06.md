# Lesson 6 — Parity and representation checks

Essential question: Which different questions can be hidden by the word parity?

Goals: compute an oriented complement and its charge; verify a diagonal dual-color action; distinguish exterior degree, weak-doublet count and physical chirality.

Prerequisite bridge: Lessons 1–2 taught wedge signs and bidegrees; Lesson 5 fixed the top product Ω and zero total basis charge. We now use those exact operations to check what representation labels mean.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Period 1: complements and orientation. Period 2: diagonal action, representations and Witten count.

## C15.06-E1 — Complements retain orientation

The complement of a subset consists of the omitted labels. A bidegree (r,s) therefore maps to (3−r,2−s). Since the total number of labels is five, an even subset complements to an odd subset. Total charge is zero at (a,b)=(−2,3), so the omitted labels' charge is −q. This does not say that odd states have been added to the chosen sixteen-state inventory.

For signs, define the complement C of a positively ordered basis product α to be the signed ordered product of omitted labels such that α∧C(α)=Ω. Extend C linearly to coefficients. To find the sign, concatenate α with its sorted omitted labels and count the swaps to Ω. In five dimensions applying this signed rule twice multiplies by (−1)^(k(5−k)), where k is α's degree: it exchanges blocks of those two lengths. This exponent is always even (one of k and 5−k is even), so C² restores the original expression.

A representation specifies how transformations act on components, not just their number. In a label (3,2), the first entry is color, the second weak. A 1 is a singlet, unchanged by that factor; a 2 is the weak doublet; 3 is the color triplet; bar3 denotes the dual color action. The supplied inventory in census order is (1,1),(1,1),(3,2),(bar3,1),(bar3,1),(1,2).

Here is a concrete explanation of the dual label. Write Ω_C=c1∧c2∧c3. The wedges d1=c2∧c3, d2=−c1∧c3, d3=c1∧c2 obey cj∧di=0 for j≠i and ci∧di=Ω_C. Thus each di pairs with exactly one color label. A diagonal color action multiplies c1,c2,c3 by λ1,λ2,λ3 with product 1. Its action on di multiplies by the product of the other two λ's, equal to 1/λi. This inverse action explains duality. We verify the diagonal case; matching three dimensions alone would not verify this action.

For a hand-checkable phase example, i is a number with i²=−1, so i(−i)=1, 1/i=−i and 1/(−i)=i. The diagonal matrix diag(i,−i,1) simply multiplies c1 by i, c2 by −i and c3 by 1; no matrix multiplication algorithm is hidden here.

## C15.06-W1 — Worked complement and count

Take α=c1∧w1. Its omitted subset is c2,c3,w2. Concatenation c1,w1,c2,c3,w2 needs two swaps, so C(α)=+c2∧c3∧w2. Bidegree changes (1,1)→(2,1); charge changes 1→−2−2+3=−1. The complement is odd degree 3.

The source's Witten test counts weak doublets, not their individual components. Q contains three color copies of a two-component weak doublet. L adds one more doublet. Hence N=3+1=4, remainder 0 mod 2. Eight individual doublet components is a different count; six sectors is yet another count.

## C15.06-P1 — Practice and worked answers

Complement c1∧c2; check C twice. Under diag(i,−i,1), compute the multiplier of c1∧c3 and compare with the inverse c2 multiplier. Finally count weak doublets first in Q alone and then in the full census.

Answers: C(c1∧c2)=c3∧w1∧w2, charge 4 and bidegree (1,2). Concatenating c3,w1,w2,c1,c2 needs six swaps, so applying C again gives +c1∧c2. The multiplier of c1∧c3 is i×1=i, equal to 1/(−i)=i. The dual basis vector d2 has an initial minus sign; it retains that coefficient and receives the same multiplier i. Q alone supplies three doublets, an odd count. Restoring L gives four and remainder zero. Keep the incomplete Q-only trial labeled rather than treating it as the full model.

## Diagnostic checks

1. **C15.06-D1:** List the six representation labels in census order and explain what the bar changes.
2. Find the signed complement of c1∧w2 and its charge.
3. Does complement preserve the selected even sector?
4. Does four weak doublets prove physical chirality or all global anomaly conditions?

Worked answers: (1) (1,1),(1,1),(3,2),(bar3,1),(bar3,1),(1,2); the bar changes the action to the dual, not the dimension. (2) −c2∧c3∧w1, since concatenation requires three swaps. The omitted labels have q=−1; the coefficient minus sign does not alter q. (3) No: it exchanges even and odd sectors. (4) No. Exterior parity counts chosen labels; weak parity here counts doublet copies. Lorentz chirality is a separately specified spacetime property. Detector antipodal parity, A1 carry parity, projective coefficient signs, and family labels are other typed quantities, not substitutes for either count.

> Claim scope: Source KFM-X027 /proof_nodes/79/formula explicitly separates internal parity from Lorentz chirality; KFM-F036 /proof_nodes/83/formula supplies the four-doublet count. The diagonal check illustrates dual action; it is not a fresh proof of every group action. Full non-liftable quotient-bundle global anomaly verification remains separately scoped.

Next dependency: [Lesson 7](lesson-07.md) turns the checks into an appropriately scoped report.
