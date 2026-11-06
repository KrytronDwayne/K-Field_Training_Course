# Lesson 01 — One subdivision at a time

**Essential question:** How can a rule name every piece without confusing pieces with boundaries?

**Goals:** Generate a binary tree; find parents; distinguish nodes, boundary vertices, and volumes.

**Bridge:** You can compare fractions and plot coordinates. Course 05 introduced cells and Lucas windows; the needed definitions are restated here. **Pacing:** explanation/examples 20, practice 15, checks/feedback 15, transition 5 minutes.

## C06.01-E1 — A repeated rule

A recursion repeats an operation on its output. The starting object is the root at depth zero. A child results from one application; its parent produced it. Depth counts applications. Start with the synthetic interval [0,1). A square bracket includes an endpoint; a round bracket excludes it. Splitting at the midpoint gives [0,1/2) and [1/2,1). Only the right child owns 1/2. Endpoint 1 remains a geometric boundary vertex even though no interval owns it.

At dyadic depth n2, each interval has width 1/2^n2. Index intervals left to right by j=0 through 2^n2−1. Interval j is [j/2^n2,(j+1)/2^n2). Parent k produces children 2k and 2k+1. Conversely parent(j)=floor(j/2), where floor means greatest integer at or below the number. Thus floor(5/2)=2. Here indices are nonnegative.

## C06.01-W1 — Worked tree

| Depth n2 | Indices and intervals | Parent indices |
|---|---|---|
| 0 | 0: [0,1) | none |
| 1 | 0: [0,1/2); 1: [1/2,1) | 0,0 |
| 2 | 0: [0,1/4); 1: [1/4,1/2); 2: [1/2,3/4); 3: [3/4,1) | 0,0,1,1 |

Index 3 is child 2(1)+1 of parent 1. Four widths of 1/4 total 1. Their distinct boundary vertices are 0,1/4,1/2,3/4,1: five, not eight. Eight counts cell–endpoint incidences (pairings), counting shared ends twice.

## C06.01-E2 and C06.01-W2 — Count the object you named

A basis B specifies three independent edge directions and lengths. Outer basis 3B triples each edge. A node is a sampled point; a complete cell volume is a region. In the source Lucas window, each axis has half-step positions −1/2,0,1/2. Independently choosing three coordinates gives 3×3×3=27 nodes. A Lucas Group instead contains three complete Cell3 cells per axis, hence 27 volumes and outer basis 3B.

Draw a row as `|---o---|---o---|---o---|`: three cell centers o, four boundary corners |. The drawing is schematic. A 9B Supergroup has nine complete cells per axis: 9×9×9=729 volumes. Equivalently it has 3×3×3=27 Groups, each with 27 cells. Counts are dimensionless; a measured volume would carry cubic length units.

> **Scope:** S02 /backbone_sequence/2/typed_finite_objects defines the three objects. The interval is synthetic. Finite counting derives totals, not a new physical mechanism. Sampling a boundary point and assigning region ownership are separate operations.

## Guided practice

**C06.01-P1:** Extend the tree to depth 3. List child indices and parents, then trace j=5.

**Answer:** Children 0,1,2,3,4,5,6,7 have parents 0,0,1,1,2,2,3,3. Index 5 is [5/8,6/8); its parents are 2 at depth 2, 1 at depth 1, and 0 at depth 0.

**C06.01-P2:** Count 9B Supergroup volumes by axes and by Groups.

**Answer:** 9^3=729 cells; 3^3 Groups times 27 cells per Group also gives 729.

## Diagnostic checks

1. **C06.01-D1:** At depth 2, are there four cells and eight distinct vertices? What about endpoint 1?
2. **C06.01-D2:** Classify 27 window nodes, 27 Group volumes, and 729 Supergroup volumes. Do the two 27s identify objects?
3. Which depth-2 interval owns 1/2? Which owns 1?
4. Give the parent of depth-3 index 6 and its sibling (the other child).

**Worked answers:** (1) Four cells and five distinct vertices; eight counts incidences. Vertex 1 is an excluded ownership endpoint. (2) Points, complete cells, complete cells. Equal cardinality means equal number only. (3) Index 2 owns 1/2; none owns 1. (4) Parent floor(6/2)=3; sibling 7.

**Next:** [Lesson 02](lesson-02.md) compares this halving rule with ternary addresses.
