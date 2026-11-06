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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-23-gravity-inertia-and-exceptional-branches",
  "topic": "Gravity, Inertia, and Exceptional Branches",
  "series_course_id": "course-23",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-10",
    "Capabilities taught in course-12",
    "Capabilities taught in course-14",
    "Capabilities taught in course-17",
    "Capabilities taught in course-22"
  ],
  "learning_outcomes": [
    "Trace the gravity-related scalar definitions to their source variables",
    "Verify a small reciprocal reconstruction with its metric",
    "Separate a directional kinematic calculation from a force law",
    "Recompute finite counts before comparing named algebraic structures",
    "Identify the map needed to connect a cycle sector to an algebra action",
    "Compare mechanisms by predictions, invariants, and required inputs",
    "Preserve the archived constructions, unconstructed extensions, and residual questions"
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
      "M19"
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
        "concept_id": "C23.01",
        "concept": "Scalar lifts and reconstructed shape",
        "operation": "Trace the gravity-related scalar definitions to their source variables"
      },
      {
        "concept_id": "C23.02",
        "concept": "Reciprocal inversion identities",
        "operation": "Verify a small reciprocal reconstruction with its metric"
      },
      {
        "concept_id": "C23.03",
        "concept": "Geometry and proposed inertial response",
        "operation": "Separate a directional kinematic calculation from a force law"
      },
      {
        "concept_id": "C23.04",
        "concept": "Cycle counts and exceptional dimensions",
        "operation": "Recompute finite counts before comparing named algebraic structures"
      },
      {
        "concept_id": "C23.05",
        "concept": "An action needs more than a matching dimension",
        "operation": "Identify the map needed to connect a cycle sector to an algebra action"
      },
      {
        "concept_id": "C23.06",
        "concept": "Comparing mechanism classes",
        "operation": "Compare mechanisms by predictions, invariants, and required inputs"
      },
      {
        "concept_id": "C23.07",
        "concept": "A map of exact and open branches",
        "operation": "Preserve the archived constructions, unconstructed extensions, and residual questions"
      }
    ],
    "source_modules": [
      "M19"
    ],
    "scope": "Produce a branch atlas with one verified reconstruction, one sufficient-mechanism comparison, and one falsifiable extension proposal.",
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
      "concept_id": "C23.01",
      "concept": "Scalar lifts and reconstructed shape",
      "introduction": "lesson-01",
      "practice": "C23.01-P1",
      "assessment": "C23.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C23.01-W1",
      "all_required_teaching_item_ids": [
        "C23.01-E1",
        "C23.01-W1",
        "C23.01-P1",
        "C23.01-D1"
      ]
    },
    {
      "concept_id": "C23.02",
      "concept": "Reciprocal inversion identities",
      "introduction": "lesson-02",
      "practice": "C23.02-P1",
      "assessment": "C23.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C23.02-W1",
      "all_required_teaching_item_ids": [
        "C23.02-E1",
        "C23.02-W1",
        "C23.02-P1",
        "C23.02-D1"
      ]
    },
    {
      "concept_id": "C23.03",
      "concept": "Geometry and proposed inertial response",
      "introduction": "lesson-03",
      "practice": "C23.03-P1",
      "assessment": "C23.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C23.03-W1",
      "all_required_teaching_item_ids": [
        "C23.03-E1",
        "C23.03-W1",
        "C23.03-P1",
        "C23.03-D1"
      ]
    },
    {
      "concept_id": "C23.04",
      "concept": "Cycle counts and exceptional dimensions",
      "introduction": "lesson-04",
      "practice": "C23.04-P1",
      "assessment": "C23.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C23.04-W1",
      "all_required_teaching_item_ids": [
        "C23.04-E1",
        "C23.04-W1",
        "C23.04-P1",
        "C23.04-D1"
      ]
    },
    {
      "concept_id": "C23.05",
      "concept": "An action needs more than a matching dimension",
      "introduction": "lesson-05",
      "practice": "C23.05-P1",
      "assessment": "C23.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C23.05-W1",
      "all_required_teaching_item_ids": [
        "C23.05-E1",
        "C23.05-W1",
        "C23.05-P1",
        "C23.05-D1"
      ]
    },
    {
      "concept_id": "C23.06",
      "concept": "Comparing mechanism classes",
      "introduction": "lesson-06",
      "practice": "C23.06-P1",
      "assessment": "C23.06-D1",
      "later_use": "lesson-07",
      "worked_example": "C23.06-W1",
      "all_required_teaching_item_ids": [
        "C23.06-E1",
        "C23.06-W1",
        "C23.06-P1",
        "C23.06-D1"
      ]
    },
    {
      "concept_id": "C23.07",
      "concept": "A map of exact and open branches",
      "introduction": "lesson-07",
      "practice": "C23.07-P1",
      "assessment": "C23.07-D1",
      "later_use": "capstone",
      "worked_example": "C23.07-W1",
      "all_required_teaching_item_ids": [
        "C23.07-E1",
        "C23.07-W1",
        "C23.07-P1",
        "C23.07-D1"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Scalar lifts and reconstructed shape",
      "entry_prerequisites": [
        "course-10",
        "course-12",
        "course-14",
        "course-17",
        "course-22"
      ],
      "concept_ids": [
        "C23.01"
      ],
      "worked_example_capability": "Trace the gravity-related scalar definitions to their source variables",
      "assessment_target": "Trace the gravity-related scalar definitions to their source variables",
      "later_use": "lesson-02",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C23.01",
        "explanation_id": "C23.01-E1",
        "bridge_to_teach": "Read the five gravity_scalar_lift formulas in S02 M19 and the missing-definition list in S03 AUD-009. Use y_ab=ln(A_ab/A_ref), etc., only as a declared classroom convention with positive areas and common A_ref. The displayed inverse algebra implies F=y_ac-y_bc and M=y_bc-y_ab; label these inferred coordinate formulas, not recovered archival definitions of F or M.",
        "worked_example": {
          "id": "C23.01-W1",
          "task_and_answer": "With y=(0,2,3), derived F=-1, M=3, G=9*0+8*2-11*3=-17. Substitution into the displayed inverse gives y_ab=(-17+8+9)/6=0, y_ac=(-17+2+27)/6=2, y_bc=(-17+8+27)/6=3. The inverse determinant is nonzero; the extra scalar organizes three coordinates, not a fourth independent shape variable."
        },
        "guided_practice": {
          "id": "C23.01-P1",
          "task_and_answer": "With y=(1,0,2), F=-2, M=1, G=-13. Recover (1,0,2) by the same three equations. A common log-area shift t leaves F,M unchanged and shifts G by6t, consistent with scale sensitivity. Integrating d ln Gamma2 also needs a reference/integration constant; do not invent it."
        },
        "diagnostic": {
          "id": "C23.01-D1",
          "task_and_answer": "Logs of raw dimensional areas are incomplete without reference conventions. The scalar identities do not choose a force law. F/M/Gamma2 source definition bodies remain VERIFIED_NOT_LOADED; algebraic inference does not close that retrieval task."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Supply the matrices, units and source cards locally. Period counts may expand; no untaught operation may first appear in the capstone.",
        "original_title": "Scalar lifts and reconstructed shape",
        "original_assessment_target": "Trace the gravity-related scalar definitions to their source variables",
        "original_concept_ids": [
          "C23.01"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "course-10",
          "course-12",
          "course-14",
          "course-17",
          "course-22"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Source variables and inferred scalar map",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          },
          {
            "session": 2,
            "focus": "Inverse reconstruction and missing definitions",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          }
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Reciprocal inversion identities",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C23.02"
      ],
      "worked_example_capability": "Verify a small reciprocal reconstruction with its metric",
      "assessment_target": "Verify a small reciprocal reconstruction with its metric",
      "later_use": "lesson-03",
      "core_minutes": 165,
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C23.02",
        "explanation_id": "C23.02-E1",
        "bridge_to_teach": "Supply a nonsingular basis B with length units, metric G=B^T B, integer address h and reciprocal q=B^-T h in inverse length units. Teach q dot q=h^T G^-1 h before Bragg inversion. Declare nonzero sine, positive wavelength/order, reciprocal scale sign, orientation, and the retained vector rho.",
        "worked_example": {
          "id": "C23.02-W1",
          "task_and_answer": "For B=diag(2,3,4) LU and h=(1,1,0), q=(1/2,1/3,0) LU^-1, q dot q=13/36 LU^-2, d=6/sqrt(13) LU and n_hat=(3,2,0)/sqrt(13). B^T q=h. In a separate synthetic Bragg example, m=2, wavelength=2 LU and sin(theta)=1/2 give d=4 LU. Angles30 and150 degrees both give that d and Gamma_B=ln(m/2)=0 with common length reference."
        },
        "guided_practice": {
          "id": "C23.02-P1",
          "task_and_answer": "For h=(0,0,1), the same B gives q=(0,0,1/4), d=4 LU and n_hat=(0,0,1). For Bragg m=1, wavelength=3 LU, sin(theta)=1/2 gives d=3 LU and Gamma_B=ln(1/2). With h=(1,1,0), g=0 and rho=(1/10,-1/5,0), q_observed=(3/5,2/15,0); reconstruct q_observed=3^0 B^-T h+rho."
        },
        "diagnostic": {
          "id": "C23.02-D1",
          "task_and_answer": "sin(theta)=0 is excluded for positive m*wavelength; B singular is outside inverse formulas. In q=n_hat/d, d and n_hat must come from that same q. The perturbed q example has a different d from the unperturbed metric example. A reciprocal residual is retained, not rounded to zero. Adjacent scaling d_next=3d gives delta ln(d/L_ref)=ln3."
        },
        "planned_periods": 3,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Supply the matrices, units and source cards locally. Period counts may expand; no untaught operation may first appear in the capstone.",
        "original_title": "Reciprocal inversion identities",
        "original_assessment_target": "Verify a small reciprocal reconstruction with its metric",
        "original_concept_ids": [
          "C23.02"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-01"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Reciprocal metric and roundtrip",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          },
          {
            "session": 2,
            "focus": "Synthetic Bragg and angle branches",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          },
          {
            "session": 3,
            "focus": "Retained rho, scaling and domain diagnostics",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          }
        ]
      }
    },
    {
      "id": "lesson-03",
      "title": "Geometry and proposed inertial response",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C23.03"
      ],
      "worked_example_capability": "Separate a directional kinematic calculation from a force law",
      "assessment_target": "Separate a directional kinematic calculation from a force law",
      "later_use": "lesson-04",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C23.03",
        "explanation_id": "C23.03-E1",
        "bridge_to_teach": "Define directional velocity v dot n and acceleration a dot n with a unit normal and declared units. A kinematic projection describes motion. An inertial or force response requires a separately specified constitutive equation, mass parameters and initial/boundary conditions.",
        "worked_example": {
          "id": "C23.03-W1",
          "task_and_answer": "Take n=(0,0,1), v=(1,2,3) LU/T and a=(0,0,-2) LU/T^2. The projections are3 LU/T and -2 LU/T^2. Reversing n changes both signs; squared projections are invariant. These calculations supply no force coefficient."
        },
        "guided_practice": {
          "id": "C23.03-P1",
          "task_and_answer": "For n=(3/5,4/5,0), v=(5,0,0) LU/T and a=(0,5,0) LU/T^2, projections are3 LU/T and4 LU/T^2. Check n dot n=1. If an explicitly proposed law supplies F_parallel=mu*a_parallel and mu=2 mass units, the conditional force is8 mass*LU/T^2; mark mu and the law as added premises."
        },
        "diagnostic": {
          "id": "C23.03-D1",
          "task_and_answer": "A dimensionless scalar lift cannot be called a dimensional force without the missing conversion and law. Preserve orientation, signed components, perpendicular motion and any proposed constitutive residual."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Supply the matrices, units and source cards locally. Period counts may expand; no untaught operation may first appear in the capstone.",
        "original_title": "Geometry and proposed inertial response",
        "original_assessment_target": "Separate a directional kinematic calculation from a force law",
        "original_concept_ids": [
          "C23.03"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-02"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Kinematic projections and conditional force premise",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          }
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "Cycle counts and exceptional dimensions",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C23.04"
      ],
      "worked_example_capability": "Recompute finite counts before comparing named algebraic structures",
      "assessment_target": "Recompute finite counts before comparing named algebraic structures",
      "later_use": "lesson-05",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C23.04",
        "explanation_id": "C23.04-E1",
        "bridge_to_teach": "Build the graph before naming an algebra: vertices (i,j,k) with coordinates0,1,2 and one-coordinate nearest-neighbor edges. A connected graph has cycle dimension E-V+1; teach a spanning tree as V-1 independent edges. For the periodic graph add wrap edges with the same edge convention.",
        "worked_example": {
          "id": "C23.04-W1",
          "task_and_answer": "Open P3 cubed: V=27, E=3*2*3^2=54, cycle dimension54-27+1=28. Periodic graph: E=81 and cycle dimension55, adding27=24+3. Source M19 records55=52+3 with global windings. Direct counting verifies the numbers; a specified sector decomposition is an additional source construction."
        },
        "guided_practice": {
          "id": "C23.04-P1",
          "task_and_answer": "For the two-dimensional open3x3 grid, V=9,E=12, cycle dimension4; periodic E=18 gives10. Given the source theorem dim H^2((Z3)^3,Z3)=6, count3^6=729 classes. State that this arithmetic uses, rather than proves, the cohomology dimension theorem."
        },
        "diagnostic": {
          "id": "C23.04-D1",
          "task_and_answer": "52 matching the dimension of F4 does not specify an action. Keep the source SU(3) octonion-stabilizer and compact F4/Albert-algebra statements as source/theorem cards; finite graph enumeration is not their proof. E6/E7 real-form choices remain extensions."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Supply the matrices, units and source cards locally. Period counts may expand; no untaught operation may first appear in the capstone.",
        "original_title": "Cycle counts and exceptional dimensions",
        "original_assessment_target": "Recompute finite counts before comparing named algebraic structures",
        "original_concept_ids": [
          "C23.04"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-03"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Open/periodic graph enumeration",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          },
          {
            "session": 2,
            "focus": "Source cohomology and exceptional counts",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          }
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "An action needs more than a matching dimension",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C23.05"
      ],
      "worked_example_capability": "Identify the map needed to connect a cycle sector to an algebra action",
      "assessment_target": "Identify the map needed to connect a cycle sector to an algebra action",
      "later_use": "lesson-06",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C23.05",
        "explanation_id": "C23.05-E1",
        "bridge_to_teach": "An action gives operators for each group element or Lie algebra generator and their relations. An intertwiner T obeys T rho(g)=sigma(g) T (or the generator version). Show an actual 2x2 example before requesting a missing map on the52-cycle sector. Domain, field, basis, bracket and normalization matter.",
        "worked_example": {
          "id": "C23.05-W1",
          "task_and_answer": "rho=diag(1,-1), sigma=diag(-1,1), T=[[0,1],[1,0]]. Both actions represent an involution, T is invertible and T rho=sigma T. Multiplying T by2 gives another intertwiner, so existence does not select a canonical one."
        },
        "guided_practice": {
          "id": "C23.05-P1",
          "task_and_answer": "rho=diag(1,-1), sigma=-I have dimension2 but traces0 and -2, so cannot be conjugate. A proposed identity T=I for the first pair fails: rho-sigma=diag(2,-2). Retain the nonzero defect matrix. For a proposed Lie action, the required defect is [R(X),R(Y)]-R([X,Y]) for each generating relation."
        },
        "diagnostic": {
          "id": "C23.05-D1",
          "task_and_answer": "A table of equal dimensions does not give operators, preserve brackets or select a real form. List these as missing construction inputs for the specific F4 action, E6/E7 selection and physical cohomology coupling; do not invent a52x52 source action."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Supply the matrices, units and source cards locally. Period counts may expand; no untaught operation may first appear in the capstone.",
        "original_title": "An action needs more than a matching dimension",
        "original_assessment_target": "Identify the map needed to connect a cycle sector to an algebra action",
        "original_concept_ids": [
          "C23.05"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-04"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Explicit small action and intertwiner",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          },
          {
            "session": 2,
            "focus": "Failed intertwiner and missing exceptional action",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          }
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "Comparing mechanism classes",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C23.06"
      ],
      "worked_example_capability": "Compare mechanisms by predictions, invariants, and required inputs",
      "assessment_target": "Compare mechanisms by predictions, invariants, and required inputs",
      "later_use": "lesson-07",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C23.06",
        "explanation_id": "C23.06-E1",
        "bridge_to_teach": "Compare explicit sufficient mechanism classes by shared observables, independent inputs, invariants and discriminating predictions. Use separately synthetic response laws as an exercise; do not present them as source laws or measured effects. Freeze parameters on one declared case before predicting another and retain the entire residual ledger.",
        "worked_example": {
          "id": "C23.06-W1",
          "task_and_answer": "Let a toy signed scalar response z be measured in U, and kinematic w=v dot n in LU/T. Hypothesis H1 predicts z=k*w, with k in U*T/LU; H2 predicts z=b*w^2, with b in U*T^2/LU^2. Set synthetic calibration w=1 LU/T,z=2U, giving k=2 and b=2 in their units. At w=-1, H1 predicts-2U while H2 predicts+2U; at w=2 they predict4U and8U. Reversal distinguishes odd from even response."
        },
        "guided_practice": {
          "id": "C23.06-P1",
          "task_and_answer": "Synthetic check cases w=(-1,2), z=(-2,5) give H1 predictions(-2,4), residuals(0,1)U; H2 predictions(2,8), residuals(-4,-3)U. Neither replaces the input list with a score. A falsifiable extension proposes fixed k and odd reversal across new held orientations; failure is recorded as an orientation-resolved residual and motivates a specified extension."
        },
        "diagnostic": {
          "id": "C23.06-D1",
          "task_and_answer": "Fitting a free parameter afresh on each test case removes the claimed forward test. A mechanism is sufficient only for its stated scope and inputs. Neither toy law yet accounts for mass reconstruction, binding or exceptional actions; list those unresolved bridges instead of asserting unification."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Supply the matrices, units and source cards locally. Period counts may expand; no untaught operation may first appear in the capstone.",
        "original_title": "Comparing mechanism classes",
        "original_assessment_target": "Compare mechanisms by predictions, invariants, and required inputs",
        "original_concept_ids": [
          "C23.06"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Mechanism inputs and frozen predictions",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          },
          {
            "session": 2,
            "focus": "Complete residual table and falsifiable extension",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          }
        ]
      }
    },
    {
      "id": "lesson-07",
      "title": "A map of exact and open branches",
      "entry_prerequisites": [
        "lesson-06"
      ],
      "concept_ids": [
        "C23.07"
      ],
      "worked_example_capability": "Preserve the archived constructions, unconstructed extensions, and residual questions",
      "assessment_target": "Preserve the archived constructions, unconstructed extensions, and residual questions",
      "later_use": "capstone",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-07",
        "concept_id": "C23.07",
        "explanation_id": "C23.07-E1",
        "bridge_to_teach": "Build an atlas with separate columns for archived claims, freshly verified finite identities, conditional predictions, missing replay definitions and unconstructed extensions. Include pointers and complete dependency boundaries. M19 requires M07,M08,M10,M13,M18; it is not a premise of the M01–M18 core closure.",
        "worked_example": {
          "id": "C23.07-W1",
          "task_and_answer": "Enter M19 scalar inverse as a checked conditional algebraic reconstruction; F/M/Gamma2 bodies as AUD-009 missing definitions; reciprocal inversion as domain-limited identities with rho retained; graph counts as finite checks; cohomology dimension and exceptional carrier statements as source theorems. Enter specific F4 action, E6/E7 real-form selection and physical cohomology coupling as unconstructed extensions."
        },
        "guided_practice": {
          "id": "C23.07-P1",
          "task_and_answer": "Assemble the practice reconstruction from lesson02, the H1/H2 signed residual table from lesson06 and its frozen-parameter reversal proposal. For every entry supply source pointer or synthetic definition, units, domain, retained information and the next missing map or test. Include a null-boundary check: a source endpoint cannot erase a constituent limitation (S03 AUD-010)."
        },
        "diagnostic": {
          "id": "C23.07-D1",
          "task_and_answer": "Do not promote a source theorem card to a freshly replayed proof or a proposed mechanism to an observation. Keeping missing definitions visible is compatible with preserving the source frozen claim; report VERIFIED_NOT_LOADED without inventing a downgrade or a completed force law."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Supply the matrices, units and source cards locally. Period counts may expand; no untaught operation may first appear in the capstone.",
        "original_title": "A map of exact and open branches",
        "original_assessment_target": "Preserve the archived constructions, unconstructed extensions, and residual questions",
        "original_concept_ids": [
          "C23.07"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-06"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Source/finite/conditional/open branch atlas",
            "minutes": 55,
            "recovery_checkpoint": "Learner reproduces the named worked operation, completes the corresponding answered practice and explains the diagnostic before advancing. If not, reteach within an added session and update dependent links."
          }
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Produce a branch atlas with one verified reconstruction, one sufficient-mechanism comparison, and one falsifiable extension proposal.",
    "required_operations": [
      "Trace the gravity-related scalar definitions to their source variables",
      "Verify a small reciprocal reconstruction with its metric",
      "Separate a directional kinematic calculation from a force law",
      "Recompute finite counts before comparing named algebraic structures",
      "Identify the map needed to connect a cycle sector to an algebra action",
      "Compare mechanisms by predictions, invariants, and required inputs",
      "Preserve the archived constructions, unconstructed extensions, and residual questions"
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C23-CAP-01",
        "operation": "Trace the gravity-related scalar definitions to their source variables",
        "introduction": "lesson-01",
        "explanation_id": "C23.01-E1",
        "worked_example_id": "C23.01-W1",
        "prior_practice_id": "C23.01-P1",
        "diagnostic_id": "C23.01-D1",
        "assessment_task": "Apply the explicitly taught practice packet, retaining all inputs, signed components, units and source status.",
        "answer_key": "With y=(1,0,2), F=-2, M=1, G=-13. Recover (1,0,2) by the same three equations. A common log-area shift t leaves F,M unchanged and shifts G by6t, consistent with scale sensitivity. Integrating d ln Gamma2 also needs a reference/integration constant; do not invent it.",
        "points": 4,
        "rubric": {
          "declared_inputs_and_scope": 1,
          "correct_operation": 1,
          "complete_reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C23-CAP-02",
        "operation": "Verify a small reciprocal reconstruction with its metric",
        "introduction": "lesson-02",
        "explanation_id": "C23.02-E1",
        "worked_example_id": "C23.02-W1",
        "prior_practice_id": "C23.02-P1",
        "diagnostic_id": "C23.02-D1",
        "assessment_task": "Apply the explicitly taught practice packet, retaining all inputs, signed components, units and source status.",
        "answer_key": "For h=(0,0,1), the same B gives q=(0,0,1/4), d=4 LU and n_hat=(0,0,1). For Bragg m=1, wavelength=3 LU, sin(theta)=1/2 gives d=3 LU and Gamma_B=ln(1/2). With h=(1,1,0), g=0 and rho=(1/10,-1/5,0), q_observed=(3/5,2/15,0); reconstruct q_observed=3^0 B^-T h+rho.",
        "points": 4,
        "rubric": {
          "declared_inputs_and_scope": 1,
          "correct_operation": 1,
          "complete_reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C23-CAP-03",
        "operation": "Separate a directional kinematic calculation from a force law",
        "introduction": "lesson-03",
        "explanation_id": "C23.03-E1",
        "worked_example_id": "C23.03-W1",
        "prior_practice_id": "C23.03-P1",
        "diagnostic_id": "C23.03-D1",
        "assessment_task": "Apply the explicitly taught practice packet, retaining all inputs, signed components, units and source status.",
        "answer_key": "For n=(3/5,4/5,0), v=(5,0,0) LU/T and a=(0,5,0) LU/T^2, projections are3 LU/T and4 LU/T^2. Check n dot n=1. If an explicitly proposed law supplies F_parallel=mu*a_parallel and mu=2 mass units, the conditional force is8 mass*LU/T^2; mark mu and the law as added premises.",
        "points": 4,
        "rubric": {
          "declared_inputs_and_scope": 1,
          "correct_operation": 1,
          "complete_reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C23-CAP-04",
        "operation": "Recompute finite counts before comparing named algebraic structures",
        "introduction": "lesson-04",
        "explanation_id": "C23.04-E1",
        "worked_example_id": "C23.04-W1",
        "prior_practice_id": "C23.04-P1",
        "diagnostic_id": "C23.04-D1",
        "assessment_task": "Apply the explicitly taught practice packet, retaining all inputs, signed components, units and source status.",
        "answer_key": "For the two-dimensional open3x3 grid, V=9,E=12, cycle dimension4; periodic E=18 gives10. Given the source theorem dim H^2((Z3)^3,Z3)=6, count3^6=729 classes. State that this arithmetic uses, rather than proves, the cohomology dimension theorem.",
        "points": 4,
        "rubric": {
          "declared_inputs_and_scope": 1,
          "correct_operation": 1,
          "complete_reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C23-CAP-05",
        "operation": "Identify the map needed to connect a cycle sector to an algebra action",
        "introduction": "lesson-05",
        "explanation_id": "C23.05-E1",
        "worked_example_id": "C23.05-W1",
        "prior_practice_id": "C23.05-P1",
        "diagnostic_id": "C23.05-D1",
        "assessment_task": "Apply the explicitly taught practice packet, retaining all inputs, signed components, units and source status.",
        "answer_key": "rho=diag(1,-1), sigma=-I have dimension2 but traces0 and -2, so cannot be conjugate. A proposed identity T=I for the first pair fails: rho-sigma=diag(2,-2). Retain the nonzero defect matrix. For a proposed Lie action, the required defect is [R(X),R(Y)]-R([X,Y]) for each generating relation.",
        "points": 4,
        "rubric": {
          "declared_inputs_and_scope": 1,
          "correct_operation": 1,
          "complete_reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C23-CAP-06",
        "operation": "Compare mechanisms by predictions, invariants, and required inputs",
        "introduction": "lesson-06",
        "explanation_id": "C23.06-E1",
        "worked_example_id": "C23.06-W1",
        "prior_practice_id": "C23.06-P1",
        "diagnostic_id": "C23.06-D1",
        "assessment_task": "Apply the explicitly taught practice packet, retaining all inputs, signed components, units and source status.",
        "answer_key": "Synthetic check cases w=(-1,2), z=(-2,5) give H1 predictions(-2,4), residuals(0,1)U; H2 predictions(2,8), residuals(-4,-3)U. Neither replaces the input list with a score. A falsifiable extension proposes fixed k and odd reversal across new held orientations; failure is recorded as an orientation-resolved residual and motivates a specified extension.",
        "points": 4,
        "rubric": {
          "declared_inputs_and_scope": 1,
          "correct_operation": 1,
          "complete_reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C23-CAP-07",
        "operation": "Preserve the archived constructions, unconstructed extensions, and residual questions",
        "introduction": "lesson-07",
        "explanation_id": "C23.07-E1",
        "worked_example_id": "C23.07-W1",
        "prior_practice_id": "C23.07-P1",
        "diagnostic_id": "C23.07-D1",
        "assessment_task": "Apply the explicitly taught practice packet, retaining all inputs, signed components, units and source status.",
        "answer_key": "Assemble the practice reconstruction from lesson02, the H1/H2 signed residual table from lesson06 and its frozen-parameter reversal proposal. For every entry supply source pointer or synthetic definition, units, domain, retained information and the next missing map or test. Include a null-boundary check: a source endpoint cannot erase a constituent limitation (S03 AUD-010).",
        "points": 4,
        "rubric": {
          "declared_inputs_and_scope": 1,
          "correct_operation": 1,
          "complete_reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
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
    "teaching_review_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\teaching\\launch-review-21-23.json",
    "teaching_amendment_sha256": "c4935f2e221ed2cf4e06ff554a8e3e82fcd070e91bcb4203ee973a618c31ecd3",
    "review_scope": "Blueprint clearance only. Actual lesson content and E05 links require independent final acceptance.",
    "applied_at": "2026-11-05T19:04:03.429535+00:00"
  },
  "validator": {
    "skill_relative_path": "scripts/validate_course.py",
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-23-gravity-inertia-and-exceptional-branches' --json"
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
  "applied_audit_amendments": {},
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
    "created_utc": "2026-11-05T19:03:09.929773+00:00",
    "scope": "Portable teaching BLUEPRINT amendments only; no completed-course acceptance.",
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
    "verification_record": "C:\\Users\\info\\Documents\\Codex\\2026-11-05\\kfield-teaching-auditor\\outputs\\teaching-verification-21-23.json",
    "verification_sha256": "1ba86ca04e3a91c21fca60a9da6901f26f1d0bd45ed513aaafc65cce59d8103c",
    "source_or_project_files_modified": false,
    "course_amendment": {
      "course_id": "course-23",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-23-gravity-inertia-and-exceptional-branches\\input-contract.json",
      "input_contract_sha256": "d7c81a2497f4c6cdcd79b6d680abaeef4a8aa9f6b7cae2be0a5d575c0d9e512b",
      "application": "Merge additively as teaching_amendment. Preserve all original concepts, source/educational amendments and supplemental exercises. Replace generic coverage references with these exact anchors and aliases. Parent applies; no project edit performed.",
      "applied_source_amendments_read": {},
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C23.01",
            "concept": "Scalar lifts and reconstructed shape",
            "operation": "Trace the gravity-related scalar definitions to their source variables"
          },
          {
            "concept_id": "C23.02",
            "concept": "Reciprocal inversion identities",
            "operation": "Verify a small reciprocal reconstruction with its metric"
          },
          {
            "concept_id": "C23.03",
            "concept": "Geometry and proposed inertial response",
            "operation": "Separate a directional kinematic calculation from a force law"
          },
          {
            "concept_id": "C23.04",
            "concept": "Cycle counts and exceptional dimensions",
            "operation": "Recompute finite counts before comparing named algebraic structures"
          },
          {
            "concept_id": "C23.05",
            "concept": "An action needs more than a matching dimension",
            "operation": "Identify the map needed to connect a cycle sector to an algebra action"
          },
          {
            "concept_id": "C23.06",
            "concept": "Comparing mechanism classes",
            "operation": "Compare mechanisms by predictions, invariants, and required inputs"
          },
          {
            "concept_id": "C23.07",
            "concept": "A map of exact and open branches",
            "operation": "Preserve the archived constructions, unconstructed extensions, and residual questions"
          }
        ],
        "source_modules": [
          "M19"
        ],
        "scope": "Produce a branch atlas with one verified reconstruction, one sufficient-mechanism comparison, and one falsifiable extension proposal.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Produce a branch atlas with one verified reconstruction, one sufficient-mechanism comparison, and one falsifiable extension proposal.",
        "required_operations": [
          "Trace the gravity-related scalar definitions to their source variables",
          "Verify a small reciprocal reconstruction with its metric",
          "Separate a directional kinematic calculation from a force law",
          "Recompute finite counts before comparing named algebraic structures",
          "Identify the map needed to connect a cycle sector to an algebra action",
          "Compare mechanisms by predictions, invariants, and required inputs",
          "Preserve the archived constructions, unconstructed extensions, and residual questions"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-23",
          "title": "Gravity, Inertia, and Exceptional Branches",
          "backbone_modules": [
            "M19"
          ],
          "topic_boundary": "Gravity scalar lift and reciprocal inversion; exact counts separated from exceptional-action extensions.",
          "cognitive_or_fidelity_risk": "Matching 52/78/133 counts does not construct a specified action.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "S02"
          ],
          "source_pointer": "/backbone_sequence/18",
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-23-gravity-inertia-and-exceptional-branches\\input-contract.json",
            "sha256": "3f5260ec3f6b15e4a47e54ce7753de492d03f62fd7fa230b851edb3be7b0370a",
            "lesson_count": 7
          },
          "required_amendment_ids": [],
          "source_launch_decision": "ready_for_source_scoped_drafting_with_required_gates",
          "decision_scope": "Source/coverage only; no new teaching acceptance or finished-course validation.",
          "educational_gate": [
            "E05",
            "independent_teaching_recheck"
          ]
        }
      ],
      "source_scope": {
        "primary": "S02#/backbone_sequence/18",
        "additional": [
          "S03#/findings/0",
          "S03#/findings/8",
          "S03#/findings/9",
          "S03#/findings/10"
        ],
        "dependencies": [
          "M07",
          "M08",
          "M10",
          "M13",
          "M18"
        ],
        "scalar_lift": "Displayed inverse identities are freshly checked under declared dimensionless log-area conventions. F=y_ac-y_bc and M=y_bc-y_ab are algebraically inferred here, not recovered archival definitions. Full source F/M/Gamma2 definitions and reference/integration constants remain VERIFIED_NOT_LOADED.",
        "reciprocal": "Nonsingular B, explicit metric, positive lengths/order and nonzero sine are mandatory. Same/opposite-angle branches and the full signed vector rho are preserved. Bragg examples are synthetic and conditional; adjacent scale identity is a logarithmic ratio with common units.",
        "mechanism": "Directional kinematics and scalar reconstruction do not by themselves specify a force law. Proposed response laws are explicitly synthetic and carry units, frozen calibration inputs, invariants, predictions and all signed residuals.",
        "exceptional": "Graph cycle counts are independently enumerated. H^2 dimension6, SU(3) stabilizer and compact F4/Albert statements remain attributed source/theorem results, not newly proved by counts. The specific F4 action on52 cycles, E6/E7 real-form choices and physical cohomology coupling are unconstructed extensions needing explicit operators and intertwiners.",
        "boundary": "M19 is a mixed D+E branch, not an M20/core-closure premise. Preserve constituent boundaries even when a stored branch endpoint is null."
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "Scalar lifts and reconstructed shape",
          "entry_prerequisites": [
            "course-10",
            "course-12",
            "course-14",
            "course-17",
            "course-22"
          ],
          "concept_ids": [
            "C23.01"
          ],
          "worked_example_capability": "Trace the gravity-related scalar definitions to their source variables",
          "assessment_target": "Trace the gravity-related scalar definitions to their source variables",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C23.01-E1",
          "worked_example_id": "C23.01-W1",
          "prior_practice_id": "C23.01-P1",
          "diagnostic_id": "C23.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Reciprocal inversion identities",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C23.02"
          ],
          "worked_example_capability": "Verify a small reciprocal reconstruction with its metric",
          "assessment_target": "Verify a small reciprocal reconstruction with its metric",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C23.02-E1",
          "worked_example_id": "C23.02-W1",
          "prior_practice_id": "C23.02-P1",
          "diagnostic_id": "C23.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "Geometry and proposed inertial response",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C23.03"
          ],
          "worked_example_capability": "Separate a directional kinematic calculation from a force law",
          "assessment_target": "Separate a directional kinematic calculation from a force law",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C23.03-E1",
          "worked_example_id": "C23.03-W1",
          "prior_practice_id": "C23.03-P1",
          "diagnostic_id": "C23.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "Cycle counts and exceptional dimensions",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C23.04"
          ],
          "worked_example_capability": "Recompute finite counts before comparing named algebraic structures",
          "assessment_target": "Recompute finite counts before comparing named algebraic structures",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C23.04-E1",
          "worked_example_id": "C23.04-W1",
          "prior_practice_id": "C23.04-P1",
          "diagnostic_id": "C23.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "An action needs more than a matching dimension",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C23.05"
          ],
          "worked_example_capability": "Identify the map needed to connect a cycle sector to an algebra action",
          "assessment_target": "Identify the map needed to connect a cycle sector to an algebra action",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C23.05-E1",
          "worked_example_id": "C23.05-W1",
          "prior_practice_id": "C23.05-P1",
          "diagnostic_id": "C23.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "Comparing mechanism classes",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C23.06"
          ],
          "worked_example_capability": "Compare mechanisms by predictions, invariants, and required inputs",
          "assessment_target": "Compare mechanisms by predictions, invariants, and required inputs",
          "later_use": "lesson-07",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C23.06-E1",
          "worked_example_id": "C23.06-W1",
          "prior_practice_id": "C23.06-P1",
          "diagnostic_id": "C23.06-D1"
        },
        {
          "id": "lesson-07",
          "title": "A map of exact and open branches",
          "entry_prerequisites": [
            "lesson-06"
          ],
          "concept_ids": [
            "C23.07"
          ],
          "worked_example_capability": "Preserve the archived constructions, unconstructed extensions, and residual questions",
          "assessment_target": "Preserve the archived constructions, unconstructed extensions, and residual questions",
          "later_use": "capstone",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C23.07-E1",
          "worked_example_id": "C23.07-W1",
          "prior_practice_id": "C23.07-P1",
          "diagnostic_id": "C23.07-D1"
        }
      ],
      "legacy_bridge_aliases": [],
      "core_periods": 13,
      "capstone_periods": 3,
      "period_minutes": 55,
      "capstone_total_points": 28,
      "capstone_sessions": [
        "55 minutes: assemble definitions, input ledger and source cards; carry out first reconstruction.",
        "55 minutes: complete mapped calculations and retain every residual, history or branch.",
        "55 minutes: finish source/mechanism classification, independently reconstruct and repair the report."
      ],
      "core_boundary": "Assess the explicit finite operations, answered practice and exact source-reading cards. Missing source L/W7, source scalar definition bodies and exceptional actions are retrieval/construction obligations, not silently assigned computations. Infinite operator examples use only their explicitly declared domains.",
      "prerequisite_status": "Blueprint closure checked; actual student-facing explanations, diagnostics, practice and capstone require later independent completed-course acceptance.",
      "inline_content_location": "Complete lesson anchors are in course_map[*].teaching_anchor; complete capstone mapping is in capstone_specification.backward_map below."
    },
    "completed_course_acceptance": false
  }
}
```
