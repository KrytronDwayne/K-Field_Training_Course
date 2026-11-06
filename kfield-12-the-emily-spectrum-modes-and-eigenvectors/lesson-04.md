# Lesson 04 · Combining three path directions

**Essential question:** Why do the eigenvalues add when path patterns are combined?

**Goals:** Construct a product pattern; derive the eigenvalue sum from neighbor actions; verify one product-mode component; explain why product modes have unit length.

**Prerequisite bridge.** Lesson 03 gave three unit modes for one path. A triple address (i,j,k) tells us which path node to use in each of three directions. Each coordinate is −1, 0, or 1. There are 3·3·3=27 addresses. Use lexicographic order: first i increases slowest, then j, then k fastest, beginning (−1,−1,−1), (−1,−1,0), (−1,−1,1), (−1,0,−1). Two periods allow time to draw slices and check the sums.

## C12.04-E1 · Multiply patterns, add actions

The **Cartesian-product graph** joins two addresses when exactly one coordinate moves to a neighbor on its open path, while the other two stay fixed. There is no wrapping from −1 to 1. The source names this graph G_L, the Lucas graph (S02 /backbone_sequence/7/definitions). Let A_L be its unweighted adjacency. Its rule sums all neighbor values in the i direction, all in the j direction, and all in the k direction.

Given three one-path patterns a,b,c, define a product pattern v(i,j,k)=a(i)b(j)c(k). For example, a(i) means the entry of pattern a stored at address i. Choose a,b,c from u+,u0,u−. Suppose their eigenvalues are α,β,γ. At a fixed triple, summing i-neighbors gives [sum of a at neighbors of i]b(j)c(k)=αa(i)b(j)c(k). The j-neighbor sum is β times the same value, and the k-neighbor sum is γ times it. Adding these contributions gives

(A_L v)(i,j,k)=(α+β+γ)v(i,j,k).

This proves the product rule at every address, including boundaries where each path already has only one neighbor. We multiply *entries* to form a pattern, but add eigenvalues because the operator adds three direction actions. A product of operators would be a different rule.

For two factors only, the same argument uses two sums: u+(i)u0(j) has eigenvalue √2+0=√2. The three-factor construction is the same operation with one additional direction.

Why is the product pattern normalized? Add its squared entries over all i,j,k. Distributing the finite sums factors the result into (sum a(i)²)(sum b(j)²)(sum c(k)²)=1·1·1=1. The same factoring works for dot products between two product patterns. If their mode choices differ in any direction, one factor is a zero dot product from Lesson 03, so the full dot product is zero. Thus the 27 choices are mutually orthonormal; Lesson 06 supplies an explicit reconstruction rule explaining their completeness.

## C12.04-W1 · A center check

Choose v=u+u+u−, meaning v(i,j,k)=u+(i)u+(j)u−(k), in that order. Its eigenvalue is √2+√2−√2=√2. At (0,0,0), v=(√2/2)(√2/2)(−√2/2)=−√2/4.

There are six neighbors. Each i-neighbor has value (1/2)(√2/2)(−√2/2)=−1/4, so the i-pair contributes −1/2. The j-pair also contributes −1/2. Each k-neighbor has value (√2/2)(√2/2)(1/2)=1/4, so the k-pair contributes 1/2. Total −1/2 agrees with √2·(−√2/4)=−1/2.

## C12.04-P1 · Guided practice and answers

Find the eigenvalues for u+u0u− and u−u−u0. They are √2+0−√2=0 and −√2−√2+0=−2√2. For the second pattern, verify address (−1,−1,−1). Its value is (1/2)(1/2)(1/√2)=1/(4√2). Its three neighbors, obtained by changing one coordinate to 0, have values −1/4,−1/4,0. Their sum is −1/2, agreeing with −2√2/(4√2). Its squared norm is 1 because all three factors have norm 1. Retain the order: the zero-mode factor belongs to the third coordinate.

> **Claim scope.** We have established the source's Cartesian-product eigenvalue addition (S02 /backbone_sequence/7/proof/3) for the pinned open adjacency and ordering. This is not the periodic graph, a weighted graph, or a dynamical law. All examples are exact dimensionless constructions.

## C12.04-D1 · Diagnostic checks

1. What eigenvalue belongs to u+u0u0? Why would multiplication of eigenvalues fail?
2. State the corner value and neighbor sum for u−u−u0 at (−1,−1,−1).
3. How many neighbors does (0,0,0) have? Does an endpoint wrap?
4. Explain why u+u0u− and u+u+u− have zero dot product.

**Worked answers.** 1. √2+0+0=√2; multiplying gives 0, which uses the wrong operator. 2. Value 1/(4√2); neighbor sum −1/4−1/4+0=−1/2. 3. Six, two per coordinate; no wrap is present. 4. The dot product factors; its second-coordinate factor u0·u+ is zero, so the whole product is zero.

**Next dependency:** [Lesson 05](lesson-05.md) counts how many ordered choices share each eigenvalue.
