# Teacher guide

This is a complete topical course for high-school seniors: six lessons over seven core periods, then two capstone periods, each 55 minutes. It teaches finite geometry and address operations. The goal is a learner who can state the type of every count, test a history, and recover every retained detail.

## Entry check and taught bridges

Ask learners to locate 5/8 on a number line, evaluate 3^2 and 2^3, and solve 3q+1=−2. Answers are between 1/2 and 3/4, 9 and 8, and q=−1. If these need repair, use fraction strips and repeated multiplication before beginning. No calculus or university algebra is assumed. Course05 context is useful but the operative window/cell definitions are restated in lesson01. Lesson03 explains toy base area and height, avoiding an untaught determinant algorithm.

## Teaching sequence

| Lesson/period | Explanation and worked examples | Answered practice | Diagnostics/feedback | Transition |
|---|---|---|---|---|
| 01 | 20: E1/W1 and E2/W2 | 15: P1,P2 | 15: D1–D4 | 5 |
| 02 | 20: remainders, product counts, rung | 15: P1,P2 | 15: D1–D4 | 5 |
| 03A | 20: scaling and corner derivation | 15: P1 | 15: D1,D3 | 5 |
| 03B | 20: half-step grid and reachability | 15: P2 | 15: D2,D4 | 5 |
| 04 | 20: balanced place values and algorithm | 15: P1 and −2 example | 15: D1–D4 | 5 |
| 05 | 20: parent map and history table | 15: P1 and incompatible parent | 15: D1–D4 | 5 |
| 06 | 20: coarse plus retained detail | 15: P1 and alternative children | 15: D1–D4 | 5 |

For capstone period 1 allocate 5 minutes setup, 40 for steps01–04, 10 for checking. Period 2 allocates 40 for steps05–09 and 15 for reconstruction demonstrations and feedback. Use capstone.md's point rubric. A correct scalar with missing depth/type/order is incomplete when the task asks for a reconstructible record.

## Teaching moves and repair routes

Have learners draw boundaries before writing formulas. Two adjoining intervals visibly share a corner, explaining why incidences differ from distinct vertices. In lesson02 physically separate cards labeled 'geometric cells' from cards labeled 'residue classes.' Equality of counts should prompt a type question, not identification.

For negative modular examples insist on a=mq+r with 0≤r<m. If a learner says −2 mod 3 is −2, preserve that integer as a valid representative but request the standard representative 1. For balanced ternary, annotate every place value before summing. An encoding must finish with zero remaining quotient to represent the requested integer exactly at that depth.

If a learner drops the low digit in lesson05, compare both outputs modulo 9. The counterexample (−1,0,1) makes the distinction concrete: high-digit removal produces −1, while low-digit removal and shifting produces 3. For lesson06 hide a detail card and ask for two possible children; then restore the card and reconstruct. Include a zero card so 'nothing changed' does not become 'nothing stored.'

## Cumulative checks and assessment use

After lesson03, require a labeled four-count comparison for 9B:729 volumes,1000 ordinary corners,6859 half-step points,55 sheets. Also require a verbal statement of what stays fixed in the dyadic experiment. Repair in lesson03 before advancing if a student conflates grids.

After lesson06, ask for a history that is incompatible, a correction, and a reversible record. Use capstone backward links in course-map.md to locate the earliest teaching source for an error. Give targeted feedback on the operation, preserving the student's original answer alongside the correction rather than deleting its informational trace.

## Evidence and boundaries

S02 M03 is an archival mathematical source. sources.md and source-provenance.json provide exact paths, hashes and pointers. Fresh verification covers finite arithmetic and file identity, not a new replay of the whole corpus proof system. Keep source-reported statuses separate from classroom derivations. Toy basis numbers are arbitrary length units, not measured Cell3 constants. The course intentionally does not infer forces or experimental effects from counting, nor identify mathematical-backbone M03 with an integration compiler label.

Infinite inverse limits are recognition-only; do not add them to assessment. Preserve all source branches in provenance and all removed bits/digits in finite records. No package installation, raw data copy or external publication is needed to teach or replay this course.

## Reproducible verification

Run verify_examples.py with the explicitly selected tf_gpu_env Python runtime. It enumerates finite grids, all three-digit balanced words, parent relations and lossless round trips. verification.json stores compact results only. The project adapter validator checks recovery hashes, dependencies, assembly identity and audit state; it does not replace a teacher's content review. Independent teaching/source review is recorded separately.
