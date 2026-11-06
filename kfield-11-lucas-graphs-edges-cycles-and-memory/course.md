# Lucas Graphs: Edges, Cycles, and Memory

A first-principles course for high-school seniors. Six lessons, nine core periods, and two capstone periods.

Read the lessons in order; attempt each practice before its answer. Supporting material: [course map](course-map.md), [glossary](terminology.md), [capstone and full key](capstone.md), [teacher guide](teacher-guide.md), and [source notes](sources.md).

<!-- BEGIN: lesson-01 -->
# Lesson 01 — From nodes to a graph

**Essential question:** What information turns a list of locations into a graph?

**Goals:** Draw a path-product graph from its adjacency rule; count vertices and edges without double counting; distinguish open and periodic boundaries.

**Bridge and time:** You can read ordered pairs and triples and multiply small whole numbers. A triple here is a label, not a physical length. Earlier coordinate courses provide useful context, but every graph operation is introduced here. One 55-minute period: retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15 minutes.

## C11.01-E1 — Locations plus allowed steps

A **vertex**, also called a node, is a labeled location. An **edge** connects two vertices. Our graphs initially have undirected edges: either endpoint may be visited first. Vertices joined by an edge are **adjacent**. A walk is a sequence of adjacent vertices; a path is a walk with no repeated vertex. A graph is **connected** when a path joins every pair of vertices. The **degree** of a vertex is its number of incident edges.

The path graph P3 has vertices 0, 1, 2 and edges 0—1 and 1—2. There is no 0—2 edge. P2 similarly has vertices 0,1 joined by one edge. In a Cartesian product of paths, a vertex is a tuple of path labels. Two tuples are adjacent exactly when one coordinate changes by one along its path and all other coordinates stay fixed. The product symbol □ means this adjacency construction, not ordinary multiplication of numbers.

Thus P3 □ P2 has vertices (x,y), where x is 0,1,2 and y is 0,1. Draw it as:

```text
(0,1) ---- (1,1) ---- (2,1)
  |          |          |
(0,0) ---- (1,0) ---- (2,0)
```

The edges stop at the ends: this is an **open** graph. A diagonal is not allowed because two coordinates would change. A jump from 0 to 2 is not allowed because it skips a path edge. The labels alone do not specify these rules; a different edge rule on the same labels would give a different graph.

## C11.01-W1 — Count by direction

The square P2 □ P2 has 2×2=4 vertices, two horizontal edges and two vertical edges, totaling 4. For the diagram above, there are 3×2=6 vertices. Each of two horizontal rows has two edges, giving 2×2=4. Each of three vertical columns has one edge, giving 3×1=3. Total: 7. We count each undirected edge once, by its direction and its lower-coordinate endpoint.

The open Lucas graph is G_L=P3 □ P3 □ P3. Each vertex is (x0,x1,x2) with each coordinate in {0,1,2}. There are 3×3×3=27 vertices. For an axis-0 edge, choose its starting axis-0 value (0 or 1), then freely choose its other two coordinates (three choices each). That gives 2×3×3=18 edges. The same calculation applies to axes 1 and 2, so E=18+18+18=54. Here V and E, when used in numerical formulas, mean the vertex and edge counts.

> **Claim scope:** The Lucas definition and counts are source facts in S02#/backbone_sequence/7/definitions. The counting argument above is a fresh finite derivation. Small diagrams are mathematical teaching examples, not measurements. All coordinates and flows in this course are dimensionless unless an application explicitly supplies units.

## C11.01-P1 — Practice before checking answers

Draw the open 3×3 square. Count its vertices and edges by direction. Then extend the count to 3×3×3. In that cube, count neighbors at a corner, at an edge center, at a face center, and at the center. Finally draw a fresh 3×2 rectangle and label its seven edges.

**Worked answer:** The square has 9 vertices and 2×3+3×2=12 edges. The cube has 27 vertices and 3×2×3×3=54 edges. A coordinate at 0 or 2 permits one step; a coordinate at 1 permits two. Thus (0,0,0) has 1+1+1=3 neighbors; (1,0,0) has 4; (1,1,0) has 5; and (1,1,1) has 6. The rectangle edges are (0,y)—(1,y) and (1,y)—(2,y) for y=0,1, plus (x,0)—(x,1) for x=0,1,2: four plus three.

## Diagnostics

1. **C11.01-D1:** Is (0,1,1)—(2,1,1) an open Lucas edge? Explain.
2. Is (0,0,0)—(1,1,0) an edge? Supply an allowed walk between them.
3. How many axis-2 edges are present? Explain the factors.
4. Does a list of 27 labels determine a graph? Explain what else is needed.

**Worked answers:** 1. No: the change is two, not one. 2. No: two coordinates change. One walk is (0,0,0),(1,0,0),(1,1,0). 3. There are 2×3×3=18; choose the lower axis-2 value and the other two labels. 4. No: an adjacency rule or edge list is also needed.

**Next dependency:** [Lesson 02](lesson-02.md) puts signs on edges and builds a table that measures net arrival at each node.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 02 — Walking, connectivity, and incidence

**Essential question:** How can a table encode the signed effect of every edge on every vertex?

**Goals:** Build an oriented incidence matrix; multiply it by a flow list; establish a small matrix's rank by elimination; keep node and edge objects distinct.

**Bridge and time:** Lesson 01 supplied edges and vertices. We now use signed arithmetic to record an arrival as positive and a departure as negative. Two 55-minute periods, each with 5 retrieval, 20 explanation/example, 15 practice and 15 diagnostics/repair minutes. Period A covers the table and multiplication; period B covers rank and orientation changes.

## C11.02-E1 — From arrows to columns

Choose an arrow on each undirected edge. This **orientation** is a reference direction, not a restriction on travel. The arrow starts at its **tail** and ends at its **head**. A signed flow coordinate f_e is positive along that arrow and negative against it. A column vector is simply an ordered list written vertically; subscripts identify entries.

The **incidence matrix D** is a rectangular table. Rows follow the declared vertex order; columns follow the declared edge order. For an edge, enter −1 in its tail row, +1 in its head row, and zero elsewhere. To compute Df, multiply each column by its flow coordinate and add the results row by row. The result is the node list of arrivals minus departures. We call it **divergence** in this course, with this explicit sign convention. Some applications choose the opposite convention.

A **node field** assigns one value to each node; an **edge field** assigns one to each oriented edge. These are different types of information even when their list lengths happen to match. Each incidence column sums to zero, so Df always sums to zero: each edge contributes equally and oppositely at its endpoints.

The **rank** of a matrix is the number of independent columns needed to generate all its columns by scaling and adding. Independent means no combination of those columns equals zero unless every coefficient is zero. To test independence, set the combination equal to zero and solve its row equations. Elimination means using one equation to find a coefficient, then substituting it into another. You already do this when solving simultaneous linear equations.

## C11.02-W1 — A triangle, computed completely

Use nodes 0,1,2 and edges 01,12,20, where 01 means 0→1. This triangle is a teaching graph, not a path-product subgraph. Its incidence matrix is

```text
       01 12 20
node0  -1  0  1
node1   1 -1  0
node2   0  1 -1
```

For f=(2,3,4), the first row gives −2+4=2, the second gives 2−3=−1, and the third gives 3−4=−1. Thus Df=(2,−1,−1), whose entries sum to zero. Notice that zero total does not mean zero at every node.

Call the columns a,b,c. Their sum is zero, so c=−a−b. To test a and b, suppose sa+tb=0. Row 0 says −s=0, so s=0. Row 1 then says s−t=0, hence t=0. These two columns are independent, and the third adds no new freedom. Rank is therefore 2.

The **transpose Dᵀ** swaps rows and columns. Applied to a node potential φ (a node value list), it produces the edge list whose entry is φ_head−φ_tail. This is a gradient or edge-difference field. Lesson 03 uses it.

> **Claim scope:** These exact tables use our declared ordering and sign convention. Choosing arrows differently changes the coordinates but not the underlying graph. This is finite linear algebra; no physical transport mechanism is assumed. S02#/backbone_sequence/7/proof/0 supplies the connected-graph rank statement which Lesson 04 will derive.

## C11.02-P1 — Square table and independent practice

Draw the square with nodes 0 bottom left, 1 bottom right, 2 top right, 3 top left. Orient its edges 01,12,23,30 around the boundary, in that order. Build D, compute D(2,3,4,5), and establish rank by solving column equations. Then reverse edge 01 and find the new flow list representing the same signed flow. Finally find Dᵀφ for φ=(0,1,3,2).

**Worked answer:** The ordered table is

```text
        01 12 23 30
node0   -1  0  0  1
node1    1 -1  0  0
node2    0  1 -1  0
node3    0  0  1 -1
```

Row calculations are −2+5=3, 2−3=−1, 3−4=−1, 4−5=−1. The fourth column is the negative sum of the first three. In sa+tb+uc=0, row 0 yields s=0, row 1 then t=0, and row 2 then u=0. Hence rank is 3. Reversing 01 negates column 01 and changes its flow to −2, so the list is (−2,3,4,5). The product of column and coordinate is unchanged. The potential differences are (1−0,3−1,2−3,0−2)=(1,2,−1,−2).

## Diagnostics

1. **C11.02-D1:** Reverse one arrow but keep its nonzero coordinate unchanged. Does the represented flow stay the same? What fixes it?
2. For the square, what are the input and output types of D and Dᵀ?
3. Compute D(1,1,1,1). Does its value imply rank zero?
4. Why can a square incidence matrix with four columns have rank only three?

**Worked answers:** 1. No. Negate both the column and the coordinate. 2. D sends four edge entries to four node divergences; Dᵀ sends four node potentials to four edge differences. Equal lengths do not identify their types. 3. Every row gives −1+1=0. Rank is still 3; one input being sent to zero does not make every column zero. 4. The fourth column equals minus the other three, while elimination proves the first three independent.

**Next dependency:** [Lesson 03](lesson-03.md) uses Df=0 to identify circulations and compares them with potential differences.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
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
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 05 — Adding periodic wrap edges

**Essential question:** How can 27 new cycle values be preserved as 24 details and three winding sums?

**Goals:** Count periodic edges and cycles; separate wrap sums from details; invert the coordinate change exactly; reconstruct a circulation in the declared basis.

**Bridge and time:** Lesson 04 supplied the open tree, ordered chords and the basis decoder. Keep that tree throughout this lesson. Two 55-minute periods with 5 retrieval, 20 teaching/example, 15 practice and 15 diagnostics/repair minutes each. Period A adds wraps and counts; period B decodes details and reconstructs.

## C11.05-E1 — Add edges without losing coordinates

For each axis line, add one **wrap edge** from coordinate 2 to coordinate 0, keeping its other coordinates fixed. It closes that three-node line into a ring. These edges connect existing vertices; they do not add vertices. There are 3×3=9 lines per axis and three axes, so 27 new edges. Retain the open tree from Lesson 04. All new edges are chords relative to that tree, and each gets a fundamental cycle using the same head-to-tail tree path rule.

Order all open edges as before, then wrap edges by axis and lexicographic tail. For axis 0 their tails are (2,0,0),(2,0,1),(2,0,2),(2,1,0),(2,1,1),(2,1,2),(2,2,0),(2,2,1),(2,2,2). The analogous rule orders axes 1 and 2. Let c_i, i=1,…,28, name the open fundamental cycles. Let h_(a,j), a=0,1,2 and j=1,…,9, name the wrap fundamental cycles. Subscripts are labels, not multiplication. Each h has +1 on its own wrap edge and only tree edges elsewhere.

A periodic circulation is reconstructed by multiplying and adding:

f = Σ_i q_i c_i + Σ_a Σ_j w_(a,j) h_(a,j).

The symbol Σ means “sum over the listed index values.” The 28 numbers q_i are read at open chords, and the 27 numbers w_(a,j) at wrap chords. We retain all of them. The open cycles are local in the sense of having no seam crossing; they need not each be a single small face.

For one axis suppress the axis label and write w=(w1,…,w9). Define its **winding coordinate** W=w1+…+w9, its mean μ=W/9, and details d_j=w_j−μ. The details sum to W−9μ=0. Hence only the first eight details are free; d9=−(d1+…+d8). The inverse rule is w_j=W/9+d_j for every j. The sum and the mean differ by a factor of nine.

Why call W a winding? With the chosen seam, it is the net signed wrap crossing on that axis. For a closed route on the periodic graph, this counts net passages through the seam; a sum of weighted cycles gives the corresponding weighted coordinate. Zero-sum changes among the nine seam entries can rearrange crossings without changing W. Such changes are retained in the eight details. Winding alone therefore cannot recover the distribution among lines.

## C11.05-W1 — Count, transform, reconstruct

The periodic graph has 54+27=81 edges and the same 27 vertices. It remains connected. Rank is still 26, so cycle dimension is 81−26=55. Each axis contributes eight free details and one winding, so

55 = 28 + 3×8 + 3 = 28 + 24 + 3 = 52 + 3.

For axis 0 choose synthetic coefficients w=(1,2,3,4,5,6,7,8,9). Their sum is 45, mean 5, and details are (−4,−3,−2,−1,0,1,2,3,4). The first eight sum to −4, so the ninth is +4. Add 5 to each detail to recover the original list. With all open coefficients and other-axis wrap coefficients zero, the entire circulation is h_(0,1)+2h_(0,2)+…+9h_(0,9). This specifies all 81 edge entries by the declared signed paths, including tree entries; it is not just a list of seam values.

> **Claim scope:** S02#/backbone_sequence/7/periodic_augmentation reports 28+24+3; the coordinate construction here makes that split explicit. S02#/backbone_sequence/18/branches/exceptional_cycle_bridge separately lists exceptional-action extensions. The equality 52=28+24 does not construct an F4 action, a force or a dynamical law. The present change of coordinates is over real or rational numbers. For integer w, details can be fractional; their allowed values must satisfy W/9+d_j being an integer, including the dependent ninth value. No free integer product decomposition is asserted.

## C11.05-P1 — A concentrated seam state

Use w=(0,0,0,0,0,0,0,0,9) on axis 0, zeros on other axes and all 28 open coefficients zero. Find W, the mean, eight independent details, the ninth detail, and all reconstructed coefficients. Write the resulting circulation in the basis. Then repeat the periodic edge/rank/cycle count. As an integer check, transform w=(1,0,0,0,0,0,0,0,0).

**Worked answer:** W=9, μ=1, d1,…,d8=−1; d9=−(−8)=8. Reconstructing gives eight zeros and 1+8=9. Other coefficients remain zero, so f=9h_(0,9). Its wrap edge runs (2,2,2)→(0,2,2); its tree return path is (0,2,2)→(1,2,2)→(2,2,2), both increasing axis 0. Thus these three edge entries are 9 and all others zero. Counts are 81 edges, rank 26, cycles 55. For the integer check W=1, μ=1/9; d1=8/9 and d2,…,d9=−1/9. Every μ+d_j is integral even though each detail is fractional. Retaining W and eight details recovers the ninth and the entire original list.

## Diagnostics

1. **C11.05-D1:** If W=9, is the mean 9? Explain the integer compatibility issue as well.
2. Why are there only eight free details per axis?
3. What is lost by keeping only the three winding sums? How do we avoid losing it?
4. If all W values are zero, must the circulation be zero?

**Worked answers:** 1. The mean is 9/9=1. With integer source coefficients each reconstructed W/9+d_j must be integral; arbitrary integer choices of W and details need not satisfy this. 2. The zero-sum equation fixes the ninth as minus the first eight. 3. The 24 wrap-distribution details and 28 open-cycle coordinates are not specified by W; retain them and the basis. 4. No. An open fundamental cycle has zero winding, and nonzero opposite wrap details can also sum to zero.

**Next dependency:** [Lesson 06](lesson-06.md) asks exactly which state these coordinates preserve, especially when the original edge field does not balance.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 06 — Memory needs a specified state

**Essential question:** What must be retained to recover a flow exactly?

**Goals:** Decode a specified cycle state; separate a general flow into cycle coefficients and a retained tree remainder; explain why coordinate counts do not determine dynamics.

**Bridge and time:** Lessons 03–05 gave cycle bases and their decoders. We now apply subtraction without discarding the information it removes. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice and 15 diagnostics/repair minutes.

## C11.06-E1 — A reversible representation

In this course **memory** means a specified retained state together with a decoder that recovers it. This is an operational information definition. To specify a cycle state, retain the graph, edge order, orientations, tree, cycle basis and coefficients. The basis tells you how each coefficient affects the edges. A verified circulation needs only those cycle coefficients once the conventions are fixed.

A general edge flow f may not satisfy Df=0. Read each chord value q_i and form the circulation s=Σ_i q_i c_i. Define the **tree remainder** r=f−s. On every chord, subtraction removes the same q_i, so r is supported on tree edges. Keep r as a primary coordinate, rather than calling it error and erasing it. The inverse is f=s+r. Moreover Dr=Df−Ds=Df because Ds=0. Thus r retains the complete divergence information. If f was a circulation, Dr=0 and tree elimination forces r=0. Otherwise the remainder may be nonzero and is essential.

This particular decomposition is determined by chord readings. It is not in general an orthogonal split into a gradient and a cycle. A tree-supported remainder need not be a gradient on the full graph. Do not confuse the 26-dimensional cut space with every possible 26-coordinate complement to cycles. Our tree remainder is selected because its inverse is easy to teach and audit.

For the periodic graph, retain 28 open-cycle coefficients, 24 independent wrap details, 3 windings, and, for a general flow, the 26 tree-remainder values. The decoder reconstructs the 27 wrap coefficients, forms the 55-cycle sum, then adds the remainder. There are 55+26=81 independent real coordinates, matching the 81 edge values. Zero entries remain entries; signs and ordering remain part of the state.

A **dynamics** or update rule says how a state changes with time. A graph and its dimension do not select that rule. For example, a synthetic device could use q(t+1)=q(t), preserving a coordinate, or q(t+1)=2q(t), doubling it each step. Both rules use the same one-dimensional state. They predict different histories. To claim a physical memory lifetime we would need a specified physical state, update or retention mechanism, and observations over time. Those are unresolved by the dimension count itself.

## C11.06-W1 — Triangle reconstruction

Use the triangle tree 01,12 and chord 20 with c=(1,1,1). For f=(2,3,4), the chord value is q=4. Its cycle contribution is 4c=(4,4,4). Subtract entry by entry: r=(2−4,3−4,4−4)=(−2,−1,0). Then 4c+r=(2,3,4), exactly. The remainder's divergence is (2,−1,−1), the same as Df. If we retained only q=4, we would decode (4,4,4) and lose the two nonzero tree values and their imbalance. The remainder is information about this chosen flow, not a disposable defect.

> **Claim scope:** The examples are exact synthetic states, not measurements of a memory device. Source M08 names memory spaces, while the finite mathematics establishes coordinate capacity and decoding. Memory duration, forces and exceptional-group actions require further defined structure. The source-reported serialization gap AUD-002 remains separate from these finite checks.

## C11.06-P1 — Square reconstruction and scope

For the square ordered 01,12,23,30, use tree 01,12,23 and c=(1,1,1,1). Starting with f=(2,3,4,5), find q and r, reconstruct f and compare Dr with Df. Repeat for f=3c. State the metadata needed to interpret q. Finally compare q(t+1)=q(t) with q(t+1)=2q(t), starting at q(0)=3 for two updates.

**Worked answer:** q=5, 5c=(5,5,5,5), r=(−3,−2,−1,0). Adding gives (2,3,4,5). Dr=(3,−1,−1,−1)=Df. For 3c, q=3 and r=0, so q alone with the conventions recovers the flow. Required metadata include graph, edge order, orientations, tree and cycle basis. The first update rule gives 3,3,3 at times 0,1,2; the second gives 3,6,12. Identical dimension does not determine change through time.

## Diagnostics

1. **C11.06-D1:** What does a dimension count say about memory duration? Name what would be needed to say more.
2. Two square flows are (2,3,4,5) and (5,5,5,5). They share q=5. How can the stored representation distinguish them?
3. In the periodic graph, what data recover a general edge field?
4. When may the tree remainder be omitted from a circulation encoding without losing a value?

**Worked answers:** 1. It supplies no duration. Need a physical state, an update/retention mechanism and time observations. 2. Retain r=(−3,−2,−1,0) for the first and r=0 for the second. 3. Keep basis metadata, 28 open coefficients, 24 wrap details, 3 windings and 26 tree values; reconstruct wrap values, sum cycles, and add r. 4. After verifying Df=0 and applying the declared chord/tree decomposition, the tree remainder is provably zero. Recording that verification justifies its implicit zero value.

**Next dependency:** The [capstone](capstone.md) uses this entire chain to audit counts and reconstruct supplied states without dropping any coordinates.
<!-- END: lesson-06 -->
