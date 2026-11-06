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
