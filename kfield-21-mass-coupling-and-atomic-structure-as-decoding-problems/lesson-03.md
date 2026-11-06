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
