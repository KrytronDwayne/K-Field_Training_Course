# Teacher guide

This short course supports an independent 15-period sequence including capstone. Supply paper for two simultaneous ledgers: the signed digits/detail components and the visible coarse or rendered result. Calculators are optional; fractions are preferred so endpoint equality and tail thresholds can be checked exactly. This is a mathematical source-reading course; it does not ask students to manufacture experimental evidence.

Before lesson 01 ask learners to compute −6 mod27 by adding 27, 3⁴, and (2+6)/2. Answers are 21,81,4. A learner who cannot explain these should receive an arithmetic bridge before advancing. The lesson explicitly teaches residues, so the first question is a readiness conversation rather than a presumed prerequisite test.

|Lesson and periods|Teaching focus|What to inspect before advancing|Repair when needed|
|---|---|---|---|
|01: 1|Signed prefixes and reduction|All four practice reductions plus failed proposal retained|Compute signed sums before residues; label each modulus|
|02: 1|Two meanings of distance|Learner names which distance is being used|Repeated division by3; compare with number-line subtraction|
|03: 2|Complete rule, then triples|General compatibility argument and 27 extensions|Separate finite table from “for every j” rule|
|04: 3|Finite subtraction proof; matrix bound; endpoint histories|Minimal tolerance depth, units, distinct histories|List consecutive powers; use a row sum by hand; retain signed tail|
|05: 1|Cylinder and pullback|Same output does not collapse input ledger|Use 7,16,25 as a counterexample table|
|06: 2|Means, matrices; projector/reconstruction checks|All three disjoint sectors saved; P₀P₁=P₀|Reconstruct entrywise before discussing infinite notation|
|07: 2|Block convergence; domains and source cards|Distinguishes x∈ℓ² from x∈Dom(D)|Compare input-square and weighted-square columns|
|Capstone: 3|Input/source ledger; calculation; independent repair|All seven operation IDs and retained information|Return to the mapped practice, not new untaught methods|

Use the 5/20/15/15-minute structure in each core period. Across 12 periods this is retrieval 60, teaching 240, practice 180, checks/repair 180 minutes. Diagnostic answers appear in each lesson so teachers can cover them during independent work, then uncover them for repair. A correct number without its depth, units or rule is incomplete when those labels change its meaning.

Unit A cumulative check: ask for the four levels of the all-negative rule and the distinction between depth 4 and an infinite sequence. Unit B: ask why the two endpoint histories share an image but are address-distance 1, and why the physical depth differs from the normalized depth for the synthetic B. Unit C: reconstruct the four-entry vector, then explain why this finite identity does not settle a missing infinite operator domain. These checks consume already scheduled diagnostic time.

Keep lesson 06's names precise: P₀,P₁ are nested averages, whereas P₀,Q₀,Q₁ are the three disjoint sectors. Their mixed-product claims differ. The optional product source bridge derives every term using explicit block-averaging properties; no product rule is inferred from Q=I−E alone. It is a recognition and finite-verification bridge, not an assessment of an unloaded infinite algebra.

Lesson 07 permits an elementary proof of convergence through block bounds. Do not require the exact value of Σ1/n², calculus, complex inner products or an adjoint calculation. Self-adjointness is a source-scope word only. No student must supply a missing archival operator: “not supplied” with an exact checklist is the correct report.

Capstone periods: first 55 minutes establish input ledger/source card and complete tasks 01–03; second 55 minutes handle rendering, observations and details (04–06); third 55 minutes finish domain/source classification (07), independently recompute and repair. The 28-point rubric in capstone.md gives four points per operation. A corrected record keeps the original proposal and labels the correction rather than overwriting evidence.

Accessibility: allow spoken explanations alongside exact arithmetic, use a color per coordinate while retaining written coordinate labels, and provide large tables for digits/moduli. More time is preferable to dropping a detail sector. Extension learners may prove a matrix identity by multiplication; every core result is already accessible through averaging rules.

Recovery for authors: manifest.json is the checkpoint authority; verify each file hash before trusting passed status. The deterministic validator checks integrity and assembly, while audit_report.json and independent-audit.json record content checks. Rebuild only defects and their dependents. Re-run verify_examples.py after mathematical edits, update assembly/hashes using finalize_course.py, and run the project validator command recorded in completion_report.json.
