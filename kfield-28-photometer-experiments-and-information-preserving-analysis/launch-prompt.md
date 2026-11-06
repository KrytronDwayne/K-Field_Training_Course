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
  "course_output_directory": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-28-photometer-experiments-and-information-preserving-analysis",
  "topic": "Photometer Experiments and Information-Preserving Analysis",
  "series_course_id": "course-28",
  "audience": "High-school seniors; first-principles teaching, with concrete prerequisite capabilities and taught bridges.",
  "prerequisites": [
    "Signed arithmetic, fractions, ratios, powers, linear equations, and coordinate graphs",
    "Capabilities taught in course-01",
    "Capabilities taught in course-07",
    "Capabilities taught in course-24",
    "Capabilities taught in course-25",
    "Capabilities taught in course-26",
    "Capabilities taught in course-27"
  ],
  "learning_outcomes": [
    "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
    "Retain ordering, timestamps, channel identities, and fault states",
    "Compute a declared Clear-reference transformation and preserve its inputs",
    "Compare same-polarity and inverted structures without erasing weak channels",
    "Freeze a geometric event rule before comparing the signal",
    "Keep window support, phase, and removed components replayable",
    "Track calibration limits, timing, gaps, and unresolved channel structure",
    "Specify a reproducible forward test and retain every outcome"
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
        "concept_id": "C28.01",
        "concept": "From light to channel readings",
        "operation": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration"
      },
      {
        "concept_id": "C28.02",
        "concept": "Acquisition identity and raw-value preservation",
        "operation": "Retain ordering, timestamps, channel identities, and fault states"
      },
      {
        "concept_id": "C28.03",
        "concept": "Normalization with an inverse account",
        "operation": "Compute a declared Clear-reference transformation and preserve its inputs"
      },
      {
        "concept_id": "C28.04",
        "concept": "Symmetry, palindromes, and signed comparisons",
        "operation": "Compare same-polarity and inverted structures without erasing weak channels"
      },
      {
        "concept_id": "C28.05",
        "concept": "Sidereal combs and event windows",
        "operation": "Freeze a geometric event rule before comparing the signal"
      },
      {
        "concept_id": "C28.06",
        "concept": "Scale and channel comparisons",
        "operation": "Keep window support, phase, and removed components replayable"
      },
      {
        "concept_id": "C28.07",
        "concept": "Uncertainty as a structured record",
        "operation": "Track calibration limits, timing, gaps, and unresolved channel structure"
      },
      {
        "concept_id": "C28.08",
        "concept": "A prospective measurement protocol",
        "operation": "Specify a reproducible forward test and retain every outcome"
      },
      {
        "concept_id": "C28.S01",
        "concept": "Comparator blindness and retained odd channels",
        "operation": "Audit whether a synthetic comparator can represent every measured parity sector; carry unrepresented odd channels forward and report the source's 25-27-to-2 triad as a retained proposed pathway."
      }
    ],
    "source_modules": [],
    "scope": "Design and execute a small synthetic photometer analysis with a frozen event rule, complete residuals, and a prospective validation plan.",
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
      "concept_id": "C28.01",
      "concept": "From light to channel readings",
      "introduction": "lesson-01",
      "practice": "C28.01-P1",
      "assessment": "C28.01-D1",
      "later_use": "lesson-02",
      "worked_example": "C28.01-W1",
      "all_required_teaching_item_ids": [
        "C28.01-E1",
        "C28.01-W1",
        "C28.01-P1",
        "C28.01-D1"
      ]
    },
    {
      "concept_id": "C28.02",
      "concept": "Acquisition identity and raw-value preservation",
      "introduction": "lesson-02",
      "practice": "C28.02-P1",
      "assessment": "C28.02-D1",
      "later_use": "lesson-03",
      "worked_example": "C28.02-W1",
      "all_required_teaching_item_ids": [
        "C28.02-E1",
        "C28.02-W1",
        "C28.02-P1",
        "C28.02-D1"
      ]
    },
    {
      "concept_id": "C28.03",
      "concept": "Normalization with an inverse account",
      "introduction": "lesson-03",
      "practice": "C28.03-P1",
      "assessment": "C28.03-D1",
      "later_use": "lesson-04",
      "worked_example": "C28.03-W1",
      "all_required_teaching_item_ids": [
        "C28.03-E1",
        "C28.03-W1",
        "C28.03-P1",
        "C28.03-D1"
      ]
    },
    {
      "concept_id": "C28.04",
      "concept": "Symmetry, palindromes, and signed comparisons",
      "introduction": "lesson-04",
      "practice": "C28.04-P1",
      "assessment": "C28.04-D1",
      "later_use": "lesson-05",
      "worked_example": "C28.04-W1",
      "all_required_teaching_item_ids": [
        "C28.04-E1",
        "C28.04-W1",
        "C28.04-P1",
        "C28.04-D1",
        "C28.S01-E1",
        "C28.S01-W1",
        "C28.S01-P1",
        "C28.S01-D1"
      ]
    },
    {
      "concept_id": "C28.05",
      "concept": "Sidereal combs and event windows",
      "introduction": "lesson-05",
      "practice": "C28.05-P1",
      "assessment": "C28.05-D1",
      "later_use": "lesson-06",
      "worked_example": "C28.05-W1",
      "all_required_teaching_item_ids": [
        "C28.05-E1",
        "C28.05-W1",
        "C28.05-P1",
        "C28.05-D1"
      ]
    },
    {
      "concept_id": "C28.06",
      "concept": "Scale and channel comparisons",
      "introduction": "lesson-06",
      "practice": "C28.06-P1",
      "assessment": "C28.06-D1",
      "later_use": "lesson-07",
      "worked_example": "C28.06-W1",
      "all_required_teaching_item_ids": [
        "C28.06-E1",
        "C28.06-W1",
        "C28.06-P1",
        "C28.06-D1"
      ]
    },
    {
      "concept_id": "C28.07",
      "concept": "Uncertainty as a structured record",
      "introduction": "lesson-07",
      "practice": "C28.07-P1",
      "assessment": "C28.07-D1",
      "later_use": "lesson-08",
      "worked_example": "C28.07-W1",
      "all_required_teaching_item_ids": [
        "C28.07-E1",
        "C28.07-W1",
        "C28.07-P1",
        "C28.07-D1"
      ]
    },
    {
      "concept_id": "C28.08",
      "concept": "A prospective measurement protocol",
      "introduction": "lesson-08",
      "practice": "C28.08-P1",
      "assessment": "C28.08-D1",
      "later_use": "capstone",
      "worked_example": "C28.08-W1",
      "all_required_teaching_item_ids": [
        "C28.08-E1",
        "C28.08-W1",
        "C28.08-P1",
        "C28.08-D1"
      ]
    },
    {
      "concept_id": "C28.S01",
      "concept": "Comparator blindness and retained odd channels",
      "introduction": "lesson-04",
      "practice": "lesson-04: worked example and guided practice",
      "assessment": "lesson-06: diagnostic checks",
      "later_use": "capstone",
      "source_pointers": [
        "S05#/records/16",
        "S05#/records/20",
        "S05#/records/27"
      ]
    }
  ],
  "course_map": [
    {
      "id": "lesson-01",
      "title": "From light to channel readings",
      "entry_prerequisites": [
        "course-01",
        "course-07",
        "course-24",
        "course-25",
        "course-26",
        "course-27"
      ],
      "concept_ids": [
        "C28.01"
      ],
      "worked_example_capability": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
      "assessment_target": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
      "later_use": "lesson-02",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-01",
        "concept_id": "C28.01",
        "explanation_id": "C28.01-E1",
        "bridge_to_teach": "A channel reading is an instrument output with wavelength response, orientation, gain, exposure, timestamp convention and calibration identity. Counts are not automatically optical power. Introduce a synthetic five-row acquisition before transforming it; distinguish mid-exposure time from interval support.",
        "worked_example": {
          "id": "C28.01-W1",
          "task_and_answer": "Toy acquisition A has sequence0..4, elapsed mid-exposure times0..4s, channel A nominal500nm, raw counts(2,5,8,1,3), Clear(10,0,20,10,10), fixed +z sensor normal, gain setting1, exposure1/5s and calibration not supplied. Each exposure spans t-1/10 to t+1/10s. These are authored counts, not observations."
        },
        "guided_practice": {
          "id": "C28.01-P1",
          "task_and_answer": "At row2 the midpoint is2s, exposure support[1.9,2.1]s, raw A=8,Clear=20. If a separate channel B is nominal600nm with raw count4, retain its own wavelength and response identity; a count ratio8/4=2 does not yet give a spectral power ratio."
        },
        "diagnostic": {
          "id": "C28.01-D1",
          "task_and_answer": "Equal counts at different gain/exposure/calibration settings do not identify equal incident energy. Missing calibration stays missing. Do not infer orientation or wavelength from the channel name alone."
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
        "original_title": "From light to channel readings",
        "original_assessment_target": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
        "original_concept_ids": [
          "C28.01"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "course-01",
          "course-07",
          "course-24",
          "course-25",
          "course-26",
          "course-27"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Acquisition identities, exposure and calibration",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-02",
      "title": "Acquisition identity and raw-value preservation",
      "entry_prerequisites": [
        "lesson-01"
      ],
      "concept_ids": [
        "C28.02"
      ],
      "worked_example_capability": "Retain ordering, timestamps, channel identities, and fault states",
      "assessment_target": "Retain ordering, timestamps, channel identities, and fault states",
      "later_use": "lesson-03",
      "core_minutes": 55,
      "teaching_anchor": {
        "lesson_id": "lesson-02",
        "concept_id": "C28.02",
        "explanation_id": "C28.02-E1",
        "bridge_to_teach": "An acquisition key includes device/session, sequence, timestamp and channel. Retain raw value, fault/status flags and any corrected view separately. Sorting, duplicate timestamps, missing samples and saturation require a reversible mapping. A diagnostic flag is not permission to delete a row.",
        "worked_example": {
          "id": "C28.02-W1",
          "task_and_answer": "Retain all five toy rows including row1 A=5,Clear=0. Mark its ratio transform invalid later, while its raw count remains valid as an authored input. If row3 is independently marked suspected saturation, keep A=1 plus the flag and reason; do not silently replace its raw value."
        },
        "guided_practice": {
          "id": "C28.02-P1",
          "task_and_answer": "Two rows may share a timestamp but differ by sequence or channel. Keep both IDs. If sequence5 is absent, add a gap record with expected time5s and no invented count. A display sorted by time also stores original sequence so the acquisition order can be recovered."
        },
        "diagnostic": {
          "id": "C28.02-D1",
          "task_and_answer": "Absent sample, recorded zero and explicit null are distinct. A mask must accompany the original values and reason, never overwrite them. A prospective acquisition is not a performed one merely because its row schema is complete."
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
        "original_title": "Acquisition identity and raw-value preservation",
        "original_assessment_target": "Retain ordering, timestamps, channel identities, and fault states",
        "original_concept_ids": [
          "C28.02"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-01"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Raw retention, order and invalid branches",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-03",
      "title": "Normalization with an inverse account",
      "entry_prerequisites": [
        "lesson-02"
      ],
      "concept_ids": [
        "C28.03"
      ],
      "worked_example_capability": "Compute a declared Clear-reference transformation and preserve its inputs",
      "assessment_target": "Compute a declared Clear-reference transformation and preserve its inputs",
      "later_use": "lesson-04",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-28"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-03",
        "concept_id": "C28.03",
        "explanation_id": "C28.03-E1",
        "bridge_to_teach": "Define Clear-reference ratio r=A/Clear only where the denominator is nonzero and the channel pairing is declared. Retain A,Clear,ratio,rounding rule and validity status. The inverse account A=r*Clear applies to defined ratios; invalid rows retain A directly.",
        "worked_example": {
          "id": "C28.03-W1",
          "task_and_answer": "For the five-row toy, ratios are(1/5,undefined,2/5,1/10,3/10). Reconstruct defined rows by multiplication and row1 from retained raw A=5. The zero-Clear branch is a preserved row, not r=0 or infinity."
        },
        "guided_practice": {
          "id": "C28.03-P1",
          "task_and_answer": "For raw A=1,Clear=3, exact r=1/3. A10-significant-digit display0.3333333333 differs by1/(3*10^10); retain that ratio closure and the original integers. For A=0,Clear=5 the ratio is valid0, contrasting with invalid0/0."
        },
        "diagnostic": {
          "id": "C28.03-D1",
          "task_and_answer": "A normalized ratio without its reference cannot reconstruct raw amplitude. A missing Clear sample differs from a measured zero-Clear value. Negative or fault-tagged inputs retain their values and source-defined validity flags rather than being discarded."
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
        "original_title": "Normalization with an inverse account",
        "original_assessment_target": "Compute a declared Clear-reference transformation and preserve its inputs",
        "original_concept_ids": [
          "C28.03"
        ],
        "required_source_amendment_ids": [
          "SA-28"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-02"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Clear ratio and zero denominator",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Exact reconstruction and decimal residual",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-04",
      "title": "Symmetry, palindromes, and signed comparisons",
      "entry_prerequisites": [
        "lesson-03"
      ],
      "concept_ids": [
        "C28.04",
        "C28.S01"
      ],
      "worked_example_capability": "Compare same-polarity and inverted structures without erasing weak channels",
      "assessment_target": "Compare same-polarity and inverted structures without erasing weak channels",
      "later_use": "lesson-05",
      "core_minutes": 165,
      "source_coverage_requirements": [
        {
          "concept_id": "C28.S01",
          "operation": "Audit whether a synthetic comparator can represent every measured parity sector; carry unrepresented odd channels forward and report the source's 25-27-to-2 triad as a retained proposed pathway.",
          "source_pointers": [
            "S05#/records/16",
            "S05#/records/20",
            "S05#/records/27"
          ]
        }
      ],
      "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
      "required_amendment_ids": [
        "SA-28"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-04",
        "concept_id": "C28.04",
        "explanation_id": "C28.04-E1",
        "bridge_to_teach": "Teach reflection R around a declared sample center separately from antipodal half-turn H on a periodic signal. Reflection components are s=(x+Rx)/2 and a=(x-Rx)/2, giving Rx=s-a and x=s+a. Same-polarity and inverted tests have different defects x-Rx and x+Rx. Keep both and the center convention.",
        "worked_example": {
          "id": "C28.04-W1",
          "task_and_answer": "For x=(1,2,4,3), reverse Rx=(3,4,2,1), same component s=(2,3,3,2) and inverted component a=(-1,-1,1,1). R s=s,R a=-a and s+a=x. Neither full input passes an exact same or inverted test; retain both nonzero defects."
        },
        "guided_practice": {
          "id": "C28.04-P1",
          "task_and_answer": "For x=(3,1,-1,1), reflection components are(2,0,0,2) and(1,1,-1,-1). For a separate midpoint-centered pair(-2,0,2), reversal negates the sequence, so inverted defect is zero. A nonzero center sample would remain a same component."
        },
        "diagnostic": {
          "id": "C28.04-D1",
          "task_and_answer": "Do not call a weak channel empty, optimize the reflection center after seeing the desired pattern without recording the search, or confuse reversal parity with a half-turn frequency split. State the fixed center, support and both signs."
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
        "supplemental_exercises": [
          {
            "concept_id": "C28.S01",
            "explanation_id": "C28.S01-E1",
            "worked_example_id": "C28.S01-W1",
            "prior_practice_id": "C28.S01-P1",
            "diagnostic_id": "C28.S01-D1",
            "explanation": "For a four-point periodic sequence H shifts by two samples. E=(I+H)/2 and O=(I-H)/2 reconstruct I and have disjoint parity. An even comparator and all its shifts lie in the E sector and cannot represent O. This nullspace is a property of the comparator, not absence of measured odd structure.",
            "worked_task_and_answer": "For x=(1,2,3,4), Ex=(2,3,2,3),Ox=(-1,-1,1,1). Their sum is x. Every circular shift of Ex has zero dot product with Ox. With the declared four-point DFT the odd spectrum is(0,-2+2i,0,-2-2i); keep both complex odd coefficients.",
            "practice_task_and_answer": "For x=(3,1,-1,1), Ex=(1,1,1,1),Ox=(2,0,-2,0). Reconstruct x and show the even comparator cannot recover amplitudes in Ox. Read S05 R017/R021: native odd1,3,9,27 modes are structurally outside an even comparator; R028 reports25–27->2 as a retained proposed pathway, not a closed identity.",
            "diagnostic_task_and_answer": "The four-point example does not resolve native25 and27 harmonics: it aliases indices modulo4. Report the native ternary ladder, Fibonacci-cutoff proposal and beat branch separately, while retaining every measured parity sector and comparison residual."
          }
        ],
        "original_title": "Symmetry, palindromes, and signed comparisons",
        "original_assessment_target": "Compare same-polarity and inverted structures without erasing weak channels",
        "original_concept_ids": [
          "C28.04",
          "C28.S01"
        ],
        "required_source_amendment_ids": [
          "SA-28"
        ],
        "source_coverage_requirements": [
          {
            "concept_id": "C28.S01",
            "operation": "Audit whether a synthetic comparator can represent every measured parity sector; carry unrepresented odd channels forward and report the source's 25-27-to-2 triad as a retained proposed pathway.",
            "source_pointers": [
              "S05#/records/16",
              "S05#/records/20",
              "S05#/records/27"
            ]
          }
        ],
        "original_entry_prerequisites": [
          "lesson-03"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Reflection same/inverted operators",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Antipodal even/odd operators",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 3,
            "focus": "C28.S01 nullspace and source ladder",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-05",
      "title": "Sidereal combs and event windows",
      "entry_prerequisites": [
        "lesson-04"
      ],
      "concept_ids": [
        "C28.05"
      ],
      "worked_example_capability": "Freeze a geometric event rule before comparing the signal",
      "assessment_target": "Freeze a geometric event rule before comparing the signal",
      "later_use": "lesson-06",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-28"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-05",
        "concept_id": "C28.05",
        "explanation_id": "C28.05-E1",
        "bridge_to_teach": "Freeze geometry before signal comparison: define the origin, normal, spacing, time convention and event equation; then map events to a predeclared window and interpolation rule. A synthetic comb demonstrates the operation without standing in for a real sidereal ephemeris.",
        "worked_example": {
          "id": "C28.05-W1",
          "task_and_answer": "Use a declared synthetic phase q(t)=t/2 cycles and events q=k, yielding t=0,2,4s. Freeze integer-second sample offsets(-1,0,1) around each event. At center2s, raw A window is(5,8,1); side same-polarity difference5-1=4 and inverted sum5+1=6. Retain center8 and both defects."
        },
        "guided_practice": {
          "id": "C28.05-P1",
          "task_and_answer": "At center0s the negative-time sample is absent; at center4s the5s sample is absent. Keep partial-support windows and masks. The normalized center2 window includes an invalid ratio at t=1 because Clear=0; report it as incomplete while retaining the complete raw window."
        },
        "diagnostic": {
          "id": "C28.05-D1",
          "task_and_answer": "Do not shift event times or discard edge windows to improve a comparison. A real sidereal comb additionally needs pinned ephemeris, site/orientation, event definitions and calibration/training boundaries; none is supplied by q=t/2."
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
        "original_title": "Sidereal combs and event windows",
        "original_assessment_target": "Freeze a geometric event rule before comparing the signal",
        "original_concept_ids": [
          "C28.05"
        ],
        "required_source_amendment_ids": [
          "SA-28"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-04"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Frozen geometry and event windows",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Partial support and invalid normalized windows",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-06",
      "title": "Scale and channel comparisons",
      "entry_prerequisites": [
        "lesson-05"
      ],
      "concept_ids": [
        "C28.06"
      ],
      "worked_example_capability": "Keep window support, phase, and removed components replayable",
      "assessment_target": "Keep window support, phase, and removed components replayable",
      "later_use": "lesson-07",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-06",
        "concept_id": "C28.06",
        "explanation_id": "C28.06-E1",
        "bridge_to_teach": "Declare the support and boundary rule of every mean, filter or spectral transform. Save represented and removed components with sample identities. Use a mean/detail decomposition before frequency views; comparisons across windows require matched or explicitly different supports.",
        "worked_example": {
          "id": "C28.06-W1",
          "task_and_answer": "The five raw A values sum19, so mean19/5 and detail(-9/5,6/5,21/5,-14/5,-4/5) reconstruct all five entries. Save the mean and full signed detail, including the row with invalid normalization."
        },
        "guided_practice": {
          "id": "C28.06-P1",
          "task_and_answer": "For window(5,8,1), mean14/3 and detail(1/3,10/3,-11/3) reconstruct the window. It is a different support from the five-row mean; do not compare the two means as though the input set were identical. A four-sample DFT retains complex phases and the declared inverse factor."
        },
        "diagnostic": {
          "id": "C28.06-D1",
          "task_and_answer": "Smoothing or a Fourier magnitude cannot replace the removed component or phase. A failed ratio transform does not erase the corresponding raw signal from a parallel comparison."
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
        "original_title": "Scale and channel comparisons",
        "original_assessment_target": "Keep window support, phase, and removed components replayable",
        "original_concept_ids": [
          "C28.06"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-05"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Full mean/detail reconstruction",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Changed support and retained spectral phases",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-07",
      "title": "Uncertainty as a structured record",
      "entry_prerequisites": [
        "lesson-06"
      ],
      "concept_ids": [
        "C28.07"
      ],
      "worked_example_capability": "Track calibration limits, timing, gaps, and unresolved channel structure",
      "assessment_target": "Track calibration limits, timing, gaps, and unresolved channel structure",
      "later_use": "lesson-08",
      "core_minutes": 110,
      "required_amendment_ids": [
        "SA-28"
      ],
      "teaching_anchor": {
        "lesson_id": "lesson-07",
        "concept_id": "C28.07",
        "explanation_id": "C28.07-E1",
        "bridge_to_teach": "Represent uncertainty by named contributors: calibration interval, exposure, timing offset, orientation, angular resolution, gaps, saturation and unresolved channel dependence. Keep their joint assumptions rather than collapsing everything into one score. Propagate simple declared bounds by endpoint arithmetic.",
        "worked_example": {
          "id": "C28.07-W1",
          "task_and_answer": "Synthetic factor k in[1.9,2.1] units/count and x in[0.9,1.1] counts give product in[1.71,2.31] units under independent box bounds and positive factors. This exercise is not an instrument calibration. With timing offset in[-0.1,0.1]s, an event at2s maps to[1.9,2.1]s before exposure support is considered."
        },
        "guided_practice": {
          "id": "C28.07-P1",
          "task_and_answer": "A duration0.2s centered at an uncertain midpoint in[1.9,2.1]s has possible support[1.8,2.2]s. Keep the common clock offset as shared across channels rather than claiming five independent timing errors. Record zero-Clear, saturation and absent-sample branches separately."
        },
        "diagnostic": {
          "id": "C28.07-D1",
          "task_and_answer": "An interval does not supply its own physical calibration or dependence model. Preserve original raw rows and masks when reporting any corrected view. T35 source calibration and exposure-transfer obligations remain explicit."
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
        "original_title": "Uncertainty as a structured record",
        "original_assessment_target": "Track calibration limits, timing, gaps, and unresolved channel structure",
        "original_concept_ids": [
          "C28.07"
        ],
        "required_source_amendment_ids": [
          "SA-28"
        ],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-06"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Named uncertainty contributors and interval products",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Shared timing offsets and exposure support",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    },
    {
      "id": "lesson-08",
      "title": "A prospective measurement protocol",
      "entry_prerequisites": [
        "lesson-07"
      ],
      "concept_ids": [
        "C28.08"
      ],
      "worked_example_capability": "Specify a reproducible forward test and retain every outcome",
      "assessment_target": "Specify a reproducible forward test and retain every outcome",
      "later_use": "capstone",
      "core_minutes": 110,
      "teaching_anchor": {
        "lesson_id": "lesson-08",
        "concept_id": "C28.08",
        "explanation_id": "C28.08-E1",
        "bridge_to_teach": "Write a prospective protocol before collecting new values: target, instrument configuration, raw schema, fixed geometry/events, training/check split, transforms, controls, uncertainty accounting, stopping rule and handling of every outcome. A synthetic rehearsal checks the instructions, not the physical hypothesis.",
        "worked_example": {
          "id": "C28.08-W1",
          "task_and_answer": "Rehearse the fixed q=t/2 rule on the toy five-row packet and publish all three windows, missing supports, zero-Clear status, reflection defects, even/odd components and mean/detail reconstruction. Mark execution as synthetic only. A future device run remains planned, with calibration and site/ephemeris inputs still required."
        },
        "guided_practice": {
          "id": "C28.08-P1",
          "task_and_answer": "Freeze future duration10s,1s midpoint cadence, exposure0.2s, all declared channels, q=t/2 only for the toy rehearsal, both parity tests and all outcome fields. For a real forward test replace that toy geometry with a pinned physical event contract before acquisition. Store completion status, interruptions and every result; a mismatch stays in the comparison."
        },
        "diagnostic": {
          "id": "C28.08-D1",
          "task_and_answer": "Do not label a protocol as measured, successful or independently replicated before it occurs. If the event rule or calibration changes after inspection, retain the earlier version and mark the revised analysis exploratory."
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
        "original_title": "A prospective measurement protocol",
        "original_assessment_target": "Specify a reproducible forward test and retain every outcome",
        "original_concept_ids": [
          "C28.08"
        ],
        "required_source_amendment_ids": [],
        "source_coverage_requirements": [],
        "original_entry_prerequisites": [
          "lesson-07"
        ],
        "session_sequence": [
          {
            "session": 1,
            "focus": "Complete evidence ledger",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          },
          {
            "session": 2,
            "focus": "Source gaps and prospective protocol",
            "minutes": 55,
            "recovery_checkpoint": "Reproduce the worked operation, complete the named answered practice and explain the diagnostic before advancing. If needed, add a recovery session and update the dependent lesson links."
          }
        ]
      }
    }
  ],
  "capstone_specification": {
    "task": "Design and execute a small synthetic photometer analysis with a frozen event rule, complete residuals, and a prospective validation plan.",
    "required_operations": [
      "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
      "Retain ordering, timestamps, channel identities, and fault states",
      "Compute a declared Clear-reference transformation and preserve its inputs",
      "Compare same-polarity and inverted structures without erasing weak channels",
      "Freeze a geometric event rule before comparing the signal",
      "Keep window support, phase, and removed components replayable",
      "Track calibration limits, timing, gaps, and unresolved channel structure",
      "Specify a reproducible forward test and retain every outcome",
      "Audit whether a synthetic comparator can represent every measured parity sector; carry unrepresented odd channels forward and report the source's 25-27-to-2 triad as a retained proposed pathway."
    ],
    "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting.",
    "backward_map": [
      {
        "step_id": "C28-CAP-01",
        "operation": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
        "introduction": "lesson-01",
        "explanation_id": "C28.01-E1",
        "worked_example_id": "C28.01-W1",
        "prior_practice_id": "C28.01-P1",
        "diagnostic_id": "C28.01-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "At row2 the midpoint is2s, exposure support[1.9,2.1]s, raw A=8,Clear=20. If a separate channel B is nominal600nm with raw count4, retain its own wavelength and response identity; a count ratio8/4=2 does not yet give a spectral power ratio.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-02",
        "operation": "Retain ordering, timestamps, channel identities, and fault states",
        "introduction": "lesson-02",
        "explanation_id": "C28.02-E1",
        "worked_example_id": "C28.02-W1",
        "prior_practice_id": "C28.02-P1",
        "diagnostic_id": "C28.02-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Two rows may share a timestamp but differ by sequence or channel. Keep both IDs. If sequence5 is absent, add a gap record with expected time5s and no invented count. A display sorted by time also stores original sequence so the acquisition order can be recovered.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-03",
        "operation": "Compute a declared Clear-reference transformation and preserve its inputs",
        "introduction": "lesson-03",
        "explanation_id": "C28.03-E1",
        "worked_example_id": "C28.03-W1",
        "prior_practice_id": "C28.03-P1",
        "diagnostic_id": "C28.03-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For raw A=1,Clear=3, exact r=1/3. A10-significant-digit display0.3333333333 differs by1/(3*10^10); retain that ratio closure and the original integers. For A=0,Clear=5 the ratio is valid0, contrasting with invalid0/0.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-04",
        "operation": "Compare same-polarity and inverted structures without erasing weak channels",
        "introduction": "lesson-04",
        "explanation_id": "C28.04-E1",
        "worked_example_id": "C28.04-W1",
        "prior_practice_id": "C28.04-P1",
        "diagnostic_id": "C28.04-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For x=(3,1,-1,1), reflection components are(2,0,0,2) and(1,1,-1,-1). For a separate midpoint-centered pair(-2,0,2), reversal negates the sequence, so inverted defect is zero. A nonzero center sample would remain a same component.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-05",
        "operation": "Freeze a geometric event rule before comparing the signal",
        "introduction": "lesson-05",
        "explanation_id": "C28.05-E1",
        "worked_example_id": "C28.05-W1",
        "prior_practice_id": "C28.05-P1",
        "diagnostic_id": "C28.05-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "At center0s the negative-time sample is absent; at center4s the5s sample is absent. Keep partial-support windows and masks. The normalized center2 window includes an invalid ratio at t=1 because Clear=0; report it as incomplete while retaining the complete raw window.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-06",
        "operation": "Keep window support, phase, and removed components replayable",
        "introduction": "lesson-06",
        "explanation_id": "C28.06-E1",
        "worked_example_id": "C28.06-W1",
        "prior_practice_id": "C28.06-P1",
        "diagnostic_id": "C28.06-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "For window(5,8,1), mean14/3 and detail(1/3,10/3,-11/3) reconstruct the window. It is a different support from the five-row mean; do not compare the two means as though the input set were identical. A four-sample DFT retains complex phases and the declared inverse factor.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-07",
        "operation": "Track calibration limits, timing, gaps, and unresolved channel structure",
        "introduction": "lesson-07",
        "explanation_id": "C28.07-E1",
        "worked_example_id": "C28.07-W1",
        "prior_practice_id": "C28.07-P1",
        "diagnostic_id": "C28.07-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "A duration0.2s centered at an uncertain midpoint in[1.9,2.1]s has possible support[1.8,2.2]s. Keep the common clock offset as shared across channels rather than claiming five independent timing errors. Record zero-Clear, saturation and absent-sample branches separately.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-08",
        "operation": "Specify a reproducible forward test and retain every outcome",
        "introduction": "lesson-08",
        "explanation_id": "C28.08-E1",
        "worked_example_id": "C28.08-W1",
        "prior_practice_id": "C28.08-P1",
        "diagnostic_id": "C28.08-D1",
        "assessment_task": "Complete the taught practice packet with explicit source/synthetic scope, units and all retained information.",
        "answer_key": "Freeze future duration10s,1s midpoint cadence, exposure0.2s, all declared channels, q=t/2 only for the toy rehearsal, both parity tests and all outcome fields. For a real forward test replace that toy geometry with a pinned physical event contract before acquisition. Store completion status, interruptions and every result; a mismatch stays in the comparison.",
        "points": 4,
        "rubric": {
          "typed_inputs_and_domain": 1,
          "correct_operation": 1,
          "reconstruction_or_source_classification": 1,
          "retained_information_and_boundary": 1
        }
      },
      {
        "step_id": "C28-CAP-09",
        "operation": "Audit whether a synthetic comparator can represent every measured parity sector; carry unrepresented odd channels forward and report the source's 25-27-to-2 triad as a retained proposed pathway.",
        "introduction": "lesson-04",
        "concept_id": "C28.S01",
        "explanation_id": "C28.S01-E1",
        "worked_example_id": "C28.S01-W1",
        "prior_practice_id": "C28.S01-P1",
        "diagnostic_id": "C28.S01-D1",
        "assessment_task": "Complete the even/odd practice reconstruction and classify the source parity and proposed beat branches.",
        "answer_key": "For x=(3,1,-1,1), Ex=(1,1,1,1),Ox=(2,0,-2,0). Reconstruct x and show the even comparator cannot recover amplitudes in Ox. Read S05 R017/R021: native odd1,3,9,27 modes are structurally outside an even comparator; R028 reports25–27->2 as a retained proposed pathway, not a closed identity.",
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
    "required_command": "& 'C:\\ProgramData\\anaconda3\\Scripts\\conda.exe' run -n tf_gpu_env python 'C:\\Users\\info\\.codex\\skills\\build-high-school-course\\scripts\\validate_course.py' 'Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-28-photometer-experiments-and-information-preserving-analysis' --json"
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
    "SA-28": {
      "id": "SA-28",
      "course": 28,
      "finding": "source_fidelity",
      "lessons": [
        "lesson-03",
        "lesson-04",
        "lesson-05",
        "lesson-07"
      ],
      "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
      "requirements": [
        "Preserve zero/invalid Clear denominators, acquisition faults, gaps, direction, phase and weak channels as flagged parallel records.",
        "Keep same-polarity and inverted reflection checks separate; freeze event and comparison rules before evaluating signal outcomes.",
        "Carry C28.S01 odd-channel comparator audit and complete residual reconstruction into the capstone."
      ],
      "source_references": [
        "S05#/records/16",
        "S05#/records/20",
        "T35"
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
      "course_id": "course-28",
      "input_contract_path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-28-photometer-experiments-and-information-preserving-analysis\\input-contract.json",
      "input_contract_sha256": "af3206e71d56e97fa48869fce616a4caa58c4664dc5d8821ee56b42538034e85",
      "application": "Merge additively as teaching_amendment; preserve every original concept, SA/EA amendment and supplemental operation. Use exact exercise anchors and legacy aliases. Parent applies; no project edit performed.",
      "applied_source_amendments_read": {
        "SA-28": {
          "id": "SA-28",
          "course": 28,
          "finding": "source_fidelity",
          "lessons": [
            "lesson-03",
            "lesson-04",
            "lesson-05",
            "lesson-07"
          ],
          "merge_action": "append unique requirements to source_audit_contract; attach to named lesson authoring obligations; preserve existing fields",
          "requirements": [
            "Preserve zero/invalid Clear denominators, acquisition faults, gaps, direction, phase and weak channels as flagged parallel records.",
            "Keep same-polarity and inverted reflection checks separate; freeze event and comparison rules before evaluating signal outcomes.",
            "Carry C28.S01 odd-channel comparator audit and complete residual reconstruction into the capstone."
          ],
          "source_references": [
            "S05#/records/16",
            "S05#/records/20",
            "T35"
          ],
          "status": "applied_to_blueprint_by_parent",
          "prior_application_status": "prepared_not_applied",
          "applied_at": "2026-11-05T17:02:05.375955+00:00"
        }
      },
      "original_subject_kernel": {
        "objects_and_operations": [
          {
            "concept_id": "C28.01",
            "concept": "From light to channel readings",
            "operation": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration"
          },
          {
            "concept_id": "C28.02",
            "concept": "Acquisition identity and raw-value preservation",
            "operation": "Retain ordering, timestamps, channel identities, and fault states"
          },
          {
            "concept_id": "C28.03",
            "concept": "Normalization with an inverse account",
            "operation": "Compute a declared Clear-reference transformation and preserve its inputs"
          },
          {
            "concept_id": "C28.04",
            "concept": "Symmetry, palindromes, and signed comparisons",
            "operation": "Compare same-polarity and inverted structures without erasing weak channels"
          },
          {
            "concept_id": "C28.05",
            "concept": "Sidereal combs and event windows",
            "operation": "Freeze a geometric event rule before comparing the signal"
          },
          {
            "concept_id": "C28.06",
            "concept": "Scale and channel comparisons",
            "operation": "Keep window support, phase, and removed components replayable"
          },
          {
            "concept_id": "C28.07",
            "concept": "Uncertainty as a structured record",
            "operation": "Track calibration limits, timing, gaps, and unresolved channel structure"
          },
          {
            "concept_id": "C28.08",
            "concept": "A prospective measurement protocol",
            "operation": "Specify a reproducible forward test and retain every outcome"
          },
          {
            "concept_id": "C28.S01",
            "concept": "Comparator blindness and retained odd channels",
            "operation": "Audit whether a synthetic comparator can represent every measured parity sector; carry unrepresented odd channels forward and report the source's 25-27-to-2 triad as a retained proposed pathway."
          }
        ],
        "source_modules": [],
        "scope": "Design and execute a small synthetic photometer analysis with a frozen event rule, complete residuals, and a prospective validation plan.",
        "common_failure_modes": [
          "Untaught prerequisite",
          "Unscoped symbol or unit",
          "An illustrative example presented as real evidence",
          "A source label promoted beyond its evidence class",
          "A residual or source branch silently omitted"
        ]
      },
      "original_capstone_specification": {
        "task": "Design and execute a small synthetic photometer analysis with a frozen event rule, complete residuals, and a prospective validation plan.",
        "required_operations": [
          "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
          "Retain ordering, timestamps, channel identities, and fault states",
          "Compute a declared Clear-reference transformation and preserve its inputs",
          "Compare same-polarity and inverted structures without erasing weak channels",
          "Freeze a geometric event rule before comparing the signal",
          "Keep window support, phase, and removed components replayable",
          "Track calibration limits, timing, gaps, and unresolved channel structure",
          "Specify a reproducible forward test and retain every outcome"
        ],
        "rule": "Map every capstone operation to a prior introduction and practice; provide full answers, point rubric, source scope, and residual accounting."
      },
      "source_coverage_review_rows": [
        {
          "course_id": "course-28",
          "title": "Photometer Experiments and Information-Preserving Analysis",
          "backbone_modules": [],
          "topic_boundary": "Acquisition identity, reversible normalization, parity-complete comparators, prospective windows and every residual channel.",
          "cognitive_or_fidelity_risk": "Retain missing/gap/fault flags and Clear denominator failures in parallel.",
          "status": "source_map_review_complete_teaching_decision_pending",
          "primary_sources": [
            "series/source-registry.json"
          ],
          "source_pointer": null,
          "packet_at_review": {
            "path": "Z:\\Kfield-doc-training\\K-Field_Training_Course\\kfield-28-photometer-experiments-and-information-preserving-analysis\\input-contract.json",
            "sha256": "bf69b5b82782b47c6a44223b453dc45346525f3f281e17db6b221ad4a72e4ecd",
            "lesson_count": 8
          },
          "required_amendment_ids": [
            "SA-28"
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
          "S05",
          "T35",
          "T50",
          "SA28"
        ],
        "retention": "Retain every raw channel, exposure, acquisition identity, calibration state, invalid zero-Clear ratio, signed residual and source version. Reflection same/inverted and antipodal even/odd use different operators and are taught separately.",
        "geometry": "Freeze geometry and train/check roles before testing. Prospective protocols and synthetic arithmetic do not count as performed observations.",
        "supplement": "C28.S01 preserves the odd comparator nullspace, native ternary ladder and separately proposed 25/27->2 mechanism."
      },
      "course_map": [
        {
          "id": "lesson-01",
          "title": "From light to channel readings",
          "entry_prerequisites": [
            "course-01",
            "course-07",
            "course-24",
            "course-25",
            "course-26",
            "course-27"
          ],
          "concept_ids": [
            "C28.01"
          ],
          "worked_example_capability": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
          "assessment_target": "Specify sensor orientation, wavelength channels, gain, exposure, and calibration",
          "later_use": "lesson-02",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C28.01-E1",
          "worked_example_id": "C28.01-W1",
          "prior_practice_id": "C28.01-P1",
          "diagnostic_id": "C28.01-D1"
        },
        {
          "id": "lesson-02",
          "title": "Acquisition identity and raw-value preservation",
          "entry_prerequisites": [
            "lesson-01"
          ],
          "concept_ids": [
            "C28.02"
          ],
          "worked_example_capability": "Retain ordering, timestamps, channel identities, and fault states",
          "assessment_target": "Retain ordering, timestamps, channel identities, and fault states",
          "later_use": "lesson-03",
          "core_minutes": 55,
          "planned_periods": 1,
          "planned_total_minutes": 55,
          "explanation_id": "C28.02-E1",
          "worked_example_id": "C28.02-W1",
          "prior_practice_id": "C28.02-P1",
          "diagnostic_id": "C28.02-D1"
        },
        {
          "id": "lesson-03",
          "title": "Normalization with an inverse account",
          "entry_prerequisites": [
            "lesson-02"
          ],
          "concept_ids": [
            "C28.03"
          ],
          "worked_example_capability": "Compute a declared Clear-reference transformation and preserve its inputs",
          "assessment_target": "Compute a declared Clear-reference transformation and preserve its inputs",
          "later_use": "lesson-04",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-28"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C28.03-E1",
          "worked_example_id": "C28.03-W1",
          "prior_practice_id": "C28.03-P1",
          "diagnostic_id": "C28.03-D1"
        },
        {
          "id": "lesson-04",
          "title": "Symmetry, palindromes, and signed comparisons",
          "entry_prerequisites": [
            "lesson-03"
          ],
          "concept_ids": [
            "C28.04",
            "C28.S01"
          ],
          "worked_example_capability": "Compare same-polarity and inverted structures without erasing weak channels",
          "assessment_target": "Compare same-polarity and inverted structures without erasing weak channels",
          "later_use": "lesson-05",
          "core_minutes": 55,
          "source_coverage_requirements": [
            {
              "concept_id": "C28.S01",
              "operation": "Audit whether a synthetic comparator can represent every measured parity sector; carry unrepresented odd channels forward and report the source's 25-27-to-2 triad as a retained proposed pathway.",
              "source_pointers": [
                "S05#/records/16",
                "S05#/records/20",
                "S05#/records/27"
              ]
            }
          ],
          "pacing_rule": "Preserve every existing operation. Split into additional sessions if these bridge/practice requirements exceed the core period; update recovery checkpoints during production.",
          "required_amendment_ids": [
            "SA-28"
          ],
          "planned_periods": 3,
          "planned_total_minutes": 165,
          "explanation_id": "C28.04-E1",
          "worked_example_id": "C28.04-W1",
          "prior_practice_id": "C28.04-P1",
          "diagnostic_id": "C28.04-D1"
        },
        {
          "id": "lesson-05",
          "title": "Sidereal combs and event windows",
          "entry_prerequisites": [
            "lesson-04"
          ],
          "concept_ids": [
            "C28.05"
          ],
          "worked_example_capability": "Freeze a geometric event rule before comparing the signal",
          "assessment_target": "Freeze a geometric event rule before comparing the signal",
          "later_use": "lesson-06",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-28"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C28.05-E1",
          "worked_example_id": "C28.05-W1",
          "prior_practice_id": "C28.05-P1",
          "diagnostic_id": "C28.05-D1"
        },
        {
          "id": "lesson-06",
          "title": "Scale and channel comparisons",
          "entry_prerequisites": [
            "lesson-05"
          ],
          "concept_ids": [
            "C28.06"
          ],
          "worked_example_capability": "Keep window support, phase, and removed components replayable",
          "assessment_target": "Keep window support, phase, and removed components replayable",
          "later_use": "lesson-07",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C28.06-E1",
          "worked_example_id": "C28.06-W1",
          "prior_practice_id": "C28.06-P1",
          "diagnostic_id": "C28.06-D1"
        },
        {
          "id": "lesson-07",
          "title": "Uncertainty as a structured record",
          "entry_prerequisites": [
            "lesson-06"
          ],
          "concept_ids": [
            "C28.07"
          ],
          "worked_example_capability": "Track calibration limits, timing, gaps, and unresolved channel structure",
          "assessment_target": "Track calibration limits, timing, gaps, and unresolved channel structure",
          "later_use": "lesson-08",
          "core_minutes": 55,
          "required_amendment_ids": [
            "SA-28"
          ],
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C28.07-E1",
          "worked_example_id": "C28.07-W1",
          "prior_practice_id": "C28.07-P1",
          "diagnostic_id": "C28.07-D1"
        },
        {
          "id": "lesson-08",
          "title": "A prospective measurement protocol",
          "entry_prerequisites": [
            "lesson-07"
          ],
          "concept_ids": [
            "C28.08"
          ],
          "worked_example_capability": "Specify a reproducible forward test and retain every outcome",
          "assessment_target": "Specify a reproducible forward test and retain every outcome",
          "later_use": "capstone",
          "core_minutes": 55,
          "planned_periods": 2,
          "planned_total_minutes": 110,
          "explanation_id": "C28.08-E1",
          "worked_example_id": "C28.08-W1",
          "prior_practice_id": "C28.08-P1",
          "diagnostic_id": "C28.08-D1"
        }
      ],
      "legacy_bridge_aliases": [],
      "core_periods": 15,
      "capstone_periods": 3,
      "period_minutes": 55,
      "capstone_total_points": 36,
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
