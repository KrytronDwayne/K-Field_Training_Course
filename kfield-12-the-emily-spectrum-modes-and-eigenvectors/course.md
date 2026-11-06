# The Emily Spectrum: Modes and Eigenvectors

Student course · 11 core periods and 2 capstone periods of 55 minutes.

<!-- BEGIN: lesson-01 -->
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
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 02 · Eigenvectors as unchanged pattern directions

**Essential question:** When does an operator change a pattern only by one common multiplier?

**Goals:** Verify an eigenpair component by component; explain zero and negative eigenvalues; verify that nonzero scaling preserves an eigenvalue.

**Prerequisite bridge.** Lesson 01 taught row multiplication and neighbor sums. We now compare an output with a scaled copy of its input. Multiplying a vector by a number means multiplying every entry by that same number.

## C12.02-E1 · The common-multiplier test

A nonzero pattern v is an **eigenvector** of an operator A when Av=λv for one number λ, called its **eigenvalue**. The pair (λ,v) is an eigenpair. Equality means equality at every node: the first output equals λ times the first input, the second equals λ times the second, and so on. Do not divide by entries that are zero; compare products directly.

“Unchanged direction” includes three cases. A positive λ scales the pattern without reversing it. A negative λ reverses every sign while scaling. A zero λ sends that entire pattern to zero. The input must still be nonzero. The all-zero vector is excluded because A0=λ0 for every λ; it cannot select a particular multiplier.

Before using the three-node path, try the two-node path. Its adjacency S=[[0,1],[1,0]] simply swaps two entries: S(a,b)=(b,a). We use S to avoid confusing its two-address domain with A's three-address domain.

## C12.02-W1 · Two patterns that keep their direction

S(1,1)=(1,1)=1·(1,1), so (1,(1,1)) is an eigenpair. S(1,−1)=(−1,1)=−1·(1,−1), so (−1,(1,−1)) is another. Both entries have been checked in each case.

Multiply the first input by 3: S(3,3)=(3,3). Multiply the second by 3: S(3,−3)=(−3,3)=−1·(3,−3). The eigenvalues remain 1 and −1, respectively. Why? Each row is a sum of fixed multiples, so A(tv)=t(Av)=tλv=λ(tv). Here t is any nonzero number. Choosing t=0 would produce the excluded zero vector. This distributive rule is called linearity; it also gives A(v+w)=Av+Aw.

We will soon need √2. For a positive number q, √q means the positive number whose square is q. Thus (√2)²=2 exactly; √2 is approximately 1.414, but we keep the exact symbol. The equation x²=2 has two answers, √2 and −√2, even though the symbol √2 itself names the positive one.

## C12.02-P1 · Guided practice and worked answers

Verify S(2,2), S(2,−2), and the path action A(2,0,−2). The swap gives (2,2) and (−2,2), hence eigenvalues 1 and −1. The path rule gives (0,2−2,0)=(0,0,0)=0·(2,0,−2). This third input is a valid nonzero zero-eigenvalue vector. A zero output does not mean there was no input information: the input's amplitude cannot be recovered from this output alone.

Try the path candidate (1,1,1). Its output is (1,2,1); the first component requires λ=1, while the middle requires λ=2. Thus no common λ works. Also check (√2)(√2)=2 and (−√2)²=2; both follow from the square-root definition and signed multiplication.

> **Claim scope.** “Mode” will mean a chosen eigenvector pattern, not a physical oscillation by default. The calculations establish finite operator facts. A mechanism or measured frequency needs additional definitions and evidence. See S02 /backbone_sequence/7/proof/2–4 for the later source spectrum.

## C12.02-D1 · Diagnostic checks

1. Test S(3,−3) and name its eigenvalue.
2. Why is (0,0) not an eigenvector, although S(0,0)=0·(0,0)?
3. Test (1,1,1) for the three-node A. Is a zero eigenvalue forbidden?
4. If Av=λv, does multiplying v by −2 change λ? Explain using row distributivity.

**Worked answers.** 1. S(3,−3)=(−3,3)=−(3,−3), so λ=−1. 2. The eigenvector definition excludes zero; every λ would work for it. 3. It fails because (1,2,1) is not a common multiple. Zero λ is allowed for a nonzero input such as (2,0,−2). 4. A(−2v)=−2Av=λ(−2v); λ stays the same.

**Next dependency:** [Lesson 03](lesson-03.md) finds every eigenvalue of the three-node path and gives its modes unit length.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 03 · The three-node path spectrum

**Essential question:** Can we derive and compare all the modes of the open three-node path?

**Goals:** Derive all three eigenvalues using component equations; verify three eigenpairs; normalize modes and check their pairwise dot products.

**Prerequisite bridge.** Use A(a,b,c)=(b,a+c,b) and Av=λv from Lessons 01–02. Recall that √2 is positive and squares to 2. This lesson takes two periods: first derive and verify, then learn length and orthogonality.

## C12.03-E1 · Solve the component equations

An eigenpair must satisfy b=λa, a+c=λb, and b=λc. If λ=0, the first equation gives b=0 and the second gives c=−a. A nonzero input requires a≠0, giving multiples of (1,0,−1).

If λ≠0, the first and third equations imply a=c: divide λa=λc by the nonzero λ. Then the middle equation becomes 2a=λb=λ²a. Here a cannot be zero, since a=0 would force b=c=0. Dividing by a gives λ²=2, so λ=√2 or −√2. Taking a=1 produces (1,√2,1) or (1,−√2,1). These cases cover all possibilities, so no other eigenvalue exists. The list of eigenvalues, including how many independent modes share each value, is the **spectrum**.

To compare sizes, define the dot product x·y as the sum of matching-entry products. Thus (a,b,c)·(d,e,f)=ad+be+cf. The squared length of x is x·x; its length or norm is √(x·x). It is positive for a nonzero vector. Dividing every entry by that length produces a **normalized** vector of length 1. Two vectors are **orthogonal** when their dot product is zero. Here orthogonality is a precise algebraic test, so no spatial drawing is required. A list of mutually orthogonal unit vectors is **orthonormal**.

## C12.03-W1 / C12-EIG-EX1 · Verify every row and length

Let r=√2 for this calculation, so r²=2.

| Mode | Row outputs Av | λv | Squared length |
|---|---|---|---|
| v+=(1,r,1) | (r,1+1,r)=(r,2,r) | r(1,r,1)=(r,2,r) | 1+2+1=4 |
| v0=(1,0,−1) | (0,1−1,0)=(0,0,0) | 0(1,0,−1)=(0,0,0) | 1+0+1=2 |
| v−=(1,−r,1) | (−r,1+1,−r)=(−r,2,−r) | −r(1,−r,1)=(−r,2,−r) | 1+2+1=4 |

The lengths are 2,r,2. Our fixed mode order is (+,0,−), and the normalized modes are

u+=(1/2,r/2,1/2), u0=(1/r,0,−1/r), u−=(1/2,−r/2,1/2).

All have squared length 1. Their mutual dot products are u+·u−=(1−2+1)/4=0, u+·u0=(1−1)/(2r)=0, and u0·u−=(1−1)/(2r)=0. Scaling preserved the eigenvalues, so Au+=r u+, Au0=0, Au−=−r u−.

## C12.03-P1 / C12-EIG-P1 · Guided practice and answers

Verify A(2,0,−2)=0 and explain why the input remains an eigenvector. Its row outputs are (0,2−2,0)=0, and it is twice v0 with nonzero scale 2. Normalize (2,2r,2): its squared length is 4+8+4=16, length 4, and division by 4 gives u+. Check Au− directly: the outputs are (−r/2,1,−r/2)=−r(1/2,−r/2,1/2). Finally compute u+·u−=0 and u0·u−=0 using the fractions above.

Practice the derivation without looking: separate λ=0 from λ≠0, then explain why dividing by a in the second case is legal. Answer: a=0 would make all entries zero, violating the eigenvector condition. This is why the two-case argument does not miss a solution.

> **Claim scope.** This direct derivation supplies the finite path proof used in S02 /backbone_sequence/7/proof/2. No general spectral theorem is assumed or assessed. The symbols + and − label our chosen modes; they do not yet describe inversion parity, which is a different operation.

## C12.03-D1 / C12-EIG-D1 · Diagnostic checks

1. Reject (1,1,1) as an eigenvector using its three outputs.
2. Derive λ²=2 in the nonzero-λ case; state why the division is allowed.
3. Find the norm of (1,−√2,1), normalize it, and verify its middle output.
4. Calculate all three mutual dot products of u+,u0,u−. What does orthonormal mean?

**Worked answers.** 1. A(1,1,1)=(1,2,1), requiring conflicting multipliers 1 and 2. 2. Endpoints agree, b=λa, so 2a=λ²a; a≠0 as shown above. 3. Norm √4=2; u−=(1/2,−√2/2,1/2), whose middle output is 1=−√2·(−√2/2). 4. The products are (1−2+1)/4=0 and (1−1)/(2√2)=0 twice. Orthonormal means mutual zero dot products and each length 1.

**Next dependency:** [Lesson 04](lesson-04.md) combines these three one-dimensional choices into patterns on 27 nodes.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 05 · Counting Emily multiplicities

**Essential question:** What exactly is being counted when the same seven numbers appear in different places?

**Goals:** Build all seven multiplicities; distinguish modes from nodes; decompose a pattern into antipodal even and odd parts; count the independent parity coordinates.

**Prerequisite bridge.** Each of the three mode choices contributes +√2,0,or −√2 to a product eigenvalue. Divide the common symbolic factor √2 out of the bookkeeping and call those contributions +1,0,−1. The sum m gives eigenvalue m√2. Two periods separate mode counting from node and function parity.

## C12.05-E1 · Count ordered choices

For two choices, sums −2,−1,0,1,2 occur 1,2,3,2,1 times: −2 uses (−1,−1), −1 uses (−1,0),(0,−1), and 0 uses (−1,1),(0,0),(1,−1). Reverse signs for positive sums. To add the third choice and get m, use earlier sums m+1, m, or m−1 according to whether the last choice is −1,0,or 1. Add those three earlier counts; outside the two-choice range use zero. This sliding addition is sometimes called convolution; only finite addition is needed here.

## C12.05-W1 · The complete Emily ledger

The table lists every ordered mode triple. A string such as `+0−` means the factor order (u+,u0,u−), not a node address. Distinct permutations give distinct patterns even when the eigenvalue agrees.

| m | Eigenvalue | All mode labels | Multiplicity |
|---|---|---|---|
| −3 | −3√2 | `−−−` | 1 |
| −2 | −2√2 | `−−0`, `−0−`, `0−−` | 3 |
| −1 | −√2 | `−00`, `0−0`, `00−`, `−−+`, `−+−`, `+−−` | 6 |
| 0 | 0 | `000`, `+0−`, `+−0`, `0+−`, `0−+`, `−+0`, `−0+` | 7 |
| 1 | √2 | `+00`, `0+0`, `00+`, `++−`, `+−+`, `−++` | 6 |
| 2 | 2√2 | `++0`, `+0+`, `0++` | 3 |
| 3 | 3√2 | `+++` | 1 |

For example, m=0 receives two-choice counts 2+3+2=7; the labels show one all-zero choice and six arrangements of +,0,−. The total 1+3+6+7+6+3+1=27 accounts for every choice. **Multiplicity** here is the number of independent modes with that eigenvalue; Lesson 04's orthogonality ensures these listed modes are independent.

Now distinguish two other countings. For *nodes* L=(i,j,k), the source sheet label is λ_sheet=i+j+k. This is not the adjacency eigenvalue λ. The node populations have the same 1,3,6,7,6,3,1 list because the same sum-counting works on coordinate choices. Define the node label χ(L)=(-1)^(i+j+k): it is +1 on even integer sums and −1 on odd sums, including negative integers. Hence there are 3+7+3=13 positive-χ nodes and 1+6+6+1=14 negative-χ nodes. These are labels of addresses, not parity of functions.

For *functions*, reflection R sends a pattern f to Rf with (Rf)(L)=f(−L); it swaps antipodal addresses. An even function satisfies Rf=f; an odd function satisfies Rf=−f. Every pattern splits reversibly as e=(f+Rf)/2 and o=(f−Rf)/2, with f=e+o. On a pair having values a,b, these parts have values ((a+b)/2,(a+b)/2) and ((a−b)/2,(b−a)/2). Their sum recovers a,b. The center is fixed, so an odd function must have center value 0.

The 26 noncentral nodes make 13 pairs. One even value per pair plus an independent center value gives 14 even coordinates. One signed odd value per pair gives 13 odd coordinates. This is the source's 14-even/13-odd *node-function* split. On one path, u+ and u− are both even under reflection, while u0 is odd. Thus a mode's eigenvalue sign is not its reflection parity.

## C12.05-P1 · Guided practice and answers

Enumerate m=1: three placements of + in (+,0,0), and three placements of − in (+,+,−), give 6. Re-add the ledger to get 27. Split f=(1,2,3): Rf=(3,2,1), e=(2,2,2), o=(−1,0,1); adding gives f. Count the Lucas pairs: (27−1)/2=13, so even dimension 13+1=14 and odd dimension 13. Recompute χ counts by even versus odd sheet sums: 13 and 14. Notice that χ-positive count 13 does not equal the even-function count 14.

> **Claim scope and source card.** S02 /backbone_sequence/7/proof/4–5 and /backbone_sequence/7/emily_spectrum support the mode ledger and function parity; /backbone_sequence/2/sheet_populations supports the separate node ledger. Thirteen antipodal pairs are pairs of addresses. Thirteen decoder channels in S02 /backbone_sequence/16 are decoder inputs; seven syndrome dimensions are retained residual coordinates there. These are different carriers. No common count supplies an operator-preserving map. The full decoder is recognition-only in this course.

## C12.05-D1 · Diagnostic checks

1. Derive the multiplicity at m=−1 using the two-choice counts.
2. Why are there 14 even function coordinates but only 13 odd ones?
3. Split (4,1,0) into even and odd path parts and reconstruct it.
4. Do seven sheet populations and seven distinct Emily eigenvalues establish an identification? Compare χ counts with function parity counts.

**Worked answers.** 1. Earlier sums 0,−1,−2 contribute 3+2+1=6. 2. Both have 13 pair coordinates; only the even part has an unrestricted center. 3. Rf=(0,1,4), e=(2,1,2), o=(2,0,−2); e+o=(4,1,0). 4. No: sheet populations count nodes, eigenvalues classify modes; a map and operators remain to be specified. χ has 13 positive and 14 negative nodes, while function parity has 14 even and 13 odd dimensions.

**Next dependency:** [Lesson 06](lesson-06.md) uses modes to reconstruct a state and explains exactly what happens to its uniform mean.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
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
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 07 · Spectral resemblance and typed identity

**Essential question:** What must a map preserve before two spectral descriptions can be identified?

**Goals:** Name the input and output spaces and operators; test an invertible map by two calculation routes; distinguish count agreement from an operator-preserving identification.

**Prerequisite bridge.** Lessons 01–06 taught matrix action, linearity, modes, and reversible coordinates. We now compare two systems using an explicit map T. A **domain** is the set of allowed inputs; a **codomain** is the declared output set. A **carrier** names the kind of object: node functions, node labels, or decoder channels, for example.

## C12.07-E1 · Compare two routes

Suppose A_X acts on states in X, B_Y acts on states in Y, and T sends X states to Y states. To preserve the action, both routes must agree for every state x:

B_Y(Tx)=T(A_X x), abbreviated B_Y T=T A_X.

Read composition right to left: first T, then B_Y on the left; first A_X, then T on the right. Such a map is called an **intertwiner**. For an identification of whole state spaces, also require T to be invertible: another rule recovers every original x. Counts or matching spectra alone do not verify a proposed T.

How can a finite check establish “every x”? For two-coordinate states, write x=a(1,0)+b(0,1). If both routes agree on (1,0) and (0,1), linearity makes them agree on every such combination. The two resulting columns form the matrix of the composite action. This teaches the needed matrix product without a new general algorithm.

The local name B_Y is an operator in this lesson, not the source-locked geometric basis B of Cell3. No metric or physical unit is being transferred here.

## C12.07-W1 · A genuine swap identification

Let X and Y each be ordered pairs of real numbers. Define A_X(a,b)=(a,2b), B_Y(p,q)=(2p,q), and T(a,b)=(b,a). In matrix shorthand A_X=diag(1,2), B_Y=diag(2,1), T=[[0,1],[1,0]]. “diag” means the listed numbers sit on the main diagonal and other entries are zero.

Route one gives B_Y T(a,b)=B_Y(b,a)=(2b,a). Route two gives T A_X(a,b)=T(a,2b)=(2b,a). Both are the matrix [[0,2],[1,0]] applied to (a,b). Since swapping twice restores (a,b), T is invertible. For x=(3,4), Tx=(4,3), both routes give (8,3), and T(Tx)=(3,4).

This also transports eigenvectors: if A_X v=λv, then B_Y(Tv)=T(λv)=λTv. Invertibility keeps Tv nonzero. The equation, not the matching number of entries, supplies the connection.

## C12.07-P1 · Guided practice and answers

Propose instead T=I, the identity map I(a,b)=(a,b). The routes give (2a,b) and (a,2b). Their difference is (a,−b), the matrix diag(1,−1) applied to the input. On (1,0) the routes differ, so this proposed map fails even though A_X and B_Y each have eigenvalues 1 and 2. The successful swap still exists; failure of one map does not refute all possible maps.

For the successful T, x=(1,−2) maps to (−2,1), then swaps back exactly. Both routes yield (−4,1). Now compare adjacency modes with node sheets: naming seven groups on each side does not specify an operator on sheet data, a domain of states there, or an invertible T to adjacency modes. Record these as missing specifications, not as an identification.

Reflection R on the Lucas graph does commute with adjacency. To see this, reflecting each neighbor of L gives exactly a neighbor of −L, because open coordinate steps reflect to open coordinate steps. Thus summing reflected input neighbors and reflecting the neighbor-sum output agree: A_L R=R A_L. Consequently an even input has even output and an odd input has odd output. This preserves the full 14-even/13-odd sectors. It does not additionally preserve the constant line, as Lesson 06 showed. Practice this distinction on the path: for f=(1,2,3), ARf=A(3,2,1)=(2,4,2)=RAf.

> **Claim scope.** Source carriers remain separate: 27 Emily modes in seven eigenvalue groups; 27 node addresses in seven sheet populations; 13 antipodal address pairs; 13 decoder channels; and a seven-dimensional decoder syndrome (S02 /backbone_sequence/7, /2/sheet_populations, /16). In M17 the 13-by-6 matrix has rank 6, independently checked in the teacher verification, leaving seven residual coordinates. Its full decoder is recognition-only here. Backbone M08 is not automatically compiler module M08. S03 /findings/1 reports missing formula-DAG expansions; this finite course does not certify global source closure or rerun formal integration proofs.

## C12.07-D1 · Diagnostic checks

1. Calculate both swap routes on (2,5) and give the inverse of T.
2. Give one input refuting T=I for the same A_X,B_Y.
3. What three specifications are absent from a bare assertion that sheet populations “are” Emily modes?
4. Does reflection symmetry justify dropping a uniform Emily mode? Explain using two separately tested properties.

**Worked answers.** 1. Both give (10,2); the inverse is the same swap. 2. (1,0): B_Y I gives (2,0), while I A_X gives (1,0). 3. Explicit carriers/state spaces, the operators on both sides, and an invertible map satisfying the two-route equation. 4. No. Reflection commutes with adjacency and preserves even/odd sectors. The constant line is not invariant because its adjacency output is the nonconstant degree vector. These are different claims.

**Next dependency:** [Capstone](capstone.md) combines the ledger, exact reconstruction, retained residuals, and map tests.
<!-- END: lesson-07 -->

