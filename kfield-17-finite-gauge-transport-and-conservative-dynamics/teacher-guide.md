# Teacher guide — Finite Gauge Transport and Conservative Dynamics

This topical course for seniors takes thirteen 55-minute core periods and three capstone periods (880 minutes total). Its prerequisites are signed arithmetic, fractions, powers, linear equations and coordinate graphs. Courses 07 and 14 supply context, but every complex-number, matrix, metric and certificate-reading operation needed for assessment is rebuilt here. The course does not require calculus, abstract algebra, university linear algebra or quantum mechanics.

## Sequence and pacing

| Lesson | Periods | What to teach in each period | Required exit capability |
|---|---:|---|---|
| 01 | 1 | Complex pairs, row action, adjoint and inverse | Transport and recover with direction declared |
| 02 | 1 | Transported subtraction and frame cancellation | Verify d′=G_xd with complete components |
| 03 | 2 | A: row-column multiplication and path; B: conjugation and noncommutation | Multiply ZX and XZ and explain order |
| 04 | 1 | Trace, action and retained curvature coordinate | Invariant action with full loop retained |
| 05 | 2 | A: conjugate division and step; B: adjoint proof and counterexample | Check Cayley hypotheses and invert step |
| 06 | 3 | A: weighted lengths; B: area pairs and Hodge blocks; C: normalization and branch comparison | Compute both blocks with units and J convention |
| 07 | 2 | A: source card and units; B: replay gaps and toy minimum | Distinguish reading from numerical replay |
| 08 | 1 | N, Q_L, normalized expectation and scope | Keep state remainder alongside invariants |

Each period reserves 5 minutes retrieval, 20 teaching/worked example, 15 practice, and 15 diagnostic checks and repair. For multi-period lessons distribute the listed practice subparts across periods; use the first diagnostics as interim checks and all four as the final exit review. These are planning allocations, not measured classroom timing. If a class cannot independently multiply complex pairs in lesson 01, add a bridge period before lesson 02 and record the pacing change; do not remove content to preserve a calendar.

## Teach with visible representations

Start by writing a+bi as a point (a,b). Draw i as a quarter-turn, then use distributive multiplication to verify the drawing. Use index cards labeled input y and output x for each link. When multiplying a loop, physically place the rightmost link first in travel order. Keep a separate state column next to each map; students often otherwise confuse a frame's label with a number.

Before the Cayley proof, ask students to conjugate a diagonal entry and then transpose an off-diagonal table. Before lesson 06, give the two-dimensional ruler interpretation; do not begin with wedge notation. For area factors, draw a rectangle whose two sides are scaled, so the area gains the product of the side factors. J is a supplied coordinate pairing, not an empirical discovery.

The source cards are exercises in precise reading. S02's mathematical-backbone M13 is not a compiler integration label. Teach the difference between verifying bytes, deriving an identity, and replaying a certificate. The historical formula remains in the course precisely so students can see why a normalization claim changes when its exponent changes.

## Checks and repair routes

| Observed difficulty | Return to | Repair |
|---|---|---|
| Writes U_xy as x→y | 01-W1/P1 | Annotate input/output before multiplying |
| Keeps U fixed during frame change | 02-W1 | Write the three stages G_y⁻¹, U, G_x |
| Assumes matrices commute | 03-P1 | Apply XZ and ZX to (1,0) |
| Treats trace as full state | 04-W1 | Compare off-diagonal entries of F and F′ |
| Omits a Cayley hypothesis | 05-D1 | Recompute the non-self-adjoint scalar counterexample |
| Squares entries for wedge² | 06-E1/P1 | Multiply factors in each named coordinate pair |
| Uses historical exponents | 06-D1 | Test determinant and physical units at δ=64 |
| Converts a bound into equality | 07-W1 | Read strict and non-strict signs aloud |
| Calls 8 the normalized expectation | 08-P1 | Divide Q_L=8 by N=6 |

Local diagnostic answers are supplied after the questions. For independent work, ask students to cover them until they have recorded both a result and its method. The capstone answer key includes component-wise and source-scope criteria, so it can be graded without inventing external inputs. Maintain zero unresolved conceptual errors in direction, hypotheses, units and evidence class before declaring mastery, even if the point score is otherwise high.

## Evidence and information preservation

There are no empirical datasets in this course. The examples are declared synthetic finite models; source facts are what exact archival bytes report. The finite algebra is independently recomputed. No inferred mechanism is needed to solve the tasks. Reference mathematics supplies definitions of complex arithmetic, matrix action and finite unitarity. Optional infinite-domain and continuum claims remain separate. A claim labeled VERIFIED_NOT_LOADED is neither silently certified nor silently rejected.

Keep every component and comparison remainder. A squared norm, trace or normalized block is a useful summary but cannot replace the full state, loop or metric scale. Store the original reference and the remainder with the reconstruction equation; no outlier deletion or loss of weak components is involved. The course uses compact synthetic records rather than copied source datasets.

## Unit and final reviews

After lesson 04 review the shared convention U_xy:y→x and verify the loop/action chain. After lesson 06 review all three different scales: action coefficient β, Cayley time τ_C, and metric lengths; none is silently equated with source τ_R. After lesson 08 use the capstone backward map to confirm that every required operation has an earlier worked explanation and answered practice. The thermal series is recognition-only and adds no assessed convergence operation.

Read sources.md for exact source paths, hashes and gaps. Read worked-example-verification.json for the executable arithmetic checks, and audit_report.json plus independent-lesson-audit.json for actual findings. The deterministic validator checks containment, file hashes, dependency order, assembly identity and audit consistency; it is not a substitute for a human or independent-agent teaching review.
