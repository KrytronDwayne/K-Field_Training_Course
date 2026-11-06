# Face-Area Ratios and the K-Field Mass Bridge

Student lessons in dependency order. Supporting source cards, glossary, teacher guide, and capstone are separate files.

<!-- BEGIN: lesson-01 -->
# Lesson 1: From faces to dimensionless ratios

Essential question: What information does a face-area ratio keep, and what must we retain to recover size?

Goals

- Compute a ray in bc/ac/ab order.
- Reconstruct all three areas from the ray and its labeled divisor.
- Explain why an area ray does not specify a unique spatial cell.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Courses 03 and 07 supply labeled geometry and arithmetic. Here the needed entry skills are multiplying two lengths to find a rectangular area and simplifying a fraction. Check: 3 times 4 is 12; 8/12 reduces to 2/3 by dividing numerator and denominator by 4. If either operation is uncertain, repeat with 6/9 before proceeding.

## C08.01-E1 — Labels before division

Imagine a classroom box with three perpendicular edges named a, b, and c. The face meeting b and c is called bc; the other two face types are ac and ab. Write their areas as A_bc, A_ac, and A_ab. A is a name for area, and its subscript identifies the face. If a length unit is U, area uses U²: a square U by U. Cell3 faces need not be rectangles. In this course their areas are supplied, so no angle formula or vector operation is needed.

An ordered triple is a list whose positions have declared meanings. We always use (A_bc,A_ac,A_ab). A positive area ray is the collection of all positive common multiples of one such triple. For example, (12,8,6) and (18,12,9) belong to one ray because the second is 3/2 times the first. The order still matters.

To normalize, divide each entry by the positive first area. This produces r=(1,A_ac/A_bc,A_ab/A_bc). The symbol r names the normalized area ray. Each quotient has units U²/U²=1, so it is dimensionless. The first entry is always 1; only the other two entries can vary independently. This determines the area triple up to one common multiplier. It does not determine all angles, edge directions, or a unique basis in space. In the source's phrase “projective shape,” the scope here is the projective **area** triple; a spatial reconstruction needs additional geometric assumptions.

Normalizing without retaining A_bc loses the absolute size. We therefore keep the pair (A_bc,r), including the unit and labels. The reconstruction rule is (A_bc,A_ac,A_ab)=A_bc times r, meaning multiply every component by the retained area.

## C08.01-W1 — A fully labeled synthetic box

Take a=2 U, b=3 U, c=4 U, mutually perpendicular. Its areas are bc=3×4=12 U², ac=2×4=8 U², ab=2×3=6 U². Normalize: 12/12=1, 8/12=2/3, 6/12=1/2. Thus r=(1,2/3,1/2), with divisor 12 U². Reconstruction gives 12×1=12, 12×2/3=8, and 12×1/2=6 U². Every original component is recovered.

> Claim scope: This is a synthetic orthogonal box, not Cell3 or a measurement. The ray definition is S02#/backbone_sequence/4/definitions. Source paths and verified hashes are in sources.md. Source Cell3 uses an ordered basis with a negative determinant; positive face-area magnitudes do not encode that orientation.

Guided practice — C08.01-P1

Normalize (18,12,9) U², keep the divisor, and reconstruct. Work before reading the answer. **Answer:** dividing by 18 U² gives (1,2/3,1/2). Multiplying that ray by 18 U² gives (18,12,9) U². The normalized shape matches W1, while each area is 3/2 as large. The divisor distinguishes them.

Diagnostic checks

1. **C08.01-D1** Swap ac and ab in W1 while retaining the declared order. What ray results?

2. **C08.01-D2** Normalize (15,10,5) U² and reconstruct it.

3. **C08.01-D3** Can (1,2/3,1/2) alone tell you A_bc or the cell angles?

4. **C08.01-D4** Why must A_bc be positive in this course?

Worked diagnostic answers

1. The input becomes (12,6,8), so r=(1,1/2,2/3); this differs from W1.

2. Dividing by 15 gives (1,2/3,1/3). Retain 15 U²; multiplying returns (15,10,5) U².

3. No. Any positive divisor supplies a possible size, and the ray contains no complete angle specification.

4. Zero would make division undefined; negative values would not be positive face-area magnitudes. The positivity contract also makes every later reciprocal defined.

Next dependency: [lesson-02](lesson-02.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2: What uniform scaling leaves unchanged

Essential question: Why can changing every length leave the area ray unchanged?

Goals

- Derive the square law for uniform length scaling.
- Prove cancellation in both independent ratios.
- Distinguish uniform scaling from changing a single supplied area.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Lesson 1 taught the ordered triple and retained divisor. Recall that multiplying a fraction numerator and denominator by the same nonzero number preserves its value. Check 8/12=32/48=2/3. We now explain where the common factor comes from.

## C08.02-E1 — One scale, two length factors

Let s be a positive dimensionless length multiplier: every length becomes s times its old value while angles remain fixed. A face has two length factors. In a rectangle, (s×length)(s×width)=s²×area. A parallelogram obeys the same rule: its base and perpendicular height both scale by s. Here s² means s×s. Thus all three areas are multiplied by s². This uniform transformation is sometimes written B→sB, where B is the ordered list of the three basis vectors; no matrix calculation is needed here.

Write A'_ac=s²A_ac and A'_bc=s²A_bc, where the prime marks the scaled value. Because s>0 and A_bc>0, the denominator is nonzero. Cancel the common factor to obtain A'_ac/A'_bc=(s²A_ac)/(s²A_bc)=A_ac/A_bc. Separately, A'_ab/A'_bc=(s²A_ab)/(s²A_bc)=A_ab/A_bc. These two calculations prove invariance of both independent components, rather than relying on one numerical coincidence. The first ray component remains 1.

To reverse the scaling, divide all scaled areas by s² if s is retained. Alternatively retain the original A_bc as a dimensional anchor along with r. A ray by itself cannot tell us which s was used.

## C08.02-W1 — Doubling lengths

Starting with (12,8,6) U², choose s=2. Then s²=4 and the new areas are (48,32,24) U². Dividing by 48 gives (1,32/48,24/48)=(1,2/3,1/2). Divide the new areas by 4 to recover (12,8,6). The areas changed, although the ray did not.

> Claim scope: The proof applies to a positive uniform rescaling with angles and face labels fixed. It does not assert that any arbitrary change in three supplied areas is uniform scaling. It reproduces the common-scale argument in S01 and S02, M05; it establishes algebraic invariance, not a physical mechanism.

Guided practice — C08.02-P1

Use s=1/2 on W1’s original input. Compute the areas, normalize, and reverse. Then prove both ratio cancellations for an arbitrary positive s and positive starting areas. **Answer:** s²=1/4, so the areas are (3,2,3/2) U². Their ray is (1,2/3,1/2). Dividing by 1/4, equivalently multiplying by 4, restores (12,8,6) U². For arbitrary s>0, the two ratios are (s²A_ac)/(s²A_bc)=A_ac/A_bc and (s²A_ab)/(s²A_bc)=A_ab/A_bc. Each cancellation is valid because s² is nonzero and A_bc>0. Thus both independent components remain unchanged for every permitted s, not only the numerical case.

Diagnostic checks

1. **C08.02-D1** Change only A_ac from 8 to 9 U². Does the ray remain fixed?

2. **C08.02-D2** Starting with (15,10,5), test s=2 and s=1/2.

3. **C08.02-D3** Why is s=0 excluded from the proof?

4. **C08.02-D4** If areas all double, did lengths necessarily double under uniform scaling?

Worked diagnostic answers

1. No. The new ray is (1,9/12,6/12)=(1,3/4,1/2). Only one supplied area changed.

2. The triples are (60,40,20) and (15/4,5/2,5/4). Divide by 60 or 15/4 respectively to get (1,2/3,1/3) in both cases.

3. All areas would become zero, so the normalized fractions would be 0/0 and undefined.

4. No. Doubling lengths multiplies areas by 4. An area factor of 2 requires a positive length multiplier whose square equals 2; no square-root computation is required.

Next dependency: [lesson-03](lesson-03.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
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
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 4: Locked and historical numerical branches

Essential question: How can we preserve numerical history without turning it into a second active geometry?

Goals

- Build separate active and historical provenance rows.
- Retain signed branch differences with a reconstruction rule.
- Detect a mixed-input calculation mislabeled as active.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Lesson 3 distinguished stored lexemes from fresh computations. We now attach each number to its origin. A source pointer is a path inside a JSON document: /backbone_sequence/4 refers to the fifth array entry because indexing begins at zero. A SHA-256 is a file fingerprint used here to check that the read bytes match the supplied source; it does not by itself prove a claim.

## C08.04-E1 — The branch ledger

A numerical witness is a recorded value accompanying a source claim. A branch is a coherent set of values with a stated provenance and role. To keep a replayable ledger, record source ID, its hash from sources.md, exact pointer, original decimal lexeme, component label, units, and active or historical role. “More digits” does not mean “more authoritative.”

S02 supplies the active mature ray. S01 contains two longer-string rays, named master_geometry and locked_mass_bridge, and a separate mass_bridge_calibration input set. Preserve all of these as history. S04’s M05 audit directs the earlier rays into a superseded-history ledger, and S03 assigns mature stored lexemes precedence. Thus the word locked inside an old field name does not override the later authority contract.

For a comparison, define d=active−historical component by component. Then active=historical+d and historical=active−d. Negative d means the active component is smaller. These differences are provenance comparisons; they are not measurement residuals or alternative active geometry coordinates. The active ray stored in S02 and a fresh ray obtained by dividing S02 decimal areas also remain separately typed records.

## C08.04-W1 — Preserve three ray records

The active row is S02#/backbone_sequence/4/projective_ray, order bc/ac/ab, dimensionless: (1.0,0.7297352564331424,0.5446170214888189). Attach S02’s complete hash from sources.md. Compare it separately to each historical S01 row below; attach S01’s hash to each. The fractions are exact differences of the displayed finite lexemes, independently checked in verification.json. For the master_geometry ac row, subtraction gives a negative fraction: the active value is smaller by about 2.6063552449324×10⁻¹¹. Here 10⁻¹¹ means dividing by 100000000000. That short decimal display is only an aid; the exact difference remains in the table.

Historical pointer: `S01#/backbone_sequence/4/projective_rays/master_geometry`.

| Component in bc/ac/ab order | Historical lexeme | Active S02 lexeme | Exact active − historical |
|---|---|---|---|
| bc | 1 | 1.0 | 0 |
| ac | 0.72973525645920595244932401459164514764311273208360709830244089259013899526544427 | 0.7297352564331424 | -2606355244932401459164514764311273208360709830244089259013899526544427/100000000000000000000000000000000000000000000000000000000000000000000000000000000 |
| ab | 0.54461702151513304256465588852004665566471160638980820098958492135543133394303553 | 0.5446170214888189 | -2631414256465588852004665566471160638980820098958492135543133394303553/100000000000000000000000000000000000000000000000000000000000000000000000000000000 |

Historical pointer: `S01#/backbone_sequence/4/projective_rays/locked_mass_bridge`.

| Component in bc/ac/ab order | Historical lexeme | Active S02 lexeme | Exact active − historical |
|---|---|---|---|
| bc | 1 | 1.0 | 0 |
| ac | 0.72973525643314250302457952646916832280660213133653604957798803819933561573639928 | 0.7297352564331424 | -1287807244080864604035082526641706700619724850477491695196704991/12500000000000000000000000000000000000000000000000000000000000000000000000000000 |
| ab | 0.54461702148881883791248505567449693562745711038305542415906631382184511315519240 | 0.5446170214888189 | 155218787360813757660931357224042361439602334215445387217112019/2500000000000000000000000000000000000000000000000000000000000000000000000000000 |

In the historical locked_mass_bridge comparison, ac decreases and ab increases. Reversing subtraction would reverse both signs. The leading component has difference zero in both comparisons because 1.0 and 1 are equal numbers; the original spellings remain recorded.

> Claim scope: These are source-history differences, not measured changes through time. The active field does not inherit extra digits from either historical field. S01#/mass_bridge_calibration is a separate historical calibration record; its face inputs must not be substituted into active S02 formulas.

Guided practice — C08.04-P1

Use the second table to recover the active ab component from the historical ab component and d. Then name the complete historical calibration input set. **Answer:** historical ab+d=0.5446170214888189 exactly; retaining the table’s positive fraction ensures exact recovery. The historical calibration areas at S01#/mass_bridge_calibration/face_areas_nm2 are (bc,ac,ab)=(0.3578095391285618,0.26110623579953135,0.1948691654698998) nm². They are one historical input set, not rounded replacements for active inputs. For each of the two tables, the full signed difference vector is its last column in bc/ac/ab order; retain all three components including zero.

**P1 ledger construction:** Build a complete provenance row for the active ray, then a historical row for S01's locked_mass_bridge ray. Include the original lexemes, hash reference, pointer, order, unit, and role. **Answer:**

| Source and hash reference | Exact pointer | Original lexemes | Order and unit | Role |
|---|---|---|---|---|
| S02; full verified S02 SHA-256 in sources.md | /backbone_sequence/4/projective_ray | (1.0,0.7297352564331424,0.5446170214888189) | bc/ac/ab; dimensionless | Active mature stored ray |
| S01; full verified S01 SHA-256 in sources.md | /backbone_sequence/4/projective_rays/locked_mass_bridge | (1,0.72973525643314250302457952646916832280660213133653604957798803819933561573639928,0.54461702148881883791248505567449693562745711038305542415906631382184511315519240) | bc/ac/ab; dimensionless | Superseded historical ray |

Attach the second comparison table's full difference vector to these two rows, explicitly labeled active minus historical. This adds the comparison without overwriting either source record.

Diagnostic checks


1. **C08.04-D1** A calculation uses historical A_ab and mature A_bc and calls its result “active eta.” What is wrong?

2. **C08.04-D2** Does the longer historical ac lexeme outrank the shorter mature lexeme?

3. **C08.04-D3** In the second table, what does a positive ab difference mean, and how do you recover history?

4. **C08.04-D4** What distinguishes a provenance difference from the closure difference of lesson 3?

Worked diagnostic answers

1. It mixes source branches. Use all active S02 inputs for active recomputation, or label the result a mixed-input diagnostic with both exact pointers. It is not an active eta witness.

2. No. Authority follows the source contract and branch role, not digit count.

3. The active ab ray component is larger. Historical=active−d, using the exact positive fraction.

4. Provenance difference compares records from separate branches; algebraic closure compares equivalent calculation paths for one input set. Neither is automatically an experimental measurement residual.

Next dependency: [lesson-05](lesson-05.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
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
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6: Sensitivity and retained numerical closure

Essential question: How can we change one input and preserve every resulting difference?

Goals

- Reevaluate all outputs after a finite input change.
- Retain signed changes and reconstruct every new output.
- Distinguish finite sensitivity from arithmetic closure.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Lesson 3 supplies all output formulas; lesson 4 supplies signed differences and reconstruction. A finite change compares two complete input triples. We need no derivative or limit. Subtract fractions using a common denominator: 1/2−1/3=3/6−2/6=1/6.

## C08.06-E1 — Two different kinds of difference

Sensitivity here means how the output changes when a specified input changes and the other inputs remain fixed. Keep the original triple, the input-change vector, the full new outputs, and the signed output differences. An input-change vector is simply the ordered list of new-minus-old changes. Zeros matter because they tell us what stayed fixed.

For any quantity y, write Δy=y_new−y_old; Δ is just a label meaning change. The reconstruction rule is y_new=y_old+Δy. This preserves the full finite difference even if a short decimal display hides it. Separately calculate closure c=eta×alpha−10 A_ac/A_ab using the same complete input triple. Sensitivity can be nonzero while c stays zero. One compares two input states; the other compares two algebraic paths within one state.

## C08.06-W1 — Change the ab area

Baseline areas are (12,8,6) U². Change only ab by +1/10 U², so the new triple is (12,8,61/10) U² and the input change is (0,0,1/10) U². Normalize: (1,8/12,(61/10)/12)=(1,2/3,61/120). Evaluate eta=1000×12/(61/10)=120000/61; alpha_inverse=150; alpha=1/150. The product path gives (120000/61)/150=800/61. The direct path gives 10×8/(61/10)=800/61. Closure is zero.

| Output | Old | New | Signed new − old |
|---|---|---|---|
| r_bc | 1 | 1 | 0 |
| r_ac | 2/3 | 2/3 | 0 |
| r_ab | 1/2 | 61/120 | 1/120 |
| eta | 2000 | 120000/61 | −2000/61 |
| alpha_inverse | 150 | 150 | 0 |
| alpha | 1/150 | 1/150 | 0 |
| eta_alpha | 40/3 | 800/61 | −40/183 |

For eta, subtract 2000=122000/61 to obtain −2000/61. For the product, use denominator 183: 800/61−40/3=(2400−2440)/183=−40/183. Reconstruction returns eta=2000−2000/61=120000/61 and product=40/3−40/183=800/61. For the ray’s third component, 1/2+1/120=61/120. Adding zero returns every unchanged entry. All outputs are dimensionless; only the supplied area changes carry U².

> Claim scope: These are supplied synthetic area states, not a measured trajectory or an experiment on Cell3. Exact finite sensitivity and exact arithmetic closure are taught core operations. No approximation is needed, and no difference is discarded.

Guided practice — C08.06-P1

Return to the baseline and instead change only ac from 8 to 81/10 U². Compute every output, difference, and both product paths. **Answer:** input change (0,1/10,0) U²; new ray (1,27/40,1/2). Eta=2000; alpha_inverse=1200/(81/10)=4000/27; alpha=27/4000. Product=2000×27/4000=27/2, also 10×(81/10)/6=27/2. Ray differences are (0,1/120,0); remaining differences in eta, alpha_inverse, alpha, eta_alpha order are 0,−50/27,1/12000,1/6. For example 4000/27−150=(4000−4050)/27=−50/27 and 27/4000−1/150=(81−80)/12000=1/12000. Reconstruct each by adding: 2/3+1/120=27/40; 150−50/27=4000/27; 1/150+1/12000=27/4000; 40/3+1/6=27/2. Unchanged components reconstruct by adding zero.

Diagnostic checks

1. **C08.06-D1** For W1 give the product-path value, direct-path value, closure, and product sensitivity.

2. **C08.06-D2** Why is retaining only the largest output change insufficient?

3. **C08.06-D3** In P1, reconstruct alpha_inverse from its baseline and signed difference.

4. **C08.06-D4** A student calls the W1 product difference −40/183 an algebraic failure. Correct this.

Worked diagnostic answers

1. The two paths are both 800/61; closure is 0; sensitivity relative to baseline is −40/183. They compare different things.

2. It loses the other components, signs, and unchanged coordinates, preventing complete reconstruction. Keep all seven entries and the input change.

3. 150+(−50/27)=(4050−50)/27=4000/27.

4. −40/183 compares the product at two different input triples. Within the new triple both algebraic paths agree exactly, so there is no closure failure.

Next dependency: [capstone](capstone.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
<!-- END: lesson-06 -->
