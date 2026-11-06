# Source notes and evidence boundaries

All sources were read-only. No raw source acquisition, full-array archive, source snapshot or large npz was copied. Compact derived replay diagnostics and the single required four-count source card are teaching/verification artifacts. Pinned objects were read in memory; whole-object hashes and pointers retain every underlying field.

Corpus generation and manifest: sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7. Fresh search confirmed both. Capabilities enumerated the read-only interface; exact artifacts were then retrieved by digest. Search coverage is not an exhaustive corpus certificate.

## Pinned application sources

**T35** — `applications/kfield_lucas_lab/rag_corpus/35_spectral_energy_phase.md`  
SHA-256: `03dc7e11045b3912f1e8cc0d69a4789b6ad300ac78b4549ea86c45e51228c7bc`. Complete range [0,3018) read, returned digest matched. Pointers: whole document.

**T50** — `applications/kfield_lucas_lab/rag_corpus/50_physical_closure.md`  
SHA-256: `c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a`. Complete range [0,1761) read, returned digest matched. Pointers: whole document.

**spectral_bundle** — `applications/kfield_lucas_lab/contracts/spectrophotometer_evidence_bundle_v1.json`  
SHA-256: `04044230f3b2536d22654b294760106eca301f212e4eb4157989b330ff611f17`. Complete range [0,6438) read, returned digest matched. Pointers: /cross_document_integrity, /works, /interpretation_boundaries, /to_be_filled.

**spectral_work** — `applications/kfield_lucas_lab/sources/K-Field_spectrophotometer_quadratic_phase_cost_analysis_1787748698.json`  
SHA-256: `d4105a6d6802e6bb2a2ba8e76a1d23a27973fca3d3335fd8335690a41ab72dfa`. Complete range [0,48364) read, returned digest matched. Pointers: /formulas, /events/0..13, /quadratic_phase_cost, /dataset.

**energy_work** — `applications/kfield_lucas_lab/sources/K-Field_spectrophotometer_energy_per_200ms_reading_1787713812.json`  
SHA-256: `9120f80210b235b8612d6479fe25272eb3824f31c5a1394e7e9d12718e57e70f`. Complete range [0,22424) read, returned digest matched. Pointers: /estimators, /all_event_channel_modulations/0..13, /energy_equivalent_results, /constants.

T35 supplies four-angle contrast, ratio and input-energy definitions plus evidence obligations. T50's item 4 supplies the optical-transfer ambiguity boundary. We do not claim to have compiled its referenced Agda modules. spectral_bundle is the binding contract for representations, revisions and source obligations. spectral_work /formulas calls fractional gain G; T35 calls contrast counts G. Lessons use contrast_counts and fractional_gain. energy_work uses lambda-sheet where the spectral family is lambda; this alias is explicit.

## Local archive sources

**S01** — `Z:/Archive_20260911/Aug14_Sept1/K-Field_Mathematical_Essence_Corrected_Complete_Proof_1788231864.json`  
SHA-256: `18f5d20233981c97bf991e0b409020e917815647e5099df56ad9fa1763da6180`. Historical corrected branch; byte identity checked, no constants imported.

**S02** — `Z:/Archive_20260911/Aug14_Sept1/K-Field_Mathematical_Essence_Mature_Complete_Proof_1788234894.json`  
SHA-256: `6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3`. /typed_conventions and /mature_locked_cell3 inspected for symbol/orientation guards. No fresh proof verification claimed.

**S03** — `Z:/Archive_20260911/Aug14_Sept1/K-Field_Mathematical_Essence_Authoritative_Audit_Correction_Instruction_1788263935.json`  
SHA-256: `f54c6c7515205dbbcc498864b1415755aa767d5274194140150b2b16979d656e`. Audit-correction source; identity checked; do not merge historical and mature branches.

**S04** — `Z:/Archive_20260911/Aug14_Sept1/K-Field_Mathematical_Essence_Mature_Corpus_Audit_1788234146.json`  
SHA-256: `77c0ab41a911fc819d3bcba0667d9127294b3dacf0634aec9add6e45e8c023a2`. Archive audit source, identity checked; reported audit is not our fresh compiler result.

**S05** — `Z:/Archive_20260911/Aug14_Sept1/K-Field_3D_periodic_table_hidden_dimensions_recent24h_1788145361.json`  
SHA-256: `d17197c1bec71893e1fd8344e0a35f6e63da3668f35dc3085247a66ad112eae7`. /records/15,16,20,25,26,27 read exactly in place.

S05 pointers use zero-based indices: /records/15 is R016, an archive_stated observation of nine-channel odd AC fractions about 0.504–0.536; /records/16 is R017, the archive_stated comparator equation; /records/20 is R021, a synthesis about the native ternary nullspace. /records/25 R026 is cutoff/dimension synthesis, /records/26 R027 compares 27 and 25, and /records/27 R028 evaluates a retained beat pathway. R028 reports rank 5 of 22 adjacent odd pairs and strongest response in F7; those are source statements, not replays of its underlying arrays. No course result promotes them to a closed identity.

## Exact retained source conditions

The spectral bundle's /cross_document_integrity declares energy revision f98cfec9980986adda0eb44cc91ab26f524dec9e5e3bae3d153cb947f13d324a but packages 9120f80210b235b8612d6479fe25272eb3824f31c5a1394e7e9d12718e57e70f. Its quadratic PDF record declares 989c5fe7d230e5bddc3727420710c232bb550ba8305e9b6f6baa6dba42ec2e6d and 509185 bytes, versus packaged 35b3af799854f5dd9070c660a7e9cbcd0c27c20087a011a612cdfdfda545a052 and 530068 bytes. Keep that mismatch; no silent correction was made.

All 14 /events rows and linked energy /all_event_channel_modulations rows are retained by these whole-object digests, exact pointers and derived row diagnostics in source-replay.json. Diagnostics preserve pair identity, time, channel, sign, family, energy presence, pair means, half-differences and signed closure. Source velocity signs, all other phase coordinates and source uncertainty fields remain available in the immutable objects; no summary substitutes for them. Covariance not supplied is not assumed zero. Family summaries do not replace response rows.

Source dataset pointers /dataset report 65880 rows, 65845 healthy and 35 excluded_diagnostic_rows. This course's retention policy requires all original diagnostic rows, their masks/reasons and any corrected view in a future production replay; the source's exclusion label is not permission to erase them. Raw source bytes were not acquired here.

The unresolved measurement obligations are raw pic_id21A.csv, LED datasheet, radiometric calibration, blank/reference ledger, uncertainty, angular interpolation/mechanical uncertainty, exposure-transfer/down-conversion witness and independent preregistered replay. The acquisition grid is 4 degrees, not the finer displayed interpolation separation. Keep experiment-local trajectory separate from physical CMB authority 369812.50200040644 m/s and from any phase-transformed vector; the Galactic Center remains a visual gauge. No short-window Solar/Galactic dynamics are invented.

## What was newly verified

Fresh checks cover pinned byte identity, finite synthetic arithmetic and reconstruction, complete source-row accounting and reported-event binary64 arithmetic. They do not certify raw acquisition, source interval bounds, detector calibration, transferred energy, compiler bodies or a proposed coupling mechanism. Exact rational teaching examples and binary64 source replay are labeled separately. See verification.json, source-replay.json and independent-audit.json for actual checks.
