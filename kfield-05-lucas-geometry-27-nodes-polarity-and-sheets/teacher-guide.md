# Teacher guide

Teach the complete course in eight 55-minute periods: six core lessons and two capstone periods. Students need signed arithmetic, fractions, coordinate triples and one-step linear equations. Start Lesson 1 by asking students to distinguish (1,0,0) from (0,1,0); start Lesson 2 by having them halve a negative number. These are readiness checks, not exclusion gates. If a student needs support, model one coordinate at a time and let the student explain the second.

The core lesson budget is 20 minutes of explanation and worked example, 15 of guided practice, 15 of diagnostics with feedback, and 5 for connecting to the next lesson. Lesson 4 divides explanation evenly between parity and remainders, with 7 and 8 minutes of respective practice. These timings are estimates; the authored core uses finite hand calculations. Do not add inverse-transpose derivation, complex exponentials or infinite recursion to the assessed core.

|Lesson|Teaching emphasis|Likely error and repair|Exit evidence|
|---|---|---|---|
|1|Nested lists and product count|Adding three menu lengths: draw one 3×3 block, then make three blocks|Explain distinctness and 1+6+12+8|
|2|Column steps, origin, half-address and ownership|Using BL or omitting O: check the center; confusing window with ownership: compare ±1/2|Map, invert and assign owner in D1/D3/D5|
|3|Enumerate sums before interpreting planes|Dropping center or O: list λ=0; evaluate both dot products in E2|Seven totals and affine check|
|4|Two distinct integer groupings|Negative remainder or negative λ treated as negative χ: solve λ=3k+r₃ and λ=2k separately|Explain 9/9/9 versus 13/14|
|5|Pair plus orientation reconstruction|χ used as s: compare two antipodes; center counted twice: solve L=−L|Reconstruct sv and count 13+1 classes|
|6|Independent checks and retained residuals|Totals mistaken for complete validation: change p without changing λ|Compute a nonzero R_L in P2 and preserve it|

At the end of Lesson 2, check that students can move both ways between L and p and explain z+u. At the end of Lesson 4, ask a student to give two nodes sharing χ and two sheet numbers sharing r₃ but differing in χ. At the end of Lesson 6, ask for one error that a count check misses and one error that an inverse check misses. These cumulative checks cover notation stability, prerequisite closure and capstone readiness. Repair the earliest misconception and repeat the affected check.

Capstone period 1: 5 minutes interpreting inputs, 15 for enumeration and q, 25 for p and z/u, 10 for peer comparison by address. Period 2: 15 minutes for λ/χ/r₃, 10 for v/s, 20 for inverse/pair/count checks, 10 for the information-preservation explanation and rubric feedback. Provide a blank 27-row table or allow students to construct it. A pair of students may divide arithmetic, but each student must independently reconstruct one row, explain one boundary case and show why s cannot be replaced by χ. The supplied full registry is the complete key; retain an independent attempt before distributing it.

All lesson practices and diagnostics have worked answers in their own files. The capstone rubric totals 100 points and avoids double-penalizing propagated arithmetic. A high numerical score does not waive repair of an omitted origin, discarded row, or missing direction sign. Additional practice can reuse the same procedure with another row from the 27-row window; no untaught operation is necessary.

Evidence language: call source statements source definitions or source-reported statuses; call the finite counts derived results; call the chosen numerical geometry a classroom analogue. No experimental observations are introduced. A proposed physical mechanism would be a new layer requiring its own premises, so it is not an assessed conclusion here. Preserve all discrepancies and correction histories. The source's broad mature-core status is not a fresh verification result from this course.

Recovery and maintenance: manifest.json is the authority after its hashes have been checked. Lesson text is assembled verbatim in course.md. Do not edit course.md independently; repair a source lesson, rebuild assembly, recompute affected checks, then refresh hashes. build_course.py contains the initial authored draft; do not rerun it over audited lesson repairs. finish_course.py rebuilds supports and the synthetic registry. verify_examples.py independently checks that registry. finalize_course.py refreshes assembly, audit and manifest only after review. The installed deterministic validator is run using the parent-approved project-root adapter. No rendered document is requested; Markdown tables and links are the delivery format.
