# Lesson 05 — Small differences at deeper levels

Essential question: When can two different rays have identical integer records, and where is their difference stored?

Goals: compare two exact inputs over stated generations; identify the first integer difference within that range; preserve earlier residual differences; interpret a historical replay without merging source branches.

Bridge: An integer and residual recover the ray together. Before proceeding, explain how inputs 0.1 and 0.2 can have the same integer 0 but different residuals. A generation table now lets us follow this distinction across scales.

## C09.05-E1 — Scaling a difference

Let two inputs in the same coordinate differ by delta, a signed amount. Their scaled difference at generation g is K_g delta. This does not tell us the rounded difference alone: the positions relative to half-integers also matter. Compare every earlier generation before declaring the first differing generation. “First” always refers to the specified starting level, inputs, and tie rule.

If Q'_g=Q_g but r'=r+delta, then epsilon'_g=Q_g−K_g(r+delta)=epsilon_g−K_g delta. Thus **epsilon'_g−epsilon_g=−K_g delta** while the integer records agree. There is no loss of the distinction in the complete pair. Once the integers differ, the general relation is epsilon'_g−epsilon_g=(Q'_g−Q_g)−K_g delta.

For two distinct exact scalar inputs, a sufficiently large scale will separate the integers: inputs that round to one integer lie in an interval of width 1, so a scaled separation greater than 1 cannot fit there. Since repeated multiplication by 27 can exceed any fixed positive bound, nonzero differences eventually separate. This gives a sufficient bound, not a universal predetermined first generation. Our assessments use explicit finite tables.

## C09.05-W1 — Worked synthetic comparison

Compare R=(1,2/3,1/2) with R'=(1,2/3+1/1000,1/2). Only b changes; keep a and c exactly as in lesson 03.

| g | Scaled b of R' | Q_b of R / R' | epsilon_b of R / R' |
|---|---|---|---|
| 0 | 2003/3000 | 1 / 1 | 1/3 / 997/3000 |
| 1 | 18027/1000 | 18 / 18 | 0 / −27/1000 |
| 2 | 486729/1000 | 486 / 487 | 0 / 271/1000 |

At g=2 the changed input is 486.729, which rounds to 487. Its residual is 487−486.729=0.271. The first integer difference is g=2; already at g=0 the residual difference is −1/1000. For both rays the other signed residuals at g=0,1,2 are epsilon_a=0 and epsilon_c=−1/2. These statements specify all three residual coordinates, not just the differing coordinate.

## C09.05-P1 — Guided comparison and answers

Compare T=(1,1/3,1/4) with T'=(1,1/3+1/10000,1/4) through g=3. Find every b integer and signed residual. Retain the common a,c residuals too.

Answers:

| g | K_g | Q_b of T / T' | epsilon_b of T / T' | common (epsilon_a,epsilon_c) |
|---|---:|---|---|---|
| 0 | 1 | 0 / 0 | −1/3 / −10003/30000 | (0,−1/4) |
| 1 | 27 | 9 / 9 | 0 / −27/10000 | (0,1/4) |
| 2 | 729 | 243 / 243 | 0 / −729/10000 | (0,−1/4) |
| 3 | 19683 | 6561 / 6563 | 0 / 317/10000 | (0,1/4) |

At g=3 the perturbed scaled b is 6561+19683/10000=6562.9683. Round to 6563 and subtract to obtain 0.0317. The a coordinates of Q are K_g; the c coordinates are 0,7,182,4921 for both rays. Integers first differ at g=3; residuals differ from g=0. Subtracting signed residuals verifies −K_g/10000 before the split and 2−19683/10000 afterward.

## C09.05-E2 — Historical source-reading card

S01#/backbone_sequence/4/projective_rays preserves two different decimal-string rays, named master_geometry and locked_mass_bridge. S01 M06 reports agreement through g=7 and master-minus-locked=(0,8,7) at g=8. A fresh exact rational replay of those stored strings gives the same result; the complete compact replay and signed residual differences are in worked-example-verification.json. At g=8 the locked Q is (282429536481,206098790228,153815932939); the master Q is (282429536481,206098790236,153815932946). Subtract the triples to check the reported difference yourself.

> Scope: This card is a historical finite-input replay, not a replacement for S02's active ray. The fresh check concerns supplied decimal strings, not unreported infinite digits. It neither promotes the source's broader proof status nor identifies a physical mechanism. Source branches remain separate even where their integers agree.

## Diagnostic checks

1. **C09.05-D1:** From the historical card, compute the g=8 difference. Does agreement through g=7 make the source rays identical?
2. **C09.05-D2:** In W1, calculate epsilon'_b−epsilon_b at g=1 and g=2 using the general relation.
3. **C09.05-D3:** Does every distinct pair first differ at g=2? Use the two synthetic comparisons.
4. **C09.05-D4:** Why must a table keep exact input identity and the residual even before its integer split?

Worked answers: (1) Difference=(0,8,7). No; distinct residuals preserve the differences before integer separation. (2) At g=1 it is 0−27/1000=−27/1000; at g=2 it is 1−729/1000=271/1000. (3) No: W1 splits at 2; P1 splits at 3. (4) Shared integers do not identify a ray; the branch and signed residual identify which input can be recovered.

Next: [lesson 06](lesson-06.md) packages the finite history into a reversible ledger.
