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
