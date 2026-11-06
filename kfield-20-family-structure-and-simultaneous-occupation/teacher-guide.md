# Teacher guide

Teach the actual finite reasoning and ask students to point to the premise behind each count. Course placement follows courses 15 and 18; all operations needed for this course are nevertheless introduced in its lessons. Entry check: compute −5+8, 2/3 divided by 5/3, solve 3u+2=8 and locate a coordinate triple. Answers: 3, 2/5, u=2, and an ordered three-coordinate address. Repair fraction division and signed arithmetic before the core course; do not hide them inside a trace calculation.

## Pacing and classroom use

| Lesson | 55-minute periods | Session emphasis and readiness check |
|---|---:|---|
| 1 | 1 | Enumerate residues and all classes; student explains nine choices per class |
| 2 | 2 | Mean/detail first; norm and independent coordinates second; reconstruct all entries |
| 3 | 4 | A matrices/lift; B complex arithmetic/Fourier; C shift/phase and trace; D full Weyl practice; retain all nine coordinates |
| 4 | 2 | Column equations/projector; product basis/dimension versus rank |
| 5 | 2 | Typed source-factor table; history alternatives and orthogonality conditions |
| 6 | 1 | Claim/guard/correction card; explain missing selection dependency without erasing the source claim |
| 7 | 3 | Numerical scope; Schur substitution/reconstruction; singular cases and repair |
| Capstone | 3 | Parts 1–3; parts 4–6; parts 7–9 and checking |

Within each core period allow about 5 minutes retrieval, 20 explanation/worked example, 15 guided practice and 15 independent diagnosis/repair. The written lessons include full answers so learners can check after attempting. Reveal answer sections after the attempt or use a separate viewing window; the supplied Markdown is deliberately a complete reference. Use the extra sessions for students to derive each displayed table themselves. These are planned durations, not measured classroom completion times. Slow a session when a readiness check fails; do not remove Weyl or Schur practice to recover time.

Allocated minutes by lesson make the teaching/practice/check commitments explicit:

| Lesson | Retrieval | Teaching/worked examples | Guided practice | Independent checks/repair | Total |
|---|---:|---:|---:|---:|---:|
| 1 | 5 | 20 | 15 | 15 | 55 |
| 2 | 10 | 40 | 30 | 30 | 110 |
| 3 | 20 | 80 | 60 | 60 | 220 |
| 4 | 10 | 40 | 30 | 30 | 110 |
| 5 | 10 | 40 | 30 | 30 | 110 |
| 6 | 5 | 20 | 15 | 15 | 55 |
| 7 | 15 | 60 | 45 | 45 | 165 |

## Targeted teaching and repair

In lesson 1 a negative remainder error is repaired by writing n=3q+r with 0≤r<3. Keep the table's pair order. In lesson 2 distinguish mean m from normalized coefficient 3m; ask learners to reconstruct a specific entry. Averages without detail and detail without means are incomplete representations.

In lesson 3 explicitly read row-by-column multiplication aloud. Demonstrate conjugation with i before ω. Have students verify ω², ω³ and 1+ω+ω², then compute one Fourier inverse coordinate at a time. Trace is a sum of three diagonal entries, not a determinant. For Weyl extraction use the entrywise formula to see why six coefficients vanish; listing only nonzero coefficients does not complete the required table. D/P order is part of the basis convention. The 243 lift output slots carry only 27 independently chosen input coordinates.

In lesson 4 require the equations α/2=0 and β=0 to justify independence; counting visible columns is not enough. The two-by-three label table precedes the projector count. In lesson 5 the restriction to one family has rank 16, while its history factor has rank one. Ask a student to say which one they mean each time. Rank-one projectors at different histories need an additional orthogonality condition. The finite q₃=0 example is deliberately declared as a teaching branch, not a recovered source definition.

In lesson 6 retain the five source records together. Accept neither automatic promotion of a source label into a fresh proof nor automatic downgrade because the proof body is not loaded. The documented AUD-007 conflict is the reason to distinguish mathematical construction from physical-carrier identification. This is not a general consensus disclaimer. The course does not assess belief in a mechanism.

In lesson 7 have students substitute the computed u,w into both original equations. E≠0 and S≠0 are separate tests. E=0 does not imply det K=0. For S=0 keep either the free variable with its reconstruction rule or the incompatible equations. Every original coordinate and residual stays available.

## Assessment alignment

The exact explanation, example, answered-practice and diagnostic IDs for all nine capstone parts are in course-map.md. Capstone parts 7 and 9 intentionally share a scalar system: part 7 assesses scope and a checked state, part 9 assesses derivation, reconstruction and branch handling. This overlap supports synthesis rather than introducing an untaught task. Part 8 uses the already practiced Weyl matrix. Full answers and a 100-point rubric are in capstone.md.

Use diagnostic answers to choose repairs, not to delete a student's discrepant result. Keep initial attempt, correction and the reason. Suggested mastery is 80 points plus successful scope/reconstruction repairs, as described in the rubric. Extensions such as a general matrix-block Schur proof, physical Yukawa derivation or source certificate replay are recognition-only and earn no required core points.

## Recovery and evidence use

Use manifest.json as the checkpoint index and verify hashes before resuming. Source-provenance.json records exact archival paths, hashes, pointers and retrieval boundaries. Verification is replayable using verify_examples.py under tf_gpu_env; verification.json records the checks. The independent review and audit report describe actual checks and repairs. The final course assembles passed lessons verbatim; supporting guides and capstone remain separately accessible. No PDF/Word or rendered artifact was requested, so Markdown is the delivered format.
