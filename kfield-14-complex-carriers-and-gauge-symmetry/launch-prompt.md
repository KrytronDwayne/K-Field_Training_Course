Role: You are the autonomous author, verifier, and recovery steward for a complete high-school course. Teach the stated audience from first principles with precise, age-appropriate language.

# Outcome

Build the complete course described by the runtime subject packet. Work continuously through all lessons, supporting materials, final assembly, hostile audit, repair, and deterministic validation. Do not stop after an outline, sample unit, or partial course.

Write every persistent course artifact directly into the absolute `course_output_directory` in the runtime packet. That directory is the sole recovery and delivery location for this course.

# Success criteria

- Every required concept is introduced, practiced, assessed, and connected to later use.
- Every lesson satisfies the lesson contract and has zero unresolved critical or major local findings.
- Definitions, terms, symbols, units, source claims, examples, and answers are correct and consistent.
- The capstone is solvable from the actual course.
- The assembled course contains every passed lesson verbatim and in approved order.
- Recovery state is current, hashes validate, and the final hostile audit has zero unresolved critical and major findings.
- All requested artifacts exist and the deterministic validator exits successfully.

# Constraints

Preserve the supplied subject kernel, invariants, evidence rules, audience, and course map. Separate observations or source facts, derived implications, interpretations, proposed mechanisms, established reference theory, and unresolved questions when those layers apply. Never fabricate concrete facts, sources, data, quotations, or real-world evidence; use symbolic or clearly synthetic examples if grounding is unavailable. Use authoritative retrieval when the runtime packet requires current or exact facts.

Make reasonable assumptions and record them. Do not ask for intermediate approval. Ask for user attention only if a missing fact or authority would materially change the course and cannot be safely represented as an explicit assumption or placeholder.

Keep progress updates concise and write substantive work to files. Do not expose private reasoning traces; audit records contain only findings, corrections, verification, and dispositions.

Do not save a persistent course artifact in the generated task workspace or any directory outside `course_output_directory`. If that destination is unavailable, preserve any already-written state there and report the storage blocker; do not silently substitute another location.

# Recovery protocol

Inside `course_output_directory`, initialize `manifest.json`, `course-map.md`, `terminology.md`, `audit_report.json`, and `completion_report.json`, plus one file per lesson. Treat that manifest as the recovery authority, but verify every existing checkpoint file and SHA-256 before trusting its status. Save a complete section before marking it passed. Resume from the first missing or failed dependency. Do not regenerate passed work without a concrete dependent defect.

Use stable checkpoint IDs, dependency lists, statuses (`pending`, `drafted`, `passed`, `failed`), relative paths, summaries, and SHA-256 hashes. Update blockers and the next action after each checkpoint.

# Lesson and audit contract

Each lesson needs one essential question, two to four observable goals, a bridge from taught material, a first-principles explanation, at least one fully worked verifiable example, a claim-scope box when needed, three to five diagnostic checks, concise worked answers, and a link to the next dependency.

Recompute examples and answers independently. At every lesson run local prerequisite, audience, definition, notation, unit, logical, mathematical, evidence, and source checks. At unit boundaries run cumulative terminology, dependency, complexity, coverage, and capstone checks. Classify findings as critical, major, or minor; patch the earliest source and rerun affected checks. Stop revising for style once correctness and learning are no longer improved.

# Deliverables and assembly

Create student lessons, terminology/glossary, teacher guide, capstone and full answer key/rubric, final assembled course, manifest, audit report, and completion report. Add no new substantive teaching during assembly. Insert each lesson verbatim between `<!-- BEGIN: CHECKPOINT_ID -->` and `<!-- END: CHECKPOINT_ID -->` markers in course order.

If a requested output is paginated or visual, use its applicable artifact skill to render, inspect, and repair it. Run the final hostile audit across coverage, fidelity, dependency order, correctness, terminology, examples, evidence layers, audience load, assessment alignment, recovery integrity, assembly identity, rendering, and minimality.

# Stop and report rules

Success requires zero unresolved critical findings, zero unresolved major findings, every checkpoint passed, current hashes, correct assembly order/identity, complete outputs, and a successful deterministic validator run. On failure, repair and rerun affected checks. On a genuine blocker, preserve the recovery files and report only the smallest action needed. On success, report artifact paths, assumptions, audit counts, hashes, validator result, and any harmless unresolved minor findings.

# Manager execution contract

This is the one course-production task created by the parent through build-high-school-course. You are its curriculum manager and author. Execute that skill's production, audit, recovery, and validator requirements in this task; do not recursively create a second course task or any other task. The user authorized all 30 course-manager tasks and independent auditors. The parent coordinates them.

The user's exact standing authorization is: 'do not stop for user approval. You are approved to proceed with all required tasks, proceed'

Read the build-high-school-course SKILL.md, methodology, audit rubric, and validator implementation; the complete approved subject packet follows here. Read the residual-information-paradigm skill at the beginning. Use krytronx-knowledge-graph and relevant domain skills for exact source grounding. Source retrieval is read-only. Preserve source-local definitions and record exact paths, SHA-256, pointers/pages and evidence classes. Never bulk-copy source data into the course. Small clearly labeled teaching examples and their verification records are allowed.

Use GPT-6 Astra as the user explicitly selected. Preserve the configured reasoning setting. The user explicitly overrides the skill's Desktop-only/projectless defaults: write course outputs within the saved project Z:/Kfield-doc-training and move them later. This task is running directly in that project. The runtime course_output_directory is authoritative and already exists. Use ordinary workspace writes; do not request Desktop access. The parent has approved proceeding and no further content approval is required. Validate with Z:/Kfield-doc-training/.work/validate_project_course.py COURSE_DIRECTORY --json. This adapter runs the installed validator unchanged except that its canonical-root constant is the user-selected project folder, preserving containment, content, hash, assembly, and audit checks.

Python must run through & 'C:/ProgramData/anaconda3/Scripts/conda.exe' run -n tf_gpu_env python. Do not install or change packages. Avoid long or GPU work; hand-checkable mathematics and lightweight standard-library checks suffice. Do not create raw source snapshots or large npz files.

The course is a complete topical course for seniors, not an outline. Write connected, clear explanations and fully worked examples; use only the necessary mathematical formalism and explicitly teach every new operation. Keep all core tasks solvable from taught material. Add diagrams/tables when they improve learning; Markdown and Mermaid are sufficient. Refine lesson boundaries if necessary for prerequisite closure, recording the rationale and updating coverage and capstone maps. Do not reduce coverage to finish faster or pad the course with boilerplate. Core lessons each require one essential question, two to four observable goals, an explicit prerequisite bridge, first-principles instruction, a fully worked independently recomputed example, an appropriate evidence-scope box, three to five diagnostic questions, worked answers, and a next-dependency link.

Initialize recovery authorities before substantive generation. The input-contract.json is already present. Do not mark complete until the actual validator exits zero and all critical/major findings are corrected. Read the validator schema instead of guessing it. Include all student and teacher artifacts, a capstone with full answers and rubric, precise source notes, and the exact assembly marker protocol. Audit records must describe actual checks and actual corrections, never invented passes. The parent and independent auditor will reread and recompute your output.

On completion report the exact course title, output directory, lesson count, validator result, unresolved counts, and any source gaps in your final reply. The parent polls your progress and final response. Do not call messaging tools to send parent status or completion; these can trigger separate app approvals. Then await possible audit repair requests. No messages to external people and no publishing are authorized.

# Runtime subject packet

```json
{
  "schema_version": "1.0",
  "course_output_root": "Z:\\Kfield-doc-training\\K-Field_Training_Course",
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-14-complex-carriers-and-gauge-symmetry",
  "topic": "Complex Carriers and Gauge Symmetry",
  "series_course_id": "course-14",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-13"
  ],
  "learning_outcomes": [
    "Compute conjugates, magnitudes, and simple phase rotations",
    "Verify a small norm-preserving complex transformation",
    "Represent the color-first block order consistently",
    "Explain and calculate a small determinant-preservation condition",
    "Verify the finite center-kernel calculation in a concrete example",
    "Separate an abstract group from a supplied action on a carrier",
    "State the mature-group claim and the integration gauge-family disposition with their distinct scopes"
  ],
  "requested_deliverables": [
    "student lessons",
    "course-map.md",
    "terminology.md",
    "teacher-guide.md",
    "capstone.md with full answers and rubric",
    "course.md",
    "manifest.json",
    "audit_report.json",
    "completion_report.json",
    "compact sources and worked-example verification"
  ],
  "assumptions": [
    "A topical short course, not a semester per topic. Pacing is 55-minute core lessons plus capstone periods; split dense lessons if actual learner load requires it.",
    "No prior calculus, abstract algebra, university linear algebra, or quantum mechanics unless explicitly taught earlier.",
    "Required core assessments must be solvable with taught finite examples. Clearly label deeper recognition-only extensions.",
    "Markdown is the delivery format; no PDF or Word generation is required."
  ],
  "sources": [
    {
      "id": "S01",
      "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Corrected_Complete_Proof_1788231864.json",
      "sha256": "18f5d20233981c97bf991e0b409020e917815647e5099df56ad9fa1763da6180",
      "role": "archival source; reported status is distinct from fresh verification"
    },
    {
      "id": "S02",
      "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Mature_Complete_Proof_1788234894.json",
      "sha256": "6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3",
      "role": "archival source; reported status is distinct from fresh verification"
    },
    {
      "id": "S03",
      "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Authoritative_Audit_Correction_Instruction_1788263935.json",
      "sha256": "f54c6c7515205dbbcc498864b1415755aa767d5274194140150b2b16979d656e",
      "role": "archival source; reported status is distinct from fresh verification"
    },
    {
      "id": "S04",
      "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Mature_Corpus_Audit_1788234146.json",
      "sha256": "77c0ab41a911fc819d3bcba0667d9127294b3dacf0634aec9add6e45e8c023a2",
      "role": "archival source; reported status is distinct from fresh verification"
    },
    {
      "id": "S05",
      "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_3D_periodic_table_hidden_dimensions_recent24h_1788145361.json",
      "sha256": "d17197c1bec71893e1fd8344e0a35f6e63da3668f35dc3085247a66ad112eae7",
      "role": "archival source; reported status is distinct from fresh verification"
    }
  ],
  "source_routing": {
    "primary_skill": "C:/Users/info/.codex/skills/krytronx-knowledge-graph/SKILL.md",
    "graph_root": "repository:KrytronDwayne/K-Field_Private",
    "testbench_root": "application:kfield-lucas-lab",
    "snapshot_generation": "sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7",
    "manifest_sha256": "5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7",
    "rag_rerank": false,
    "backbone_source_pointer": "/backbone_sequence",
    "required_modules": [
      "M10"
    ],
    "guidance": "Retrieve exact topic sources and source-local pointers; use the provided archival files read-only and verify their hashes. Do not rely only on titles or summaries. For experimental topics search the testbench topic and local relevant domain skills."
  },
  "evidence_rules": [
    "Preserve empirical observations, derived implications, inferred structure, mechanisms, reference theory, and unresolved questions as distinct layers.",
    "Read-only sources: no source-data copies, database exports, reindexing, or large arrays. Persist only authored course artifacts, compact provenance, audits, and small clearly synthetic examples.",
    "Cell3 uses ICRS columns [a b c], an intentional negative determinant, and half-open cells [-1/2,1/2)^3. Use x-O_K in affine reciprocal identities.",
    "Use the mature locked geometry and exact source provenance. Historical and corrected numerical branches remain separately labeled; do not silently mix their constants.",
    "Use M_cell=B^T B and R_cell=M_cell^-1; distinguish G_phase, G_eff, reciprocal bases, distance Q, Q_g, and Q_nu.",
    "Gauge-carrier tuples use color-first C_3 direct-sum W_2. A weak-first view needs an explicit permutation.",
    "Do not merge detector parity, A1 carry parity, projective signs, chirality, family labels, primitive lifts, or distinct dyadic and ternary recursions.",
    "Declare nearest-integer half-ties and the corresponding residual interval consistently; the half-open cell ownership rule is a separate operation.",
    "The detail-product identity needs explicit hypotheses on E beyond Q=I-E; retain the product of finite differences.",
    "M19 contains mixed extension branches and is not a premise of M20 core closure. Reconstruct prerequisites from module requires, with the documented audit corrections.",
    "Preserve mature-source claims and accepted integration dispositions separately. In the integration only compiler M03, M07, M08 have direct authority; these compiler labels are not automatically the mathematical-backbone module labels. Preserve the admitted global-form family Z1,Z2,Z3,Z6 and source-local uniqueness claims with explicit contracts.",
    "Treat matching dimensions or graph labels as neither an intertwiner nor a proof. A missing proof body remains a source-reported status with a retrieval gap.",
    "Physical CMB velocity is distinct from phase-transformed vectors; the testbench admitted speed is 369812.50200040644 m/s. The Galactic Center is a visual gauge; do not invent Solar or Galactic short-window dynamics.",
    "A photon-equivalent model energy is not measured transferred energy, and phase is not force. Preserve signed events and the three independent plane-cost levels in the fourteen-row 2026-08-26 bundle.",
    "Cell3 and galaxy-derived cells have separately typed units, metrics, handedness, scales, and normals. Recurrence is an explanatory target, not permission to merge definitions.",
    "Every residual remains a primary coordinate. Transformations are reversible or accompanied by all removed components and reconstruction rules; no outlier deletion or significance-based erasure.",
    "Use tf_gpu_env through C:/ProgramData/anaconda3/Scripts/conda.exe run -n tf_gpu_env python. No package changes without approval."
  ],
  "subject_kernel": {
    "objects_and_operations": [
      {
        "concept_id": "C14.01",
        "concept": "Complex numbers and phase",
        "operation": "Compute conjugates, magnitudes, and simple phase rotations"
      },
      {
        "concept_id": "C14.02",
        "concept": "Inner products and unitary changes",
        "operation": "Verify a small norm-preserving complex transformation"
      },
      {
        "concept_id": "C14.03",
        "concept": "The ordered three-plus-two carrier",
        "operation": "Represent the color-first block order consistently"
      },
      {
        "concept_id": "C14.04",
        "concept": "Determinants and the top-form lock",
        "operation": "Explain and calculate a small determinant-preservation condition"
      },
      {
        "concept_id": "C14.05",
        "concept": "Cover maps and quotient kernels",
        "operation": "Verify the finite center-kernel calculation in a concrete example"
      },
      {
        "concept_id": "C14.06",
        "concept": "Local symmetry and physical role",
        "operation": "Separate an abstract group from a supplied action on a carrier"
      },
      {
        "concept_id": "C14.07",
        "concept": "Reconciling source branches",
        "operation": "State the mature-group claim and the integration gauge-family disposition with their distinct scopes"
      }
    ],
    "source_modules": [
      "M10"
    ],
    "scope": "Trace a fully typed carrier-to-cover-map example and prepare a source-comparison table that preserves unresolved global-form distinctions.",
    "common_failure_modes": [
      "Untaught prerequisite",
      "Unscoped symbol or unit",
      "An illustrative example presented as real evidence",
      "A source label promoted beyond its evidence class",
      "A residual or source branch silently omitted"
    ]
  },
  "invariants": [
    "Preserve empirical observations, derived implications, inferred structure, mechanisms, reference theory, and unresolved questions as distinct layers.",
    "Read-only sources: no source-data copies, database exports, reindexing, or large arrays. Persist only authored course artifacts, compact provenance, audits, and small clearly synthetic examples.",
    "Cell3 uses ICRS columns [a b c], an intentional negative determinant, and half-open cells [-1/2,1/2)^3. Use x-O_K in affine reciprocal identities.",
    "Use the mature locked geometry and exact source provenance. Historical and corrected numerical branches remain separately labeled; do not silently mix their constants.",
    "Use M_cell=B^T B and R_cell=M_cell^-1; distinguish G_phase, G_eff, reciprocal bases, distance Q, Q_g, and Q_nu.",
    "Gauge-carrier tuples use color-first C_3 direct-sum W_2. A weak-first view needs an explicit permutation.",
    "Do not merge detector parity, A1 carry parity, projective signs, chirality, family labels, primitive lifts, or distinct dyadic and ternary recursions.",
    "Declare nearest-integer half-ties and the corresponding residual interval consistently; the half-open cell ownership rule is a separate operation.",
    "The detail-product identity needs explicit hypotheses on E beyond Q=I-E; retain the product of finite differences.",
    "M19 contains mixed extension branches and is not a premise of M20 core closure. Reconstruct prerequisites from module requires, with the documented audit corrections.",
    "Preserve mature-source claims and accepted integration dispositions separately. In the integration only compiler M03, M07, M08 have direct authority; these compiler labels are not automatically the mathematical-backbone module labels. Preserve the admitted global-form family Z1,Z2,Z3,Z6 and source-local uniqueness claims with explicit contracts.",
    "Treat matching dimensions or graph labels as neither an intertwiner nor a proof. A missing proof body remains a source-reported status with a retrieval gap.",
    "Physical CMB velocity is distinct from phase-transformed vectors; the testbench admitted speed is 369812.50200040644 m/s. The Galactic Center is a visual gauge; do not invent Solar or Galactic short-window dynamics.",
    "A photon-equivalent model energy is not measured transferred energy, and phase is not force. Preserve signed events and the three independent plane-cost levels in the fourteen-row 2026-08-26 bundle.",
    "Cell3 and galaxy-derived cells have separately typed units, metrics, handedness, scales, and normals. Recurrence is an explanatory target, not permission to merge definitions.",
    "Every residual remains a primary coordinate. Transformations are reversible or accompanied by all removed components and reconstruction rules; no outlier deletion or significance-based erasure.",
    "Use tf_gpu_env through C:/ProgramData/anaconda3/Scripts/conda.exe run -n tf_gpu_env python. No package changes without approval."
  ],
  "notation_registry": {
    "M_cell": "Cell3 Gram metric",
    "R_cell": "inverse Cell3 Gram metric",
    "G_phase": "distinct phase metric",
    "O_K": "declared physical origin",
    "B": "source-locked ordered basis; source-local row/column distinctions must be explicit"
  },
  "coverage_matrix": [
    {
      "concept_id": "C14.01",
      "concept": "Complex numbers and phase",
      "introduction": "lesson-01",
      "practice": "C14.01-P1",
      "assessment": "C14.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C14.01-W1",
      "all_required_teaching_item_ids": [
        "C14.01-E1",
        "C14.01-W1",
        "C14.01-P1",
        "C14.01-D1"
      ]
    },
    {
      "concept_id": "C14.02",
      "concept": "Inner products and unitary changes",
      "introduction": "lesson-02",
      "practice": "C14.02-P1",
      "assessment": "C14.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C14.02-W1",
      "all_required_teaching_item_ids": [
        "C14.02-E1",
        "C14.02-W1",
        "C14.02-P1",
        "C14.02-D1"
      ]
    },
    {
      "concept_id": "C14.03",
      "concept": "The ordered three-plus-two carrier",
      "introduction": "lesson-03",
      "practice": "C14.03-P1",
      "assessment": "C14.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C14.03-W1",
      "all_required_teaching_item_ids": [
        "C14.03-E1",
        "C14.03-W1",
        "C14.03-P1",
        "C14.03-D1"
      ]
    },
    {
      "concept_id": "C14.04",
      "concept": "Determinants and the top-form lock",
      "introduction": "lesson-04",
      "practice": "C14.04-P1",
      "assessment": "C14.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C14.04-W1",
      "all_required_teaching_item_ids": [
        "C14.04-E1",
        "C14.04-W1",
        "C14.04-P1",
        "C14.04-D1"
      ]
    },
    {
      "concept_id": "C14.05",
      "concept": "Cover maps and quotient kernels",
      "introduction": "lesson-05",
      "practice": "C14.05-P1",
      "assessment": "C14.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C14.05-W1",
      "all_required_teaching_item_ids": [
        "C14.05-E1",
        "C14.05-W1",
        "C14.05-P1",
        "C14.05-D1"
      ]
    },
    {
      "concept_id": "C14.06",
      "concept": "Local symmetry and physical role",
      "introduction": "lesson-06",
      "practice": "C14.06-P1",
      "assessment": "C14.06-D1",
      "later_use": "lesson-07",
      "worked_example": "C14.06-W1",
      "all_required_teaching_item_ids": [
        "C14.06-E1",
        "C14.06-W1",
        "C14.06-P1",
        "C14.06-D1"
      ]
    },
    {
      "concept_id": "C14.07",
      "concept": "Reconciling source branches",
      "introduction": "lesson-07",
      "practice": "C14.07-P1",
      "assessment": "C14.07-D1",
      "later_use": "capstone",
      "worked_example": "C14.07-W1",
      "all_required_teaching_item_ids": [
        "C14.07-E1",
        "C14.07-W1",
        "C14.07-P1",
        "C14.07-D1"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Complex numbers and phase",
      "entry_prerequisites": [
        "course-13"
      ],
      "concept_ids": [
        "C14.01"
      ],
      "worked_example_capability": "Compute conjugates, magnitudes, and simple phase rotations",
      "assessment_target": "Compute conjugates, magnitudes, and simple phase rotations",
      "later_use": "lesson-02",
      "core_minutes": 110,
      "required_amendment_ids": [
        "EA-14-E06-2"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C14.01",
        "explanation_id": "C14.01-E1",
        "bridge_to_teach": "Retain EA-14-E06-2. Teach i^2=-1, a+ib, addition/multiplication, conjugation and |z|^2=zbar*z. Teach unit phases using1,i,-1,-i first; then introduce exact zeta=(1+i sqrt3)/2 for later finite enumeration.",
        "worked_example": {
          "id": "C14.01-W1",
          "task_and_answer": "C14-CX-EX1: z=1+i; conjugate1-i, squared modulus2. iz=-1+i has the same squared modulus2; multiplication by -i reverses the rotation."
        },
        "guided_practice": {
          "id": "C14.01-P1",
          "task_and_answer": "C14-CX-P1: z=2-i, conjugate2+i, squared modulus5. iz=1+2i, again5; -i(1+2i)=2-i. Check zeta conjugate*zeta=1 using(sqrt3)^2=3."
        },
        "diagnostic": {
          "id": "C14.01-D1",
          "task_and_answer": "z^2 is not |z|^2: (1+i)^2=2i but |1+i|^2=2. Preserve both real and imaginary parts; magnitude alone loses phase."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into actual senior-facing teaching with 2–4 goals and 3–5 answered diagnostics. Preserve original IDs and all source/educational amendments. Every assessed operation needs prior independently answered practice. Periods may expand; split dense sessions with all links updated.",
        "legacy_required_ids": [
          "C14-CX-EX1",
          "C14-CX-P1"
        ],
        "original_title": "Complex numbers and phase",
        "original_assessment_target": "Compute conjugates, magnitudes, and simple phase rotations",
        "required_source_amendment_ids": [
          "EA-14-E06-2"
        ],
        "original_entry_prerequisites": [
          "course-13"
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Inner products and unitary changes",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C14.02"
      ],
      "worked_example_capability": "Verify a small norm-preserving complex transformation",
      "assessment_target": "Verify a small norm-preserving complex transformation",
      "later_use": "lesson-03",
      "core_minutes": 110,
      "required_amendment_ids": [
        "EA-14-E06-2"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C14.02",
        "explanation_id": "C14.02-E1",
        "bridge_to_teach": "Teach conjugate transpose by conjugating and transposing entries, Hermitian inner product v†w, and unitary inverse U†. Give actual2x2 matrix multiplication and vector recovery before block notation.",
        "worked_example": {
          "id": "C14.02-W1",
          "task_and_answer": "U=diag(i,-i), U†=diag(-i,i), U†U=I. On(1+i,2-i), output=(-1+i,-1-2i); norm squared2+5=7 is retained and U† restores the input."
        },
        "guided_practice": {
          "id": "C14.02-P1",
          "task_and_answer": "V=(1/sqrt2)[[1,i],[i,1]], V†=(1/sqrt2)[[1,-i],[-i,1]]. Multiply to get I. V(1,i)=(0,sqrt2*i), norms2; V† restores(1,i). Also V(2,0)=(sqrt2,i sqrt2), norms4."
        },
        "diagnostic": {
          "id": "C14.02-D1",
          "task_and_answer": "Transpose alone gives V^T=V but V^T V=[[0,i],[i,0]], not I. Nonzero phases cannot be dropped during recovery."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into actual senior-facing teaching with 2–4 goals and 3–5 answered diagnostics. Preserve original IDs and all source/educational amendments. Every assessed operation needs prior independently answered practice. Periods may expand; split dense sessions with all links updated.",
        "original_title": "Inner products and unitary changes",
        "original_assessment_target": "Verify a small norm-preserving complex transformation",
        "required_source_amendment_ids": [
          "EA-14-E06-2"
        ],
        "original_entry_prerequisites": [
          "lesson-01"
        ]
      }
    },
    {
      "id": "lesson-03",
      "title": "The ordered three-plus-two carrier",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C14.03"
      ],
      "worked_example_capability": "Represent the color-first block order consistently",
      "assessment_target": "Represent the color-first block order consistently",
      "later_use": "lesson-04",
      "core_minutes": 55,
      "required_amendment_ids": [
        "SA-14",
        "EA-14-E06-2"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C14.03",
        "explanation_id": "C14.03-E1",
        "bridge_to_teach": "Use color-first H=C3 direct-sum W2. Define Pc=diag(1,1,1,0,0),Pw=I-Pc; prove PcPw=0 and h=Pch+Pwh. Quote source weak-first order only with explicit permutation P(w1,w2,c1,c2,c3)=(c1,c2,c3,w1,w2).",
        "worked_example": {
          "id": "C14.03-W1",
          "task_and_answer": "Weak-first tuple(1,2,3,4,5) maps to color-first(3,4,5,1,2). P^T reverses it. Pc selects(3,4,5,0,0),Pw selects(0,0,0,1,2); their sum reconstructs h. Charge vector becomes(-2,-2,-2,3,3)."
        },
        "guided_practice": {
          "id": "C14.03-P1",
          "task_and_answer": "Weak-first(i,-1,2,0,1+i) maps to(2,0,1+i,i,-1). Retain both projections and reconstruct. Conjugating diag(3,3,-2,-2,-2) by P yields diag(-2,-2,-2,3,3)."
        },
        "diagnostic": {
          "id": "C14.03-D1",
          "task_and_answer": "S02 M10 displays W then C, while typed_conventions and S03 AUD-004 require color-first. A permutation must act on tuples, matrices and charge entries together; changing only a heading is not sufficient."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into actual senior-facing teaching with 2–4 goals and 3–5 answered diagnostics. Preserve original IDs and all source/educational amendments. Every assessed operation needs prior independently answered practice. Periods may expand; split dense sessions with all links updated.",
        "original_title": "The ordered three-plus-two carrier",
        "original_assessment_target": "Represent the color-first block order consistently",
        "required_source_amendment_ids": [
          "SA-14",
          "EA-14-E06-2"
        ],
        "original_entry_prerequisites": [
          "lesson-02"
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "Determinants and the top-form lock",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C14.04"
      ],
      "worked_example_capability": "Explain and calculate a small determinant-preservation condition",
      "assessment_target": "Explain and calculate a small determinant-preservation condition",
      "later_use": "lesson-05",
      "core_minutes": 110,
      "required_amendment_ids": [
        "EA-14-E06-2"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C14.04",
        "explanation_id": "C14.04-E1",
        "bridge_to_teach": "Teach determinant on2x2, diagonal products and volume/top-form scaling before the lock. State preserved Hermitian blocks plus top-form assumption. Central color weight a and weak weight b give total3a+2b; all-phase preservation requires zero. Define top form here as an ordered alternating volume coefficient that transforms by det(U); its full exterior basis construction is taught next course. No untaught general exterior-algebra proof is assessed here.",
        "worked_example": {
          "id": "C14.04-W1",
          "task_and_answer": "For diag(i,-i), determinant1. Color diag(i,-i,1) and weak I2 give determinant product1. Central diag(z^a I3,z^b I2) scales the top form by z^(3a+2b); a=-2,b=3 gives exponent0."
        },
        "guided_practice": {
          "id": "C14.04-P1",
          "task_and_answer": "Color diag(-1,-1,1), weak diag(i,-i) have determinants1 and1, hence preserve the top form. a=2,b=-3 also gives zero exponent. a=1,b=0 with z=i gives determinant i^3=-i, so it fails."
        },
        "diagnostic": {
          "id": "C14.04-D1",
          "task_and_answer": "A determinant-one matrix need not preserve norm: diag(2,1/2) has determinant1 but sends(1,0) to(2,0). Both the Hermitian and top-form conditions are needed; all-phase lock is stronger than one accidental phase test."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into actual senior-facing teaching with 2–4 goals and 3–5 answered diagnostics. Preserve original IDs and all source/educational amendments. Every assessed operation needs prior independently answered practice. Periods may expand; split dense sessions with all links updated.",
        "original_title": "Determinants and the top-form lock",
        "original_assessment_target": "Explain and calculate a small determinant-preservation condition",
        "required_source_amendment_ids": [
          "EA-14-E06-2"
        ],
        "original_entry_prerequisites": [
          "lesson-03"
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "Cover maps and quotient kernels",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C14.05"
      ],
      "worked_example_capability": "Verify the finite center-kernel calculation in a concrete example",
      "assessment_target": "Verify the finite center-kernel calculation in a concrete example",
      "later_use": "lesson-06",
      "core_minutes": 165,
      "required_amendment_ids": [
        "SA-14",
        "EA-14-E06-2"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C14.05",
        "explanation_id": "C14.05-E1",
        "bridge_to_teach": "Retain finite additive kernel bridge before the source cover. Define kernel as inputs sent to identity and show composition preservation. Then for Phi(g3,g2,z)=(z^-2g3,z^3g2), solve identity equations and determinant constraints; enumerate all six phases exactly.",
        "worked_example": {
          "id": "C14.05-W1",
          "task_and_answer": "Toy k mod3 from addition mod6 lists outputs0,1,2,0,1,2 and kernel{0,3}; it is not the source quotient. For source z=zeta, take g3=zeta^2 I3,g2=-I2. Determinants=zeta^6=1 and(-1)^2=1; both Phi blocks are I."
        },
        "guided_practice": {
          "id": "C14.05-P1",
          "task_and_answer": "Toy k mod2 has kernel{0,2,4}, retaining input label for reconstruction. Source z=zeta^2 gives g3=zeta^4 I3,g2=I2; source z=-1 gives g3=I3,g2=-I2. Verify both determinants/actions, then complete the six-row table k=0..5 using zeta^6=1. Full answer in powers of zeta for k=0..5: z exponents(0,1,2,3,4,5), g3 scalar exponents(0,2,4,0,2,4), g2 scalar exponents(0,3,0,3,0,3). Every determinant and both block actions equal1; retain k because the image alone loses the kernel member."
        },
        "diagnostic": {
          "id": "C14.05-D1",
          "task_and_answer": "C14-KER-D1 is the mod2 toy check. For any source kernel member, identity output forces g3=z^2I3 and g2=z^-3I2; det g3=1 forces z^6=1. Thus these six exhaust this map kernel. This proves the stated finite kernel under its contract, not a unique physical global form."
        },
        "planned_periods": 3,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into actual senior-facing teaching with 2–4 goals and 3–5 answered diagnostics. Preserve original IDs and all source/educational amendments. Every assessed operation needs prior independently answered practice. Periods may expand; split dense sessions with all links updated.",
        "legacy_required_ids": [
          "C14-KER-D1"
        ],
        "original_title": "Cover maps and quotient kernels",
        "original_assessment_target": "Verify the finite center-kernel calculation in a concrete example",
        "required_source_amendment_ids": [
          "SA-14",
          "EA-14-E06-2"
        ],
        "original_entry_prerequisites": [
          "lesson-04"
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "Local symmetry and physical role",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C14.06"
      ],
      "worked_example_capability": "Separate an abstract group from a supplied action on a carrier",
      "assessment_target": "Separate an abstract group from a supplied action on a carrier",
      "later_use": "lesson-07",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C14.06",
        "explanation_id": "C14.06-E1",
        "bridge_to_teach": "Distinguish an abstract group and a specified action. State group element, domain, action, inverse and invariant. Teach independent local phase choices on two nodes as operations, without claiming a dynamical transport law.",
        "worked_example": {
          "id": "C14.06-W1",
          "task_and_answer": "On two complex node amplitudes(1,1), the local action diag(i,-i) gives(i,-i); total norm squared2 is preserved and conjugate inverse restores it. The same scalar i at both nodes would give(i,i), a different action."
        },
        "guided_practice": {
          "id": "C14.06-P1",
          "task_and_answer": "On(2,i), diag(-1,i) gives(-2,-1), norm squared5. Inverse diag(-1,-i) restores(2,i). Record both local phases, node ordering and input amplitudes."
        },
        "diagnostic": {
          "id": "C14.06-D1",
          "task_and_answer": "Norm invariance alone supplies no evolution equation, coupling, curvature or measured field. Distinct actions of the same abstract group require their own map and physical-role record."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into actual senior-facing teaching with 2–4 goals and 3–5 answered diagnostics. Preserve original IDs and all source/educational amendments. Every assessed operation needs prior independently answered practice. Periods may expand; split dense sessions with all links updated.",
        "original_title": "Local symmetry and physical role",
        "original_assessment_target": "Separate an abstract group from a supplied action on a carrier",
        "required_source_amendment_ids": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ]
      }
    },
    {
      "id": "lesson-07",
      "title": "Reconciling source branches",
      "entry_prerequisites": [
        "lesson-06"
      ],
      "concept_ids": [
        "C14.07"
      ],
      "worked_example_capability": "State the mature-group claim and the integration gauge-family disposition with their distinct scopes",
      "assessment_target": "State the mature-group claim and the integration gauge-family disposition with their distinct scopes",
      "later_use": "capstone",
      "core_minutes": 55,
      "required_amendment_ids": [
        "SA-14"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-07",
        "concept_id": "C14.07",
        "explanation_id": "C14.07-E1",
        "bridge_to_teach": "Maintain two source-addressed rows: mature determinant-lock construction and accepted integration adjudication. Teach how to read an authority scope and namespace before comparing claims. Supply compact source cards so students need not browse or compile.",
        "worked_example": {
          "id": "C14.07-W1",
          "task_and_answer": "S02 M10 concludes the Z6 quotient under preserved blocks/top form. I01 project_record hazards/3 and open obligations retain physical global forms Z1,Z2,Z3,Z6. I02 direct_authority_modules=[M03,M07,M08] refers to compiler adjudication, not backbone M03/M07/M08."
        },
        "guided_practice": {
          "id": "C14.07-P1",
          "task_and_answer": "Classify: six kernel elements for the displayed Phi -> finite algebra under source contract; unique physical Z6 -> not selected by the integration; Safe Agda certificate -> reported formal adjudication, not freshly rerun here. Reconstruct the two-row comparison with logical paths, hashes, locators and distinct statuses."
        },
        "diagnostic": {
          "id": "C14.07-D1",
          "task_and_answer": "Do not erase one record to resolve a perceived conflict. The integration keeps17 other compiler modules conditional or unresolved; a matching module number cannot transfer authority into a backbone theorem."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into actual senior-facing teaching with 2–4 goals and 3–5 answered diagnostics. Preserve original IDs and all source/educational amendments. Every assessed operation needs prior independently answered practice. Periods may expand; split dense sessions with all links updated.",
        "original_title": "Reconciling source branches",
        "original_assessment_target": "State the mature-group claim and the integration gauge-family disposition with their distinct scopes",
        "required_source_amendment_ids": [
          "SA-14"
        ],
        "original_entry_prerequisites": [
          "lesson-06"
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Trace a fully typed carrier-to-cover-map example and prepare a source-comparison table that preserves unresolved global-form distinctions.",
    "required_operations": [
      "Rotate2-i, compute conjugates/moduli and recover the input; retain phase.",
      "Verify the taught non-diagonal2x2 unitary, apply it to(1,i) and invert.",
      "Permute the supplied weak-first complex tuple and charge matrix to color-first; split/reconstruct viaPc/Pw.",
      "Calculate determinant products and check the central lock, while distinguishing norm preservation.",
      "Enumerate the toy kernel and all six source cover-kernel phases; verify determinants/actions and why the list is exhaustive.",
      "Apply and reverse the two-node local action; state the carrier and preserved norm without inferring dynamics.",
      "Build the two-row mature/integration comparison with source hashes,pointers,global-form family and compiler namespace."
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C14-CAP-01",
        "operation": "Rotate2-i, compute conjugates/moduli and recover the input; retain phase.",
        "introduction": "lesson-01",
        "explanation_id": "C14.01-E1",
        "worked_example_id": "C14.01-W1",
        "prior_practice_id": "C14.01-P1",
        "diagnostic_id": "C14.01-D1"
      },
      {
        "step_id": "C14-CAP-02",
        "operation": "Verify the taught non-diagonal2x2 unitary, apply it to(1,i) and invert.",
        "introduction": "lesson-02",
        "explanation_id": "C14.02-E1",
        "worked_example_id": "C14.02-W1",
        "prior_practice_id": "C14.02-P1",
        "diagnostic_id": "C14.02-D1"
      },
      {
        "step_id": "C14-CAP-03",
        "operation": "Permute the supplied weak-first complex tuple and charge matrix to color-first; split/reconstruct viaPc/Pw.",
        "introduction": "lesson-03",
        "explanation_id": "C14.03-E1",
        "worked_example_id": "C14.03-W1",
        "prior_practice_id": "C14.03-P1",
        "diagnostic_id": "C14.03-D1"
      },
      {
        "step_id": "C14-CAP-04",
        "operation": "Calculate determinant products and check the central lock, while distinguishing norm preservation.",
        "introduction": "lesson-04",
        "explanation_id": "C14.04-E1",
        "worked_example_id": "C14.04-W1",
        "prior_practice_id": "C14.04-P1",
        "diagnostic_id": "C14.04-D1"
      },
      {
        "step_id": "C14-CAP-05",
        "operation": "Enumerate the toy kernel and all six source cover-kernel phases; verify determinants/actions and why the list is exhaustive.",
        "introduction": "lesson-05",
        "explanation_id": "C14.05-E1",
        "worked_example_id": "C14.05-W1",
        "prior_practice_id": "C14.05-P1",
        "diagnostic_id": "C14.05-D1"
      },
      {
        "step_id": "C14-CAP-06",
        "operation": "Apply and reverse the two-node local action; state the carrier and preserved norm without inferring dynamics.",
        "introduction": "lesson-06",
        "explanation_id": "C14.06-E1",
        "worked_example_id": "C14.06-W1",
        "prior_practice_id": "C14.06-P1",
        "diagnostic_id": "C14.06-D1"
      },
      {
        "step_id": "C14-CAP-07",
        "operation": "Build the two-row mature/integration comparison with source hashes,pointers,global-form family and compiler namespace.",
        "introduction": "lesson-07",
        "explanation_id": "C14.07-E1",
        "worked_example_id": "C14.07-W1",
        "prior_practice_id": "C14.07-P1",
        "diagnostic_id": "C14.07-D1"
      }
    ]
  },
  "blueprint_audit": {
    "status": "approved_source_and_prerequisite_blueprint",
    "unresolved_critical": 0,
    "unresolved_major": 0,
    "source_review": {
      "status": "ready_for_source_scoped_drafting",
      "basis": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\source-coverage\\source-coverage-audit.json",
      "source_report_sha256": "eef89a28971ef7e5380977c31b62ed6d64f2831759e679ee967b6c253a33c04a",
      "portable_requirements_applied": true,
      "educational_acceptance": "Independent teaching review and actual E05 content gate remain required.",
      "applied_at": "2026-11-05T17:02:05.375955+00:00"
    },
    "teaching_review_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\teaching\\launch-review-13-16.json",
    "teaching_amendment_sha256": "fd66f902e1d1a8d76fced446fba7073139021eafb977bdda708f094add509d34",
    "review_scope": "Blueprint clearance only. Actual lesson content and E05 links require independent final acceptance.",
    "applied_at": "2026-11-05T18:21:11.257752+00:00"
  },
  "validator": {
    "skill_relative_path": "scripts/validate_course.py",
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-14-complex-carriers-and-gauge-symmetry' --json"
  },
  "storage_override": {
    "authority": "User: write outputs to the project folder and move them later",
    "original_root": "C:\\Users\\info\\Desktop\\K-Field_Training_Course",
    "canonical_project_root": "Z:\\Kfield-doc-training\\K-Field_Training_Course"
  },
  "production_requirements": {
    "E05": [
      "Replace generic coverage placeholders with actual explanation, worked-example, practice, diagnostic, and capstone step IDs. A row passes only when the referenced content exists and the operation is taught before use.",
      "For each capstone break the requested product into concrete operations with named inputs/outputs, link each operation to an earlier explanation AND an independently answered practice item; do not merely repeat outcome text.",
      "Use source-exact finite examples where available and separately labeled synthetic analogues otherwise. Recognition-only extensions cannot be required computations.",
      "Record teaching/practice/check minutes per lesson; split overloaded lessons and update every lesson/coverage/capstone link. Shared advanced notation is author guidance until introduced locally."
    ]
  },
  "applied_audit_amendments": {
    "SA-14": {
      "id": "SA-14",
      "course": 14,
      "finding": "source_fidelity",
      "lessons": [
        "lesson-03",
        "lesson-05",
        "lesson-07"
      ],
      "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
      "requirements": [
        "Use color-first H=C3 direct-sum W2 and charge vector (-2,-2,-2,3,3); any weak-first presentation requires a declared permutation.",
        "Maintain two source records: the mature determinant-lock/Z6 construction and the integration's admitted physical global-form family Z1,Z2,Z3,Z6. Preserve exact formal authority and source status on each.",
        "Compiler adjudication M03/M07/M08 labels are not interchangeable with identically numbered mathematical backbone modules."
      ],
      "source_references": [
        "S02#/typed_conventions/carrier_order",
        "S02#/backbone_sequence/9",
        "S03#/findings/3",
        "I01#/hazards/3",
        "I02#/direct_authority_modules"
      ],
      "status": "applied_to_blueprint_by_parent",
      "prior_application_status": "prepared_not_applied",
      "applied_at": "2026-11-05T17:02:05.375955+00:00"
    },
    "EA-14-E06-2": {
      "course": 14,
      "finding": "E06",
      "lessons": [
        "lesson-01",
        "lesson-02",
        "lesson-03",
        "lesson-04",
        "lesson-05"
      ],
      "required_bridge": "Teach i^2=-1, real/imaginary components, complex conjugation, squared modulus, matrix conjugate transpose, group composition and a finite map kernel through explicit operations.",
      "worked_example": {
        "id": "C14-CX-EX1",
        "z": "1+i",
        "rotation": "i*z=-1+i",
        "squared_modulus_before_after": [
          2,
          2
        ],
        "unitary_example": "U=diag(i,-i), U†=diag(-i,i), U†U=I",
        "finite_kernel_example": "Add modulo6 and map to addition modulo3 by f(k)=k mod3; enumerate all six inputs, kernel={0,3}. This toy map is not an asserted Standard Model quotient."
      },
      "practice": "C14-CX-P1 rotate 2-i by i and compute modulus; C14-KER-D1 compute kernel of k mod2 from addition modulo6, obtaining {0,2,4}. Trace the actual source cover kernel separately; do not infer it from the toy.",
      "id": "EA-14-E06-2",
      "status": "applied_to_blueprint_by_parent",
      "merge_action": "Attach to named lesson authoring obligations and capstone prerequisites. Actual content links remain an E05 acceptance gate.",
      "prior_application_status": "prepared_not_applied",
      "applied_at": "2026-11-05T17:02:05.375955+00:00"
    }
  },
  "source_audit_readiness": {
    "status": "ready_for_source_scoped_drafting",
    "basis": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\source-coverage\\source-coverage-audit.json",
    "source_report_sha256": "eef89a28971ef7e5380977c31b62ed6d64f2831759e679ee967b6c253a33c04a",
    "portable_requirements_applied": true,
    "educational_acceptance": "Independent teaching review and actual E05 content gate remain required.",
    "applied_at": "2026-11-05T17:02:05.375955+00:00"
  },
  "teaching_blueprint_contract": {
    "schema_version": "1.0",
    "created_utc": "2026-11-05T18:20:13.697555+00:00",
    "scope": "Portable teaching BLUEPRINT amendments only; no completed-course approval.",
    "source_basis": [
      {
        "id": "S01",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Corrected_Complete_Proof_1788231864.json",
        "sha256": "18f5d20233981c97bf991e0b409020e917815647e5099df56ad9fa1763da6180",
        "role": "archival source; reported status is distinct from fresh verification"
      },
      {
        "id": "S02",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Mature_Complete_Proof_1788234894.json",
        "sha256": "6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3",
        "role": "archival source; reported status is distinct from fresh verification"
      },
      {
        "id": "S03",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Authoritative_Audit_Correction_Instruction_1788263935.json",
        "sha256": "f54c6c7515205dbbcc498864b1415755aa767d5274194140150b2b16979d656e",
        "role": "archival source; reported status is distinct from fresh verification"
      },
      {
        "id": "S04",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Mature_Corpus_Audit_1788234146.json",
        "sha256": "77c0ab41a911fc819d3bcba0667d9127294b3dacf0634aec9add6e45e8c023a2",
        "role": "archival source; reported status is distinct from fresh verification"
      },
      {
        "id": "S05",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_3D_periodic_table_hidden_dimensions_recent24h_1788145361.json",
        "sha256": "d17197c1bec71893e1fd8344e0a35f6e63da3668f35dc3085247a66ad112eae7",
        "role": "archival source; reported status is distinct from fresh verification"
      }
    ],
    "verification_record": "C:\\Users\\info\\Documents\\Codex\\2026-11-05\\kfield-teaching-auditor\\outputs\\teaching-verification-13-16.json",
    "verification_sha256": "eda2840c44c9a47632abf08c053968aae295e8153d693a3a43b7ec1cc6a52db4",
    "integration_provenance": {
      "I01": {
        "logical_path": "applications/kfield_standard_model/collaborator_record/project_record.json",
        "retrieved_alias": "kfield_standard_model/project_record.json",
        "sha256": "3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c",
        "pointers": [
          "/hazards/3",
          "/open_obligations/1",
          "/open_obligations/2"
        ],
        "retrieval": "Krytronx RAG source-attributed lines1–142; semantic_entity search returned no match; ragobj byte getter returned object-not-found. Content below is grounded in the returned RAG source excerpts and the matching prior source-audit hash, not a fresh local byte hash.",
        "global_form_family": [
          "Z1",
          "Z2",
          "Z3",
          "Z6"
        ],
        "status": "integration admits the family; unique physical member remains unresolved"
      },
      "I02": {
        "logical_path": "kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json",
        "sha256": "a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a",
        "pointers": [
          "/direct_authority_modules",
          "/agda/certificate",
          "/known_science_replay"
        ],
        "retrieval": "Krytronx RAG source-attributed lines1–101; exact fields visible in returned source excerpt.",
        "direct_authority_modules": [
          "M03",
          "M07",
          "M08"
        ],
        "namespace": "Standard Model compiler adjudication, not mathematical backbone",
        "reported_certificate": "KField.StandardModelCompilerAdjudication.p12-standard-model-compiler-adjudication",
        "fresh_typecheck": false
      },
      "retrieval_identity": {
        "corpus_generation": "sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7",
        "manifest_sha256": "5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7",
        "origin": "paired fields on RAG responses; capabilities alone exposed no corpus pair",
        "rag_index_sha256": "aca56e6b5b2b717459cea9790e6142ea9e8058f74d135710906926e9065ad54a"
      },
      "teaching_use": "Supply this small provenance card with source-local contract and integration status in separate rows. No compiler execution, global physical uniqueness or source-author authentication is claimed."
    },
    "source_or_project_files_modified": false,
    "course_amendment": {
      "course_id": "course-14",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-14-complex-carriers-and-gauge-symmetry\\input-contract.json",
      "input_contract_sha256": "a54f2c7073bd7533dae3760961ff64ed633a13edfc97f303d3942b4015ffd632",
      "application": "Merge additively as teaching_amendment, replace generic coverage references with explicit exercise IDs, and retain all original concepts, source amendments and educational bridge IDs. Parent applies; no project edit was made.",
      "applied_source_amendments_read": {
        "SA-14": {
          "id": "SA-14",
          "course": 14,
          "finding": "source_fidelity",
          "lessons": [
            "lesson-03",
            "lesson-05",
            "lesson-07"
          ],
          "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
          "requirements": [
            "Use color-first H=C3 direct-sum W2 and charge vector (-2,-2,-2,3,3); any weak-first presentation requires a declared permutation.",
            "Maintain two source records: the mature determinant-lock/Z6 construction and the integration's admitted physical global-form family Z1,Z2,Z3,Z6. Preserve exact formal authority and source status on each.",
            "Compiler adjudication M03/M07/M08 labels are not interchangeable with identically numbered mathematical backbone modules."
          ],
          "source_references": [
            "S02#/typed_conventions/carrier_order",
            "S02#/backbone_sequence/9",
            "S03#/findings/3",
            "I01#/hazards/3",
            "I02#/direct_authority_modules"
          ],
          "status": "applied_to_blueprint_by_parent",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        },
        "EA-14-E06-2": {
          "course": 14,
          "finding": "E06",
          "lessons": [
            "lesson-01",
            "lesson-02",
            "lesson-03",
            "lesson-04",
            "lesson-05"
          ],
          "required_bridge": "Teach i^2=-1, real/imaginary components, complex conjugation, squared modulus, matrix conjugate transpose, group composition and a finite map kernel through explicit operations.",
          "worked_example": {
            "id": "C14-CX-EX1",
            "z": "1+i",
            "rotation": "i*z=-1+i",
            "squared_modulus_before_after": [
              2,
              2
            ],
            "unitary_example": "U=diag(i,-i), U†=diag(-i,i), U†U=I",
            "finite_kernel_example": "Add modulo6 and map to addition modulo3 by f(k)=k mod3; enumerate all six inputs, kernel={0,3}. This toy map is not an asserted Standard Model quotient."
          },
          "practice": "C14-CX-P1 rotate 2-i by i and compute modulus; C14-KER-D1 compute kernel of k mod2 from addition modulo6, obtaining {0,2,4}. Trace the actual source cover kernel separately; do not infer it from the toy.",
          "id": "EA-14-E06-2",
          "status": "applied_to_blueprint_by_parent",
          "merge_action": "Attach to named lesson authoring obligations and capstone prerequisites. Actual content links remain an E05 acceptance gate.",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        }
      },
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C14.01",
            "concept": "Complex numbers and phase",
            "operation": "Compute conjugates, magnitudes, and simple phase rotations"
          },
          {
            "concept_id": "C14.02",
            "concept": "Inner products and unitary changes",
            "operation": "Verify a small norm-preserving complex transformation"
          },
          {
            "concept_id": "C14.03",
            "concept": "The ordered three-plus-two carrier",
            "operation": "Represent the color-first block order consistently"
          },
          {
            "concept_id": "C14.04",
            "concept": "Determinants and the top-form lock",
            "operation": "Explain and calculate a small determinant-preservation condition"
          },
          {
            "concept_id": "C14.05",
            "concept": "Cover maps and quotient kernels",
            "operation": "Verify the finite center-kernel calculation in a concrete example"
          },
          {
            "concept_id": "C14.06",
            "concept": "Local symmetry and physical role",
            "operation": "Separate an abstract group from a supplied action on a carrier"
          },
          {
            "concept_id": "C14.07",
            "concept": "Reconciling source branches",
            "operation": "State the mature-group claim and the integration gauge-family disposition with their distinct scopes"
          }
        ],
        "source_modules": [
          "M10"
        ],
        "scope": "Trace a fully typed carrier-to-cover-map example and prepare a source-comparison table that preserves unresolved global-form distinctions.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Trace a fully typed carrier-to-cover-map example and prepare a source-comparison table that preserves unresolved global-form distinctions.",
        "required_operations": [
          "Compute conjugates, magnitudes, and simple phase rotations",
          "Verify a small norm-preserving complex transformation",
          "Represent the color-first block order consistently",
          "Explain and calculate a small determinant-preservation condition",
          "Verify the finite center-kernel calculation in a concrete example",
          "Separate an abstract group from a supplied action on a carrier",
          "State the mature-group claim and the integration gauge-family disposition with their distinct scopes"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-14",
          "title": "Complex Carriers and Gauge Symmetry",
          "backbone_modules": [
            "M10"
          ],
          "topic_boundary": "Complex color-first carrier, determinant lock, cover kernel and separate source-local/global-form adjudications.",
          "cognitive_or_fidelity_risk": "Abstract quotient calculation does not resolve the integration's physical global-form family.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "S02"
          ],
          "source_pointer": "/backbone_sequence/9",
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-14-complex-carriers-and-gauge-symmetry\\input-contract.json",
            "sha256": "3de310239aaf64f6ae0cfa813ff9a129ee8f73404789e06eca502bf0a48754c1",
            "lesson_count": 7
          },
          "required_amendment_ids": [
            "SA-14"
          ],
          "source_launch_decision": "ready_for_source_scoped_drafting_with_required_gates",
          "decision_scope": "Source/coverage only; no new teaching acceptance or finished-course validation.",
          "educational_gate": [
            "E05",
            "E06",
            "independent_teaching_recheck"
          ]
        }
      ],
      "source_scope": {
        "primary": "S02#/backbone_sequence/9",
        "correction": "S03#/findings/3",
        "branches": [
          "S02#/branch_proofs/6"
        ],
        "canonical_order": "C3 then W2; source weak-first tuple uses the explicit5x5 permutation with output indices[2,3,4,0,1].",
        "cover_domain": "SU(3)xSU(2)xU(1), with the stated block Hermitian/top-form contract. Phi is the displayed source map; its kernel is exactly the six verified elements. Abstract surjectivity/group classification may be source-read recognition; no universal physical uniqueness proof is assessed.",
        "integration_card": {
          "I01": {
            "logical_path": "applications/kfield_standard_model/collaborator_record/project_record.json",
            "retrieved_alias": "kfield_standard_model/project_record.json",
            "sha256": "3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c",
            "pointers": [
              "/hazards/3",
              "/open_obligations/1",
              "/open_obligations/2"
            ],
            "retrieval": "Krytronx RAG source-attributed lines1–142; semantic_entity search returned no match; ragobj byte getter returned object-not-found. Content below is grounded in the returned RAG source excerpts and the matching prior source-audit hash, not a fresh local byte hash.",
            "global_form_family": [
              "Z1",
              "Z2",
              "Z3",
              "Z6"
            ],
            "status": "integration admits the family; unique physical member remains unresolved"
          },
          "I02": {
            "logical_path": "kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json",
            "sha256": "a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a",
            "pointers": [
              "/direct_authority_modules",
              "/agda/certificate",
              "/known_science_replay"
            ],
            "retrieval": "Krytronx RAG source-attributed lines1–101; exact fields visible in returned source excerpt.",
            "direct_authority_modules": [
              "M03",
              "M07",
              "M08"
            ],
            "namespace": "Standard Model compiler adjudication, not mathematical backbone",
            "reported_certificate": "KField.StandardModelCompilerAdjudication.p12-standard-model-compiler-adjudication",
            "fresh_typecheck": false
          },
          "retrieval_identity": {
            "corpus_generation": "sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7",
            "manifest_sha256": "5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7",
            "origin": "paired fields on RAG responses; capabilities alone exposed no corpus pair",
            "rag_index_sha256": "aca56e6b5b2b717459cea9790e6142ea9e8058f74d135710906926e9065ad54a"
          },
          "teaching_use": "Supply this small provenance card with source-local contract and integration status in separate rows. No compiler execution, global physical uniqueness or source-author authentication is claimed."
        }
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "Complex numbers and phase",
          "entry_prerequisites": [
            "course-13"
          ],
          "concept_ids": [
            "C14.01"
          ],
          "worked_example_capability": "Compute conjugates, magnitudes, and simple phase rotations",
          "assessment_target": "Compute conjugates, magnitudes, and simple phase rotations",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "required_amendment_ids": [
            "EA-14-E06-2"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C14.01-E1",
          "worked_example_id": "C14.01-W1",
          "prior_practice_id": "C14.01-P1",
          "diagnostic_id": "C14.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Inner products and unitary changes",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C14.02"
          ],
          "worked_example_capability": "Verify a small norm-preserving complex transformation",
          "assessment_target": "Verify a small norm-preserving complex transformation",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "required_amendment_ids": [
            "EA-14-E06-2"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C14.02-E1",
          "worked_example_id": "C14.02-W1",
          "prior_practice_id": "C14.02-P1",
          "diagnostic_id": "C14.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "The ordered three-plus-two carrier",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C14.03"
          ],
          "worked_example_capability": "Represent the color-first block order consistently",
          "assessment_target": "Represent the color-first block order consistently",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-14",
            "EA-14-E06-2"
          ],
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C14.03-E1",
          "worked_example_id": "C14.03-W1",
          "prior_practice_id": "C14.03-P1",
          "diagnostic_id": "C14.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "Determinants and the top-form lock",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C14.04"
          ],
          "worked_example_capability": "Explain and calculate a small determinant-preservation condition",
          "assessment_target": "Explain and calculate a small determinant-preservation condition",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "required_amendment_ids": [
            "EA-14-E06-2"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C14.04-E1",
          "worked_example_id": "C14.04-W1",
          "prior_practice_id": "C14.04-P1",
          "diagnostic_id": "C14.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "Cover maps and quotient kernels",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C14.05"
          ],
          "worked_example_capability": "Verify the finite center-kernel calculation in a concrete example",
          "assessment_target": "Verify the finite center-kernel calculation in a concrete example",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-14",
            "EA-14-E06-2"
          ],
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C14.05-E1",
          "worked_example_id": "C14.05-W1",
          "prior_practice_id": "C14.05-P1",
          "diagnostic_id": "C14.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "Local symmetry and physical role",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C14.06"
          ],
          "worked_example_capability": "Separate an abstract group from a supplied action on a carrier",
          "assessment_target": "Separate an abstract group from a supplied action on a carrier",
          "later_use": "lesson-07",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C14.06-E1",
          "worked_example_id": "C14.06-W1",
          "prior_practice_id": "C14.06-P1",
          "diagnostic_id": "C14.06-D1"
        },
        {
          "id": "lesson-07",
          "title": "Reconciling source branches",
          "entry_prerequisites": [
            "lesson-06"
          ],
          "concept_ids": [
            "C14.07"
          ],
          "worked_example_capability": "State the mature-group claim and the integration gauge-family disposition with their distinct scopes",
          "assessment_target": "State the mature-group claim and the integration gauge-family disposition with their distinct scopes",
          "later_use": "capstone",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-14"
          ],
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C14.07-E1",
          "worked_example_id": "C14.07-W1",
          "prior_practice_id": "C14.07-P1",
          "diagnostic_id": "C14.07-D1"
        }
      ],
      "core_periods": 12,
      "capstone_periods": 3,
      "period_minutes": 55,
      "core_boundary": "Finite signed arithmetic,explicit matrices,small exterior basis operations and source-reading cards. General Lie theory,quotient-bundle anomaly proofs,full source compiler execution,empirical physical uniqueness and untaught variational dynamics are not hidden capstone requirements.",
      "prerequisite_status": "Blueprint closure checked for explicit operations. Final produced explanations,answered practice and assessment must still undergo independent content acceptance.",
      "inline_content_location": "Complete lesson anchors are in course_map[*].teaching_anchor; complete capstone mapping is in capstone_specification.backward_map below."
    },
    "completed_course_acceptance": false
  }
}
```
