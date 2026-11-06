# Capstone — A reversible shape-and-scale change report

Allow two 55-minute periods. Use the lessons and exact symbolic expressions; calculators are optional. These are separate synthetic records, not one physical acquisition. Submit ordered inputs, transformed values, inverse checks, units, domains, source pointers and retained remainders. L=ln2. Label the dimensionless change parameter t_change and the positive length scale t_length in your final report.

## Student tasks

**C10-CAP-01 (10 points).** Record AREAS has A0=1 LU² and A/A0=(2,4,16) in [ab,ac,bc] order. Find its log triple. Halve all edges at fixed angles, giving a common area factor 1/4. Find the changed logs and dimensional areas, then reconstruct the original areas. Explain the difference between that operation and changing only A0 to 4A0.

**C10-CAP-02 (20 points).** For the original AREAS triple calculate m,z and s,u,v. Use both decompositions to recover every log and area. State what changes and what stays fixed under the edge halving. Explain the limitation of the word shape.

**C10-CAP-03 (15 points).** Record LINEAR uses H with rows (1,1),(1,-1) and input (1,-2)t_change. Apply and invert it. Record SQUARE separately uses f(t_change)=(1+t_change)² with initial value 1. At t_change=1/10 calculate output, change, tangent and signed remainder. Give the exact log change as well. Keep each record's exact versus local status explicit.

**C10-CAP-04 (20 points).** Record JACK uses input (2,-1,1)t_change in [dln l_a,dln l_b,dln l_c] order. Use J from Lesson 4 to find [dln eta,dln alpha,dln Gamma2], then reverse it. Check det J. Check the third output separately using the area tangent changes and coefficients 9,8,-11. State the angle domain, units, meanings of dA and Gamma2, and relevant source pointers.

**C10-CAP-05 (25 points).** Build a typed ledger. Record BOX uses B=diag(2,2,2) LU in a declared synthetic Cartesian frame. Find M_cell, its metric cofactor matrix, R_cell and the inverse product, all with units. Retain B and explain why. Record BRANCH has S=4,A_branch=2; decode and re-encode it, checking integer admissibility. In a separately labeled ANCHOR record, orthogonal face areas are (9,18,18) LU². Find eta, alpha_inverse, k_b,k_c, positive t_length and all edge lengths; reconstruct every area. Include the AREAS scale/shape coordinates from step 2 and JACK scalar tangent from step 4 as separately identified records rather than one unlabeled vector.

**C10-CAP-06 (10 points).** Audit your report. Compare the zero inverse residual of JACK with the finite SQUARE remainder. State the retained reference, angle and branch metadata. Identify what additional information is required for changing angles or a finite physical Gamma2 prediction. Distinguish source formula, fresh finite calculation, synthetic input and unresolved mechanism. Do not delete any signed remainder.

## Full worked answer key

**01.** Original logs y=(1,2,4)L and original areas (2,4,16) LU². Edge halving subtracts 2L from each log, giving (-1,0,2)L and (1/2,1,4) LU². Add 2L to reverse the operation and exponentiate to recover (2,4,16) LU². Changing only the reference to 4A0 produces the same changed log numbers but reconstructs unchanged physical areas with the NEW reference: 4A0 times (1/2,1,4)=(2,4,16)A0. All areas/references are positive.

**02.** m=7L/3; z=(-4,-1,5)L/3, whose sum is zero. s=7L/sqrt3, u=L/sqrt2, v=5L/sqrt6. Mean reconstruction gives coefficients (7-4,7-1,7+5)/3=(1,2,4). Normalized reconstruction gives (7/3-1/2-5/6,7/3+1/2-5/6,7/3+10/6)=(1,2,4). A0 exp(y)=(2,4,16) LU². Edge halving gives m_new=m-2L=L/3 and s_new=s-2sqrt3 L=L/sqrt3; z,u,v stay fixed. Area shape is complete for face-area ratios modulo a common factor, not arbitrary edge-angle shear.

**03.** H(1,-2)t_change=(-1,3)t_change. H/2 returns ((-1+3)/2,(-1-3)/2)t_change=(1,-2)t_change. Its inverse residual is exactly (0,0). SQUARE expands to 1+2t_change+t_change². At 0.1: output 1.21, change 0.21, tangent 0.20, remainder +0.01. The baseline-plus-parts check is 1+0.20+0.01=1.21. Exact log change is 2ln(11/10), approximately 0.19062036. Its difference from log tangent 0.20 is 2ln(11/10)-0.20, approximately -0.00937964. This negative log remainder differs from the positive relative-change remainder; preserve the coordinate label.

**04.** J input gives (-2+1,2+1,34+2-3)t_change=(-1,3,33)t_change. Inverse numerators (33-6-3,33-42-3,33-6-15)=(24,-12,12) give (2,-1,1)t_change after division by 12. Residual is (0,0,0). Determinant=(-1)(3)+(1)(15)=12. Area tangents are (2-1,2+1,-1+1)t_change=(1,3,0)t_change; 9+24-0=33 verifies dG. All entries are dimensionless tangent changes, with fixed included nondegenerate angles and coherent edge scaling. dA=dln alpha, not area or dln alpha_inverse. Gamma2 is a named scalar lift, not a force. Sources: S02#/backbone_sequence/6 for J, /backbone_sequence/4 for eta/alpha, /backbone_sequence/18/branches/gravity_scalar_lift for 9,8,-11.

**05.** BOX: M_cell=4I LU², det(M_cell)=64 LU⁶, cof(M_cell)=16I LU⁴, R_cell=I/4 LU^-2; M_cell R_cell=I. B=diag(2,2,2) LU and its synthetic frame remain in the record because its metric loses orientation. Its face areas are (4,4,4) LU², distinct from the separate AREAS and ANCHOR datasets. BRANCH: both 4 and 2 are even, so C_b=(4+2)/2=3, C_c=(4-2)/2=1 are integers. Re-encoding gives S=3+1=4, A_branch=3-1=2. ANCHOR: eta=1000(18/9)=2000 and alpha_inverse=100(18/18)=100. Orthogonal sine factors=1 imply k_b=1,k_c=2. t_length=sqrt(9/1)=3 LU; lengths (3,3,6) LU reconstruct (9,18,18) LU². The ledger separately retains AREAS (A0,m,z,s,u,v) and JACK dG=33t_change with its source/domain. Metric, shape, scalar tangent and integer branch entries keep distinct types and inverse maps.

**06.** JACK reverses its linear map exactly; SQUARE retains a +0.01 finite approximation remainder, so these results are consistent. The reference is A0=1 LU² for AREAS, with any reference change recorded. JACK angles are fixed; ANCHOR angles are perpendicular. BRANCH has same-parity integer inputs and the M06 side-mode map. All record names, orders and units remain. Varying angles requires their additional dln sin(theta) terms and geometry; J alone is insufficient. A finite physical Gamma2 prediction additionally needs a stated finite relation and physical interpretation/baseline, which the tangent matrix alone does not give. The numeric inputs are synthetic; formula provenance is archival; matrix and reconstruction arithmetic are freshly checkable; a dynamical mechanism is unresolved here. S03 AUD-002's wider DAG gap remains outside these finite checks.

## Rubric

| Step | Points and allocation |
|---|---|
| 01 | 10: positive reference/order 2; original logs 2; scaling 3; reversal/reference distinction 3 |
| 02 | 20: mean/zero-sum 5; projections 5; two reconstructions with areas 6; scale and scope 4 |
| 03 | 15: H and inverse 5; exact square/tangent/remainder 6; exact log and scope 4 |
| 04 | 20: forward 4; inverse 4; determinant 3; independent area-row check 4; domain/units/source meanings 5 |
| 05 | 25: metric/cofactor/reciprocal with units 7; basis retention 2; branch round trip/parity 4; anchor/lengths/area round trip 8; typed separate records 4 |
| 06 | 10: two residual types 3; retained metadata 3; source/synthetic/finite/mechanism distinction and limits 4 |

Total 100. Give method credit for a correctly propagated arithmetic error; identify the earliest defect instead of deducting repeatedly. A high score does not waive a missing scale, omitted residual, changed-angle misuse or force-law conflation: repair those before calling the report reversible. Exact expressions are preferred; rounded decimals must retain their exact parent expression. No novelty or consensus judgment is assessed.
