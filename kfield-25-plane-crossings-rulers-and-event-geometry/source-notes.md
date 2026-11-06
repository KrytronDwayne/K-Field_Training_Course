# Source notes and evidence boundaries

This course is an authored synthetic geometry course grounded in a supplied source contract. It neither reproduces source datasets nor claims a fresh proof replay. Exact paths/digests and bounded-read witnesses are in sources.json. The source data remain at their original locations.

## What was actually read

- **S01:** Corrected complete proof JSON, `/root_contract` including `/coordinate_lock` and `/epistemic_types`. The file's SHA-256 was independently checked against the runtime packet. This supplies column order, origin, handedness, half-open ownership and typed evidence distinctions; it is not a fresh proof check.
- **S02:** Mature complete proof JSON, `/mature_locked_cell3` and `/typed_conventions`. Digest verified. The locked geometry has intentional negative determinant and separately named direct/reciprocal metrics. Its numerical cell entries were inspected but are not copied into synthetic exercises or mixed with older branches.
- **S03:** Audit correction instruction JSON, `/authority_contract`. Digest verified. Its unavailable-body and frozen-gate statuses remain source-reported; absence of a body is a retrieval limitation, not proof failure. The latest mature locked values retain precedence.
- **S04:** Mature corpus audit JSON, `/audit_contract`. Digest verified. It explicitly separates source acceptance from self-reported PASS and distinguishes superseded provenance from active residual coordinates.
- **T10:** `applications/kfield_lucas_lab/rag_corpus/10_geometry_trajectory.md`, bytes [0,545), whole file. It names optical wavelength, oscillator period and matter crystal spacing; distinguishes directional crossing rate from magnitude-based physical beat frequency; reports physical Earth/CMB speed 369812.50200040644 m/s in ICRS. These are the source facts used in Lessons 2 and 4. No propagation or detector transfer law is inferred from the short source.
- **T45:** `applications/kfield_lucas_lab/rag_corpus/45_moving_reference_frames.md`, bytes [0,2651), whole file; also located as RAG lines 1–45 with the same digest. It describes the typed frame path, independently scaled visual chambers, a source-reported 97-state sidereal replay and deliberately absent Solar/Galactic short-window dynamics. These boundaries support Lessons 2 and 6.

T45 also reports a finite source-bound non-alignment result for its four displayed candidates relative to a camera vector. This is more specific than the installed skill's older blanket `not_established` summary. It remains a source-reported finite result in this course: no compiler was run, and it is not a universal claim about all physical axes. The course teaches no alignment inference from display appearance.

## Retrieval scope and gaps

Capabilities were queried once. They returned a read-only interface but no corpus-generation field. Subsequent RAG and graph responses returned the paired generation/manifest `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7`, matching the packet. Source retrieval used rerank:false. The first prefix search found no chunks; a later unprefixed exact contract-name search found T45. Root and construct graph traversals were explicitly truncated, so they are discovery witnesses, not exhaustive coverage certificates. The display node ID with qkf prefix did not resolve for the follow-up; the source-original `construct:trajectory-rulers` did, retaining its `uses_authority` link.

T45 names `contracts/kfield_reference_frame_loom_v1.json`, `contracts/kfield_sidereal_replay_v1.json`, and Agda modules. The bounded source/graph/search routes used here did not expose those underlying bodies as pinned artifacts. Consequently the course does not claim to replay the frame engine or certify its numeric output. T10's short description likewise is not a full detector or ruler-transfer implementation. This retrieval limitation does not leave a core computation missing: the approved course scope explicitly supplies complete synthetic plane, path, clock and interpolation contracts. Every assessed operation uses those local inputs.

## Claim-to-content map

| Content | Evidence class | Basis and limit |
|---|---|---|
| Oriented plane coordinate and projected rate | Mathematical derivation from declared inputs | Lessons 1–2; exact synthetic fractions |
| Period, phase and piecewise accumulation | Mathematical derivation | Lesson 3, constant/nonconstant distinctions explicit |
| Three ruler categories and signed/magnitude distinction | Pinned source facts | T10 whole-file pointer; physical transfer not supplied |
| Display scales and absent short-window dynamics | Pinned source report | T45 whole-file pointer; underlying replay not independently executed |
| Root existence and linear interpolation | Mathematical reference definitions/derivations | Lesson 5; hypotheses stated locally |
| Meridian/hour-angle equations | Declared reference coordinate convention | Lesson 6; fictional objects, no real ephemeris claim |
| All numeric event tables and residual samples | Synthetic examples and derived outputs | Local cards and exact arithmetic verification |
| Potential detector mechanism | Unresolved input, not asserted | Needs response/transfer inputs absent here |

## Applicability of the complete invariant packet

The complete invariants remain in input-contract.json without alteration. Active guards are oriented normals, fixed/moving origins, dimensioned spacings, signed rates, separate polarity, exact clocks, residual reconstruction, source-branch separation and no raw-data copying. Cell3 source guards remain columns [a b c], intentional negative determinant, half-open cells, x−O_K in affine identities and distinct M_cell/R_cell/G_phase.

Gauge-carrier order, parity/lift/recursion distinctions, detail-product hypotheses, M19/M20 dependency corrections, compiler authority labels and admitted global-form families are not used as premises in this course. Neither matrices nor gauge modules are required student operations. They remain source-local rather than being silently equated with our family names, sheet indices or polarity tags. No nearest-integer rounding occurs, so no undeclared tie rule is introduced. Cell3 and galaxy-derived geometries are not blended. No physical energy or force is computed; the fourteen-row spectral bundle is not sampled or reinterpreted. Thus its signed rows and three independent plane-cost levels are left intact by immutable reference rather than repackaged as six synthetic ledger rows.

## Reproduction

The course-local `independent-audit-check.py` recomputes exact rational examples and checks actual teaching IDs. `manage_course.py` maintains hashes, source metadata, assembly and completion. The independent reviewer also reread the teaching and assessment prose. The project-root validator checks containment, checkpoints, dependency order, hashes, audit counts and exact lesson assembly; it does not substitute for the content audit.
