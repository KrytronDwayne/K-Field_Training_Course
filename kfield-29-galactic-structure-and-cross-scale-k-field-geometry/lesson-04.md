# Shared grammar and distinct metrics

Essential question: Which shared constructions survive when the basis changes?

Goals: Verify root closure and orthogonality; compare two typed metrics; distinguish a common algebraic construction from a physical identification.

Prerequisite bridge. Lesson 03 taught column bases, transposes, inverses and the Gram matrix. We now subtract basis steps and ask which formulas remain true for every independent basis. The first period develops closure; the second compares source roles and units.

## C29.04-E1 — Different routes to the same sheet

An integer address (i,j,k) records steps along a,b,c. Its sum lambda=i+j+k labels a sheet. A change such as (1,-1,0) has sum zero and stays in that sheet. The set of integer changes with sum zero is called the A2 address lattice here. “Rank two” means two independent changes suffice: every (i,j,k) with sum zero equals i(1,0,-1)+j(0,1,-1). This is a concrete operational definition; no abstract algebra is needed.

In the local half-step window a primitive lift is a/2, b/2 or c/2. Here i,j,k count half-steps: the corresponding full-step address is (i,j,k)/2, and the local sheet label lambda=i+j+k is twice its full-step coordinate sum. Each primitive lift increases this local label by one. Taking one lift forward and another backward produces an in-sheet displacement, called a root or elementary holonomy displacement in G02:

`s_ab=(a-b)/2`, `s_bc=(b-c)/2`, `s_ac=(a-c)/2`.

Add the first two expressions. The -b and +b cancel, giving `(a-c)/2=s_ac`. This closure identity holds for any three vectors, not only a fitted galaxy cell. It does not force their lengths or angles to agree.

The vector `g=A⁻ᵀ(1,1,1)` uses inverse transpose: transpose the inverse, then multiply. It satisfies g·a=g·b=g·c=1 by reciprocity. Hence g·s_ab=(1-1)/2=0, and similarly for the other roots. Thus g points perpendicular to the root sheet. Dividing g by its length gives a unit normal N. With `h=1/(2||g||)`, each primitive half-step has normal component h. Its remainder t_a=a/2-hN is the in-sheet slip; recover a/2 by adding hN+t_a. No component is discarded.

## C29.04-W1 — Worked comparison

Synthetic A=diag(1,2,3)L gives a=(1,0,0)L, b=(0,2,0)L and c=(0,0,3)L. Therefore s_ab=(1/2,-1,0)L, s_bc=(0,1,-3/2)L and s_ac=(1/2,0,-3/2)L. Adding the first two gives the third component by component.

Here g=(1,1/2,1/3)/L. Its dot product with s_ab is 1/2-1/2=0; with s_bc it is 1/2-1/2=0; with s_ac it is 1/2-1/2=0. The Gram metric is diag(1,4,9)L². It describes lengths and angles that closure alone did not specify.

## C29.04-P1 — Guided practice and answer

Change to synthetic A'=diag(2,1,4)L. Compute roots and metric. The roots are (1,-1/2,0)L, (0,1/2,-2)L and (1,0,-2)L, again closing. The metric becomes diag(4,1,16)L², different from the previous metric. The new perpendicular vector is g'=(1/2,1,1/4)/L; for example g'·s'_ab=1/2-1/2=0. The two normals are not parallel because their component ratios are not all equal. Shared closure has not identified their directions.

Now classify a proposed ratio “galaxy sheet spacing divided by Cell3 spacing in nm.” The numerator is an uncalibrated unit-sphere reconstruction length, the denominator a physical length. It is not an admitted physical scale ratio. A galaxy radial calibration and a declared mapping would be needed. Dimensionless comparisons formed separately within each cell can still be meaningful.

## Source comparison card

| Contract | Galaxy cell | Mature Cell3 |
|---|---|---|
| Basis | A_gal, G01, ICRS columns | B, S02#/mature_locked_cell3, ICRS columns |
| Length type | unit-sphere reconstruction | nm in the locked record |
| Handedness | positive determinant | intentional negative determinant |
| Origin use | c_k=A_gal(k+phi) | x-O_K in affine addresses |
| Direct metric | M_gal=A_galᵀA_gal | M_cell=BᵀB |
| Inverse metric | M_gal⁻¹ | R_cell=M_cell⁻¹ |
| Normal | derived from A_gal | separately derived from B |

> Evidence scope. G02 pp3–5,17,20 and G01#/comparison_to_authoritative_K_field report shared algebra but distinct metric anisotropy and ICRS orientation. The historical normal-angle comparison is source-reported, not a fresh mature-lock replay. Our two diagonal bases establish the general logical distinction exactly. A common formula is useful explanatory structure; an additional physical correspondence needs its own transformation and prediction.

The symbols G_phase and G_eff from neighboring work have different source-defined roles; neither is silently substituted for M_cell. Similarly Q_gal is a reciprocal basis here, not a distance quadratic form called Q elsewhere, and not the indexed integerization Q_g or Q_nu. Label both symbol and source before combining equations.

## Diagnostics — C29.04-D1

1. Why does s_ab+s_bc=s_ac survive a change of basis?
2. Does equality of sheet counts fix a normal in ICRS?
3. What is the reconstruction rule for a/2 after separating its normal component?
4. What must be supplied before an orientation comparison becomes a physical scale comparison?

Worked answers. 1. The b terms cancel algebraically for all vectors. 2. No: the normal depends on the actual inverse transpose, as the two diagonal examples show. 3. a/2=hN+t_a; store both parts. 4. A calibrated length relationship and explicit mapping, preserving the different origins, orientations and units. An angle alone supplies no physical distance.

Next: [lesson 05](lesson-05.md) calculates how a metric changes address differences into geometric distance.
