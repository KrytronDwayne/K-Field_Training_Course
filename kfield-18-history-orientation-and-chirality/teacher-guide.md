# Teacher guide — History, Orientation, and Chirality

The course aims at operational understanding: students can build and recover finite ledgers, distinguish domains, and read exact source claims without replacing their premises. It is a 12-period topical course with a three-period synthesis assessment. All periods are 55 minutes. Student lessons contain complete practice and diagnostic answers; capstone.md contains the full 100-point key. Separate that key during assessment if appropriate.

## Entry check and bridges

Ask students to evaluate (−2)²+3², compute 2·(1/2), distinguish ordered pairs (1,2) and (2,1), and explain why a missing slot differs from a slot containing zero. Answers: 13, 1, distinct order, and different record structure. Repair signed arithmetic before matrix work. No determinant expansion, calculus, Hilbert-space proof or quantum physics is an assumed skill. Courses 06, 15 and 17 provide series context, but each required finite operation is retaught here.

Use labeled index cards to implement words and paired factors. Keep every label on the table even when its coefficient is zero. Have students state an input domain and output codomain before deciding whether a map is reversible. This catches the central false transfer from infinite unilateral shift to finite square truncation.

## Session plan and interventions

Each core session allocates 5 minutes retrieval, 20 explanation/worked example, 15 guided or independent practice, and 15 diagnostic feedback/repair. Totals are 60 retrieval, 240 teaching, 180 practice and 180 diagnostics = 660 core minutes.

| Period | Material | Observable check and intervention |
|---|---|---|
| 1 | Lesson 01 | All seven labels present. If Ω disappears, compare e_Ω to the zero vector explicitly. |
| 2 | Lesson 02 A | Read matrix columns as unit-vector outputs; test prefix removal on root and mismatched prefix. |
| 3 | Lesson 02 B | Calculate both defects. If index −1 appears for square S, enumerate both kernels. |
| 4 | Lesson 03 | Give unreachable output e_0 for T; reconstruct arbitrary codomain vector. |
| 5 | Lesson 04 | Show q_2 can have rank 1 and yield zero on one input; check P=I counterexample. |
| 6 | Lesson 05 | Separate time sign from det B; record every swap/reflection. |
| 7 | Lesson 06 A | Derive grade projectors and GX+XG=0; distinguish sum from difference of products. |
| 8 | Lesson 06 B | Build four pair labels before selecting two. Retain the complement. |
| 9 | Lesson 06 C | Add angular dimensions; double for spin labels; enforce ell=0 exception. |
| 10 | Lesson 07 A | Read all seven source cards, match M03/M11 roles, identify missing T_0/B_8 definitions. |
| 11 | Lesson 07 B | Practice i²=−1 and row-by-column complex products; compare common diagonal maps. |
| 12 | Lesson 07 C | Recompute diagonal determinant witness; distinguish algebraic existence from phase prediction. |
| 13–15 | Capstone | 165 minutes across the task groups printed in capstone.md; require reconstruction and scope review. |

Before period 10, retrieve the generic grading proof from period 7. The six-sign-flip Clifford illustration is a conditional reading aid, not a required matrix-construction exercise. Students only need to identify its convention as a premise. If complex arithmetic needs more time, add a recovery period rather than omitting CP or assigning untaught work. The scheduled 12 core periods are planned instructional capacity, not an empirical claim about every class's pace.

## Cumulative checks

After Lesson 04, compare S, T and U in a three-row table. Require domain, terminal/root defects and reconstruction; an error here must be repaired before source index discussion. After Lesson 06, compare spatial sign, time sign, generic grade, L/R, exterior parity and spin labels. Ask which operations act on which factor; no shared-sign analogy may replace an explicit definition. After Lesson 07, ask students to sort statements into fresh finite checks, source-reported statements, conditional constructions and unresolved replay gaps. A proposed physical mechanism is welcome as an explicitly labeled proposal with its additional assumptions; it is not substituted for a taught identity.

## Assessment and feedback

Use the four diagnostics in each lesson as formative checks, covering the goals and common failure modes. Students should attempt P1 before revealing its answer. Reuse the same small numbers in the capstone to assess organization, reasoning and source scope rather than arithmetic novelty. Give a short oral variation, such as changing the terminal coefficient from 5 to −5, if independent understanding needs confirmation: only that retained coordinate changes sign; the loss in squared norm remains 25.

The capstone's ten 10-point rows sum to 100. Preserve method credit for a propagated arithmetic slip. Require correction of statements such as “finite S is an isometry,” “determinant 1 predicts nonzero CP,” or “L equals even.” Keep the original response and correction in student work so the learning residual is visible. Do not discard a low-scoring or unusual response as meaningless; use it to locate an unresolved definition or operation.

## Evidence and source policy

sources.md lists exact read-only archive hashes and JSON pointers. The principal source is mature S02, with S03 AUD-009 qualifying replay status. The title “complete proof” is a source label, not our verification result. The course freshly checks finite identities and supplied-rule arithmetic. It does not claim a full physical chirality-selection proof, T_0 replay, angular Hamiltonian or physical CP phase prediction. The binary alphabet, diagonal B and small matrices are explicitly synthetic. No measured data are fabricated or copied.

Do not introduce unrelated locked-geometry constants as exercises. Preserve ICRS [a b c] negative orientation and source-local carrier order when referring to them. Other packet invariants remain reserved guards: no dyadic/ternary identification, parity conflation, metric conflation, silent half-tie rule, or M19-to-M20 dependency is introduced. Those inactive subjects are not extra prerequisites for this topical course.

## Recovery and reproducibility

manifest.json is the recovery authority. Before trusting a passed checkpoint, hash its relative file and compare. Course assembly inserts each lesson verbatim in course_order between exact BEGIN/END markers. verify_examples.py recomputes finite examples and checks teaching IDs using only the standard library; it also verifies the five source hashes without saving source snapshots. Run it through the specified tf_gpu_env Conda command. The final project-root validator checks containment, hashes, dependencies, audit counts and assembly identity. It supplements human teaching/source audit; it cannot itself prove pedagogical completeness.
