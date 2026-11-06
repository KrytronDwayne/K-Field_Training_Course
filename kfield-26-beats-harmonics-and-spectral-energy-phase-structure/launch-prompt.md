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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-26-beats-harmonics-and-spectral-energy-phase-structure",
  "topic": "Beats, Harmonics, and Spectral Energy–Phase Structure",
  "series_course_id": "course-26",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-12",
    "Capabilities taught in course-14",
    "Capabilities taught in course-25"
  ],
  "learning_outcomes": [
    "Read and reconstruct a sinusoid with stated units",
    "Derive a two-frequency beat example",
    "Relate integer harmonics to the declared trajectory geometry",
    "Reconstruct a short signal from signed complex coefficients",
    "Compare channels without losing polarity or reference definitions",
    "Calculate a source-defined energy equivalent and state its physical meaning",
    "Read the retained spectral ledger without treating repeated levels as independent inputs",
    "Carry all unexplained components into a new comparison"
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
      "logical_path": "applications/kfield_lucas_lab/rag_corpus/35_spectral_energy_phase.md",
      "object_id": "03dc7e11045b3912f1e8cc0d69a4789b6ad300ac78b4549ea86c45e51228c7bc",
      "sha256": "03dc7e11045b3912f1e8cc0d69a4789b6ad300ac78b4549ea86c45e51228c7bc",
      "role": "Pinned testbench source; retrieve bounded bytes through krytronx_get and follow its exact underlying contract."
    },
    {
      "logical_path": "applications/kfield_lucas_lab/rag_corpus/50_physical_closure.md",
      "object_id": "c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a",
      "sha256": "c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a",
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
    "required_modules": [],
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
        "concept_id": "C26.01",
        "concept": "Oscillations, frequency, and phase",
        "operation": "Read and reconstruct a sinusoid with stated units"
      },
      {
        "concept_id": "C26.02",
        "concept": "Superposition and beat envelopes",
        "operation": "Derive a two-frequency beat example"
      },
      {
        "concept_id": "C26.03",
        "concept": "Harmonics and spatial rulers",
        "operation": "Relate integer harmonics to the declared trajectory geometry"
      },
      {
        "concept_id": "C26.04",
        "concept": "Spectral coefficients retain phase",
        "operation": "Reconstruct a short signal from signed complex coefficients"
      },
      {
        "concept_id": "C26.05",
        "concept": "Cross-channel phase and wavelength",
        "operation": "Compare channels without losing polarity or reference definitions"
      },
      {
        "concept_id": "C26.06",
        "concept": "Photon-equivalent model energy",
        "operation": "Calculate a source-defined energy equivalent and state its physical meaning"
      },
      {
        "concept_id": "C26.07",
        "concept": "Signed event evidence",
        "operation": "Read the retained spectral ledger without treating repeated levels as independent inputs"
      },
      {
        "concept_id": "C26.08",
        "concept": "Residual spectra as the next measurement",
        "operation": "Carry all unexplained components into a new comparison"
      },
      {
        "concept_id": "C26.S01",
        "concept": "Parity and comparator nullspaces",
        "operation": "Show on a short periodic sequence that antipodal symmetry removes odd harmonics; retain those channels and distinguish the ternary scale ladder from the Fibonacci-cutoff and proposed beat branches."
      }
    ],
    "source_modules": [],
    "scope": "Analyze a completely specified synthetic beat signal, reconstruct it, and compare its evidence layers with one pinned archive event.",
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
      "concept_id": "C26.01",
      "concept": "Oscillations, frequency, and phase",
      "introduction": "lesson-01",
      "practice": "C26.01-P1",
      "assessment": "C26.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C26.01-W1",
      "all_required_teaching_item_ids": [
        "C26.01-E1",
        "C26.01-W1",
        "C26.01-P1",
        "C26.01-D1"
      ]
    },
    {
      "concept_id": "C26.02",
      "concept": "Superposition and beat envelopes",
      "introduction": "lesson-02",
      "practice": "C26.02-P1",
      "assessment": "C26.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C26.02-W1",
      "all_required_teaching_item_ids": [
        "C26.02-E1",
        "C26.02-W1",
        "C26.02-P1",
        "C26.02-D1"
      ]
    },
    {
      "concept_id": "C26.03",
      "concept": "Harmonics and spatial rulers",
      "introduction": "lesson-03",
      "practice": "C26.03-P1",
      "assessment": "C26.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C26.03-W1",
      "all_required_teaching_item_ids": [
        "C26.03-E1",
        "C26.03-W1",
        "C26.03-P1",
        "C26.03-D1"
      ]
    },
    {
      "concept_id": "C26.04",
      "concept": "Spectral coefficients retain phase",
      "introduction": "lesson-04",
      "practice": "C26.04-P1",
      "assessment": "C26.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C26.04-W1",
      "all_required_teaching_item_ids": [
        "C26.04-E1",
        "C26.04-W1",
        "C26.04-P1",
        "C26.04-D1"
      ]
    },
    {
      "concept_id": "C26.05",
      "concept": "Cross-channel phase and wavelength",
      "introduction": "lesson-05",
      "practice": "C26.05-P1",
      "assessment": "C26.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C26.05-W1",
      "all_required_teaching_item_ids": [
        "C26.05-E1",
        "C26.05-W1",
        "C26.05-P1",
        "C26.05-D1",
        "C26.S01-E1",
        "C26.S01-W1",
        "C26.S01-P1",
        "C26.S01-D1"
      ]
    },
    {
      "concept_id": "C26.06",
      "concept": "Photon-equivalent model energy",
      "introduction": "lesson-06",
      "practice": "C26.06-P1",
      "assessment": "C26.06-D1",
      "later_use": "lesson-07",
      "worked_example": "C26.06-W1",
      "all_required_teaching_item_ids": [
        "C26.06-E1",
        "C26.06-W1",
        "C26.06-P1",
        "C26.06-D1"
      ]
    },
    {
      "concept_id": "C26.07",
      "concept": "Signed event evidence",
      "introduction": "lesson-07",
      "practice": "C26.07-P1",
      "assessment": "C26.07-D1",
      "later_use": "lesson-08",
      "worked_example": "C26.07-W1",
      "all_required_teaching_item_ids": [
        "C26.07-E1",
        "C26.07-W1",
        "C26.07-P1",
        "C26.07-D1"
      ]
    },
    {
      "concept_id": "C26.08",
      "concept": "Residual spectra as the next measurement",
      "introduction": "lesson-08",
      "practice": "C26.08-P1",
      "assessment": "C26.08-D1",
      "later_use": "capstone",
      "worked_example": "C26.08-W1",
      "all_required_teaching_item_ids": [
        "C26.08-E1",
        "C26.08-W1",
        "C26.08-P1",
        "C26.08-D1"
      ]
    },
    {
      "concept_id": "C26.S01",
      "concept": "Parity and comparator nullspaces",
      "introduction": "lesson-05",
      "practice": "lesson-05: worked example and guided practice",
      "assessment": "lesson-05: diagnostic checks",
      "later_use": "course-28",
      "source_pointers": [
        "S05#/records/15",
        "S05#/records/16",
        "S05#/records/20",
        "S05#/records/25",
        "S05#/records/26",
        "S05#/records/27"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "Oscillations, frequency, and phase",
      "entry_prerequisites": [
        "course-12",
        "course-14",
        "course-25"
      ],
      "concept_ids": [
        "C26.01"
      ],
      "worked_example_capability": "Read and reconstruct a sinusoid with stated units",
      "assessment_target": "Read and reconstruct a sinusoid with stated units",
      "later_use": "lesson-02",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C26.01",
        "explanation_id": "C26.01-E1",
        "bridge_to_teach": "Teach radians, period, frequency f in cycles/s, omega=2pi f in radians/s, amplitude and phase offset. Use x(t)=A cos(2pi f t+phi)+b with x units declared. Review cosine addition and sine quadrature before beats or complex notation.",
        "worked_example": {
          "id": "C26.01-W1",
          "task_and_answer": "Synthetic x(t)=2 cos(pi t+pi/2)+1 counts, f=1/2Hz,T=2s. At t=0,1/2,1,3/2s the samples are1,-1,1,3 counts. Negative AC values are signed departures from the baseline1, not missing observations."
        },
        "guided_practice": {
          "id": "C26.01-P1",
          "task_and_answer": "For y(t)=3 cos(2pi t) counts, f=1Hz and samples at0,1/4,1/2,3/4s are3,0,-3,0. Record the sample spacing1/4s and order. A phase increase pi sends the cosine AC part to its negative."
        },
        "diagnostic": {
          "id": "C26.01-D1",
          "task_and_answer": "Frequency and angular frequency differ by2pi. Phase is relative to a time origin and reference; a magnitude alone cannot determine it. Retain the baseline and every signed sample."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "original_title": "Oscillations, frequency, and phase",
        "original_assessment_target": "Read and reconstruct a sinusoid with stated units",
        "original_concept_ids": [
          "C26.01"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "course-12",
          "course-14",
          "course-25"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Unit circle, sine/cosine and frequency",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Phase, timing and signed samples",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Superposition and beat envelopes",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C26.02"
      ],
      "worked_example_capability": "Derive a two-frequency beat example",
      "assessment_target": "Derive a two-frequency beat example",
      "later_use": "lesson-03",
      "core_minutes": 110,
      "required_amendment_ids": [
        "EA-26-E10-8"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C26.02",
        "explanation_id": "C26.02-E1",
        "bridge_to_teach": "Derive cos(a+b)=cos a cos b-sin a sin b and cos(a-b)=cos a cos b+sin a sin b. Add them, then substitute a=(u+v)/2,b=(u-v)/2. Distinguish the signed modulation factor from its absolute envelope.",
        "worked_example": {
          "id": "C26.02-W1",
          "task_and_answer": "cos(2pi*4t)+cos(2pi*6t)=2cos(2pi*t)cos(2pi*5t). Carrier average is5Hz; signed factor has1Hz frequency, while absolute-envelope maxima recur at2Hz. Evaluate t=0:2; t=1/4:0."
        },
        "guided_practice": {
          "id": "C26.02-P1",
          "task_and_answer": "C26-BEAT-P1: cos(2pi*5t)+cos(2pi*7t)=2cos(2pi*t)cos(2pi*6t). Carrier6Hz, signed-factor1Hz, absolute-envelope peak rate2Hz. At t=1/2, the sum=-2 and the signed factor=-2; replacing it by its magnitude would lose phase."
        },
        "diagnostic": {
          "id": "C26.02-D1",
          "task_and_answer": "The envelope peak rate is |f1-f2|, not the frequency of the signed cosine factor. Equal frequencies give a constant factor in this zero-relative-phase example; a general relative phase must be carried explicitly."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "original_title": "Superposition and beat envelopes",
        "original_assessment_target": "Derive a two-frequency beat example",
        "original_concept_ids": [
          "C26.02"
        ],
        "required_source_amendment_ids": [
          "EA-26-E10-8"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-01"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Addition formulas and beat derivation",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Signed factor versus absolute envelope",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-03",
      "title": "Harmonics and spatial rulers",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C26.03"
      ],
      "worked_example_capability": "Relate integer harmonics to the declared trajectory geometry",
      "assessment_target": "Relate integer harmonics to the declared trajectory geometry",
      "later_use": "lesson-04",
      "core_minutes": 55,
      "required_amendment_ids": [
        "EA-26-E10-8"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C26.03",
        "explanation_id": "C26.03-E1",
        "bridge_to_teach": "A fixed spatial phase q(t)=n dot(x-o)/d supplies a signed temporal frequency qdot. A kth harmonic has phase2pi kq, integer k and the same origin convention. Harmonic arithmetic does not establish a particular physical coupling pathway.",
        "worked_example": {
          "id": "C26.03-W1",
          "task_and_answer": "For q=2t cycles, the fundamental is2Hz and k=3 is6Hz, with signal cos(12pi t). Reversing motion changes phase to-12pi t; cosine alone is even, so retain a sine/quadrature channel to expose reversal."
        },
        "guided_practice": {
          "id": "C26.03-P1",
          "task_and_answer": "For d=1/2m and n dot v=-1m/s, qdot=-2s^-1; k=2 gives signed rate-4s^-1. Its cosine samples can match a positive-rate cosine, but sin(-8pi t)=-sin(8pi t). Record both reference phases."
        },
        "diagnostic": {
          "id": "C26.03-D1",
          "task_and_answer": "Ternary scale indices1,3,9,27 are not identical to all integer harmonics or to a proposed Fibonacci-cutoff ladder. Declared geometry and preserved odd information are required to compare those branches."
        },
        "planned_periods": 1,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "original_title": "Harmonics and spatial rulers",
        "original_assessment_target": "Relate integer harmonics to the declared trajectory geometry",
        "original_concept_ids": [
          "C26.03"
        ],
        "required_source_amendment_ids": [
          "EA-26-E10-8"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-02"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Spatial phase and integer harmonics",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "Spectral coefficients retain phase",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C26.04"
      ],
      "worked_example_capability": "Reconstruct a short signal from signed complex coefficients",
      "assessment_target": "Reconstruct a short signal from signed complex coefficients",
      "later_use": "lesson-05",
      "core_minutes": 165,
      "required_amendment_ids": [
        "EA-26-E10-8"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C26.04",
        "explanation_id": "C26.04-E1",
        "bridge_to_teach": "Enumerate i^0=1,i^1=i,i^2=-1,i^3=-i. For n,k=0..3 define X_k=sum x_n exp(-2pi i k n/4), inverse x_n=(1/4)sum X_k exp(+2pi i k n/4). Write the four rows before calculation. Record dt and frequencies k/(4dt), with k=3 represented as negative frequency-1/(4dt) for real signals.",
        "worked_example": {
          "id": "C26.04-W1",
          "task_and_answer": "C26-DFT-EX1: x=(1,0,-1,0) gives X=(0,2,0,2). A one-sample delay y=(0,1,0,-1) gives Y=(0,-2i,0,2i), same magnitudes and different phase. Substitute all four inverse sums to recover each sample, including zeros."
        },
        "guided_practice": {
          "id": "C26.04-P1",
          "task_and_answer": "C26-DFT-P1 constant(1,1,1,1) gives(4,0,0,0). Then transform(1,2,3,4) to(10,-2+2i,-2,-2-2i) and reconstruct. Delaying to(4,1,2,3) multiplies coefficient k by exp(-2pi i k/4). Keep DC, Nyquist, both conjugate coefficients and their order."
        },
        "diagnostic": {
          "id": "C26.04-D1",
          "task_and_answer": "C26-DFT-D1: magnitude-only spectra cannot distinguish x from its delayed version. The inverse needs signs, phases and factor1/4; dropping them is a noninvertible transform whose removed information must be retained."
        },
        "planned_periods": 3,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "original_title": "Spectral coefficients retain phase",
        "original_assessment_target": "Reconstruct a short signal from signed complex coefficients",
        "original_concept_ids": [
          "C26.04"
        ],
        "required_source_amendment_ids": [
          "EA-26-E10-8"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-03"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Powers of i and four DFT sums",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Complete inverse and delay phases",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 3,
            "focus": "Constant/general practice and magnitude failure",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "Cross-channel phase and wavelength",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C26.05",
        "C26.S01"
      ],
      "worked_example_capability": "Compare channels without losing polarity or reference definitions",
      "assessment_target": "Compare channels without losing polarity or reference definitions",
      "later_use": "lesson-06",
      "core_minutes": 165,
      "source_coverage_requirements": [
        {
          "concept_id": "C26.S01",
          "operation": "Show on a short periodic sequence that antipodal symmetry removes odd harmonics; retain those channels and distinguish the ternary scale ladder from the Fibonacci-cutoff and proposed beat branches.",
          "source_pointers": [
            "S05#/records/15",
            "S05#/records/16",
            "S05#/records/20",
            "S05#/records/25",
            "S05#/records/26",
            "S05#/records/27"
          ]
        }
      ],
      "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
      "required_amendment_ids": [
        "SA-26"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C26.05",
        "explanation_id": "C26.05-E1",
        "bridge_to_teach": "Compare complex channel coefficients against a declared reference only when that reference is nonzero. Keep wavelength, gain, timing, polarity and transform convention. For four angles C0,C90,C180,C270, teach M=(C0+C180)/2,Q=(C90+C270)/2 and half-differences D0,D90. Then reconstruct all four counts from M,Q,D0,D90.",
        "worked_example": {
          "id": "C26.05-W1",
          "task_and_answer": "Synthetic counts(8,4,6,2) give M=7,Q=3,D0=1,D90=1, count contrast G=M-Q=4 and fractional gain g=4/3. With |v dot n|=3 speed units,c=10 same units,sin(theta)=3/5, rho=1/2 and P=8/3. Reconstruct(7+1,3+1,7-1,3-1)."
        },
        "guided_practice": {
          "id": "C26.05-P1",
          "task_and_answer": "Counts(2,5,4,3) give M=3,Q=4,D0=-1,D90=1,G=-1,g=-1/4 and P=-1/2 for the same rho. A coefficient pair reference2, channel-2i has ratio-i; reverse the channel sign and the ratio becomes+i. If reference0, keep both coefficients and mark the ratio undefined."
        },
        "diagnostic": {
          "id": "C26.05-D1",
          "task_and_answer": "Q=0 makes g undefined; rho=0 makes P undefined; sin(theta)=0 makes rho undefined. Preserve counts and any defined intermediate coordinates in every case. The source JSON calls fractional gain G, while T35 calls count contrast G and fractional gain g; use explicit typed names."
        },
        "planned_periods": 3,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "supplemental_exercises": [
          {
            "concept_id": "C26.S01",
            "explanation_id": "C26.S01-E1",
            "worked_example_id": "C26.S01-W1",
            "prior_practice_id": "C26.S01-P1",
            "diagnostic_id": "C26.S01-D1",
            "explanation": "Define half-turn Hx at index n as x_(n+2 mod4). E=(I+H)/2 and O=(I-H)/2 obey E+O=I and EO=0. For a continuous periodic signal, half-turn symmetry multiplies Fourier mode k by(-1)^k, forcing odd k to vanish only in the even comparator. It does not force measured odd information to vanish.",
            "worked_task_and_answer": "For x=(1,2,3,4), Ex=(2,3,2,3), Ox=(-1,-1,1,1). Their four-point spectra occupy even and odd indices respectively. Dot(Ex,Ox)=0, and every circular shift of the even comparator stays even; a correlation with that comparator is blind to the odd subspace. Keep Ox in the output.",
            "practice_task_and_answer": "For x=(3,1,-1,1), Ex=(1,1,1,1), Ox=(2,0,-2,0), and sum=x. Source R017/R021 explain why native odd indices1,3,9,27 lie in an even comparator nullspace. R026 gives cutoff/dimension synthesis; R027 compares27 versus25 and difference2; R028 calls that beat pathway retained, not a closed identity.",
            "diagnostic_task_and_answer": "R016 reports odd rotational AC fractions about0.504–0.536 across nine channels; the toy does not replay those measurements. A four-point DFT aliases indices modulo4 and cannot resolve25 from other congruent indices. Preserve the ternary ladder, Fibonacci-cutoff proposal and measured odd information as separate records."
          }
        ],
        "original_title": "Cross-channel phase and wavelength",
        "original_assessment_target": "Compare channels without losing polarity or reference definitions",
        "original_concept_ids": [
          "C26.05",
          "C26.S01"
        ],
        "required_source_amendment_ids": [
          "SA-26"
        ],
        "source_coverage_requirements": [
          {
            "concept_id": "C26.S01",
            "operation": "Show on a short periodic sequence that antipodal symmetry removes odd harmonics; retain those channels and distinguish the ternary scale ladder from the Fibonacci-cutoff and proposed beat branches.",
            "source_pointers": [
              "S05#/records/15",
              "S05#/records/16",
              "S05#/records/20",
              "S05#/records/25",
              "S05#/records/26",
              "S05#/records/27"
            ]
          }
        ],
        "original_entry_prerequisites": [
          "lesson-04"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Complex reference ratios and four-angle reconstruction",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Domain failures and source notation",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 3,
            "focus": "C26.S01 even/odd comparator nullspace",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "Photon-equivalent model energy",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C26.06"
      ],
      "worked_example_capability": "Calculate a source-defined energy equivalent and state its physical meaning",
      "assessment_target": "Calculate a source-defined energy equivalent and state its physical meaning",
      "later_use": "lesson-07",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-26"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C26.06",
        "explanation_id": "C26.06-E1",
        "bridge_to_teach": "Under T35 and the energy-work estimator, input-equivalent model energy is g*LED_band_power*exposure. The power interval and calibration status are inputs. Photon-equivalent count divides by h c/lambda with all units supplied; it is not an observed integer photon count or transferred energy.",
        "worked_example": {
          "id": "C26.06-W1",
          "task_and_answer": "Synthetic g=4/3,power=3 energy-units/time-unit, exposure2 time-units gives8 energy-units. With toy h=6 energy*time,c=10 length/time,lambda=3 length, photon energy20 energy-units and equivalent count2/5. For power interval[3,6], the model energy interval is[8,16]."
        },
        "guided_practice": {
          "id": "C26.06-P1",
          "task_and_answer": "With g=-1/4 and the same positive power interval/exposure, signed energy-equivalent interval is[-3,-3/2], reordered after multiplying by a negative value. The arithmetic is a separately synthetic signed extension; the source energy subset has5 selected positive rows, not all8 positive-gain events. Leave other source energy fields null, not zero."
        },
        "diagnostic": {
          "id": "C26.06-D1",
          "task_and_answer": "The source calibration, exposure transfer and revision manifest obligations remain open. Gain/responsivity pairs(2,3) and(1,6) both yield scalar output6, so that output alone does not identify transfer. A modeled energy interval cannot select one factorization."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "original_title": "Photon-equivalent model energy",
        "original_assessment_target": "Calculate a source-defined energy equivalent and state its physical meaning",
        "original_concept_ids": [
          "C26.06"
        ],
        "required_source_amendment_ids": [
          "SA-26"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Model energy, units and photon equivalent",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Intervals, signed extensions and transfer boundary",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-07",
      "title": "Signed event evidence",
      "entry_prerequisites": [
        "lesson-06"
      ],
      "concept_ids": [
        "C26.07"
      ],
      "worked_example_capability": "Read the retained spectral ledger without treating repeated levels as independent inputs",
      "assessment_target": "Read the retained spectral ledger without treating repeated levels as independent inputs",
      "later_use": "lesson-08",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-26"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-07",
        "concept_id": "C26.07",
        "explanation_id": "C26.07-E1",
        "bridge_to_teach": "Read T35 and the pinned bundle before the canonical spectral/energy JSONs. Two works have PDF/JSON/abstract representations; they are not six studies. Preserve all14 rows with source pointers, paired-event IDs, time, channel, family, signed gain and every residual. qF=n^T G_phase n, g and P=g/rho have distinct types.",
        "worked_example": {
          "id": "C26.07-W1",
          "task_and_answer": "The pinned spectral /events ledger has14 rows: w4,v4,lambda6, with8 positive and6 negative gains. Only three q_plane levels occur: w1.777875828850227,v5.949871981229392,lambda5.7964545517567245. Five rows carry energy intervals. Read /events/3 (445-555:555:v): gain is negative and P=-0.4873061982197916; retain it beside its positive partner."
        },
        "guided_practice": {
          "id": "C26.07-P1",
          "task_and_answer": "For /events/0 (415-515:415:w), g=0.0005055808785109474,rho=0.0000574509228616101 gives P approximately8.800222056115778. Its source energy field is null. Link the energy-work /all_event_channel_modulations/0 counts and retain the pair half-differences/reconstruction closure in the verification record. Identify three cost inputs, not14 independent cost levels; never collapse the14 response rows."
        },
        "diagnostic": {
          "id": "C26.07-D1",
          "task_and_answer": "The bundle remains reported_exploratory_to_be_verified and records an energy-revision mismatch and PDF digest mismatch. Label these supplied provenance conditions. Four-degree acquisition spacing is not replaced by sub-degree interpolation precision. Source family alias lambda-sheet -> lambda is explicit, not silent."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "original_title": "Signed event evidence",
        "original_assessment_target": "Read the retained spectral ledger without treating repeated levels as independent inputs",
        "original_concept_ids": [
          "C26.07"
        ],
        "required_source_amendment_ids": [
          "SA-26"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-06"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "All14 signed rows and three cost levels",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Source event, provenance and precision ledger",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-08",
      "title": "Residual spectra as the next measurement",
      "entry_prerequisites": [
        "lesson-07"
      ],
      "concept_ids": [
        "C26.08"
      ],
      "worked_example_capability": "Carry all unexplained components into a new comparison",
      "assessment_target": "Carry all unexplained components into a new comparison",
      "later_use": "capstone",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-26"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-08",
        "concept_id": "C26.08",
        "explanation_id": "C26.08-E1",
        "bridge_to_teach": "Decompose a signal with a declared represented component and full residual, then transform both with the same linear DFT and inverse. Carry their sum, phases, temporal order and channel definitions into the next comparison. For each undefined denominator, retain the input row and a reason rather than imputing zero.",
        "worked_example": {
          "id": "C26.08-W1",
          "task_and_answer": "For x=(1,2,3,4), represented even part=(2,3,2,3) and odd residual=(-1,-1,1,1). Spectra are(10,0,-2,0) and(0,-2+2i,0,-2-2i); sum recovers the full spectrum and inverse recovers x. Even-only comparison has no access to the retained odd coordinates."
        },
        "guided_practice": {
          "id": "C26.08-P1",
          "task_and_answer": "For x=(3,1,-1,1), even part=(1,1,1,1), odd part=(2,0,-2,0). Their spectra are(4,0,0,0) and(0,4,0,4); retain both. Add the three domain-failure examples Q=0,rho=0,sin(theta)=0 from lesson05 to the report with all four original counts and defined intermediates."
        },
        "diagnostic": {
          "id": "C26.08-D1",
          "task_and_answer": "A small residual score is not the residual signal. The source native odd ladder and proposed25/27 difference pathway remain distinct from a four-sample aliasing example; no native high harmonic is resolved merely by this tiny DFT."
        },
        "planned_periods": 2,
        "minutes_per_period": 55,
        "teaching_allocation_per_period": {
          "retrieval": 5,
          "explanation_and_worked_example": 20,
          "guided_practice": 15,
          "independent_diagnostics_and_repair": 15
        },
        "production_requirement": "Develop these anchors into senior-facing explanations, 2–4 observable goals and 3–5 answered diagnostics. Supply all matrices, source cards and constants locally. Keep source data in place with immutable references. Additional recovery periods are allowed; no capstone operation may first appear in the assessment.",
        "original_title": "Residual spectra as the next measurement",
        "original_assessment_target": "Carry all unexplained components into a new comparison",
        "original_concept_ids": [
          "C26.08"
        ],
        "required_source_amendment_ids": [
          "SA-26"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-07"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Full residual DFT reconstruction",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Next comparison and unresolved-domain ledger",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Analyze a completely specified synthetic beat signal, reconstruct it, and compare its evidence layers with one pinned archive event.",
    "required_operations": [
      "Read and reconstruct a sinusoid with stated units",
      "Derive a two-frequency beat example",
      "Relate integer harmonics to the declared trajectory geometry",
      "Reconstruct a short signal from signed complex coefficients",
      "Compare channels without losing polarity or reference definitions",
      "Calculate a source-defined energy equivalent and state its physical meaning",
      "Read the retained spectral ledger without treating repeated levels as independent inputs",
      "Carry all unexplained components into a new comparison",
      "Show on a short periodic sequence that antipodal symmetry removes odd harmonics; retain those channels and distinguish the ternary scale ladder from the Fibonacci-cutoff and proposed beat branches."
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C26-CAP-01",
        "operation": "Read and reconstruct a sinusoid with stated units",
        "introduction": "lesson-01",
        "explanation_id": "C26.01-E1",
        "worked_example_id": "C26.01-W1",
        "prior_practice_id": "C26.01-P1",
        "diagnostic_id": "C26.01-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For y(t)=3 cos(2pi t) counts, f=1Hz and samples at0,1/4,1/2,3/4s are3,0,-3,0. Record the sample spacing1/4s and order. A phase increase pi sends the cosine AC part to its negative.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-02",
        "operation": "Derive a two-frequency beat example",
        "introduction": "lesson-02",
        "explanation_id": "C26.02-E1",
        "worked_example_id": "C26.02-W1",
        "prior_practice_id": "C26.02-P1",
        "diagnostic_id": "C26.02-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "C26-BEAT-P1: cos(2pi*5t)+cos(2pi*7t)=2cos(2pi*t)cos(2pi*6t). Carrier6Hz, signed-factor1Hz, absolute-envelope peak rate2Hz. At t=1/2, the sum=-2 and the signed factor=-2; replacing it by its magnitude would lose phase.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-03",
        "operation": "Relate integer harmonics to the declared trajectory geometry",
        "introduction": "lesson-03",
        "explanation_id": "C26.03-E1",
        "worked_example_id": "C26.03-W1",
        "prior_practice_id": "C26.03-P1",
        "diagnostic_id": "C26.03-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For d=1/2m and n dot v=-1m/s, qdot=-2s^-1; k=2 gives signed rate-4s^-1. Its cosine samples can match a positive-rate cosine, but sin(-8pi t)=-sin(8pi t). Record both reference phases.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-04",
        "operation": "Reconstruct a short signal from signed complex coefficients",
        "introduction": "lesson-04",
        "explanation_id": "C26.04-E1",
        "worked_example_id": "C26.04-W1",
        "prior_practice_id": "C26.04-P1",
        "diagnostic_id": "C26.04-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "C26-DFT-P1 constant(1,1,1,1) gives(4,0,0,0). Then transform(1,2,3,4) to(10,-2+2i,-2,-2-2i) and reconstruct. Delaying to(4,1,2,3) multiplies coefficient k by exp(-2pi i k/4). Keep DC, Nyquist, both conjugate coefficients and their order.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-05",
        "operation": "Compare channels without losing polarity or reference definitions",
        "introduction": "lesson-05",
        "explanation_id": "C26.05-E1",
        "worked_example_id": "C26.05-W1",
        "prior_practice_id": "C26.05-P1",
        "diagnostic_id": "C26.05-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Counts(2,5,4,3) give M=3,Q=4,D0=-1,D90=1,G=-1,g=-1/4 and P=-1/2 for the same rho. A coefficient pair reference2, channel-2i has ratio-i; reverse the channel sign and the ratio becomes+i. If reference0, keep both coefficients and mark the ratio undefined.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-06",
        "operation": "Calculate a source-defined energy equivalent and state its physical meaning",
        "introduction": "lesson-06",
        "explanation_id": "C26.06-E1",
        "worked_example_id": "C26.06-W1",
        "prior_practice_id": "C26.06-P1",
        "diagnostic_id": "C26.06-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "With g=-1/4 and the same positive power interval/exposure, signed energy-equivalent interval is[-3,-3/2], reordered after multiplying by a negative value. The arithmetic is a separately synthetic signed extension; the source energy subset has5 selected positive rows, not all8 positive-gain events. Leave other source energy fields null, not zero.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-07",
        "operation": "Read the retained spectral ledger without treating repeated levels as independent inputs",
        "introduction": "lesson-07",
        "explanation_id": "C26.07-E1",
        "worked_example_id": "C26.07-W1",
        "prior_practice_id": "C26.07-P1",
        "diagnostic_id": "C26.07-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For /events/0 (415-515:415:w), g=0.0005055808785109474,rho=0.0000574509228616101 gives P approximately8.800222056115778. Its source energy field is null. Link the energy-work /all_event_channel_modulations/0 counts and retain the pair half-differences/reconstruction closure in the verification record. Identify three cost inputs, not14 independent cost levels; never collapse the14 response rows.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-08",
        "operation": "Carry all unexplained components into a new comparison",
        "introduction": "lesson-08",
        "explanation_id": "C26.08-E1",
        "worked_example_id": "C26.08-W1",
        "prior_practice_id": "C26.08-P1",
        "diagnostic_id": "C26.08-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For x=(3,1,-1,1), even part=(1,1,1,1), odd part=(2,0,-2,0). Their spectra are(4,0,0,0) and(0,4,0,4); retain both. Add the three domain-failure examples Q=0,rho=0,sin(theta)=0 from lesson05 to the report with all four original counts and defined intermediates.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C26-CAP-09",
        "operation": "Show on a short periodic sequence that antipodal symmetry removes odd harmonics; retain those channels and distinguish the ternary scale ladder from the Fibonacci-cutoff and proposed beat branches.",
        "introduction": "lesson-05",
        "concept_id": "C26.S01",
        "explanation_id": "C26.S01-E1",
        "worked_example_id": "C26.S01-W1",
        "prior_practice_id": "C26.S01-P1",
        "diagnostic_id": "C26.S01-D1",
        "assessment_task": "Complete the even/odd practice reconstruction and classify the source parity and proposed beat branches.",
        "answer_key": "For x=(3,1,-1,1), Ex=(1,1,1,1), Ox=(2,0,-2,0), and sum=x. Source R017/R021 explain why native odd indices1,3,9,27 lie in an even comparator nullspace. R026 gives cutoff/dimension synthesis; R027 compares27 versus25 and difference2; R028 calls that beat pathway retained, not a closed identity.",
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
    "teaching_review_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-series-20261105\\audits\\teaching\\launch-review-24-27.json",
    "teaching_amendment_sha256": "d5c160b344f6e3230757148c5f8469bdaac175dc00fc5c30451b28e6dace421c",
    "review_scope": "Blueprint clearance only. Actual lesson content and E05 links require independent final acceptance.",
    "applied_at": "2026-11-05T19:25:46.018916+00:00"
  },
  "validator": {
    "skill_relative_path": "scripts/validate_course.py",
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-26-beats-harmonics-and-spectral-energy-phase-structure' --json"
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
    "SA-26": {
      "id": "SA-26",
      "course": 26,
      "finding": "source_fidelity",
      "lessons": [
        "lesson-05",
        "lesson-06",
        "lesson-07",
        "lesson-08"
      ],
      "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
      "requirements": [
        "Retain reported_exploratory_to_be_verified for the spectral bundle, distinguish its two works from their PDF/JSON/abstract representations, and preserve all signed rows.",
        "Fourteen rows contain three independent plane-cost values. qF=n^T G_phase n, signed gain and input-equivalent energy have different types; calibration/transfer obligations remain explicit.",
        "Retain the exact four-angle formulas and denominator domains Q!=0, rho!=0 and sin(theta)!=0. Mark undefined results without dropping input rows.",
        "Preserve C26.S01 comparator nullspace and source S05 parity/beat branches; an even comparator cannot test retained odd modes."
      ],
      "source_references": [
        "T35",
        "S05#/records/16",
        "S05#/records/20",
        "S05#/records/27"
      ],
      "status": "applied_to_blueprint_by_parent",
      "prior_application_status": "prepared_not_applied",
      "applied_at": "2026-11-05T17:02:05.375955+00:00"
    },
    "EA-26-E10-8": {
      "course": 26,
      "finding": "E10",
      "lessons": [
        "lesson-02",
        "lesson-03",
        "lesson-04"
      ],
      "required_bridge": "Derive cos(a)+cos(b)=2cos((a-b)/2)cos((a+b)/2) from taught addition rules; identify signed amplitude factor versus its absolute envelope and define frequency convention. Teach a four-sample DFT by enumerating powers of i, with both transform signs and inverse factor specified.",
      "worked_example": {
        "id": "C26-DFT-EX1",
        "samples": [
          1,
          0,
          -1,
          0
        ],
        "forward": "X_k=sum_(n=0..3) x_n exp(-2*pi*i*k*n/4)",
        "spectrum": [
          0,
          2,
          0,
          2
        ],
        "inverse": "x_n=(1/4)sum_(k=0..3)X_k exp(+2*pi*i*k*n/4)",
        "shift_check": "y_n=x_(n-1 mod4)=[0,1,0,-1], Y=[0,-2i,0,2i]; same magnitudes but different phase. Reconstruct all four entries."
      },
      "practice": "C26-DFT-P1 transform/reconstruct (1,1,1,1) -> (4,0,0,0); C26-DFT-D1 compare full complex spectrum with magnitude-only reconstruction and retain every omitted phase or residual. C26-BEAT-P1 cos(2*pi*5t)+cos(2*pi*7t)=2cos(2*pi*t)cos(2*pi*6t); absolute-envelope peaks recur at2Hz.",
      "id": "EA-26-E10-8",
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
    "created_utc": "2026-11-05T19:22:47.846756+00:00",
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
      }
    ],
    "verification_record": "C:\\Users\\info\\Documents\\Codex\\2026-11-05\\kfield-teaching-auditor\\outputs\\teaching-verification-24-27.json",
    "verification_sha256": "4e96da088122d472476f9ab06fe6c3d8fbbad2252315d304843a6c5e64ab0e04",
    "source_or_project_files_modified": false,
    "course_amendment": {
      "course_id": "course-26",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-26-beats-harmonics-and-spectral-energy-phase-structure\\input-contract.json",
      "input_contract_sha256": "9a49123e304afc053c0ed4685e72820491b9e2c65a57031c1ac31ada0399422f",
      "application": "Merge additively as teaching_amendment; preserve every original concept, SA/EA amendment and supplemental operation. Use exact exercise anchors and legacy aliases. Parent applies; no project edit performed.",
      "applied_source_amendments_read": {
        "SA-26": {
          "id": "SA-26",
          "course": 26,
          "finding": "source_fidelity",
          "lessons": [
            "lesson-05",
            "lesson-06",
            "lesson-07",
            "lesson-08"
          ],
          "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
          "requirements": [
            "Retain reported_exploratory_to_be_verified for the spectral bundle, distinguish its two works from their PDF/JSON/abstract representations, and preserve all signed rows.",
            "Fourteen rows contain three independent plane-cost values. qF=n^T G_phase n, signed gain and input-equivalent energy have different types; calibration/transfer obligations remain explicit.",
            "Retain the exact four-angle formulas and denominator domains Q!=0, rho!=0 and sin(theta)!=0. Mark undefined results without dropping input rows.",
            "Preserve C26.S01 comparator nullspace and source S05 parity/beat branches; an even comparator cannot test retained odd modes."
          ],
          "source_references": [
            "T35",
            "S05#/records/16",
            "S05#/records/20",
            "S05#/records/27"
          ],
          "status": "applied_to_blueprint_by_parent",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        },
        "EA-26-E10-8": {
          "course": 26,
          "finding": "E10",
          "lessons": [
            "lesson-02",
            "lesson-03",
            "lesson-04"
          ],
          "required_bridge": "Derive cos(a)+cos(b)=2cos((a-b)/2)cos((a+b)/2) from taught addition rules; identify signed amplitude factor versus its absolute envelope and define frequency convention. Teach a four-sample DFT by enumerating powers of i, with both transform signs and inverse factor specified.",
          "worked_example": {
            "id": "C26-DFT-EX1",
            "samples": [
              1,
              0,
              -1,
              0
            ],
            "forward": "X_k=sum_(n=0..3) x_n exp(-2*pi*i*k*n/4)",
            "spectrum": [
              0,
              2,
              0,
              2
            ],
            "inverse": "x_n=(1/4)sum_(k=0..3)X_k exp(+2*pi*i*k*n/4)",
            "shift_check": "y_n=x_(n-1 mod4)=[0,1,0,-1], Y=[0,-2i,0,2i]; same magnitudes but different phase. Reconstruct all four entries."
          },
          "practice": "C26-DFT-P1 transform/reconstruct (1,1,1,1) -> (4,0,0,0); C26-DFT-D1 compare full complex spectrum with magnitude-only reconstruction and retain every omitted phase or residual. C26-BEAT-P1 cos(2*pi*5t)+cos(2*pi*7t)=2cos(2*pi*t)cos(2*pi*6t); absolute-envelope peaks recur at2Hz.",
          "id": "EA-26-E10-8",
          "status": "applied_to_blueprint_by_parent",
          "merge_action": "Attach to named lesson authoring obligations and capstone prerequisites. Actual content links remain an E05 acceptance gate.",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        }
      },
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C26.01",
            "concept": "Oscillations, frequency, and phase",
            "operation": "Read and reconstruct a sinusoid with stated units"
          },
          {
            "concept_id": "C26.02",
            "concept": "Superposition and beat envelopes",
            "operation": "Derive a two-frequency beat example"
          },
          {
            "concept_id": "C26.03",
            "concept": "Harmonics and spatial rulers",
            "operation": "Relate integer harmonics to the declared trajectory geometry"
          },
          {
            "concept_id": "C26.04",
            "concept": "Spectral coefficients retain phase",
            "operation": "Reconstruct a short signal from signed complex coefficients"
          },
          {
            "concept_id": "C26.05",
            "concept": "Cross-channel phase and wavelength",
            "operation": "Compare channels without losing polarity or reference definitions"
          },
          {
            "concept_id": "C26.06",
            "concept": "Photon-equivalent model energy",
            "operation": "Calculate a source-defined energy equivalent and state its physical meaning"
          },
          {
            "concept_id": "C26.07",
            "concept": "Signed event evidence",
            "operation": "Read the retained spectral ledger without treating repeated levels as independent inputs"
          },
          {
            "concept_id": "C26.08",
            "concept": "Residual spectra as the next measurement",
            "operation": "Carry all unexplained components into a new comparison"
          },
          {
            "concept_id": "C26.S01",
            "concept": "Parity and comparator nullspaces",
            "operation": "Show on a short periodic sequence that antipodal symmetry removes odd harmonics; retain those channels and distinguish the ternary scale ladder from the Fibonacci-cutoff and proposed beat branches."
          }
        ],
        "source_modules": [],
        "scope": "Analyze a completely specified synthetic beat signal, reconstruct it, and compare its evidence layers with one pinned archive event.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Analyze a completely specified synthetic beat signal, reconstruct it, and compare its evidence layers with one pinned archive event.",
        "required_operations": [
          "Read and reconstruct a sinusoid with stated units",
          "Derive a two-frequency beat example",
          "Relate integer harmonics to the declared trajectory geometry",
          "Reconstruct a short signal from signed complex coefficients",
          "Compare channels without losing polarity or reference definitions",
          "Calculate a source-defined energy equivalent and state its physical meaning",
          "Read the retained spectral ledger without treating repeated levels as independent inputs",
          "Carry all unexplained components into a new comparison"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-26",
          "title": "Beats, Harmonics, and Spectral Energy–Phase Structure",
          "backbone_modules": [],
          "topic_boundary": "Finite beats/DFT, retained complex phase, comparator nullspaces, signed event ratios and input-equivalent energy.",
          "cognitive_or_fidelity_risk": "Fourteen event rows carry three independent plane costs, not fourteen cost levels.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "series/source-registry.json"
          ],
          "source_pointer": null,
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-26-beats-harmonics-and-spectral-energy-phase-structure\\input-contract.json",
            "sha256": "a204af4a4ed045c014215b5d07f9a28f83f289e81d93876a52ed99580a59452d",
            "lesson_count": 8
          },
          "required_amendment_ids": [
            "SA-26"
          ],
          "source_launch_decision": "ready_for_source_scoped_drafting_with_required_gates",
          "decision_scope": "Source/coverage only; no new teaching acceptance or finished-course validation.",
          "educational_gate": [
            "E05",
            "E10",
            "independent_teaching_recheck"
          ]
        }
      ],
      "source_scope": {
        "primary": [
          "T35",
          "T50",
          "spectral_bundle",
          "spectral_work",
          "energy_work"
        ],
        "additional": [
          "S05#/records/15",
          "S05#/records/16",
          "S05#/records/20",
          "S05#/records/25",
          "S05#/records/26",
          "S05#/records/27"
        ],
        "evidence_class": "reported_exploratory_to_be_verified",
        "representations": "Two works, three representations each; canonical computations reference JSONs, not six independent studies.",
        "all_rows": "All14 source rows are kept by immutable whole-object hash and exact /events/0..13 and energy-work /all_event_channel_modulations pointers. Derived diagnostics reference every row; no raw dataset copies. Eight gains are positive and six negative; five energy intervals form a source-selected subset, not a synonym for all positive rows.",
        "cost_structure": "w4,v4,lambda6 rows use only3 distinct plane costs. Retain every response row, uncertainty and covariance structure; family-level diagnostics never erase within-family differences.",
        "notation": "T35 G is count contrast and g=G/Q fractional gain; spectral-work formulas.measured_gain labels fractional gain G. Use contrast_counts and fractional_gain fields. Energy family lambda-sheet maps explicitly to spectral family lambda.",
        "domains": "Q!=0 for g, sin(theta)!=0 and c!=0 for rho, rho!=0 for P. Retain undefined rows and defined intermediate values. Four counts reconstruct from two means and both signed half-differences.",
        "precision": "Source replay diagnostics use binary64 JSON inputs with explicit signed closure fields; no exact equality or interval certification is inferred. Fresh synthetic examples use exact rational/complex arithmetic.",
        "model_energy": "Input-equivalent g*power*exposure and hc/lambda are model calculations. Transfer calibration, uncertainty, angular resolution, exposure/down-conversion and independent replay obligations are supplied by the source contract. The source4-degree acquisition grid is not sub-degree measurement precision.",
        "provenance_issues": "Pinned bundle reports declared energy revision f98c... versus packaged9120... and a quadratic PDF digest/size mismatch. Preserve the full source bundle pointer; do not silently repair or merge revisions. Source processing counts65880 total,65845 healthy,35 diagnostic rows: original rows and diagnostic masks/reasons remain a production retention obligation, not permission to erase them.",
        "parity": "Even comparator E annihilates odd modes; retain O and all cross-channel complex phases. S05 native ternary ladder, Fibonacci-cutoff synthesis and proposed25/27->2 beat pathway are distinct. Four-sample DFT does not resolve native high harmonics."
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "Oscillations, frequency, and phase",
          "entry_prerequisites": [
            "course-12",
            "course-14",
            "course-25"
          ],
          "concept_ids": [
            "C26.01"
          ],
          "worked_example_capability": "Read and reconstruct a sinusoid with stated units",
          "assessment_target": "Read and reconstruct a sinusoid with stated units",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C26.01-E1",
          "worked_example_id": "C26.01-W1",
          "prior_practice_id": "C26.01-P1",
          "diagnostic_id": "C26.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Superposition and beat envelopes",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C26.02"
          ],
          "worked_example_capability": "Derive a two-frequency beat example",
          "assessment_target": "Derive a two-frequency beat example",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "required_amendment_ids": [
            "EA-26-E10-8"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C26.02-E1",
          "worked_example_id": "C26.02-W1",
          "prior_practice_id": "C26.02-P1",
          "diagnostic_id": "C26.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "Harmonics and spatial rulers",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C26.03"
          ],
          "worked_example_capability": "Relate integer harmonics to the declared trajectory geometry",
          "assessment_target": "Relate integer harmonics to the declared trajectory geometry",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "required_amendment_ids": [
            "EA-26-E10-8"
          ],
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C26.03-E1",
          "worked_example_id": "C26.03-W1",
          "prior_practice_id": "C26.03-P1",
          "diagnostic_id": "C26.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "Spectral coefficients retain phase",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C26.04"
          ],
          "worked_example_capability": "Reconstruct a short signal from signed complex coefficients",
          "assessment_target": "Reconstruct a short signal from signed complex coefficients",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "required_amendment_ids": [
            "EA-26-E10-8"
          ],
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C26.04-E1",
          "worked_example_id": "C26.04-W1",
          "prior_practice_id": "C26.04-P1",
          "diagnostic_id": "C26.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "Cross-channel phase and wavelength",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C26.05",
            "C26.S01"
          ],
          "worked_example_capability": "Compare channels without losing polarity or reference definitions",
          "assessment_target": "Compare channels without losing polarity or reference definitions",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "source_coverage_requirements": [
            {
              "concept_id": "C26.S01",
              "operation": "Show on a short periodic sequence that antipodal symmetry removes odd harmonics; retain those channels and distinguish the ternary scale ladder from the Fibonacci-cutoff and proposed beat branches.",
              "source_pointers": [
                "S05#/records/15",
                "S05#/records/16",
                "S05#/records/20",
                "S05#/records/25",
                "S05#/records/26",
                "S05#/records/27"
              ]
            }
          ],
          "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
          "required_amendment_ids": [
            "SA-26"
          ],
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C26.05-E1",
          "worked_example_id": "C26.05-W1",
          "prior_practice_id": "C26.05-P1",
          "diagnostic_id": "C26.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "Photon-equivalent model energy",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C26.06"
          ],
          "worked_example_capability": "Calculate a source-defined energy equivalent and state its physical meaning",
          "assessment_target": "Calculate a source-defined energy equivalent and state its physical meaning",
          "later_use": "lesson-07",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-26"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C26.06-E1",
          "worked_example_id": "C26.06-W1",
          "prior_practice_id": "C26.06-P1",
          "diagnostic_id": "C26.06-D1"
        },
        {
          "id": "lesson-07",
          "title": "Signed event evidence",
          "entry_prerequisites": [
            "lesson-06"
          ],
          "concept_ids": [
            "C26.07"
          ],
          "worked_example_capability": "Read the retained spectral ledger without treating repeated levels as independent inputs",
          "assessment_target": "Read the retained spectral ledger without treating repeated levels as independent inputs",
          "later_use": "lesson-08",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-26"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C26.07-E1",
          "worked_example_id": "C26.07-W1",
          "prior_practice_id": "C26.07-P1",
          "diagnostic_id": "C26.07-D1"
        },
        {
          "id": "lesson-08",
          "title": "Residual spectra as the next measurement",
          "entry_prerequisites": [
            "lesson-07"
          ],
          "concept_ids": [
            "C26.08"
          ],
          "worked_example_capability": "Carry all unexplained components into a new comparison",
          "assessment_target": "Carry all unexplained components into a new comparison",
          "later_use": "capstone",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-26"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C26.08-E1",
          "worked_example_id": "C26.08-W1",
          "prior_practice_id": "C26.08-P1",
          "diagnostic_id": "C26.08-D1"
        }
      ],
      "legacy_bridge_aliases": [
        {
          "legacy_id": "C26-DFT-EX1",
          "anchor_id": "C26.04-W1"
        },
        {
          "legacy_id": "C26-DFT-P1",
          "anchor_id": "C26.04-P1"
        },
        {
          "legacy_id": "C26-DFT-D1",
          "anchor_id": "C26.04-D1"
        },
        {
          "legacy_id": "C26-BEAT-P1",
          "anchor_id": "C26.02-P1"
        }
      ],
      "core_periods": 17,
      "capstone_periods": 3,
      "period_minutes": 55,
      "capstone_total_points": 36,
      "capstone_sessions": [
        "55 minutes: assemble the typed input/source ledger and first calculation.",
        "55 minutes: complete every mapped operation and retain signed components and domain failures.",
        "55 minutes: reconstruct, classify evidence and audit all source boundaries; repair with the point rubric."
      ],
      "core_boundary": "Finite computations use fully declared synthetic inputs. Source-event reading preserves every row by immutable reference. The course27 certificate operation audits supplied claims and missing fields; a source numeric replay is gated until complete certificate inputs are pinned. No absent source value is invented.",
      "prerequisite_status": "Blueprint closure reviewed; produced senior-facing lessons, diagnostics, answered practice and capstone still require independent completed-course acceptance.",
      "inline_content_location": "Complete lesson anchors are in course_map[*].teaching_anchor; complete capstone mapping is in capstone_specification.backward_map below."
    },
    "completed_course_acceptance": false
  }
}
```
