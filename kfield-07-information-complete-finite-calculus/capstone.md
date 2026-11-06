# Capstone — A reversible three-stage finite-data analysis

Work independently before reading the answer key. Use only operations taught in lessons 01–07. All data are synthetic. Preserve original channel h, IDs (0,1,2,3), times (0,1,2,3) s and signal h=(3,7,6,10) SU. Pair blocks are {0,1},{2,3}. In step 4 and step 6, arrays are explicitly dimensionless and separate from h.

## Tasks

1. **C07-CAP-01 (10 points):** Record the ordered source fields, calculate forward differences, retain the anchor and recover all four samples. Name the inverse operation.
2. **C07-CAP-02 (10 points):** For separate signals f:3→1 SU and g:2→5 SU on one edge, compute product change directly and by the full finite product rule. Preserve the signed joint term and product units.
3. **C07-CAP-03 (10 points):** Compute h's compact means/details and expanded E and Q views. Decode h with signs and block support.
4. **C07-CAP-04 (25 points):** State the fixed pair-average hypotheses (linearity, idempotence, unit preservation, multiplication-closed range, two-sided factor property), prove them on a generic pair and derive the detail-product identity. For dimensionless f=(0,2,2,4),g=(1,1,0,2), compute both sides. Diagnose why E_star(x,y,z)=(x,x,z+y−x) fails that identity with f=g=(0,1,0), even though it is an idempotent linear map with the stated closed range. Keep its signed mismatch.
5. **C07-CAP-05 (10 points):** Subtract fixed model (2,2,2,2) SU from h. Model its residual by pair means. Record both residual layers and reconstruct every sample.
6. **C07-CAP-06 (15 points):** For K=[[1,1],[2,2]], solve K psi=(8,16) as a family, then retain t=3 to identify an input. Separately handle (8,17): retain its compatibility coordinate and a declared first-equation-matching residual view. Contrast with the unique inverse for L=[[1,0],[0,2]].
7. **C07-CAP-07 (20 points):** Build the complete three-stage ledger: subtract the model, split residual pairs, encode their means by an anchor and difference. Reverse it and show the full reconstruction-error list. Match all EG-A1–EG-A6 premises to ledger fields or the product side calculation. Correct any assertion that these premises follow from B alone. State whether any removed component is unrecorded.

## Full answer key

1. Differences=(7−3,6−7,10−6)=(4,−1,4) SU; anchor=3 SU. Addition decodes 3,7,6,10 at IDs 0–3, retaining given times, channel and units.
2. df=−2,dg=3 SU. Direct change=1·5−3·2=−1 SU². Three terms are 9,−4,−6 SU² and sum to −1. Endpoint form is 3·3+(−2)·5=−1. The −6 interaction is retained.
3. Means=(5,8), d=(2,2) SU; Eh=(5,5,8,8), Qh=(−2,2,−2,2). Decoder yields (5−2,5+2,8−2,8+2)=h on the declared support.
4. Linearity follows by distributing weighted sums through (u+v)/2. Repeated mean of (m,m) is m, giving E²=E; averaging ones gives ones. Outputs (a,a,b,b) remain of that form under multiplication and are fixed by E. For constants c,d on a block, average(cu d,cv d)=cd(u+v)/2, which proves the two-sided factor rule. Set qf=f−Ef,qg=g−Eg. Then E(qf)=Ef−E²f=0 and E(qg)=0. Expand fg=Ef Eg+Ef qg+qf Eg+qf qg. Applying E fixes the first term, makes the middle two zero by the factor rule and retains E(qf qg). Subtract to get Q(fg)=Ef qg+qf Eg+qf qg−E(qf qg).

   For the supplied arrays, Ef=(1,1,3,3),Eg=(1,1,1,1),qf=(−1,1,−1,1),qg=(0,0,−1,1). Four RHS terms are (0,0,−3,3), (−1,1,−1,1), (0,0,1,1), and minus (0,0,1,1), giving (−1,1,−4,4). Direct fg=(0,2,0,8), E(fg)=(1,1,4,4), so Q(fg) agrees.

   E_star is linear because every component is linear in x,y,z; applying it twice returns (x,x,z+y−x). It fixes (1,1,1) and its range (a,a,b) is multiplication-closed. But with b=(1,1,0), f=(0,1,0), E_star(bf)=(0,0,1) differs from bE_star(f)=0. For f=g=(0,1,0), Ef=(0,0,1),qf=(0,1,−1); RHS=(0,0,−1)+(0,0,−1)+(0,1,1)−(0,0,2)=(0,1,−3). Direct Q_star(fg)=(0,1,−1). RHS minus direct=(0,0,−2), retained as a counterexample mismatch. Idempotence alone is insufficient.
5. M_0=(2,2,2,2),r_0=(1,5,4,8),M_1=(3,3,6,6),r_1=(−2,2,−2,2) SU. Reconstruct (2+3−2,2+3+2,2+6−2,2+6+2)=(3,7,6,10). r_0 and r_1 are distinct preserved layers.
6. psi=(8−t,t), all real t; kernel direction (−1,1), compatibility 16−2·8=0. With t=3, psi=(5,3). For j=(8,17), c=17−16=1, so no exact solution. Choose j_fit=(8,16),rho=(0,1),psi_fit=(8−t,t); with t=3 its output plus rho is (8,17). This view matches the first equation and is not a unique optimum. L sends (u,v) to (u,2v) and has unique inverse (j_1,j_2/2); K does not have that full inverse.
7. The stage-1 record contains h, M_0, r_0 and decoder M_0+r_0. Stage 2 contains block means m=(3,6),signed d=(2,2),support, M_1,r_1 and pair decoder. Stage 3 contains A=3,δ=6−3=3 SU and decoder (A,A+δ). Reverse: (3,6)→(1,5,4,8)→(3,7,6,10). Error=(0,0,0,0) SU with IDs/times intact. No removed component is unrecorded. EG-A1→source fields, supports, signs and anchors; EG-A2→the reverse check; EG-A3→δ and forward sample differences; EG-A4→the retained −6 SU² product side calculation; EG-A5→both residual layers; EG-A6→the compact typed view with source and decoder. All six have logical_role premise_not_derived_theorem. Finite decoder/product equalities follow under the supplied definitions, without deriving the constitutive physical premises from B.

## Rubric and repair

| Step | Points awarded for observable work |
|---|---|
| 1 | 3 metadata/order; 3 differences; 4 anchor and correct addition decoder |
| 2 | 2 endpoint products; 4 signed three terms; 2 agreement; 2 SU² |
| 3 | 4 means/details; 2 expanded views; 4 signed inverse/support |
| 4 | 7 hypotheses with pair proofs; 7 justified line-by-line derivation; 5 finite numerical check; 6 counterexample and missing factor property |
| 5 | 4 both residual layers; 2 M_1; 4 entrywise reconstruction |
| 6 | 4 solution family/kernel; 2 t=3; 5 incompatibility and residual view; 4 invertible contrast/scope |
| 7 | 6 complete three-stage ledger; 4 reverse replay/errors; 6 all six premise links; 4 source scope and removed-component accounting |

Total: 100 points. Award arithmetic partial credit when the method and retained coordinates are explicit. Exact reconstruction, all six premise IDs and the E hypotheses must be repaired if missing, regardless of score. Recognition-only gauge/infinite-resolution extensions are not assessed. The source gap about a general archival E is not filled by this capstone; the theorem proved here is the explicit finite block theorem.
