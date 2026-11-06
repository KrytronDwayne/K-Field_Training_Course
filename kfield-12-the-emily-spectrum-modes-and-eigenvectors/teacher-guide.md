# Teacher guide · The Emily Spectrum: Modes and Eigenvectors

The course ends with a finite accomplishment: students can derive the seven-entry Emily eigenvalue ledger, account for all 27 modes, reconstruct a small state, and test an operator identification. Use exact radicals throughout. Calculators may check decimals but must not replace the equality √2·√2=2.

## Pacing and prerequisite checks

Each row below is one 55-minute period: 5 minutes of retrieval, 20 minutes of explanation and worked example, 15 minutes of guided practice, and 15 minutes of independent diagnostics and repair. This totals 11 core periods. Use the two capstone periods for 5 minutes of setup, 45 minutes of work and 5 minutes of review each; collect the complete answer packet after the second period. No new mathematics is introduced during the capstone.

| Period | Lesson | Explanation/worked focus (20 min) | Guided practice (15 min) | Check/repair focus (15 min) |
|---|---|---|---|---|
| 1 | 01 | Neighbor sums and row multiplication | C12.01-P1, both vectors and carrier labels | Four C12.01-D1 checks |
| 2 | 02 | Common multiplier, zero and negative eigenvalues; square roots | C12.02-P1 and constant candidate | Four C12.02-D1 checks |
| 3 | 03a | Component derivation, zero/nonzero cases | Re-derive both cases and verify rows | D1 questions 1–2 |
| 4 | 03b | Dot product, norm and unit modes | C12.03-P1 normalization and dots | D1 questions 3–4 |
| 5 | 04a | Triple ordering, product graph and additive action | Two-factor and zero-sum products | D1 questions 1,3 |
| 6 | 04b | Center check and product norm | C12.04-P1 corner calculation | D1 questions 2,4 |
| 7 | 05a | Two-choice counting and all 27 labels | C12.05-P1 multiplicity 1 and sum | D1 question 1 plus ledger replay |
| 8 | 05b | Sheet labels, χ, reflection and function parity | C12.05-P1 splits and counts | D1 questions 2–4 |
| 9 | 06a | Coefficient readback and exact reconstruction | C12.06-P1 mode contributions and residual | D1 question 1 |
| 10 | 06b | Mean/detail, parity, degree and quotient guard | C12.06-P1 mean and degree table | D1 questions 2–4 |
| 11 | 07 | Two-route test and inverse map | C12.07-P1 failed identity and reflection | Four C12.07-D1 checks |

At entry ask students to calculate 2+(−3), 1/2+1/2, and solve 2a=8. Supply signed-arithmetic repair if needed. Review node versus edge by drawing the three-node path. The course supplies all other necessary bridges; do not assume prior matrix multiplication or a spectral theorem.

## Teaching and repair moves

Have students point to each input address as they multiply a matrix row. If a sign disappears, preserve the student's original work and mark the precise changed entry. To repair division-by-zero reasoning, return to the product equation Av=λv instead of ratios. If students confuse eigenvalue zero with vector zero, use (2,0,−2) and physically mark its two nonzero inputs.

At the end of Unit 1 (lesson 03), require a row-by-row eigenpair check, exact norm, and one mutual dot product before proceeding. If a student rounds √2, redo the calculation symbolically. At the end of Unit 2 (lesson 05), require the full multiplicity sum and a spoken distinction between a node, a mode and a function parity coordinate. At the end of Unit 3 (lesson 07), require full reconstruction plus a successful and failed map test. These are cumulative dependency gates, not extra topics.

The 14-even/13-odd distinction is easy to reverse because χ has 13 positive and 14 negative nodes. Draw one fixed center and 13 pairs. Ask what a function may independently assign on each pair. Then compare that to assigning a sign label to every address. Use u− as the decisive example: it has negative eigenvalue but is even under inversion.

Mean subtraction is not eigenmode deletion. Ask for A_L **1** at a corner and the center. The unequal results 3 and 6 settle the claimed invariant-line question. Keep the mean as an explicit coordinate; otherwise centered data alone cannot recover the input. In incomplete mode models, keep the full residual vector, with signs and ordering. No residual deletion or scalar replacement is permitted.

## Assessment and scope

The capstone contains full answers and a 100-point rubric. Award calculation credit for an explicit correct intermediate result even if a later arithmetic slip occurs. For a conceptual error, use the rubric's named operation to identify the earliest prerequisite needing repair. Do not award the type-distinction points for count agreement alone. Do not assess M17 pseudoinverse formulas, rank algorithms, general spectral theorems, compiler module identities or physical dynamics.

All numerical state examples are clearly synthetic, dimensionless classroom data. The graph definitions and source ledger are source facts; the row computations, exact enumeration, parity count and reconstruction are fresh finite derivations. Proposed physical mechanisms are outside the core, not silently inferred. [sources.md](sources.md) records exact archival pointers and the global-DAG limitation. The graph search returned integration labels but failed bounded object retrieval; no fresh formal-authority claim is based on those labels.

## Verification and recovery

[verify.py](verify.py) runs with the specified tf_gpu_env and uses standard-library rational pairs for exact a+b√2 arithmetic. It independently enumerates nodes, builds neighbor actions, checks all 27 eigenvectors and their pairwise dot products, checks reconstruction, parity and degree counts, and row-reduces the source M17 matrix using exact fractions. Its rank result is teacher context only. [verification.json](verification.json) preserves compact exact outputs and source digests without copying source data.

The manager stores each checkpoint's relative path, SHA-256 and dependency in manifest.json. On recovery verify hashes before trusting a status. Passed work is only revised for a concrete defect; refresh assembly and all dependent hashes after any revision. Run the project validator only after audit and final hashing. Its machine checks establish containment, assembly identity and consistent recovery records; the independent teaching audit supplies separate educational review.
