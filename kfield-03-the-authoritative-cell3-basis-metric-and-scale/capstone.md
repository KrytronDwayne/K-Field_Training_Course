# Capstone — Two geometry cards with a checked boundary between them

Use two 55-minute periods. You may consult the lessons, terminology, geometry-card.md, sources.md and verification.json. Submit a calculation sheet labeled **Classroom analogue, not Cell3**, a separate locked Cell3 card, and a short precision note. All derivations use the taught small analogue. The locked card is a source-reading task; do not invert its decimal matrix by hand.

## Part A — Derive the classroom card (60 points)

Use B_ex=L[[1,1,0],[0,2,0],[0,0,−3]], with rows displayed and columns a,b,c. L is an arbitrary length unit.

1. Write a,b,c, calculate the displacement for q=(1,−1,2), and recover q from the displacement. State the roles of q, B_ex and the origin in x=O_K+B_ex q. (10)
2. Compute all entries of M_ex=B_ex^T B_ex. For q=(1,−1,0), find squared length using both external components and the metric. Identify the signed cross contribution. (12)
3. Calculate a×b, a×c, b×c, their magnitudes in ab/ac/bc order, det(B_ex), and unsigned volume. Explain the negative sign without changing an axis. (12)
4. Derive the inverse metric using the two-equation block method. Verify M_ex R_ex=I and B_ex R_ex B_ex^T=I, including units. Give a zero-volume counterexample and explain why the inverse identity does not apply. (16)
5. Choose the positive scale that makes the analogue's ab area 18L². Give its new ac area, determinant, and inverse-metric factor. Explain one invariant ratio and why an area anchor supplies information absent from ratios. (10)

## Part B — Read the actual locked Cell3 card (25 points)

6. Make a clearly separate record containing: the actual a and c columns with units; fixed axis convention; determinant and handedness; centered-cell ownership interval; ab/ac/bc face areas; and bc/ac/ab normalized area ray. Identify the source ID, full-file digest and exact pointers for B and face areas. Explain S01's historical role and S03's canonical confirmation. (15)
7. State the definitions and units of M_cell, R_cell and reciprocal basis D, and write the coordinate recovery formula with a declared origin. State the assumptions under which the supplied ratios give the positive length ray and an area anchor fixes t. Identify which physical inputs this course does not derive. (10)

## Part C — Keep the numerical information (15 points)

8. In the synthetic rounding example with stored 0.3333, compute 3·0.3333−1 and reconstruct the computed product. Distinguish that calculation from a measured physical discrepancy. (5)
9. The stored Cell3 reciprocal metric has R_12=0.0015348024281924184 and R_21=0.0015348024281924234 nm^−2. Compute R_12−R_21. Explain why a symmetric mathematical inverse can have unequal stored entries and what must be retained. (5)
10. Describe how to reproduce the new closure matrix E=M_stored R_stored−I, its units, and reconstruction rule. Why may the source-reported closure scalar not replace this matrix? Specify arithmetic and source identifiers rather than asserting that a small difference vanishes. (5)

## Complete answer key and analytic rubric

**1 (10):** a=(1,0,0)L, b=(1,2,0)L, c=(0,0,−3)L (3). B_ex q=a−b+2c=(0,−2,−6)L (2). Recover q_2=−2/2=−1, q_1=0−(−1)=1, q_3=−6/(−3)=2 (3). q counts edges without units, B_ex carries length, and O_K is the declared external origin added to the displacement (2).

**2 (12):** The nine dot products yield M_ex=L²[[1,1,0],[1,5,0],[0,0,9]] (6: one point for each independent diagonal/upper-triangle entry with symmetric completion). B_ex(1,−1,0)=(0,−2,0)L gives 4L² (2). q^T M_ex q=1+5−2=4L² (2); the two off-diagonal contributions sum to −2L² (2).

**3 (12):** Cross vectors are (0,0,2), (0,3,0), (−6,3,0), all in L² (6). Their magnitudes are 2,3,3sqrt(5), all in L² (3). a·(b×c)=−6L³, volume 6L³, negative orientation is intentional relative to the fixed ordered axes (3).

**4 (16):** Solve u+v=s, u+5v=t to obtain v=(t−s)/4 and u=(5s−t)/4. Thus R_ex=L^−2[[5/4,−1/4,0],[−1/4,1/4,0],[0,0,1/9]] (4). The upper block of MR has entries 1,0,0,1 from 5/4−1/4, −1/4+1/4, 5/4−5/4, −1/4+5/4; third diagonal 9/9=1 and remaining entries zero (4). B_ex R_ex=L^−1[[1,0,0],[−1/2,1/2,0],[0,0,−1/3]]. Multiplication by B_ex^T yields I because its second row gives (0,1,0), its third (0,0,1), and its first (1,0,0) (4). MR units L²L^−2 and BRB^T units LL^−2L cancel (2). Replacing c by (2,0,0)L gives zero triple product: the edges lie in a plane, so no invertible three-dimensional basis or inverse Gram matrix exists (2).

**5 (10):** 2s²L²=18L² gives s=3 (2). New ac area is 27L², determinant −162L³, inverse metric R_ex/9 (3). A_ac/A_ab=27/18=3/2, unchanged from 3/2 (2). A positive dimensional anchor fixes size that dimensionless ratios leave free; s must be positive to stay on the specified scale ray and retain handedness (3).

**6 (15):** a=(0.3275012420558906,−0.0548970078840064,−0.0374875028947299) nm and c=(−0.0101293176267288,−0.3897877023662599,−0.6897344083672676) nm (4). Fixed ICRS columns [a b c], det=−0.11791489191174465 nm³, intentional left-handedness, coordinates in [−1/2,1/2)^3 (3). Face areas ab=0.19486916546048413, ac=0.2611062357902053, bc=0.3578095391285615 nm²; ray in bc/ac/ab order is (1.0,0.7297352564331424,0.5446170214888189), dimensionless (3). S02 digest is `6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3`; pointers `/mature_locked_cell3/B_nm` and `/mature_locked_cell3/face_areas_nm2`, with original path from sources.md (3). S01 `/backbone_sequence/0` is historical, while S03 `/canonical_locked_values` confirms the active mature values; no mixed constants (2).

**7 (10):** M_cell=B^T B in nm², R_cell=M_cell^−1 in nm^−2, D=B R_cell=B^−T in nm^−1 (3). q=D^T(x−O_K)=B^−1(x−O_K) (2). The labeled nondegenerate angular frame, positive eta/alpha-derived ratios k_b,k_c, and a positive labeled area anchor are supplied. Lengths t(1,k_b,k_c), t>0; for an ab anchor, t=sqrt(A_*/[k_b sin(theta_ab)]) (3). Directions, ratio inputs and physical origin of the area anchor are not derived here; the mass-bridge interpretation is deferred (2).

**8 (5):** Residual −0.0001 (2); reconstructed product 1−0.0001=0.9999 (2). This is a synthetic numerical calculation, not observed transferred energy or another measurement (1).

**9 (5):** Difference −0.0000000000000000050=−5.0×10^−18 nm^−2 (2). Separately stored finite-precision entries need not coincide exactly even though the exact inverse is symmetric (1). Retain both source strings, their locations and units, and the signed difference; do not silently average or overwrite them (2).

**10 (5):** Use the hash-identified S02 stored direct/inverse metric strings and Decimal arithmetic at 60 significant digits with ROUND_HALF_EVEN (2). Compute each row-column product minus its identity entry and preserve all nine signed values; E is dimensionless and MR=I+E (2). A reported maximum omits component signs/locations and may use different unspecified arithmetic; retain its source-reported status separately (1).

Total: 100 points. Give method credit for consistent propagation of one arithmetic slip, while recording the correction. Do not mark a capability secure if a fundamental axis convention, domain restriction, unit, provenance, or residual reconstruction remains wrong. A correct final number alone earns only the result points, not missing explanation points. No extra credit is required to achieve full marks.

## Prerequisite and evidence map

| Task | Prior introduction and practice | Evidence class |
|---|---|---|
| 1 | L1 worked map/recovery and checks 1–2 | synthetic exact geometry |
| 2 | L2 nine-entry table and check 2 | synthetic exact geometry |
| 3 | L3 all face products and checks 1–4 | synthetic exact geometry |
| 4 | L4 block inverse, two products and checks 1–4 | synthetic exact geometry |
| 5 | L5 scaled example and checks 1–3 | synthetic exact geometry |
| 6 | L1 source-column reading; L6 card/pointer examples | source facts |
| 7 | L4 recovery; L5 conditional positive ray | defined inputs and derived implications |
| 8–10 | L6 worked rounding, residual matrices and diagnostics | synthetic or declared numerical witnesses |

The calculation sheet and locked card remain separately labeled even where they share formulas. All original source strings remain available through the hash-addressed files. No source dataset is copied or removed; all computed residual components are retained in the companion verification record.
