# Lesson 04 — Cycle counts and exceptional dimensions

**Essential question:** What can a finite count establish, and what additional structure is needed to turn that count into an algebraic action?

**Goals.** By the end, you can (1) count vertices and edges under an explicit boundary rule, (2) derive and use the connected-graph cycle formula, and (3) separate a recomputed count from an attributed theorem and an unconstructed extension.

**Prerequisite bridge.** Lesson 03 separated a directional calculation from an added response law. Here the same discipline applies to counting: a number is a result of specified operations, while an action also requires rules for transforming objects. We need only whole-number arithmetic and coordinate triples. Every count below is dimensionless; no laboratory measurement is represented.

**Time:** two 55-minute periods. Each uses 5 minutes of retrieval, 20 of explanation/worked calculation, 15 of practice, and 15 of diagnostics and repair. Period 1 covers graph enumeration; period 2 covers source theorem cards and the boundary of dimension comparisons.

## C23.04-E1 — Build the object before counting it

A **graph** consists of vertices (points) and edges (links). Our edges are undirected: a link from A to B is the same link as one from B to A. A **path** follows edges. A graph is **connected** when every vertex can be reached from any other. A **cycle** is a closed route without repeated vertices except its starting/ending vertex. A picture can contain many cycles even though only a smaller number are independent.

Begin with three points labeled 0, 1, 2 on a line, linked by 0—1 and 1—2. Call this graph P3. An open three-dimensional grid has vertices (i,j,k), where each coordinate is 0, 1, or 2. An edge changes just one coordinate between 0 and 1 or between 1 and 2, leaving the others fixed. For example, (0,1,2) links to (1,1,2), but not to (1,2,2): that latter change alters two coordinates. “Open” means 0 and 2 are not directly linked along a coordinate line.

A **spanning tree** connects all vertices without cycles. You can build one by starting at a single vertex and adding an edge to one previously unreached vertex at each step. Each step adds one vertex and one edge. Reaching V vertices therefore uses V−1 edges. Because the tree has no cycles, there is exactly one path within it between any two vertices; two distinct paths would create a cycle.

Now restore an edge omitted from the tree. Its endpoints already have a tree path, so the new edge closes one cycle. Each omitted edge gives a cycle containing that particular omitted edge and no other omitted edge. Thus none of these cycles can be built from the others. They generate all cycle patterns: remove an arbitrary closed pattern's non-tree edges using these cycles, and no cycle can remain entirely inside a tree. This establishes the **cycle dimension**

\[
\text{cycle dimension}=E-(V-1)=E-V+1
\]

for a finite connected graph with E edges and V vertices. More precisely, we can describe a cycle pattern by marking edges 0 or 1, combining patterns by addition modulo 2: an edge used twice cancels. The dimension counts independent choices in this description, not the number of all distinct closed routes. This elementary convention is sufficient for our finite counts. Other coefficient conventions must be declared when comparing with a source's richer construction.

For a **periodic** grid, add the wrap edge 2—0 on every coordinate line. We retain one undirected edge per pair on that line. With three points, each line becomes a triangle with three edges. We are not adding separate copies for clockwise and counterclockwise travel. Open and periodic grids are different graphs and must remain separate entries in the record.

## C23.04-W1 — Recompute the three-dimensional counts

There are three choices for each of three coordinates, so V=3×3×3=27. To count open edges in the i direction, choose j and k in 3×3=9 ways; each resulting line has two edges. This gives 18 edges. The j and k directions contribute 18 each, with no overlap because an edge changes only one coordinate. Hence E=54 and cycle dimension 54−27+1=28.

For the periodic version, each of those nine lines per direction has three edges. Therefore E=3×9×3=81, and cycle dimension 81−27+1=55. Periodic augmentation adds 81−54=27 edges without adding vertices, increasing cycle dimension by 27. Independently check the arithmetic by starting from the cycle dimensions: 55−28=27.

| Graph | V | E | E−V+1 |
|---|---:|---:|---:|
| Open P3 × P3 × P3 | 27 | 54 | 28 |
| Periodic three-coordinate grid | 27 | 81 | 55 |

S02's M19 branch records the additional decomposition 27=24+3 and the sector count 55=52+3, describing 52 zero-sum/open-cycle coordinates and 3 global windings. A winding records going around a periodic direction. The arithmetic 52+3=55 checks, but choosing the actual 52-coordinate sector and its relation to the winding coordinates needs a specified map or basis. Our enumeration does not construct that map. Preserve both the directly checked totals and the source's more structured statement.

## Source theorem cards — recognition only

The following cards are attributed to **S02, `/backbone_sequence/18/branches/exceptional_cycle_bridge/exact_counts`**. Their proof bodies are not supplied in that short source entry and are not reconstructed by this lesson. Students identify their status and perform only the explicitly taught arithmetic.

| Source card | Meaning sufficient for this course | Boundary |
|---|---|---|
| dim H²((Z3)³,Z3)=6, giving 729 classes | Z3 denotes three labels with arithmetic modulo 3; H² labels a cohomology classification space. Given six independent three-way coordinates, the number of assignments is 3⁶. | We use the dimension theorem; we do not prove it by grid counting or define physical coupling from it. |
| The stabilizer of one octonion unit is SU(3) | A stabilizer is a collection of transformations preserving the specified object; SU(3) is the source's named symmetry structure. | The exact octonion-unit convention and theorem hypotheses require the fuller theorem. This is not a claim about any arbitrarily chosen unit. |
| The Euclidean Albert algebra supplies compact F4 | The source names an algebraic carrier and a compact symmetry structure. | This does not furnish an F4 action on the particular 52-cycle sector. |

Names F4, E6, and E7 identify exceptional algebraic structures. The often-compared dimension labels 52, 78, and 133 are recognition labels in this course, not a construction of their operators. The supplied M19 entry identifies E6/E7 real-form selection as an extension; it does not provide a 78- or 133-dimensional graph construction to verify here. A **real form** specifies a real-number version of a broader algebraic structure. Selecting one requires a contract beyond naming its dimension.

> **Claim scope.** The finite grid counts above are fresh deductions from declared graph rules. Cohomology and exceptional-algebra statements remain source/theorem cards. The specific F4 cycle action, E6/E7 real forms, and physical coupling of cohomology classes remain extension obligations. M19 is a mixed branch, not a premise of M20 core closure (S03 `/findings/0`, AUD-001). A null endpoint cannot cancel a constituent limitation (S03 `/findings/9`, AUD-010).

## C23.04-P1 — Guided practice before assessment

Build an open two-dimensional 3×3 grid with vertices (i,j). Count V, horizontal edges, vertical edges, E, and cycle dimension. Then add wrap edges and repeat. Finally, using the supplied six-coordinate cohomology theorem, count the classes. State exactly which part of your answer is conditional on a source theorem.

**Worked practice answer.** V=3×3=9. Three horizontal lines each contain two edges, giving 6, and three vertical lines give another 6. Thus E=12 and cycle dimension 12−9+1=4. Periodic lines each have three edges: E=9+9=18 and cycle dimension 18−9+1=10. The increase is six, equal to the six added wrap edges. For six independent coordinates with three choices each, repeated multiplication gives 3×3×3×3×3×3=729. The multiplication is verified here; the premise that this cohomology space has six independent coordinates is the attributed theorem.

## C23.04-D1 — Diagnostic checks

1. A connected graph has 8 vertices and 11 edges. Find its cycle dimension and explain the subtraction.
2. In the open three-dimensional grid, why is E not 27×6?
3. A table lists 52 cycle coordinates and dimension 52 for F4. What has the table supplied, and what is still needed?
4. Does 3⁶=729 prove the cohomology dimension is six? What record should retain the missing proof?

**Worked answers.** (1) A spanning tree has 8−1=7 edges, leaving 11−7=4 independent cycle choices. (2) Boundary vertices have fewer than six neighbors, and counting every link from each end double-counts it. Counting the coordinate lines gives 54 exactly. (3) It supplies a dimension match. One still needs the cycle sector, field, basis, operators, preserved algebraic relations, and a map connecting the claimed actions; Lesson 05 teaches a small version. (4) No: it computes the consequence of a given dimension. The source card must retain the theorem attribution, pointer, and proof-body retrieval gap rather than replace them with an arithmetic check.

**Next dependency:** [Lesson 05 — An action needs more than a matching dimension](lesson-05.md) turns a dimension comparison into a concrete map test.
