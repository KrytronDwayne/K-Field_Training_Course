# Lesson 06 · Reading a state through modes

**Essential question:** How can a different set of coordinates retain every entry of a state?

**Goals:** Calculate mode coefficients and reconstruct a path state; preserve a residual when retaining fewer modes; compare mode, parity, and mean coordinates; test the constant-pattern claim on the Lucas graph.

**Prerequisite bridge.** We know the orthonormal path modes and the dot product. A state is simply the full list of values at the declared addresses. Coefficients will be a new list describing the same state. Two periods let us practice reconstruction before comparing representations.

## C12.06-E1 · Read and write a state

For each unit mode u_j, define c_j=u_j·f. Here j is one of the labels +,0,−, not a node. If f=c+u+ + c0u0 + c−u−, taking its dot product with u+ leaves c+ alone: its own dot product is 1 and the other two are zero. The same argument isolates the other coefficients.

We also need to show that every path state can be written this way. For f=(a,b,c) and r=√2, the dot products give c+=(a+c)/2+b/r, c0=(a−c)/r, c−=(a+c)/2−b/r. Rebuild the first entry: (c++c−)/2+c0/r=(a+c)/2+(a−c)/2=a. The middle entry is r(c+−c−)/2=b. The last is (c++c−)/2−c0/r=c. This is a direct reconstruction proof, not an appeal to an untaught theorem. A collection allowing unique reconstruction is a **basis**.

For the 27-node graph, apply this one-path expansion successively to each coordinate direction. Each step is reversible, so their composition is reversible. The resulting coefficient for product mode U is the sum of U(L)f(L) over all 27 nodes, and f is the sum of all 27 coefficient-times-mode patterns. This explains why all listed product modes are needed for arbitrary states.

## C12.06-W1 · Read back (1,2,3)

The coefficients in (+,0,−) order are c+=1/2+√2+3/2=2+√2, c0=(1−3)/√2=−√2, c−=2−√2. Reconstruct:

first entry (2+√2)/2−1+(2−√2)/2=1;
middle entry (2+√2)√2/2−(2−√2)√2/2=2;
last entry (2+√2)/2+1+(2−√2)/2=3.

The residual f minus the reconstruction is exactly (0,0,0). If we keep only the zero-mode term, the retained part is (−1,0,1), and the residual is (2,2,2). Keep both: their sum is the original state. A residual is a full signed pattern, not merely a score.

A different representation retains the **mean** μ, the sum of entries divided by their count, and the **centered detail** d=f−μ**1**. Then f=μ**1**+d and the entries of d sum to zero. For this example μ=2 and d=(−1,0,1). The match with a zero-mode term in this example does not make mean subtraction a mode deletion in general.

## C12.06-P1 · Guided practice and answers

For f=(2,0,0), compute (c+,c0,c−)=(1,√2,1). The three contributions are (1/2,√2/2,1/2), (1,0,−1), and (1/2,−√2/2,1/2), adding to (2,0,0). Retaining only c0u0 gives (1,0,−1); preserve residual (1,0,1).

Its parity representation is e=(1,0,1), o=(1,0,−1). Its mean representation has μ=2/3 and d=(4/3,−2/3,−2/3). Each representation reconstructs f exactly. These are alternatives, not independent extra measurements of f.

For a Lucas node, each coordinate equal to 0 supplies two neighbors; each coordinate equal to −1 or 1 supplies one. Thus degree=3+(number of zero coordinates). Count and calculate:

| Node type | Number | Degree / value of A_L **1** |
|---|---|---|
| No zeros (corners) | 2³=8 | 3 |
| One zero | 3·2²=12 | 4 |
| Two zeros | 3·2=6 | 5 |
| Three zeros (center) | 1 | 6 |

The constant vector therefore is not an eigenvector of A_L. Its output has several different values.

Mean subtraction affects only the even function part: each antipodal odd pair sums to zero and its center is zero. The 14 even coordinates obey one independent mean-zero equation after centering, leaving 13 even details; all 13 odd coordinates remain. Record the mean separately to recover the full 27 coordinates: 1+13+13=27. This gives the source's 13+13 observable coordinate count without discarding the mean.

Why doesn't this define a 26-mode Emily spectrum? An **invariant** set of patterns stays within that set under the operator. Constant patterns do not: A_L **1** is not constant. If two states differ by a constant and we regard them as the same, their adjacency outputs can differ by a nonconstant degree pattern. Adjacency would then assign incompatible outputs to that single equivalence class. Thus quotienting constants does not induce this adjacency operator. Defining a new projected operator would require a new rule and a fresh spectrum; we do not introduce one.

> **Claim scope.** S02 /backbone_sequence/7/proof/5 supplies the coordinate count. Our degree calculation limits its operator interpretation. No uniform Emily eigenmode is removed. Every residual and removed mean remains reconstructible; these classroom values are synthetic and dimensionless.

## C12.06-D1 · Diagnostic checks

1. Reconstruct (2,0,0) from its coefficients, and give the residual if only its zero mode is retained.
2. Give that state's mean, centered detail, and parity parts.
3. Explain the counts 14+13 and 1+13+13 without treating χ as function parity.
4. Use a corner and the center to refute the claim “constant is an Emily eigenmode, so removing it leaves 26 Emily modes.”

**Worked answers.** 1. The three contributions above sum to (2,0,0); omitted part (1,0,1) must be retained as residual. 2. μ=2/3, d=(4/3,−2/3,−2/3); e=(1,0,1), o=(1,0,−1). 3. Fourteen even plus thirteen odd node-function coordinates; separating one uniform mean leaves thirteen even details and thirteen odd values plus the retained mean. 4. A_L **1** is 3 at a corner and 6 at the center, so no common eigenvalue works. Mean removal is a different coordinate operation, not deletion of one adjacency eigenmode.

**Next dependency:** [Lesson 07](lesson-07.md) tests when a proposed coordinate identification actually preserves an operator.
