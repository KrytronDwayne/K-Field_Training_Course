# Lesson 5: Geometry, calibration, and interpretation

Essential question: What additional information turns an algebraic ratio into a physical claim?

Goals

- Separate a dimensional anchor from a dimensionless ratio.
- Classify source facts, algebra, calibration, physical identification, and mechanism.
- State the provenance needed for a mass measurement comparison.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Lessons 1–4 taught reconstruction and provenance. A calibration is a rule or reference that fixes a numerical scale or interpretation. Here we can supply an area anchor without claiming it was measured. Ask first whether a sentence describes a calculation, a source record, or a physical identification.

## C08.05-E1 — A ratio-to-claim ledger

Write each claim beside its inputs and evidence class. “S02 stores eta=1836.1526734259999” is a source fact verified by reading the file. “The two area quotients survive a uniform rescaling” is a mathematical implication proved in lesson 2. “Choose A_bc=12 U²” is a supplied dimensional anchor in a synthetic example. “Interpret eta as a specified physical mass ratio” adds a physical identification. A proposed mechanism would explain why that physical system obeys the identified relation, including what connects its measured quantities to these areas. These sentences can support one investigation while remaining different kinds of statements.

An area ray cannot select an absolute scale, because every positive common area multiple gives the same ray. An anchor supplies that missing scale. Likewise a dimensionless eta is not itself a mass in kilograms. Even identifying eta with a ratio m_1/m_2 requires names and definitions for both physical masses; finding m_1 from that relation also requires a dimensional m_2. This is a unit argument, not a dismissal of the proposed identification.

If testing the identification experimentally, retain the measurement records, units, instrument and calibration information, acquisition conditions and dates, definitions of the compared masses, the complete model input branch, and every signed prediction-minus-measurement difference. None of those measurements is supplied by the classroom examples. Repeated agreement could motivate a common mechanism, but algebra, calibration, observations, and interpretation should remain traceable separately. A candidate mechanism must at least account for the ratio’s common-scale invariance and the coupling between its two independent components; the course does not invent such a mechanism.

## C08.05-W1 — Recover size without inventing a mass

Given synthetic r=(1,2/3,1/2), supply A_bc=12 U². This is an input, not a conclusion. Multiply: A_ac=12×2/3=8 U² and A_ab=12×1/2=6 U². Those are derived reconstructions. Evaluating eta gives 2000 and alpha gives 1/150, both dimensionless. A statement “eta is a physical mass ratio” belongs in a new interpretation row with its own physical definitions. The area multiplication has not measured a mass.

| Ledger row | Evidence class | What follows |
|---|---|---|
| Supplied A_bc=12 U² | Synthetic anchor | Fixes area scale in this example |
| A_ac=8 U²; A_ab=6 U² | Derived reconstruction | Recovers the supplied triple |
| eta=2000 | Derived definition | Dimensionless quotient |
| eta identified with specified m_1/m_2 | Proposed physical identification | Needs physical definitions and measurement provenance |
| A process causes that identification | Proposed mechanism | Needs a stated rule connecting system and geometry |

> Claim scope: No new particle-mass dataset is supplied. S04 describes the calibrated Mass-Bridge theorem in source-reported terms. Its reported status is preserved in sources.md, distinct from this course’s fresh fraction checks. Established dimensional arithmetic is our reference tool; it does not supply missing physical observations.

Guided practice — C08.05-P1

A fictional calibration sets A_bc=18 U² with the same ray. Recover areas and eta/alpha; classify the anchor, reconstruction, and an asserted physical identification. **Answer:** areas (18,12,9) U²; eta=1000×18/9=2000; alpha=12/(100×18)=1/150. Anchor: supplied calibration. Areas and quotients: derived. Physical identification: additional interpretation. No measured mass was supplied. A future measurement ledger needs the mass definitions, measured values and units, instrument/calibration, acquisition context, model branch, and signed differences.

Diagnostic checks

1. **C08.05-D1** Repair the claim “calculating eta from areas independently measured a particle mass.”

2. **C08.05-D2** If the dimensional anchor changes from 12 to 18 U² but the ray stays fixed, what happens to eta?

3. **C08.05-D3** Name one missing input for converting a dimensionless mass ratio into a mass.

4. **C08.05-D4** Is the assertion “a mechanism makes geometry control masses” the same evidence class as computing eta?

Worked diagnostic answers

1. We calculated a source-defined dimensionless quotient. A separate physical identification and independently documented measurement would be needed for a measurement claim. Keep the interpretation as a proposed identification, not as fabricated observation.

2. It stays 2000: both numerator and denominator acquire the same factor 3/2.

3. A reference mass with its unit, together with the identification of numerator and denominator physical quantities.

4. No. The former is a proposed mechanism; the latter is a derived calculation. A mechanism needs a connecting rule and predictions beyond the quotient evaluation.

Next dependency: [lesson-06](lesson-06.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
