# Capstone — Build a ratio-to-claim ledger

Use only the taught formulas and the source-reading cards in lessons 3 and 4. Work in bc/ac/ab order. All small-number areas are synthetic. The mature and historical rows are source facts, not experimental datasets. Keep all signed differences and record reconstruction equations. Two 55-minute periods are provided.

| Step | Named inputs → required outputs | Earlier explanation and worked example | Independently answered practice |
|---|---|---|---|
| C08-CAP-01 | (15,10,5) U² → ray, divisor, reconstructed areas | C08.01-E1/W1 | C08.01-P1 |
| C08-CAP-02 | That triple; s=2 and 1/2 → scaled triples, both cancellation proofs | C08.02-E1/W1 | C08.02-P1 |
| C08-CAP-03 | Same triple plus locked source card → four constants, two product paths, stored/recomputed distinction | C08.03-E1/E2/W1 | C08.03-P1 including source-card follow-up |
| C08-CAP-04 | S02 active and both S01 history cards → provenance rows, exact signed branch differences | C08.04-E1/W1 | C08.04-P1 |
| C08-CAP-05 | Supplied anchor, derived quotients, asserted mass interpretation → evidence tags and measurement-provenance list | C08.05-E1/W1 | C08.05-P1 |
| C08-CAP-06 | Baseline (12,8,6) U² and either taught +1/10 change → all seven output changes, reconstruction and closure | C08.06-E1/W1 | C08.06-P1 |

## Student tasks

1. **C08-CAP-01 (15 points).** Normalize (15,10,5) U². Retain enough information to reverse the transformation. Reconstruct all areas and explain what the ray cannot tell you about spatial geometry.
2. **C08-CAP-02 (15 points).** Prove that both independent ratios remain fixed for any positive uniform length multiplier s. Test s=2 and s=1/2 on the capstone triple. Name the factor needed to undo each scaling.
3. **C08-CAP-03 (20 points).** Calculate eta, alpha_inverse, alpha, and eta_alpha for the capstone triple. Check the product by both paths. Record the active area pointer and unit, and read all four rows of the locked evaluation card: identify stored value, exact recomputation, exact signed difference, and reconstruction rule. You may reference each entire card row by quantity rather than recopy long integers; state the four signs. Explain why a fresh quotient does not overwrite the source-stored witness.
4. **C08-CAP-04 (20 points).** Make separate ledger rows for the active ray and both historical rays. Include source ID, hash (or exact sources.md reference), pointer, order, dimensionless unit, and role. Attach each exact difference vector from lesson 4’s last column with direction active−historical. State the reconstruction equation and both nonleading signs for each vector. Explain why an eta made from mature bc and historical ab is not active eta. Name the separate historical calibration input pointer.
5. **C08-CAP-05 (10 points).** Tag the capstone area anchor, calculated quotients, and an asserted physical mass-ratio identification by evidence class. List the provenance needed to compare with measurements. Explain why an area ray alone supplies neither an absolute area nor a mass unit.
6. **C08-CAP-06 (20 points).** Return to baseline (12,8,6) U². Choose ab→61/10 or ac→81/10. Provide the input-change vector; all three new ray components; the four new constants; every signed new-minus-old difference, including zeros; and reconstruction of each output. Verify both product paths and their closure difference. State why these supplied states are not a measured trajectory.

## Full answer key

1. Divisor 15 U²; r=(1,2/3,1/3). Multiply 15 by each component to recover 15,10,5 U². The ray fixes a positive area triple up to common scale, not all angles or a unique spatial basis.
2. All areas become s² times their initial values. (s²A_ac)/(s²A_bc)=A_ac/A_bc and (s²A_ab)/(s²A_bc)=A_ab/A_bc because s²A_bc is nonzero. For s=2 the triple is (60,40,20); for s=1/2 it is (15/4,5/2,5/4), all U². Both normalize to (1,2/3,1/3). Divide by 4 and by 1/4 respectively to reverse.
3. Eta=1000×15/5=3000; alpha_inverse=100×15/10=150; alpha=1/150; eta_alpha=3000/150=20. Direct path 10×10/5=20; closure 0. Units are dimensionless. Active area pointer is S02#/mature_locked_cell3/face_areas_nm2, unit nm². Use the four exact rows in lesson 3, retained also in verification.json, as the answer card. Their signed differences in eta, alpha_inverse, alpha, eta_alpha order have signs +,+,−,−. For each, recomputed=stored+the complete signed fraction. Source-stored lexemes have their source-authority role; evaluating finite input lexemes creates a separately typed diagnostic.
4. Active: S02#/backbone_sequence/4/projective_ray, (1.0,0.7297352564331424,0.5446170214888189), order bc/ac/ab, dimensionless; S02 hash from sources.md. Historical: S01#/backbone_sequence/4/projective_rays/master_geometry and S01#/backbone_sequence/4/projective_rays/locked_mass_bridge, with their exact lexemes and S01 hash as printed in lesson 4 and sources.md. The exact signed vectors are the full last columns of those two lesson 4 tables, also in verification.json under branch_comparisons. First vector signs: 0,−,−; second: 0,−,+. Active=historical+d component by component. A mixed-input ratio changes the branch contract; it is a labeled mixed diagnostic, not active eta. The separate historical area input pointer is S01#/mass_bridge_calibration/face_areas_nm2.
5. Anchor 15 U²: supplied synthetic dimensional input. Quotients: derived algebra. Mass-ratio identification: additional physical interpretation. Required comparison provenance includes definitions and identities of masses, measured values and units, instrument/calibration, acquisition dates and conditions, full model-input branch, and every signed prediction-minus-measurement difference. Common scale was divided away, and ratios cancel units; neither an absolute area nor a kilogram value can be recovered from r alone.
6. **ab option:** input change (0,0,1/10) U². New outputs in r_bc,r_ac,r_ab,eta,alpha_inverse,alpha,eta_alpha order: (1,2/3,61/120,120000/61,150,1/150,800/61). Signed changes: (0,0,1/120,−2000/61,0,0,−40/183). Reconstruction: 1+0=1; 2/3+0=2/3; 1/2+1/120=61/120; 2000−2000/61=120000/61; 150+0=150; 1/150+0=1/150; 40/3−40/183=800/61. Product=(120000/61)/150=800/61; direct=10×8/(61/10)=800/61; closure=0.

   **ac option:** input change (0,1/10,0) U². New outputs in the same order: (1,27/40,1/2,2000,4000/27,27/4000,27/2). Changes: (0,1/120,0,0,−50/27,1/12000,1/6). Reconstruction: 1+0=1; 2/3+1/120=27/40; 1/2+0=1/2; 2000+0=2000; 150−50/27=4000/27; 1/150+1/12000=27/4000; 40/3+1/6=27/2. Product=2000×27/4000=27/2; direct=10×(81/10)/6=27/2; closure=0. Neither option supplies timestamps or measurements; they are finite synthetic sensitivity states.

## Point rubric

| Step | Allocation |
|---|---|
| 1 | Correct ordered ray 6; divisor/units 3; reconstruction 4; scope 2 |
| 2 | Two cancellation proofs 6; both scaled triples 6; reverse factors 3 |
| 3 | Four constants 8; both paths/closure 4; source pointer/unit 2; full difference-row references/signs/reconstruction 4; authority distinction 2 |
| 4 | Three complete provenance rows 8; two exact difference vectors with direction/signs 6; reconstruction 2; mixed-input diagnosis 2; historical calibration pointer 2 |
| 5 | Three evidence tags 4; measurement-provenance list 4; scale/unit explanation 2 |
| 6 | Input change 2; seven outputs 5; all differences 5; all reconstructions 4; both paths/closure 2; synthetic scope 2 |

Total 100. Allow valid equivalent fractions and exact references to supplied long-number cards. Do not award reconstruction credit for merely dropping small differences. Require repair of a branch mix, missing dimensional anchor, or alpha/reciprocal confusion before using the ledger in later courses.
