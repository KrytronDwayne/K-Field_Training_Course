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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-13-root-systems-symmetry-and-a1-a2-structure",
  "topic": "Root Systems, Symmetry, and A1–A2 Structure",
  "series_course_id": "course-13",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-09",
    "Capabilities taught in course-11",
    "Capabilities taught in course-12"
  ],
  "learning_outcomes": [
    "Check closure and invariants in a small transformation set",
    "Derive the allowed two-side transfer and its parity quotient",
    "Draw sum-zero triples and compute their basic inner products",
    "Distinguish a root step from a weight class",
    "Separate primitive lifts, family labels, and detector parity",
    "Specify the carrier and map needed for a symmetry claim"
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
      "M09"
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
        "concept_id": "C13.01",
        "concept": "Symmetry as an operation with a rule",
        "operation": "Check closure and invariants in a small transformation set"
      },
      {
        "concept_id": "C13.02",
        "concept": "Side transfers and the A1 pattern",
        "operation": "Derive the allowed two-side transfer and its parity quotient"
      },
      {
        "concept_id": "C13.03",
        "concept": "Three channels and the A2 plane",
        "operation": "Draw sum-zero triples and compute their basic inner products"
      },
      {
        "concept_id": "C13.04",
        "concept": "Roots, weights, and quotient labels",
        "operation": "Distinguish a root step from a weight class"
      },
      {
        "concept_id": "C13.05",
        "concept": "Primitive lifts and role separation",
        "operation": "Separate primitive lifts, family labels, and detector parity"
      },
      {
        "concept_id": "C13.06",
        "concept": "From a geometric pattern to an action",
        "operation": "Specify the carrier and map needed for a symmetry claim"
      }
    ],
    "source_modules": [
      "M09"
    ],
    "scope": "Build a labeled A1/A2 transfer atlas with invariant checks and a precise account of each quotient.",
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
      "concept_id": "C13.01",
      "concept": "Symmetry as an operation with a rule",
      "introduction": "lesson-01",
      "practice": "C13.01-P1",
      "assessment": "C13.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C13.01-W1",
      "all_required_teaching_item_ids": [
        "C13.01-E1",
        "C13.01-W1",
        "C13.01-P1",
        "C13.01-D1"
      ]
    },
    {
      "concept_id": "C13.02",
      "concept": "Side transfers and the A1 pattern",
      "introduction": "lesson-02",
      "practice": "C13.02-P1",
      "assessment": "C13.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C13.02-W1",
      "all_required_teaching_item_ids": [
        "C13.02-E1",
        "C13.02-W1",
        "C13.02-P1",
        "C13.02-D1"
      ]
    },
    {
      "concept_id": "C13.03",
      "concept": "Three channels and the A2 plane",
      "introduction": "lesson-03",
      "practice": "C13.03-P1",
      "assessment": "C13.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C13.03-W1",
      "all_required_teaching_item_ids": [
        "C13.03-E1",
        "C13.03-W1",
        "C13.03-P1",
        "C13.03-D1"
      ]
    },
    {
      "concept_id": "C13.04",
      "concept": "Roots, weights, and quotient labels",
      "introduction": "lesson-04",
      "practice": "C13.04-P1",
      "assessment": "C13.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C13.04-W1",
      "all_required_teaching_item_ids": [
        "C13.04-E1",
        "C13.04-W1",
        "C13.04-P1",
        "C13.04-D1"
      ]
    },
    {
      "concept_id": "C13.05",
      "concept": "Primitive lifts and role separation",
      "introduction": "lesson-05",
      "practice": "C13.05-P1",
      "assessment": "C13.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C13.05-W1",
      "all_required_teaching_item_ids": [
        "C13.05-E1",
        "C13.05-W1",
        "C13.05-P1",
        "C13.05-D1"
      ]
    },
    {
      "concept_id": "C13.06",
      "concept": "From a geometric pattern to an action",
      "introduction": "lesson-06",
      "practice": "C13.06-P1",
      "assessment": "C13.06-D1",
      "later_use": "capstone",
      "worked_example": "C13.06-W1",
      "all_required_teaching_item_ids": [
        "C13.06-E1",
        "C13.06-W1",
        "C13.06-P1",
        "C13.06-D1"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Symmetry as an operation with a rule",
      "entry_prerequisites": [
        "course-09",
        "course-11",
        "course-12"
      ],
      "concept_ids": [
        "C13.01"
      ],
      "worked_example_capability": "Check closure and invariants in a small transformation set",
      "assessment_target": "Check closure and invariants in a small transformation set",
      "later_use": "lesson-02",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C13.01",
        "explanation_id": "C13.01-E1",
        "bridge_to_teach": "Define a transformation, composition, identity and inverse by acting on explicit tuples. Build finite composition tables before the group name. State the carrier and the quantity preserved.",
        "worked_example": {
          "id": "C13.01-W1",
          "task_and_answer": "On ordered real pairs let R(x,y)=(y,x). I and R satisfy II=I,IR=RI=R,RR=I. For(2,5), R gives(5,2), preserving sum7 and squared norm29; inverse is R."
        },
        "guided_practice": {
          "id": "C13.01-P1",
          "task_and_answer": "On ordered triples let T(x,y,z)=(z,x,y). T(1,2,3)=(3,1,2), T^2 gives(2,3,1), T^3=I. The three operations compose by exponents modulo3 and preserve sum6 and squared norm14."
        },
        "diagnostic": {
          "id": "C13.01-D1",
          "task_and_answer": "The set{I,T} is not closed since T*T=T^2 is missing. A rule without a carrier or composition law is insufficient for a symmetry claim."
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
        "original_title": "Symmetry as an operation with a rule",
        "original_assessment_target": "Check closure and invariants in a small transformation set",
        "required_source_amendment_ids": [],
        "original_entry_prerequisites": [
          "course-09",
          "course-11",
          "course-12"
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Side transfers and the A1 pattern",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C13.02"
      ],
      "worked_example_capability": "Derive the allowed two-side transfer and its parity quotient",
      "assessment_target": "Derive the allowed two-side transfer and its parity quotient",
      "later_use": "lesson-03",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C13.02",
        "explanation_id": "C13.02-E1",
        "bridge_to_teach": "Review signed carries, S=C_b+C_c and A=C_b-C_c; derive inverse halves and equal-parity condition. Teach integer congruence including negative examples and the root-step quotient Q1=2Z within P1=Z.",
        "worked_example": {
          "id": "C13.02-W1",
          "task_and_answer": "(C_b,C_c)=(2,1) gives(S,A)=(3,1). Transfer(1,-1) yields(3,0),(S,A)=(3,3); S fixed,A increased2, odd class retained. Reverse by(-1,1)."
        },
        "guided_practice": {
          "id": "C13.02-P1",
          "task_and_answer": "(-1,3) gives S=2,A=-4; after transfer(0,2),S=2,A=-2. Both represent even class0 mod2. Recover the input as((S+A)/2,(S-A)/2)=(-1,3)."
        },
        "diagnostic": {
          "id": "C13.02-D1",
          "task_and_answer": "A parity class alone loses the integer A; retain A or quotient representative plus its even displacement. S=1,A=0 cannot decode integer carries. Carry parity is not detector antipodal parity."
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
        "original_title": "Side transfers and the A1 pattern",
        "original_assessment_target": "Derive the allowed two-side transfer and its parity quotient",
        "required_source_amendment_ids": [],
        "original_entry_prerequisites": [
          "lesson-01"
        ]
      }
    },
    {
      "id": "lesson-03",
      "title": "Three channels and the A2 plane",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C13.03"
      ],
      "worked_example_capability": "Draw sum-zero triples and compute their basic inner products",
      "assessment_target": "Draw sum-zero triples and compute their basic inner products",
      "later_use": "lesson-04",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C13.03",
        "explanation_id": "C13.03-E1",
        "bridge_to_teach": "Build the plane x+y+z=0 with integer vectors. Define alpha1=(1,-1,0),alpha2=(0,1,-1); use ordinary Euclidean dot products on this abstract carrier, not a Cell3 physical metric. Teach Cartan entries2(alpha_i dot alpha_j)/(alpha_j dot alpha_j).",
        "worked_example": {
          "id": "C13.03-W1",
          "task_and_answer": "alpha1^2=alpha2^2=2 and alpha1 dot alpha2=-1, so Cartan=[[2,-1],[-1,2]]. All six roots are the signed differences e_i-e_j. q=(2,-3,1)=2alpha1-alpha2."
        },
        "guided_practice": {
          "id": "C13.03-P1",
          "task_and_answer": "q=(-1,3,-2)=-alpha1+2alpha2; reconstruct each component. alpha1+alpha2=(1,0,-1) has norm squared2; alpha1 dot(alpha1+alpha2)=1. Verify zero sum for every root."
        },
        "diagnostic": {
          "id": "C13.03-D1",
          "task_and_answer": "Zero-sum(1/2,-1/2,0) lies in the real plane but not its integer root lattice. Any integer q=(x,y,z) with sum0 equals x alpha1-z alpha2; show this componentwise."
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
        "original_title": "Three channels and the A2 plane",
        "original_assessment_target": "Draw sum-zero triples and compute their basic inner products",
        "required_source_amendment_ids": [],
        "original_entry_prerequisites": [
          "lesson-02"
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "Roots, weights, and quotient labels",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C13.04"
      ],
      "worked_example_capability": "Distinguish a root step from a weight class",
      "assessment_target": "Distinguish a root step from a weight class",
      "later_use": "lesson-05",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C13.04",
        "explanation_id": "C13.04-E1",
        "bridge_to_teach": "Define centered weights u_i=e_i-(1,1,1)/3. Explicitly define P2=Z u1+Z u2 with u3=-u1-u2, and Q2 as integer zero-sum vectors. Show a u1+b u2 is integral iff a+b=0 mod3, giving three classes without assuming an abstract quotient theorem.",
        "worked_example": {
          "id": "C13.04-W1",
          "task_and_answer": "u1=(2,-1,-1)/3; u1-u2=alpha1. u1 and2u1 are nonintegral but3u1=(2,-1,-1) is a root-lattice vector. Representatives0,u1,2u1 have classes0,1,2; addition is modulo3."
        },
        "guided_practice": {
          "id": "C13.04-P1",
          "task_and_answer": "u1+u2=(1,1,-2)/3 has class2. 2u1+u2=(1,0,-1)=alpha1+alpha2 has class0. u2-u1=(-1,1,0) lies in Q2, so u1 andu2 share a class. Retain coefficients(a,b) when making a quotient view."
        },
        "diagnostic": {
          "id": "C13.04-D1",
          "task_and_answer": "The three displayed weights u1,u2,u3 are three channels in one nonzero quotient class, not the three quotient classes. A root step leaves class unchanged but changes the vector; quotient label alone cannot reconstruct it."
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
        "original_title": "Roots, weights, and quotient labels",
        "original_assessment_target": "Distinguish a root step from a weight class",
        "required_source_amendment_ids": [],
        "original_entry_prerequisites": [
          "lesson-03"
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "Primitive lifts and role separation",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C13.05"
      ],
      "worked_example_capability": "Separate primitive lifts, family labels, and detector parity",
      "assessment_target": "Separate primitive lifts, family labels, and detector parity",
      "later_use": "lesson-06",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C13.05",
        "explanation_id": "C13.05-E1",
        "bridge_to_teach": "Use a typed record to separate formal primitive-lift channel basis e1,e2,e3, their centered weights, family labels, projective ray coordinates and detector parity. Read source M09 guards and distinguish three primitive channels from all compatible address lifts.",
        "worked_example": {
          "id": "C13.05-W1",
          "task_and_answer": "Formal e1,e2 have sum1 and differencealpha1. Centering givesu1,u2. A source-compatible lift of residue(1,0,0) mod3 is(1,0,0)+3(0,1,-1)=(1,3,-3), reducing to the same residue. It is not a new face-area ratio."
        },
        "guided_practice": {
          "id": "C13.05-P1",
          "task_and_answer": "Use lift(1,0,0)+3(-1,0,1)=(-2,0,3); reduction mod3 again(1,0,0), and retained lift digit(-1,0,1) reconstructs it. Separately record an arbitrary family tag F2 and detector parity -1; neither is determined by A mod2 or weight class."
        },
        "diagnostic": {
          "id": "C13.05-D1",
          "task_and_answer": "There are27 compatible lifts when all three digits vary in{-1,0,1}; this does not mean27 primitive channel types. The source three primitive lifts are not the three projective ray coordinates; do not identify them just because both use triples."
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
        "original_title": "Primitive lifts and role separation",
        "original_assessment_target": "Separate primitive lifts, family labels, and detector parity",
        "required_source_amendment_ids": [],
        "original_entry_prerequisites": [
          "lesson-04"
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "From a geometric pattern to an action",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C13.06"
      ],
      "worked_example_capability": "Specify the carrier and map needed for a symmetry claim",
      "assessment_target": "Specify the carrier and map needed for a symmetry claim",
      "later_use": "capstone",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C13.06",
        "explanation_id": "C13.06-E1",
        "bridge_to_teach": "Require a carrier, map and invariant check for an action. Use explicit permutation matrices on the root plane. Keep numerical coincidences and physical assignments separate from the finite action proved.",
        "worked_example": {
          "id": "C13.06-W1",
          "task_and_answer": "T(x,y,z)=(z,x,y) sends alpha1 toalpha2 and alpha2 to(-1,0,1)=-(alpha1+alpha2). T^3=I and T^T T=I, hence it permutes roots and preserves dot products and the zero-sum plane."
        },
        "guided_practice": {
          "id": "C13.06-P1",
          "task_and_answer": "T(2,-3,1)=(1,2,-3)=alpha1+3alpha2. T^2 returns via(-3,1,2), and T^3 restores(2,-3,1). Compute squared norm14 before/after; retain the original vector with quotient label."
        },
        "diagnostic": {
          "id": "C13.06-D1",
          "task_and_answer": "A matching A2 diagram on a different carrier does not specify a physical action. Supply an explicit map and check that the declared operations commute with it; otherwise label the identification unresolved."
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
        "original_title": "From a geometric pattern to an action",
        "original_assessment_target": "Specify the carrier and map needed for a symmetry claim",
        "required_source_amendment_ids": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Build a labeled A1/A2 transfer atlas with invariant checks and a precise account of each quotient.",
    "required_operations": [
      "Build the three-operation permutation table and verify identity,inverse,sum and norm on(1,2,3).",
      "Apply the side transfer to(-1,3), decode S/A and preserve the quotient class with full carry data.",
      "Enumerate six roots, calculate Cartan entries and reconstruct(-1,3,-2) from simple roots.",
      "Compute centered weights and classes ofu1+u2 and2u1+u2; distinguish the three weight channels from the three quotient classes.",
      "Decode the taught compatible lift, retaining residue and lift digit; separate primitive channels,family tag,ray coordinates and detector parity.",
      "Verify the supplied cyclic action on roots and(2,-3,1), state carrier,map and limits on physical identification."
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C13-CAP-01",
        "operation": "Build the three-operation permutation table and verify identity,inverse,sum and norm on(1,2,3).",
        "introduction": "lesson-01",
        "explanation_id": "C13.01-E1",
        "worked_example_id": "C13.01-W1",
        "prior_practice_id": "C13.01-P1",
        "diagnostic_id": "C13.01-D1"
      },
      {
        "step_id": "C13-CAP-02",
        "operation": "Apply the side transfer to(-1,3), decode S/A and preserve the quotient class with full carry data.",
        "introduction": "lesson-02",
        "explanation_id": "C13.02-E1",
        "worked_example_id": "C13.02-W1",
        "prior_practice_id": "C13.02-P1",
        "diagnostic_id": "C13.02-D1"
      },
      {
        "step_id": "C13-CAP-03",
        "operation": "Enumerate six roots, calculate Cartan entries and reconstruct(-1,3,-2) from simple roots.",
        "introduction": "lesson-03",
        "explanation_id": "C13.03-E1",
        "worked_example_id": "C13.03-W1",
        "prior_practice_id": "C13.03-P1",
        "diagnostic_id": "C13.03-D1"
      },
      {
        "step_id": "C13-CAP-04",
        "operation": "Compute centered weights and classes ofu1+u2 and2u1+u2; distinguish the three weight channels from the three quotient classes.",
        "introduction": "lesson-04",
        "explanation_id": "C13.04-E1",
        "worked_example_id": "C13.04-W1",
        "prior_practice_id": "C13.04-P1",
        "diagnostic_id": "C13.04-D1"
      },
      {
        "step_id": "C13-CAP-05",
        "operation": "Decode the taught compatible lift, retaining residue and lift digit; separate primitive channels,family tag,ray coordinates and detector parity.",
        "introduction": "lesson-05",
        "explanation_id": "C13.05-E1",
        "worked_example_id": "C13.05-W1",
        "prior_practice_id": "C13.05-P1",
        "diagnostic_id": "C13.05-D1"
      },
      {
        "step_id": "C13-CAP-06",
        "operation": "Verify the supplied cyclic action on roots and(2,-3,1), state carrier,map and limits on physical identification.",
        "introduction": "lesson-06",
        "explanation_id": "C13.06-E1",
        "worked_example_id": "C13.06-W1",
        "prior_practice_id": "C13.06-P1",
        "diagnostic_id": "C13.06-D1"
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
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-13-root-systems-symmetry-and-a1-a2-structure' --json"
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
      "course_id": "course-13",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-13-root-systems-symmetry-and-a1-a2-structure\\input-contract.json",
      "input_contract_sha256": "7de23b047626f64f38043f8f6e0f4a3f768fb0b56120b8b2b7761a247d4cb5b3",
      "application": "Merge additively as teaching_amendment, replace generic coverage references with explicit exercise IDs, and retain all original concepts, source amendments and educational bridge IDs. Parent applies; no project edit was made.",
      "applied_source_amendments_read": {},
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C13.01",
            "concept": "Symmetry as an operation with a rule",
            "operation": "Check closure and invariants in a small transformation set"
          },
          {
            "concept_id": "C13.02",
            "concept": "Side transfers and the A1 pattern",
            "operation": "Derive the allowed two-side transfer and its parity quotient"
          },
          {
            "concept_id": "C13.03",
            "concept": "Three channels and the A2 plane",
            "operation": "Draw sum-zero triples and compute their basic inner products"
          },
          {
            "concept_id": "C13.04",
            "concept": "Roots, weights, and quotient labels",
            "operation": "Distinguish a root step from a weight class"
          },
          {
            "concept_id": "C13.05",
            "concept": "Primitive lifts and role separation",
            "operation": "Separate primitive lifts, family labels, and detector parity"
          },
          {
            "concept_id": "C13.06",
            "concept": "From a geometric pattern to an action",
            "operation": "Specify the carrier and map needed for a symmetry claim"
          }
        ],
        "source_modules": [
          "M09"
        ],
        "scope": "Build a labeled A1/A2 transfer atlas with invariant checks and a precise account of each quotient.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Build a labeled A1/A2 transfer atlas with invariant checks and a precise account of each quotient.",
        "required_operations": [
          "Check closure and invariants in a small transformation set",
          "Derive the allowed two-side transfer and its parity quotient",
          "Draw sum-zero triples and compute their basic inner products",
          "Distinguish a root step from a weight class",
          "Separate primitive lifts, family labels, and detector parity",
          "Specify the carrier and map needed for a symmetry claim"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-13",
          "title": "Root Systems, Symmetry, and A1–A2 Structure",
          "backbone_modules": [
            "M09"
          ],
          "topic_boundary": "A1 carry-side transfers and A2 primitive lifts; roots, weights and quotient labels preserve physical roles.",
          "cognitive_or_fidelity_risk": "An isomorphic lattice is not an identified physical action.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "S02"
          ],
          "source_pointer": "/backbone_sequence/8",
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-13-root-systems-symmetry-and-a1-a2-structure\\input-contract.json",
            "sha256": "30856fd09d2a404367464adf249afc82fa5c0e85900f5e06a8d1dfafea98859b",
            "lesson_count": 6
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
        "primary": "S02#/backbone_sequence/8",
        "branches": [
          "S02#/branch_proofs/3",
          "S02#/branch_proofs/6"
        ],
        "finite_scope": "A1 carry difference root2Z in weightZ; A2 roots are integer zero-sum triples, centered weight lattice generated byu1,u2; quotient criterion a+b mod3. Abstract Euclidean root dot product is not the Cell3 physical metric. Primitive-lift channel roles, 27 compatible address lifts, family tags, face-ray coordinates and detector parity are separate.",
        "source_formula_ids": [
          "KFM-X020",
          "KFM-X021",
          "KFM-X014"
        ],
        "extension_boundary": "Full address/character-channel compiler and physical action identification are not prerequisites of this finite root atlas."
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "Symmetry as an operation with a rule",
          "entry_prerequisites": [
            "course-09",
            "course-11",
            "course-12"
          ],
          "concept_ids": [
            "C13.01"
          ],
          "worked_example_capability": "Check closure and invariants in a small transformation set",
          "assessment_target": "Check closure and invariants in a small transformation set",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C13.01-E1",
          "worked_example_id": "C13.01-W1",
          "prior_practice_id": "C13.01-P1",
          "diagnostic_id": "C13.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Side transfers and the A1 pattern",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C13.02"
          ],
          "worked_example_capability": "Derive the allowed two-side transfer and its parity quotient",
          "assessment_target": "Derive the allowed two-side transfer and its parity quotient",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C13.02-E1",
          "worked_example_id": "C13.02-W1",
          "prior_practice_id": "C13.02-P1",
          "diagnostic_id": "C13.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "Three channels and the A2 plane",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C13.03"
          ],
          "worked_example_capability": "Draw sum-zero triples and compute their basic inner products",
          "assessment_target": "Draw sum-zero triples and compute their basic inner products",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C13.03-E1",
          "worked_example_id": "C13.03-W1",
          "prior_practice_id": "C13.03-P1",
          "diagnostic_id": "C13.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "Roots, weights, and quotient labels",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C13.04"
          ],
          "worked_example_capability": "Distinguish a root step from a weight class",
          "assessment_target": "Distinguish a root step from a weight class",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C13.04-E1",
          "worked_example_id": "C13.04-W1",
          "prior_practice_id": "C13.04-P1",
          "diagnostic_id": "C13.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "Primitive lifts and role separation",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C13.05"
          ],
          "worked_example_capability": "Separate primitive lifts, family labels, and detector parity",
          "assessment_target": "Separate primitive lifts, family labels, and detector parity",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C13.05-E1",
          "worked_example_id": "C13.05-W1",
          "prior_practice_id": "C13.05-P1",
          "diagnostic_id": "C13.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "From a geometric pattern to an action",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C13.06"
          ],
          "worked_example_capability": "Specify the carrier and map needed for a symmetry claim",
          "assessment_target": "Specify the carrier and map needed for a symmetry claim",
          "later_use": "capstone",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C13.06-E1",
          "worked_example_id": "C13.06-W1",
          "prior_practice_id": "C13.06-P1",
          "diagnostic_id": "C13.06-D1"
        }
      ],
      "core_periods": 9,
      "capstone_periods": 2,
      "period_minutes": 55,
      "core_boundary": "Finite signed arithmetic,explicit matrices,small exterior basis operations and source-reading cards. General Lie theory,quotient-bundle anomaly proofs,full source compiler execution,empirical physical uniqueness and untaught variational dynamics are not hidden capstone requirements.",
      "prerequisite_status": "Blueprint closure checked for explicit operations. Final produced explanations,answered practice and assessment must still undergo independent content acceptance.",
      "inline_content_location": "Complete lesson anchors are in course_map[*].teaching_anchor; complete capstone mapping is in capstone_specification.backward_map below."
    },
    "completed_course_acceptance": false
  }
}
```
