# Teacher guide — Lucas Graphs: Edges, Cycles, and Memory

This topical course serves high-school seniors comfortable with signed arithmetic, fractions, coordinate labels and short simultaneous equations. The series lists courses 05 and 10 as prerequisites; this course locally teaches every graph, matrix and basis operation actually assessed. Do not assume university linear algebra. The goal is for learners to reproduce the finite constructions and preserve state information, rather than repeat dimension labels.

## Pacing and checkpoints

| Lesson | Periods × 55 min | Focus and readiness evidence |
|---|---:|---|
| 01 | 1 | Count by direction; distinguish an edge from a diagonal or jump |
| 02 | 2 | A: incidence and multiplication; B: rank elimination, transpose and orientation |
| 03 | 2 | A: tree/chord cycle; B: gradient, cut interpretation, dot product and decoder |
| 04 | 1 | Derive V−1 and E−V+1; specify the actual Lucas tree |
| 05 | 2 | A: periodic construction and counts; B: mean/details inverse and full basis sum |
| 06 | 1 | Reconstruct general flows and keep the tree remainder |
| Capstone | 2 | First period steps 1–4; second steps 5–6 and repair |

Each core period allocates 5 minutes retrieval, 20 instruction and worked example, 15 independently attempted guided practice, and 15 diagnostics and repair. Total core time is 495 minutes; capstone 110; total 605. These nine core periods preserve the blueprint's dense-lesson splits while keeping the original six lesson IDs. If a class needs more time, use the diagnostic repair tasks below before continuing; no accelerated omission is implied.

For Lesson 02 period B, revisit the square practice and ask students to derive the independence equations without looking at the answer. For Lesson 03 period B, rework the square with the supplied potential and require typed node/edge labels. For Lesson 05 period B, cover the answer and recover the supplied nine entries from W and eight details; then locate the three nonzero edges of 9h_(0,9). The second period in each lesson adds conceptual work, not extra unexplained notation.

## Teaching moves and diagnostic repairs

Start with dots and string or a plain drawing. Count edges with a mark at the lower-coordinate endpoint, so learners do not count both directions twice. A graph arrow is a reference sign: demonstrate reversal by changing both arrow and coordinate. Ask students to name a matrix row's node and a column's edge before calculating. Write one row product in full before abbreviating Df.

If learners think zero total divergence means a cycle, use (3,−1,−1,−1): the sum is zero but every entry is not. If they think four entries means dimension four, use the square's fourth-column dependence and solve s=t=u=0. If they memorize E−V+1, require the leaf argument and the own-chord coefficient argument on the 3×2 rectangle. A large matrix is unnecessary.

If a cycle sign is wrong, trace its return path from head to tail and compare each step with the stored arrow. If the ninth detail is missing, sum the first eight and restore its negative; then perform the inverse. If students keep only W, compare concentrated and evenly distributed wrap lists sharing W=9: (0,…,0,9) and (1,…,1). They have the same winding and different details. If they erase a tree remainder, compare the two square flows in Lesson 06 diagnostic 2 and reconstruct both explicitly.

At the end of Lesson 03, run a cumulative check: draw the square, build D, multiply a flow, identify a chord and decode a circulation. At the end of Lesson 05, require the reproducible Lucas tree, 28-cycle proof and complete wrap inverse. Terms must retain the meanings in the glossary. Progress after students can explain their corrections, not only after seeing the answer.

## Evidence and notation discipline

Use “source reports” for archive statements and “we derive” for the classroom count proof. The verification script checks finite examples; it does not certify all archived claims. S03 AUD-002 is a recorded serialization/DAG gap, not a computational counterexample to the graph counts. Mathematical backbone M08 is not interchangeable with compiler M08. The exceptional-action branch is recognition-only context; no group theory is assessed.

All numerical flow examples are synthetic and dimensionless. Incidence D is reserved for the graph table; B remains reserved for the source's physical basis and is not reused. No Cell3 metric, physical unit, parity convention, CMB vector or geometric constant is needed for this finite graph course. Those series invariants remain in input-contract.json and are neither altered nor used as unstated premises. The chosen tree complement is not called an orthogonal gradient component. If an application attaches units, all flow entries and their remainders must retain those same units.

“Memory” denotes specified retained information and a decoder in this course. Ask what state, basis, order, signs, remainder and update rule are known. A real-valued dimension does not equal a number of digital bits; precision and allowed values would also need specification. No observed memory lifetime is claimed.

## Assessment and recovery

The capstone contains a full 100-point key. Use its subpart rubric; require repair of any missing reconstruction data or unsupported dynamics inference. Accept a correctly transformed convention with its conversion back to the requested ordering. Have students explain one tree-leaf elimination and one chord restriction argument aloud as a check against copying.

For course maintenance, manifest.json records checkpoint dependencies and hashes. Verify a checkpoint hash before trusting its status. Repair the earliest affected lesson, rerun its numerical checks and dependent capstone links, rebuild the verbatim assembly, refresh hashes and run the deterministic project validator. The independent verification script is a supplement, not a student prerequisite. Keep source files read-only and do not create source snapshots.
