# Lesson 01 · A matrix acting on a pattern

**Essential question:** How can one rule update every node value without losing track of which node is which?

**Goals:** Calculate three neighbor sums; read a matrix row as a rule; distinguish node adjacency from edge incidence.

**Prerequisite bridge.** You can add signed numbers and read ordered coordinates. Course 11 used nodes and edges: a node is an address, and an edge joins two addresses. Here we attach a number to each node. These numbers are a *pattern*, not edge flows. We review the needed graph language so the calculation does not require remembering course 11's cycle construction.

## C12.01-E1 · One rule, three addresses

Draw the open path `−1 — 0 — 1`. The labels are addresses, not the values stored there. “Open” means the two endpoints are not connected to each other. The order throughout this path calculation is (−1,0,1). Write a pattern as f=(a,b,c), meaning a at −1, b at 0, and c at 1. We write tuples horizontally to save space but matrices act on them as columns.

Define adjacency action by adding the values at neighboring nodes. The left node has only the middle neighbor, the middle has both endpoints, and the right has only the middle. Therefore

Af=(b,a+c,b), with A=[[0,1,0],[1,0,1],[0,1,0]].

A matrix is an array of numbers. Row i gives the rule for output i: multiply each row entry by the input in its corresponding column, then add. For example, the middle row says 1·a+0·b+1·c=a+c. A zero entry means “do not include this input”; a one means “include it once.” The two equal endpoint outputs follow from the graph's connections, not from assuming equal inputs. The operation accepts negative values without changing the rule.

The same input and output addresses make A a 3-by-3 matrix. An incidence matrix D from course 11 instead accepts *edge* values and returns signed node divergence. For this path it has three rows and two columns after edge directions are declared. A graph Laplacian is another node rule: degree times the node's own value minus its neighbor sum, where degree means number of neighbors. It is not our A. No Laplacian calculation is required here; naming the distinction prevents an accidental operator swap later.

## C12.01-W1 · Fully worked example

For f=(1,2,3), row 1 gives 0·1+1·2+0·3=2. Row 2 gives 1·1+0·2+1·3=4. Row 3 gives 0·1+1·2+0·3=2. Thus Af=(2,4,2).

For the constant pattern **1**=(1,1,1), the same calculation gives A**1**=(1,2,1). Each output counts neighbors. It is impossible to obtain this output by multiplying all three input entries by the same number: the endpoints demand multiplier 1, while the middle demands 2.

## C12.01-P1 · Guided practice and worked answers

First compute A(2,−1,0) and A(1,0,0) yourself. For the first input, the endpoint sums are −1 and the middle sum is 2+0=2, so the answer is (−1,2,−1). For the second, only the middle node touches the nonzero input, giving (0,1,0). In both cases verify your result using all three matrix rows.

Now label the input carrier for A and D. A takes three node numbers; D takes two directed-edge numbers. A list's length alone is never its full meaning: its labels and rule matter too.

> **Claim scope.** These are exact, dimensionless classroom patterns on an unweighted graph. They are not measured signals, forces, or time evolution. The path is a factor in the source's Lucas graph (S02, /backbone_sequence/7/definitions and /proof/2). All node order choices are explicit classroom conventions.

## C12.01-D1 · Diagnostic checks

1. Find A(−1,3,2) by rows.
2. Explain why A has three input columns, while this path's incidence D has two.
3. Does adjacency preserve a constant pattern up to one multiplier on this path?
4. A student reports A(2,−1,0)=(1,2,1). Identify the error.

**Worked answers.** 1. (3,−1+2,3)=(3,1,3). 2. A inputs one value per node; D inputs one flow per edge. 3. No: A(1,1,1)=(1,2,1), whose entries cannot share one multiplier relative to the input. 4. The student erased the negative neighbor value; both endpoint outputs must be −1. Preserve signs as part of the information.

**Next dependency:** [Lesson 02](lesson-02.md) asks which nonzero patterns *do* keep one common multiplier.
