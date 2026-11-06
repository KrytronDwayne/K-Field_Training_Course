# Lesson 04 — The 26 and 28 dimensions

**Essential question:** Why do 54 edge values divide into 26 cut dimensions and 28 cycle dimensions?

**Goals:** Derive connected incidence rank from a spanning tree; derive cycle dimension from chords; specify a reproducible Lucas tree and cycle decoder.

**Bridge and time:** Lessons 02–03 taught independence, gradients, chords and leaf elimination. Here **dimension** means the number of independent scalar coordinates required, not a spatial direction. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice, 15 diagnostics/repair minutes.

## C11.04-E1 — Derive the counts

A tree on V vertices has V−1 edges. One way to see this is to remove a leaf with its single edge repeatedly until one vertex and no edges remain. Each removal reduces both counts by one. A connected graph has a spanning tree: start at one node and attach a new node by an edge from the reached set until all nodes are reached. Such an edge exists at every stage because the graph is connected; attaching a new vertex cannot create a cycle.

The tree's incidence columns are independent. If a combination of those columns is zero, it describes a circulation supported on the tree; leaf elimination forces all coefficients to zero. Thus rank is at least V−1. All incidence columns have coordinate sum zero, and a node list with sum zero is determined by its first V−1 values, since its last value is their negative sum. Rank can be no larger than V−1. Therefore connected incidence rank is exactly V−1.

Cut dimension is also V−1. Choose a root and subtract its potential value from every node potential; this makes the root potential zero without changing any edge difference. The remaining V−1 potentials can vary freely. Distinct rooted potential lists give distinct gradients: if all edge differences of their difference are zero, connectivity forces the potential difference constant, and root zero forces that constant zero. This proves the cut count directly without assuming a theorem about matrix transposes. If absolute potentials matter, retain the root value as well; removing a constant for gradient coordinates is not permission to erase physical state.

There are E−(V−1) chords. Give each chord its own fundamental cycle, coefficient +1 on that chord and signed tree entries on the return path. No other chord appears in that cycle. Consequently these cycle columns are independent: in a combination that vanishes, inspecting each chord forces its coefficient to zero. They also generate every circulation f. Subtract f's chord entry times each corresponding cycle. The remainder has no chord entries and still balances; it is a tree circulation, hence zero. So there are exactly E−V+1 independent cycle coordinates. A **basis** is an independent list that generates every field in the specified space.

For reproducibility, order Lucas vertices lexicographically: compare x0 first, then x1, then x2; the first few are (0,0,0),(0,0,1),(0,0,2),(0,1,0). Open edges point in increasing coordinate. Order them by axis 0,1,2, and within each axis by lexicographic tail. Root at (0,0,0). Each other vertex has one parent: decrement its first nonzero coordinate. The tree edge runs from that parent to the vertex. Repeated parent steps lower x0+x1+x2 until reaching zero, so every vertex connects to the root. There are 26 distinct parent edges, hence a spanning tree. Keep all non-tree edges in inherited edge order as chords. These conventions specify the complete cycle basis without printing 54×28 entries.

## C11.04-W1 — Rectangle first, then Lucas

For the open 3×2 rectangle, V=6 and E=7. Root (0,0) with the same first-nonzero parent rule. Its five tree edges are the four horizontal edges and (0,0)→(0,1). Its chords are (1,0)→(1,1) and (2,0)→(2,1). The first chord's return tree path is (1,1)→(0,1)→(0,0)→(1,0), with signs −,−,+ relative to increasing coordinates. Together with chord sign + this closes the cycle. Rank is 5, cycle dimension 7−5=2. One cycle per chord gives a basis even though the second fundamental cycle surrounds both small squares.

For Lucas, V=27 and E=54. The declared parent tree has 26 edges. Incidence rank and cut dimension are 26; the remaining 54−26=28 edges are chords, so cycle dimension is 28. For example, parent(1,2,1)=(0,2,1), then parent(0,2,1)=(0,1,1), then (0,0,1), then root. The construction is concrete enough to reproduce, not merely a count.

> **Claim scope:** These are freshly derived graph dimensions, agreeing with S02#/backbone_sequence/7/proof/0 and /proof/1. “28 coordinates” describes how many values a circulation needs after a basis is declared. It supplies neither the values nor an evolution law. The mature backbone's M08 is not automatically compiler module M08 in a different integration.

## C11.04-P1 — Reuse the proof

Count a 3×3 open square's tree edges, rank and cycles. Explain why its chord cycles are independent and generate all circulations. Then repeat the argument for Lucas, state its parent rule, find parent(0,1,2), and explain how to recover every cycle coefficient from a circulation. Construct the second rectangle chord cycle as further signed-path practice.

**Worked answer:** V=9,E=12, tree edges=8, rank=8, cycles=12−8=4. Each chord cycle has its own unique +1 chord entry, proving independence. Subtraction of those entries times cycles leaves a zero tree circulation, proving generation. Lucas gives V=27,E=54, tree=26, rank=26, cycles=28 by the same argument. Decrement the first nonzero coordinate, so parent(0,1,2)=(0,0,2). Read coefficients directly at the ordered chord entries. The second rectangle cycle follows (2,0)→(2,1) on the chord, then (2,1)→(1,1)→(0,1)→(0,0)→(1,0)→(2,0), with return signs −,−,−,+,+.

## Diagnostics

1. **C11.04-D1:** Does “cycle dimension 28” determine a Lucas circulation? What is missing?
2. Why does one chord cycle not use another chord?
3. Is connectivity optional in rank=V−1? Test two isolated nodes.
4. Why can the 28 cycle columns not satisfy a nontrivial zero combination?

**Worked answers:** 1. No: need 28 values, the ordered basis, and orientations. 2. Its closing path lies wholly in the tree. 3. No: two isolated nodes have no columns and rank 0, not 1. 4. Each chord row exposes exactly its own coefficient, forcing that coefficient zero.

**Next dependency:** [Lesson 05](lesson-05.md) keeps this same tree while adding periodic edges and decoding their additional information.
