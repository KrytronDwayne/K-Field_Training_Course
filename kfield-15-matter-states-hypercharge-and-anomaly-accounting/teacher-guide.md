# Teacher guide — Matter States, Hypercharge, and Anomaly Accounting

This topical course takes fourteen core 55-minute periods and three capstone periods. It is designed for seniors who can handle signed arithmetic, fractions, powers and a linear equation. Course 14 is the series entry prerequisite, but Lesson 1 restates the carrier/order and later lessons teach every operation assessed here. No calculus, quantum mechanics, general Lie theory or abstract linear algebra is assumed. Students may use a basic calculator; code is an optional verification aid, never an assessment prerequisite.

## Sequence and pacing

|Lesson|Periods|First session focus|Further session focus|
|---|---:|---|---|
|1|2|Signed sorting; zero from repetition|Subset counts and combinations|
|2|2|Bidegrees and multiplicities|Explicit degree-four list; block signs|
|3|2|Additive charges and normalization|Remainders and descent; component ledger|
|4|3|Linear and cubic sums|Mixed/pure-color indices; general polynomials and failed trials|
|5|2|Factorization; completing the square|Integer line; primitive sign; determinant contract|
|6|2|Oriented complements|Diagonal action; dual label; doublet count|
|7|1|Report construction and evidence scope|Integrated practice and repair|

Every core period allocates 5 retrieval, 20 explanation/worked example, 15 practice, 15 independent checks and repair. Total core allocations are 70 retrieval, 280 teaching/example, 210 practice and 210 check/repair minutes: 770 minutes. Capstone adds 165, total 935 minutes. Lesson files retain their original seven stable IDs but have explicit session boundaries; dense lessons are not compressed into one period. If learners need more time, extend a session while retaining the dependencies and all practice.

Before Lesson 1, ask students to calculate −2×3, (−2)³, 5×4/2, and solve 3a=−2b when b=3. Answers are −6,−8,10,−2. A missing skill needs a short arithmetic bridge before proceeding. Ask what counts as an independent label: students need not explain the physical origin of C3 or W2. Those are declared inputs.

## Instruction and correction cues

Use five labeled cards to make subsets. Turning a pair around should move a separate sign token; it must not create another basis direction. Keep an empty-selection card distinct from a zero-expression card. In Lesson 2 require an enumeration by all r values rather than a memorized sum. If students omit a degree-four state, recover it by naming the omitted label.

In Lesson 3 separate three columns: charge per component, component multiplicity, and contribution to a named sum. If a student cubes a row total, ask them to list three identical component charges and cube each before adding. Remainders are nonnegative representatives: r=3 gives t=0; s=2 gives p=0. Hypercharge Y is not electric charge in coulombs.

In Lesson 4 teach the index weights as supplied reference-theory rules. T already accounts for the active representation: only spectator copies multiply it. Require every zero row in the first ledger so an omission cannot masquerade as cancellation. A dual color has the same quadratic index and opposite cubic-color sign. Preserve trial ledgers even when their sums fail; this is essential evidence about the condition being solved. Label their inputs synthetic, not experimental.

In Lesson 5 have students multiply the proposed factors before discussing why the factorization matters. Completing the square uses only expansion and the nonnegativity of real squares. The determinant bridge is limited to a diagonal product/top-form exponent and its declared preservation for every phase parameter. Ask separately whether a pair lies on the line, whether it is primitive, and whether it follows the sign convention.

In Lesson 6 distinguish the omitted subset from its orientation coefficient. The dual action example teaches i²=−1 and inverses before using them. Students do not need a general unitary-matrix theory. Count doublet copies as 3+1, not eight components or two named sectors. Never identify exterior degree with Lorentz chirality or detector/carry parity.

## Assessment and mastery gates

Each P1 has a full answer; have students cover it, work independently, then compare. Each lesson has four diagnostics and worked answers. A successful exit requires the central operation to be correct and its scope to be named. Diagnose the earliest missing prerequisite and repeat the affected operation with its original input. Do not silently normalize an incorrect trial to make it pass.

At the end of Lesson 3, check that all sixteen states occur exactly once, six multiplicities sum correctly, and per-component charges/descent are correct. At the end of Lesson 5, require all five named tests, both retained failing trials, factorization, integer primitive solution, and convention. At the end of Lesson 7, check that the report preserves all source/integration distinctions. These unit checks correspond to enumeration/charge, constraint solving, and interpretation.

The capstone gives explicit input/output operations, prior teaching/practice IDs, a complete answer key and a 100-point rubric. Method credit is appropriate for a traceable arithmetic slip, but material sign/index/source-scope errors must be repaired before marking the construction verified. The teacher may hand out the student task separately from its key without altering either.

## Evidence and delivery notes

The course's primary source is mathematical-backbone M11 in S02; other packet sources are hash-checked provenance context, not silently blended numerical branches. Sources.md records exact paths, hashes, JSON pointers and retrieval classes. The source theorem status and accepted compiler/integration authority remain separate. General quotient-bundle topology and upstream proof closure are recognition-only boundaries, not hidden computation tasks.

All deliverables are Markdown or compact JSON/Python. Markdown is the approved format, so no paginated rendering is required. Course.md contains the seven lessons verbatim in order; teach from either that assembly or the individual files. The manifest and completion report carry hashes. Re-run verify_examples.py using the required tf_gpu_env, then the project-root validator command in completion_report.json. Never treat a validator's structural success as a substitute for the independent content audit.
