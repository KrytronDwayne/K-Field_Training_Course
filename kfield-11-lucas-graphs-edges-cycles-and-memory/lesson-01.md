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
