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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-04-affine-cells-reciprocal-planes-and-unique-addresses",
  "topic": "Affine Cells, Reciprocal Planes, and Unique Addresses",
  "series_course_id": "course-04",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-03"
  ],
  "learning_outcomes": [
    "Convert between an affine address and a physical point",
    "Assign boundary points using the declared half-open convention",
    "Verify a direct-reciprocal pairing in a small example",
    "Compute a normal and spacing from a reciprocal vector",
    "Demonstrate why coordinate orthogonality need not be physical orthogonality",
    "Reconstruct points and test exact boundaries without rounding ambiguity"
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
      "M02"
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
        "concept_id": "C04.01",
        "concept": "Address coordinates and physical points",
        "operation": "Convert between an affine address and a physical point"
      },
      {
        "concept_id": "C04.02",
        "concept": "Why half-open cells have one owner",
        "operation": "Assign boundary points using the declared half-open convention"
      },
      {
        "concept_id": "C04.03",
        "concept": "Reciprocal vectors as plane counters",
        "operation": "Verify a direct-reciprocal pairing in a small example"
      },
      {
        "concept_id": "C04.04",
        "concept": "Plane normals and physical spacing",
        "operation": "Compute a normal and spacing from a reciprocal vector"
      },
      {
        "concept_id": "C04.05",
        "concept": "Metric angles versus address angles",
        "operation": "Demonstrate why coordinate orthogonality need not be physical orthogonality"
      },
      {
        "concept_id": "C04.06",
        "concept": "Reconstruction and boundary checks",
        "operation": "Reconstruct points and test exact boundaries without rounding ambiguity"
      }
    ],
    "source_modules": [
      "M02"
    ],
    "scope": "Build a small cell-address atlas with boundary cases, reciprocal plane labels, and a complete reconstruction check.",
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
      "concept_id": "C04.01",
      "concept": "Address coordinates and physical points",
      "introduction": "lesson-01",
      "practice": "C04.01-P1",
      "assessment": "C04.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C04.01-W1",
      "all_required_teaching_item_ids": [
        "C04.01-W1",
        "C04.01-P1",
        "C04.01-D1"
      ]
    },
    {
      "concept_id": "C04.02",
      "concept": "Why half-open cells have one owner",
      "introduction": "lesson-02",
      "practice": "C04.02-P1",
      "assessment": "C04.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C04.02-W1",
      "all_required_teaching_item_ids": [
        "C04.02-W1",
        "C04.02-P1",
        "C04.02-D1"
      ]
    },
    {
      "concept_id": "C04.03",
      "concept": "Reciprocal vectors as plane counters",
      "introduction": "lesson-03",
      "practice": "C04.03-P1",
      "assessment": "C04.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C04.03-W1",
      "all_required_teaching_item_ids": [
        "C04.03-W1",
        "C04.03-P1",
        "C04.03-D1",
        "C04.03-W2",
        "C04.03-P2",
        "C04.03-D2"
      ]
    },
    {
      "concept_id": "C04.04",
      "concept": "Plane normals and physical spacing",
      "introduction": "lesson-04",
      "practice": "C04.04-P1",
      "assessment": "C04.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C04.04-W1",
      "all_required_teaching_item_ids": [
        "C04.04-W1",
        "C04.04-P1",
        "C04.04-D1"
      ]
    },
    {
      "concept_id": "C04.05",
      "concept": "Metric angles versus address angles",
      "introduction": "lesson-05",
      "practice": "C04.05-P1",
      "assessment": "C04.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C04.05-W1",
      "all_required_teaching_item_ids": [
        "C04.05-W1",
        "C04.05-P1",
        "C04.05-D1"
      ]
    },
    {
      "concept_id": "C04.06",
      "concept": "Reconstruction and boundary checks",
      "introduction": "lesson-06",
      "practice": "C04.06-P1",
      "assessment": "C04.06-D1",
      "later_use": "capstone",
      "worked_example": "C04.06-W1",
      "all_required_teaching_item_ids": [
        "C04.06-W1",
        "C04.06-P1",
        "C04.06-D1"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Address coordinates and physical points",
      "entry_prerequisites": [
        "course-03"
      ],
      "concept_ids": [
        "C04.01"
      ],
      "worked_example_capability": "Convert between an affine address and a physical point",
      "assessment_target": "Convert between an affine address and a physical point",
      "later_use": "lesson-02",
      "core_minutes": 55,
      "required_amendment_ids": [
        "SA-04"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C04.01",
        "bridge_to_teach": "Review column multiplication, subtracting an origin, and inverse action; distinguish physical length units from dimensionless addresses.",
        "worked_example": {
          "id": "C04.01-W1",
          "task_and_answer": "Use synthetic B and O. q=(1/2,-1/2,1) gives x=(2,-2,1). Recover q=B^-1(x-O)."
        },
        "guided_practice": {
          "id": "C04.01-P1",
          "task_and_answer": "q=(1,0,-1) gives x=(3,-1,7); subtract O then invert to recover q."
        },
        "diagnostic": {
          "id": "C04.01-D1",
          "task_and_answer": "x=O gives q=0, not B^-1 O. Explain why the origin must be subtracted."
        },
        "pacing_minutes": {
          "explain_and_work": 20,
          "guided_practice": 15,
          "diagnostics_and_feedback": 15,
          "transition": 5
        },
        "production_rule": "Expand this anchor diagnostic to 3–5 diagnostic checks; teach all operations before use. Split the lesson if these activities exceed 55 minutes."
      }
    },
    {
      "id": "lesson-02",
      "title": "Why half-open cells have one owner",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C04.02"
      ],
      "worked_example_capability": "Assign boundary points using the declared half-open convention",
      "assessment_target": "Assign boundary points using the declared half-open convention",
      "later_use": "lesson-03",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C04.02",
        "bridge_to_teach": "Define interval brackets and floor using a number line, including negatives. Cell ownership is a partition operation, not a generic rounding convention.",
        "worked_example": {
          "id": "C04.02-W1",
          "task_and_answer": "For q=(1/2,-1/2,3/2), z=floor(q+1/2)=(1,0,2), u=q-z=(-1/2,-1/2,-1/2)."
        },
        "guided_practice": {
          "id": "C04.02-P1",
          "task_and_answer": "q=(-3/2,49/100,51/100) gives z=(-1,0,1), u=(-1/2,49/100,-49/100)."
        },
        "diagnostic": {
          "id": "C04.02-D1",
          "task_and_answer": "q1=499/1000 has owner 0; q1=1/2 has owner 1. Do not round 499/1000 to 1/2 before assigning its owner."
        },
        "pacing_minutes": {
          "explain_and_work": 20,
          "guided_practice": 15,
          "diagnostics_and_feedback": 15,
          "transition": 5
        },
        "production_rule": "Expand this anchor diagnostic to 3–5 diagnostic checks; teach all operations before use. Split the lesson if these activities exceed 55 minutes."
      }
    },
    {
      "id": "lesson-03",
      "title": "Reciprocal vectors as plane counters",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C04.03"
      ],
      "worked_example_capability": "Verify a direct-reciprocal pairing in a small example",
      "assessment_target": "Verify a direct-reciprocal pairing in a small example",
      "later_use": "lesson-04",
      "core_minutes": 55,
      "required_amendment_ids": [
        "SA-04"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C04.03",
        "bridge_to_teach": "Define reciprocal vectors by their three dot pairings, then introduce B^-T. Teach h as an integer plane label; all affine equations use x-O.",
        "worked_example": {
          "id": "C04.03-W1",
          "task_and_answer": "h=(1,0,0) gives g=(1,-1/2,0) in inverse length units. Pairing with columns a,b,c is (1,0,0)."
        },
        "guided_practice": {
          "id": "C04.03-P1",
          "task_and_answer": "h=(0,1,0) gives g=(0,1/2,0), pairings (0,1,0). For q=(1/2,-1/2,1), g dot (x-O)=-1/2."
        },
        "diagnostic": {
          "id": "C04.03-D1",
          "task_and_answer": "h=(1,1,0) gives g=(1,0,0). Verify g dot (x-O)=h dot q=0 for the worked point, whereas g dot x=2."
        },
        "pacing_minutes": {
          "explain_and_work": 20,
          "guided_practice": 15,
          "diagnostics_and_feedback": 15,
          "transition": 5
        },
        "production_rule": "Expand this anchor diagnostic to 3–5 diagnostic checks; teach all operations before use. Split the lesson if these activities exceed 55 minutes.",
        "source_reading_check": {
          "worked_id": "C04.03-W2",
          "practice_id": "C04.03-P2",
          "diagnostic_id": "C04.03-D2",
          "worked": "Read canonical u/v/w spacings and normals from S02 /backbone_sequence/1/result or /mature_locked_cell3. Keep axis order, nm units, full lexemes and source pointer.",
          "practice": "Compare one canonical spacing with the explicitly superseded /reciprocal_witness field using S03 /findings/4. Record branch identity; do not label a superseded value as a measurement residual.",
          "diagnostic": "Reject a proposed card mixing a canonical normal and a stale spacing; name the canonical field to use.",
          "restriction": "h must be nonzero; h=0 has no unit normal or finite plane spacing. This check is source-reading, not hand computation of locked decimals."
        }
      }
    },
    {
      "id": "lesson-04",
      "title": "Plane normals and physical spacing",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C04.04"
      ],
      "worked_example_capability": "Compute a normal and spacing from a reciprocal vector",
      "assessment_target": "Compute a normal and spacing from a reciprocal vector",
      "later_use": "lesson-05",
      "core_minutes": 55,
      "required_amendment_ids": [
        "SA-04"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C04.04",
        "bridge_to_teach": "Teach magnitude, unit normalization and projection distance explicitly. Explain why increasing the integer plane level by one changes signed distance by 1/|g|.",
        "worked_example": {
          "id": "C04.04-W1",
          "task_and_answer": "For h=(1,0,0), |g|=sqrt(5)/2, unit normal=(2,-1,0)/sqrt(5), spacing=2/sqrt(5) length units."
        },
        "guided_practice": {
          "id": "C04.04-P1",
          "task_and_answer": "h=(0,1,0) gives normal=(0,1,0), spacing=2. h=(0,0,1) gives normal=(0,0,-1), spacing=3."
        },
        "diagnostic": {
          "id": "C04.04-D1",
          "task_and_answer": "Replace h by (2,0,0): g doubles, normal stays the same, spacing for consecutive integer levels halves to 1/sqrt(5). Explain the changed plane family."
        },
        "pacing_minutes": {
          "explain_and_work": 20,
          "guided_practice": 15,
          "diagnostics_and_feedback": 15,
          "transition": 5
        },
        "production_rule": "Expand this anchor diagnostic to 3–5 diagnostic checks; teach all operations before use. Split the lesson if these activities exceed 55 minutes."
      }
    },
    {
      "id": "lesson-05",
      "title": "Metric angles versus address angles",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C04.05"
      ],
      "worked_example_capability": "Demonstrate why coordinate orthogonality need not be physical orthogonality",
      "assessment_target": "Demonstrate why coordinate orthogonality need not be physical orthogonality",
      "later_use": "lesson-06",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C04.05",
        "bridge_to_teach": "Use the already taught Gram form to compare address dot products with physical dot products; an inverse cosine is optional, not required.",
        "worked_example": {
          "id": "C04.05-W1",
          "task_and_answer": "Address e1 dot e2=0, but physical a dot b=1 and cos(angle)=1/sqrt(5). The physical directions are not perpendicular."
        },
        "guided_practice": {
          "id": "C04.05-P1",
          "task_and_answer": "a dot c=0 and b dot c=0. Verify these using both physical components and entries of the Gram matrix."
        },
        "diagnostic": {
          "id": "C04.05-D1",
          "task_and_answer": "For q=(1,1,0), |Bq|^2=8, not 1+5=6: retain the two cross terms."
        },
        "pacing_minutes": {
          "explain_and_work": 20,
          "guided_practice": 15,
          "diagnostics_and_feedback": 15,
          "transition": 5
        },
        "production_rule": "Expand this anchor diagnostic to 3–5 diagnostic checks; teach all operations before use. Split the lesson if these activities exceed 55 minutes."
      }
    },
    {
      "id": "lesson-06",
      "title": "Reconstruction and boundary checks",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C04.06"
      ],
      "worked_example_capability": "Reconstruct points and test exact boundaries without rounding ambiguity",
      "assessment_target": "Reconstruct points and test exact boundaries without rounding ambiguity",
      "later_use": "capstone",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C04.06",
        "bridge_to_teach": "Teach a typed reconstruction ledger with separate q,z,u, source values and display values; use exact fractions at boundaries.",
        "worked_example": {
          "id": "C04.06-W1",
          "task_and_answer": "Combine q=(1/2,-1/2,3/2), x=(2,-2,-1/2), z=(1,0,2), u=(-1/2,-1/2,-1/2); verify O+B(z+u)=x."
        },
        "guided_practice": {
          "id": "C04.06-P1",
          "task_and_answer": "Use q=(-3/2,49/100,51/100): x=(99/100,-1/50,247/100). Reconstruct from z,u and retain all fractions."
        },
        "diagnostic": {
          "id": "C04.06-D1",
          "task_and_answer": "For q=(499/1000,0,0), displayed q=(1/2,0,0), retain r=(-1/1000,0,0); true owner is zero. Recover the original before cell assignment."
        },
        "pacing_minutes": {
          "explain_and_work": 20,
          "guided_practice": 15,
          "diagnostics_and_feedback": 15,
          "transition": 5
        },
        "production_rule": "Expand this anchor diagnostic to 3–5 diagnostic checks; teach all operations before use. Split the lesson if these activities exceed 55 minutes."
      }
    }
  ],
  "capstone_specification": {
    "task": "Build a small cell-address atlas with boundary cases, reciprocal plane labels, and a complete reconstruction check.",
    "required_operations": [
      "Declare synthetic basis, origin and units; convert three specified points in both directions.",
      "Assign owners and local coordinates for exact negative/positive half boundaries and a near-boundary fraction.",
      "Compute reciprocal vectors and verify direct-reciprocal pairings and affine plane levels.",
      "Compute unit normals and consecutive-level spacings for the supplied h labels.",
      "Compare address perpendicularity with physical dot products, retaining cross terms.",
      "Reconstruct all points from z+u and restore displayed coordinates using retained rounding residuals.",
      "Read canonical reciprocal fields and reject stale/canonical branch mixing; declare nonzero h."
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C04-CAP-01",
        "operation": "Declare synthetic basis, origin and units; convert three specified points in both directions.",
        "introduction": "lesson-01",
        "worked_example_id": "C04.01-W1",
        "prior_practice_id": "C04.01-P1",
        "diagnostic_id": "C04.01-D1"
      },
      {
        "step_id": "C04-CAP-02",
        "operation": "Assign owners and local coordinates for exact negative/positive half boundaries and a near-boundary fraction.",
        "introduction": "lesson-02",
        "worked_example_id": "C04.02-W1",
        "prior_practice_id": "C04.02-P1",
        "diagnostic_id": "C04.02-D1"
      },
      {
        "step_id": "C04-CAP-03",
        "operation": "Compute reciprocal vectors and verify direct-reciprocal pairings and affine plane levels.",
        "introduction": "lesson-03",
        "worked_example_id": "C04.03-W1",
        "prior_practice_id": "C04.03-P1",
        "diagnostic_id": "C04.03-D1"
      },
      {
        "step_id": "C04-CAP-04",
        "operation": "Compute unit normals and consecutive-level spacings for the supplied h labels.",
        "introduction": "lesson-04",
        "worked_example_id": "C04.04-W1",
        "prior_practice_id": "C04.04-P1",
        "diagnostic_id": "C04.04-D1"
      },
      {
        "step_id": "C04-CAP-05",
        "operation": "Compare address perpendicularity with physical dot products, retaining cross terms.",
        "introduction": "lesson-05",
        "worked_example_id": "C04.05-W1",
        "prior_practice_id": "C04.05-P1",
        "diagnostic_id": "C04.05-D1"
      },
      {
        "step_id": "C04-CAP-06",
        "operation": "Reconstruct all points from z+u and restore displayed coordinates using retained rounding residuals.",
        "introduction": "lesson-06",
        "worked_example_id": "C04.06-W1",
        "prior_practice_id": "C04.06-P1",
        "diagnostic_id": "C04.06-D1"
      },
      {
        "step_id": "C04-CAP-07",
        "operation": "Read canonical reciprocal fields and reject stale/canonical branch mixing; declare nonzero h.",
        "introduction": "lesson-03",
        "worked_example_id": "C04.03-W2",
        "prior_practice_id": "C04.03-P2",
        "diagnostic_id": "C04.03-D2"
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
    "teaching_review_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\teaching\\launch-review-04-06.json",
    "teaching_amendment_sha256": "035fa9ae4259adf498078dcaccba244a1be0b7c7026cc119d3fef979cd468c3a",
    "review_scope": "Blueprint clearance only. Actual lesson content and E05 links require independent final acceptance.",
    "applied_at": "2026-11-05T17:08:19.397502+00:00"
  },
  "validator": {
    "skill_relative_path": "scripts/validate_course.py",
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-04-affine-cells-reciprocal-planes-and-unique-addresses' --json"
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
    "SA-04": {
      "id": "SA-04",
      "course": 4,
      "finding": "source_fidelity",
      "lessons": [
        "lesson-01",
        "lesson-03",
        "lesson-04"
      ],
      "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
      "requirements": [
        "Use g_h=B^-T h for nonzero integer h and planes g_h dot (x-O_K)=m. Affine origins remain explicit.",
        "Use canonical S02 /backbone_sequence/1/result or /mature_locked_cell3, not the stale /reciprocal_witness branch. Label superseded values as provenance, not measurement residuals."
      ],
      "source_references": [
        "S02#/backbone_sequence/1",
        "S03#/findings/4"
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
    "synthetic_geometry": {
      "label": "Classroom analogue, not Cell3 and not measured data",
      "basis_rows": [
        [
          1,
          1,
          0
        ],
        [
          0,
          2,
          0
        ],
        [
          0,
          0,
          -3
        ]
      ],
      "origin": [
        2,
        -1,
        4
      ],
      "units": "arbitrary length unit; q,L,h dimensionless",
      "inverse_rows": [
        [
          "1",
          "-1/2",
          "0"
        ],
        [
          "0",
          "1/2",
          "0"
        ],
        [
          "0",
          "0",
          "-1/3"
        ]
      ]
    },
    "source_interface": {
      "read_in_place": "S02 /backbone_sequence/1 and /backbone_sequence/2",
      "rules": "Use x-O or p-O in affine identities. Source auditor independently clears source constants and corrected branches. Toy constants never replace source values. Ternary bonding is reduction modulo3^d; dyadic counts refer to fixed outer3B."
    },
    "course_amendment": {
      "course_id": "course-04",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-04-affine-cells-reciprocal-planes-and-unique-addresses\\input-contract.json",
      "input_contract_sha256": "fd35c1844a413c9fc099510bf262812ede824f0e5ee53ac3f7469f3aea541178",
      "application": "Merge as teaching_amendment and replace generic coverage references with IDs below. Keep existing source invariants. Parent project is not edited by this report.",
      "applied_source_amendments_read": {
        "SA-04": {
          "id": "SA-04",
          "course": 4,
          "finding": "source_fidelity",
          "lessons": [
            "lesson-01",
            "lesson-03",
            "lesson-04"
          ],
          "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
          "requirements": [
            "Use g_h=B^-T h for nonzero integer h and planes g_h dot (x-O_K)=m. Affine origins remain explicit.",
            "Use canonical S02 /backbone_sequence/1/result or /mature_locked_cell3, not the stale /reciprocal_witness branch. Label superseded values as provenance, not measurement residuals."
          ],
          "source_references": [
            "S02#/backbone_sequence/1",
            "S03#/findings/4"
          ],
          "status": "applied_to_blueprint_by_parent",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        }
      },
      "lesson_required_amendment_ids_read": {
        "lesson-01": [
          "SA-04"
        ],
        "lesson-02": [],
        "lesson-03": [
          "SA-04"
        ],
        "lesson-04": [
          "SA-04"
        ],
        "lesson-05": [],
        "lesson-06": []
      },
      "source_amendment_merge_rule": "Preserve every applied source requirement and every lesson attachment. The teaching anchors below add scaffolding; they do not supersede source obligations.",
      "capstone_periods": 2,
      "core_periods": 6,
      "core_vs_recognition": "Only the finite operations explicitly taught here are assessed. Infinite inverse limits, complex phase exponentials and general abstract quotient proofs are recognition-only in this strand.",
      "exit_checks": [
        "C04-CAP-01",
        "C04-CAP-02",
        "C04-CAP-03",
        "C04-CAP-04",
        "C04-CAP-05",
        "C04-CAP-06",
        "C04-CAP-07"
      ],
      "inline_content_location": "Complete lesson anchors are in course_map[*].teaching_anchor; complete capstone mapping is in capstone_specification.backward_map below."
    },
    "completed_course_acceptance": false
  }
}
```
