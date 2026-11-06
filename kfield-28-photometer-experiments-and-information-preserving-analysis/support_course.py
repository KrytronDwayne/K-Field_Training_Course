from build_course import *

def supports():
 rows=['# Course map','',P['topic'],'','Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, ratios, powers, simple linear equations and coordinate graphs. Courses 01,07,24–27 are named background prerequisites; this course teaches its finite operators explicitly.','', 'Eight lessons occupy 15 periods of 55 minutes (825 minutes); the capstone adds three periods (165 minutes), total 18 periods / 990 minutes. Unit A: lessons 1–3 (records and ratios). Unit B: lessons 4–6 (comparators, events and scale). Unit C: lessons 7–8 (uncertainty and prospective tests).','', '| Concept | Introduction / worked / practice / diagnostic | Assessment | Later use | Periods |','|---|---|---|---|---|']
 for i,L in enumerate(P['course_map']):
  cid=L['teaching_anchor']['concept_id']
  rows.append(f"| {cid} | [{L['id']}]({L['id']}.md): {cid}-E1 / W1 / P1 / D1 | C28-CAP-{i+1:02} | {L['later_use']} | {L['teaching_anchor']['planned_periods']} |")
 rows+=['| C28.S01 | lesson-04: C28.S01-E1 / W1 / P1 / D1 | C28-CAP-09 | lessons 5–8 and capstone | Included in lesson 4 |','', 'The original lesson order and exercise IDs are preserved. Lesson 4 includes explicit complex-number arithmetic and inverse sums to close the DFT prerequisite. Its three periods separate reflection, half-turn parity, and comparator/DFT/source branches. No other course is required to supply missing operations.','', 'Recovery gate at each lesson: reproduce the worked input, answer diagnostics, and repair any misunderstanding before its dependent lesson. Unit reviews compare definitions, support and evidence scope. See teacher-guide.md. All nine capstone operations have a named prior practice; the capstone introduces no new transform.']
 write('course-map.md','\n'.join(rows))
 write('terminology.md','''# Terminology and notation

| Term/symbol | Meaning and unit/domain | First lesson |
|---|---|---|
| Channel / response identity | Named detector pathway and its wavelength-response definition | 1 |
| nm | Nanometre, 10^-9 metre; nominal wavelength is not a response curve | 1 |
| Count | Instrument output unit; not automatically energy or power | 1 |
| Gain / exposure e | Instrument setting / acquisition duration in seconds | 1 |
| Calibration | Documented input/output relation with conditions and reference | 1 |
| Sensor normal +z | Perpendicular direction in the declared toy bench frame | 1 |
| t / support | Elapsed midpoint seconds / contributing interval or sample set, explicitly stated | 1 |
| Acquisition key | Device, session, sequence and channel; timestamp accompanies it | 2 |
| Null / absent / zero | Explicit missing numeric entry / missing expected acquisition / numeric value | 2 |
| Flag / mask | Diagnostic state and reason / named view's parallel validity record | 2 |
| A, C | Spectral count and same-row Clear count (Clear is abbreviated C in formulas) | 1 |
| r=A/C | Dimensionless same-row Clear-reference ratio on its declared valid domain | 3 |
| delta | Exact ratio minus displayed ratio; signed rounding closure | 3 |
| R, s, a | Declared reversal; (x+Rx)/2 same component; (x-Rx)/2 inverted component | 4 |
| H, E, O, I | Two-position shift on four-point circle; even/odd/identity operations | 4 |
| Parity | Sign under the explicitly named operator; R parity and H parity differ | 4 |
| Dot product | Sum of matching-entry products | 4 |
| Nullspace | Inputs a comparator maps to zero | 4 |
| DFT / Fj | Four-sample discrete Fourier transform / complex coefficient at index j | 4 |
| i | Imaginary unit, i*i=-1; coefficient a+bi has two signed coordinates | 4 |
| Phase / magnitude | Cycle position encoded in complex coefficients / size without position | 4,6 |
| Aliasing | Different native indices produce identical sampled weights | 4 |
| Harmonic | Integer cycle count relative to a declared period | 4 |
| Ternary ladder | Source ladder multiplying by 3: 1,3,9,27 | 4 |
| q,k / comb | Unwrapped toy phase in cycles, integer event index / fixed event list | 5 |
| Ephemeris / sidereal | Versioned astronomical positions / relative to celestial directions | 5 |
| m,d_i | Mean over named support / signed detail x_i-m in input units | 6 |
| k in lesson 7 | Locally scoped calibration factor, output units/count; distinct from event index k | 7 |
| delta_t | Shared clock offset in seconds | 7 |
| Identifiability | Whether supplied outputs determine the requested separate inputs/parameters | 7 |
| Prospective / exploratory | Frozen before new outcome inspection / revised using inspected outcomes | 8 |

Evidence labels: synthetic input (authored); derived transform (arithmetic from named inputs); source-reported observation (archive statement); inferred structure (interpretation); proposed mechanism (candidate process); reference theory (comparison model); unresolved information (retained incomplete account). None automatically promotes another.

Avoid cross-course collisions: this course does not use Q for a projector or for distance. In T35, Q is a source-local quadrature baseline; it is not a Cell3 distance. M_cell, R_cell, G_phase and G_eff retain their packet types and are not required for the finite student arithmetic. The toy +z frame is not ICRS. The DFT index is not a backbone/compiler module label.
''')
 write('teacher-guide.md','''# Teacher guide

Teach the course with paper, a four-position circle sketch, and a basic calculator if desired. No hardware, package installation, raw database export or astronomical calculation is required. All numerical teaching records are synthetic. Students should be able to add signed numbers, work with fractions and solve t/2=k. Check those capabilities with 5-8=-3, 2/10=1/5 and t/2=2 giving t=4 before lesson 1.

Each 55-minute period allocates 5 minutes to retrieval, 20 to explanation and a worked example, 15 to guided practice, and 15 to diagnostics and repair. In multiperiod lessons follow the named session focuses in each lesson. Use the first practice pass with the answer covered, then compare each retained field with the worked answer. Homework is optional; no essential instruction depends on it.

| Lesson | Periods | Teaching focus and readiness gate |
|---|---:|---|
| 1 | 1 | Draw sensor normal and exposure interval; student labels counts and missing calibration correctly. |
| 2 | 1 | Build raw and gap ledgers; student keeps duplicate times, zero and faults distinct. |
| 3 | 2 | First valid/invalid ratios, then exact reconstruction and rounding closure. Student recovers all five raw values including the invalid row. |
| 4 | 3 | First reversal; second half-turn and dot products; third complex arithmetic/DFT and source cards. Student demonstrates the two operators differ and inverts the odd spectrum. |
| 5 | 2 | Solve frozen events, then partial windows and parallel masks. Student lists all three windows. |
| 6 | 2 | Mean/detail, then changed support and phase. Student reconstructs the full and window records. |
| 7 | 2 | Positive interval products, then shared timing and exposure. Student distinguishes a support union from exposure duration. |
| 8 | 2 | Assemble evidence ledger, then freeze forward protocol and classify gaps. Student states what remains planned. |

Unit A review after lesson 3: ask students to reconstruct raw A=(2,5,8,1,3). Correct answers use valid products and the retained raw row 1. Misconception “undefined means zero” requires revisiting lesson 3 before windows.

Unit B review after lesson 6: ask students to apply R and H to the same four-entry list and explain why they differ. Then reconstruct the five-point mean/detail example. A student who has memorized a score without fields has not met the retention outcome. Return to lesson 4 or 6 as appropriate.

Unit C review after lesson 8: request an evidence ledger with synthetic, source-reported, derived, inferred, proposed and unresolved fields. A frozen protocol may predict a comparison, but the physical run is still planned. Student claims of real calibration from the toy factor require correction in lesson 7.

Complex arithmetic support: have students compute i*(2+3i)=2i+3*(-1)=-3+2i, then (-i)*(2+3i)=3-2i. The DFT uses only multiplication by 1,-1,i,-i and addition. A full trigonometry course is unnecessary. For independent practice, the odd input (2,0,-2,0) yields (0,4,0,4), with inverse factor 1/4.

For a weak-channel extension multiply every entry of the lesson 4 vector x=(1,2,4,3) by 1/100. Its components and defects also scale by 1/100; no channel disappears. Keep this as answered optional transfer practice: reflection components become (0.02,0.03,0.03,0.02) and (-0.01,-0.01,0.01,0.01).

Capstone: three 55-minute periods. Period 1 builds the typed ledger and ratios (steps 1–3); period 2 computes windows, reflection, mean/detail and comparator fields (steps 4–6 and 9); period 3 completes uncertainty, prospective protocol, reconstruction and evidence audit (steps 7–8 plus repairs). Use the 36-point rubric. Award reasoning and retained information separately from arithmetic; correct a mistaken result without discarding the student's residual account.

If diagnostic repair takes longer, add a recovery period and record the actual pacing. Fifteen core periods are a plan, not evidence that every class will finish at that speed. Source claims are evaluated at the scope of sources.md. Do not assign native-data numerical replay: complete native arrays and physical calibration inputs are not part of this course.
''')

 write('capstone.md','''# Capstone — a complete information-preserving rehearsal

Work for three periods with the lessons available. Label the entire numerical submission **synthetic rehearsal**. Preserve raw inputs, ordered identities, every signed field, masks and inverse rules. Use the nine named steps below; each is worth 4 points, total 36.

Input card: device T, session A; toy bench frame x right, y away, z up; normal +z; gain setting 1; exposure 0.2 s; A nominal 500 nm (response A-toy), Clear broadband (C-toy); calibration missing. Sequence 0..4 has midpoint t=0..4 s, A=(2,5,8,1,3), C=(10,0,20,10,10). Row 3 has stipulated suspected-saturation flag with reason “synthetic instrument-status exercise”; raw values remain. Sequence 5 at expected t=5 s is absent. Optional separate B-toy at row 2 is nominal 600 nm with count 4.

Freeze Toy-v1 before calculations: z(t)=(1 m/s)t, origin 0, normal +z, spacing 2 m; q=t/(2 s); events integer q over midpoint interval [0,4] s; exact midpoint offsets (-1,0,1) s, no interpolation or zero padding. All flags travel with their keys. The four-point reflection and parity inputs below are separate synthetic exercise records, not selections silently extracted from session A.

## Student tasks

1. **C28-CAP-01 (lesson-01 P1):** Write the row-2 acquisition card and exposure support. Explain what A/B=8/4 can and cannot mean.
2. **C28-CAP-02 (lesson-02 P1):** Retain all five raw rows, the row-3 flag and a separate expected sequence-5 gap record. State a key that preserves simultaneous channels and explain how original sequence restores a sorted display.
3. **C28-CAP-03 (lesson-03 P1):** Compute all Clear ratios and reconstruct A. Separately calculate the exact closure for displaying 1/3 as 0.3333333333. Compare 0/5 and 0/0.
4. **C28-CAP-04 (lesson-04 P1):** For x=(3,1,-1,1), compute R, s, a and both defects. Also test (-2,0,2) for inversion about its middle sample. State how a weak channel would be retained.
5. **C28-CAP-05 (lesson-05 P1):** Solve the event rule, list all raw and normalized windows with support masks, and compute the center-2 side difference and sum. Explain why the rule cannot be called a physical sidereal prediction.
6. **C28-CAP-06 (lesson-06 P1):** Compute full-record and center-2-window means/details and reconstruct both inputs. State what the DFT inverse requires and why magnitude alone is insufficient.
7. **C28-CAP-07 (lesson-07 P1):** With synthetic positive box bounds k=[1.9,2.1] units/count and x=[0.9,1.1] counts, compute product bounds. Apply shared clock offset [-0.1,0.1] s to midpoint 2 s, then add exposure support. List unresolved contributors separately.
8. **C28-CAP-08 (lesson-08 P1):** Write a forward rehearsal protocol over midpoint interval [0,10) s at cadence 1 s, exposure 0.2 s. Include version, keys, geometry, masks, controls, stopping/interruptions, train/check roles and every outcome. Identify required replacements before a real physical test. Classify synthetic arithmetic, archived report, proposed mechanism and planned measurement.
9. **C28-CAP-09 (lesson-04 C28.S01-P1):** For x=(3,1,-1,1), compute Ex and Ox, their reconstruction and the odd DFT. Show an even comparator cannot represent Ox. Separately classify the source native ternary ladder, Fibonacci-cutoff proposal and 25–27→2 pathway, including the four-point aliasing boundary.

## Full answer key and point rubric

Each numbered answer gives four one-point criteria. Equivalent precise wording earns credit. All fields must be traceable to their declared input; a mismatch is repaired and retained rather than erased.

1. (1) Row key T/A/2/A with t=2 s and A=8 counts; paired C=20 with its own channel identity. (1) Exposure [1.9,2.1] s from 2±0.1. (1) +z normal, gain 1, nominal wavelengths and response IDs retained. (1) Ratio 2 is a count ratio, not calibrated spectral power; calibration is missing. B=4 is a separate supplied channel, not a fabricated full B series.

2. (1) Raw ledger rows (sequence,t,A,C) are (0,0,2,10),(1,1,5,0),(2,2,8,20),(3,3,1,10),(4,4,3,10), with counts and seconds typed. (1) Row 3 retains its stipulated flag/reason beside A=1 and C=10. (1) Expectation ledger says sequence 5,t=5 absent, no invented count. (1) Keys include device/session/sequence/channel; original sequence can restore order despite duplicate timestamps or display sorting.

3. (1) r=(1/5,undefined,2/5,1/10,3/10), mask (1,0,1,1,1); row 3 retains its diagnostic flag independently. (1) Products return 2,8,1,3 on valid rows; retained row 1 returns A=5,C=0 directly. (1) Exact delta=1/30000000000 and A=(display+delta)*3=1 for the separate rounding example. (1) 0/5=0 is valid; 0/0 is undefined. Keep inputs, decimal rule, response identities and masks.

4. (1) Rx=(1,-1,1,3), s=(2,0,0,2). (1) a=(1,1,-1,-1), so s+a=(3,1,-1,1). (1) Same defect=(2,2,-2,-2), inverted defect=(4,0,0,4). For (-2,0,2), reversal=(2,0,-2)=-x and inverted defect=(0,0,0). (1) Retain both signs, fixed center/support and every channel; a nonzero center contributes to the same component, and weakness is not a deletion rule.

5. (1) Events at t=0,2,4 s; raw windows (absent,2,5),(5,8,1),(1,3,absent) with masks (0,1,1),(1,1,1),(1,1,0). (1) Ratio windows (absent,1/5,undefined),(undefined,2/5,1/10),(1/10,3/10,absent), validity masks (0,1,0),(0,1,1),(1,1,0); keep reasons for absent versus undefined. (1) Center-2 side difference 4, sum 6, center 8 retained. (1) Geometry is synthetic; real site/time/ephemeris/orientation/event/calibration versions remain required. No center shifts or dropped edge windows.

6. (1) Full mean 19/5, detail (-9/5,6/5,21/5,-14/5,-4/5), reconstructing (2,5,8,1,3). (1) Window mean 14/3, detail (1/3,10/3,-11/3), reconstructing (5,8,1). (1) Support, ordering, flags, weights and both fields retained; different means have different supports. (1) DFT requires both complex coordinates, sample order, transform signs and inverse 1/4; single pulses at different positions have equal magnitudes but different phases.

7. (1) Positive box bounds give [1.9*0.9,2.1*1.1]=[1.71,2.31] output units. (1) Midpoint [1.9,2.1] s. (1) Possible exposure support [1.8,2.2] s; each exposure still lasts 0.2 s and common clock offset is shared. (1) Retain missing calibration, orientation/angular uncertainty, gaps, zero Clear, stipulated saturation, unresolved channel structure and transfer assumptions as distinct contributors. These synthetic bounds do not calibrate the actual instrument.

8. (1) Forward-Toy-v1 freezes ten expected midpoints 0..9, duration interval [0,10), gain/orientation/response IDs and exposure 0.2; acquisition coverage begins -0.1 relative to first midpoint. (1) Freeze q=t/(2 s), exact offsets/no interpolation, all raw/ratio/parity/mean-detail fields and validity reasons; prior training is none for this authored toy, and future values cannot tune the check rule. (1) Stop after tenth scheduled midpoint or record interruption; retain every outcome and a separately identified same-setting blank/reference control. (1) Real-test v1 remains planned until site, UTC time scale, ephemeris, physical geometry and calibration/transfer references replace the toy inputs. Archive statements stay reported; 25–27→2 stays proposed; toy arithmetic stays synthetic. A changed rule receives a new exploratory version.

9. (1) Hx=(-1,1,3,1), Ex=(1,1,1,1), Ox=(2,0,-2,0); sum restores x. (1) Odd DFT=(0,4,0,4); inverse gives (2,0,-2,0). (1) (p,q,p,q) dot Ox=2p-2p=0; all circular shifts are also even, so comparator blindness cannot justify dropping Ox. (1) S05 R021's 1,3,9,27 is a source synthesis; R026's Fibonacci-related cutoff continuation and R028's 25–27→2 are separate branches, the latter a retained proposed pathway. Four samples alias native 25 and 27 modulo 4 and cannot newly verify their coupling. Retain the unrepresented odd field and full comparison residuals.

Final reconstruction audit: all five raw A values remain recoverable; all three event windows remain listed; all invalid/absent reasons remain distinguishable; reflection and half-turn parity are separate; proposed mechanism is not silently promoted to measured energy. Use sources.md for exact source addresses.
''')

 sources=[]
 for s in P['sources']:
  if 'path' in s:
   actual=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()
   assert actual==s['sha256']
   sources.append(dict(s,verified_sha256=actual,read_scope='Hash verified; no source-specific theorem body is used in this course. Backbone invariants retained from input contract.'))
 s05=next(s for s in P['teaching_blueprint_contract']['source_basis'] if s['id']=='S05')
 assert hashlib.sha256(Path(s05['path']).read_bytes()).hexdigest()==s05['sha256']
 sources.append(dict(s05,read_scope='Fresh local records 16,18,20,25,26,27 read; zero-based JSON pointers.',pointers=['/records/16','/records/18','/records/20','/records/25','/records/26','/records/27']))
 for sid,s in zip(['T35','T50'],[s for s in P['sources'] if 'logical_path' in s]):
  sources.append(dict(s,id=sid,read_scope='Full bounded krytronx_get bytes read; range digest equals pinned SHA-256.',byte_range=[0,3018 if sid=='T35' else 1761],evidence_class='source'))
 dump('sources.json',{'sources':sources,'generation':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','manifest_sha256':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','freshness':'Capabilities called; snapshot identity absent there, confirmed by subsequent rerank:false RAG response. Search was discovery only; exact claims grounded in bounded pinned sources/local records.','source_copies_created':False,'gaps':['Native AS7341 arrays and their original calculation contracts not replayed.','No physical run, radiometric calibration or exposure transfer supplied.','No fresh Agda/compiler or backbone proof verification; source status stays reported.']})
 write('sources.md','''# Source notes and evidence boundaries

The exact paths, SHA-256 values and scopes are in sources.json. Source files remain in place; no raw archive, database export or large array was copied. A hash verifies byte identity, not the truth of every claim in those bytes.

S05 is `Z:/Archive_20260911/Aug14_Sept1/K-Field_3D_periodic_table_hidden_dimensions_recent24h_1788145361.json`, SHA-256 `d17197c1bec71893e1fd8344e0a35f6e63da3668f35dc3085247a66ad112eae7`. Freshly read exact records:

| Pointer (zero-based) / record | Source evidence class | What the course uses |
|---|---|---|
| /records/16 / R017 | archive_stated | Antipodally symmetric comparator has odd-harmonic structural zeros. |
| /records/18 / R019 | archive_stated | Reported cutoffs 1,3,5,9,15 and modulation fractions 2/45,4/45,6/45,10/45,16/45. |
| /records/20 / R021 | synthesis | Native ternary ladder 1,3,9,27 lies in the comparator's odd nullspace. |
| /records/25 / R026 | synthesis | Dimensions 2,4,6,10,16 equal twice 1,2,3,5,8; proposed continuation gives dimensions 26,42 and cutoffs 25,41. |
| /records/26 / R027 | synthesis | Ternary and cutoff ladders meet at 1,3,9 and diverge at 27 versus 25. |
| /records/27 / R028 | synthesis | The 25–27→2 triad remains a retained pathway, not a closed identity. |

The source R028 also reports rank fifth of 22 adjacent odd pairs and strongest response in F7. This course does not recompute that ranking or assign a new evidentiary status. Native arrays remain unexported. The four-point exercise verifies the comparator's finite algebra, not the native harmonic numbers or physical coupling.

T35: `applications/kfield_lucas_lab/rag_corpus/35_spectral_energy_phase.md`, SHA-256 `03dc7e11045b3912f1e8cc0d69a4789b6ad300ac78b4549ea86c45e51228c7bc`, full bytes [0,3018). Its “Constructive and categorical boundary” and “Open obligations” separate model-equivalent input energy from apparatus transferred-energy measurement. Fourteen event rows share three distinct plane-family cost levels; two works with three representations each are two bundles, not six independent studies. The source status is reported_exploratory_to_be_verified. No numerical event rows are reproduced or silently selected here; the source bundle is retained by its immutable reference. Lessons 1,7,8 use the calibration and exposure-transfer boundary only, not a fresh event replay.

T50: `applications/kfield_lucas_lab/rag_corpus/50_physical_closure.md`, SHA-256 `c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a`, full bytes [0,1761). Numbered result 4 is the optical-transfer identifiability boundary. Result 2's reported angular-response law is distinct from physical K-field co-rotation. Results 1 and 3 retain finite-candidate and conditional-premise scopes. This course reads their reported dispositions; it does not execute the formal artifacts named inside them.

S01–S04 hashes were freshly checked against the supplied contract. They are background mathematical-essence sources; no backbone theorem is invoked by the finite photometer arithmetic. The course does not mix historical constants with the mature lock, construct new Cell3 geometry, or identify a compiler module with a mathematical module. The full invariant list remains in input-contract.json.

Operational references read: residual-information-paradigm/SKILL.md (raw and residual retention); clear-normalize/SKILL.md (same-record reference, ten significant digits, stricter positive-C software domain); sidereal-alignment-comb/SKILL.md (separate calibration and frozen prediction, explicit event geometry). This course implements no real sidereal pipeline or retained calibration. The runtime packet's prospective-test requirement governs the toy training/check separation. No source skill permits replacing missing observations with toy values.

Remaining source gaps are scope limits, not hidden lesson prerequisites: native arrays are not replayed; physical calibration and exposure transfer are not supplied; formal theorem bodies are not freshly checked. Every required core task is finite and synthetic and can be solved from these lessons.
''')

if __name__=='__main__': supports()


