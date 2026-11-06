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
