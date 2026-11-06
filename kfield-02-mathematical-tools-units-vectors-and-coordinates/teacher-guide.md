# Teacher guide

## Intended use and entry check

Teach to high-school seniors who can subtract signed numbers, operate on fractions, multiply powers, solve one linear equation, and read a coordinate graph. Begin with four quick checks: -2-(-5) = 3; (3/4)×4 = 3; 2x+1 = 7 gives x = 3; plot (2,-1) with horizontal coordinate first. If these fail, model the specific operation and have the learner explain a second example before proceeding. No trigonometry, matrix multiplication, determinant, or inverse is assumed. Course-01's evidence distinction is restated in Lesson 01.

The seven lessons form three units: quantities and scale (01–02), arrows and projection (03–04), and reversible coordinate converters (05–07). Each unit ends with the cumulative checks below. Core lessons are designed for 55 minutes each; capstone uses two additional periods. Keep exact fractions on the board. A calculator may check arithmetic but is not needed for any core operation. Square roots can stay exact.

## Pacing and teaching moves

| Lesson | 55-minute sequence | Focus for feedback |
|---|---|---|
| 01 | 5 entry check, 12 units/scientific notation, 10 worked cycle, 8 guided practice, 15 diagnostics, 5 correction | Make students write cancelling units; a reciprocal millisecond is not a Hz |
| 02 | 5 recall, 12 factor derivation, 10 box example, 8 square practice, 15 diagnostics, 5 correction | Ask which lengths changed before choosing s² or s³ |
| 03 | 5 bridge, 12 point/vector and magnitude, 10 worked origin shift, 8 reverse-arrow practice, 15 diagnostics, 5 correction | Same numeric pair may label different objects; zero has no unit direction |
| 04 | 5 recall of normalization, 15 right triangles and projection, 10 worked axis case, 10 tilted case together, 10 diagnostics, 5 correction | Require scalar and vector answers separately, retain perpendicular r |
| 05 | 5 bridge, 12 column combinations, 10 worked forward/reverse, 8 guided practice, 15 diagnostics, 5 correction | Recover through equations first; coefficient is not projection |
| 06 | 5 recall, 15 determinant/inverse derivation, 10 negative example, 10 singular case, 10 diagnostics, 5 correction | D = 0 forbids inverse; D < 0 does not |
| 07 | 5 recall, 12 contract/rounding, 10 worked restoration, 8 guided practice, 15 diagnostics, 5 correction | Signed component residuals are part of the record |

For dense L04 or L06, the guided case is teacher-supported. If learners need more time, extend guided practice into a further period rather than omitting normalization, the inverse derivation, or the singular counterexample. Ask learners to explain a mistake in words before repeating arithmetic.

## Diagnostic use and unit checkpoints

Every lesson has four checks with worked answers. First let learners attempt the checks without the answer section visible, then compare methods and repair. A correct numerical result with missing units/order is not enough for a verified converter. Before advancing, require successful correction of the target mistake on a second case.

After L02, ask for the square-metre area of a 3 cm square and the volume factor under doubling. Answers: 0.0009 m² and 8. This tests conversion powers separately from physical scale. After L04, ask for the projection of (2,3) m along (0,2), dimensionless: scalar 3 m, vector (0,3) m, residual (2,0) m. Require reconstruction and explain the divide-by-2 step. After L07, ask learners to state a complete contract, find det([[1,2],[2,0]] m) = -4 m², and explain why a negative determinant is compatible with an inverse. Have them restore the worked example from its rounded coefficients and signed residual.

When an answer disagrees, keep the original attempt and corrected version as a learning record. A scalar error score can help plan practice but cannot replace the calculation or identify which coordinate was misunderstood. Preserve all residual components in the mathematical examples.

## Capstone administration

Period 1: 10 minutes to read and specify the contract, 35 minutes for tasks 1–4, 10 minutes to compare forward/reverse checks. Period 2: 25 minutes for projection and rounding, 15 minutes for a peer to reproduce the converter, and 15 minutes for correction and explanation. Use the 40-point rubric in capstone.md. Accept another declared rounding precision/rule only with consistent tie tests and full residual restoration. The key provides one complete implementation.

The capstone changes the numerical basis from the lessons, requiring transfer of the taught method. It introduces no new operation. Students may use the inverse derivation from L06 and the contract template from L07. A singular example must provide a concrete collision of inputs. Report mastery by operation as well as score. Any missing core operation is assigned targeted repair.

## Source and evidence boundaries

All concrete device and coordinate inputs are synthetic, not archived observations. Exact source context is limited to S02's basis and metric conventions. Source-reported proof labels remain reported labels; no archival proof has been freshly established by this course. The frozen-service capability response did not provide the packet's corpus generation; sources.md records that limitation. Local exact source hashes and required pointers were verified directly. Historical files are inventoried separately and their constants are not combined with the mature source.

Do not turn context-only ICRS, Cell3, or metric names into required student calculations. The pedagogic goal is the 2D mathematical toolkit. Later courses can bind those operations to source-locked geometry. Definitions, empirical observations, derivations, interpretations, and mechanisms remain separate evidence categories. Here the operative categories are synthetic inputs, derived mathematics, and source-reported conventions.

## Artifact and validation guide

course.md is assembled from the standalone lessons without substantive additions; links point to the capstone, glossary, and source records. verify_examples.py uses only Python's standard library, exact rational arithmetic, and small synthetic cases. Run it through the required tf_gpu_env Conda invocation. Then run the location-only validator adapter described in completion_report.json. The validator checks hashes, dependency order, assembly identity, audit consistency, and containment; it does not replace an educational or mathematical audit. Independent audit findings and repairs are in audit_report.json.
