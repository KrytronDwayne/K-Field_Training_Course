# Teacher guide

Audience: high-school seniors comfortable with signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs. No calculus, abstract algebra or prior university linear algebra is assumed. The earlier course references are contextual; local finite bridges teach every assessed operation.

## Session plan

### lesson-01 — Measurements as linear channels

- Session 1: Channel equations and consistency.
- Session 2: Normal equations and complete residual reconstruction.

### lesson-02 — Rank and retained syndromes

- Session 1: Field rank and residual complement.
- Session 2: Integer lattice counterexample and saturation requirement.

### lesson-03 — The thirteen-channel decoder

- Session 1: Source A and Gram rank.
- Session 2: Thirteen-channel reconstruction and integer witness.
- Session 3: C21.S01 character table and intertwiner distinction.

### lesson-04 — Reconstruction and dimensional meaning

- Session 1: Channel reconstruction and units.
- Session 2: Mass renderer inputs and retained syndrome.

### lesson-05 — Atomic and isotope inventories

- Session 1: Composition/isotope/charge inventory.
- Session 2: C21.S02 moves and unresolved fibers.
- Session 3: C21-RXN balanced endpoint bridge.

### lesson-06 — Binding and periodic organization

- Session 1: R029–R032 source application trace.
- Session 2: C21.S03 energy, rate and power inputs.

### lesson-07 — Solver convergence and unresolved information

- Session 1: Convergent update with complete trace.
- Session 2: Divergent parameter branch and reconstruction.

### lesson-08 — A reproducible decoding report

- Session 1: Source/derived/synthetic report assembly.

Each period uses 5 minutes for prerequisite retrieval, 20 for explanation and a worked example, 15 for guided practice, and 15 for independent diagnostics and repair. Allow an additional period if learners cannot reconstruct the previous packet; retain all eight conceptual lessons and record the extension in the class pacing log. The approved baseline is 17 core periods plus 3 capstone periods.

## Teaching moves and readiness checks

In lesson 1, have students write the three equations before using the matrix symbol. Check fraction subtraction individually. Ask pairs to reconstruct all three channels, then explain why a scalar residual score is insufficient. In lesson 2, draw a horizontal line and mark integer points; highlight that the even lattice misses odd points. Do not assume students know vector spaces from the word alone.

Lesson 3 is the highest-load block. Session 1 begins with e1 column selection, then two column dot products, then the explicit six-equation decoding recipe. Split the thirteen ledger rows across pairs and require each pair to return both predicted and residual entries. The provided exact ledger is a checking aid, not a memorization target. Session 2 handles integer extraction and saturation using the six explicit recipes. Session 3 teaches the four-label table (two bits per label), one orthogonality check and the concrete swap intertwiner. General S3 representation theory is recognition-only; students are assessed on the small table and explicit action products.

At the lesson-04 boundary, ask whether a mass scalar can reconstruct a changed syndrome. If students say yes, use identical c with two distinct s packets. Keep source b and toy b on separate cards. A missing a_e does not authorize a guessed value. No physical occupied-state coefficient selection is assessed.

Lesson 5 introduces chemistry vocabulary before applying moves. Check each endpoint for nonnegative counts separately from the weighted-sum test. Have students physically cross off matching synthetic A and B labels on each side of the reaction. Charge and whole-object mass state must be stated before subtraction. If neutral and ionic conventions are mixed, preserve the attempted ledger and mark what additional objects/states are needed.

Lesson 6 uses source cards as a reading exercise. A blank field means not supplied, not zero. Students need not construct a phase tensor or compute a graph spectrum: these are requested source coordinates whose absence must be tracked. They must distinguish mechanism synthesis from checked nominal arithmetic. Keep the synthetic reaction labels separate from the CHNO composition row.

Lesson 7 compares step parameters using exact fractions. Each iteration row includes all three residual entries and both normal sums. A divergent branch is valid saved information about the algorithm and parameter. Lesson 8 asks partners to recreate a result from the report alone. Demand separate rounding closure, channel syndrome and source retrieval gaps.

## Common errors and targeted repair

| Observed error | Repair task |
| --- | --- |
| Three channels means three coefficients | Rebuild y=(c1,c2,c1+c2), count free inputs, then derive residual t. |
| Zero normal residual means no residual | Substitute (-1/3,-1/3,1/3) into both dot products and reconstruct y. |
| Rank proves integer equality | Show (1,0) missing from integer multiples of (2,0). |
| L_int is the source L | Compare shapes and products: 6 by 13/identity versus 7 by 13/zero. |
| Equal rank proves physical identity | Ask for an explicit typed map and the actions it preserves. |
| Nominal V is exact mass or isomer identity | Compare two different nonnegative formulas with V=68 and list unresolved isotope/structure fields. |
| Positive Q gives power | Request duration and recoverable fraction, then compute units. |
| Failed solver values should be removed | Reconstruct y from the divergent second iterate and full residual. |

## Assessment and recovery

Use the answered diagnostics after each session sequence. At unit boundaries (02,04,06,08), recompute one previous example without its answer and check terminology and source layers. An incorrect response is retained alongside its correction. Do not grade a missing definition as student failure; reteach the earliest dependency. Capstone operations all have earlier named explanations, worked examples and answered practices in course-map.md. The answer key and 44-point rubric are in capstone.md.

## Reproducibility and authority

Run verify_examples.py with the explicitly selected tf_gpu_env; it reads sources and writes only compact verification.json in this course directory. The validator adapter path is supplied in the production contract. No package installation, physical-data copying or source mutation is needed. Markdown tables and fenced matrices are the delivery format; no paginated artifact is requested. Source paths, hashes and scope are in sources.md. Formal-looking archival statuses remain attributed when replay objects are absent.
