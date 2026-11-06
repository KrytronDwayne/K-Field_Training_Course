# Lesson 5 — The typed Devon object

Essential question: How can a reduced record preserve geometry, scale, shape, scalar response, and branch information?

Goals: compute a diagonal metric/cofactor/reciprocal example; decode admissible branch modes; recover positive edge scale from an area anchor; label each component and inverse.

Bridge: Lessons 2 and 4 separated shape/scale and reconstructed tangent changes. Neither result says that geometry and integer branch records become the same kind of object. A typed record tells us what each number belongs to, its units, order, domain, source, and reconstruction rule.

## C10.05-E1 — A record with distinct components

The source Devon object includes the direct metric, cofactors, reciprocal metric, common scale, A2 area-shape fiber, scalar lift, branch modes, and invertible maps. We compute small diagonal examples; recognition of the broader object does not require university matrix theory.

Let B=[a b c] be a table whose columns are three edge vectors. In Cell3 those columns use ICRS coordinates and intentional negative determinant. Our positive diagonal B below is explicitly a different synthetic box, not the locked Cell3 basis. A diagonal table diag(p,q,r) has p,q,r on its diagonal and zero elsewhere. A transpose B^T exchanges rows and columns. The metric M_cell=B^T B stores edge dot products: entry ij is edge i dot edge j. For a diagonal B, M_cell=diag(p²,q²,r²). It measures squared lengths and angles; its entries have units LU².

For a diagonal metric diag(m1,m2,m3), its determinant is m1 m2 m3 and its cofactor matrix is diag(m2 m3,m1 m3,m1 m2). A cofactor is the signed determinant after deleting one row and one column; in this diagonal case the remaining two diagonal numbers multiply, and off-diagonal cofactors vanish. Units are LU⁴. These metric cofactors are distinct from cofactors of B itself. The reciprocal metric is R_cell=M_cell^-1=diag(1/m1,1/m2,1/m3), units LU^-2. Multiplying corresponding diagonal entries verifies M_cell R_cell=I. Equivalently divide each metric cofactor by det(M_cell), with units LU⁶, to get the reciprocal metric. We never rename this G_phase, the distinct phase metric.

The source M06 branch card defines S=C_b+C_c and A_branch=C_b-C_c. Its symbol is A in the source; here A_branch avoids collision with areas and dA. Adding and subtracting yields C_b=(S+A_branch)/2 and C_c=(S-A_branch)/2. For integer C_b,C_c, S and A_branch must both be even or both odd. This is an admissibility condition: S=3,A_branch=0 would yield halves and is not an integer branch pair. These are carry-side coordinates, not the shape projections u,v or detector parity. We decode supplied pairs; we do not generate a carry history or introduce a new nearest-integer tie convention.

| Component | Type/units | Retained information and return map |
|---|---|---|
| B and geometry | Ordered basis, LU; frame/orientation declared | Keep basis/orientation because metric alone loses absolute orientation |
| M_cell, cof(M_cell), R_cell | Matrices; LU², LU⁴, LU^-2 | B^T B; diagonal cofactors; reciprocal entries |
| m or s; A0 | Dimensionless common log coordinate; area | y=m1+z and areas=A0 exp(y) |
| u,v or z | Dimensionless area shape | y=s e_s+u e_u+v e_v with s retained |
| dG=dln Gamma2 | Dimensionless scalar tangent | Fixed-angle J inverse, with named branch and baseline context |
| S,A_branch | Integer branch coordinates, same parity | (S+A_branch)/2,(S-A_branch)/2 |

## C10.05-W1 — Worked synthetic ledger

For B=diag(1,2,3) LU, M_cell=diag(1,4,9) LU². Its determinant is 36 LU⁶, cofactors diag(36,9,4) LU⁴, reciprocal diag(1,1/4,1/9) LU^-2. The product diagonal is (1,1,1). Its orthogonal face areas are (2,3,6) LU²; with A0=1 LU² retain y=(ln2,ln3,ln6), m=(ln2+ln3+ln6)/3, u=(ln3-ln2)/sqrt2, v=(2ln6-ln2-ln3)/sqrt6. These need not be decimalized. A separate supplied synthetic branch pair S=2,A_branch=-2 gives C_b=0,C_c=2. Retain both records with their different labels. The tangent scalar relation may be stored as a map with no supplied dG value; do not manufacture a measurement.

## C10.05-P1 — Practice

For the separate synthetic B=diag(2,2,2) LU, calculate the three matrices with units and check the inverse. Decode S=4,A_branch=2. Classify m,u,v,dG and the branch pair; explain why B must be retained if orientation is needed.

Answer: M_cell=4I LU², determinant 64 LU⁶, cofactors 16I LU⁴, R_cell=I/4 LU^-2. Their product is I. C_b=(4+2)/2=3, C_c=(4-2)/2=1; recombination gives (4,2). Each area is 4 LU², so for A0=1 LU², m=ln4=2L and u=v=0. dG is a scalar tangent, not one of these shape entries. Rotating every basis edge together preserves all dot products, so M_cell does not recover the original frame orientation; keep B and its frame.

## C10.05-E2 — An area anchor fixes the remaining scale

At fixed known nondegenerate angles of a coherent three-edge geometry, divide A_bc by A_ab: l_b cancels, leaving (l_c/l_a)sin(theta_bc)/sin(theta_ab). Similarly A_bc/A_ac gives l_b/l_a times its angle factors. Thus, using the source ratios,

    k_c=l_c/l_a=(eta/1000) sin(theta_ab)/sin(theta_bc),
    k_b=l_b/l_a=(alpha_inverse/100) sin(theta_ac)/sin(theta_bc).

These ratios fix lengths only up to a common positive length t: (l_a,l_b,l_c)=t(1,k_b,k_c). In this section t is a LENGTH, unlike Lesson 3's dimensionless change parameter. Use the dimensional anchor A_ab=t² k_b sin(theta_ab). Divide by its positive dimensionless factor, then take the positive square root:

    t=sqrt(A_ab/[k_b sin(theta_ab)]).

Recompute all three areas to check compatibility with the supplied angles and ratios. The anchor determines size, not orientation or handedness.

## C10.05-W2 — Worked synthetic anchor

Orthogonal areas (6,8,12) LU² have sine factors all 1. eta=1000(12/6)=2000; alpha_inverse=100(12/8)=150. Therefore k_c=2, k_b=3/2. The anchor gives t=sqrt(6/(3/2))=sqrt4=2 LU. Lengths are (2,3,4) LU. Reconstructed areas are 2 times 3=6, 2 times 4=8, 3 times 4=12 LU².

## C10.05-P2 — Practice

Repeat with orthogonal areas (9,18,18) LU²; find both ratios, t and all lengths. State what remains undetermined if the anchor is omitted.

Answer: eta=2000, alpha_inverse=100, k_c=2, k_b=1. t=sqrt9=3 LU; lengths (3,3,6) LU. Products give (9,18,18) LU². Without the anchor, any positive t gives the same ratios; no absolute length is determined.

> Claim scope: The Devon list is S02#/backbone_sequence/6/devon_dimension; branch maps are /backbone_sequence/5/side_modes; area anchoring is /scale_uniqueness_theorem. Synthetic orthogonal boxes are not the mature locked Cell3. Neither a metric nor the anchor recovers its handed basis. The scalar lift remains separately sourced to M19 gravity_scalar_lift and is not a demonstrated force law.

## Diagnostic checks

1. **C10.05-D1:** Why is an unlabeled tuple of metric entries, u,v and branch modes insufficient?
2. **C10.05-D2:** What fails if angles or the dimensional anchor are omitted?
3. Is S=3,A_branch=2 an admissible integer pair?
4. What units does cof(M_cell)/det(M_cell) have?
5. Is a positive diagonal basis the locked Cell3 basis?

Worked answers: (1) It loses carrier, units, order and inverse metadata. (2) Without angles the length-ratio equations do not close; without anchor the positive length t is free. (3) No, because (3+2)/2=2.5 and (3-2)/2=0.5 are not integers. (4) LU⁴/LU⁶=LU^-2. (5) No; it is a declared synthetic comparison, while Cell3 preserves its source basis and negative determinant.

Next: [Lesson 6](lesson-06.md) tests the entire record. Pacing revised to THREE 55-minute periods: typed geometry, branch decoding, then anchor reconstruction. Each: 5 retrieval + 20 teaching/example + 15 practice + 15 checks. The extra period protects first-principles instruction without reducing coverage.
