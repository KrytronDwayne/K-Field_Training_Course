# Mass, Coupling, and Atomic Structure as Decoding Problems

Student course, approved lesson order. Supporting material: [glossary](terminology.md), [capstone](capstone.md), [sources](sources.md), [teacher guide](teacher-guide.md).

<!-- BEGIN: lesson-01 -->
# lesson-01: Measurements as linear channels

2 sessions of 55 minutes.

**Essential question:** How can three channels describe two unknowns without throwing away the third reading?

**Goals**

- Translate channel recipes into equations and an ordered matrix.
- Solve two normal equations by elimination.
- Reconstruct every input from represented and residual entries.

## Prerequisite bridge

You need signed arithmetic, fractions and linear equations. A tuple is an ordered list: (2,3,6) means first channel 2, second 3, third 6. Multiplying a tuple by a number multiplies every entry; adding tuples adds corresponding entries. These are the only operations needed to begin. Earlier courses motivate retained information, but all matrix operations used here are taught locally.

<a id="C21.01-E1"></a>
## Explanation — C21.01-E1

Imagine two adjustable coordinates, c1 and c2. A channel is a stated recipe for combining them. Our synthetic instrument reports c1, c2, and c1+c2. A linear recipe multiplies each coordinate by a fixed number and adds; there are no products of unknown coordinates. Arrange the recipes as rows:

```text
A_small = [1 0]     c = [c1]       A_small c = (c1,c2,c1+c2)
          [0 1]         [c2]
          [1 1]
```

A matrix is this rectangular table of coefficients. A row times a column means multiply matching entries and add. Its shape is 3 by 2: three output channels and two input coordinates. The system is overdetermined because there are more equations than unknowns. It may be exactly consistent, but it need not be. For y=(2,3,6), the first two equations demand c1=2 and c2=3, whose sum is 5 rather than 6. Keep all three readings.

Declare a decoding convention before solving. In this course the scalar field is the real numbers, written R, and the inner product is Euclidean: u dot v is the sum of pairwise products. For example (1,0,1) dot (2,3,6)=8. We choose the represented vector A_small c so that the residual r=y-A_small c is perpendicular to each column. Perpendicular here means dot product zero. This convention is a reproducible coordinate choice, not a discovery that the residual lacks information.

The transpose A_small^T is obtained by turning columns into rows. Thus A_small^T r=(r1+r3,r2+r3). Set both entries to zero. Substituting r=(2-c1,3-c2,6-c1-c2) gives 8-2c1-c2=0 and 9-c1-2c2=0. These are the normal equations. In compact notation A_small^T A_small c=A_small^T y. Multiplication here has already been defined by sums; it introduces no new physical assumption.

Solve 2c1+c2=8 and c1+2c2=9. Twice the first minus the second gives 3c1=7, so c1=7/3. Then c2=8-14/3=10/3. The represented channels are (7/3,10/3,17/3). Subtract each from y to obtain r=(-1/3,-1/3,1/3). The two perpendicularity checks are -1/3+1/3=0 and -1/3+1/3=0. Reconstruction gives (7/3-1/3,10/3-1/3,17/3+1/3)=(2,3,6).

This construction also minimizes the sum of squared residual entries, but that score is not our saved output. To see the mathematical fact without calculus, change c by h. The new residual is r-A_small h. Its squared length is r dot r minus twice r dot A_small h plus (A_small h) dot (A_small h). The middle term is zero by the perpendicularity condition, and the last term is nonnegative. This explains the convention while leaving the entire signed residual intact.

> Scope: All channel values in these exercises are synthetic and dimensionless. The Euclidean metric is declared. A different weighting would define a different decoder and must be recorded. No physical source coefficient-selection law is being inferred.

For practice y=(1,2,3), compute A_small^T y=(1+3,2+3)=(4,5). Elimination gives c=(1,2). All three residual entries are zero, so explicitly retain (0,0,0), the channel order and the matrix. A missing entry and a known zero are different records.

<a id="C21.01-W1"></a>
## Worked example — C21.01-W1

C21-DEC-EX1: y=(2,3,6) makes c1=2, c2=3, c1+c2=6 inconsistent. The normal equations are 2c1+c2=8 and c1+2c2=9. Elimination gives c=(7/3,10/3). A c=(7/3,10/3,17/3); r=(-1/3,-1/3,1/3). Reconstruct all three channels.

<a id="C21.01-P1"></a>
## Guided practice — C21.01-P1

Try the operation before reading the solution. C21-DEC-P1: y=(1,2,3) gives right side (4,5), c=(1,2), A c=y, r=(0,0,0). Write all three zero residual entries and the original A.

<a id="C21.01-D1"></a>
## Diagnostic checks — C21.01-D1

1. For y=(1,1,3), write and solve the normal equations; retain r.
2. Explain why three rows need not provide three independently adjustable coefficients.
3. Check every reconstruction entry for y=(2,3,6).
4. What extra information is lost if only the residual squared length is stored?

## Worked answers

1. The equations are 2c1+c2=4 and c1+2c2=4. Subtraction gives c1=c2; hence c=(4/3,4/3), represented=(4/3,4/3,8/3), r=(-1/3,-1/3,1/3).
2. There are only two column recipes; the third output is their sum. More readings do not create an additional coefficient direction.
3. 7/3-1/3=2; 10/3-1/3=3; 17/3+1/3=6.
4. Signs and channel positions disappear. For instance r and -r have the same squared length but reconstruct different input vectors.

**Boundary to carry forward:** C21-DEC-D1: y=(1,1,3) gives c=(4/3,4/3), r=(-1/3,-1/3,1/3). Three channels do not imply three independently recoverable coefficient coordinates; here rank is two.

**Next dependency:** [lesson-02](lesson-02.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# lesson-02: Rank and retained syndromes

2 sessions of 55 minutes.

**Essential question:** What does an independent residual coordinate preserve?

**Goals**

- Count independent column and residual directions.
- Recover a full residual vector from its declared coordinate and basis.
- Distinguish real-space equality from integer-lattice equality.

## Prerequisite bridge

Lesson 1 taught row multiplication, dot products and reconstruction. We now ask how many freely chosen numbers each part needs. Keep A_small and its ordered three channels. All computations still use exact fractions.

<a id="C21.02-E1"></a>
## Explanation — C21.02-E1

A column direction is independent of others if it cannot be made by combining them. For A_small, a times (1,0,1) plus b times (0,1,1) is zero only if a=0 and b=0, because its first two entries are a and b. The rank is therefore two. A vector space allows any real multiples and sums of its directions. The image of a matrix is the set of outputs it can make; its kernel is the set of inputs it sends to zero.

The residual conditions r1+r3=0 and r2+r3=0 imply r=(-t,-t,t). Choose t=r3 freely and the other entries are fixed. The residual subspace, also called the left-null space of A_small, therefore has one independent coordinate. We may save t together with the basis vector (-1,-1,1), but saving t without that convention is ambiguous. This course saves the full vector as well. Here the word syndrome names retained coordinates outside the represented image, not an error verdict.

The three numbers (c1,c2,t) reconstruct y=(c1-t,c2-t,c1+c2+t). Conversely y3-y1-y2=3t, so t=(y3-y1-y2)/3, c1=y1+t, and c2=y2+t. This gives an independent route to the previous answers. For (2,3,6), t=(6-2-3)/3=1/3. These formulas demonstrate lossless separation, not merely a count of dimensions.

Real numbers and integers support different claims. Write Z for the integers. An integer lattice consists of integer combinations of the declared columns. Take A0=(2,0)^T and L0=(0,1). The first maps a number a to (2a,0); the second maps (x,y) to y. Over R, the image of A0 and kernel of L0 are both the entire horizontal line. Over Z, the image contains only even horizontal coordinates, but the kernel contains (1,0). Their ranks agree and L0 A0=0, yet their integer sets differ.

A lattice is saturated in its real span if every integer point in that span already belongs to the lattice. The even horizontal lattice is not saturated. Replacing A0 by (1,0)^T repairs this example: (n,0)=A0 n for every integer n. In lesson 3 we will prove saturation for the particular source matrix using an integer coefficient extractor. This is stronger evidence than an unsupported appeal to matching rank.

> Scope: S02 /proof_nodes/10 reports an integer exact-sequence statement, while its displayed dimension argument alone establishes the real-space part. S03 /findings/8 flags the missing source L. We keep the reported status, the argument’s scope and the missing object separate; the small counterexample is freshly checked teaching mathematics.

At the first unit boundary, explain the distinction aloud: A_small^T r=0 says two sums cancel. It does not say each of the three entries of r vanishes. A full residual can remain even when the decoder equations are solved exactly.

<a id="C21.02-W1"></a>
## Worked example — C21.02-W1

Reuse C21-DEC-EX1: t=1/3, so the two represented coordinates plus one syndrome coordinate reconstruct y. Over R, A0=(2,0)^T and L0=(0,1) have ranks one and L0 A0=0; their real image/kernel coincide. Over Z, (1,0) lies in ker L0 but not im A0, so rank alone fails to prove lattice equality.

<a id="C21.02-P1"></a>
## Guided practice — C21.02-P1

Try the operation before reading the solution. For A0=(1,0)^T and L0=(0,1), integer equality does hold: every kernel point is (n,0)=A0 n. For y=(1,1,3), explicitly check (-1/3+1/3,-1/3+1/3)=(0,0) and reconstruct the three entries.

<a id="C21.02-D1"></a>
## Diagnostic checks — C21.02-D1

1. For y=(1,1,3), find t and reconstruct y.
2. Why is A_small^T r=0 compatible with a nonzero r?
3. Show integer image/kernel equality for A0=(1,0)^T and L0=(0,1).
4. What fails if only rank is supplied for the even-lattice example?

## Worked answers

1. t=(3-1-1)/3=1/3; c1=c2=4/3. Reconstruction is (1,1,8/3+1/3)=(1,1,3).
2. The constraints concern sums r1+r3 and r2+r3; (-1,-1,1) satisfies them without being zero.
3. L0(x,y)=0 forces y=0. Every integer (n,0) is obtained by applying A0 to integer n, and every such output is in the kernel.
4. Rank counts real directions, not missing integer points. (1,0) is a specific missing point demonstrating the failure.

**Boundary to carry forward:** A zero normal residual A^T r is not a zero channel residual r. A lattice claim needs saturation or index evidence in addition to field rank. Missing source L cannot be recovered by naming the orthogonal projector L.

**Next dependency:** [lesson-03](lesson-03.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# lesson-03: The thirteen-channel decoder

3 sessions of 55 minutes.

**Essential question:** How can thirteen readings be retained as six represented and seven residual coordinates?

**Goals**

- Use the source matrix in its stated order and verify its rank.
- Reconstruct a full thirteen-channel ledger.
- Distinguish the integer extractor from the missing source syndrome map.
- Check a small character table and a specified intertwiner.

## Prerequisite bridge

Lesson 2 taught image, kernel, rank, integer lattices and residual bases. This lesson extends the same operations to a larger rectangular table. Work in three sessions: channel decoding; integer extraction; signed characters. Long tables are for careful checking one row at a time, not memorization.

<a id="C21.03-E1"></a>
## Explanation — C21.03-E1

S02 /backbone_sequence/16 (M17) supplies the following 13 by 6 matrix A. Row i means channel i; column j multiplies coefficient cj. Keep this ordering. Its columns correspond to the renderer order b=(1,alpha,alpha^2,alpha^3,a_e,eta), which lesson 4 interprets. The classroom calculations use dimensionless channels.

```text
0 0 1 0 0 0
0 1 0 0 0 0
0 1 1 0 0 1
0 1 1 0 0 -1
1 0 0 0 0 0
1 0 1 0 1 0
1 0 1 0 -1 0
1 1 0 1 0 0
1 1 1 1 1 1
1 1 1 1 -1 -1
1 1 0 -1 0 0
1 1 1 -1 1 -1
1 1 1 -1 -1 1
```

For c=e1=(1,0,0,0,0,0), multiplying A by c simply selects column 1: (0,0,0,0,1,1,1,1,1,1,1,1,1). This is the safest first check of the row order.

The Gram matrix is G=A^T A: its entry (j,k) is the dot product of columns j and k. Column 1 has nine ones, so G11=9; columns 1 and 2 overlap in six ones, so G12=6. Carrying out the remaining dot products gives a top-left block [[9,6,6],[6,9,6],[6,6,9]], bottom-right block diag(6,6,6), and zeros between. This G is only a decoder Gram matrix, not M_cell or G_phase.

The first block acts on (a,b,d) by 3(a,b,d)+6(a+b+d)(1,1,1). On the constant direction (1,1,1) it multiplies by 21. On directions whose entries sum to zero it multiplies by 3. A direction scaled without changing direction is called an eigenvector, and the scale is its eigenvalue. Every triple is a constant triple plus a sum-zero triple: subtract its mean (a+b+d)/3 from each entry. Thus no nonzero triple is sent to zero. The last three directions multiply by 6. All six coefficients can therefore be recovered uniquely; rank A=6. Thirteen total channel coordinates minus six independent represented directions leaves seven independent residual directions.

You do not need a general matrix-inverse algorithm to decode this A. First calculate d=A^T y by column dot products. Set S=(d1+d2+d3)/21. Then c1=(d1-6S)/3, c2=(d2-6S)/3, c3=(d3-6S)/3, and cj=dj/6 for j=4,5,6. Why? S=c1+c2+c3 and the first three normal equations read dj=3cj+6S. Summing them gives 21S=d1+d2+d3.

For y=(1,2,...,13), d=(81,72,65,-9,-3,-1); S=218/21. The equations yield c=(131/21,68/21,19/21,-3/2,-1/2,-1/6). Multiply each row and subtract to obtain this complete ledger:

| channel i | y_i | (Ac)_i | s_i |
| --- | --- | --- | --- |
| 1 | 1 | 19/21 | 2/21 |
| 2 | 2 | 68/21 | -26/21 |
| 3 | 3 | 167/42 | -41/42 |
| 4 | 4 | 181/42 | -13/42 |
| 5 | 5 | 131/21 | -26/21 |
| 6 | 6 | 93/14 | -9/14 |
| 7 | 7 | 107/14 | -9/14 |
| 8 | 8 | 335/42 | 1/42 |
| 9 | 9 | 115/14 | 11/14 |
| 10 | 10 | 401/42 | 19/42 |
| 11 | 11 | 461/42 | 1/42 |
| 12 | 12 | 485/42 | 19/42 |
| 13 | 13 | 171/14 | 11/14 |

For example row 3 predicts c2+c3+c6=68/21+19/21-1/6=167/42; adding -41/42 recovers 3. All thirteen rows are retained. The six sums A^T s vanish. The seven-dimensional syndrome is stored here as thirteen entries constrained by those six equations. A specified seven-element basis could compress the entries reversibly; the source’s particular basis is not supplied.

Compact recognition notation: Aplus=(A^T A)^(-1)A^T names the recipe just derived; inverse means the operation undoing a nonsingular matrix. P=A Aplus extracts represented channels and R=I-P extracts the residual; I leaves every vector unchanged. Since Aplus A=I6, applying P twice gives P again, as does applying R twice. Also A^T R=0. The verification file checks these exact identities. R is a 13 by 13 projector and is not the missing 7 by 13 source L.

There is a different, integer extractor for vectors already in the image. If z=Ac, then c1=z5, c2=z2, c3=z1, c4=z8-z5-z2, c5=z6-z5-z1, c6=z3-z2-z1. These six recipes define L_int, a 6 by 13 integer matrix, with L_int A=I6. Recognition-only certificate vocabulary: their selected rows (5,2,1,8,6,3) form a triangular 6 by 6 matrix (entries above its main diagonal are zero). For a triangular matrix the determinant is the product of diagonal entries, here 1. A square submatrix with determinant 1 or -1 is called a unit minor. The explicit integer recipes, rather than determinant vocabulary, are the core proof used next. An integer z in the real image consequently has integer c=L_int z, proving saturation for this A. If an integer rank-seven source L with LA=0 is supplied, real image/kernel equality plus this saturation establishes integral equality. The extractor does not identify that L. Applied to arbitrary y outside the image, it is not the Euclidean decoder; rational c remains possible.

### A finite bridge to signed characters

Use two-bit labels 00,01,10,11. Addition of labels is bitwise addition modulo 2 (1+1 becomes 0). For a row label x and column label k, multiply matching bits, add, and set W[x,k]=(-1) raised to that sum. Even sums give +1; odd sums give -1. A character is a sign recipe respecting addition: the sign for x+x-prime is the product of the two signs. The table is

```text
       00  01  10  11
00      1   1   1   1
01      1  -1   1  -1
10      1   1  -1  -1
11      1  -1  -1   1
```

Each column has squared length 4; two different columns have dot product zero (for columns 01 and 10, the products are 1,-1,-1,1). Hence W^T W=4I and coefficients a=W^T v/4 reconstruct v=Wa. For v=(1,2,3,4), the four sums are 10,-2,-4,0, giving a=(5/2,-1/2,-1,0). The first reconstructed entry is 5/2-1/2-1=1; the others are 2,3,4.

A representation describes how each group operation acts on coordinates. To compare two actions rho and sigma, an intertwiner T must obey T rho(g)=sigma(g) T for every operation g. In the two-action example below it is enough to check the nonidentity involution (an operation whose square is identity). With rho=diag(1,-1), sigma=diag(-1,1), swapping coordinates by T=[[0,1],[1,0]] gives both products [[0,-1],[1,0]]. T is invertible, and 2T also works, so compatibility does not choose a unique map. In contrast rho has a fixed nonzero vector (1,0), whereas -I has none; an invertible intertwiner to -I cannot preserve that action. Their traces, the sums of diagonal entries, are 0 and -2, another obstruction.

> Source boundary: S02 /branch_proofs/11 reports closed exact module compatibility; /proof_nodes/10, /11 and /23 give the active/syndrome and character claims. Conditional arithmetic 3(1,1,1)+2(2,0,-1)=(7,3,1) and 3²+2²=13 is checkable here. The representation-theory interpretation requires the source actions. Source L (7 by 13) and W7 (eight group elements by seven nonconstant characters, ordered source action not loaded) remain VERIFIED_NOT_LOADED under S03 /findings/8. This toy 4 by 4 W and derived L_int do not replace them.

<a id="C21.03-W1"></a>
## Worked example — C21.03-W1

Rank A=6, left-nullity=7. Set Aplus=(A^T A)^-1 A^T, P=A Aplus and R=I-P. For the supplied worked ledger y=(1,...,13), use every exact c, represented and syndrome entry in the verification record. Check P^2=P, R^2=R, A^T R=0 and y=A c+s. Demonstrate the simpler c=e1 example by reading the first A column.

<a id="C21.03-P1"></a>
## Guided practice — C21.03-P1

Try the operation before reading the solution. Use c0=(1,-1,2,0,1,0) and s=(-2,-2,1,1,0,0,0,0,0,0,0,0,0). Form y=A c0+s. A^T s=0, so decoding returns c0 and this entire s. Compare against the exact practice ledger. The 13 residual entries satisfy six constraints; they are not 13 independent syndrome coordinates.

<a id="C21.S01-E1"></a>
## Supplemental explanation — C21.S01-E1

Use signed characters on the explicitly synthetic group (Z/2)^2 with rows/columns 00,01,10,11 and W[x,k]=(-1)^(x dot k). This four-character table is not W7. An intertwiner T obeys T rho(g)=sigma(g) T. Matching dimension is weaker than matching action; compatible actions still do not select one canonical T.

<a id="C21.S01-W1"></a>
### Worked example — C21.S01-W1

W=[[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]. W^T W=4I. For v=(1,2,3,4), a=W^T v/4=(5/2,-1/2,-1,0), and W a=v. Source character arithmetic 3(1,1,1)+2(2,0,-1)=(7,3,1) and 3^2+2^2=13 is conditional on the source representation data.

<a id="C21.S01-P1"></a>
### Practice with answer — C21.S01-P1

For v=(2,0,0,2), a=(1,0,0,1) and W a=v. On a separate two-dimensional involution example, rho=diag(1,-1), sigma=diag(-1,1), T=[[0,1],[1,0]] obeys T rho=sigma T and det T=-1; 2T also intertwines, demonstrating nonuniqueness.

<a id="C21.S01-D1"></a>
### Diagnostic boundary — C21.S01-D1

rho=diag(1,-1) and sigma=-I have equal dimension but traces 0 and -2, so no invertible intertwiner exists. The source L, W7 and their action conventions remain missing; the toy table and L_int do not fill that retrieval gate.

<a id="C21.03-D1"></a>
## Diagnostic checks — C21.03-D1

1. How many independent coefficients and syndrome coordinates occur? Why save thirteen residual entries?
2. Decode the c0 and s practice packet below; reconstruct its first four entries.
3. What does L_int prove, and why is it not source L?
4. For v=(2,0,0,2), compute the four signed coefficients and reconstruct v.
5. Why do equal-dimensional actions rho=diag(1,-1) and sigma=-I fail to have an invertible intertwiner?

## Worked answers

1. Six and seven. Thirteen entries carry the seven-dimensional residual with six constraints; this representation fixes channel meaning without inventing a basis.
2. Ac0=(2,-1,1,1,1,4,2,0,3,1,0,3,1). Adding s gives y=(0,-3,2,2,1,4,2,0,3,1,0,3,1). A^T s=0 so the decoder returns c0 and the full s.
3. L_int A=I6 provides integer recovery on the image and saturation. Its shape is 6 by 13 and product is identity, whereas source L is 7 by 13 with product zero.
4. W^T v=(4,0,0,4); divide by 4 to get (1,0,0,1). Adding columns 00 and 11 gives (2,0,0,2).
5. An invertible action-preserving map would send the nonzero fixed vector of rho to a nonzero fixed vector of -I, which has none. Equal dimension alone is insufficient.

**Boundary to carry forward:** The newly derived L_int is 6x13 and L_int A=I6. It proves saturation of this A via integer coefficient recovery, but it is not the source 7x13 L with L A=0, nor W7. Orthogonal decoding of arbitrary integer y may give rational c. Full source L/W7 replay remains VERIFIED_NOT_LOADED.

**Next dependency:** [lesson-04](lesson-04.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# lesson-04: Reconstruction and dimensional meaning

2 sessions of 55 minutes.

**Essential question:** What does a mass renderer add, and what information must remain beside it?

**Goals**

- Reconstruct channels before rendering a scalar.
- Evaluate a supplied dimensionless dot product and restore mass units.
- Identify missing occupied-state and reference-mass inputs.

## Prerequisite bridge

Lesson 3 supplied six coefficients and a complete syndrome. A dot product was taught in lesson 1. A ratio of two quantities with the same unit is dimensionless: 6 mass units divided by 2 mass units is the number 3.

<a id="C21.04-E1"></a>
## Explanation — C21.04-E1

A decoder answers how a channel vector splits under a declared geometry. A renderer answers a different question: what scalar is associated with supplied coordinates? M17 writes m/m_e=c dot b with b=(1,alpha,alpha²,alpha³,a_e,eta). In words, multiply c1 by 1, c2 by alpha, c3 by alpha², c4 by alpha³, c5 by a_e and c6 by eta, then add. Here alpha² means alpha times itself; alpha³ multiplies three copies. The renderer is dimensionless if c and b are dimensionless. Multiply by a supplied reference mass m_e to obtain a dimensional m.

The source stores alpha=0.0072973525643314245 and eta=1836.1526734259999, and describes a_e as an occupied-state coordinate. These are source witnesses with the displayed precision, not new measurements or newly established exact rational constants. A physically occupied coefficient state needs an explicit selection rule or supplied state. Solving the channel equations alone does not supply that rule. If a contributing renderer entry is missing, keep its term symbolic; for example, an absent a_e leaves c5 a_e symbolic when c5 is nonzero. If only the numerical reference mass m_e is absent, compute the dimensionless ratio m/m_e=c dot b from the supplied entries and retain m=(c dot b)m_e symbolically. Only the numerical dimensional mass remains unresolved in that case.

To practice the arithmetic without pretending to fill those gaps, use b_toy=(1,1/10,1/100,1/1000,1/5,2), and define m_ref=2 synthetic mass units. For c=(1,0,0,0,0,1), the ratio is 1+2=3 and mass is 3 times 2=6 mass units. These are separately declared classroom inputs. Retain c, b_toy, m_ref and s; the number 6 cannot reconstruct thirteen channels.

For the practice c=(0,2,0,0,1,0), the ratio is 2/10+1/5=2/5. Multiplying by m_ref gives 4/5 mass units. With s=0, the source channel matrix yields y=(0,2,2,2,0,1,-1,2,3,1,2,3,1). Even a zero syndrome must be saved as thirteen zero entries with its channel order. A negative channel in this synthetic linear system is permitted; it does not assert a negative physical mass.

Different c may give the same scalar dot product. For example in this toy renderer c=(1,0,0,0,0,0) and c=(0,10,0,0,0,0) both give ratio 1, but their channel vectors differ. Scalar rendering therefore does not replace channel decoding or residual preservation.

> Scope: The source renderer and its witness values are S02 /backbone_sequence/16. The toy renderer is synthetic and is never substituted for physical b. Neither an occupied-state rule nor a_e’s missing definition body is manufactured. Binding, coupling interpretation and measured mass require their own typed input records.

<a id="C21.04-W1"></a>
## Worked example — C21.04-W1

Small reconstruction: (7/3,10/3,17/3)+(-1/3,-1/3,1/3)=(2,3,6). For a separately synthetic renderer b_toy=(1,1/10,1/100,1/1000,1/5,2), c=(1,0,0,0,0,1) yields m/m_ref=3. If m_ref=2 mass units, m=6 mass units. Retain c and all syndrome entries.

<a id="C21.04-P1"></a>
## Guided practice — C21.04-P1

Try the operation before reading the solution. With the same b_toy, c=(0,2,0,0,1,0) gives 2/10+1/5=2/5; m=4/5 mass units for m_ref=2. Reconstruct a channel packet from this c and s=0 using the pinned A; do not substitute b_toy for source b.

### Answered practice: reference mass withheld

Use the existing synthetic c=(1,0,0,0,0,1) and b_toy=(1,1/10,1/100,1/1000,1/5,2), but withhold the numerical value of m_ref. Find the ratio and state exactly what remains unresolved.

**Answer:** c dot b_toy=1+2=3, so m/m_ref=3 and m=3*m_ref. The dimensionless ratio is completely computed. The numerical dimensional mass remains unresolved until m_ref is supplied. Keep the coefficient and syndrome records; withholding the reference mass does not erase their known values.

<a id="C21.04-D1"></a>
## Diagnostic checks — C21.04-D1

1. Compute the practice mass and list the required synthetic inputs.
2. Why does a mass ratio have no mass unit?
3. If a_e is missing and c5 is nonzero, what result can be reported?
4. Show why saving just m cannot preserve the syndrome.

## Worked answers

1. The ratio is 2/5 and m=4/5 mass units. Inputs: the six c values, b_toy, m_ref=2 mass units, A and thirteen zero s entries.
2. The numerator and denominator have the same unit, which cancels; restoring mass requires multiplication by a reference mass.
3. Report the symbolic term c5 a_e with the other known terms and mark the occupied-state input unresolved.
4. Changing s while keeping c fixed changes y=Ac+s but leaves c dot b unchanged. Thus many complete channel packets can share one rendered mass.

**Boundary to carry forward:** Neither b nor a solver chooses a physical occupied c. Missing contributing renderer entries leave their terms symbolic. If only m_e is absent, report the computable dimensionless ratio c dot b and retain m=(c dot b)m_e symbolically; the numerical dimensional mass is unresolved. A rounded report 2.33 is not exact 7/3; retain their difference.

**Next dependency:** [lesson-05](lesson-05.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# lesson-05: Atomic and isotope inventories

3 sessions of 55 minutes.

**Essential question:** Which atomic labels must be fixed before two masses can be compared?

**Goals**

- Compute a nominal composition label and verify allowed endpoint counts.
- Test dependent and independent composition-preserving moves.
- Balance synthetic constituent and charge ledgers before applying a mass-energy conversion.

## Prerequisite bridge

Lessons 1–4 taught linear maps and reconstruction. Composition counting is another linear map, but its inputs have different meanings: atom counts rather than decoder coefficients. Do not identify the two spaces merely because both use tuples.

<a id="C21.05-E1"></a>
## Explanation — C21.05-E1

An element identifies a nucleus by its proton count. Isotopes of the same element have different neutron counts. A neutral atom has equal numbers of electrons and protons; removing an electron makes its charge one elementary charge more positive. A molecular formula counts constituent atoms. An isomer has the same formula but a different arrangement. These labels answer different questions, so a report keeps them in separate fields.

Declare the order (C,H,N,O), where each letter is the count of carbon, hydrogen, nitrogen or oxygen atoms. S05 R008 defines nominal V=12C+H+14N+16O. For (4,4,0,1), V=12 times 4+4+14 times 0+16=68. The source calls the label nominal Da; here we say nominal units to distinguish the arithmetic from exact isotope masses. It is not a physical geometric volume despite the symbol V. Negative counts cannot describe an endpoint formula, though signed differences between valid formulas can be useful.

A fiber is the set of inputs sharing one output value. Different compositions can lie in the same V-fiber. A move U is an integer difference tuple; V stays fixed precisely when its weighted sum is zero. For U1=(-1,-2,1,0), the weighted sum is -12-2+14=0. For U2=(1,4,0,-1), it is 12+4-16=0. For U3=(0,2,1,-1), it is 2+14-16=0. But U1+U2=U3 entry by entry, so these are only two independent directions. U1 and U2 are independent because the N entry forces the coefficient of U1 to vanish in a zero combination, after which U2’s O entry forces its coefficient to vanish.

The move K=(-4,0,0,3) also preserves V because -48+48=0. It cannot equal aU1+bU2: its N entry would force a=0, its H entry then forces 4b=0, leaving no C change. K adds a third direction. One constraint on four real coordinates leaves three independent directions; integer-lattice basis questions still require more than a rank count. These moves establish independent directions, not automatically a full integer basis.

Starting from (4,4,0,1), U1 gives (3,2,1,1), whose label is 36+2+14+16=68. U2 gives (5,8,0,0), whose label is 60+8=68. K sends (4,0,0,0) to (0,0,0,3); both labels are 48. Attempting K from (1,0,0,0) would give (-3,0,0,3), an invalid endpoint. A nominal count move is not automatically a physically balanced reaction: carbon and oxygen nuclei are different constituent types.

### Before subtracting endpoint masses

For a synthetic assembly A+B → AB, declare conserved labels A and B. Initial inventory is one A label and one B label; final AB contains exactly those same labels. Declare all three objects neutral and in the specified reference state, so total charge is zero on both sides. Declare each listed mass to include the entire object and its electrons and binding state. Isotopic identities are stipulated unchanged constituents, not inferred from nominal integer weights. There is no emitted unlisted object in this classroom ledger.

Use the reference relation Q_release=(m_initial-m_final)c_light². The symbol c_light is the speed entering mass-energy conversion, not the coefficient vector c. Positive Q_release means energy available by this endpoint difference; negative Q_release means required energy input under the convention. For classroom arithmetic stipulate a synthetic conversion of 1 u times c_light²=10 E_unit. This is not the physical numerical conversion for an atomic mass unit; u here is a declared mass unit in the synthetic problem.

With complete-object masses A=2u, B=3u, AB=4.9u, initial mass is 5u. Subtract final mass to retain delta m=0.1u. Multiply by 10 E_unit/u to get Q_release=1 E_unit. Setting AB=5.05u changes delta m to -0.05u and Q_release to -0.5 E_unit. The latter requires input of 0.5 E_unit; do not erase the sign or normalize it away.

If the initial masses include electrons but the final mass describes a bare positive ion, this ledger is incomplete. Specify the removed electron and consistent binding/ionization states before subtracting; a missing mass cannot be guessed. Even equal formulas can represent different binding states or isomers.

> Source scope: S05 /records/7 is archive_stated nominal composition arithmetic. /records/21 reports dependence of three tested moves; /records/22 reports the independent 4C↔3O direction and a mass-step claim of 15.25614129 mDa (one mDa is one thousandth of a dalton). That decimal and its source claim of exactness are attributed synthesis, not a fresh isotope-mass replay: the required isotope constants and full endpoints have not been loaded. We freshly verify nominal invariance and independence only. R032’s three rank-three structures do not supply a canonical connecting map.

<a id="C21.05-W1"></a>
## Worked example — C21.05-W1

C21-RXN-EX1: synthetic A+B -> AB conserves stipulated A and B constituent counts and charge. All are complete objects in one reference convention. Masses 2u+3u ->4.9u with synthetic 1u c^2=10 E_unit give delta m=0.1u and Q=1 E_unit. The mass difference is retained; this is not a measured reaction.

<a id="C21.05-P1"></a>
## Guided practice — C21.05-P1

Try the operation before reading the solution. C21-RXN-P1: keep every endpoint label but set final mass 5.05u. Delta m=-0.05u and Q=-0.5 E_unit, requiring input 0.5 E_unit. Separately calculate V for (C,H,N,O)=(4,4,0,1): V=68 nominal units. Neither calculation identifies an isomer.

<a id="C21.S02-E1"></a>
## Supplemental explanation — C21.S02-E1

Declare tuple order (C,H,N,O) and weights (12,1,14,16). Use U1=(-1,-2,1,0), U2=(1,4,0,-1), U3=(0,2,1,-1), K=(-4,0,0,3). Check nonnegative endpoints separately. The weights are nominal composition arithmetic, not exact isotope masses.

<a id="C21.S02-W1"></a>
### Worked example — C21.S02-W1

All four weighted moves are zero and U3=U1+U2. Starting (4,4,0,1), U1 gives (3,2,1,1), both V=68. The first three moves have rank two. If K=aU1+bU2, the N row forces a=0 and the H row b=0, a contradiction; K adds a third direction.

<a id="C21.S02-P1"></a>
### Practice with answer — C21.S02-P1

From (4,4,0,1), U2 gives (5,8,0,0), both V=68. From (4,0,0,0), K gives (0,0,0,3), both V=48. Explain why these are valid count endpoints but not an asserted physical carbon-to-oxygen reaction. S05 R023 reports a 15.25614129 mDa step as source synthesis; no missing isotope constants are invented to replay it.

<a id="C21.S02-D1"></a>
### Diagnostic boundary — C21.S02-D1

Negative atom counts invalidate an endpoint. Same V does not mean same formula, isotope mass, isomer or charge state. The three rank-three fibers in R032 recur structurally, but their canonical connecting map is unresolved.

<a id="C21.05-D1"></a>
## Diagnostic checks — C21.05-D1

1. Calculate V for (3,2,1,1), and compare it with (4,4,0,1).
2. Show U3=U1+U2 and explain why K supplies another direction.
3. Apply K to (1,0,0,0). Is this a valid composition endpoint?
4. For the neutral synthetic A+B → AB, calculate Q if final mass is 5.05u.
5. What must be repaired if a final positive ion is compared with initial neutral masses?

## Worked answers

1. 36+2+14+16=68, equal to 48+4+16=68. The formulas differ despite their common label.
2. The sum is (0,2,1,-1). If K=aU1+bU2, N forces a=0 and H forces b=0, contradicting K≠0.
3. The result (-3,0,0,3) has a negative C count and is invalid, though K remains a formal kernel direction.
4. 5-5.05=-0.05u; multiplying by the declared 10 E_unit/u gives -0.5 E_unit. Input 0.5 E_unit is needed.
5. Include removed electrons and consistent charge, isotope and binding/reference states for all whole objects; until supplied, mark the endpoint incomplete rather than compute an unsupported difference.

**Boundary to carry forward:** C21-RXN-D1: initial neutral-object masses and final bare-ion masses cannot be subtracted under an unstated electron convention. Supply all electrons and ionization/binding states first, or mark the endpoint incomplete. A nominally invariant composition move is not by itself a balanced physical reaction.

**Next dependency:** [lesson-06](lesson-06.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# lesson-06: Binding and periodic organization

2 sessions of 55 minutes.

**Essential question:** How can an atomic application be source-traced while its missing coordinates remain explicit?

**Goals**

- Classify each source card as synthesis, mechanism or unresolved record.
- Build a periodic-coordinate ledger without inventing values.
- Compute an energy difference and distinguish it from a rate or power.

## Prerequisite bridge

Lesson 5 separated formula, isotope, charge, arrangement and binding state. Lesson 3 showed why equal dimensions do not specify an action-preserving map. We now use both ideas to read an archival application without filling its gaps by analogy.

<a id="C21.06-E1"></a>
## Explanation — C21.06-E1

A source-traced report records what a document actually supplies and which operation was freshly checked. The source cards below are bounded readings of S05. The exact file path and digest appear in sources.md; record numbers use one-based labels but JSON pointers use zero-based array positions.

| Card | Pointer | Stored class | What the course can carry forward |
| --- | --- | --- | --- |
| R029 | /records/28 | synthesis | A proposed periodic coordinate package: base Cell3 address plus nested coordinate fibers. |
| R030 | /records/29 | synthesis; type mechanism | Nuclear, chemical and orientational relations as distinct types of edges. |
| R031 | /records/30 | archive_stated; type unresolved | Formula and nominal label leave isomers unresolved; preserve graph and binding information. |
| R032 | /records/31 | synthesis; type architecture | Three rank-three structures recur, while a canonical connecting map remains absent. |

A graph is a collection of vertices and edges: objects and their declared connections. An adjacency table records which vertex pairs connect; graph identity includes the labeled vertices and full edge list. A Laplacian is the degree table minus the adjacency table (degree counts the incident edges). Its spectrum is a list of eigenvalues, using the scaling-direction idea from lesson 3. These terms are recognition-only here: no unprovided molecular graph is assigned. A spectrum compresses a graph and need not uniquely identify it, so preserve graph identity alongside any spectral summary. An edge labeled chemical rearrangement is not the same operation as a nuclear change or an orientational coupling.

For a source-traced worked row, start with the synthetic composition (4,4,0,1). We know the counts and derived nominal V=68. R029 requests many more coordinates. A correct report looks like this:

| Field requested by R029 | Present value/status in this classroom packet |
| --- | --- |
| Composition counts, nominal label | (4,4,0,1), V=68; synthetic and freshly computed |
| Base Cell3 address | Not supplied |
| Scale/face sector and isospin lambda | Not supplied; source-local labels |
| Three composition-null coordinates | No basis and origin for this point supplied; invariant moves checked separately |
| Exact isotope mass | Not supplied; nominal weights do not replace it |
| Graph identity and spectrum | Not supplied; formula alone is insufficient |
| Charge/parity | Not supplied for this composition row; do not borrow synthetic A/B charge |
| Binding residual | Not supplied; retain as a required coordinate |
| QPC phase tensor | Not supplied; source-local phase-cost object, recognition only |
| Occupied coefficient selection | Not supplied; R030 edge classes do not select c |

The repeated rank three in R032 is an explanatory target: composition-null directions, a geometric isofacial tangent fiber and the EG three-channel phase transform. We have constructed only the composition arithmetic. A meaningful map would need typed domains, units, bases, actions and a rule taking one object to the other. The rank count alone is insufficient. No Cell3 metric, physical coordinate or phase tensor is introduced numerically in this course; their source-local meanings are not merged with our decoder Gram matrix.

### Energy, rate and power have different input requirements

Retain the complete neutral-object convention of lesson 5 and its synthetic conversion. For AB=4.8u, delta m=2+3-4.8=0.2u, and Q_release=2 E_unit. This is an endpoint difference. It supplies no duration, transition frequency or usable-energy fraction. A rate counts events per time; average power is energy delivered divided by duration. If a separate premise says this 2 E_unit release is delivered over 4 time units and half is recovered, recovered energy is 1 E_unit and mean recovered power is 1/4 E_unit per time unit. The duration and fraction must remain in the ledger.

The reference relation delta E=delta m c_light² concerns differences of rest energies of specified complete objects. It does not turn phase into force or a model energy into measured transferred energy. Our numerical conversion is stipulated, so every constant needed for the calculation is supplied locally; no external mass table is required.

> Claim scope: R029 and R030 are archival synthesis and proposed mechanism. The ledger’s missing fields are unresolved inputs, not zero values. The energy arithmetic is a synthetic application of a declared reference relation. No physical periodic address, nuclear reaction rate, binding force or occupied-state selection is claimed by these exercises.

<a id="C21.06-W1"></a>
## Worked example — C21.06-W1

Build a source-traced row: S05#/records/28 (R029) requests address, scale/face sector, lambda, composition-null coordinates, isotope mass, graph spectrum, charge/parity, binding residual and QPC phase tensor. For the synthetic composition from lesson05, only counts and nominal V are supplied; mark all other values not supplied. R030 describes edge classes rather than choosing coefficients.

<a id="C21.06-P1"></a>
## Guided practice — C21.06-P1

Try the operation before reading the solution. S05#/records/30 (R031) says formula/nominal volume leave isomers unresolved; retain adjacency or Laplacian data and binding residual. S05#/records/31 (R032) compares three rank-three fibers but supplies no canonical isomorphism. Complete a row with those exact source statuses. Repeat A+B -> AB with final 4.8u: Q=2 E_unit.

<a id="C21.S03-E1"></a>
## Supplemental explanation — C21.S03-E1

Repeat the declared Q_release=(m_initial-m_final)c^2 relation with balanced constituents/charge, complete-object masses, reference state and conversion. Binding differences remain coordinates. Energy difference, transition rate and recoverable power require different inputs.

<a id="C21.S03-W1"></a>
### Worked example — C21.S03-W1

Use synthetic neutral complete objects A=2u, B=3u, AB=4.8u with conserved A/B labels and 1u c^2=10 E_unit. Delta m=0.2u and Q=2 E_unit. No duration or efficiency was supplied, so power is not determined.

<a id="C21.S03-P1"></a>
### Practice with answer — C21.S03-P1

Repeat final AB=5.05u under the same balanced convention: Q=-0.5 E_unit. If, in a separate stipulated release example, 2 E_unit is delivered over 4 time units with efficiency 1/2, recovered mean power is (1/2)*2/4=1/4 E_unit per time unit. Those extra premises must be recorded.

<a id="C21.S03-D1"></a>
### Diagnostic boundary — C21.S03-D1

A positive Q does not supply a rate. An ion endpoint missing the removed electron fails bookkeeping. Preserve mass difference and supplied binding state rather than normalizing the discrepancy away.

<a id="C21.06-D1"></a>
## Diagnostic checks — C21.06-D1

1. Which R029 fields are actually known for the composition (4,4,0,1)?
2. What are the different roles of R030 and R031?
3. Why does R032 not furnish a canonical map?
4. Compute Q for AB=4.8u, then compute recovered mean power with fraction 1/2 and duration 4.
5. Does positive Q alone determine a transition rate?

## Worked answers

1. Only the supplied counts and V=68; none of the other required coordinate values follows just from those counts.
2. R030 proposes typed binding/transition edges; R031 records unresolved isomer distinction and calls for graph and binding coordinates.
3. Three spaces of equal rank can have different bases, units and actions. The source explicitly does not supply a canonical connecting map.
4. Delta m=0.2u, Q=2 E_unit; recovered energy=(1/2)2=1 E_unit; divide by 4 time units for 1/4 E_unit per time unit.
5. No. A rate requires an additional time-dependent process or supplied event count and duration.

**Boundary to carry forward:** A shared rank of three does not furnish a canonical map. A graph spectrum may also be shared by distinct graphs, so retain graph identity as well. Source mechanism synthesis, supplied coordinates and freshly checked arithmetic must occupy separate fields.

**Next dependency:** [lesson-07](lesson-07.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# lesson-07: Solver convergence and unresolved information

2 sessions of 55 minutes.

**Essential question:** What can a failed numerical iteration teach us without losing its input?

**Goals**

- Perform two explicit solver updates and retain the full history.
- Explain convergence or divergence using two taught error directions.
- Distinguish numerical convergence, channel closure and physical identification.

## Prerequisite bridge

Use A_small and synthetic y=(2,3,6) from lesson 1. The exact solution c_star=(7/3,10/3) is already known. A sequence is an ordered list indexed n=0,1,2,...; c_n is simply the coefficient pair after n updates.

<a id="C21.07-E1"></a>
## Explanation — C21.07-E1

A solver is a rule for producing successive candidates. Declare c_0=(0,0) and a step parameter t. At every stage compute r_n=y-A_small c_n, then the two normal residual sums g_n=A_small^T r_n, then c_(n+1)=c_n+t g_n. Save n, t, c_n, r_n and g_n together. These are different fields: the normal residual is two sums; the channel residual is three entries.

For t=1/4, the initial normal residual is (8,9). Multiply by 1/4 to get c_1=(2,9/4). Its represented channels are (2,9/4,17/4), so r_1=(0,3/4,7/4). Adding first-plus-third and second-plus-third gives g_1=(7/4,5/2). Multiply that by 1/4 and add to c_1: c_2=(2+7/16,9/4+5/8)=(39/16,23/8). Subtract its channels from y to get (-7/16,1/8,11/16).

Step t=1/4

| n | c_n | r_n | A_small^T r_n |
| --- | --- | --- | --- |
| 0 | (0, 0) | (2, 3, 6) | (8, 9) |
| 1 | (2, 9/4) | (0, 3/4, 7/4) | (7/4, 5/2) |
| 2 | (39/16, 23/8) | (-7/16, 1/8, 11/16) | (1/4, 13/16) |

Step t=1

| n | c_n | r_n | A_small^T r_n |
| --- | --- | --- | --- |
| 0 | (0, 0) | (2, 3, 6) | (8, 9) |
| 1 | (8, 9) | (-6, -6, -11) | (-17, -17) |
| 2 | (-9, -8) | (11, 11, 23) | (34, 34) |

The t=1 branch is a useful comparison, not a discarded run. It first gives c_1=(8,9), so r_1=(2-8,3-9,6-17)=(-6,-6,-11). Thus g_1=(-17,-17), and c_2=(-9,-8). Reconstruction still works: (-9,-8,-17)+(11,11,23)=(2,3,6). The solver has moved away from its target while the retained packet remains exact.

To explain these branches without calculus, define coefficient error e_n=c_n-c_star. Since the exact solution obeys A_small^T y=G c_star with G=[[2,1],[1,2]], subtraction gives e_(n+1)=(I-tG)e_n. The sum direction (1,1) is multiplied by G by 3; the difference direction (1,-1) by 1. Every error (a,b) equals ((a+b)/2)(1,1)+((a-b)/2)(1,-1). Each update multiplies these two parts by 1-3t and 1-t respectively.

If a multiplier has absolute value less than one, repeated multiplication shrinks that component toward zero. For t=1/4, the multipliers are 1/4 and 3/4, so both shrink. For t=1, they are -2 and 0; the nonzero sum component flips sign and doubles each step. In general both shrink when 0<t<2/3. At the boundary t=2/3, the sum component flips without shrinking; at t=0 it does not move. These conclusions are about this explicit solver and matrix, not about all solvers.

Even as c_n approaches c_star, the channel residual approaches (-1/3,-1/3,1/3), not zero. Numerical convergence is reaching the decoder’s coefficients. Channel closure is whether r itself vanishes. Physical identification is whether the model coordinates and source selection rule describe the measured system. They are three distinct claims.

If columns are dependent, the normal matrix may be singular, meaning it has no unique inverse. For example two identical columns produce the same channels for coefficients (1,0) and (0,1). A solver must preserve the free-coordinate ambiguity, use additional declared constraints if supplied, and check compatibility; it must not invent uniqueness.

> Scope: These finite iteration histories are synthetic computations. Divergence exposes parameter dependence; it is not a reason to delete inputs, negative residuals or the failed branch. A scalar norm may index a history but cannot replace any saved coordinate.

<a id="C21.07-W1"></a>
## Worked example — C21.07-W1

For t=1/4, c0=(0,0), r0=(2,3,6); c1=(2,9/4), r1=(0,3/4,7/4); c2=(39/16,23/8), r2=(-7/16,1/8,11/16). Error multipliers 3/4 and 1/4 imply convergence to the previously solved c, whose full r remains nonzero.

<a id="C21.07-P1"></a>
## Guided practice — C21.07-P1

Try the operation before reading the solution. For t=1, c1=(8,9), r1=(-6,-6,-11), c2=(-9,-8), r2=(11,11,23). Error multiplier -2 exposes a divergent branch for these inputs. Preserve this branch and all signed entries. Compare against the exact trace instead of deleting the failed result.

<a id="C21.07-D1"></a>
## Diagnostic checks — C21.07-D1

1. Recompute c_2 and r_2 for t=1/4.
2. Recompute the t=1 branch through its second update.
3. At t=2/3, what happens to the sum-direction error?
4. If g_n=0, must r_n=0 or c_n represent a physical occupied state?

## Worked answers

1. c_2=(39/16,46/16); its third channel is 85/16. Subtract from (32/16,48/16,96/16) to get (-7/16,2/16,11/16).
2. c_1=(8,9), r_1=(-6,-6,-11), g_1=(-17,-17), c_2=(-9,-8), r_2=(11,11,23).
3. The multiplier 1-3(2/3)=-1 flips the sign without shrinking a nonzero component.
4. No. At c_star the two normal sums are zero while r_star=(-1/3,-1/3,1/3). Physical occupied-state selection is a separate, here missing, input.

**Boundary to carry forward:** Convergence of a numerical update is different from channel closure or physical identification. A singular normal matrix requires compatibility/free-coordinate handling; an unstable t does not erase the measurements.

**Next dependency:** [lesson-08](lesson-08.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-07 -->

<!-- BEGIN: lesson-08 -->
# lesson-08: A reproducible decoding report

1 sessions of 55 minutes.

**Essential question:** What must a report contain so another reader can reconstruct every result?

**Goals**

- Assemble a ledger separating input, definition, derivation and source status.
- Retain approximation differences independently of channel residuals.
- Reconstruct a report and identify unresolved source obligations.

## Prerequisite bridge

The previous lessons provided all required computations. This final lesson introduces no new physical model. It joins the channel, source, composition, endpoint and history ledgers into a report that a classmate can check.

<a id="C21.08-E1"></a>
## Explanation — C21.08-E1

A reproducible report tells the reader what was supplied, which operation was applied and what remains unresolved. A measured value comes from an actual observation with acquisition provenance. No new empirical measurement is supplied here: y is synthetic. A source coefficient or witness is a number stated by a document and must retain its source and precision. A derived coefficient is the result of a declared calculation. An approximant is a convenient replacement accompanied by its exact difference. A model output is conditional on model inputs and conventions.

For the worked packet, record y=(2,3,6), channel order 1,2,3, the three rows of A_small, field R, Euclidean inner product and dimensionless units. Derived c=(7/3,10/3); represented=(7/3,10/3,17/3); retained r=(-1/3,-1/3,1/3). The normal check is (0,0), but it is not a substitute for r. Reconstruct each entry before making an interpretation.

Suppose you display c1 as 2.33. This is exactly 233/100 as a decimal approximant. The rounding closure is 7/3-233/100=(700-699)/300=1/300. Store that separately. If both coefficients are displayed as (2.33,3.33), the exact-minus-displayed vector is delta c=(1/300,1/300), whose represented-channel difference is A_small delta c=(1/300,1/300,1/150). Then y=A_small c_display+r+A_small delta c. Rounding information and the original syndrome account for different differences.

The source ledger should identify S02 M17’s matrix and stored renderer witnesses, the missing source L and W7, and S05 R029–R032’s application statuses. A source label such as exact_representation_theory remains an attributed status when the action matrices required for fresh replay are absent. The course has independently recomputed the finite examples; it has not loaded every physical definition body.

For the practice packet y=(1,2,3), report c=(1,2), represented=(1,2,3), r=(0,0,0). Add the negative-Q endpoint record from lesson 5 with its neutral complete-object convention, initial 5u, final 5.05u, delta m=-0.05u, stipulated conversion 10 E_unit/u and Q=-0.5 E_unit. Attach the R029 row showing unsupplied atomic coordinates. These separate records do not turn the synthetic channel into an isotope measurement.

> Report scope: Retain observations if any are later supplied, derived transforms, proposed mechanisms, established reference relations and unresolved inputs in separate fields. No outlier deletion, significance-based erasure or replacement of residual fields by scores is part of this course. Preserve source-local definitions and branches rather than harmonizing away their differences.

Before submitting, give a partner only the inputs and rules. Ask them to recompute a row, a signed residual and an endpoint difference. If the result requires guessing a unit, coefficient selection or source status, repair the earliest missing field. A compact report is successful when it is reconstructable, not when it hides the most information.

<a id="C21.08-W1"></a>
## Worked example — C21.08-W1

For the lesson01 packet, put synthetic y in the input field, A in the definition field, 7/3 and 10/3 in exact derived coefficients, and r=(-1/3,-1/3,1/3) in retained information. If displaying 2.33 for 7/3, record exact approximation closure 7/3-233/100=1/300 separately from the channel residual.

<a id="C21.08-P1"></a>
## Guided practice — C21.08-P1

Try the operation before reading the solution. Assemble the practice packet y=(1,2,3), c=(1,2), r=(0,0,0), plus the negative-Q endpoint ledger from lesson05 and the R029/R031/R032 source row. An auditor can reconstruct all channels and energy bookkeeping while seeing which atomic coordinates remain unprovided.

<a id="C21.08-D1"></a>
## Diagnostic checks — C21.08-D1

1. Classify y=(2,3,6), source alpha, 7/3, 2.33 and the toy rendered mass.
2. Compute the approximation closure for 7/3 displayed as 2.33.
3. What is missing from a report containing only c and a residual squared length?
4. What must remain unresolved in the source-traced atomic row?

## Worked answers

1. Synthetic input; source witness; exact derived coefficient; decimal approximant; conditional synthetic model output. None is a newly measured physical value.
2. 7/3-233/100=1/300; retain it separately from r1=-1/3.
3. The signed channel residual and its order/basis, plus any omitted input and decoder conventions. A scalar score cannot reconstruct y.
4. The unsupplied Cell3 address, typed additional fibers, isotope mass, graph data, charge/parity, binding residual, phase tensor and occupied-state rule; source L/W7 replay remains unloaded.

**Boundary to carry forward:** Do not relabel synthetic y as measured data, source alpha as an exact rational constant of nature, solver c as a selected occupied state, or a syndrome score as the complete syndrome. Each is a different report field.

**Next dependency:** [capstone](capstone.md). Use this lesson’s reconstruction and scope checks there.
<!-- END: lesson-08 -->
