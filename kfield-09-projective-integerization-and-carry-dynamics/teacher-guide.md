# Teacher guide

This course teaches a complete finite encoding and decoding workflow to seniors. It assumes signed arithmetic, exact fractions, powers, elementary equations, and coordinate order. The entry bridge refreshes the needed course-08 capability: reading a normalized ordered ray. It does not require calculus, abstract algebra, programming, or a physical interpretation of the ray.

## Pacing and dependency gates

| Lesson | Periods | Retrieval | Explanation/worked | Guided practice | Diagnostics/repair |
|---|---:|---:|---:|---:|---:|
| 01 rounding | 1 | 5 | 20 | 15 | 15 |
| 02 scales | 1 | 5 | 20 | 15 | 15 |
| 03 residual decoder | 1 | 5 | 20 | 15 | 15 |
| 04 carries: first period E1/W1 | 1 | 5 | 20 | 15 | 15 |
| 04 side coordinates: second period E2/P1 | 1 | 5 | 20 | 15 | 15 |
| 05 comparisons | 1 | 5 | 20 | 15 | 15 |
| 06 finite compiler | 1 | 5 | 20 | 15 | 15 |

Minutes in each row sum to 55. Add the two capstone periods described in capstone.md: nine periods, 495 minutes total. If a gate fails, add targeted practice time before advancing; this is a pacing estimate, not a requirement to hurry learners.

In lesson 01, teach E2 before the signed-tie return portion of P1. Ask students to speak “Q minus input” and “input minus owner” aloud to expose the different signs. A number line suffices; a complicated geometry diagram would obscure this distinction. Check both negative and positive ties without relying on a calculator's default rounding.

In lesson 02, insist on separate scaled-input and rounded-output columns. Read 729/2 as an exact fraction before discussing 364.5. Students should normalize (6,4,3) and explain why a magnitude would have to be retained to reconstruct that original triple. Carry only dimensionless normalized ratios into the ledger.

In lesson 03, require recovery of all three coordinates, not only the one with the largest residual. Use D3 to detect loss of sign. If a learner adds epsilon in the decoder, return to epsilon=Q−Kr and solve for Kr before dividing.

In lesson 04 period 1, compare integer subtraction with the separately computed residual-rounding route. Use P1's carry part for guided practice and D2/D4 for the check. Period 2 introduces sums/differences and even/odd integers before the name “lattice.” Use the side-mode part of P1 and D1/D3. Do not identify this parity with detector labels or introduce a root-system theory as a prerequisite.

In lesson 05, the historical g8 card is supplied reading, not an assignment to multiply 70-digit inputs by hand. Core calculations are the two finite rational comparisons. Ask “first within which generations, inputs, and rule?” and “what differs before the integers differ?” Preserve the entire residual triple. Teacher verification uses exact rational arithmetic rather than tolerances.

In lesson 06, cover the g2 expansion before the optional compact finite-sum notation. Hide the original practice ray during the backward decoder so that reconstruction is a genuine operation. The last fresh-rounding audit is needed even if a recurrence table is internally consistent.

## Assessment and repair

The worked examples model the operation; P1 items require an independent attempt before their displayed answers. Fold or hide answer sections for student copies. The diagnostics are short assessment items with worked feedback. Require correct operation and explanation on each dependency gate; use the capstone rubric for feedback, while unresolved sign, tie, parity, branch, or terminal-residual mistakes require repair regardless of total score.

For fresh repair numbers, use t=5/2 and −5/2: nint gives 2 and −3, each with epsilon=−1/2; cell owners are 3 and −2. For mode repair, S=6,A=−2 gives C_b=2,C_c=4, while S=6,A=−1 is invalid. These are extra practice, not new teaching. Ask the learner to explain why each operation is reversible before retrying the relevant diagnostic.

At the end of lesson 03, audit terminology and the integer/residual sign. At the end of lesson 04, audit recurrence, equal-parity inversion, and prerequisite closure. At the end of lesson 06, check every capstone map row. The coverage and backward maps in course-map.md identify actual content locations.

## Evidence and source handling

Sources are read-only. S02 M06 is the mathematical source for the generation and carry definitions; S03 identifies the rounding ambiguity repaired explicitly here. The finite examples are exact synthetic teaching inputs. The historical comparison uses S01 strings; the active S02 decimal tokens have their own replay. None of these computations certifies the archive's broader physical or formal claims. Unrelated Cell3 geometry, gauge branches, or energy models are not needed premises of this topical course.

Do not discard a residual, a disagreeing calculation, or a source branch. Keep the proposed row and its correction in student audit notes. Exact recovery concerns supplied inputs: normalization magnitude and unsupplied digits cannot be recreated by assertion. See sources.md and worked-example-verification.json for precise provenance and verification scope.

## Recovery and reproducibility

The manifest is the checkpoint authority. Before resuming, rehash its referenced files; a mismatched file is not passed. Review the first failed dependency before changing downstream material. Rebuild course.md only from the saved lesson files and refresh manifests after any correction. verify_examples.py checks the small rational ledgers and source hashes using the prescribed tf_gpu_env interpreter; it writes only compact teaching verification. The project validator checks containment, checkpoint hashes, dependencies, audit counts, and verbatim assembly, but does not substitute for reading the mathematics or the learning sequence.
