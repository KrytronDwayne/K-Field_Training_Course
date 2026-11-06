# Teacher guide — Affine Cells, Reciprocal Planes, and Unique Addresses

Teach this as six 55-minute core lessons followed by two capstone periods. The audience is high-school seniors who can handle signed fractions, coordinate triples and simple linear equations. Course-03 is the series prerequisite, but all matrix actions required here are rebuilt from component arithmetic. No calculus, general matrix inversion, abstract algebra or quantum mechanics is assessed.

Start with an entry check: ask students to solve 2t=-1 and -3s=9/2, add (1,0,3)+(2,-1,4), and locate -3/2 on a number line. Answers are t=-1/2, s=-3/2, (3,-1,7), and halfway between -2 and -1. If these capabilities are missing, rehearse signed multiplication and common denominators before lesson 1; do not hide the gap under matrix notation.

## Pacing and instructional moves

| Lesson | Explanation/work | Practice | Checks/feedback | Transition | Teaching focus |
|---|---:|---:|---:|---:|---|
| 1 | 20 | 15 | 15 | 5 | Scale columns physically; undo component equations |
| 2 | 20 | 15 | 15 | 5 | Draw included left/excluded right endpoints; negatives matter |
| 3 | 20 | 20 | 10 | 5 | Ten minutes pairing practice; ten minutes supplied source-card reading |
| 4 | 20 | 15 | 15 | 5 | Check one-spacing motion by dotting it with g |
| 5 | 20 | 15 | 15 | 5 | Expand all step pairings before naming the Gram form |
| 6 | 20 | 15 | 15 | 5 | Keep q,z,u,q_disp,r in distinct ledger columns |

Lesson 3 is the highest-density lesson: issue the canonical card before class and use its already printed values, not an online retrieval task. The normal's numerical computation is deferred to lesson 4; in lesson 3 it is only an identified source field. If the dot-product bridge takes more than its allocation, use a second instructional period for source reading rather than deleting the source check. This changes pacing, not prerequisite order. All listed times are planning assumptions, not measured classroom outcomes.

In capstone period 1, spend 10 minutes reading the task and unit contract, 25 on conversions/ownership, 15 on reciprocal pairings and 5 reviewing unfinished rows. In period 2, spend 15 minutes on normals/angles, 15 on reconstruction/residuals, 15 on source cards and 10 on peer checking with the answer key. Keep the key separate from initial independent work if using the capstone as an assessment.

## Formative checks and repairs

- An omitted O often produces internally tidy but displaced answers. Return to lesson 1's x=O test before practicing more inverses.
- Floor is not truncation toward zero. Use lesson 2's -7/5 example and the inequality defining floor.
- A reciprocal vector is defined by three pairings, not its visual resemblance to a direct step. Have students write all three pairings.
- Unit normals have magnitude 1, while reciprocal readers have inverse-length units. Ask which vector measures an address and which only gives direction.
- Scaling one plane equation and scaling a family label are different. Have students list q1=0,1/2,1 for h=(2,0,0).
- Two off-diagonal Gram terms produce the cross term. Let students check (1,1,0) and (1,-1,0) so both signs appear.
- A displayed boundary can change ownership. Insist on restoring q_disp+r before applying floor, retaining even zero components.
- A tiny numerical difference can identify a different source branch. The active branch comes from the source correction contract, not the size of the difference.

## Unit-boundary and acceptance checks

After lessons 1–2, ask students to convert a point and explain why z alone cannot reconstruct it. After lessons 3–4, have them pair one g with all columns and demonstrate a normal step with level increment one. After lessons 5–6, require both direct and Gram length calculations plus exact recovery of a rounded display. These are cumulative checks, not additional prerequisites.

Use the capstone's 100-point rubric to identify specific repairs. A student completes this course when every required operation is demonstrated and boundary/origin/source/residual errors are corrected. A high total does not substitute for an unperformed operation. Full answers for every lesson practice and diagnostic are in that lesson; full capstone answers and source card are provided.

## Evidence and source handling

The synthetic analogue is declared throughout and uses LU; locked Cell3 cards use nm and ICRS component order. S02 `/backbone_sequence/1` supplies M02 definitions; S03 `/findings/4` corrects the stale witness branch. All supplied source file hashes were checked. See sources.md for exact paths, pointers and scope. Source-reported closure status is not a new whole-corpus proof in this course. No new experimental mechanism or empirical data is taught. The negative determinant is intentional and is not “fixed” by swapping columns.

Use M_cell only for the Gram metric and R_cell for its inverse. Advanced metrics and other series quantities are reserved names, not extra assessment content. Infinite inverse limits, complex phase exponentials and abstract quotient proofs remain recognition-only outside this topical course. Keep observations, derivations, source facts, interpretations and unresolved questions separate when discussing extensions.

Markdown is the requested delivery format; no paginated artifact is required. Read course.md for the verbatim lesson sequence and use its linked supporting files. Verification scripts are teacher/reviewer aids; students do not need Python.
