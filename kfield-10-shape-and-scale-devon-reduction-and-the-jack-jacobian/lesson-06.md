# Lesson 6 — Limits and reconstruction tests

Essential question: What must a reversible change report retain and check?

Goals: distinguish inverse residual from approximation remainder; reconstruct areas from retained coordinates; audit domain, units and provenance.

Bridge: Lessons 1–5 supplied every operation. We now combine them without introducing a new model. Keep unrelated synthetic examples in separately labeled records; do not imply that a branch pair, a square model and an area triple were measured together.

## C10.06-E1 — Two different checks

An inverse residual is recovered input minus supplied input for a declared map. For the Jack coefficient map it is J^-1(Jx)-x, an ordered triple. Algebra makes it exactly zero in the domain. An approximation remainder is exact finite output change minus tangent prediction. In the product model it is 2t²; the square model has t². A zero inverse residual does not force either remainder to vanish. Preserve signs, coordinates and the starting value in both records.

Use this report procedure. First name the record, input order, units, references and source pointer. Next state the domain: positive areas, fixed angles when needed, an admissible integer branch pair, and whether a map is exact or tangent. Calculate transformed coordinates. Preserve the common scale, geometry and all residual information. Finally reconstruct the input and compare component by component. If a residual is nonzero, locate the missing term, approximation or transcription error. A single magnitude or score cannot replace its signed entries.

For log areas, both y=m1+z and y=s e_s+u e_u+v e_v must agree. Then A_i=A0 exp(y_i) restores dimensional areas. If changing the reference, retain the new A0. If changing angles, retain those changes and do not apply J as if they vanished. A scalar baseline or finite response law cannot be recovered from a tangent table alone.

## C10.06-W1 — Worked report audit

Record PRODUCT is the classroom function (1+t)(1+2t) at dimensionless t=0.1. It starts at 1, ends at 1.32, and has change 0.32=0.30+0.02. Save the positive remainder 0.02.

Record JACK uses S02#/backbone_sequence/6, with the M19 gravity_scalar_lift branch named. The synthetic tangent input (1,2,3)t gives (2,-1,4)t and returns to (1,2,3)t. Its inverse residual is (0,0,0). This says nothing about the product's finite remainder.

Record AREAS has A0=1 LU², m=5L/3, z=(-5,1,4)L/3. Addition recovers (0,2,3)L. Exponentiation gives (1,4,8) LU², so the reconstruction residual against those supplied areas is (0,0,0) LU². Keep the original area order, reference and any geometry record; the reduced shape alone could not have restored them.

## C10.06-P1 — Practice

Prepare separate SQUARE, JACK, AREAS and GEOMETRY/BRANCH records using prior practice data: t=0.1 in (1+t)²; Jack input (2,-1,1)t; area logs (1,2,4)L with A0=1 LU²; diagonal basis (2,2,2) LU and branch (4,2). Include inverse and approximation checks. Add the independent anchor record (9,18,18) LU² with perpendicular angles. Explain why the area triples in the different records need not coincide.

Answer: SQUARE gives baseline 1, output 1.21, change 0.21=0.20+0.01. JACK gives (-1,3,33)t and inverse (2,-1,1)t, zero inverse residual. AREAS gives m=7L/3, z=(-4,-1,5)L/3, reconstructing (1,2,4)L and (2,4,16) LU². GEOMETRY gives M_cell=4I LU², cofactors=16I LU⁴, R_cell=I/4 LU^-2; the product is I. BRANCH gives (C_b,C_c)=(3,1), returning to (4,2). ANCHOR yields eta=2000, alpha_inverse=100, t=3 LU and lengths (3,3,6) LU, restoring (9,18,18) LU². These are explicitly separate classroom records; merging them as one box would introduce contradictory geometry.

> Claim scope: Fresh checks verify the displayed finite algebra. S03#/findings/1 reports wider serialization/DAG incompleteness including M07; this course does not certify its global repair. The verified arithmetic, the archived formula statement and an unestablished physical mechanism remain different evidence layers. No empirical datasets are supplied or claimed here.

## Diagnostic checks — C10.06-D1

1. Is the square remainder 0.01 evidence that the Jack inverse failed?
2. What information is lost if a report keeps only u,v?
3. If included angles vary, can zero residual under the old J certify the geometry?
4. What must accompany a dimensional area reconstruction?

Worked answers: (1) No; they concern different maps and checks. (2) Common scale and absolute area reconstruction are lost unless m or s and A0 are retained. (3) No; omitted angle-change terms lie outside that map's stated input domain. (4) Positive A0 with units, the ordered log coordinates or their complete reversible decomposition, and the declared operation/reference history; geometry additionally needs its own basis or angle record.

Next: [Capstone](capstone.md) constructs a reversible report using these same operations. Pacing: 55 minutes = 5 retrieval + 20 worked synthesis + 15 practice + 15 checks/repair.
