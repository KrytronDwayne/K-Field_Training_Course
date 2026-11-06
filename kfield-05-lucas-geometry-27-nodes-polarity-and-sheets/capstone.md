# Capstone — Build a reversible 27-node registry

Work in two 55-minute periods. Use Lessons 1–6 and a blank table before opening the full answer registry. You may use a calculator or a small script, but explain the counting and reconstruction checks in words. No coding skill is required. All constants below describe the classroom analogue, not Cell3 or observations.

**Inputs:** L entries −1,0,1; O=(2,−1,4) U; basis columns a=(1,0,0), b=(1,2,0), c=(0,0,−3) U. Use the half-basis map and the half-open owner convention from Lesson 2. Keep the centered-window boundaries. Use g_λ=(1,0,−1/3)/U. The output is all 27 rows plus a check ledger and a brief information-preservation explanation.

## Tasks and prior preparation

|Step|Concrete input → output|Earlier explanation and answered practice|
|---|---|---|
|C05-CAP-01|Three coordinate menus → 27 distinct L and center/face/edge/vertex tally|C05.01-E1, W1 and P1 in Lesson 1|
|C05-CAP-02|L,O,B → q,p,z,u in every row; one boundary explanation|C05.02-E1/E2, W1 and P1 in Lesson 2|
|C05-CAP-03|Each L and p → λ, seven counts and one written affine identity check|C05.03-E1/E2, W1 and P1 in Lesson 3|
|C05-CAP-04|Each λ → χ; explain unchanged χ under negation|C05.04-E1, W1 and P1 in Lesson 4|
|C05-CAP-05|Each nonzero L → v,s; center singleton; reconstruct L and both pair points|C05.05-E1, W1, P1 and P2 in Lesson 5|
|C05-CAP-06|Completed rows → inverse residual triples, uniqueness and pair checks, retained correction ledger|C05.06-E1/E2, W1, P1 and P2 in Lesson 6|
|C05-CAP-07|Each λ → r₃; three counts and comparison with χ counts|C05.04-E2, W2 and P2 in Lesson 4|

For step 6, retain every original row. If you find an error, add a note recording the old field, corrected field, reason and closure residual before and after. If no error occurs, explicitly report no corrections and still provide the per-row zero residuals. Explain which information survives a pair-only quotient and which extra field makes it invertible. Do not replace the complete registry by totals.

## Full answer key

The two tables in [registry.md](registry.md) are the full row-by-row answer, including every q,p,λ,χ,r₃,v,s,z,u and inverse residual. [registry.json](registry.json) is the same small synthetic record in machine-readable form. Compare by L, not merely row order. Equivalent exact fractions and a different declared enumeration order are acceptable.

**C05-CAP-01:** Three independent choices give 3³=27 unique rows. Zero, one, two and three nonzero entries give 1,6,12,8 rows respectively: center, face centers, edge centers, vertices. The sum is 27. A row count alone would miss a duplicate-and-omission error.

**C05-CAP-02:** For every row use q=L/2 and p=(2+(L₁+L₂)/2,−1+L₂,4−3L₃/2) U. Set each owner component to 1 only when the corresponding L entry is +1; otherwise set it to 0. Then u=q−z. At L=(1,0,0), p=(5/2,−1,4) U, z=(1,0,0), u=(−1/2,0,0). This node is on the centered window's boundary, yet belongs to the positive neighbor's half-open cell. Keeping z and u reconstructs q.

**C05-CAP-03:** λ=−3,−2,−1,0,1,2,3 has populations 1,3,6,7,6,3,1. At L=(1,−1,1), p−O=(0,−1,−3/2) U. Dotting with g_λ gives 1/2, equal to λ/2. Generally the dot product equals (L₁+L₂)/2+L₃/2. Omitting O changes it by 2/3 in this analogue.

**C05-CAP-04:** χ is +1 on −2,0,2 and −1 on −3,−1,1,3. Counts are 13 and 14. The negative of an even integer remains even and the negative of an odd integer remains odd, so χ is unchanged for opposite nodes. It cannot substitute for orientation s.

**C05-CAP-05:** The 13 representatives are listed in Lesson 5 P2 and appear in the registry, each twice. Each noncentral member is L=s v. For example v=(0,1,1) gives p(+v)=(5/2,0,5/2) U and p(−v)=(3/2,−2,11/2) U. Their sum equals 2O. Center L=0 has p=O, v=0, s=N/A and occurs once. Including the singleton gives 14 classes. A pair-only view retains the representative, the unoriented pair and antipodally even quantities, including χ and λ². It loses which member was selected and generally the signed λ, the member's r₃, position and displacement. Adding s to v restores the member; retaining O and B restores position. At λ=0 or r₃=0 some labels coincide, but member direction still needs s.

**C05-CAP-06:** For each stored p, subtract O, then compute L_recovered=(2dₓ−dᵧ,dᵧ,−2d_z/3). Every R_L=L_recovered−L is (0,0,0) in the answer table. Verify q=z+u for all rows and −1/2≤u_i<1/2, check that each pair has signs −1 and +1, and check pair position sums 2O. An erroneous stored p_z=3 in the row L=(1,−1,1) would give R_L=(0,0,−1/3); the correction note would retain that discrepancy and set p_z to 5/2 with a subsequent zero residual. The supplied answer registry needed no row corrections. This deliberate error is a teaching example, not an observed acquisition fault.

**C05-CAP-07:** r₃=0 groups sheets −3,0,3 (1+7+1=9); r₃=1 groups −2,1 (3+6=9); r₃=2 groups −1,2 (6+3=9). The seven-sheet, two-polarity and three-remainder partitions each account for the same 27 rows, with different information retained. None replaces the address.

## Rubric — 100 points

|Step|Points|Full-credit evidence and partial-credit rule|
|---|---|---|
|01|15|10 for all 27 distinct triples (deduct 1 per missing/duplicate intended row to zero); 5 for justified 1/6/12/8 tally|
|02|20|12 for complete correct q,p (deduct 1 per erroneous row to zero); 4 for z,u; 4 for boundary explanation with origin and units|
|03|15|5 for row λ values; 5 for complete seven counts; 5 for a correct affine identity with O subtraction|
|04|10|5 for row χ and counts; 5 for the antipodal parity explanation|
|05|15|8 for v,s and separate center; 4 for reconstruction and pair midpoint; 3 for the information-loss explanation|
|06|15|5 for complete retained rows/uniqueness check; 5 for per-row inverse/ownership checks; 5 for pair check and explicit discrepancy/correction accounting|
|07|10|5 for r₃ per row; 5 for 9/9/9 reconciliation and distinction from parity|

For any non-row subcriterion award half its points when the method is correct but a local arithmetic error remains, and zero when absent or conceptually incorrect. Do not deduct twice for a propagated arithmetic error: mark later method work on its own merits. Give repair feedback for missing origin, omitted orientation, or dropped rows regardless of score; successful mastery requires those conceptual errors to be corrected.

**Source and evidence scope:** Node and sheet definitions come from S02 M03, with the affine correction SA-05. Cell ownership comes from S02 M02. All numerical positions here use the supplied synthetic analogue. Counting and rational identities are derivations, not empirical measurements. There are no new physical mechanisms or statistical conclusions in this task. Every owned-cell residual and inverse closure residual is retained separately.
