# Independent hostile audit — course 27

Audit scope: draft lessons 01–07, capstone, input-contract teaching anchors and sources ledger, read on 2026-11-05. This review applies the residual-information-paradigm. No lesson was modified. This is a content audit, not a claim that final assembly or deterministic validation has passed.

## Findings requiring correction

### IA27-01 — Major — E05 prior-practice coverage is coarser than the actual capstone operations

Locations: capstone C27-CAP-02, C27-CAP-03 and C27-CAP-05; lessons C27.02-P1, C27.03-P1 and C27.05-P1; capstone backward map.

The capstone asks students to derive the physical ruler matrix, compute every entry of the forward pullback, and prove the general finite-route lower bound. Those operations are explained and worked, but their named prior practice does not independently ask and answer those operations: 02-P1 computes rates/counts/cost from the already supplied rulers, 03-P1 reuses W and checks reverse congruence, and 05-P1 computes an example excess and changed constraints. The backward map therefore overstates independent answered practice for these suboperations. This is an E05 assessment-alignment issue, not a mathematical error.

Required repair: append small independently attempted and explicitly answered practice substeps to 02-P1 (construct A and compute A^T H A), 03-P1 (recompute all entries of B^T G B/4), and 05-P1 (show the weighted-deviation sum is zero, expand the mixed terms, and conclude the lower bound and attainment under the finite domain). Keep existing practice. Point the capstone map to those exact substeps. The teacher guide can allocate the existing practice sessions to them. No new advanced prerequisite is needed.

### IA27-02 — Minor — the authored ellipse is a coordinate table rather than a plotted worked figure

Location: C27.01-W1. The input teaching anchor explicitly says to plot the anchors when producing the lesson. The lesson derives the ellipse correctly and gives all eight anchors, then instructs the student to plot them; it contains no plotted worked figure. Add a small authored diagram with equal axes and semiaxis labels (or record an explicit pedagogical disposition that the table plus independently produced student plot is the intended representation). This does not invalidate the arithmetic or student plotting instructions.

## Independent check evidence

- Read all seven lessons and all seven capstone tasks and rubric rows. Each lesson has an essential question, three observable goals, an explicit bridge, instruction, worked example, answered practice, four answered diagnostic checks, evidence scope and next dependency. Sequence teaches vector/matrix operations before dependent finite calculations; continuum material is expressly recognition-only.
- Recomputed with exact Fraction arithmetic through the required tf_gpu_env: q(1,2)=14, q(1,-1)=2, q(1,1)=6, q(2,-1)=6; W=[[2,1/2],[1/2,1/2]]; T_B^T W T_B=[[2,1],[1,2]]; route totals 4 and 8; 1/3-3333/10000=1/30000; bound gap=1/5. Command exited zero. Conda printed an unrelated missing OpenCL temp-file message before successful results; no package changes occurred.
- Independently checked the ellipse by substitution: the diagonal short endpoints have q=6(1/6)=1; diagonal long endpoints have q=2(1/2)=1; axis crossings have q=2(1/2)=1. The rotated expression 3s²+t² gives semiaxes 1/sqrt(3) and 1 in L units.
- Hand-checked all ledger endpoints, reversed ordering and half-duration subdivision. Rates are tau^-2, increments tau^-1, and costs reconstruct consistently. The changed T=4tau case gives 2/tau and is correctly separated from the original problem.
- Checked the finite decomposition: duration-weighted deviations vanish by endpoint closure, mixed terms cancel by symmetry, and positive G makes the remaining sum nonnegative. The obstacle caveat correctly preserves only the bound, not the original attaining path. The continuum statement explicitly states additional admissibility and integral conditions.
- Hand-checked the recognition-only linear-velocity example: v_x=2t/tau in L/tau gives integral of 8t²/tau^4 over [0,tau], namely 8/(3tau), whereas constant mean gives 2/tau.
- Recomputed S01–S04 SHA-256 from original files; all four match the input packet. Read original S02 typed_conventions, branch_proofs/12, proof_nodes/32/formula and proof_nodes/41/formula, and S03 findings/7 and findings/8. Their formulas, residual string and source/replay distinction agree with the course cards. AUD-009 is a broader missing-body disposition; the course does not present it as a numerical route proof.
- Read the actual quadratic-phase-cost skill: its integral convention has no factor 1/2 and m²/s units. The course explicitly separates that convention from its L^-2 classroom metric and tau^-1 accumulated cost.
- Checked residual retention: signed velocities and durations remain reconstructible; scalar equality is not treated as vector equality; the full source residual string is preserved; the synthetic 1/30000 precision rule is not imposed on it; the frozen response prediction retains +1D and -1D diagnostic residuals.
- Application T20/T35/TS retrieval is documented by the author with hashes/ranges. This independent pass did not rerun connector retrieval, so that evidence is checked against the course's supplied source packet and ledger, not independently re-attested here. No locked numeric source route replay is asserted or required by the approved source-scoped assessment.

## Status at handoff

Unresolved findings in reviewed drafts: critical 0, major 1, minor 1. No arithmetic, unit or source-promotion defect found in the checked examples. The route certificate and source precision bridge remain disclosed source gaps, not a fabricated replay.

At this read, course-map.md and terminology.md still contain Pending authoring; teacher-guide.md, final course.md and verification.json are not yet present. Their absence is expected ongoing production, not assessed as a finished-course failure. Final assembly identity, final recovery hashes, completed support artifacts and actual validator success remain outside this draft audit and must be checked before completion. Recheck IA27-01 after the additions and inspect those late artifacts.

## Repair recheck and final content disposition — 2026-11-05

This section supersedes the draft handoff counts above while retaining the original findings as history.

- **IA27-01: resolved.** Read the added P1a in Lessons 2, 3 and 5 and independently checked the displayed steps. The ruler matrix has entries (1,0,0,1/4)L^-2; the forward congruence includes all four entries and the factor 1/4; the finite proof correctly expands the weighted sum and establishes the lower bound and conditional attainment. The capstone backward-map rows 02, 03 and 05 now explicitly identify these P1a tasks. The teacher guide allocates each second session's practice block to the added operation. This supplies independently answered practice before assessment.
- **IA27-02: resolved.** Opened and visually inspected ellipse.png with the image viewer. It shows the correct tilted ellipse on equal-scale x/L and y/L axes, the eight taught anchors, the long semiaxis L and short semiaxis L/sqrt(3), with readable labels. The plotted diagonal endpoints agree with the already checked exact coordinates. The authored worked visualization now exists.
- Read completed course-map.md, terminology.md and teacher-guide.md in full. The seven-lesson sequence, 13 core periods, three capstone periods and 880-minute total agree. The map points to actual E1/W1/P1/D1 content; detailed capstone mapping identifies the new substeps. The glossary distinguishes source metrics, classroom units, matrix order, cost and detector response; locally reused symbols are scoped. The teacher guide supplies prerequisite recovery, cumulative checks, exact finite task boundaries, item-level scoring and retention of original student work alongside repairs. No new critical, major or minor content finding arose.
- Inspected verification.json: it records 74 passed arithmetic, anchor, lesson-contract and source-hash checks under the required executable. This records the author's successful check run; the independent exact arithmetic and original-source hashes above were separately recomputed in this audit. It is not a substitute for final structural validation.

**Final unresolved content findings: critical 0; major 0; minor 0.** Independent teaching/source/math content acceptance is complete within the scope stated above. The disclosed missing locked route matrices/certificate/precision bridge remain source retrieval gaps with an explicitly taught missing-field audit; no numerical source replay is claimed. Final assembled-course identity, final recovery hashes and actual deterministic validator result remain the author's separate completion checks and are not reported as passed by this content audit.
