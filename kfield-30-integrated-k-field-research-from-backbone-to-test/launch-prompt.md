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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-30-integrated-k-field-research-from-backbone-to-test",
  "topic": "Integrated K-Field Research: From Backbone to Test",
  "series_course_id": "course-30",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-19",
    "Capabilities taught in course-20",
    "Capabilities taught in course-21",
    "Capabilities taught in course-22",
    "Capabilities taught in course-23",
    "Capabilities taught in course-27",
    "Capabilities taught in course-28",
    "Capabilities taught in course-29"
  ],
  "learning_outcomes": [
    "Connect the core modules and distinguish supplied premises from derived objects",
    "Read the scope of a proof, replay, calibration, and measurement",
    "Use a small inverse problem to test which parameters a measurement can recover",
    "Compare candidate mechanisms by predictions and parameter needs",
    "Freeze inputs, transformations, comparisons, and outcome handling",
    "Retain all outcomes and define the next informative measurement",
    "Write a reproducible report with sources, equations, residuals, and unresolved branches",
    "Defend a complete geometric-to-instrument chain and its next test"
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
    },
    {
      "logical_path": "applications/kfield_lucas_lab/rag_corpus/50_physical_closure.md",
      "object_id": "c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a",
      "sha256": "c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a",
      "role": "Pinned testbench source; retrieve bounded bytes through krytronx_get and follow its exact underlying contract."
    },
    {
      "logical_path": "applications/kfield_lucas_lab/rag_corpus/20_phase_route.md",
      "object_id": "c9335e2df74344bff5665df5a5e0b9094fef22147c76458f1a54efe49cefce62",
      "sha256": "c9335e2df74344bff5665df5a5e0b9094fef22147c76458f1a54efe49cefce62",
      "role": "Pinned testbench source; retrieve bounded bytes through krytronx_get and follow its exact underlying contract."
    },
    {
      "logical_path": "applications/kfield_lucas_lab/rag_corpus/30_interferometer_capabilities.md",
      "object_id": "e9c6d0346e7f4fa120e9836df9d4a45b7e2c587bc046874d91cb38a0c68c16bc",
      "sha256": "e9c6d0346e7f4fa120e9836df9d4a45b7e2c587bc046874d91cb38a0c68c16bc",
      "role": "Pinned testbench source; retrieve bounded bytes through krytronx_get and follow its exact underlying contract."
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
      "M20"
    ],
    "guidance": "Retrieve exact topic sources and source-local pointers; use the provided archival files read-only and verify their hashes. Do not rely only on titles or summaries. For experimental topics search the testbench topic and local relevant domain skills.",
    "retrieval_notes": [
      "RAG reranking is disabled by server policy; use rerank:false.",
      "Original source JSON digests are not all addressable through krytronx_get; the mature and corrected mathematical-essence files were found locally and their hashes verified.",
      "Root traversal is truncated at depth one; it is a discovery route, not an exhaustive coverage certificate.",
      "Stable keys named in testbench prose did not resolve in graph traversal; retrieve pinned exact artifacts and contracts rather than treating a display label as a graph ID."
    ]
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
        "concept_id": "C30.01",
        "concept": "Rebuilding the complete dependency chain",
        "operation": "Connect the core modules and distinguish supplied premises from derived objects"
      },
      {
        "concept_id": "C30.02",
        "concept": "Formal witnesses and empirical witnesses",
        "operation": "Read the scope of a proof, replay, calibration, and measurement"
      },
      {
        "concept_id": "C30.03",
        "concept": "Interferometers and identifiable coupling",
        "operation": "Use a small inverse problem to test which parameters a measurement can recover"
      },
      {
        "concept_id": "C30.04",
        "concept": "Choosing discriminating experiments",
        "operation": "Compare candidate mechanisms by predictions and parameter needs"
      },
      {
        "concept_id": "C30.05",
        "concept": "Preregistering a complete protocol",
        "operation": "Freeze inputs, transformations, comparisons, and outcome handling"
      },
      {
        "concept_id": "C30.06",
        "concept": "Independent replication and negative outcomes",
        "operation": "Retain all outcomes and define the next informative measurement"
      },
      {
        "concept_id": "C30.07",
        "concept": "Professional scientific communication",
        "operation": "Write a reproducible report with sources, equations, residuals, and unresolved branches"
      },
      {
        "concept_id": "C30.08",
        "concept": "The integrated research defense",
        "operation": "Defend a complete geometric-to-instrument chain and its next test"
      }
    ],
    "source_modules": [
      "M20"
    ],
    "scope": "Produce a senior research portfolio connecting at least one exact backbone construction to an instrument model, retained residual analysis, and a falsifiable independent test.",
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
      "concept_id": "C30.01",
      "concept": "Rebuilding the complete dependency chain",
      "introduction": "lesson-01",
      "practice": "C30.01-P1",
      "assessment": "C30.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C30.01-W1",
      "all_required_teaching_item_ids": [
        "C30.01-E1",
        "C30.01-W1",
        "C30.01-P1",
        "C30.01-D1"
      ]
    },
    {
      "concept_id": "C30.02",
      "concept": "Formal witnesses and empirical witnesses",
      "introduction": "lesson-02",
      "practice": "C30.02-P1",
      "assessment": "C30.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C30.02-W1",
      "all_required_teaching_item_ids": [
        "C30.02-E1",
        "C30.02-W1",
        "C30.02-P1",
        "C30.02-D1"
      ]
    },
    {
      "concept_id": "C30.03",
      "concept": "Interferometers and identifiable coupling",
      "introduction": "lesson-03",
      "practice": "C30.03-P1",
      "assessment": "C30.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C30.03-W1",
      "all_required_teaching_item_ids": [
        "C30.03-E1",
        "C30.03-W1",
        "C30.03-P1",
        "C30.03-D1"
      ]
    },
    {
      "concept_id": "C30.04",
      "concept": "Choosing discriminating experiments",
      "introduction": "lesson-04",
      "practice": "C30.04-P1",
      "assessment": "C30.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C30.04-W1",
      "all_required_teaching_item_ids": [
        "C30.04-E1",
        "C30.04-W1",
        "C30.04-P1",
        "C30.04-D1"
      ]
    },
    {
      "concept_id": "C30.05",
      "concept": "Preregistering a complete protocol",
      "introduction": "lesson-05",
      "practice": "C30.05-P1",
      "assessment": "C30.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C30.05-W1",
      "all_required_teaching_item_ids": [
        "C30.05-E1",
        "C30.05-W1",
        "C30.05-P1",
        "C30.05-D1"
      ]
    },
    {
      "concept_id": "C30.06",
      "concept": "Independent replication and negative outcomes",
      "introduction": "lesson-06",
      "practice": "C30.06-P1",
      "assessment": "C30.06-D1",
      "later_use": "lesson-07",
      "worked_example": "C30.06-W1",
      "all_required_teaching_item_ids": [
        "C30.06-E1",
        "C30.06-W1",
        "C30.06-P1",
        "C30.06-D1"
      ]
    },
    {
      "concept_id": "C30.07",
      "concept": "Professional scientific communication",
      "introduction": "lesson-07",
      "practice": "C30.07-P1",
      "assessment": "C30.07-D1",
      "later_use": "lesson-08",
      "worked_example": "C30.07-W1",
      "all_required_teaching_item_ids": [
        "C30.07-E1",
        "C30.07-W1",
        "C30.07-P1",
        "C30.07-D1"
      ]
    },
    {
      "concept_id": "C30.08",
      "concept": "The integrated research defense",
      "introduction": "lesson-08",
      "practice": "C30.08-P1",
      "assessment": "C30.08-D1",
      "later_use": "capstone",
      "worked_example": "C30.08-W1",
      "all_required_teaching_item_ids": [
        "C30.08-E1",
        "C30.08-W1",
        "C30.08-P1",
        "C30.08-D1"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Rebuilding the complete dependency chain",
      "entry_prerequisites": [
        "course-19",
        "course-20",
        "course-21",
        "course-22",
        "course-23",
        "course-27",
        "course-28",
        "course-29"
      ],
      "concept_ids": [
        "C30.01"
      ],
      "worked_example_capability": "Connect the core modules and distinguish supplied premises from derived objects",
      "assessment_target": "Connect the core modules and distinguish supplied premises from derived objects",
      "later_use": "lesson-02",
      "core_minutes": 165,
      "required_amendment_ids": [
        "SA-30"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C30.01",
        "explanation_id": "C30.01-E1",
        "bridge_to_teach": "Build a typed dependency map, not a list of impressive labels. The S02 backbone M20 integrates M01–M18 plus EG-A1–A6, declared domains and supplied state coordinates. M19 remains a separately retained mixed branch. Source corrections repair edge serialization and premise wording; record both the corrected interpretation and source occurrence.",
        "worked_example": {
          "id": "C30.01-W1",
          "task_and_answer": "Read S02#/backbone_sequence/19: its18 required modules are M01 through M18. Group their jobs as root/volume/reciprocal geometry; retained calculus/shape/graphs; internal modules/carriers; interaction/history/action/family; decoder/paired continuum. Read all four state-coordinate entries: pre-anchor scale,time/action normalization,vacuum/operator inputs,occupied six-coordinate state."
        },
        "guided_practice": {
          "id": "C30.01-P1",
          "task_and_answer": "Trace backbone M17 from M05 and M11, then into M20; trace M18 from M03 and M04, then into M20. Keep M19 inputs M07,M08,M10,M13,M18 and its exceptional extensions on a separate branch. Classify EG-A2 as a constitutive decoder premise and c in the mass renderer as a supplied occupied-state coordinate, not a theorem choosing its value."
        },
        "diagnostic": {
          "id": "C30.01-D1",
          "task_and_answer": "Do not infer premise-free derivation from the compressed theorem wording. S03 AUD001 removes M19->M20 from closure; AUD011 requires the full premise contract. The live source-module table in the report preserves every requires edge and boundary."
        },
        "planned_periods": 3,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "Rebuilding the complete dependency chain",
        "original_assessment_target": "Connect the core modules and distinguish supplied premises from derived objects",
        "original_concept_ids": [
          "C30.01"
        ],
        "required_source_amendment_ids": [
          "SA-30"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "course-19",
          "course-20",
          "course-21",
          "course-22",
          "course-23",
          "course-27",
          "course-28",
          "course-29"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "All core module roles",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Premises and supplied state coordinates",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 3,
            "focus": "M19 boundary and M20 dependency map",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Formal witnesses and empirical witnesses",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C30.02"
      ],
      "worked_example_capability": "Read the scope of a proof, replay, calibration, and measurement",
      "assessment_target": "Read the scope of a proof, replay, calibration, and measurement",
      "later_use": "lesson-03",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-30"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C30.02",
        "explanation_id": "C30.02-E1",
        "bridge_to_teach": "Give every result a source hash/pointer and evidence type: formal theorem under premises, executable replay under inputs, calibration against a reference, observation with acquisition identity, or prospective protocol. Keep compiler-adjudication labels separate from backbone labels even when both use M numbers.",
        "worked_example": {
          "id": "C30.02-W1",
          "task_and_answer": "I02 reports direct-authority compiler modules M03,M07,M08. S02 backbone M03 is its own named construction; the reused numeral alone supplies no identity or authority transfer. I01 results/9 classifies20 compiler modules; results/10 gives six minimal two-question experiment portfolios as designs. None is a performed favorable experiment."
        },
        "guided_practice": {
          "id": "C30.02-P1",
          "task_and_answer": "Sort four cards: exact mean/detail reconstruction is finite algebra; a checker output with hash is a replay receipt; a known reference and transfer interval is calibration; timestamped detector values are observations. A planned detector run is a fifth card, a protocol. Assign source pointer and assumptions to each. Keep compiler M20 compositeNonterminal distinct from the attributed backbone M20 closure theorem."
        },
        "diagnostic": {
          "id": "C30.02-D1",
          "task_and_answer": "Safe Agda typechecking and hostile-mutant rejection establish their stated formal/transport properties, not apparatus calibration or source authorship. I01 retains global-form family Z1,Z2,Z3,Z6; a source-specific Z6 lock is not silently promoted to unique global physical selection."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "Formal witnesses and empirical witnesses",
        "original_assessment_target": "Read the scope of a proof, replay, calibration, and measurement",
        "original_concept_ids": [
          "C30.02"
        ],
        "required_source_amendment_ids": [
          "SA-30"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-01"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Evidence types and source pointers",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Compiler namespace and authority limits",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-03",
      "title": "Interferometers and identifiable coupling",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C30.03"
      ],
      "worked_example_capability": "Use a small inverse problem to test which parameters a measurement can recover",
      "assessment_target": "Use a small inverse problem to test which parameters a measurement can recover",
      "later_use": "lesson-04",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C30.03",
        "explanation_id": "C30.03-E1",
        "bridge_to_teach": "For a linear instrument model y=H theta, identify recoverable parameter combinations from rank and nullspace. Show explicit different parameter vectors with identical outputs before adding a discriminating measurement. Keep all original channels and calibration assumptions.",
        "worked_example": {
          "id": "C30.03-W1",
          "task_and_answer": "H=[[1,1],[2,2]],thetaA=(2,1),thetaB=(1,2) both give y=(3,6). Rank1 and null direction(1,-1) show that only the sum is identified. Adding a row(1,-1) distinguishes responses+1 and-1. Sum s and difference d reconstruct theta=((s+d)/2,(s-d)/2)."
        },
        "guided_practice": {
          "id": "C30.03-P1",
          "task_and_answer": "For s=5,d=-1 recover theta=(2,3). Verify original rows give5 and10, and the new row gives-1. If a detector provides only product gain*responsivity=6, the pairs(2,3) and(1,6) remain indistinguishable without a separate calibration, even if a geometric model is exact."
        },
        "diagnostic": {
          "id": "C30.03-D1",
          "task_and_answer": "A new row must be physically measurable with known transfer, not just algebraically convenient. T30 detection, extraction and induction have different witness requirements. A beat frequency alone identifies neither power nor force."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "Interferometers and identifiable coupling",
        "original_assessment_target": "Use a small inverse problem to test which parameters a measurement can recover",
        "original_concept_ids": [
          "C30.03"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-02"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Rank and indistinguishable parameters",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Calibrated discriminating measurement",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "Choosing discriminating experiments",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C30.04"
      ],
      "worked_example_capability": "Compare candidate mechanisms by predictions and parameter needs",
      "assessment_target": "Compare candidate mechanisms by predictions and parameter needs",
      "later_use": "lesson-05",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-30"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C30.04",
        "explanation_id": "C30.04-E1",
        "bridge_to_teach": "Compare mechanisms by a shared input contract, frozen parameters and predicted observables. Teach two binary questions with four synthetic states to explain why a design may need more than one question; do not substitute this toy for the six integration portfolios.",
        "worked_example": {
          "id": "C30.04-W1",
          "task_and_answer": "Four synthetic states labelled00,01,10,11 are distinguished by asking each bit; one binary answer has only two values and cannot distinguish all four. The source I01 results/10 reports six goal-specific two-question designs with separate formal minimality witnesses; no outcomes are present."
        },
        "guided_practice": {
          "id": "C30.04-P1",
          "task_and_answer": "For thetaA=(2,1) and thetaB=(1,2), the sum measurement predicts3 for both and the difference predicts+1 versus-1. Freeze this discriminating sign prediction before a new calibrated measurement. Record equal-output candidates, any unresolved parameters and the alternative response each mechanism requires."
        },
        "diagnostic": {
          "id": "C30.04-D1",
          "task_and_answer": "A design is not a measurement. No source portfolio result is inferred from the toy two-bit count. A proposed test that refits parameters after every outcome has not retained its original discriminating prediction."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "Choosing discriminating experiments",
        "original_assessment_target": "Compare candidate mechanisms by predictions and parameter needs",
        "original_concept_ids": [
          "C30.04"
        ],
        "required_source_amendment_ids": [
          "SA-30"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-03"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Two-bit synthetic design",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Source portfolios and prospective predictions",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "Preregistering a complete protocol",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C30.05"
      ],
      "worked_example_capability": "Freeze inputs, transformations, comparisons, and outcome handling",
      "assessment_target": "Freeze inputs, transformations, comparisons, and outcome handling",
      "later_use": "lesson-06",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-30"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C30.05",
        "explanation_id": "C30.05-E1",
        "bridge_to_teach": "Write a complete prospective protocol: question and candidates, source/premise hashes, instrument/channel identities, calibration and units, exposure/timing/site/orientation, frozen geometry, train/check roles, transforms, comparisons, uncertainty, raw retention, stopping rule, exceptions and independent reviewer. Explicitly mark planned versus executed.",
        "worked_example": {
          "id": "C30.05-W1",
          "task_and_answer": "Synthetic protocol rehearsal fixes thetaA=(2,1),two operators sum and difference, predicted(3,1), and two labelled input rows. Stop after both rows or record an interruption; keep all outcomes and residuals. A real experiment additionally needs a calibrated apparatus implementing those operators and a preregistered uncertainty/transfer contract."
        },
        "guided_practice": {
          "id": "C30.05-P1",
          "task_and_answer": "Draft the real protocol as planned with raw acquisition destination in place, UTC midpoint convention, exposure duration, calibration reference/version, orientation convention and blinded operator labels. Unavailable instrument/calibration fields are marked missing with owners/return addresses. Analysis rules remain frozen; no readings are filled in."
        },
        "diagnostic": {
          "id": "C30.05-D1",
          "task_and_answer": "Explicit null, absent field, string unknown and source-reported status are distinct. Record source hash, pointer, raw kind and presence. An interrupted run or calibration change is retained and versioned, never silently called a completed favorable test."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "Preregistering a complete protocol",
        "original_assessment_target": "Freeze inputs, transformations, comparisons, and outcome handling",
        "original_concept_ids": [
          "C30.05"
        ],
        "required_source_amendment_ids": [
          "SA-30"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-04"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Frozen protocol and instrument requirements",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Missing inputs and stopping branches",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "Independent replication and negative outcomes",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C30.06"
      ],
      "worked_example_capability": "Retain all outcomes and define the next informative measurement",
      "assessment_target": "Retain all outcomes and define the next informative measurement",
      "later_use": "lesson-07",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C30.06",
        "explanation_id": "C30.06-E1",
        "bridge_to_teach": "Independent replication needs a new acquisition identity and an independently replayable fixed protocol. Preserve successful, discrepant, zero, invalid and interrupted outcomes. Use residual structure to choose the next informative measurement; do not equate arithmetic reproduction with new empirical data.",
        "worked_example": {
          "id": "C30.06-W1",
          "task_and_answer": "Synthetic rehearsal prediction(3,1),authored test values(3,0) gives residual(0,-1). Reconstruct both values from prediction+residual. This is a performed synthetic arithmetic check only; no real experiment occurred. The missing difference response remains information about the model/transfer distinction."
        },
        "guided_practice": {
          "id": "C30.06-P1",
          "task_and_answer": "If an independent future reading were(4,1), the frozen residual would be(1,0); label this conditional example, not an observation. A separate known-reference calibration can distinguish detector gain from a changed parameter sum. Retain both branches and the same frozen original predictions."
        },
        "diagnostic": {
          "id": "C30.06-D1",
          "task_and_answer": "Rerunning software on the same samples is replay, not independent physical replication. Do not discard a negative result or reinterpret undefined rows as zero response. Specify the next measurement and its calibration needs without claiming it was done."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "Independent replication and negative outcomes",
        "original_assessment_target": "Retain all outcomes and define the next informative measurement",
        "original_concept_ids": [
          "C30.06"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Replication and retained residuals",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-07",
      "title": "Professional scientific communication",
      "entry_prerequisites": [
        "lesson-06"
      ],
      "concept_ids": [
        "C30.07"
      ],
      "worked_example_capability": "Write a reproducible report with sources, equations, residuals, and unresolved branches",
      "assessment_target": "Write a reproducible report with sources, equations, residuals, and unresolved branches",
      "later_use": "lesson-08",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-07",
        "concept_id": "C30.07",
        "explanation_id": "C30.07-E1",
        "bridge_to_teach": "A reproducible report separates source observations, exact derived transforms, supplied model inputs, proposed mechanisms and unresolved information. Include every equation with units/domains, source return addresses, raw-data pointers, transformation versions, complete residuals and branch status.",
        "worked_example": {
          "id": "C30.07-W1",
          "task_and_answer": "Assemble a source-reading row for M20 with its18 core dependencies and supplied premises, an exact synthetic rank calculation, a prospective instrument protocol and the rehearsal residual(0,-1). Keep the missing named route certificate and the spectral cross-document revision discrepancy as source gaps; neither is filled by the toy calculation."
        },
        "guided_practice": {
          "id": "C30.07-P1",
          "task_and_answer": "Create four status rows: /a explicitly null; /b absent; /c string unknown; /d string reported. Retain presence/raw-kind separately so each can be read back. A source-stated proof, freshly checked arithmetic and proposed detector measurement receive different evidence labels and execution dates."
        },
        "diagnostic": {
          "id": "C30.07-D1",
          "task_and_answer": "A short summary must not replace the residual vectors or logical boundaries. When an archived branch endpoint has null exact_boundary but a constituent has limits, carry those limits forward as S03 AUD010 requires. Null is not an empty permission."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "Professional scientific communication",
        "original_assessment_target": "Write a reproducible report with sources, equations, residuals, and unresolved branches",
        "original_concept_ids": [
          "C30.07"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-06"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Reproducible reporting and raw field kinds",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-08",
      "title": "The integrated research defense",
      "entry_prerequisites": [
        "lesson-07"
      ],
      "concept_ids": [
        "C30.08"
      ],
      "worked_example_capability": "Defend a complete geometric-to-instrument chain and its next test",
      "assessment_target": "Defend a complete geometric-to-instrument chain and its next test",
      "later_use": "capstone",
      "core_minutes": 165,
      "teaching_anchor": {
        "lesson_id": "lesson-08",
        "concept_id": "C30.08",
        "explanation_id": "C30.08-E1",
        "bridge_to_teach": "Defend one continuous geometric-to-instrument chain using previously taught operations: exact geometry and coordinate transform; supplied motion/ruler and signal model; retained decoder/residual; explicit transfer; and a new independent test. Include all six determinant-line factors and trivialization where phase closure is invoked.",
        "worked_example": {
          "id": "C30.08-W1",
          "task_and_answer": "With an explicitly chosen scalar trivialization, toy factors(UV,light,reg,heavy,cap,induced)=(i,i,-1,-i,i,1) multiply to1. Deleting heavy leaves i, so six factors matter. This verifies finite arithmetic, not global determinant-line existence or every admitted sector. Preserve the original S02 M15 factor names and source topology/domain obligations."
        },
        "guided_practice": {
          "id": "C30.08-P1",
          "task_and_answer": "Use the previously taught M17 small decoder A=[[1,0],[0,1],[1,1]], y=(2,3,6), c=(7/3,10/3),r=(-1/3,-1/3,1/3); reconstruct every channel. Connect the proposed sum/difference instrument model through an explicit calibration requirement, then state the frozen prospective prediction and all failure branches. The source M20/M19 and compiler scopes remain distinct."
        },
        "diagnostic": {
          "id": "C30.08-D1",
          "task_and_answer": "Do not call a complete presentation a completed empirical theory. Retain missing route/precision/occupation or transfer bodies with their source status, all supplied state coordinates and the exact next test. No favorable experiment or unprovided certificate is invented."
        },
        "planned_periods": 3,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Expand into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all source cards, matrices, units and definitions locally. Keep original source data in place with immutable pointers. Add recovery periods when needed; no operation first appears in the capstone.",
        "original_title": "The integrated research defense",
        "original_assessment_target": "Defend a complete geometric-to-instrument chain and its next test",
        "original_concept_ids": [
          "C30.08"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-07"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Six determinant-line factors",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Decoder reconstruction and transfer",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 3,
            "focus": "Integrated defense with all source gaps",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Produce a senior research portfolio connecting at least one exact backbone construction to an instrument model, retained residual analysis, and a falsifiable independent test.",
    "required_operations": [
      "Connect the core modules and distinguish supplied premises from derived objects",
      "Read the scope of a proof, replay, calibration, and measurement",
      "Use a small inverse problem to test which parameters a measurement can recover",
      "Compare candidate mechanisms by predictions and parameter needs",
      "Freeze inputs, transformations, comparisons, and outcome handling",
      "Retain all outcomes and define the next informative measurement",
      "Write a reproducible report with sources, equations, residuals, and unresolved branches",
      "Defend a complete geometric-to-instrument chain and its next test"
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C30-CAP-01",
        "operation": "Connect the core modules and distinguish supplied premises from derived objects",
        "introduction": "lesson-01",
        "explanation_id": "C30.01-E1",
        "worked_example_id": "C30.01-W1",
        "prior_practice_id": "C30.01-P1",
        "diagnostic_id": "C30.01-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Trace backbone M17 from M05 and M11, then into M20; trace M18 from M03 and M04, then into M20. Keep M19 inputs M07,M08,M10,M13,M18 and its exceptional extensions on a separate branch. Classify EG-A2 as a constitutive decoder premise and c in the mass renderer as a supplied occupied-state coordinate, not a theorem choosing its value.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C30-CAP-02",
        "operation": "Read the scope of a proof, replay, calibration, and measurement",
        "introduction": "lesson-02",
        "explanation_id": "C30.02-E1",
        "worked_example_id": "C30.02-W1",
        "prior_practice_id": "C30.02-P1",
        "diagnostic_id": "C30.02-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Sort four cards: exact mean/detail reconstruction is finite algebra; a checker output with hash is a replay receipt; a known reference and transfer interval is calibration; timestamped detector values are observations. A planned detector run is a fifth card, a protocol. Assign source pointer and assumptions to each. Keep compiler M20 compositeNonterminal distinct from the attributed backbone M20 closure theorem.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C30-CAP-03",
        "operation": "Use a small inverse problem to test which parameters a measurement can recover",
        "introduction": "lesson-03",
        "explanation_id": "C30.03-E1",
        "worked_example_id": "C30.03-W1",
        "prior_practice_id": "C30.03-P1",
        "diagnostic_id": "C30.03-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For s=5,d=-1 recover theta=(2,3). Verify original rows give5 and10, and the new row gives-1. If a detector provides only product gain*responsivity=6, the pairs(2,3) and(1,6) remain indistinguishable without a separate calibration, even if a geometric model is exact.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C30-CAP-04",
        "operation": "Compare candidate mechanisms by predictions and parameter needs",
        "introduction": "lesson-04",
        "explanation_id": "C30.04-E1",
        "worked_example_id": "C30.04-W1",
        "prior_practice_id": "C30.04-P1",
        "diagnostic_id": "C30.04-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For thetaA=(2,1) and thetaB=(1,2), the sum measurement predicts3 for both and the difference predicts+1 versus-1. Freeze this discriminating sign prediction before a new calibrated measurement. Record equal-output candidates, any unresolved parameters and the alternative response each mechanism requires.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C30-CAP-05",
        "operation": "Freeze inputs, transformations, comparisons, and outcome handling",
        "introduction": "lesson-05",
        "explanation_id": "C30.05-E1",
        "worked_example_id": "C30.05-W1",
        "prior_practice_id": "C30.05-P1",
        "diagnostic_id": "C30.05-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Draft the real protocol as planned with raw acquisition destination in place, UTC midpoint convention, exposure duration, calibration reference/version, orientation convention and blinded operator labels. Unavailable instrument/calibration fields are marked missing with owners/return addresses. Analysis rules remain frozen; no readings are filled in.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C30-CAP-06",
        "operation": "Retain all outcomes and define the next informative measurement",
        "introduction": "lesson-06",
        "explanation_id": "C30.06-E1",
        "worked_example_id": "C30.06-W1",
        "prior_practice_id": "C30.06-P1",
        "diagnostic_id": "C30.06-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "If an independent future reading were(4,1), the frozen residual would be(1,0); label this conditional example, not an observation. A separate known-reference calibration can distinguish detector gain from a changed parameter sum. Retain both branches and the same frozen original predictions.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C30-CAP-07",
        "operation": "Write a reproducible report with sources, equations, residuals, and unresolved branches",
        "introduction": "lesson-07",
        "explanation_id": "C30.07-E1",
        "worked_example_id": "C30.07-W1",
        "prior_practice_id": "C30.07-P1",
        "diagnostic_id": "C30.07-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Create four status rows: /a explicitly null; /b absent; /c string unknown; /d string reported. Retain presence/raw-kind separately so each can be read back. A source-stated proof, freshly checked arithmetic and proposed detector measurement receive different evidence labels and execution dates.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C30-CAP-08",
        "operation": "Defend a complete geometric-to-instrument chain and its next test",
        "introduction": "lesson-08",
        "explanation_id": "C30.08-E1",
        "worked_example_id": "C30.08-W1",
        "prior_practice_id": "C30.08-P1",
        "diagnostic_id": "C30.08-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Use the previously taught M17 small decoder A=[[1,0],[0,1],[1,1]], y=(2,3,6), c=(7/3,10/3),r=(-1/3,-1/3,1/3); reconstruct every channel. Connect the proposed sum/difference instrument model through an explicit calibration requirement, then state the frozen prospective prediction and all failure branches. The source M20/M19 and compiler scopes remain distinct.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
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
    "teaching_review_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\teaching\\launch-review-28-30.json",
    "teaching_amendment_sha256": "f533beac5c5a374a225b00a0e5c43319079d12ff7fe3f59a00714594b3a6866d",
    "review_scope": "Blueprint clearance only. Actual lesson content and E05 links require independent final acceptance.",
    "applied_at": "2026-11-05T19:44:08.246370+00:00"
  },
  "validator": {
    "skill_relative_path": "scripts/validate_course.py",
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-30-integrated-k-field-research-from-backbone-to-test' --json"
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
    "SA-30": {
      "id": "SA-30",
      "course": 30,
      "finding": "source_fidelity",
      "lessons": [
        "lesson-01",
        "lesson-02",
        "lesson-04",
        "lesson-05"
      ],
      "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
      "requirements": [
        "Reconstruct M20 from M01-M18 plus constitutive principles, domain hypotheses, time/action normalization, vacuum/operator and occupied-state coordinates. M19 remains a separately retained extension.",
        "Preserve all six determinant-line factors and all constituent logical boundaries even where compressed branch endpoint exact_boundary is null.",
        "Keep integration's six minimal two-question experiment portfolios as designs, with no performed or favorable outcome inferred. Any current measurement case keeps its independent provenance.",
        "Treat explicit null, missing, unknown and source-reported statuses as distinct values with return addresses."
      ],
      "source_references": [
        "S02#/backbone_sequence/19",
        "S02#/constitutive_principles",
        "S03#/findings/0",
        "S03#/findings/9",
        "S03#/findings/10",
        "I01#/results/10",
        "I01#/open_obligations",
        "T30"
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
    "created_utc": "2026-11-05T19:43:16.419731+00:00",
    "scope": "Portable teaching BLUEPRINT amendments only; no completed-course acceptance.",
    "source_basis": [
      {
        "id": "S01",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Corrected_Complete_Proof_1788231864.json",
        "sha256": "18f5d20233981c97bf991e0b409020e917815647e5099df56ad9fa1763da6180",
        "role": "archival source; reported status is distinct from fresh verification",
        "hash_check": "verified locally; original source left in place",
        "evidence_class": "source"
      },
      {
        "id": "S02",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Mature_Complete_Proof_1788234894.json",
        "sha256": "6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3",
        "role": "archival source; reported status is distinct from fresh verification",
        "hash_check": "verified locally; original source left in place",
        "evidence_class": "source"
      },
      {
        "id": "S03",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Authoritative_Audit_Correction_Instruction_1788263935.json",
        "sha256": "f54c6c7515205dbbcc498864b1415755aa767d5274194140150b2b16979d656e",
        "role": "archival source; reported status is distinct from fresh verification",
        "hash_check": "verified locally; original source left in place",
        "evidence_class": "source"
      },
      {
        "id": "S04",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_Mathematical_Essence_Mature_Corpus_Audit_1788234146.json",
        "sha256": "77c0ab41a911fc819d3bcba0667d9127294b3dacf0634aec9add6e45e8c023a2",
        "role": "archival source; reported status is distinct from fresh verification",
        "hash_check": "verified locally; original source left in place",
        "evidence_class": "source"
      },
      {
        "id": "S05",
        "path": "Z:\\Archive_20260911\\Aug14_Sept1\\K-Field_3D_periodic_table_hidden_dimensions_recent24h_1788145361.json",
        "sha256": "d17197c1bec71893e1fd8344e0a35f6e63da3668f35dc3085247a66ad112eae7",
        "role": "archival source; reported status is distinct from fresh verification",
        "hash_check": "verified locally; original source left in place",
        "evidence_class": "source"
      },
      {
        "id": "G01",
        "path": "Z:/Archive_20260911/Pre_Aug14/galaxy_cell_hidden_holonomy_summary_1783791371.json",
        "sha256": "bd6ff0e335f3c405000cd1f8adfa3ae947dc9362dfeb772764cf98ef62ae6f63",
        "pointers": [
          "/ordered_direct_basis_A",
          "/reciprocal_basis_Q",
          "/joint_phase_origin",
          "/galaxy_cell_geometry",
          "/holonomy",
          "/observed_27_node_occupancy",
          "/pure_holonomy_coordinate_tests",
          "/comparison_to_authoritative_K_field"
        ],
        "scope": "Exact small record read; 114381-direction sky-position cell; phase origin is a reciprocal phase coordinate.",
        "evidence_class": "source",
        "hash_check": "verified before controlled stop"
      },
      {
        "id": "G02",
        "path": "Z:/Archive_20260911/Pre_Aug14/K-field_cell3_vs_galaxy_derived_cell_analogue_1783794540.pdf",
        "sha256": "69dcaace292365d22b9b48c43edc0ac4936b148ec68a5b265abc72aaff4f4447",
        "pages_read": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          17,
          18,
          19,
          20,
          21
        ],
        "locators": "p3 distinct axis versus sky-position pathways; p4 column basis, ICRS, positive galaxy determinant and unit-sphere reconstruction lengths; p8 frozen geometry; p17-20 occupancy, mixed coordinates and comparison boundaries.",
        "scope": "No radial physical calibration. Historical Cell3 carrier values p7 do not replace S02 mature lock.",
        "evidence_class": "source",
        "hash_check": "verified before controlled stop"
      },
      {
        "id": "G03",
        "path": "Z:/Archive_20260911/Pre_Aug14/K-field_spherical_gravity_response_graph_audited_1783692220.json",
        "sha256": "aa7f4236b7f956c652690934d6444f597ea38b6e485cc77a22be884b567d1cea",
        "pointers": [
          "/status",
          "/precision_contract",
          "/coordinate_frame",
          "/analytic_spherical_response",
          "/reconstruction_sequence"
        ],
        "scope": "Historical Cell3-derived spherical response, not the galaxy cell. Domain excludes n dot N=0; G_star=D/F has transfer singularities; absolute scalar calibration undefined. Large graph arrays were not exported.",
        "evidence_class": "source",
        "hash_check": "verified before controlled stop"
      },
      {
        "id": "G04",
        "path": "Z:/Archive_20260911/Pre_Aug14/K-field_galaxy_sky_position_volumetric_quantization_1783789746.pdf",
        "sha256": "856777f0fae0d6b50e8d235435068b7ea3c25a83068cfbfb197b62835cbb8fbd",
        "pages_read": [
          1,
          2,
          3,
          4
        ],
        "locators": "p3 unit-sphere direction, discovery57076/holdout57305 and antipodal discovery versus directed assignments; p4 q_j dot x=k_j+phi_j, R rows=q_j^T, A=R^-1, center=A(k+phi), closest-vector assignment and retained vector/angular/radial residuals.",
        "scope": "Phase origin phi and physical reconstruction center A phi have different types; closest-center assignment is not independent coordinate rounding in a skew metric.",
        "evidence_class": "source",
        "hash_check": "verified before controlled stop"
      }
    ],
    "source_registry_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\source-registry.json",
    "source_registry_sha256": "208a8ed59a10d72a74e1aa084b86d1f6809bb8f43168c7a98edc68598db5e78b",
    "pinned_application_reads": [
      {
        "id": "T50",
        "logical_path": "applications/kfield_lucas_lab/rag_corpus/50_physical_closure.md",
        "sha256": "c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a",
        "byte_range": [
          0,
          1761
        ],
        "read_status": "Full bounded bytes read through krytronx_get; returned range digest matched registry."
      },
      {
        "id": "T35",
        "logical_path": "applications/kfield_lucas_lab/rag_corpus/35_spectral_energy_phase.md",
        "sha256": "03dc7e11045b3912f1e8cc0d69a4789b6ad300ac78b4549ea86c45e51228c7bc",
        "byte_range": [
          0,
          3018
        ],
        "read_status": "Full bounded bytes read through krytronx_get; returned range digest matched registry."
      },
      {
        "id": "T45",
        "logical_path": "applications/kfield_lucas_lab/rag_corpus/45_moving_reference_frames.md",
        "sha256": "c8485397ee3cd5560624885a3bfcf20c9f6190e26129320e37037810b984e1aa",
        "byte_range": [
          0,
          2651
        ],
        "read_status": "Full bounded bytes read through krytronx_get; returned range digest matched registry."
      },
      {
        "id": "T40",
        "logical_path": "applications/kfield_lucas_lab/rag_corpus/40_cmb_quarantine.md",
        "sha256": "1dfff4443f99ebb949ca6f080a01452bdb6c58075a694c4b74055e64b4d4ecfb",
        "byte_range": [
          0,
          426
        ],
        "read_status": "Full bounded bytes read through krytronx_get; returned range digest matched registry."
      },
      {
        "id": "T20",
        "logical_path": "applications/kfield_lucas_lab/rag_corpus/20_phase_route.md",
        "sha256": "c9335e2df74344bff5665df5a5e0b9094fef22147c76458f1a54efe49cefce62",
        "byte_range": [
          0,
          470
        ],
        "read_status": "Full bounded bytes read through krytronx_get; returned range digest matched registry."
      },
      {
        "id": "T10",
        "logical_path": "applications/kfield_lucas_lab/rag_corpus/10_geometry_trajectory.md",
        "sha256": "ce1abe83011a43bfbcd8aaf98f7fb9fdfabd31acbfdbc1208e45176596602ccb",
        "byte_range": [
          0,
          545
        ],
        "read_status": "Full bounded bytes read through krytronx_get; returned range digest matched registry."
      },
      {
        "id": "spectral_bundle",
        "sha256": "04044230f3b2536d22654b294760106eca301f212e4eb4157989b330ff611f17",
        "byte_range": [
          0,
          6438
        ]
      },
      {
        "id": "spectral_work",
        "sha256": "d4105a6d6802e6bb2a2ba8e76a1d23a27973fca3d3335fd8335690a41ab72dfa",
        "byte_range": [
          0,
          48364
        ]
      },
      {
        "id": "energy_work",
        "sha256": "9120f80210b235b8612d6479fe25272eb3824f31c5a1394e7e9d12718e57e70f",
        "byte_range": [
          0,
          22424
        ]
      },
      {
        "id": "I01",
        "sha256": "3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c",
        "logical_path": "applications/kfield_standard_model/collaborator_record/project_record.json",
        "read_scope": "Full13847 bytes; results/9,results/10,hazards,open_obligations"
      },
      {
        "id": "I02",
        "sha256": "a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a",
        "logical_path": "kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json",
        "read_scope": "RAG lines1–101, direct-authority and replay fields"
      },
      {
        "id": "I03",
        "sha256": "01c849f3d184f367e0c53e1e00f521fa2fad98c1682d0aaa03e7de30667840ad",
        "logical_path": "kfield_standard_model/formal/KField/StandardModelCompilerAdjudication.agda",
        "read_scope": "RAG excerpts in lines1–199, readiness/disposition/routes; byte lookup unavailable, no compiler run"
      },
      {
        "id": "T30",
        "sha256": "e9c6d0346e7f4fa120e9836df9d4a45b7e2c587bc046874d91cb38a0c68c16bc",
        "byte_range": [
          0,
          687
        ],
        "read_scope": "Full bounded source text"
      }
    ],
    "verification_record": "C:\\Users\\info\\Documents\\Codex\\2026-11-05\\kfield-teaching-auditor\\outputs\\teaching-verification-28-30.json",
    "verification_sha256": "40b5b402379561e5b46439cf6d727ee1283bc1a7595bed2e6e4c15f26cbcabf8",
    "source_or_project_files_modified": false,
    "course_amendment": {
      "course_id": "course-30",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-30-integrated-k-field-research-from-backbone-to-test\\input-contract.json",
      "input_contract_sha256": "ef34c51ff7c0fdfb4bfeacf90ef0eb66d2ec3f21688e61be617a69bfef861052",
      "application": "Merge additively as teaching_amendment; preserve every original concept, SA/EA amendment and supplemental operation. Use exact exercise anchors and legacy aliases. Parent applies; no project edit performed.",
      "applied_source_amendments_read": {
        "SA-30": {
          "id": "SA-30",
          "course": 30,
          "finding": "source_fidelity",
          "lessons": [
            "lesson-01",
            "lesson-02",
            "lesson-04",
            "lesson-05"
          ],
          "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
          "requirements": [
            "Reconstruct M20 from M01-M18 plus constitutive principles, domain hypotheses, time/action normalization, vacuum/operator and occupied-state coordinates. M19 remains a separately retained extension.",
            "Preserve all six determinant-line factors and all constituent logical boundaries even where compressed branch endpoint exact_boundary is null.",
            "Keep integration's six minimal two-question experiment portfolios as designs, with no performed or favorable outcome inferred. Any current measurement case keeps its independent provenance.",
            "Treat explicit null, missing, unknown and source-reported statuses as distinct values with return addresses."
          ],
          "source_references": [
            "S02#/backbone_sequence/19",
            "S02#/constitutive_principles",
            "S03#/findings/0",
            "S03#/findings/9",
            "S03#/findings/10",
            "I01#/results/10",
            "I01#/open_obligations",
            "T30"
          ],
          "status": "applied_to_blueprint_by_parent",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        }
      },
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C30.01",
            "concept": "Rebuilding the complete dependency chain",
            "operation": "Connect the core modules and distinguish supplied premises from derived objects"
          },
          {
            "concept_id": "C30.02",
            "concept": "Formal witnesses and empirical witnesses",
            "operation": "Read the scope of a proof, replay, calibration, and measurement"
          },
          {
            "concept_id": "C30.03",
            "concept": "Interferometers and identifiable coupling",
            "operation": "Use a small inverse problem to test which parameters a measurement can recover"
          },
          {
            "concept_id": "C30.04",
            "concept": "Choosing discriminating experiments",
            "operation": "Compare candidate mechanisms by predictions and parameter needs"
          },
          {
            "concept_id": "C30.05",
            "concept": "Preregistering a complete protocol",
            "operation": "Freeze inputs, transformations, comparisons, and outcome handling"
          },
          {
            "concept_id": "C30.06",
            "concept": "Independent replication and negative outcomes",
            "operation": "Retain all outcomes and define the next informative measurement"
          },
          {
            "concept_id": "C30.07",
            "concept": "Professional scientific communication",
            "operation": "Write a reproducible report with sources, equations, residuals, and unresolved branches"
          },
          {
            "concept_id": "C30.08",
            "concept": "The integrated research defense",
            "operation": "Defend a complete geometric-to-instrument chain and its next test"
          }
        ],
        "source_modules": [
          "M20"
        ],
        "scope": "Produce a senior research portfolio connecting at least one exact backbone construction to an instrument model, retained residual analysis, and a falsifiable independent test.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Produce a senior research portfolio connecting at least one exact backbone construction to an instrument model, retained residual analysis, and a falsifiable independent test.",
        "required_operations": [
          "Connect the core modules and distinguish supplied premises from derived objects",
          "Read the scope of a proof, replay, calibration, and measurement",
          "Use a small inverse problem to test which parameters a measurement can recover",
          "Compare candidate mechanisms by predictions and parameter needs",
          "Freeze inputs, transformations, comparisons, and outcome handling",
          "Retain all outcomes and define the next informative measurement",
          "Write a reproducible report with sources, equations, residuals, and unresolved branches",
          "Defend a complete geometric-to-instrument chain and its next test"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-30",
          "title": "Integrated K-Field Research: From Backbone to Test",
          "backbone_modules": [
            "M20"
          ],
          "topic_boundary": "Complete M01-M18 premise audit, separately retained M19 branches, instrument identifiability and prospective experiments.",
          "cognitive_or_fidelity_risk": "Educational prerequisite course23 does not create a mathematical M19-to-M20 edge.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "series/source-registry.json"
          ],
          "source_pointer": "/backbone_sequence/19",
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-30-integrated-k-field-research-from-backbone-to-test\\input-contract.json",
            "sha256": "9fcf0d27d4723a4aba1ac23d5bbcbc3865656d9ccf188f4bc9d21965ec55c0dc",
            "lesson_count": 8
          },
          "required_amendment_ids": [
            "SA-30"
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
        "primary": [
          "S02",
          "S03",
          "I01",
          "I02",
          "I03",
          "T30",
          "SA30"
        ],
        "backbone": "Core M01–M18 with EG-A1–A6 and all supplied state coordinates feeds M20. M19 extensions remain separate. Preserve every dependency and inherited boundary.",
        "module_table": [
          {
            "id": "M01",
            "type": "D",
            "title": "Mature locked Cell3 and scale uniqueness",
            "requires": [],
            "definitions": [
              "B=B_nm is the locked labeled ICRS column basis [a b c]",
              "G=B^T B",
              "R=G^-1",
              "V=|det B|",
              "A_ij=||edge_i cross edge_j||",
              "(l_a,l_b,l_c)=t(1,k_b,k_c), t>0"
            ],
            "computation": [
              "G_ij=edge_i dot edge_j",
              "||edge_i||=sqrt(G_ii)",
              "theta_ij=acos(G_ij/sqrt(G_ii G_jj))",
              "A_ij=||c_ij||",
              "B R B^T=I"
            ],
            "result": {
              "B_nm": [
                [
                  0.3275012420558906,
                  0.0353307758438284,
                  -0.0101293176267288
                ],
                [
                  -0.0548970078840064,
                  0.2073198504401918,
                  -0.3897877023662599
                ],
                [
                  -0.0374875028947299,
                  -0.5474010853885081,
                  -0.6897344083672676
                ]
              ],
              "det_B_nm3": -0.11791489191174465,
              "volume_nm3": 0.11791489191174465,
              "face_areas_nm2": {
                "ab": 0.19486916546048413,
                "ac": 0.2611062357902053,
                "bc": 0.3578095391285615
              },
              "projective_ray_bc_ac_ab": [
                1.0,
                0.7297352564331424,
                0.5446170214888189
              ]
            },
            "invariants": [
              "det(B)<0",
              "G=G^T>0",
              "B R B^T=I"
            ],
            "proof": [
              "The locked matrix has det(B)=-0.11791489191174465<0, preserving the intentional left-handed orientation.",
              "G is positive definite because x^T G x=||Bx||^2>0 for x!=0.",
              "The angular frame and Mass-Bridge ratios give l_c/l_a=(eta/1000)sin(theta_ab)/sin(theta_bc) and l_b/l_a=(alpha^-1/100)sin(theta_ac)/sin(theta_bc).",
              "Thus one positive scale t is the only continuous freedom; the locked area anchor fixes t.",
              "R=G^-1 and B R B^T=I."
            ]
          },
          {
            "id": "M02",
            "type": "D",
            "title": "Affine partition and reciprocal-plane theorem",
            "requires": [
              "M01"
            ],
            "definitions": [
              "C_z=O_K+B(z+[-1/2,1/2)^3), z in Z^3",
              "q=B^{-1}(x-O_K)",
              "z=floor(q+1/2) componentwise",
              "u=q-z in [-1/2,1/2)^3",
              "g_h=B^{-T}h, h in Z^3"
            ],
            "proof": [
              "The half-open intervals [k-1/2,k+1/2) partition R uniquely.",
              "Their Cartesian product partitions R^3 uniquely in address coordinates.",
              "Invertibility of B transports this partition bijectively to physical ICRS space.",
              "g_h dot (Bk)=h^T k, so g_h dot x=m is the physical plane family with integer address level m.",
              "Adjacent levels differ by 1 in g_h dot x; therefore d_h=1/||g_h||."
            ],
            "boundary_rule": "An exact +1/2 coordinate belongs to the positive-index neighbor; exact -1/2 remains in the current cell.",
            "reciprocal_witness": {
              "u": {
                "normal": [
                  0.9959651903089612,
                  -0.08360216250737675,
                  0.032619290564399855
                ],
                "spacing_nm": 0.3295465297092934
              },
              "v": {
                "normal": [
                  0.08905259410160504,
                  0.8665767692910322,
                  -0.49103394832627595
                ],
                "spacing_nm": 0.4515973797241299
              },
              "w": {
                "normal": [
                  -0.19409220080776765,
                  -0.9131771688212287,
                  -0.35837923479080414
                ],
                "spacing_nm": 0.605097741514743
              }
            },
            "result": {
              "reciprocal_normals_u_v_w": [
                [
                  0.9959651903089612,
                  -0.08360216250737743,
                  0.03261929056440005
                ],
                [
                  0.0890525941016049,
                  0.8665767692910323,
                  -0.4910339483262759
                ],
                [
                  -0.19409220080776696,
                  -0.9131771688212286,
                  -0.3583792347908047
                ]
              ],
              "reciprocal_spacings_u_v_w_nm": [
                0.32954652969544673,
                0.4515973797212846,
                0.6050977415185554
              ],
              "boundary": "[-1/2,1/2)^3"
            }
          },
          {
            "id": "M03",
            "type": "D",
            "title": "Lucas sheets and two non-aliased recursion systems",
            "requires": [
              "M02"
            ],
            "definitions": [
              "p(L)=O_K+B L/2, L in {-1,0,1}^3",
              "lambda(L)=L_1+L_2+L_3",
              "chi(L)=(-1)^lambda",
              "g_lambda=B^{-T}(1,1,1)^T",
              "n_lambda=g_lambda/||g_lambda||",
              "h_lambda=1/(2||g_lambda||)"
            ],
            "proof": [
              "g_lambda dot p(L)=lambda/2, hence n_lambda dot p(L)=h_lambda lambda.",
              "chi(L)=exp(i pi lambda)=exp(i K_chi dot p(L)) with K_chi=2 pi g_lambda.",
              "The sheet population polynomial is (x^{-1}+1+x)^3=x^{-3}+3x^{-2}+6x^{-1}+7+6x+3x^2+x^3.",
              "The rung equation 3^g 2^n+1=10 has the unique nonnegative solution (g,n)=(2,0), fixing the 1,27,729 Cell3/Group/Supergroup hierarchy."
            ],
            "sheet_populations": {
              "lambda": [
                -3,
                -2,
                -1,
                0,
                1,
                2,
                3
              ],
              "population": [
                1,
                3,
                6,
                7,
                6,
                3,
                1
              ]
            },
            "sheet_spacing_nm": 0.15127268804248478,
            "positive_sheet_normal": [
              0.8769768663662008,
              0.04722312422998791,
              -0.47820660011806404
            ],
            "typed_finite_objects": {
              "lucas_limit": "the smallest centered address window with one negative, one zero, and one positive coordinate on each primitive axis",
              "lucas_window": "27 half-step nodes p(L), L in {-1,0,1}^3, classified as 8 vertices, 12 edge centers, 6 face centers, and 1 center",
              "lucas_group": "3x3x3 array of 27 complete Cell3 volumes with outer basis 3B",
              "lucas_supergroup": "9x9x9 array of 729 complete Cell3 volumes, equivalently 27 Lucas Groups",
              "supergroup_half_step_points": 6859,
              "devon_super_sheets": "For refined coordinates -9..9 on each axis, lambda spans -27..27 and gives 55 constant-lambda sheets."
            },
            "recursions": {
              "group_dyadic": {
                "formula": "B_{p,n}=3^p 2^{-n} B",
                "native_module": "B Z[1/2]^3",
                "group_root": "B_G=3B",
                "subcells_at_depth_n": "27*8^n",
                "merged_nodes_at_depth_n": "(3*2^n+1)^3"
              },
              "ternary_address": {
                "formula": "A_d=(Z/3^d Z)^3",
                "cardinality": "27^d",
                "bonding_map": "pi_d:A_{d+1}->A_d by coordinatewise reduction mod 3^d",
                "inverse_limit": "lim A_d = Z_3^3"
              }
            },
            "type_guard": "The dyadic depth n_2, ternary address depth g_3, and algebraic degree d are distinct coordinates.",
            "supergroup_uniqueness": {
              "equation": "3^g 2^n + 1 = 10",
              "domain": "g,n are nonnegative integers",
              "unique_solution": {
                "g": 2,
                "n": 0
              },
              "counts": {
                "Cell3": 1,
                "Lucas_Group": 27,
                "9B_Supergroup": 729
              }
            }
          },
          {
            "id": "M04",
            "type": "D",
            "title": "Information-complete constitutive finite calculus",
            "requires": [
              "M03"
            ],
            "definitions": [
              "d_e f=f(t(e))-f(s(e))",
              "nabla_e psi=U_e psi_t-psi_s",
              "I=P_0+sum_{n>=1}Q_n",
              "Q=I-E"
            ],
            "proof": [
              "Write f_t=f_s+df and g_t=g_s+dg.",
              "Then d(fg)=f_tg_t-f_sg_s=f_s dg+g_s df+(df)(dg).",
              "Equivalently d(fg)=f_s dg+(df)g_t.",
              "Applying Q=I-E to the exact product expansion gives Q(fg)=E(f)Q(g)+Q(f)E(g)+Q(f)Q(g)-E(Q(f)Q(g)).",
              "No remainder is discarded: f=E(f)+Q(f), and the detail product is retained as a new channel."
            ],
            "gauge_covariance": "psi_x->G_x psi_x and U_xy->G_x U_xy G_y^{-1} imply nabla_e psi->G_{s(e)} nabla_e psi.",
            "source_relation": "K psi=j remains primary on singular strata; inverse formulas are restricted to the invertible subspace and kernel/cokernel data are retained."
          },
          {
            "id": "M05",
            "type": "D",
            "title": "Cofactor quotient and Mass Bridge",
            "requires": [
              "M01",
              "M04"
            ],
            "definitions": [
              "r=(1,A_ac/A_bc,A_ab/A_bc) in [bc,ac,ab] order",
              "eta=1000 A_bc/A_ab",
              "alpha^{-1}=100 A_bc/A_ac",
              "eta alpha=10 A_ac/A_ab"
            ],
            "proof": [
              "Common scale cancels from every face-area quotient.",
              "The two independent ratios of three positive face areas determine the unique projective shape.",
              "The mature locked ray is the sole active ray and generates one recursive carry history."
            ],
            "witness": {
              "eta": 1836.1526734259999,
              "alpha": 0.0072973525643314245,
              "alpha_inverse": 137.035999177,
              "eta_alpha": 13.399053419929224
            },
            "projective_ray": [
              1.0,
              0.7297352564331424,
              0.5446170214888189
            ]
          },
          {
            "id": "M06",
            "type": "D",
            "title": "Lossless projective integerization",
            "requires": [
              "M05"
            ],
            "definitions": [
              "K_g=27^g",
              "Q_g=nint(K_g r) componentwise",
              "epsilon_g=Q_g-K_g r in [-1/2,1/2)^3",
              "C_g=Q_g-27Q_{g-1}=nint(-27 epsilon_{g-1})"
            ],
            "proof": [
              "Q_g=K_g r+epsilon_g and 27Q_{g-1}=K_g r+27epsilon_{g-1}.",
              "Subtracting gives C_g=epsilon_g-27epsilon_{g-1}.",
              "Because epsilon_g is the centered representative, C_g=nint(-27epsilon_{g-1}).",
              "Thus epsilon_g=27epsilon_{g-1}+C_g and Q_g=27Q_{g-1}+C_g.",
              "Iterating yields Q_g=27^g Q_0+sum_{j=1}^g 27^{g-j}C_j.",
              "Dividing by 27^g and taking the limit yields r=Q_0+sum_{j>=1}C_j/27^j."
            ],
            "locked_replay": [
              {
                "g": 0,
                "Q": [
                  1,
                  1,
                  1
                ],
                "C": null
              },
              {
                "g": 1,
                "Q": [
                  27,
                  20,
                  15
                ],
                "C": [
                  0,
                  -7,
                  -12
                ]
              },
              {
                "g": 2,
                "Q": [
                  729,
                  532,
                  397
                ],
                "C": [
                  0,
                  -8,
                  -8
                ]
              },
              {
                "g": 3,
                "Q": [
                  19683,
                  14363,
                  10720
                ],
                "C": [
                  0,
                  -1,
                  1
                ]
              },
              {
                "g": 4,
                "Q": [
                  531441,
                  387811,
                  289432
                ],
                "C": [
                  0,
                  10,
                  -8
                ]
              },
              {
                "g": 5,
                "Q": [
                  14348907,
                  10470903,
                  7814659
                ],
                "C": [
                  0,
                  6,
                  -5
                ]
              },
              {
                "g": 6,
                "Q": [
                  387420489,
                  282714390,
                  210995793
                ],
                "C": [
                  0,
                  9,
                  0
                ]
              },
              {
                "g": 7,
                "Q": [
                  10460353203,
                  7633288527,
                  5696886405
                ],
                "C": [
                  0,
                  -3,
                  -6
                ]
              },
              {
                "g": 8,
                "Q": [
                  282429536481,
                  206098790228,
                  153815932939
                ],
                "C": [
                  0,
                  -1,
                  4
                ]
              }
            ],
            "side_modes": {
              "S": "C_b+C_c",
              "A": "C_b-C_c",
              "inverse": [
                "C_b=(S+A)/2",
                "C_c=(S-A)/2"
              ],
              "lattice": "{(S,A) in Z^2: S congruent A mod 2}",
              "root_witness": "g=3 has C=(0,-1,+1), S=0, A=-2"
            },
            "active_ray": [
              1.0,
              0.7297352564331424,
              0.5446170214888189
            ]
          },
          {
            "id": "M07",
            "type": "D",
            "title": "Devon reduction and Jack invertibility",
            "requires": [
              "M01",
              "M05",
              "M06"
            ],
            "definitions": [
              "y=(ln A_ab,ln A_ac,ln A_bc)^T",
              "P_H=I-(1/3)11^T",
              "e_s=(1,1,1)/sqrt(3)",
              "e_u=(-1,1,0)/sqrt(2)",
              "e_v=(-1,-1,2)/sqrt(6)",
              "y=s e_s+u e_u+v e_v"
            ],
            "proof": [
              "Under B->rho B, y->y+2ln(rho)1; therefore P_H y is the complete scale-free two-coordinate shape.",
              "u=ln(A_ac/A_ab)/sqrt(2).",
              "v=ln(A_bc^2/(A_ab A_ac))/sqrt(6).",
              "For fixed included angles, (dln eta,dln alpha,dln Gamma2)^T=J_Jack(dln|a|,dln|b|,dln|c|)^T.",
              "J_Jack=[[-1,0,1],[1,-1,0],[17,-2,-3]] and det(J_Jack)=12!=0.",
              "Therefore two shape coordinates plus one scalar lift locally reconstruct all three coherent edge-scale perturbations."
            ],
            "jack_inverse": [
              "x_a=(dG-2dA+3dE)/12",
              "x_b=(dG-14dA+3dE)/12",
              "x_c=(dG-2dA+15dE)/12"
            ],
            "devon_dimension": "The typed reduced object containing direct metric, cofactors, reciprocal metric, common scale, A2 shape fiber, scalar lift, branch modes, and their invertible maps; its components are not collapsed into one untyped vector.",
            "locked_face_areas_nm2": {
              "ab": 0.19486916546048413,
              "ac": 0.2611062357902053,
              "bc": 0.3578095391285615
            }
          },
          {
            "id": "M08",
            "type": "D",
            "title": "Lucas graph, Emily eigen-spectrum, and memory spaces",
            "requires": [
              "M03",
              "M07"
            ],
            "definitions": [
              "G_L=P_3 square P_3 square P_3",
              "|V(G_L)|=27",
              "|E(G_L)|=3*(3-1)*3*3=54"
            ],
            "proof": [
              "G_L is connected, so an oriented incidence matrix has rank |V|-1=26.",
              "dim cut(G_L)=26 and dim cycle(G_L)=|E|-rank=54-26=28.",
              "The adjacency spectrum of P_3 is {sqrt(2),0,-sqrt(2)}.",
              "Cartesian-product adjacency eigenvalues add, so the Emily spectrum is m sqrt(2), m=-3..3.",
              "Multiplicities are coefficients of (x^{-1}+1+x)^3: 1,3,6,7,6,3,1.",
              "Inversion pairs 26 noncentral nodes and fixes the center; hence node functions split into 14 even and 13 odd dimensions. Removing the uniform even gauge leaves 13 even and 13 odd observable coordinates."
            ],
            "emily_spectrum": [
              {
                "eigenvalue": "-3sqrt(2)",
                "multiplicity": 1
              },
              {
                "eigenvalue": "-2sqrt(2)",
                "multiplicity": 3
              },
              {
                "eigenvalue": "-sqrt(2)",
                "multiplicity": 6
              },
              {
                "eigenvalue": "0",
                "multiplicity": 7
              },
              {
                "eigenvalue": "sqrt(2)",
                "multiplicity": 6
              },
              {
                "eigenvalue": "2sqrt(2)",
                "multiplicity": 3
              },
              {
                "eigenvalue": "3sqrt(2)",
                "multiplicity": 1
              }
            ],
            "periodic_augmentation": "Adding the 27 wrap-edge cycle coordinates gives 55 total cycle coordinates, decomposed as 28 open cycles plus 24 zero-sum wrap coordinates plus 3 global windings."
          },
          {
            "id": "M09",
            "type": "D",
            "title": "A1 side root and A2 primitive-lift root",
            "requires": [
              "M06",
              "M08"
            ],
            "definitions": [
              "L_W=Z e_b direct-sum Z e_c",
              "sigma_W=e_b+e_c",
              "alpha_W=e_b-e_c",
              "Q_1=2Z subset P_1=Z",
              "L_C=Z^3",
              "Q_2=ker(sum:Z^3->Z)",
              "u_1=(2,-1,-1)/3; u_2=(-1,2,-1)/3; u_3=(-1,-1,2)/3"
            ],
            "proof": [
              "A unit transfer (C_b,C_c)->(C_b+1,C_c-1) preserves S and changes A by 2, so the A1 root lattice is 2Z and P_1/Q_1=Z_2.",
              "Primitive-lift differences span x_a+x_b+x_c=0 and have Cartan matrix [[2,-1],[-1,2]], so this is A2.",
              "The weight/root quotient is P_2/Q_2=Z_3.",
              "The three centered weights sum to zero and form the defining three-channel representation."
            ],
            "type_guards": [
              "A1 carry parity is not detector antipodal parity.",
              "The three primitive lifts are not the three projective ray coordinates."
            ]
          },
          {
            "id": "M10",
            "type": "D",
            "title": "Complex 2+3 carrier and global gauge group",
            "requires": [
              "M09"
            ],
            "definitions": [
              "W=L_W tensor_Z C isomorphic C^2",
              "C=L_C tensor_Z C isomorphic C^3",
              "H=W direct-sum C",
              "Omega=det(W) tensor det(C)"
            ],
            "proof": [
              "Canonical complexification preserves the ordered integral bases and produces type projectors P_W and P_C with P_W P_C=0.",
              "A central phase acts with charge b on W and a on C.",
              "Preserving Omega requires det(U_W)det(U_C)=1, equivalently 2b+3a=0.",
              "The connected group preserving the Hermitian blocks and top form is S(U(2)xU(3)).",
              "The map Phi(g_3,g_2,z)=(z^{-2}g_3,z^3g_2) has kernel Z_6, hence S(U(3)xU(2)) isomorphic (SU(3)xSU(2)xU(1))/Z_6."
            ],
            "result": {
              "group": "S(U(2)xU(3))",
              "quotient": "(SU(3)xSU(2)xU(1))/Z_6",
              "descent_condition": "q+2t+3p congruent 0 mod 6",
              "hypercharge_on_H": "Y=(1/2)I_2 direct-sum (-1/3)I_3"
            }
          },
          {
            "id": "M11",
            "type": "D",
            "title": "Exterior matter and anomaly-fixed hypercharge",
            "requires": [
              "M10"
            ],
            "definitions": [
              "S_plus=Lambda^even H",
              "dim S_plus=sum_{k even} binom(5,k)=16",
              "q=6Y=-2r_C+3s_W on bidegree (r_C,s_W)"
            ],
            "sector_census": [
              {
                "bidegree": [
                  0,
                  0
                ],
                "representation": "(1,1)",
                "multiplicity": 1,
                "q": 0,
                "sector": "nu^c"
              },
              {
                "bidegree": [
                  0,
                  2
                ],
                "representation": "(1,1)",
                "multiplicity": 1,
                "q": 6,
                "sector": "e^c"
              },
              {
                "bidegree": [
                  1,
                  1
                ],
                "representation": "(3,2)",
                "multiplicity": 6,
                "q": 1,
                "sector": "Q"
              },
              {
                "bidegree": [
                  2,
                  0
                ],
                "representation": "(bar3,1)",
                "multiplicity": 3,
                "q": -4,
                "sector": "u^c"
              },
              {
                "bidegree": [
                  2,
                  2
                ],
                "representation": "(bar3,1)",
                "multiplicity": 3,
                "q": 2,
                "sector": "d^c"
              },
              {
                "bidegree": [
                  3,
                  1
                ],
                "representation": "(1,2)",
                "multiplicity": 2,
                "q": -3,
                "sector": "L"
              }
            ],
            "anomaly_computation": [
              "A_SU3^2U1=A_SU2^2U1=3a+2b",
              "A_grav^2U1=8(3a+2b)",
              "A_U1^3=(3a+2b)(36a^2+24ab+20b^2)",
              "The quadratic-factor matrix [[36,12],[12,20]] has positive leading minor 36 and determinant 576, hence 36a^2+24ab+20b^2>0 for (a,b)!=(0,0).",
              "Therefore simultaneous anomaly cancellation forces 3a+2b=0.",
              "The primitive integral solution is (a,b)=(-2,3) up to global sign, giving 6Y=(-2,-2,-2,3,3)."
            ],
            "result": "One sixteen-component left-Weyl family, including nu^c, with the Standard Model hypercharge census."
          },
          {
            "id": "M12",
            "type": "D",
            "title": "Higgs and Yukawa interface",
            "requires": [
              "M11"
            ],
            "definitions": [
              "I_u=Omega^{-1}(u^c wedge Q wedge H_Higgs)",
              "I_nu=nu^c Omega^{-1}(L wedge H_Higgs)",
              "I_d=Omega^{-1}(Q wedge iota_{bar H} d^c)",
              "I_e=Omega^{-1}(L wedge iota_{bar H} e^c)"
            ],
            "proof": [
              "Each contraction is an S(U(3)xU(2))-invariant scalar because color, weak, and hypercharge degrees sum to the top-form degree and zero total charge.",
              "For <H_Higgs>=(0,v/sqrt(2)), Q_electric=T_3+Y leaves one U(1) generator unbroken.",
              "The gauge-boson quadratic form gives m_W^2=g_2^2v^2/4 and m_Z^2=(g_2^2+g_Y^2)v^2/4, hence rho=1 at the compiler level."
            ],
            "state_coordinates": [
              "vacuum magnitude",
              "Higgs-potential coefficients",
              "Yukawa coefficient matrices",
              "mixing coordinates",
              "matching scale"
            ]
          },
          {
            "id": "M13",
            "type": "D",
            "title": "Finite gauge transport and Yang-Mills hierarchy",
            "requires": [
              "M04",
              "M10",
              "site-indexed compact-group links",
              "positive native plaquette/detail coefficients"
            ],
            "definitions": [
              "U_p=ordered product of links around plaquette p",
              "F_p=I-U_p or an equivalent retained group-valued curvature coordinate",
              "S_YM=sum_p beta_p Re Tr(I-U_p)",
              "C_tau=(I-i tau L_hat)(I+i tau L_hat)^(-1)",
              "H_E=tau^2 R=delta^(1/3)R",
              "H_B=tau^(-2) J M J^T=delta^(2/3) wedge^2(R)"
            ],
            "proof": [
              "Under U_xy->G_xU_xyG_y^{-1}, a closed plaquette transforms by conjugation, so Re Tr(I-U_p) is gauge invariant.",
              "If L_hat is self-adjoint, direct multiplication gives C_tau^dagger C_tau=I.",
              "For the Cell3 x time product, the electric and magnetic two-form Hodge blocks satisfy det(H_E)=det(H_B)=1 and J H_B J^T=H_E^{-1}.",
              "For the explicit finite native lattice compiler, the archived interval bounds epsilon_E<0.007744166 and epsilon_B<0.015868134 imply contraction alpha<=0.5244.",
              "The corresponding finite-rung transfer gap satisfies Delta>0.10185916 H_N/tau_R.",
              "For detail Hamiltonians h_{n,C}=2^n(H_N/tau_R)C with C>=c_*>0, the recursive gap obeys Delta_K>=min(Delta_root,2c_*)H_N/tau_R.",
              "The thermal detail sum converges because sum_{n>=0}8^n exp(-beta c_*2^n)<infinity."
            ],
            "status_partition": {
              "exact_finite_theorems": [
                "finite gauge covariance",
                "finite-rung gap on the pinned compiler",
                "Cayley unitarity",
                "determinant-normalized electric and magnetic Hodge blocks"
              ],
              "domain_hypotheses": [
                "site-indexed compact-group links",
                "positive native plaquette and detail coefficients"
              ],
              "optional_comparison_theorems": [
                "complete infinite-depth operator-domain comparison",
                "conventional continuum Yang-Mills mass-gap comparison"
              ]
            },
            "hodge_normalization_theorem": {
              "given": "delta=det(M)=V^2 and det(R)=delta^-1 in dimension 3",
              "electric": "det(delta^a R)=delta^(3a-1)=1 forces a=1/3",
              "magnetic": "det(wedge^2 R)=delta^-2, so det(delta^b wedge^2 R)=delta^(3b-2)=1 forces b=2/3",
              "correct": [
                "H_E=delta^(1/3)R",
                "H_B=delta^(2/3) wedge^2 R"
              ]
            }
          },
          {
            "id": "M14",
            "type": "D",
            "title": "History isometry and physical chirality",
            "requires": [
              "M03",
              "M11"
            ],
            "definitions": [
              "F_hist=l^2(B_8^*)",
              "S_b e_w=e_{bw}",
              "S_b^dagger S_c=delta_bc I",
              "sum_b S_b S_b^dagger=I-P_Omega",
              "W^dagger W=I and WW^dagger!=I",
              "q_n=W^n P_Pi (W^dagger)^n",
              "{gamma_K^mu,gamma_K^nu}=2g_K^{mu nu}I",
              "gamma_5=i gamma_0 gamma_1 gamma_2 gamma_3",
              "P_L=(I-gamma_5)/2; P_R=(I+gamma_5)/2"
            ],
            "proof": [
              "Prefixing different branch letters gives orthogonal ranges, proving the Toeplitz-Cuntz relations.",
              "If P_Pi lies in the root defect space, q_n^2=q_n=q_n^dagger and q_n q_m=0 for n!=m.",
              "The left-handed Cell3 spatial coframe plus the forward history covector fixes the oriented K4 coframe used in gamma_5.",
              "Clifford anticommutation implies gamma_5^2=I and {gamma_5,gamma_mu}=0, hence P_L and P_R are orthogonal idempotents.",
              "Spacetime chirality and exterior parity commute because they act on distinct tensor factors."
            ],
            "correlated_projector": "Pi_phys=P_L tensor P_even + P_R tensor P_odd",
            "index": "On the radial history subspace, Ind(T_0)=-1; tensoring with the retained matter/family carrier transports the signed chiral class."
          },
          {
            "id": "M15",
            "type": "D",
            "title": "Action, topology, measure, and phase closure",
            "requires": [
              "M10",
              "M13",
              "M14"
            ],
            "action": "S_K[q]=int d tau sum_L {mu_L/2 dot(q_L)^T M dot(q_L)-kappa_K/2 tr(M Q_L R Q_L^T)-epsilon_K U_K(Cq_L)+s_L^Tq_L}",
            "topology": [
              "ell:det E_3 tensor det E_2 -> 1",
              "c=c_1(E_2)=-c_1(E_3)",
              "n_3=A_3+C/3; n_2=A_2+C/4; n_1=C/72",
              "dual charges satisfy d_3 in Z, d_2 in Z, d_3/3+d_2/4+d_1/72 in Z"
            ],
            "determinant_line": [
              "S_total=s_UV tensor s_light tensor s_reg tensor s_heavy tensor s_cap tensor s_induced",
              "tau:L_total->C is a trivialization",
              "Phi_total_hat(sigma)=1 for every admitted sector sigma is the phase-closure condition"
            ],
            "proof": [
              "Every action term is typed on a declared carrier and contracts all free indices.",
              "The quotient charge lattice follows from the Z_6 descent relation and the determinant lock.",
              "The total phase is defined only after tensoring every determinant-line contribution; no individual factor may be silently deleted."
            ],
            "state_coordinates": [
              "operator coefficients",
              "boundary-sector values",
              "time/action normalization"
            ]
          },
          {
            "id": "M16",
            "type": "D",
            "title": "Finite family transition and simultaneous occupation",
            "requires": [
              "M11",
              "M14"
            ],
            "definitions": [
              "X=F_3^3",
              "lambda(x)=x_1+x_2+x_3 mod 3",
              "C_r=lambda^{-1}(r)",
              "Phi_r=(1/3)sum_{x in C_r}delta_x",
              "W_r={f in C^{C_r}:sum_x f(x)=0}",
              "C^X=U_lambda direct-sum W_0 direct-sum W_1 direct-sum W_2",
              "U_lambda=span{Phi_0,Phi_1,Phi_2}"
            ],
            "all_lifts": "V_lift f=(1/3)sum_{v in L}P_v f tensor |v>, with V_lift^dagger V_lift=I_27",
            "weyl_basis": [
              "B_ab=D^aP^b",
              "Y=sum_ab y_ab D^aP^b",
              "y_ab=(1/3)Tr((D^aP^b)^dagger Y)"
            ],
            "schur_interface": [
              "K=[[A,B],[C,E]]",
              "S=A-BE^{-1}C",
              "r=s_U-BE^{-1}s_W",
              "w=E^{-1}(s_W-Cu)",
              "det K=(det E)(det S)"
            ],
            "family_projector": {
              "formula": "Q_n=I_16 tensor I_3 tensor q_n",
              "rank": 48,
              "occupation": [
                1,
                1,
                1
              ],
              "proof": [
                "rank(I_16)=16, rank(I_3)=3, rank(q_n)=1.",
                "rank(A tensor B tensor C)=rank(A)rank(B)rank(C), so rank(Q_n)=16*3*1=48.",
                "The identity I_3 acts uniformly on all three family labels; restriction to each label has rank one history occupation, giving (1,1,1).",
                "Q_n^2=Q_n, Q_n^dagger=Q_n, Q_nQ_m=0 for n!=m, and history covariance transports all three labels identically."
              ]
            },
            "type_guard": "Family labels are not inferred from projective channels; simultaneous occupation follows from the explicit I_3 tensor factor."
          },
          {
            "id": "M17",
            "type": "D",
            "title": "Six-coordinate mass/coupling decoder with retained seven-coordinate syndrome",
            "requires": [
              "M05",
              "M11"
            ],
            "basis": "b=(1,alpha,alpha^2,alpha^3,a_e,eta)",
            "channel_matrix_A": [
              [
                0,
                0,
                1,
                0,
                0,
                0
              ],
              [
                0,
                1,
                0,
                0,
                0,
                0
              ],
              [
                0,
                1,
                1,
                0,
                0,
                1
              ],
              [
                0,
                1,
                1,
                0,
                0,
                -1
              ],
              [
                1,
                0,
                0,
                0,
                0,
                0
              ],
              [
                1,
                0,
                1,
                0,
                1,
                0
              ],
              [
                1,
                0,
                1,
                0,
                -1,
                0
              ],
              [
                1,
                1,
                0,
                1,
                0,
                0
              ],
              [
                1,
                1,
                1,
                1,
                1,
                1
              ],
              [
                1,
                1,
                1,
                1,
                -1,
                -1
              ],
              [
                1,
                1,
                0,
                -1,
                0,
                0
              ],
              [
                1,
                1,
                1,
                -1,
                1,
                -1
              ],
              [
                1,
                1,
                1,
                -1,
                -1,
                1
              ]
            ],
            "decoder": [
              "y=A c+s",
              "c=(A^T A)^{-1}A^T y",
              "s=(I-AA^+)y in ker(A^T)",
              "m/m_e=c dot b"
            ],
            "rank_proof": [
              "A^T A has a 3x3 block [[9,6,6],[6,9,6],[6,6,9]] with eigenvalues 21,3,3.",
              "Its remaining diagonal block is diag(6,6,6).",
              "All six eigenvalues are positive, so rank(A)=6.",
              "For A in R^{13x6}, left-nullity=13-rank(A)=7.",
              "Therefore the six decoded coefficients and seven-dimensional residual syndrome form a lossless 13-coordinate decomposition."
            ],
            "mass_bridge_basis_witness": {
              "alpha": 0.0072973525643314245,
              "eta": 1836.1526734259999,
              "a_e": "occupied-state coordinate"
            },
            "information_rule": "The syndrome s is a primary retained coordinate, not a scalar fit score.",
            "renderer_scope": "m/m_e=c dot b is deterministic on an occupied coefficient state; y=Ac+s retains six active and seven syndrome coordinates exactly."
          },
          {
            "id": "M18",
            "type": "D",
            "title": "Inverse-limit continuum renderer",
            "requires": [
              "M03",
              "M04"
            ],
            "definitions": [
              "A_d=(Z/3^d Z)^3",
              "pi_d:A_{d+1}->A_d",
              "A_infinity=lim_inverse A_d isomorphic Z_3^3",
              "r(u)=(B/2)sum_{n>=1}3^{-n}u_n, u_n in {-1,0,1}^3"
            ],
            "proof": [
              "Compatibility pi_d(a_{d+1})=a_d defines a unique 3-adic address.",
              "The real renderer converges absolutely because ||u_n|| is bounded and sum 3^{-n} converges.",
              "After depth N, the coordinate tail is bounded by (1/2)sum_{n>N}3^{-n}=1/(4*3^N) per normalized coordinate.",
              "Cylinder observables depend on a finite prefix and pull back consistently to all finer depths.",
              "The filtration I=P_0+sum_{n>=0}Q_n retains each detail sector, so the limit does not erase finite-rung information."
            ],
            "duality": "Real ICRS coordinates render the convergent geometric image; Z_3^3 retains the exact recursive address history.",
            "result": "The mature continuum object is the ordered pair (exact 3-adic address history, convergent real ICRS image) with explicit tail bound."
          },
          {
            "id": "M19",
            "type": "D+E",
            "title": "Dependency-bearing branches",
            "requires": [
              "M07",
              "M08",
              "M10",
              "M13",
              "M18"
            ],
            "branches": {
              "gravity_scalar_lift": {
                "formulas": [
                  "dln Gamma2=9dln A_ab+8dln A_ac-11dln A_bc",
                  "G_Gamma=9y_ab+8y_ac-11y_bc",
                  "y_ab=(G_Gamma-8F+3M)/6",
                  "y_ac=(G_Gamma-2F+9M)/6",
                  "y_bc=(G_Gamma-8F+9M)/6"
                ],
                "result": "F, M, and Gamma2 reconstruct all three log face areas; Gamma2 is a scalar lift, not a fourth shape coordinate."
              },
              "exceptional_cycle_bridge": {
                "exact_counts": [
                  "dim cycle(P3 square P3 square P3)=28",
                  "periodic augmentation adds 27=24+3 coordinates",
                  "55=52+3 with 52 zero-sum/open-cycle coordinates and 3 global windings",
                  "dim H^2((Z_3)^3,Z_3)=6, giving 3^6=729 cohomology classes",
                  "the stabilizer of one octonion unit is SU(3)",
                  "the Euclidean Albert algebra supplies compact F4"
                ],
                "exceptional_action_extension": [
                  "identification of the 52-cycle sector with a specific F4 action",
                  "selection of E6/E7 real forms",
                  "physical coupling of cohomology classes"
                ]
              },
              "reciprocal_plane_inversion": {
                "formulas": [
                  "2d sin(theta)=m lambda_wave",
                  "d=m lambda_wave/(2|sin theta|)",
                  "Gamma_B=ln d+ln|sin theta|-ln lambda_wave=ln(m/2)",
                  "q=n_hat/d=3^{+/-g}B^{-T}h+rho",
                  "Delta ln d=ln 3 between adjacent linear recursion depths"
                ],
                "branch_identity": "sin(pi-theta)=sin(theta), so same-side and opposite-side solutions preserve d.",
                "residual": "rho is retained as the next reciprocal-address coordinate."
              }
            },
            "result": "The gravity scalar lift, reciprocal-plane inversion, cycle/cohomology counts, and exceptional carriers are exact; unique exceptional actions require explicit intertwiners."
          },
          {
            "id": "M20",
            "type": "D",
            "title": "Mature closure theorem",
            "requires": [
              "M01",
              "M02",
              "M03",
              "M04",
              "M05",
              "M06",
              "M07",
              "M08",
              "M09",
              "M10",
              "M11",
              "M12",
              "M13",
              "M14",
              "M15",
              "M16",
              "M17",
              "M18"
            ],
            "theorem": "The mature locked Cell3 generates a dependency-complete, scale-covariant compiler through exact geometry, information-complete finite calculus, lossless projective quantization, forced A1+A2 internal modules, S(U(2)xU(3)), a 16-state exterior matter family, exact typed interactions, finite gauge/history/chiral dynamics, simultaneous rank-48 three-family occupation, lossless six-coordinate plus seven-syndrome decoding, and paired 3-adic/real-ICRS continuum rendering.",
            "proof": [
              "M01-M03 fix the locked oriented root, half-open volume filling, reciprocal planes, sheet algebra, and 1/27/729 hierarchy.",
              "M04-M08 establish constitutive lossless calculus, the unique Mass-Bridge ray, exact recursive integerization, scale/shape separation, and Lucas graph structure.",
              "M09-M11 force A1+A2, C^2 direct-sum C^3, the determinant-locked global group, primitive hypercharge, and the complete 16-state family.",
              "M12-M16 establish exact typed interactions, determinant-normalized Hodge/gauge transport, oriented history chirality, retained action sectors, and simultaneous occupation (1,1,1).",
              "M17-M18 close lossless numerical decoding and the paired exact-address/convergent-ICRS continuum renderer."
            ],
            "state_coordinates": [
              "uniform scale before the locked area anchor",
              "time/action normalization",
              "vacuum magnitude and admitted operator coefficients",
              "occupied six-coordinate mass/coupling state"
            ],
            "optional_comparison_theorems": [
              "Osterwalder-Schrader or conventional Lorentzian equivalence",
              "conventional continuum Yang-Mills mass-gap comparison",
              "full quotient-bundle bordism verification beyond the finite carrier theorem"
            ],
            "exceptional_extension": [
              "unique 52-cycle-to-F4 action",
              "unique E6/E7 real-form selector",
              "physical cohomology coupling action"
            ]
          }
        ],
        "compiler": "Compiler M labels are a separate namespace. I02 direct-authority M03,M07,M08 does not transfer authority by numeral to backbone modules. Compiler M20 compositeNonterminal is distinct from the attributed backbone closure theorem.",
        "determinant_line": "Retain UV, light, regulator, heavy, cap and induced factors, trivialization, topology and admitted sectors. Toy scalar multiplication is not proof of global line triviality.",
        "evidence": "Proof, finite replay, calibration, measurement, prospective protocol and independent replication remain distinct. Integration experiment portfolios are designs; no favorable experiments were invented.",
        "source_gaps": "Full named route certificate and complete locked G_phase,C,W precision linkage remain unavailable. Preserve AUD008 nonzero residual, AUD009 unloaded bodies, source revision mismatches and inherited boundaries."
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "Rebuilding the complete dependency chain",
          "entry_prerequisites": [
            "course-19",
            "course-20",
            "course-21",
            "course-22",
            "course-23",
            "course-27",
            "course-28",
            "course-29"
          ],
          "concept_ids": [
            "C30.01"
          ],
          "worked_example_capability": "Connect the core modules and distinguish supplied premises from derived objects",
          "assessment_target": "Connect the core modules and distinguish supplied premises from derived objects",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-30"
          ],
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C30.01-E1",
          "worked_example_id": "C30.01-W1",
          "prior_practice_id": "C30.01-P1",
          "diagnostic_id": "C30.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Formal witnesses and empirical witnesses",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C30.02"
          ],
          "worked_example_capability": "Read the scope of a proof, replay, calibration, and measurement",
          "assessment_target": "Read the scope of a proof, replay, calibration, and measurement",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-30"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C30.02-E1",
          "worked_example_id": "C30.02-W1",
          "prior_practice_id": "C30.02-P1",
          "diagnostic_id": "C30.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "Interferometers and identifiable coupling",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C30.03"
          ],
          "worked_example_capability": "Use a small inverse problem to test which parameters a measurement can recover",
          "assessment_target": "Use a small inverse problem to test which parameters a measurement can recover",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C30.03-E1",
          "worked_example_id": "C30.03-W1",
          "prior_practice_id": "C30.03-P1",
          "diagnostic_id": "C30.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "Choosing discriminating experiments",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C30.04"
          ],
          "worked_example_capability": "Compare candidate mechanisms by predictions and parameter needs",
          "assessment_target": "Compare candidate mechanisms by predictions and parameter needs",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-30"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C30.04-E1",
          "worked_example_id": "C30.04-W1",
          "prior_practice_id": "C30.04-P1",
          "diagnostic_id": "C30.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "Preregistering a complete protocol",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C30.05"
          ],
          "worked_example_capability": "Freeze inputs, transformations, comparisons, and outcome handling",
          "assessment_target": "Freeze inputs, transformations, comparisons, and outcome handling",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-30"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C30.05-E1",
          "worked_example_id": "C30.05-W1",
          "prior_practice_id": "C30.05-P1",
          "diagnostic_id": "C30.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "Independent replication and negative outcomes",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C30.06"
          ],
          "worked_example_capability": "Retain all outcomes and define the next informative measurement",
          "assessment_target": "Retain all outcomes and define the next informative measurement",
          "later_use": "lesson-07",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C30.06-E1",
          "worked_example_id": "C30.06-W1",
          "prior_practice_id": "C30.06-P1",
          "diagnostic_id": "C30.06-D1"
        },
        {
          "id": "lesson-07",
          "title": "Professional scientific communication",
          "entry_prerequisites": [
            "lesson-06"
          ],
          "concept_ids": [
            "C30.07"
          ],
          "worked_example_capability": "Write a reproducible report with sources, equations, residuals, and unresolved branches",
          "assessment_target": "Write a reproducible report with sources, equations, residuals, and unresolved branches",
          "later_use": "lesson-08",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C30.07-E1",
          "worked_example_id": "C30.07-W1",
          "prior_practice_id": "C30.07-P1",
          "diagnostic_id": "C30.07-D1"
        },
        {
          "id": "lesson-08",
          "title": "The integrated research defense",
          "entry_prerequisites": [
            "lesson-07"
          ],
          "concept_ids": [
            "C30.08"
          ],
          "worked_example_capability": "Defend a complete geometric-to-instrument chain and its next test",
          "assessment_target": "Defend a complete geometric-to-instrument chain and its next test",
          "later_use": "capstone",
          "core_minutes": 55,
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C30.08-E1",
          "worked_example_id": "C30.08-W1",
          "prior_practice_id": "C30.08-P1",
          "diagnostic_id": "C30.08-D1"
        }
      ],
      "legacy_bridge_aliases": [],
      "core_periods": 16,
      "capstone_periods": 3,
      "period_minutes": 55,
      "capstone_total_points": 32,
      "capstone_sessions": [
        "55 minutes: assemble the typed input/source ledger and first calculation.",
        "55 minutes: complete every mapped operation and retain signed components and domain failures.",
        "55 minutes: reconstruct, classify evidence and audit all source boundaries; repair with the point rubric."
      ],
      "core_boundary": "Finite computations use fully declared synthetic inputs. Source-event reading preserves every row by immutable reference. Source numeric replay is gated until complete inputs and precision contracts are pinned. Galaxy geometry retains its unit-sphere domain. Compiler labels remain distinct from backbone labels. No absent source value is invented.",
      "prerequisite_status": "Blueprint closure reviewed; produced senior-facing lessons, diagnostics, answered practice and capstone still require independent completed-course acceptance.",
      "inline_content_location": "Complete lesson anchors are in course_map[*].teaching_anchor; complete capstone mapping is in capstone_specification.backward_map below."
    },
    "completed_course_acceptance": false
  }
}
```
