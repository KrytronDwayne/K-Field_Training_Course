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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-17-finite-gauge-transport-and-conservative-dynamics",
  "topic": "Finite Gauge Transport and Conservative Dynamics",
  "series_course_id": "course-17",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-07",
    "Capabilities taught in course-14"
  ],
  "learning_outcomes": [
    "Apply a small link map to a state",
    "Check how a difference changes when local frames change",
    "Multiply ordered links around a small loop",
    "Verify a simple invariant loop quantity",
    "Check a rational or Cayley update under its stated hypotheses",
    "Introduce a low-dimensional metric-weighted comparison before the source matrices",
    "Identify its domain, supplied coefficients, and precision",
    "Test a conserved quantity and distinguish finite evolution from a limit theorem"
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
      "M13"
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
        "concept_id": "C17.01",
        "concept": "Link transport between local frames",
        "operation": "Apply a small link map to a state"
      },
      {
        "concept_id": "C17.02",
        "concept": "Covariant finite differences",
        "operation": "Check how a difference changes when local frames change"
      },
      {
        "concept_id": "C17.03",
        "concept": "Loops and holonomy",
        "operation": "Multiply ordered links around a small loop"
      },
      {
        "concept_id": "C17.04",
        "concept": "A finite gauge-invariant action",
        "operation": "Verify a simple invariant loop quantity"
      },
      {
        "concept_id": "C17.05",
        "concept": "Norm-preserving time steps",
        "operation": "Check a rational or Cayley update under its stated hypotheses"
      },
      {
        "concept_id": "C17.06",
        "concept": "Metric and Hodge factors",
        "operation": "Introduce a low-dimensional metric-weighted comparison before the source matrices"
      },
      {
        "concept_id": "C17.07",
        "concept": "Reading a fixed-rung certificate",
        "operation": "Identify its domain, supplied coefficients, and precision"
      },
      {
        "concept_id": "C17.08",
        "concept": "Conservation and continuum scope",
        "operation": "Test a conserved quantity and distinguish finite evolution from a limit theorem"
      }
    ],
    "source_modules": [
      "M13"
    ],
    "scope": "Build and verify a small linked-state model with a loop invariant and a conservative update, then map its objects to the source construction.",
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
      "concept_id": "C17.01",
      "concept": "Link transport between local frames",
      "introduction": "lesson-01",
      "practice": "C17.01-P1",
      "assessment": "C17.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C17.01-W1",
      "all_required_teaching_item_ids": [
        "C17.01-E1",
        "C17.01-W1",
        "C17.01-P1",
        "C17.01-D1"
      ]
    },
    {
      "concept_id": "C17.02",
      "concept": "Covariant finite differences",
      "introduction": "lesson-02",
      "practice": "C17.02-P1",
      "assessment": "C17.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C17.02-W1",
      "all_required_teaching_item_ids": [
        "C17.02-E1",
        "C17.02-W1",
        "C17.02-P1",
        "C17.02-D1"
      ]
    },
    {
      "concept_id": "C17.03",
      "concept": "Loops and holonomy",
      "introduction": "lesson-03",
      "practice": "C17.03-P1",
      "assessment": "C17.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C17.03-W1",
      "all_required_teaching_item_ids": [
        "C17.03-E1",
        "C17.03-W1",
        "C17.03-P1",
        "C17.03-D1"
      ]
    },
    {
      "concept_id": "C17.04",
      "concept": "A finite gauge-invariant action",
      "introduction": "lesson-04",
      "practice": "C17.04-P1",
      "assessment": "C17.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C17.04-W1",
      "all_required_teaching_item_ids": [
        "C17.04-E1",
        "C17.04-W1",
        "C17.04-P1",
        "C17.04-D1"
      ]
    },
    {
      "concept_id": "C17.05",
      "concept": "Norm-preserving time steps",
      "introduction": "lesson-05",
      "practice": "C17.05-P1",
      "assessment": "C17.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C17.05-W1",
      "all_required_teaching_item_ids": [
        "C17.05-E1",
        "C17.05-W1",
        "C17.05-P1",
        "C17.05-D1"
      ]
    },
    {
      "concept_id": "C17.06",
      "concept": "Metric and Hodge factors",
      "introduction": "lesson-06",
      "practice": "C17.06-P1",
      "assessment": "C17.06-D1",
      "later_use": "lesson-07",
      "worked_example": "C17.06-W1",
      "all_required_teaching_item_ids": [
        "C17.06-E1",
        "C17.06-W1",
        "C17.06-P1",
        "C17.06-D1"
      ]
    },
    {
      "concept_id": "C17.07",
      "concept": "Reading a fixed-rung certificate",
      "introduction": "lesson-07",
      "practice": "C17.07-P1",
      "assessment": "C17.07-D1",
      "later_use": "lesson-08",
      "worked_example": "C17.07-W1",
      "all_required_teaching_item_ids": [
        "C17.07-E1",
        "C17.07-W1",
        "C17.07-P1",
        "C17.07-D1"
      ]
    },
    {
      "concept_id": "C17.08",
      "concept": "Conservation and continuum scope",
      "introduction": "lesson-08",
      "practice": "C17.08-P1",
      "assessment": "C17.08-D1",
      "later_use": "capstone",
      "worked_example": "C17.08-W1",
      "all_required_teaching_item_ids": [
        "C17.08-E1",
        "C17.08-W1",
        "C17.08-P1",
        "C17.08-D1"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Link transport between local frames",
      "entry_prerequisites": [
        "course-07",
        "course-14"
      ],
      "concept_ids": [
        "C17.01"
      ],
      "worked_example_capability": "Apply a small link map to a state",
      "assessment_target": "Apply a small link map to a state",
      "later_use": "lesson-02",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C17.01",
        "explanation_id": "C17.01-E1",
        "bridge_to_teach": "Declare local complex state spaces and U_xy as a map FROM frame y TO frame x. Review adjoint/unitary inverse and exact complex multiplication before links. Distinguish changing coordinates from changing the state.",
        "worked_example": {
          "id": "C17.01-W1",
          "task_and_answer": "Scalar link U_xy=i sends psi_y=2 to2i in frame x; inverse -i restores2. A2x2 link diag(i,-i) sends(1,2) to(i,-2i), norm squared5; conjugate transpose restores input."
        },
        "guided_practice": {
          "id": "C17.01-P1",
          "task_and_answer": "U_xy=-i sends psi_y=1+i to1-i; inverse i restores1+i, norm squared2. For diag(-1, i), input(2,1) gives(-2, i), norm squared5 and inverse diag(-1,-i) restores."
        },
        "diagnostic": {
          "id": "C17.01-D1",
          "task_and_answer": "U_xy and U_yx cannot be silently exchanged. With a unitary link U_yx=U_xy dagger; it maps the other direction."
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
        "original_title": "Link transport between local frames",
        "original_assessment_target": "Apply a small link map to a state",
        "original_concept_ids": [
          "C17.01"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "course-07",
          "course-14"
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Covariant finite differences",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C17.02"
      ],
      "worked_example_capability": "Check how a difference changes when local frames change",
      "assessment_target": "Check how a difference changes when local frames change",
      "later_use": "lesson-03",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C17.02",
        "explanation_id": "C17.02-E1",
        "bridge_to_teach": "Teach the finite covariant difference d_x=psi_x-U_xy psi_y and frame rules psi_x prime=G_x psi_x, U_xy prime=G_x U_xy G_y inverse. Derive cancellation of the intermediate frame by multiplication.",
        "worked_example": {
          "id": "C17.02-W1",
          "task_and_answer": "psi_x=1, psi_y=2, U=i givesd=1-2i. WithG_x=i, G_y=-1, Uprime=1 and transformed difference2+i=i*d."
        },
        "guided_practice": {
          "id": "C17.02-P1",
          "task_and_answer": "psi_x=2, psi_y=1+i, U=-i givesd=1+i. G_x=-1, G_y=i makesUprime=1, psi_x prime=-2, psi_y prime=-1+i; dprime=-1-i=G_x*d. Retain both descriptions."
        },
        "diagnostic": {
          "id": "C17.02-D1",
          "task_and_answer": "Subtracting untransported vectors from different frames loses the declared comparison. A difference is covariant; it need not have identical components in two frames."
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
        "original_title": "Covariant finite differences",
        "original_assessment_target": "Check how a difference changes when local frames change",
        "original_concept_ids": [
          "C17.02"
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
      "title": "Loops and holonomy",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C17.03"
      ],
      "worked_example_capability": "Multiply ordered links around a small loop",
      "assessment_target": "Multiply ordered links around a small loop",
      "later_use": "lesson-04",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C17.03",
        "explanation_id": "C17.03-E1",
        "bridge_to_teach": "Define loop product with a basepoint and rightmost map acting first. For U01 U12 U20, intermediate changes cancel and the loop transforms byG0 Uloop G0 inverse. Teach noncommuting2x2 multiplication.",
        "worked_example": {
          "id": "C17.03-W1",
          "task_and_answer": "UseX=[[0,1],[1,0]], Z=diag(1,-1), U01=X, U12=Z, U20=I. LoopXZ=[[0,-1],[1,0]], whileZX=-XZ; order matters."
        },
        "guided_practice": {
          "id": "C17.03-P1",
          "task_and_answer": "Exchange linksU01=Z, U12=X, U20=I; loopZX=[[0,1],[-1,0]]. Apply to(1,0) to obtain(0,-1), compared with(0,1) fromXZ. Verify conjugation byZ sends either loop to its negative."
        },
        "diagnostic": {
          "id": "C17.03-D1",
          "task_and_answer": "The scalar loop i*1*i=-1 happens to commute, but cannot justify reordering matrix links. Record the basepoint and complete ordered product."
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
        "original_title": "Loops and holonomy",
        "original_assessment_target": "Multiply ordered links around a small loop",
        "original_concept_ids": [
          "C17.03"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-02"
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "A finite gauge-invariant action",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C17.04"
      ],
      "worked_example_capability": "Verify a simple invariant loop quantity",
      "assessment_target": "Verify a simple invariant loop quantity",
      "later_use": "lesson-05",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C17.04",
        "explanation_id": "C17.04-E1",
        "bridge_to_teach": "Define trace as diagonal sum and demonstrate trace invariance under conjugation. Use the supplied finite action term beta ReTr(I-Uloop), with positive beta and a declared action-unit normalization.",
        "worked_example": {
          "id": "C17.04-W1",
          "task_and_answer": "ForXZ, Tr(XZ)=0 and ReTr(I-XZ)=2; beta=3 action units gives6. Conjugation byZ gives-XZ with the same trace/action."
        },
        "guided_practice": {
          "id": "C17.04-P1",
          "task_and_answer": "ForZX withbeta=2 action units, action4. Scalar loop-1 withbeta=2 action units also gives4. Frame phasesG0=-1, G1=i, G2=1 change(i,1, i) links to(-1, i,-i), leaving loop-1."
        },
        "diagnostic": {
          "id": "C17.04-D1",
          "task_and_answer": "Matching one trace does not mean matching full loops. Retain the loop matrices and all coefficients; gauge-invariance is a finite algebraic property, not a measurement or continuum theorem."
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
        "original_title": "A finite gauge-invariant action",
        "original_assessment_target": "Verify a simple invariant loop quantity",
        "original_concept_ids": [
          "C17.04"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-03"
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "Norm-preserving time steps",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C17.05"
      ],
      "worked_example_capability": "Check a rational or Cayley update under its stated hypotheses",
      "assessment_target": "Check a rational or Cayley update under its stated hypotheses",
      "later_use": "lesson-06",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-17"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C17.05",
        "explanation_id": "C17.05-E1",
        "bridge_to_teach": "Review complex adjoints and norms; require Lhat=Lhat dagger, real tau_C and invertible I+i tau_C Lhat. Make tau_C Lhat dimensionless. Prove Cayley adjoint cancellation before asserting conservation; retain the inverse step.",
        "worked_example": {
          "id": "C17.05-W1",
          "task_and_answer": "Lhat=diag(1,2), tau_C=1 in compatible time units givesC=diag(-i,-3/5-4i/5). Input(1,2) maps(-i,-6/5-8i/5); norm squared5 is preserved, C dagger recovers input."
        },
        "guided_practice": {
          "id": "C17.05-P1",
          "task_and_answer": "Lhat=diag(0,2), tau_C=1/2 givesC=diag(1,-i). Input(1+i,2) maps(1+i,-2i), norm squared6; reverse withC dagger. Verify both diagonal factors have modulus1 and denominator determinant nonzero."
        },
        "diagnostic": {
          "id": "C17.05-D1",
          "task_and_answer": "If scalarLhat=i/2, tau_C=1, C=3 and norm squared scales by9; self-adjointness cannot be omitted. Do not reuse tau_C as the Hodge normalization length or archived tau_R without a declared conversion."
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
        "original_title": "Norm-preserving time steps",
        "original_assessment_target": "Check a rational or Cayley update under its stated hypotheses",
        "original_concept_ids": [
          "C17.05"
        ],
        "required_source_amendment_ids": [
          "SA-17"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-04"
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "Metric and Hodge factors",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C17.06"
      ],
      "worked_example_capability": "Introduce a low-dimensional metric-weighted comparison before the source matrices",
      "assessment_target": "Introduce a low-dimensional metric-weighted comparison before the source matrices",
      "later_use": "lesson-07",
      "core_minutes": 165,
      "required_amendment_ids": [
        "SA-17"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C17.06",
        "explanation_id": "C17.06-E1",
        "bridge_to_teach": "Begin with a metric-weighted norm diag(1,4): vector(1,1) has squared length5. Then declare3D M, R=M^-1, delta=detM=V², bivector order(12,13,23), wedge²R as2x2 minors and J=[[0,0,1],[0,-1,0],[1,0,0]].",
        "worked_example": {
          "id": "C17.06-W1",
          "task_and_answer": "Synthetic M=diag(1,4,16) LU², delta64 LU^6, R=diag(1,1/4,1/16) LU^-2. HE=delta^(1/3)R=diag(4,1,1/4); HB=delta^(2/3)wedge²R=diag(4,1,1/4). Both determinants1; J HB J^T=HE^-1."
        },
        "guided_practice": {
          "id": "C17.06-P1",
          "task_and_answer": "M=diag(4,1,16) givesHE=diag(1,4,1/4), HB=diag(4,1/4,1); J HB J^T=diag(1,1/4,4)=HE^-1. Scale M by4:delta scales64, R by1/4; HE andHB unchanged. In2D metricdiag(4,1), vector(1,2) has squared length8."
        },
        "diagnostic": {
          "id": "C17.06-D1",
          "task_and_answer": "M LU², delta LU^6, R LU^-2, wedge²R LU^-4 make both normalized blocks dimensionless. In3D det(delta^a R)=delta^(3a-1) and det(delta^b wedge²R)=delta^(3b-2); hencea=1/3, b=2/3. S01 older2/3,4/3 exponents are historical; atdelta64 their determinants64 and4096 fail normalization."
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
        "original_title": "Metric and Hodge factors",
        "original_assessment_target": "Introduce a low-dimensional metric-weighted comparison before the source matrices",
        "original_concept_ids": [
          "C17.06"
        ],
        "required_source_amendment_ids": [
          "SA-17"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ]
      }
    },
    {
      "id": "lesson-07",
      "title": "Reading a fixed-rung certificate",
      "entry_prerequisites": [
        "lesson-06"
      ],
      "concept_ids": [
        "C17.07"
      ],
      "worked_example_capability": "Identify its domain, supplied coefficients, and precision",
      "assessment_target": "Identify its domain, supplied coefficients, and precision",
      "later_use": "lesson-08",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-17"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-07",
        "concept_id": "C17.07",
        "explanation_id": "C17.07-E1",
        "bridge_to_teach": "Read the finite-rung claims as certificate-scoped source statements. Record exact compiler/rung, coefficient positivity, units, precision/interval bounds, source hash and replay-object availability. Without a full pinned certificate, assign scoped reading only, not numerical replay.",
        "worked_example": {
          "id": "C17.07-W1",
          "task_and_answer": "S02 M13 reports epsilon_E<.007744166, epsilon_B<.015868134, alpha<=.5244 and gapDelta>.10185916 H_N/tau_R. Keep strict/non-strict signs and digits. H_N action divided bytau_R time gives energy. AUD-009 names missing fixed-rung inputs; no fresh certificate replay is claimed."
        },
        "guided_practice": {
          "id": "C17.07-P1",
          "task_and_answer": "Classify a packet containing only those four numbers: source summary available; full compiler matrices, positive coefficient list, interval method, hash/replay command and domain absent. Mark replay unavailable. Separately a synthetic normalized boundd_root=3/10, c*=1/20 yieldsmin(d_root,2c*)=1/10 timesE0=H_N/tau_R; it does not reproduce the archived bound."
        },
        "diagnostic": {
          "id": "C17.07-D1",
          "task_and_answer": "Retain positive c*>0 and the fixed-compiler domain. A source-local VERIFIED_NOT_LOADED label is a retrieval/status record, not invented certification or automatic refutation. Infinite-depth operator and continuum comparisons remain separate."
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
        "original_title": "Reading a fixed-rung certificate",
        "original_assessment_target": "Identify its domain, supplied coefficients, and precision",
        "original_concept_ids": [
          "C17.07"
        ],
        "required_source_amendment_ids": [
          "SA-17"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-06"
        ]
      }
    },
    {
      "id": "lesson-08",
      "title": "Conservation and continuum scope",
      "entry_prerequisites": [
        "lesson-07"
      ],
      "concept_ids": [
        "C17.08"
      ],
      "worked_example_capability": "Test a conserved quantity and distinguish finite evolution from a limit theorem",
      "assessment_target": "Test a conserved quantity and distinguish finite evolution from a limit theorem",
      "later_use": "capstone",
      "core_minutes": 55,
      "required_amendment_ids": [
        "SA-17"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-08",
        "concept_id": "C17.08",
        "explanation_id": "C17.08-E1",
        "bridge_to_teach": "Test the exact conserved quantity of the specified finite update; distinguish unitary norm conservation from other observables and from a continuum limit. Preserve every component and any finite comparison remainder.",
        "worked_example": {
          "id": "C17.08-W1",
          "task_and_answer": "For the worked Cayley step, norm squared =5 and psi dagger Lhat psi=9 before/after because this C is a function ofLhat. The two complex amplitudes change and are retained."
        },
        "guided_practice": {
          "id": "C17.08-P1",
          "task_and_answer": "For the practice step, norm squared =6 and Lhat expectation8 before/after. Two steps give(1+i,-2), still norm squared 6; inverse steps recover the original. Repeated finite unitarity does not prove convergence to an unprovided continuum operator."
        },
        "diagnostic": {
          "id": "C17.08-D1",
          "task_and_answer": "Source thermal-detail convergence uses positive coefficients and its infinite series; the first three synthetic terms forbeta*c*=ln16 are1/16,1/32,1/1024. Finite terms illustrate but do not certify missing infinite operator-domain premises. Report finite theorem, source certificate claim and optional continuum comparison separately."
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
        "original_title": "Conservation and continuum scope",
        "original_assessment_target": "Test a conserved quantity and distinguish finite evolution from a limit theorem",
        "original_concept_ids": [
          "C17.08"
        ],
        "required_source_amendment_ids": [
          "SA-17"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-07"
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Build and verify a small linked-state model with a loop invariant and a conservative update, then map its objects to the source construction.",
    "required_operations": [
      "Apply and invert the taught link on a complex state with declared source/target frames.",
      "Compute the practice covariant difference and its transformed components, verifying dprime=Gx*d.",
      "Multiply the noncommuting practice loop in the declared order and compare reversed order.",
      "Calculate the loop action before/after the taught frame change and retain the full loop.",
      "Compute and invert the practice Cayley step,check adjoint/norm and all hypotheses.",
      "Compute the practice HE/HB blocks,determinants,duality and units; identify historical exponents.",
      "Read the archived finite-rung bound with its domains,precision and missing replay inputs; evaluate only the separately declared synthetic minimum.",
      "Verify finite norm and Lhat expectation conservation and distinguish source/continuum claims."
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C17-CAP-01",
        "operation": "Apply and invert the taught link on a complex state with declared source/target frames.",
        "introduction": "lesson-01",
        "explanation_id": "C17.01-E1",
        "worked_example_id": "C17.01-W1",
        "prior_practice_id": "C17.01-P1",
        "diagnostic_id": "C17.01-D1"
      },
      {
        "step_id": "C17-CAP-02",
        "operation": "Compute the practice covariant difference and its transformed components, verifying dprime=Gx*d.",
        "introduction": "lesson-02",
        "explanation_id": "C17.02-E1",
        "worked_example_id": "C17.02-W1",
        "prior_practice_id": "C17.02-P1",
        "diagnostic_id": "C17.02-D1"
      },
      {
        "step_id": "C17-CAP-03",
        "operation": "Multiply the noncommuting practice loop in the declared order and compare reversed order.",
        "introduction": "lesson-03",
        "explanation_id": "C17.03-E1",
        "worked_example_id": "C17.03-W1",
        "prior_practice_id": "C17.03-P1",
        "diagnostic_id": "C17.03-D1"
      },
      {
        "step_id": "C17-CAP-04",
        "operation": "Calculate the loop action before/after the taught frame change and retain the full loop.",
        "introduction": "lesson-04",
        "explanation_id": "C17.04-E1",
        "worked_example_id": "C17.04-W1",
        "prior_practice_id": "C17.04-P1",
        "diagnostic_id": "C17.04-D1"
      },
      {
        "step_id": "C17-CAP-05",
        "operation": "Compute and invert the practice Cayley step,check adjoint/norm and all hypotheses.",
        "introduction": "lesson-05",
        "explanation_id": "C17.05-E1",
        "worked_example_id": "C17.05-W1",
        "prior_practice_id": "C17.05-P1",
        "diagnostic_id": "C17.05-D1"
      },
      {
        "step_id": "C17-CAP-06",
        "operation": "Compute the practice HE/HB blocks,determinants,duality and units; identify historical exponents.",
        "introduction": "lesson-06",
        "explanation_id": "C17.06-E1",
        "worked_example_id": "C17.06-W1",
        "prior_practice_id": "C17.06-P1",
        "diagnostic_id": "C17.06-D1"
      },
      {
        "step_id": "C17-CAP-07",
        "operation": "Read the archived finite-rung bound with its domains,precision and missing replay inputs; evaluate only the separately declared synthetic minimum.",
        "introduction": "lesson-07",
        "explanation_id": "C17.07-E1",
        "worked_example_id": "C17.07-W1",
        "prior_practice_id": "C17.07-P1",
        "diagnostic_id": "C17.07-D1"
      },
      {
        "step_id": "C17-CAP-08",
        "operation": "Verify finite norm and Lhat expectation conservation and distinguish source/continuum claims.",
        "introduction": "lesson-08",
        "explanation_id": "C17.08-E1",
        "worked_example_id": "C17.08-W1",
        "prior_practice_id": "C17.08-P1",
        "diagnostic_id": "C17.08-D1"
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
    "applied_at": "2026-11-05T18:49:31.662839+00:00"
  },
  "validator": {
    "skill_relative_path": "scripts/validate_course.py",
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-17-finite-gauge-transport-and-conservative-dynamics' --json"
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
    "SA-17": {
      "id": "SA-17",
      "course": 17,
      "finding": "source_fidelity",
      "lessons": [
        "lesson-05",
        "lesson-06",
        "lesson-07",
        "lesson-08"
      ],
      "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
      "requirements": [
        "With delta=det(M_cell)=V^2, use H_E=delta^(1/3)R_cell and H_B=delta^(2/3) wedge^2 R_cell. The corrected-file older exponents remain historical.",
        "For Cayley norm preservation specify self-adjoint L_hat, real tau and inverse domain. For gap certificates preserve positive coefficient assumptions, fixed-rung inputs and time/action units.",
        "Retrieve a full pinned certificate before assigning a numerical certificate replay; otherwise teach exact scoped reading with replay inputs marked unavailable."
      ],
      "source_references": [
        "S02#/backbone_sequence/12",
        "S02#/hodge_normalization_theorem",
        "S04#/hodge_correction_proof",
        "S03#/findings/8"
      ],
      "status": "applied_to_blueprint_by_parent",
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
      "course_id": "course-17",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-17-finite-gauge-transport-and-conservative-dynamics\\input-contract.json",
      "input_contract_sha256": "f48ee46040414a6355434cec1a8fb54a820d6a35e15182e197bc688230cce30c",
      "application": "Merge additively as teaching_amendment. Replace generic coverage references with exact exercise IDs. Preserve every original concept,source/educational amendment,supplemental exercise and legacy bridge ID. Parent applies; no project edit made.",
      "applied_source_amendments_read": {
        "SA-17": {
          "id": "SA-17",
          "course": 17,
          "finding": "source_fidelity",
          "lessons": [
            "lesson-05",
            "lesson-06",
            "lesson-07",
            "lesson-08"
          ],
          "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
          "requirements": [
            "With delta=det(M_cell)=V^2, use H_E=delta^(1/3)R_cell and H_B=delta^(2/3) wedge^2 R_cell. The corrected-file older exponents remain historical.",
            "For Cayley norm preservation specify self-adjoint L_hat, real tau and inverse domain. For gap certificates preserve positive coefficient assumptions, fixed-rung inputs and time/action units.",
            "Retrieve a full pinned certificate before assigning a numerical certificate replay; otherwise teach exact scoped reading with replay inputs marked unavailable."
          ],
          "source_references": [
            "S02#/backbone_sequence/12",
            "S02#/hodge_normalization_theorem",
            "S04#/hodge_correction_proof",
            "S03#/findings/8"
          ],
          "status": "applied_to_blueprint_by_parent",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        }
      },
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C17.01",
            "concept": "Link transport between local frames",
            "operation": "Apply a small link map to a state"
          },
          {
            "concept_id": "C17.02",
            "concept": "Covariant finite differences",
            "operation": "Check how a difference changes when local frames change"
          },
          {
            "concept_id": "C17.03",
            "concept": "Loops and holonomy",
            "operation": "Multiply ordered links around a small loop"
          },
          {
            "concept_id": "C17.04",
            "concept": "A finite gauge-invariant action",
            "operation": "Verify a simple invariant loop quantity"
          },
          {
            "concept_id": "C17.05",
            "concept": "Norm-preserving time steps",
            "operation": "Check a rational or Cayley update under its stated hypotheses"
          },
          {
            "concept_id": "C17.06",
            "concept": "Metric and Hodge factors",
            "operation": "Introduce a low-dimensional metric-weighted comparison before the source matrices"
          },
          {
            "concept_id": "C17.07",
            "concept": "Reading a fixed-rung certificate",
            "operation": "Identify its domain, supplied coefficients, and precision"
          },
          {
            "concept_id": "C17.08",
            "concept": "Conservation and continuum scope",
            "operation": "Test a conserved quantity and distinguish finite evolution from a limit theorem"
          }
        ],
        "source_modules": [
          "M13"
        ],
        "scope": "Build and verify a small linked-state model with a loop invariant and a conservative update, then map its objects to the source construction.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Build and verify a small linked-state model with a loop invariant and a conservative update, then map its objects to the source construction.",
        "required_operations": [
          "Apply a small link map to a state",
          "Check how a difference changes when local frames change",
          "Multiply ordered links around a small loop",
          "Verify a simple invariant loop quantity",
          "Check a rational or Cayley update under its stated hypotheses",
          "Introduce a low-dimensional metric-weighted comparison before the source matrices",
          "Identify its domain, supplied coefficients, and precision",
          "Test a conserved quantity and distinguish finite evolution from a limit theorem"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-17",
          "title": "Finite Gauge Transport and Conservative Dynamics",
          "backbone_modules": [
            "M13"
          ],
          "topic_boundary": "Finite gauge transport, Cayley hypotheses, mature determinant-normalized Hodge blocks and finite-rung certificate domains.",
          "cognitive_or_fidelity_risk": "Use exponents 1/3 and 2/3 with delta=det(M), not S01's older exponents.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "S02"
          ],
          "source_pointer": "/backbone_sequence/12",
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-17-finite-gauge-transport-and-conservative-dynamics\\input-contract.json",
            "sha256": "4212f2c483c6e77fdf70267f69d93643a24dbb3cbab0a993a2ae4c88e4b2620b",
            "lesson_count": 8
          },
          "required_amendment_ids": [
            "SA-17"
          ],
          "source_launch_decision": "ready_for_source_scoped_drafting_with_required_gates",
          "decision_scope": "Source/coverage only; no new teaching acceptance or finished-course validation.",
          "educational_gate": [
            "E05",
            "independent_teaching_recheck"
          ]
        }
      ],
      "source_scope": {
        "primary": "S02#/backbone_sequence/12",
        "additional": [
          "S02#/hodge_normalization_theorem",
          "S04#/hodge_correction_proof",
          "S03#/findings/8"
        ],
        "Hodge_convention": "Synthetic M in LU^2,R in LU^-2,delta=det M=V^2 in LU^6. Bivectors(12,13,23); J=[[0,0,1],[0,-1,0],[1,0,0]]. HE=delta^(1/3)R,HB=delta^(2/3)wedge^2 R are dimensionless. Exponents follow requiring normalization for every positive delta,not only delta=1. This chosen J is declared for the example,not substituted for an unloaded archival convention.",
        "historical_branch": {
          "source": "S01#/backbone_sequence/12/definitions",
          "electric": "delta^(2/3)R",
          "magnetic": "delta^(4/3)wedge^2 R",
          "status": "historical exponents superseded by mature determinant-normalization correction"
        },
        "Cayley_domain": "Self-adjoint Lhat,real tau_C and invertible denominator; tau_C*Lhat dimensionless. Keep tau_C distinct from any Hodge-length symbol and source tau_R unless a conversion is explicitly supplied.",
        "certificate_scope": {
          "source_reported_bounds": {
            "epsilon_E": "<0.007744166",
            "epsilon_B": "<0.015868134",
            "alpha": "<=0.5244",
            "Delta": ">0.10185916 H_N/tau_R"
          },
          "full_pinned_replay_inputs": "not available in the read source packet",
          "assigned_operation": "source-scoped reading only; no numerical certificate replay",
          "positive_domain": "native plaquette/detail coefficients positive; c_*>0",
          "units": "H_N action,tau_R time,H_N/tau_R energy; normalized root bound distinguished from physical energy gap"
        },
        "continuum": "Finite unitary identities and source finite-compiler claims do not certify optional infinite operator-domain or continuum comparison theorems."
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "Link transport between local frames",
          "entry_prerequisites": [
            "course-07",
            "course-14"
          ],
          "concept_ids": [
            "C17.01"
          ],
          "worked_example_capability": "Apply a small link map to a state",
          "assessment_target": "Apply a small link map to a state",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C17.01-E1",
          "worked_example_id": "C17.01-W1",
          "prior_practice_id": "C17.01-P1",
          "diagnostic_id": "C17.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Covariant finite differences",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C17.02"
          ],
          "worked_example_capability": "Check how a difference changes when local frames change",
          "assessment_target": "Check how a difference changes when local frames change",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C17.02-E1",
          "worked_example_id": "C17.02-W1",
          "prior_practice_id": "C17.02-P1",
          "diagnostic_id": "C17.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "Loops and holonomy",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C17.03"
          ],
          "worked_example_capability": "Multiply ordered links around a small loop",
          "assessment_target": "Multiply ordered links around a small loop",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C17.03-E1",
          "worked_example_id": "C17.03-W1",
          "prior_practice_id": "C17.03-P1",
          "diagnostic_id": "C17.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "A finite gauge-invariant action",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C17.04"
          ],
          "worked_example_capability": "Verify a simple invariant loop quantity",
          "assessment_target": "Verify a simple invariant loop quantity",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C17.04-E1",
          "worked_example_id": "C17.04-W1",
          "prior_practice_id": "C17.04-P1",
          "diagnostic_id": "C17.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "Norm-preserving time steps",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C17.05"
          ],
          "worked_example_capability": "Check a rational or Cayley update under its stated hypotheses",
          "assessment_target": "Check a rational or Cayley update under its stated hypotheses",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-17"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C17.05-E1",
          "worked_example_id": "C17.05-W1",
          "prior_practice_id": "C17.05-P1",
          "diagnostic_id": "C17.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "Metric and Hodge factors",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C17.06"
          ],
          "worked_example_capability": "Introduce a low-dimensional metric-weighted comparison before the source matrices",
          "assessment_target": "Introduce a low-dimensional metric-weighted comparison before the source matrices",
          "later_use": "lesson-07",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-17"
          ],
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C17.06-E1",
          "worked_example_id": "C17.06-W1",
          "prior_practice_id": "C17.06-P1",
          "diagnostic_id": "C17.06-D1"
        },
        {
          "id": "lesson-07",
          "title": "Reading a fixed-rung certificate",
          "entry_prerequisites": [
            "lesson-06"
          ],
          "concept_ids": [
            "C17.07"
          ],
          "worked_example_capability": "Identify its domain, supplied coefficients, and precision",
          "assessment_target": "Identify its domain, supplied coefficients, and precision",
          "later_use": "lesson-08",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-17"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C17.07-E1",
          "worked_example_id": "C17.07-W1",
          "prior_practice_id": "C17.07-P1",
          "diagnostic_id": "C17.07-D1"
        },
        {
          "id": "lesson-08",
          "title": "Conservation and continuum scope",
          "entry_prerequisites": [
            "lesson-07"
          ],
          "concept_ids": [
            "C17.08"
          ],
          "worked_example_capability": "Test a conserved quantity and distinguish finite evolution from a limit theorem",
          "assessment_target": "Test a conserved quantity and distinguish finite evolution from a limit theorem",
          "later_use": "capstone",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-17"
          ],
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C17.08-E1",
          "worked_example_id": "C17.08-W1",
          "prior_practice_id": "C17.08-P1",
          "diagnostic_id": "C17.08-D1"
        }
      ],
      "core_periods": 13,
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
