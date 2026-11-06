# Teacher guide

This course teaches six linked operations, not a survey of later K-Field mechanisms. Keep two sheets visible throughout: the integer **Classroom analogue, not Cell3**, and the separately labeled locked geometry card. Students calculate with the analogue and read the actual record with provenance. The required output is a checked pair of cards, supported by calculations and a residual record.

## Entry check and preparation

Before Lesson 1, ask students to calculate −2+5, 3/4−1/4, solve 2v=6, and plot (1,−2). Answers are 3, 1/2, v=3, and one unit right/two down. Then ask them to add (1,0)+(1,2)=(2,2) and distinguish a point from a displacement. If the last two capabilities are unfamiliar, use the Lesson 1 bridge with arrows before introducing the third component. Signed arithmetic and simple equations are the only assumed calculation tools. Matrix multiplication, cross products and inversion are taught here.

Print or display the six lessons, geometry-card.md, and terminology.md. A calculator in degree mode is useful for the optional decimal angle; students may leave cos(theta)=1/sqrt(5) exactly. No coding or archive access is required for core assessment. The teacher may replay verify_examples.py through the specified tf_gpu_env runtime; verification.json already contains the declared arithmetic and all residual entries. Do not install packages. Do not rerun initialize.py: it is a historical production script that resets drafts.

## Pacing and instructional decisions

Each row totals 55 minutes. The two units end after Lessons 3 and 6. Allocate two additional 55-minute capstone periods, for 440 minutes overall. These are planning allocations, not measured classroom timings.

| Lesson | Bridge/read | Explanation/model | Guided practice | Independent diagnostics | Discuss/exit |
|---|---:|---:|---:|---:|---:|
| 1: ordered columns | 8 | 15 | 12 | 12 | 8 |
| 2: Gram matrix | 7 | 18 | 12 | 12 | 6 |
| 3: faces/volume | 7 | 17 | 13 | 12 | 6 |
| 4: inverse | 5 | 20 | 15 | 10 | 5 |
| 5: scale | 7 | 18 | 13 | 12 | 5 |
| 6: reproducibility | 7 | 15 | 15 | 12 | 6 |

In Lesson 1, color the columns before doing arithmetic. Ask students to say “copies of edges” when describing q and “external components” when describing Bq. Use the negative third edge to discuss intentional handedness without changing axes. In Lesson 2, have pairs compute opposite off-diagonal entries separately, then compare them. Require both the Cartesian and Gram calculation for q=(1,−1,0). Their agreement exposes the omitted-cross-term error directly.

In Lesson 3, label ab/ac/bc before any cross product. Test perpendicularity with a dot product, then distinguish a signed triple product from positive volume. At the unit boundary, ask students to recover q=(1,−1,2) from (0,−2,−6)L and explain why the Gram entries do not encode handedness alone. The earlier lessons supply both operations. Correct the earliest misunderstood column or sign before proceeding.

Lesson 4 is the densest lesson. Keep the same block matrix on the board; do not add a general inverse formula or determinant expansion. Solve u+v=s and u+5v=t slowly, then read the coefficients into the inverse. The reciprocal-basis section provides reconstruction meaning; students need not memorize a separate inversion algorithm. Pair students to check the two products entry by entry. If the prerequisite check reveals fraction or block-inverse difficulty, add a guided-practice period before Lesson 5. Recheck the two-equation solution and one inverse-product entry before dependent work or independent assessment. Keep the six conceptual lesson IDs; the total number of teaching periods is flexible.

In Lesson 5, first scale the analogue; then introduce the source's conditional theorem. Stress the fixed angular frame, positive ratios and positive anchor. The separate right-angle ray is explicitly a different synthetic example. Students are not asked to derive eta, alpha, an astronomical frame, or a mass interpretation. At the second unit boundary, ask each student to identify one input, one derived quantity, and one retained residual from the card/verification materials.

Lesson 6 is a reading-and-reconstruction lesson. Display the two unequal stored reciprocal entries side by side. Ask what averaging them would change. For all decimal checks, keep the originals, operation, signed difference, and reconstruction equation together. The full matrices in verification.json are teacher replay support; students interpret one entry and its units, not a new software API.

## Diagnose and repair

| Observable error | Targeted repair | Recheck |
|---|---|---|
| Reads a row as an edge | Trace one column across x/y/z labels | L1 check 1 |
| Omits cross terms | Expand both ij and ji terms | L2 check 2 |
| Treats negative volume as negative size | Compare determinant with its absolute value | L3 check 3 |
| Uses R as direct position-to-coordinate map | Contrast R units with reciprocal basis D; subtract O_K | L4 check 3 |
| Claims ratios determine absolute size | Compare s=1 and s=2 with same area ratios | L5 check 3 |
| Erases a small residual | Reconstruct computed value as reference plus residual | L6 check 3 |
| Blends historical and mature values | Require source ID and pointer on each card field | Capstone B |

All diagnostic keys are in their lessons. Award method credit when a single arithmetic slip propagates consistently, but require correction of conceptual mistakes before regarding the associated capability as secure. Do not use a total score to hide an unresolved column convention, inverse-domain error, or fabricated source claim.

## Capstone administration

Period 1: 10 minutes retrieval/review, 35 minutes Part A, 10 minutes paired arithmetic checking with corrections visibly retained. Period 2: 25 minutes Part B, 15 minutes Part C, 15 minutes explanation and revision. Supply the locked card, sources.md and the printed residual component requested in Part C. Students submit their own final explanations. The 100-point analytic rubric and complete key are in capstone.md. No task requires numerical inversion of the long-decimal locked matrix.

For extensions only, students may compare additional stored closure components or verify D^T D=R symbolically. These are not hidden prerequisites or required core assessments. The course's boundary is geometric specification and conditional scale uniqueness. It makes no new empirical or mechanism claim.

## Verification and recovery

The manifest identifies the active files, dependencies and SHA-256 hashes. course.md contains the lessons verbatim in order. Full residuals are retained alongside reconstruction formulas, and the source files remain at their recorded paths. A source-reported closure scalar is not presented as the fresh Decimal calculation. The source's underlying arithmetic for that scalar remains unspecified; the fresh calculation has a complete declared recipe.

The location adapter changes only the validator's containment root, as authorized by the user. It does not waive lesson, hash, audit, assembly or completion checks. Use completion_report.json and the [destination validation record](../kfield-series-20261105/audits/consolidation/course-03-consolidation.json); its destination_validator_passed field records the project-folder validation. Subsequent audit repairs and final validation are recorded in [parent acceptance](../kfield-series-20261105/audits/independent-completion/course-03-parent-acceptance.json).
