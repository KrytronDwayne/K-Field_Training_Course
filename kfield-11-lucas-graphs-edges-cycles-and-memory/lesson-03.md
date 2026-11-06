# Lesson 03 — Cuts and cycles

**Essential question:** What can circulate without changing the net amount at any node?

**Goals:** Verify a circulation with D; construct a fundamental cycle from a tree and chord; compute a gradient and its dot product with a cycle; decode a cycle coefficient.

**Bridge and time:** Lesson 02 taught incidence, row multiplication, transpose and independence. Two 55-minute periods use 5/20/15/15 minutes each for retrieval, teaching/example, practice and diagnostics/repair. Period A treats trees and cycles; period B treats gradients, cuts and decoding.

## C11.03-E1 — Keep an edge route and its coefficients

A simple cycle is a closed route with no repeated vertex apart from its start/end. A signed edge field f is a **circulation** if Df=0: each node balances. Sums and scalar multiples of circulations also balance, because multiplication distributes over addition. The set of all such fields is the **cycle space**. A cycle vector records +1 for following an edge arrow, −1 for traversing it backwards, and 0 for not using it.

A **tree** is a connected graph with no cycle. A **spanning tree** uses every vertex of a graph but only enough edges to connect them without a cycle. Any edge outside the tree is called a **chord**. Adding a chord produces one **fundamental cycle**: follow the chord from its tail to its head, then return along the unique tree path from head to tail. Record the signs relative to the fixed edge arrows. Choose coefficient +1 on the chord itself. This choice is a reproducible basis convention, not a property of a drawing.

Why is the tree path unique? Two different simple paths between the same endpoints would enclose a cycle, contradicting the tree definition. A tree with more than one vertex has a **leaf**, a node with only one tree edge: follow a nonrepeating path as far as possible, and its endpoint cannot have another unused neighbor. A circulation supported only on a tree must be zero. At a leaf, its sole edge must carry zero to balance that leaf. Remove that edge and leaf and repeat. Eventually every edge is zero. This is leaf elimination.

A **cut** separates vertices into a chosen set S and its complement; its cut edges connect the two sets. Assign potential 1 to nodes in S and 0 elsewhere. The edge differences Dᵀφ are zero off the cut and ±1 on its edges. The **cut space** here means all real linear combinations of such signed cut fields, equivalently all gradients Dᵀφ. To see the equivalence, express any potential as a sum of single-node indicator fields multiplied by their node values.

The **dot product** of two equally ordered lists means multiply matching entries and add: (a,b)·(u,v)=au+bv. A cycle and a gradient have zero dot product. Along a closed route, the differences φ_head−φ_tail telescope: each visited potential appears once with each sign. Algebraically, summing by nodes gives (Dᵀφ)·c=φ·(Dc)=0. We call zero dot product **orthogonality**; it is a statement about these coordinates.

## C11.03-W1 — Triangle balance and potential

Use Lesson 02's triangle, tree edges 01,12, and chord 20. Follow 2→0, then tree path 0→1→2. All steps follow the listed arrows, so c=(1,1,1). The three rows of Dc give −1+1, 1−1 and 1−1: all zero. For potential φ=(2,5,7), Dᵀφ=(5−2,7−5,2−7)=(3,2,−5). Its dot product with c is 3+2−5=0.

The circulation 4c=(4,4,4) has one independent number, 4. Read that number on the chord 20; multiplying c by it reconstructs every edge. If we chose −c as the cycle orientation, the same circulation would have coefficient −4. A coefficient without its basis and orientation is incomplete information.

> **Claim scope:** All examples are synthetic exact states. “Cut space” and “cycle space” are finite real vector spaces, not physical storage claims. This lesson supplies the mathematical bridge to the two dimensions reported in S02#/backbone_sequence/7/proof/1.

## C11.03-P1 — Square cycle and decoder

Use the square ordered 01,12,23,30, tree 01,12,23 and chord 30. Construct c, verify Dc, compute the gradient of (0,1,3,2), and verify orthogonality. Decode 3c. Express the same 3c using basis −c and verify reconstruction. Finally test whether f=(2,3,4,5) is a circulation.

**Worked answer:** The return path for 3→0 is 0→1→2→3, so c=(1,1,1,1). Each row of Dc is zero. The gradient is (1,2,−1,−2); dotting with c gives 1+2−1−2=0. The chord entry of 3c is 3, and 3c=(3,3,3,3). In basis −c=(−1,−1,−1,−1), the coefficient is −3: multiplying gives (−3)(−c)=(3,3,3,3), the same state. For the last flow Df=(3,−1,−1,−1), so it is not a circulation. A general flow may contain circulating information without itself balancing.

## Diagnostics

1. **C11.03-D1:** A square node potential and a square circulation both have four entries. Are they the same kind of object? Explain their decoders.
2. Why is (1,1,1,0) not a circulation on the ordered square?
3. If c is replaced by −c, what coefficient represents 3c?
4. Can a nonzero circulation exist on a tree? Give the elimination argument.

**Worked answers:** 1. No. Node entries are attached to vertices; cycle entries to ordered oriented edges. A cycle coefficient also needs its declared basis to decode. 2. D gives (−1,0,0,1), so the two endpoints fail balance. 3. −3, because (−3)(−c)=3c. 4. No: balance forces the sole edge at each leaf to zero, and repeating removes all edges.

**Next dependency:** [Lesson 04](lesson-04.md) counts independent cut and cycle coordinates using tree elimination rather than a memorized formula.
