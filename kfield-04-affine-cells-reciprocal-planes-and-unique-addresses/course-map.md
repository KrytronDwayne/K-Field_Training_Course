# Course map — Affine Cells, Reciprocal Planes, and Unique Addresses

Audience: high-school seniors. Entry capabilities are signed arithmetic, exact fractions, coordinate triples and solving linear equations, plus course-03 capabilities. Lesson 1 rebuilds column multiplication and inverse action; lesson 2 teaches floor; lesson 3 teaches dot products and transpose; lesson 4 teaches magnitude, normalization and projection; lesson 5 rebuilds the Gram form. No unprovided course-03 notation is needed to solve the assessments.

Six core lessons of 55 minutes, two capstone periods. This is a topical course, not a semester syllabus. All numerical hand calculations use the declared synthetic B and O. The source-reading exercise retains the locked Cell3 branch separately. Markdown is the delivery format; no PDF/Word rendering is required.

## Dependency order and coverage

| Concept | Introduction and explanation | Worked example | Answered practice | Diagnostic | Later use |
|---|---|---|---|---|---|
| C04.01 Address and point | lesson-01 C04.01-E1 | C04.01-W1 | C04.01-P1 | C04.01-D1 | lesson-02, CAP-01 |
| C04.02 Unique half-open owner | lesson-02 C04.02-E1 | C04.02-W1 | C04.02-P1 | C04.02-D1 | lesson-03, CAP-02 |
| C04.03 Reciprocal plane counter | lesson-03 C04.03-E1 | C04.03-W1 | C04.03-P1 | C04.03-D1 | lesson-04, CAP-03 |
| C04.03 Canonical source branch | lesson-03 C04.03-E2 | C04.03-W2 | C04.03-P2 | C04.03-D2 | lesson-04, CAP-07 |
| C04.04 Normal and spacing | lesson-04 C04.04-E1 | C04.04-W1 | C04.04-P1 | C04.04-D1 | lesson-05, CAP-04 |
| C04.05 Physical metric angles | lesson-05 C04.05-E1 | C04.05-W1 | C04.05-P1 and P2 | C04.05-D1 | lesson-06, CAP-05 |
| C04.06 Reconstruction | lesson-06 C04.06-E1 | C04.06-W1 | C04.06-P1 and P2 | C04.06-D1 | CAP-06 |

The course has three audit units: lessons 1–2 (address and ownership), lessons 3–4 (readers and rulers), lessons 5–6 (geometry and recovery). Each lesson consumes the previous lesson's capability. The capstone consumes all six. There is no cycle and no computation introduced for the first time in the capstone.

## E05 capstone operations: inputs, outputs and prior teaching

All abbreviated CAP IDs below have prefix C04-. The required item IDs are written in the lesson text and carry actual worked solutions.

| Step | Named inputs → required outputs | Prior explanation | Prior answered practice | Check |
|---|---|---|---|---|
| C04-CAP-01 | B,O and A/B/C exact q → x, x-O, recovered q, typed columns | C04.01-E1 component map/inverse | C04.01-P1 both directions | C04.01-D1 origin |
| C04-CAP-02 | A/B/C exact q → z,u, endpoint inclusion explanations | C04.02-E1 floor inequality and partition | C04.02-P1 negative and near-half cases | C04.02-D1 near vs exact |
| C04-CAP-03 | Four nonzero h, B and A → g, three pairings, affine levels and integer membership | C04.03-E1 dot pairings/transpose | C04.03-P1 reciprocal reader and level | C04.03-D1 mixed label/origin |
| C04-CAP-04 | Four g plus doubled first h → magnitudes, n, d_h and inserted-plane explanation | C04.04-E1 normalization and projection derivation | C04.04-P1 two normals and level-step checks | C04.04-D1 doubled label |
| C04-CAP-05 | e1,e2 and (1,1,0) → address/physical dot comparison, cosine and two squared lengths | C04.05-E1 Gram distribution and cosine | C04.05-P1 dot comparison, zero cosines and signed cross-term length; C04.05-P2 nonzero cosine | C04.05-D1 positive cross terms |
| C04-CAP-06 | z,u,q_disp and full q → reconstructed x,r, restored q, exact differences and owner comparisons | C04.06-E1 typed ledger and exact inequalities | C04.06-P1 reconstruction; C04.06-P2 display restoration before ownership | C04.06-D1 wrong display owner |
| C04-CAP-07 | Canonical card plus mixed u card → source-exact rows, units/order, pointer/hash and branch rejection | C04.03-E2 source pointer and lexemes | C04.03-P2 active/superseded comparison | C04.03-D2 repair mixed card |

## Course boundaries and recorded choices

The approved six-lesson sequence is preserved. Lesson 3 reallocates its 55 minutes to 20 minutes explanation/work, 20 minutes practice (10 pairing plus 10 source reading), 10 minutes diagnostics and 5 transition. It uses a supplied card; no locked-decimal inversion or live source search is assigned to students. Lesson 6 adds C04.06-P2 so display restoration is practiced before assessment. The teacher guide permits an extra source-reading period if actual classroom load requires it; the six-lesson artifact sequence does not change.

SA-04 applies to lessons 1,3,4: retain the affine origin in g_h dot (x-O_K)=m, use g_h=B^-T h for nonzero h when normal/spacing is requested, and select canonical S02 result fields over stale reciprocal_witness. Canonical source values are not replaced with the synthetic analogue. Source review status is distinct from fresh finite-example verification.

All broader series invariants remain in input-contract.json. Their advanced operations are outside this course's kernel, so they are not silently used as premises or assessed calculations. In particular no gauge-carrier, parity, recursion, phase-energy, CMB-dynamics or compiler-authority assertion is inferred from this affine atlas. M_cell and R_cell stay distinct from phase/effective metrics and separately typed distance quantities.

## Deliverables

Read [course.md](course.md) for the verbatim lesson sequence; use [terminology.md](terminology.md), [teacher-guide.md](teacher-guide.md), [capstone.md](capstone.md), [sources.md](sources.md) and [canonical-card.md](canonical-card.md) alongside it. Recovery and verification live in manifest.json, audit_report.json, completion_report.json and verification.json. The original input contract is retained intact. Verification scripts act only on these course artifacts and read supplied sources in place.
