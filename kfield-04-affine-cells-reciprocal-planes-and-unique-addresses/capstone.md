# Capstone — A three-point cell-address atlas

Work for two 55-minute periods. Use the synthetic B with rows (1,1,0), (0,2,0), (0,0,-3) LU and O=(2,-1,4) LU from lesson 1. This is a classroom analogue, not measured Cell3 geometry. All input fractions are exact. You may consult the lessons and canonical source card. A calculator is optional; leave square roots exact.

Your atlas must retain every input, owner, local coordinate and signed display residual. Label physical entries in LU, reciprocal entries in LU^-1, and addresses as dimensionless. Keep the source-reading nm card separate.

## Tasks

1. **C04-CAP-01 — Convert and invert.** Make one row each for A: q=(1/2,-1/2,3/2), B: q=(-3/2,49/100,51/100), and C: q=(499/1000,0,0). Compute physical points x, then independently use x-O and inverse action to recover each q. State the column order and units.
2. **C04-CAP-02 — Assign owners.** For each row compute z=floor(q+1/2) and u=q-z. Check all three entries against [-1/2,1/2). Explain ownership of the exact positive and negative half boundaries in A and B, and C's near-boundary fraction.
3. **C04-CAP-03 — Count planes.** For h=(1,0,0), (0,1,0), (0,0,1), and (1,1,0), compute g_h and all three pairings with a,b,c. For point A, compute g_h dot (x-O) and h dot q for each label. Indicate which of these levels is an integer.
4. **C04-CAP-04 — Supply a physical ruler.** For those same four nonzero h labels, compute unit normals and consecutive-level spacings. Add h=(2,0,0) and explain why its spacing differs from h=(1,0,0). Explicitly exclude h=0 from normalization.
5. **C04-CAP-05 — Compare angles.** Compare e1 dot e2 with (Be1) dot (Be2), then report the physical cosine. Compute |B(1,1,0)|² two ways, retaining all cross terms.
6. **C04-CAP-06 — Reconstruct the ledger.** Reconstruct all three points using O+B(z+u). Display the addresses as A_disp=(1/2,-1/2,3/2), B_disp=(-3/2,1/2,1/2), and C_disp=(1/2,0,0). Calculate every signed residual r=q-q_disp, restore q, and show which owners a display-only calculation would get wrong. Retain exact reconstruction differences, even if zero.
7. **C04-CAP-07 — Resolve a source card.** Using the supplied canonical card, record all u,v,w normal and spacing lexemes, nm units, S02 pointer and source hash. Reject or accept this proposed u entry: canonical normal paired with 0.3295465297092934 nm. Cite S03's correction pointer and explain why a displaced source version is not a measurement residual. This is source reading, not recomputation of the locked decimals.

## Full worked answer key

### 1–2. Affine conversion and unique ownership

The columns are a=(1,0,0), b=(1,2,0), c=(0,0,-3) LU. Addresses, owners and local coordinates are dimensionless.

| Point | x (LU) | x-O (LU) | z | u |
|---|---|---|---|---|
| A | (2,-2,-1/2) | (0,-1,-9/2) | (1,0,2) | (-1/2,-1/2,-1/2) |
| B | (99/100,-1/50,247/100) | (-101/100,49/50,-153/100) | (-1,0,1) | (-1/2,49/100,-49/100) |
| C | (2499/1000,-1,4) | (499/1000,0,0) | (0,0,0) | (499/1000,0,0) |

Inverse action uses q2=d2/2, q3=-d3/3, q1=d1-d2/2. For A these give -1/2,3/2,1/2 in that solving order. For B they give 49/100,51/100,-101/100-49/100=-3/2. For C they give 0,0,499/1000. Reorder each result as (q1,q2,q3) to recover the supplied q.

At +1/2 the first owner is 1 and local coordinate -1/2; at -1/2 the owner is 0 and local coordinate -1/2. The negative boundary -3/2 belongs to owner -1, not -2. C remains strictly below +1/2 because 998<1000 after multiplication by 2000. Every local coordinate is at least -1/2 and strictly below +1/2.

### 3–4. Pairings, levels, normals and spacings

| h | g_h (LU^-1) | (g dot a,g dot b,g dot c) | A level | Unit normal n | Spacing (LU) |
|---|---|---|---|---|---|
| (1,0,0) | (1,-1/2,0) | (1,0,0) | 1/2 | (2,-1,0)/sqrt(5) | 2/sqrt(5) |
| (0,1,0) | (0,1/2,0) | (0,1,0) | -1/2 | (0,1,0) | 2 |
| (0,0,1) | (0,0,-1/3) | (0,0,1) | 3/2 | (0,0,-1) | 3 |
| (1,1,0) | (1,0,0) | (1,1,0) | 0 | (1,0,0) | 1 |
| (2,0,0) | (2,-1,0) | (2,0,0) | 1 | (2,-1,0)/sqrt(5) | 1/sqrt(5) |

For the first four rows, dotting g with (0,-1,-9/2) gives 1/2,-1/2,3/2,0. Dotting h with A's q gives the same list. Only the fourth of those four levels is an integer, so A lies on an integer-level plane of that family. The extra doubled label has integer level 1 too. The normal direction does not change under positive doubling, but all integer m are allowed, so 2q1=m includes halfway planes q1=1/2,3/2 and so on. h=0 gives g=0 and cannot be divided by its zero magnitude.

Magnitudes for the five rows are sqrt(5)/2, 1/2, 1/3, 1 and sqrt(5) LU^-1. Dividing each g by that magnitude gives the normals; taking the reciprocal magnitude gives the spacings. The signs in the third normal must be preserved.

### 5. Geometry

e1 dot e2=0 but a dot b=1 LU². Physical cosine is 1/(1×sqrt(5))=1/sqrt(5), so the physical directions are not perpendicular. B(1,1,0)=(2,2,0) LU gives squared length 8 LU². Using the Gram expression gives 1+2(1)(1)+5=8 LU²; dropping both cross terms would give the wrong answer 6 LU².

### 6. Reconstruction and display residuals

For A, z+u=(1/2,-1/2,3/2), with B(z+u)=(0,-1,-9/2) LU. For B, z+u=(-3/2,49/100,51/100), with B(z+u)=(-101/100,49/50,-153/100) LU. For C, z+u=(499/1000,0,0), with B(z+u)=(499/1000,0,0) LU. Adding O returns each x in the atlas table. Each reconstructed-minus-input physical difference is (0,0,0) LU.

| Point | r=q-q_disp | B r (LU) | Display-only owner | True owner |
|---|---|---|---|---|
| A | (0,0,0) | (0,0,0) | (1,0,2) | (1,0,2) |
| B | (0,-1/100,1/100) | (-1/100,-1/50,-3/100) | (-1,1,1) | (-1,0,1) |
| C | (-1/1000,0,0) | (-1/1000,0,0) | (1,0,0) | (0,0,0) |

B's displayed point is (1,0,5/2) LU; adding B r restores (99/100,-1/50,247/100) LU. C's displayed point is (5/2,-1,4) LU; its correction restores (2499/1000,-1,4) LU. Restore q_disp+r before ownership. A's zero residual is still retained. The local u is not interchangeable with display residual r.

### 7. Source reading

The full three rows are supplied in [canonical-card.md](canonical-card.md), which is part of this answer key and was read from S02 `/backbone_sequence/1/result/reciprocal_normals_u_v_w` and `/backbone_sequence/1/result/reciprocal_spacings_u_v_w_nm`. The same active fields occur in `/mature_locked_cell3`. The source SHA-256 is `6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3`.

Reject the proposed mixed entry. The u spacing must be **0.32954652969544673 nm**, matched to the canonical u normal. S03 `/findings/4` (AUD-005) explicitly marks the older witness superseded. Preserve it only as typed provenance. It is neither a measured fluctuation nor the display residual r of an atlas point. Unit normals are dimensionless; spacings use nm, and the arrays retain u,v,w order. These numerical cards are source-reported mathematical witnesses, not independent experimental measurements.

## Rubric: 100 points

| Step | Points | Award criteria |
|---|---|---|
| 01 | 15 | 3 for basis/origin/units, 6 for three forward points, 6 for inverse checks |
| 02 | 15 | 6 for owners, 6 for retained local coordinates/ranges, 3 for boundary explanation |
| 03 | 15 | 8 for four g vectors and pairings, 4 for matching affine levels, 3 for integer-level interpretation |
| 04 | 15 | 8 for four normals/spacings, 4 for doubled label and inserted planes, 3 for units and nonzero restriction |
| 05 | 10 | 5 for angle comparison/cosine, 5 for squared length by two methods with cross terms |
| 06 | 20 | 6 for three exact reconstructions, 6 for signed residuals and restoration, 4 for owner changes, 4 for typed differences and no deleted components |
| 07 | 10 | 4 for complete canonical rows/units/order, 3 for pointers/hash, 3 for rejecting mixed provenance with S03 |

Give method credit when a single arithmetic slip is propagated consistently. Require correction of wrong boundary convention, omitted origin, lost residual, mixed source branch or zero-vector normalization before marking the relevant capability mastered. The score describes performance; it is not a license to erase an incorrect or incomplete ledger.
