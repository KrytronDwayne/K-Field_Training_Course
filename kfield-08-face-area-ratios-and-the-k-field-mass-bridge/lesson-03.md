# Lesson 3: The eta and alpha constructions

Essential question: How do the source definitions turn two area ratios into eta and alpha?

Goals

- Evaluate eta, alpha_inverse, alpha, and their product from one labeled triple.
- Verify the product using a second algebraic path.
- Read stored and recomputed source values with their units and signed closure differences.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Lesson 2 established that a common area factor cancels. A reciprocal of a nonzero number x is 1/x; multiplying x by 1/x gives 1. Thus alpha⁻¹ means 1/alpha, not a negative alpha. The spelling alpha_inverse below means the same reciprocal.

## C08.03-E1 — Definitions, not guessed numerical matches

The active definitions in S02#/backbone_sequence/4/definitions are eta=1000 A_bc/A_ab and alpha_inverse=100 A_bc/A_ac. The factors 1000 and 100 are part of these definitions and dimensionless. They are not unit conversions invented by this course. Compute each fraction before interpreting it. Because alpha is the reciprocal of alpha_inverse, alpha=A_ac/(100 A_bc).

Multiplying the definitions gives eta×alpha=(1000 A_bc/A_ab)×(A_ac/(100 A_bc)). Cancel the nonzero A_bc and reduce 1000/100 to 10. The result is eta×alpha=10 A_ac/A_ab. This supplies two paths to the same quantity: multiply the separately calculated eta and alpha, or use the direct face quotient. Their signed difference, product path minus direct path, is the algebraic closure difference. Exact arithmetic makes it zero for any positive input triple.

Every result is dimensionless because area units cancel. A dimensionless number can serve a physical ratio, but the formula alone does not name a measured physical object. We return to that distinction in lesson 5.

## C08.03-W1 — Evaluate and cross-check

Use the synthetic triple (12,8,6) U². Eta=1000×12/6=2000. Alpha_inverse=100×12/8=150. Its reciprocal is alpha=1/150. The product is 2000/150=40/3. The direct path is 10×8/6=80/6=40/3. Subtracting gives 40/3−40/3=0. No intermediate rounded decimals were needed.

## C08.03-E2 — Reading the locked evaluation card

For active Cell3 the source-stored input areas, in nm², are bc=0.3578095391285615, ac=0.2611062357902053, ab=0.19486916546048413 (S02#/mature_locked_cell3/face_areas_nm2). A nanometre, nm, is 10⁻⁹ metre; nm² is its square area unit. All three inputs use the same unit, so it cancels. The source's stored output decimals are separately recorded facts about that file. They remain the authoritative stored witnesses; a fresh quotient is an arithmetic diagnostic, not a replacement authority.

A decimal lexeme is the original written number, including its digits. For exact recomputation, interpret a finite decimal as an integer divided by a power of ten: for example 0.125=125/1000=1/8. Apply this rule to each source area, then evaluate the definitions using fractions. The supplied card below removes long-integer arithmetic from the required student workload. Read a row as three linked numbers: stored, recomputed, and signed difference d=recomputed−stored. The reconstruction equation is recomputed=stored+d. Keep d even when it is tiny. These are arithmetic discrepancies between finite records, not new experimental residuals.

| Quantity | Stored S02 lexeme | Exact recomputation | Signed recomputed − stored |
|---|---|---|---|
| eta | 1836.1526734259999 | 35780953912856150000/19486916546048413 | 43827170816668413/194869165460484130000000000000 |
| alpha_inverse | 137.035999177 | 357809539128561500/2611062357902053 | 85645389619/2611062357902053000000000 |
| alpha | 0.0072973525643314245 | 2611062357902053/357809539128561500 | -1741030399723427/1431238156514246000000000000000000 |
| eta_alpha | 13.399053419929224 | 23736930526382300/1771537867822583 | -791906356108199/221442233477822875000000000000 |

The exact eta fraction, for example, is obtained by 1000×(3578095391285615/10¹⁶)/(19486916546048413/10¹⁷)=35780953912856150000/19486916546048413. The two product paths agree exactly when they use this same area triple. Mixing a stored output with a recomputed output need not give exact closure. The complete card and decimal displays are also in verification.json.

> Claim scope: W1 is synthetic. The card is a fresh evaluation of stored decimal areas alongside source-reported constants. S03#/authority_contract assigns precedence to mature stored lexemes; the arithmetic comparison does not reassign that precedence or certify the source's full physical interpretation.

Guided practice — C08.03-P1

For synthetic (15,10,5) U² calculate every output and both product paths. **Answer:** r=(1,2/3,1/3); eta=1000×15/5=3000; alpha_inverse=100×15/10=150; alpha=1/150. Product 3000/150=20, direct 10×10/5=20, closure 0. **P1 source-card follow-up:** identify the sign and reconstruction rule for the alpha row. **Answer:** d is negative; recomputed alpha equals the stored alpha plus that entire negative fraction. Do not replace d by zero.

Diagnostic checks

1. **C08.03-D1** Someone writes alpha=100 A_bc/A_ac. Repair it, then record all four signed differences from the locked card.

2. **C08.03-D2** For the synthetic W1 input, are the outputs in U², kilograms, or dimensionless?

3. **C08.03-D3** Why can 10 A_ac/A_ab be used as an independent arithmetic cross-check?

4. **C08.03-D4** Does the source-stored eta become invalid merely because a decimal-area recomputation differs?

Worked diagnostic answers

1. The displayed formula is alpha_inverse; alpha=A_ac/(100 A_bc). The four signed differences are the complete fractions in the card’s final column in eta, alpha_inverse, alpha, eta_alpha order; their signs are +,+,−,−. Retaining those exact fractions and using recomputed=stored+d completes the record.

2. Dimensionless: each construction divides equal area units and multiplies by dimensionless factors.

3. Substitution and cancellation derived it from eta×alpha, so a disagreement on identical exact inputs reveals arithmetic or input inconsistency.

4. No. Keep the stored witness in its source-authority role and the fresh value in its arithmetic-diagnostic role. Finite decimal input reconstruction and stored output records are distinct.

Next dependency: [lesson-04](lesson-04.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
