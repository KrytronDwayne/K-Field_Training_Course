# Lesson 5 — Metric angles versus address angles

**Essential question:** Why can two perpendicular address axes represent physical directions that are not perpendicular?

**Goals:** Compare address and physical dot products; build a Gram matrix from step-vector pairings; retain cross terms when computing a squared physical length.

**Bridge:** Lesson 1 converts an address displacement v into physical displacement Bv. Lesson 3 taught dot products, and lesson 4 taught magnitude and unit directions. Here v and w are changes of address, not physical points; origin subtraction has already occurred when comparing two points.

## C04.05-E1 — Let the step vectors carry the geometry

The address e1=(1,0,0) means one a step. The address e2=(0,1,0) means one b step. Their ordinary address dot product is zero. But the actual steps are a=(1,0,0) LU and b=(1,2,0) LU. They both have a positive first physical component. The coordinate labels alone have hidden this overlap.

For two nonzero physical vectors p and s, their direction comparison is (p dot s)/(|p||s|). This equals the cosine of their angle: a number equal to 0 for a right angle, 1 for the same direction, and -1 for opposite directions. You only need the zero test for perpendicularity; calculating an inverse cosine in degrees is optional. The dot product formula is consistent with projection: p dot (s/|s|) is the signed length of p along s's unit direction, then dividing by |p| compares directions without lengths.

To avoid expanding every physical vector repeatedly, make a table of the direct step dot products. This is the **Gram metric** M_cell=B^T B. Transpose T swaps rows and columns, as in lesson 3. Entry ij is the dot product of column i with column j:

```text
             a     b     c
M_cell =   [ 1     1     0 ]
           [ 1     5     0 ] LU^2.
           [ 0     0     9 ]
```

The two off-diagonal 1 entries both matter. For address displacements v and w, the physical dot product is **(Bv) dot (Bw)=v^T M_cell w**. To compute the right side, multiply M_cell by w row by row, then dot with v. This formula follows by distributing (v1a+v2b+v3c) dot (w1a+w2b+w3c): each vi wj is multiplied by the corresponding step pairing.

For one displacement q, its squared physical length is q^T M_cell q=q1²+2q1q2+5q2²+9q3² LU². The cross term 2q1q2 combines q1q2(a dot b) and q2q1(b dot a). Their signs follow the inputs; they are never deleted because they complicate the calculation.

## C04.05-W1 — An address right angle is not a physical right angle

e1 dot e2=0. Their physical images are a and b, so a dot b=1 LU², |a|=1 LU, and |b|=sqrt(5) LU. Thus cos(angle)=1/sqrt(5), not zero. The directions are not perpendicular. The Gram method gives the same answer: M_cell e2=(1,5,0) LU², and e1 dot this triple is 1 LU².

## C04.05-P1 — Test the third direction two ways

Check whether a and c are perpendicular, then b and c, using physical components and Gram entries. Calculate the cosine for each pair. Also compute the physical squared length of address displacement (1,-1,0).

**Worked answer:** a dot c=1×0+0×0+0×(-3)=0; b dot c=1×0+2×0+0×(-3)=0, so both are perpendicular pairs. M13=M31=M23=M32=0 confirms them. Their magnitudes are |a|=1, |b|=sqrt(5), |c|=3 LU, so the cosines are 0/(1×3)=0 and 0/(sqrt(5)×3)=0. For (1,-1,0), Bq=(0,-2,0) LU gives length squared 4 LU². The Gram expression gives 1-2+5=4 LU², including the negative cross term.

> **Claim scope and names:** M_cell here is the Gram construction evaluated on the explicitly synthetic B; its displayed numbers are not Cell3 constants. In the actual source, M_cell uses the locked Cell3 B in nm and has nm² units. The reciprocal Gram metric is R_cell=M_cell^-1, with inverse-square-length units. An inverse metric is not the reciprocal basis B^-T: it is a different matrix acting on different quantities. G_phase and G_eff are separate phase/effective metrics; distance Q, Q_g and Q_nu are separately typed source quantities. None is substituted for this physical Gram form. No assessment requires their advanced theory.

## C04.05-P2 — Practice a nonzero physical cosine

Compare address displacements v=e1 and w=(1,1,0). Find their physical dot product, magnitudes and cosine. Explain why both vectors must be converted before using the physical angle formula.

**Worked answer:** Bv=(1,0,0) LU and Bw=(2,2,0) LU. Their dot product is 2 LU² and their magnitudes are 1 LU and sqrt(8)=2sqrt(2) LU. Therefore the physical cosine is 2/(1×2sqrt(2))=1/sqrt(2). The address dot product and address lengths would describe the address graph, not the physical geometry carried by B.

## Diagnostic checks

1. **C04.05-D1:** For q=(1,1,0), calculate |Bq|² directly and through the Gram expression. Why is 1+5=6 incomplete?
2. Does a negative third column make the squared length of c negative?
3. Compute the physical dot product of address displacements v=(1,-1,0) and w=(1,0,0).
4. What units must v^T M_cell w have when v and w are dimensionless?

**Worked answers:** (1) Bq=(2,2,0) LU, giving 4+4=8 LU². The Gram expression is 1+2+5=8. The value 6 omits both cross terms. (2) No: c dot c=9 LU²; orientation and squared length are different properties. (3) Bv=(0,-2,0), Bw=(1,0,0), dot product 0. Using M_cell w=(1,1,0), v dot it is 1-1=0. These physical directions are perpendicular even though v dot w=1. (4) LU², inherited from the metric.

**Pacing:** 20 minutes explanation/worked example, 15 practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** [Lesson 6](lesson-06.md) combines physical geometry, exact ownership and retained display residuals in a reconstruction ledger.
