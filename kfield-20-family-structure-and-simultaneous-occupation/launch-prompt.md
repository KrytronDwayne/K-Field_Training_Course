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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-20-family-structure-and-simultaneous-occupation",
  "topic": "Family Structure and Simultaneous Occupation",
  "series_course_id": "course-20",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-15",
    "Capabilities taught in course-18"
  ],
  "learning_outcomes": [
    "Compute the three source-defined lambda classes",
    "Decompose a small class into mean and retained detail",
    "Check a finite lift map and its normalization",
    "Count independent labels in a product carrier",
    "Verify the declared rank and uniform family occupancy construction",
    "Separate the mathematical projector from the premise identifying the occupied carrier",
    "State which masses and mixing coordinates are supplied or unresolved"
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
      "M16"
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
        "concept_id": "C20.01",
        "concept": "Residues modulo three",
        "operation": "Compute the three source-defined lambda classes"
      },
      {
        "concept_id": "C20.02",
        "concept": "Uniform and zero-sum sectors",
        "operation": "Decompose a small class into mean and retained detail"
      },
      {
        "concept_id": "C20.03",
        "concept": "Lifts and Fourier-style channels",
        "operation": "Check a finite lift map and its normalization"
      },
      {
        "concept_id": "C20.04",
        "concept": "Tensor products and rank multiplication",
        "operation": "Count independent labels in a product carrier"
      },
      {
        "concept_id": "C20.05",
        "concept": "The rank-48 projector",
        "operation": "Verify the declared rank and uniform family occupancy construction"
      },
      {
        "concept_id": "C20.06",
        "concept": "Selection, state, and source status",
        "operation": "Separate the mathematical projector from the premise identifying the occupied carrier"
      },
      {
        "concept_id": "C20.07",
        "concept": "Family labels and numerical properties",
        "operation": "State which masses and mixing coordinates are supplied or unresolved"
      },
      {
        "concept_id": "C20.S01",
        "concept": "Finite Weyl coordinates",
        "operation": "Introduce shift and phase matrices and trace-coordinate extraction on a small supplied matrix; keep coefficient choice distinct from the basis decomposition."
      },
      {
        "concept_id": "C20.S02",
        "concept": "Schur elimination and reconstruction",
        "operation": "Solve a two-block scalar example, reconstruct the eliminated variable, and preserve the E=0 branch instead of applying an inverse there."
      }
    ],
    "source_modules": [
      "M16"
    ],
    "scope": "Build a fully typed family-projector accounting table and trace its occupation conclusion to the actual source premises.",
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
      "concept_id": "C20.01",
      "concept": "Residues modulo three",
      "introduction": "lesson-01",
      "practice": "C20.01-P1",
      "assessment": "C20.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C20.01-W1",
      "all_required_teaching_item_ids": [
        "C20.01-E1",
        "C20.01-W1",
        "C20.01-P1",
        "C20.01-D1"
      ]
    },
    {
      "concept_id": "C20.02",
      "concept": "Uniform and zero-sum sectors",
      "introduction": "lesson-02",
      "practice": "C20.02-P1",
      "assessment": "C20.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C20.02-W1",
      "all_required_teaching_item_ids": [
        "C20.02-E1",
        "C20.02-W1",
        "C20.02-P1",
        "C20.02-D1"
      ]
    },
    {
      "concept_id": "C20.03",
      "concept": "Lifts and Fourier-style channels",
      "introduction": "lesson-03",
      "practice": "C20.03-P1",
      "assessment": "C20.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C20.03-W1",
      "all_required_teaching_item_ids": [
        "C20.03-E1",
        "C20.03-W1",
        "C20.03-P1",
        "C20.03-D1",
        "C20.S01-E1",
        "C20.S01-W1",
        "C20.S01-P1",
        "C20.S01-D1"
      ]
    },
    {
      "concept_id": "C20.04",
      "concept": "Tensor products and rank multiplication",
      "introduction": "lesson-04",
      "practice": "C20.04-P1",
      "assessment": "C20.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C20.04-W1",
      "all_required_teaching_item_ids": [
        "C20.04-E1",
        "C20.04-W1",
        "C20.04-P1",
        "C20.04-D1"
      ]
    },
    {
      "concept_id": "C20.05",
      "concept": "The rank-48 projector",
      "introduction": "lesson-05",
      "practice": "C20.05-P1",
      "assessment": "C20.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C20.05-W1",
      "all_required_teaching_item_ids": [
        "C20.05-E1",
        "C20.05-W1",
        "C20.05-P1",
        "C20.05-D1"
      ]
    },
    {
      "concept_id": "C20.06",
      "concept": "Selection, state, and source status",
      "introduction": "lesson-06",
      "practice": "C20.06-P1",
      "assessment": "C20.06-D1",
      "later_use": "lesson-07",
      "worked_example": "C20.06-W1",
      "all_required_teaching_item_ids": [
        "C20.06-E1",
        "C20.06-W1",
        "C20.06-P1",
        "C20.06-D1"
      ]
    },
    {
      "concept_id": "C20.07",
      "concept": "Family labels and numerical properties",
      "introduction": "lesson-07",
      "practice": "C20.07-P1",
      "assessment": "C20.07-D1",
      "later_use": "capstone",
      "worked_example": "C20.07-W1",
      "all_required_teaching_item_ids": [
        "C20.07-E1",
        "C20.07-W1",
        "C20.07-P1",
        "C20.07-D1",
        "C20.S02-E1",
        "C20.S02-W1",
        "C20.S02-P1",
        "C20.S02-D1"
      ]
    },
    {
      "concept_id": "C20.S01",
      "concept": "Finite Weyl coordinates",
      "introduction": "lesson-03",
      "practice": "lesson-03: worked example and guided practice",
      "assessment": "lesson-03: diagnostic checks",
      "later_use": "lesson-07",
      "source_pointers": [
        "S02#/backbone_sequence/15/weyl_basis"
      ]
    },
    {
      "concept_id": "C20.S02",
      "concept": "Schur elimination and reconstruction",
      "introduction": "lesson-07",
      "practice": "lesson-07: worked example and guided practice",
      "assessment": "lesson-07: diagnostic checks",
      "later_use": "capstone",
      "source_pointers": [
        "S02#/backbone_sequence/15/schur_interface"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Residues modulo three",
      "entry_prerequisites": [
        "course-15",
        "course-18"
      ],
      "concept_ids": [
        "C20.01"
      ],
      "worked_example_capability": "Compute the three source-defined lambda classes",
      "assessment_target": "Compute the three source-defined lambda classes",
      "later_use": "lesson-02",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C20.01",
        "explanation_id": "C20.01-E1",
        "bridge_to_teach": "Review residues modulo 3, including negatives. Define X=F3^3, lambda(x)=sum coordinates modulo 3 and classes C_r. Choose x1, x2 freely and solve x3=r-x1-x2 modulo 3.",
        "worked_example": {
          "id": "C20.01-W1",
          "task_and_answer": "lambda(2,2,2)=0; lambda(0,0,1)=1; lambda(0,0,2)=2. For r=0 and (x1, x2)=(1,2), x3=0. Nine choices of the first two coordinates give nine nodes in each class, total 27."
        },
        "guided_practice": {
          "id": "C20.01-P1",
          "task_and_answer": "For r=2 and (x1, x2)=(2,1), x3=2. For r=1 and (2,2), x3=0. Enumerate all nine pairs to recover counts 9+9+9, retaining node order."
        },
        "diagnostic": {
          "id": "C20.01-D1",
          "task_and_answer": "Three finite lambda classes do not by counting alone identify physical family occupation."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into actual senior-facing explanations,2–4 observable goals and3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Split dense sessions with links updated; period counts may expand.",
        "original_title": "Residues modulo three",
        "original_assessment_target": "Compute the three source-defined lambda classes",
        "original_concept_ids": [
          "C20.01"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "course-15",
          "course-18"
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Uniform and zero-sum sectors",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C20.02"
      ],
      "worked_example_capability": "Decompose a small class into mean and retained detail",
      "assessment_target": "Decompose a small class into mean and retained detail",
      "later_use": "lesson-03",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C20.02",
        "explanation_id": "C20.02-E1",
        "bridge_to_teach": "Normalize Phi_r=(1/3)sum delta_x over its nine class nodes. Orthogonal entries give norm 1. Teach class mean plus zero-sum detail and retain both; derive three class-constant dimensions and eight detail dimensions per class.",
        "worked_example": {
          "id": "C20.02-W1",
          "task_and_answer": "Values (1,2,3,4,5,6,7,8,9) have mean 5 and details (-4,-3,-2,-1,0,1,2,3,4). The normalized-indicator coefficient is 15, so 15 Phi_r is constant 5 on the class."
        },
        "guided_practice": {
          "id": "C20.02-P1",
          "task_and_answer": "Values (9,0,0,0,0,0,0,0,0) have mean 1 and details (8,-1,-1,-1,-1,-1,-1,-1,-1). The indicator coefficient is 3. Reconstruct all nine entries; across classes, dimensions are 3+8+8+8=27."
        },
        "diagnostic": {
          "id": "C20.02-D1",
          "task_and_answer": "Amplitude 1/9 gives indicator norm squared 1/9, not 1. Removing means without retaining their three coefficients loses reconstruction."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into actual senior-facing explanations,2–4 observable goals and3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Split dense sessions with links updated; period counts may expand.",
        "original_title": "Uniform and zero-sum sectors",
        "original_assessment_target": "Decompose a small class into mean and retained detail",
        "original_concept_ids": [
          "C20.02"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-01"
        ]
      }
    },
    {
      "id": "lesson-03",
      "title": "Lifts and Fourier-style channels",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C20.03",
        "C20.S01"
      ],
      "worked_example_capability": "Check a finite lift map and its normalization",
      "assessment_target": "Check a finite lift map and its normalization",
      "later_use": "lesson-04",
      "core_minutes": 220,
      "source_coverage_requirements": [
        {
          "concept_id": "C20.S01",
          "operation": "Introduce shift and phase matrices and trace-coordinate extraction on a small supplied matrix; keep coefficient choice distinct from the basis decomposition.",
          "source_pointers": [
            "S02#/backbone_sequence/15/weyl_basis"
          ]
        }
      ],
      "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
      "required_amendment_ids": [
        "EA-20-E07-3"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C20.03",
        "explanation_id": "C20.03-E1",
        "bridge_to_teach": "Introduce normalized lift maps and orthogonal label spaces, then finite Fourier channels with complex adjoints. Specify a synthetic nine-translation model, keeping the missing source L/P_v definitions separate. Include the Weyl supplement and rank bridge.",
        "worked_example": {
          "id": "C20.03-W1",
          "task_and_answer": "Synthetic L={(a, b,0):a, b=0,1,2}; P_v delta_x=delta_(x+v). Set V f=(1/3)sum_v P_v f tensor |v>. Orthogonal labels give V dagger V=(1/9)sum P_v dagger P_v=I27. A unit delta input gives nine amplitudes 1/3 and norm 1."
        },
        "guided_practice": {
          "id": "C20.03-P1",
          "task_and_answer": "Input 2 delta_(1,0,0) gives nine amplitudes 2/3 and norm squared 4; V dagger V restores it. Separately use F_jk=omega^(jk)/sqrt(3): F e0=(1,1,1)/sqrt(3), F e1=(1, omega, omega^2)/sqrt(3), and F dagger reverses both."
        },
        "diagnostic": {
          "id": "C20.03-D1",
          "task_and_answer": "Using 27 unitary translations with prefactor 1/3 gives norm-squared factor 3, not 1. The source all-lifts claim requires its exact L and operators; AUD-009 records missing objects. This nine-label model is explicitly a classroom analogue."
        },
        "planned_periods": 4,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into actual senior-facing explanations,2–4 observable goals and3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Split dense sessions with links updated; period counts may expand.",
        "supplemental_exercises": [
          {
            "concept_id": "C20.S01",
            "explanation_id": "C20.S01-E1",
            "worked_example_id": "C20.S01-W1",
            "prior_practice_id": "C20.S01-P1",
            "diagnostic_id": "C20.S01-D1",
            "explanation": "Define omega=(-1+i sqrt(3))/2, omega^3=1 and 1+omega+omega^2=0. With P e_j=e_(j+1 modulo 3), D=diag(1, omega, omega^2), set B_ab=D^a P^b. Teach trace and Hermitian orthogonality before extracting coefficients.",
            "worked_task_and_answer": "DP=omega PD and Tr(B_ab dagger B_cd)=3 delta_ac delta_bd. For Y=I+2P-D^2 P, y_ab=Tr(B_ab dagger Y)/3 gives y00=1, y01=2, y21=-1 and all six other coefficients zero. Rebuild Y from all nine coordinates.",
            "practice_task_and_answer": "For Y=2I+D-P^2, y00=2, y10=1, y02=-1 and all others zero. Direct Y has diagonal (3,2+omega,2+omega^2) and -1 at positions (0,1),(1,2),(2,0). Check each trace coefficient and entrywise reconstruction; retain zeros.",
            "diagnostic_task_and_answer": "A basis decomposition represents a supplied Y; it does not select physical Y. Swapping D/P order changes phases, so retain the exact basis and trace convention."
          }
        ],
        "original_title": "Lifts and Fourier-style channels",
        "original_assessment_target": "Check a finite lift map and its normalization",
        "original_concept_ids": [
          "C20.03",
          "C20.S01"
        ],
        "required_source_amendment_ids": [
          "EA-20-E07-3"
        ],
        "source_coverage_requirements": [
          {
            "concept_id": "C20.S01",
            "operation": "Introduce shift and phase matrices and trace-coordinate extraction on a small supplied matrix; keep coefficient choice distinct from the basis decomposition.",
            "source_pointers": [
              "S02#/backbone_sequence/15/weyl_basis"
            ]
          }
        ],
        "original_entry_prerequisites": [
          "lesson-02"
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "Tensor products and rank multiplication",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C20.04"
      ],
      "worked_example_capability": "Count independent labels in a product carrier",
      "assessment_target": "Count independent labels in a product carrier",
      "later_use": "lesson-05",
      "core_minutes": 110,
      "required_amendment_ids": [
        "EA-20-E07-3"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C20.04",
        "explanation_id": "C20.04-E1",
        "bridge_to_teach": "Preserve EA-20-E07-3. Teach column independence through linear equations, then distinguish carrier dimension, product-label count and projector image rank. Retain the complement of every projection.",
        "worked_example": {
          "id": "C20.04-W1",
          "task_and_answer": "C20-RANK-EX1: P=[[1/2,1/2,0],[1/2,1/2,0],[0,0,1]]. P^2=P; the first two columns coincide and the third is independent, so rank is 2 in dimension 3. P(2,0,3)=(1,1,3); complement=(1,-1,0)."
        },
        "guided_practice": {
          "id": "C20.04-P1",
          "task_and_answer": "C20-RANK-P1: P(4,2,-1)=(3,3,-1), complement=(1,-1,0), and their sum restores the input. A 2-by-3 label table has six entries. I2 tensor I3 tensor diag(1,0) acts in dimension 12 with rank 6."
        },
        "diagnostic": {
          "id": "C20.04-D1",
          "task_and_answer": "C20-RANK-D1: diag(1,0,0) has rank 1, not 3. A label count does not establish projector rank without its independent image basis."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into actual senior-facing explanations,2–4 observable goals and3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Split dense sessions with links updated; period counts may expand.",
        "legacy_required_ids": [
          "C20-RANK-EX1",
          "C20-RANK-P1",
          "C20-RANK-D1"
        ],
        "original_title": "Tensor products and rank multiplication",
        "original_assessment_target": "Count independent labels in a product carrier",
        "original_concept_ids": [
          "C20.04"
        ],
        "required_source_amendment_ids": [
          "EA-20-E07-3"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-03"
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "The rank-48 projector",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C20.05"
      ],
      "worked_example_capability": "Verify the declared rank and uniform family occupancy construction",
      "assessment_target": "Verify the declared rank and uniform family occupancy construction",
      "later_use": "lesson-06",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-20",
        "EA-20-E07-3"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C20.05",
        "explanation_id": "C20.05-E1",
        "bridge_to_teach": "State Q_n=I16 tensor I3 tensor q_n with q_n self-adjoint, idempotent and nonzero of rank 1. Build its image basis and restrict to each family label. Separate conditional rank arithmetic from the source physical-occupation claim.",
        "worked_example": {
          "id": "C20.05-W1",
          "task_and_answer": "The image basis has 16 internal choices, 3 family choices and 1 history choice: rank 48. Each family restriction has 16 internal states and one history coordinate. The stated family/history occupation label (1,1,1) is not a measured density."
        },
        "guided_practice": {
          "id": "C20.05-P1",
          "task_and_answer": "The toy I2 tensor I3 tensor q1 has rank 6, two internal states per family. Finite history q3=0 gives rank 0. A rank-2 history factor would give rank 96 in the 16-by-3 product, showing why rank(q_n)=1 matters."
        },
        "diagnostic": {
          "id": "C20.05-D1",
          "task_and_answer": "I3 makes this declared projector uniform across labels. It does not by itself prove that physical states occupy its image. Retain the SA-20 claim, guard and correction records."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into actual senior-facing explanations,2–4 observable goals and3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Split dense sessions with links updated; period counts may expand.",
        "original_title": "The rank-48 projector",
        "original_assessment_target": "Verify the declared rank and uniform family occupancy construction",
        "original_concept_ids": [
          "C20.05"
        ],
        "required_source_amendment_ids": [
          "SA-20",
          "EA-20-E07-3"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-04"
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "Selection, state, and source status",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C20.06"
      ],
      "worked_example_capability": "Separate the mathematical projector from the premise identifying the occupied carrier",
      "assessment_target": "Separate the mathematical projector from the premise identifying the occupied carrier",
      "later_use": "lesson-07",
      "core_minutes": 55,
      "required_amendment_ids": [
        "SA-20"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C20.06",
        "explanation_id": "C20.06-E1",
        "bridge_to_teach": "Read M16, KFM-F038, KFM-X033, D10.guard and S03 AUD-007 together. Separate source-local status from fresh arithmetic and record the retrieval state of the physical-carrier selection proof.",
        "worked_example": {
          "id": "C20.06-W1",
          "task_and_answer": "M16 and F038 claim exact simultaneous occupation; D10.guard states No physical occupation conclusion. AUD-007 requests the occupation-selection proof and removal of the obsolete guard if discharged. Otherwise retain VERIFIED_NOT_LOADED without automatically downgrading VERIFIED_FROZEN."
        },
        "guided_practice": {
          "id": "C20.06-P1",
          "task_and_answer": "Classify 16*3*1=48 as freshly checked conditional rank; occupation=(1,1,1) as the recorded source claim; D10 as the retained conflicting guard; and the connecting physical-carrier proof as not loaded in this review. Preserve all pointers and records."
        },
        "diagnostic": {
          "id": "C20.06-D1",
          "task_and_answer": "Rank arithmetic cannot decide which guard is obsolete or establish empirical occupation. VERIFIED_FROZEN and VERIFIED_NOT_LOADED are source-local dispositions, not new certificates issued by this course."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into actual senior-facing explanations,2–4 observable goals and3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Split dense sessions with links updated; period counts may expand.",
        "original_title": "Selection, state, and source status",
        "original_assessment_target": "Separate the mathematical projector from the premise identifying the occupied carrier",
        "original_concept_ids": [
          "C20.06"
        ],
        "required_source_amendment_ids": [
          "SA-20"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ]
      }
    },
    {
      "id": "lesson-07",
      "title": "Family labels and numerical properties",
      "entry_prerequisites": [
        "lesson-06"
      ],
      "concept_ids": [
        "C20.07",
        "C20.S02"
      ],
      "worked_example_capability": "State which masses and mixing coordinates are supplied or unresolved",
      "assessment_target": "State which masses and mixing coordinates are supplied or unresolved",
      "later_use": "capstone",
      "core_minutes": 165,
      "source_coverage_requirements": [
        {
          "concept_id": "C20.S02",
          "operation": "Solve a two-block scalar example, reconstruct the eliminated variable, and preserve the E=0 branch instead of applying an inverse there.",
          "source_pointers": [
            "S02#/backbone_sequence/15/schur_interface"
          ]
        }
      ],
      "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
      "required_amendment_ids": [
        "SA-20"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-07",
        "concept_id": "C20.07",
        "explanation_id": "C20.07-E1",
        "bridge_to_teach": "Separate family labels from numerical masses, mixing and supplied matrix coefficients. Teach block elimination with full reconstruction and an explicit E=0 branch; keep the Weyl basis separate from choosing physical coefficients.",
        "worked_example": {
          "id": "C20.07-W1",
          "task_and_answer": "A three-family carrier does not determine a Yukawa matrix. For synthetic K=[[2,1],[1,3]], s=(5,7), E=3, Schur=5/3, reduced source=8/3, u=8/5 and w=9/5. Both original equations hold; det K=5."
        },
        "guided_practice": {
          "id": "C20.07-P1",
          "task_and_answer": "K=[[3,1],[2,2]], s=(7,8) gives E=2, Schur=2, reduced source=3, u=3/2, w=5/2 and det K=4. With E=0, use K=[[1,1],[1,0]], s=(3,1): solve the original equations to get u=1, w=2 without dividing by E."
        },
        "diagnostic": {
          "id": "C20.07-D1",
          "task_and_answer": "Elimination from an intermediate equation does not authorize forgetting w. Preserve all zero Weyl coordinates, singular branches, coefficient inputs and physical-occupation premises."
        },
        "planned_periods": 3,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into actual senior-facing explanations,2–4 observable goals and3–5 answered diagnostics. Preserve original IDs and every supplemental concept. Split dense sessions with links updated; period counts may expand.",
        "supplemental_exercises": [
          {
            "concept_id": "C20.S02",
            "explanation_id": "C20.S02-E1",
            "worked_example_id": "C20.S02-W1",
            "prior_practice_id": "C20.S02-P1",
            "diagnostic_id": "C20.S02-D1",
            "explanation": "For A u+B w=sU and C u+E w=sW, invertible E permits w=E^-1(sW-Cu), Schur S=A-BE^-1C and reduced source r=sU-BE^-1sW. Solve S u=r only if its own inverse exists. Keep both original equations.",
            "worked_task_and_answer": "K=[[2,1],[1,3]], s=(5,7) gives S=5/3, r=8/3, u=8/5, w=9/5. Then 2u+w=5, u+3w=7 and det K=3*(5/3)=5.",
            "practice_task_and_answer": "K=[[3,1],[2,2]], s=(7,8) gives S=2, r=3, u=3/2, w=5/2. Then 3u+w=7,2u+2w=8 and det K=4. For E=0, K=[[1,1],[1,0]], s=(3,1), directly solve u=1, w=2; K is invertible even though E is not.",
            "diagnostic_task_and_answer": "Singular E or S falls outside the corresponding inverse formula. Retain compatibility or free coordinates, or solve the full system. Never erase w or treat division by zero as a branch solution."
          }
        ],
        "original_title": "Family labels and numerical properties",
        "original_assessment_target": "State which masses and mixing coordinates are supplied or unresolved",
        "original_concept_ids": [
          "C20.07",
          "C20.S02"
        ],
        "required_source_amendment_ids": [
          "SA-20"
        ],
        "source_coverage_requirements": [
          {
            "concept_id": "C20.S02",
            "operation": "Solve a two-block scalar example, reconstruct the eliminated variable, and preserve the E=0 branch instead of applying an inverse there.",
            "source_pointers": [
              "S02#/backbone_sequence/15/schur_interface"
            ]
          }
        ],
        "original_entry_prerequisites": [
          "lesson-06"
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Build a fully typed family-projector accounting table and trace its occupation conclusion to the actual source premises.",
    "required_operations": [
      "Enumerate the source-defined lambda classes and verify9+9+9 nodes.",
      "Normalize classindicators,decompose the practice class into mean+detail and reconstruct.",
      "Check the explicitly synthetic normalized lift and three-channel Fourier examples,distinguishing missing sourceobjects.",
      "Verify the practice EA20 projector,image/complement and small tensor rank versusdimension.",
      "Derive48 from the stated factors andtest a vanishing/rank2 history counterexample.",
      "Preserve sourceoccupation claim,D10guard,AUD007 correction and retrieval statuses in a comparison table.",
      "State which masses,mixing andcoefficients remain inputs,and solve the practice two-block system.",
      "Extract all nine practice Weyl coefficients bytrace and reconstruct the matrix,includingzero coordinates.",
      "Apply Schur elimination,reconstructw and originalequations,and solve the E=0 branch directly."
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C20-CAP-01",
        "operation": "Enumerate the source-defined lambda classes and verify9+9+9 nodes.",
        "introduction": "lesson-01",
        "explanation_id": "C20.01-E1",
        "worked_example_id": "C20.01-W1",
        "prior_practice_id": "C20.01-P1",
        "diagnostic_id": "C20.01-D1"
      },
      {
        "step_id": "C20-CAP-02",
        "operation": "Normalize classindicators,decompose the practice class into mean+detail and reconstruct.",
        "introduction": "lesson-02",
        "explanation_id": "C20.02-E1",
        "worked_example_id": "C20.02-W1",
        "prior_practice_id": "C20.02-P1",
        "diagnostic_id": "C20.02-D1"
      },
      {
        "step_id": "C20-CAP-03",
        "operation": "Check the explicitly synthetic normalized lift and three-channel Fourier examples,distinguishing missing sourceobjects.",
        "introduction": "lesson-03",
        "explanation_id": "C20.03-E1",
        "worked_example_id": "C20.03-W1",
        "prior_practice_id": "C20.03-P1",
        "diagnostic_id": "C20.03-D1"
      },
      {
        "step_id": "C20-CAP-04",
        "operation": "Verify the practice EA20 projector,image/complement and small tensor rank versusdimension.",
        "introduction": "lesson-04",
        "explanation_id": "C20.04-E1",
        "worked_example_id": "C20.04-W1",
        "prior_practice_id": "C20.04-P1",
        "diagnostic_id": "C20.04-D1"
      },
      {
        "step_id": "C20-CAP-05",
        "operation": "Derive48 from the stated factors andtest a vanishing/rank2 history counterexample.",
        "introduction": "lesson-05",
        "explanation_id": "C20.05-E1",
        "worked_example_id": "C20.05-W1",
        "prior_practice_id": "C20.05-P1",
        "diagnostic_id": "C20.05-D1"
      },
      {
        "step_id": "C20-CAP-06",
        "operation": "Preserve sourceoccupation claim,D10guard,AUD007 correction and retrieval statuses in a comparison table.",
        "introduction": "lesson-06",
        "explanation_id": "C20.06-E1",
        "worked_example_id": "C20.06-W1",
        "prior_practice_id": "C20.06-P1",
        "diagnostic_id": "C20.06-D1"
      },
      {
        "step_id": "C20-CAP-07",
        "operation": "State which masses,mixing andcoefficients remain inputs,and solve the practice two-block system.",
        "introduction": "lesson-07",
        "explanation_id": "C20.07-E1",
        "worked_example_id": "C20.07-W1",
        "prior_practice_id": "C20.07-P1",
        "diagnostic_id": "C20.07-D1"
      },
      {
        "step_id": "C20-CAP-08",
        "operation": "Extract all nine practice Weyl coefficients bytrace and reconstruct the matrix,includingzero coordinates.",
        "introduction": "lesson-03",
        "concept_id": "C20.S01",
        "explanation_id": "C20.S01-E1",
        "worked_example_id": "C20.S01-W1",
        "prior_practice_id": "C20.S01-P1",
        "diagnostic_id": "C20.S01-D1"
      },
      {
        "step_id": "C20-CAP-09",
        "operation": "Apply Schur elimination,reconstructw and originalequations,and solve the E=0 branch directly.",
        "introduction": "lesson-07",
        "concept_id": "C20.S02",
        "explanation_id": "C20.S02-E1",
        "worked_example_id": "C20.S02-W1",
        "prior_practice_id": "C20.S02-P1",
        "diagnostic_id": "C20.S02-D1"
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
    "teaching_review_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\teaching\\launch-review-17-20.json",
    "teaching_amendment_sha256": "20586b6d3d025073cdf48f90007d8f4141cadcd8a8627af48ec93419f8a10352",
    "review_scope": "Blueprint clearance only. Actual lesson content and E05 links require independent final acceptance.",
    "applied_at": "2026-11-05T18:49:31.664838+00:00"
  },
  "validator": {
    "skill_relative_path": "scripts/validate_course.py",
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-20-family-structure-and-simultaneous-occupation' --json"
  },
  "source_coverage_review": {
    "status": "required_source_additions_recorded",
    "report": "Z:/Kfield-doc-training/K-Field_Training_Course/kfield-series-20261105/audits/source-coverage/source-coverage-audit.json",
    "approval_boundary": "Source additions are blueprint requirements. Educational recheck and worked lesson verification remain pending."
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
    "SA-20": {
      "id": "SA-20",
      "course": 20,
      "finding": "source_fidelity",
      "lessons": [
        "lesson-05",
        "lesson-06",
        "lesson-07"
      ],
      "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
      "requirements": [
        "Retain the source occupation claim, D10 guard conflict and correction record together. Rank multiplication verifies the projector count; source physical-carrier identification has its own premises and retrieval state.",
        "Quote VERIFIED_FROZEN/VERIFIED_NOT_LOADED only as source-local statuses. Do not invent a missing occupation-selection proof or automatically downgrade a source merely because its body was not loaded.",
        "Keep the existing C20.S01 Weyl and C20.S02 Schur rows; E07 rank example supplements them and does not replace them."
      ],
      "source_references": [
        "S02#/proof_nodes/78",
        "S02#/proof_nodes/81",
        "S03#/findings/6"
      ],
      "status": "applied_to_blueprint_by_parent",
      "prior_application_status": "prepared_not_applied",
      "applied_at": "2026-11-05T17:02:05.375955+00:00"
    },
    "EA-20-E07-3": {
      "course": 20,
      "finding": "E07",
      "lessons": [
        "lesson-03",
        "lesson-04",
        "lesson-05"
      ],
      "required_bridge": "Define column independence and rank by explicit linear equations. Explain carrier dimension, number of product labels, and projector image rank as different counts.",
      "worked_example": {
        "id": "C20-RANK-EX1",
        "P": [
          [
            "1/2",
            "1/2",
            0
          ],
          [
            "1/2",
            "1/2",
            0
          ],
          [
            0,
            0,
            1
          ]
        ],
        "input": [
          2,
          0,
          3
        ],
        "projected": [
          1,
          1,
          3
        ],
        "retained_complement": [
          1,
          -1,
          0
        ],
        "checks": "Multiply P^2=P; identify equal first two columns and independent third, rank2 in dimension3; reconstruct input from image+complement. A separate 2-by-3 product label table has six labels and establishes no projector rank."
      },
      "practice": "C20-RANK-P1 apply P to (4,2,-1), retain (1,-1,0); C20-RANK-D1 count rank of diag(1,0,0). Actual rank48 source claim must include exact factorization, assumptions, locator, and source-reported versus freshly verified status.",
      "id": "EA-20-E07-3",
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
    "created_utc": "2026-11-05T18:44:36.579330+00:00",
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
    "verification_record": "C:\\Users\\info\\Documents\\Codex\\2026-11-05\\kfield-teaching-auditor\\outputs\\teaching-verification-17-20.json",
    "verification_sha256": "95f3b9026083e396970204003ff19e5b6ac06ee4d714f57f5af73f7bbc4026a2",
    "source_or_project_files_modified": false,
    "course_amendment": {
      "course_id": "course-20",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-20-family-structure-and-simultaneous-occupation\\input-contract.json",
      "input_contract_sha256": "86625e4e042e90445c47601ad4c787a898a80bd620be9b31b91eb3876027083c",
      "application": "Merge additively as teaching_amendment. Replace generic coverage references with exact exercise IDs. Preserve every original concept,source/educational amendment,supplemental exercise and legacy bridge ID. Parent applies; no project edit made.",
      "applied_source_amendments_read": {
        "SA-20": {
          "id": "SA-20",
          "course": 20,
          "finding": "source_fidelity",
          "lessons": [
            "lesson-05",
            "lesson-06",
            "lesson-07"
          ],
          "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
          "requirements": [
            "Retain the source occupation claim, D10 guard conflict and correction record together. Rank multiplication verifies the projector count; source physical-carrier identification has its own premises and retrieval state.",
            "Quote VERIFIED_FROZEN/VERIFIED_NOT_LOADED only as source-local statuses. Do not invent a missing occupation-selection proof or automatically downgrade a source merely because its body was not loaded.",
            "Keep the existing C20.S01 Weyl and C20.S02 Schur rows; E07 rank example supplements them and does not replace them."
          ],
          "source_references": [
            "S02#/proof_nodes/78",
            "S02#/proof_nodes/81",
            "S03#/findings/6"
          ],
          "status": "applied_to_blueprint_by_parent",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        },
        "EA-20-E07-3": {
          "course": 20,
          "finding": "E07",
          "lessons": [
            "lesson-03",
            "lesson-04",
            "lesson-05"
          ],
          "required_bridge": "Define column independence and rank by explicit linear equations. Explain carrier dimension, number of product labels, and projector image rank as different counts.",
          "worked_example": {
            "id": "C20-RANK-EX1",
            "P": [
              [
                "1/2",
                "1/2",
                0
              ],
              [
                "1/2",
                "1/2",
                0
              ],
              [
                0,
                0,
                1
              ]
            ],
            "input": [
              2,
              0,
              3
            ],
            "projected": [
              1,
              1,
              3
            ],
            "retained_complement": [
              1,
              -1,
              0
            ],
            "checks": "Multiply P^2=P; identify equal first two columns and independent third, rank2 in dimension3; reconstruct input from image+complement. A separate 2-by-3 product label table has six labels and establishes no projector rank."
          },
          "practice": "C20-RANK-P1 apply P to (4,2,-1), retain (1,-1,0); C20-RANK-D1 count rank of diag(1,0,0). Actual rank48 source claim must include exact factorization, assumptions, locator, and source-reported versus freshly verified status.",
          "id": "EA-20-E07-3",
          "status": "applied_to_blueprint_by_parent",
          "merge_action": "Attach to named lesson authoring obligations and capstone prerequisites. Actual content links remain an E05 acceptance gate.",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        }
      },
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C20.01",
            "concept": "Residues modulo three",
            "operation": "Compute the three source-defined lambda classes"
          },
          {
            "concept_id": "C20.02",
            "concept": "Uniform and zero-sum sectors",
            "operation": "Decompose a small class into mean and retained detail"
          },
          {
            "concept_id": "C20.03",
            "concept": "Lifts and Fourier-style channels",
            "operation": "Check a finite lift map and its normalization"
          },
          {
            "concept_id": "C20.04",
            "concept": "Tensor products and rank multiplication",
            "operation": "Count independent labels in a product carrier"
          },
          {
            "concept_id": "C20.05",
            "concept": "The rank-48 projector",
            "operation": "Verify the declared rank and uniform family occupancy construction"
          },
          {
            "concept_id": "C20.06",
            "concept": "Selection, state, and source status",
            "operation": "Separate the mathematical projector from the premise identifying the occupied carrier"
          },
          {
            "concept_id": "C20.07",
            "concept": "Family labels and numerical properties",
            "operation": "State which masses and mixing coordinates are supplied or unresolved"
          },
          {
            "concept_id": "C20.S01",
            "concept": "Finite Weyl coordinates",
            "operation": "Introduce shift and phase matrices and trace-coordinate extraction on a small supplied matrix; keep coefficient choice distinct from the basis decomposition."
          },
          {
            "concept_id": "C20.S02",
            "concept": "Schur elimination and reconstruction",
            "operation": "Solve a two-block scalar example, reconstruct the eliminated variable, and preserve the E=0 branch instead of applying an inverse there."
          }
        ],
        "source_modules": [
          "M16"
        ],
        "scope": "Build a fully typed family-projector accounting table and trace its occupation conclusion to the actual source premises.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Build a fully typed family-projector accounting table and trace its occupation conclusion to the actual source premises.",
        "required_operations": [
          "Compute the three source-defined lambda classes",
          "Decompose a small class into mean and retained detail",
          "Check a finite lift map and its normalization",
          "Count independent labels in a product carrier",
          "Verify the declared rank and uniform family occupancy construction",
          "Separate the mathematical projector from the premise identifying the occupied carrier",
          "State which masses and mixing coordinates are supplied or unresolved"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-20",
          "title": "Family Structure and Simultaneous Occupation",
          "backbone_modules": [
            "M16"
          ],
          "topic_boundary": "Lambda classes modulo three, normalized lifts, Weyl expansion, Schur reconstruction, rank-48 projector and occupation status.",
          "cognitive_or_fidelity_risk": "New Weyl/Schur practice increases load; split sessions as necessary.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "S02"
          ],
          "source_pointer": "/backbone_sequence/15",
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-20-family-structure-and-simultaneous-occupation\\input-contract.json",
            "sha256": "27e6903cb6ce4f0013923a080120048bb7120f16080d2fe67f1a2bb3e05a1bab",
            "lesson_count": 7
          },
          "required_amendment_ids": [
            "SA-20"
          ],
          "source_launch_decision": "ready_for_source_scoped_drafting_with_required_gates",
          "decision_scope": "Source/coverage only; no new teaching acceptance or finished-course validation.",
          "educational_gate": [
            "E05",
            "E07",
            "independent_teaching_recheck"
          ]
        }
      ],
      "source_scope": {
        "primary": "S02#/backbone_sequence/15",
        "additional": [
          "S02#/proof_nodes/78",
          "S02#/proof_nodes/81",
          "S02#/proof_operations:step_id=D10",
          "S03#/findings/6",
          "S03#/findings/8"
        ],
        "classes": "Each Cr has9 nodes; indicatoramplitude1/3 givesnorm1; classconstants3 plus3*8 details gives27. Means anddetails retained.",
        "lift_scope": "Explicit nine-translation classroom model hasorthogonal liftlabels andprefactor1/3. The source liftsetL andPv are not fully defined in the read packet; no source isometry replay is claimed. A27-unitary-label example withsameprefactor yieldsnormfactor3 and diagnoses why exactinputs matter.",
        "Weyl": "P e_j=e_(j+1mod3),D=diag(1,omega,omega^2),B_ab=D^aP^b,Tr(B_ab dagger B_cd)=3delta_ab,cd. All nine tracecoordinates,includingzeros,are retained. Basis choice doesnot choose numerical Y.",
        "Schur": "E inverse andSchur inverse each need their own domain. Retain eliminatedw,originalequations andsingularE=0 branches.",
        "occupation_records": {
          "M16": "source family_projector rank48 andoccupation(1,1,1)",
          "F038": "exact_simultaneous_family_occupation; common history projector",
          "X033": "exact_rank_48_family_projector",
          "D10_guard": "No physical occupation conclusion.",
          "AUD007": "Recover selection proof; remove obsolete guard if discharged. If body cannot be loaded,retain VERIFIED_NOT_LOADED without automatic downgrade of VERIFIED_FROZEN.",
          "this_review": "Conditional rank and finite examples freshly checked; connecting physical-carrier selection proof not loaded or invented. Source claim and conflict both retained."
        }
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "Residues modulo three",
          "entry_prerequisites": [
            "course-15",
            "course-18"
          ],
          "concept_ids": [
            "C20.01"
          ],
          "worked_example_capability": "Compute the three source-defined lambda classes",
          "assessment_target": "Compute the three source-defined lambda classes",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C20.01-E1",
          "worked_example_id": "C20.01-W1",
          "prior_practice_id": "C20.01-P1",
          "diagnostic_id": "C20.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Uniform and zero-sum sectors",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C20.02"
          ],
          "worked_example_capability": "Decompose a small class into mean and retained detail",
          "assessment_target": "Decompose a small class into mean and retained detail",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C20.02-E1",
          "worked_example_id": "C20.02-W1",
          "prior_practice_id": "C20.02-P1",
          "diagnostic_id": "C20.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "Lifts and Fourier-style channels",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C20.03",
            "C20.S01"
          ],
          "worked_example_capability": "Check a finite lift map and its normalization",
          "assessment_target": "Check a finite lift map and its normalization",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "source_coverage_requirements": [
            {
              "concept_id": "C20.S01",
              "operation": "Introduce shift and phase matrices and trace-coordinate extraction on a small supplied matrix; keep coefficient choice distinct from the basis decomposition.",
              "source_pointers": [
                "S02#/backbone_sequence/15/weyl_basis"
              ]
            }
          ],
          "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
          "required_amendment_ids": [
            "EA-20-E07-3"
          ],
          "planned_periods": 4,
          "planned_total_minutes": 220,
          "explanation_id": "C20.03-E1",
          "worked_example_id": "C20.03-W1",
          "prior_practice_id": "C20.03-P1",
          "diagnostic_id": "C20.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "Tensor products and rank multiplication",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C20.04"
          ],
          "worked_example_capability": "Count independent labels in a product carrier",
          "assessment_target": "Count independent labels in a product carrier",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "required_amendment_ids": [
            "EA-20-E07-3"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C20.04-E1",
          "worked_example_id": "C20.04-W1",
          "prior_practice_id": "C20.04-P1",
          "diagnostic_id": "C20.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "The rank-48 projector",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C20.05"
          ],
          "worked_example_capability": "Verify the declared rank and uniform family occupancy construction",
          "assessment_target": "Verify the declared rank and uniform family occupancy construction",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-20",
            "EA-20-E07-3"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C20.05-E1",
          "worked_example_id": "C20.05-W1",
          "prior_practice_id": "C20.05-P1",
          "diagnostic_id": "C20.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "Selection, state, and source status",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C20.06"
          ],
          "worked_example_capability": "Separate the mathematical projector from the premise identifying the occupied carrier",
          "assessment_target": "Separate the mathematical projector from the premise identifying the occupied carrier",
          "later_use": "lesson-07",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-20"
          ],
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C20.06-E1",
          "worked_example_id": "C20.06-W1",
          "prior_practice_id": "C20.06-P1",
          "diagnostic_id": "C20.06-D1"
        },
        {
          "id": "lesson-07",
          "title": "Family labels and numerical properties",
          "entry_prerequisites": [
            "lesson-06"
          ],
          "concept_ids": [
            "C20.07",
            "C20.S02"
          ],
          "worked_example_capability": "State which masses and mixing coordinates are supplied or unresolved",
          "assessment_target": "State which masses and mixing coordinates are supplied or unresolved",
          "later_use": "capstone",
          "core_minutes": 55,
          "source_coverage_requirements": [
            {
              "concept_id": "C20.S02",
              "operation": "Solve a two-block scalar example, reconstruct the eliminated variable, and preserve the E=0 branch instead of applying an inverse there.",
              "source_pointers": [
                "S02#/backbone_sequence/15/schur_interface"
              ]
            }
          ],
          "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
          "required_amendment_ids": [
            "SA-20"
          ],
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C20.07-E1",
          "worked_example_id": "C20.07-W1",
          "prior_practice_id": "C20.07-P1",
          "diagnostic_id": "C20.07-D1"
        }
      ],
      "core_periods": 15,
      "capstone_periods": 3,
      "period_minutes": 55,
      "core_boundary": "Assess the explicit finite operations and exact source-reading cards. No missing certificate replay,full Clifford/physical chirality proof,global determinant-line existence proof,continuum limit,or physical occupation-selection proof is silently assigned.",
      "prerequisite_status": "Blueprint closure checked; actual produced student-facing explanations,answered practice and capstone require later independent content acceptance.",
      "inline_content_location": "Complete lesson anchors are in course_map[*].teaching_anchor; complete capstone mapping is in capstone_specification.backward_map below."
    },
    "completed_course_acceptance": false
  }
}
```
