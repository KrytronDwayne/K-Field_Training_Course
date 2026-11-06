from pathlib import Path
import json,hashlib,math,sys
R=Path(__file__).parent
C=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
def w(p,s): (R/p).write_text(s.strip()+'\n',encoding='utf-8')
def j(p,x): w(p,json.dumps(x,indent=2,ensure_ascii=False))
def h(p): return hashlib.sha256((R/p).read_bytes()).hexdigest()
w('course-map.md','''# Moving Reference Frames and Laboratory Motion

Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs, plus the coordinate capabilities named in courses 02–04. This course reintroduces matrix application/inversion, trigonometry and the limited derivative rules it uses; no prior calculus is assumed.

Eleven core 55-minute periods plus three capstone periods. Lessons 1–4 each use two periods; lessons 5–7 one each. Lesson 4 may use an extra recovery period if students cannot explain a limiting rate and the product rule. This preserves all approved content instead of hiding a prerequisite. No new substantive instruction is added during assembly.

|Concept|Introduction/worked example|Answered prior practice|Diagnostic|Capstone/later use|
|---|---|---|---|---|
'''+ '\n'.join(f'|C24.{i:02}|[Lesson {i}](lesson-{i:02}.md), C24.{i:02}-E1/W1|C24.{i:02}-P1|C24.{i:02}-D1|C24-CAP-{i:02}; '+('lesson '+str(i+1) if i<7 else 'reproducible synthesis')+'|' for i in range(1,8))+'''

Dependency order: origins/axes/time → spherical and local components → nested motion → moving-axis rates → carried/fixed comparison → display/source scope → reproducible contract. Cumulative checks occur after lessons 2, 4 and 7.

Legacy anchors: C24-FRAME-EX1 names both the Lesson 1 trajectory bridge and Lesson 2 spherical example. C24-FRAME-P1 aliases C24.02-P1. C24-TRAJ-D1 aliases C24.01-P1. All are present in the student text. SA-24 is implemented in lessons 3–6; EA-24-E10-7 in lessons 1–2. Every capstone operation has prior answered practice.

Deliverables: seven student lessons, assembled course, terminology, teacher guide, capstone with answers/rubric, source ledger, executable verification and recovery/audit reports. Mathematical-backbone topics not used in this topical course remain governed by the unchanged input contract; no substitute Cell3 constants, metrics, parity rules or integration authority are introduced.
''')
w('terminology.md','''# Terms and notation

|Term/symbol|Meaning and units/convention|First use|
|---|---|---|
|Frame; origin O|Axes and reference point used to assign coordinates|1|
|Epoch t0|Named time for a state; distinct from publication date|1|
|p,x,o|Position, trajectory position, origin offset; local length units stated|1|
|v; Δt|Velocity (length/time); elapsed duration in seconds|1|
|R; R^T|Dimensionless orthonormal rotation; transpose/inverse|1|
|ICRS|Common celestial reference-system axes; not by itself an origin/time|2|
|α, δ, r|RA from +x toward +y; declination from xy-plane; nonnegative length|2|
|RA hours|Angular labels: 24h=360°; not elapsed time|2|
|sin, cos; radian|Unit-circle coordinates; arc/radius angle|2|
|L; norm |p||Declared length unit; √(x²+y²+z²)|2|
|E,N,U|Local east/north/up unit vectors in declared common axes|2|
|CMB; EMB|Cosmic microwave background; Earth–Moon barycenter|3|
|v_A/B|Velocity of A relative to B, with common axes/time/units required|3|
|G_phase V|Phase-transformed vector; not the admitted physical CMB velocity|3|
|Derivative; dot; acceleration|Limiting rate; one time derivative; velocity rate in m/s²|4|
|ω|Angular speed, rad/s; ωt is the angle|4|
|Residual r|Comparison minus model; context distinct from Lesson 2 radius|4|
|e_x,e_y,e_z|Cartesian unit vectors|5|
|Dot product u·v|Sum of three coordinate products|5|
|Hat; arccos; antipodal|Unit vector; inverse cosine; identification of opposite directions|5|
|Cell3|Source-defined geometry; distinct from the orthonormal toy triad|5|
|Gauge; scale chamber|Chosen visual comparison; independently scaled display region|6|
|Sgr A*|Source's Galactic-center sightline target|6|
|UTC/TAI/TT/TDB|Distinct time-scale labels, with conversions explicitly required when used|7|
|Ephemeris; EOP; datum|Celestial time-dependent record; Earth orientation parameters; site reference convention|7|
|SHA-256|Byte fingerprint, not a proof or evidence-class promotion|7|
|Interpolation|Declared rule for values between supplied samples|7|

Evidence labels: synthetic definition = invented teaching input explicitly declared; derived = result of stated arithmetic/model; source-reported = read claim, not freshly proved; interpretation = meaning assigned within scope; proposed mechanism = explanatory hypothesis; unresolved = missing input or open claim. Established reference mathematics includes the coordinate, trigonometric and differentiable-function rules taught here.
'''.replace('|L; norm |p||','|L; vector norm|'))
w('teacher-guide.md','''# Teacher guide

Plan 14 periods of 55 minutes: eleven core and three capstone. For each core period use 5 minutes of retrieval, 20 of explanation and worked example, 15 of answered practice with the answer initially covered, and 15 of independent diagnostics and repair. Retain original student answers alongside corrections so errors become useful records of missing operations.

|Period|Teaching focus|Advance only when students can…|
|---|---|---|
|1|Lesson 1 origins, axes, matrix rows and inverse|Undo translation before applying transpose|
|2|Lesson 1 update/reversal|Label all three epochs and recover p0|
|3|Lesson 2 unit circle, hours and radians|Explain why 6h means 90°|
|4|Lesson 2 triad and normalization|Recover magnitude times unit direction|
|5|Lesson 3 chain types|Name all four relative terms without double counting|
|6|Lesson 3 decomposed trajectory|Retain both signed x contributions|
|7|Lesson 4 limiting rates and product rule|Explain why a product has two derivative terms|
|8|Lesson 4 moving frame and cancellation|Keep rotational velocity when local velocity is zero|
|9|Lesson 5 carried/fixed layers|Distinguish directed 180° from axial 0°|
|10|Lesson 6 scales and source scope|Limit nonalignment to the displayed finite set|
|11|Lesson 7 trajectory contract|Distinguish missing required input from not applicable|
|12–14|Capstone: inputs/calculation; completion; reconstruction/audit|Complete all seven mapped operations and repair using rubric|

At the lesson 2 boundary check hours→degrees→components, transpose inversion and normalization. At lesson 4 check origin/axes/time/unit compatibility and recover every signed term in a cancellation. At lesson 7 check all seven capstone prerequisites against the course map. If an operation fails, revisit its earliest introduction and repeat its practice, not merely the final sum. A recovery period is appropriate for Lesson 4's derivative bridge; do not omit it or assume calculus.

Use a circle sketch and three colored arrows for x,y,z. A physical book can illustrate rotating all attached arrows together while a room arrow remains fixed. These demonstrations introduce no measurements of celestial motion. A calculator should use degrees in Lesson 2's sky conversion and radians for Lesson 4's derivative formulas. Exact radicals and π are acceptable; decimal rounding should retain an exact expression or a rounding residual.

Mark source claims by their actual class. The course reads T45/T50's finite formal-result report without compiling its Agda modules. Do not describe the course's arithmetic checks as a new observational experiment. Keep the physical vector's unknown epoch explicit. The 97 replay states and 180000 reported samples are different populations. The Cell3 basis is not the toy triad; no new Cell3 numerical parameters are authorized here.

Full diagnostic answers follow each lesson; full capstone answers and a 28-point rubric are in capstone.md. Ask students to attempt first, then compare line by line. Award method credit separately from arithmetic, and require repair of a source-type error even when the numerical sum is right. No significance threshold or outlier deletion is part of this course.
''')
w('capstone.md','''# Capstone — A trajectory another reader can reproduce

Use three 55-minute periods: build the typed input ledger and first calculation; complete the remaining operations; reverse the calculations and audit scope. All numerical exercises are synthetic unless explicitly called source-reported. This is one portfolio of linked calculations, not one astronomical dataset: keep its km, m and display chambers separately typed.

Supply every intermediate signed vector, units, frame, origin and epoch. Use t0=2026-11-05T00:00:00Z with elapsed seconds and no leap crossing. Frame F is fixed orthonormal right-handed with fixed origin O. Source cards in lessons 3, 5 and 6 are supplied reading, not quantities to remeasure.

## Tasks

1. **C24-CAP-01.** In F take p0=(1,2,3)km, v=(2,-1,0)km/s and Δt=2s. Find p1,p2, label their epochs and reverse to p0. Explain the synthetic scope. Prerequisite: C24.01-E1/W1/P1/D1.
2. **C24-CAP-02.** Convert r=3L, α=0°, δ=0° to components. Separately use E=(0,1,0), N=(0,0,1), U=(1,0,0) to map local (0,1,1); normalize it and give its sky angles. Explain how to reconstruct the unnormalized vector. Prerequisite: C24.02-E1/W1/P1/D1.
3. **C24-CAP-03.** Use chain terms (10,0,0),(0,2,0),(-1,0,0),(0,0,1)m/s in Sun/CMB, EMB/Sun, Earth/EMB, lab/Earth order, with x0=(1,2,3)m. Find all two-second displacements and endpoint. Reverse only Earth/EMB to +1 in x and compare endpoints. Explain why the physical Earth/CMB authority is not an extra term. Prerequisite: C24.03-E1/W1/P1/D1.
4. **C24-CAP-04.** Use the separate Lesson 4 rotating example: o=(t,0,0)m in its stated units, θ=(1rad/s)t, fixed local point (1,0,0)m. Find each velocity contribution at t=π/2s and acceleration at t=0. For the separate synthetic comparison (1.2,0.9,0)m/s against model (1,1,0)m/s, preserve and reconstruct the residual. Prerequisite: C24.04-E1/W1/P1/D1.
5. **C24-CAP-05.** Apply a 180° z rotation to carried e_x and offset (1,1,0). Keep comparison e_x fixed. Give directed and axis angles; state what the absolute-value reduction removes. Distinguish 97 replay states from the source's 180000-sample metadata. Prerequisite: C24.05-E1/W1/P1/D1.
6. **C24-CAP-06.** Chamber A uses 1000km/cm and B uses 1km/cm. Interpret 2cm in each. Explain the Galactic-center gauge. Classify the finite a,b,c,(111) nonalignment report, nearest c at 31.6153896617°, and the 11.165830°/3.749971° internal model comparisons. Prerequisite: C24.06-E1/W1/P1/D1.
7. **C24-CAP-07.** Write the complete trajectory contract for the original meter-based chain in task 3, including its inverse. Add a separate real-source card containing the Lesson 3 physical vector, units, ICRS label, path/hash/pointer and unresolved epoch. Identify which site, time-conversion, ephemeris, EOP and geometry fields are unnecessary for the synthetic case but must be resolved for a new real propagation. Prerequisite: C24.07-E1/W1/P1/D1.

## Full worked answers

1. Each update adds (4,-2,0)km. p1=(5,0,3)km at t0+2s; p2=(9,-2,3)km at t0+4s. p2-(8,-4,0)=(1,2,3)km. Retain p0,v,Δt and F/O; these are stipulated values, not an ephemeris.
2. cos0=1, sin0=0 gives (3,0,0)L. The local vector is N+U=(1,0,1), norm √2, unit direction (1,0,1)/√2. α=0°, δ=45°. Multiply the unit direction by √2 to recover the vector; a real terrestrial triad requires site/time orientation.
3. Displacements are (20,0,0),(0,4,0),(-2,0,0),(0,0,2)m. Sum (18,4,2)m and endpoint (19,6,5)m. After reversal the third displacement is (+2,0,0)m, total velocity (11,2,1)m/s and endpoint (23,6,5)m. Difference (4,0,0)m. Save both lists. Already composed Earth/CMB includes upstream motion; adding it would double count. Its source speed 369812.50200040644m/s is not the toy speed.
4. ȯ=(1,0,0), Ṙp=(-1,0,0), Rv_local=(0,0,0)m/s, so total velocity is zero. At t=0, ö=0, R̈p=(-1,0,0)m/s² and both local-motion terms vanish; total acceleration is (-1,0,0)m/s². Residual is (0.2,-0.1,0)m/s; (1,1,0)+(0.2,-0.1,0)=(1.2,0.9,0)m/s. Preserve cancellation terms and residual; neither implies no motion throughout the interval.
5. Carried e_x→(-1,0,0), node→(-1,-1,0); comparison remains (1,0,0). Unit dot=-1 yields 180° directed, arccos(1)=0° axis angle. Absolute value discards polarity, so save original vectors. The 97 states are finite replay, whereas 180000 samples, 2000 rotations and ten channels are source-reported acquisition metadata.
6. A: 2×1000=2000km; B: 2×1=2km. Inter-chamber separation is not a physical distance. Fixing a Galactic-center sightline chooses a visual reference, not absolute rest or a time law. Nonalignment applies only to the displayed four candidates; nearest c has the reported 31.6153896617° angle. The other angles compare model directions internally, not exact Sgr A* alignment. None is a fresh course measurement or universal axis theorem.
7. Use the full field table in C24.07-W1, with epoch/time interval, fixed F/O, meters and m/s, all four constant terms, x0 and x(t)=x0+t(9,2,1). No measured residual is supplied; this is not an assertion of zero physical residual. At t=2 subtract the four task-3 displacements to recover (1,2,3)m. Site, ephemeris, EOP and real time conversion are explicitly not applicable to this synthetic construction; geometry is the stated identity-oriented F axes. The real-source card is the physical vector (-359003.19906581304,76679.88603400199,-44701.060100687995)m/s, ICRS, at the exact physical-authority path/hash in sources.md and pointer /derived_results/earth_cmb/V_E_icrs_m_s. Its epoch remains not specified. Real propagation awaits the full epoch, site, orientation, ephemeris and geometry contract; publication time and the distinct experiment-local 361.838…km/s label cannot fill these gaps.

## Rubric — 28 points

Each task has four separately earned points: (1) correct typed inputs/domain and units; (2) correct operation/calculation; (3) reconstruction or source classification; (4) retained information and scope boundary. For task 1 the last point requires all epochs and synthetic label; task 2 magnitude preservation; task 3 both term ledgers and no double counting; task 4 cancellation terms plus signed residual; task 5 polarity plus replay/metadata separation; task 6 finite/model/display boundaries; task 7 all applicability/missing-input fields. A numerically right answer with the wrong evidence class does not earn the classification or boundary points. Repair every missing operation after scoring; a total score does not replace the seven capability checks.
''')
# Compact provenance, never a raw source copy.
lines=['# Source ledger','', 'Exact application byte ranges were read through krytronx_get in this task. Returned whole-range hashes equaled the pinned object digests. Evidence class here is source-reported text; no Agda compilation was executed.','', '|ID|Logical path|SHA-256|Pointer/range and use|','|---|---|---|---|']
for s in C['sources']:
    if 'logical_path' in s:
        f=s['logical_path']; key={'40':'T40','50':'T50','45':'T45','10':'T10'}[f.split('/')[-1][:2]]; size={'T40':426,'T50':1761,'T45':2651,'T10':545}[key]
        lines.append(f'|{key}|{f}|{s["sha256"]}|bytes [0,{size}); full short source; lessons 3–7|')
    else:
        actual=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest(); assert actual==s['sha256']
        lines.append(f'|{s["id"]}|{s["path"]}|{actual}|Hash verified; background archival branch, no mathematical-backbone theorem used in this course|')
lines += ['', 'Physical authority: `Z:/Archive_20260911/Pre_Aug14/K-Field_linear_inertia_derivation_1784989727.json`; SHA-256 `4651a532fe43e8091748ef4f7e28bb899e1a2ea798d689ba1724e99530cd55ab`. Read `/derived_results/earth_cmb/V_E_icrs_m_s` and `/derived_results/earth_cmb/speed_m_s` directly and verified whole-file hash. ICRS, m/s; vector epoch not explicitly attached in the inspected authority. The G_phase_V_E_m_s field is a different object denied as physical velocity by T40.', '', 'T45 paragraphs on typed path and scale chambers ground lessons 3/6; its replay paragraph grounds lesson 5; its finite-refutation and orientation paragraphs ground lesson 6. T50 numbered items 1–2 corroborate finite-candidate and replay/acquisition scope. T40 grounds the physical/transformed exclusion; T10 grounds the admitted speed. Source contracts/Agda modules named inside these texts were not independently compiled; their proof status stays source-reported. The course assigns no exact numerical replay of those contracts.', '', 'Requested frozen generation/manifest: sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7. The capabilities call returned a read-only operation registry but no corpus generation/manifest pair. Therefore freshness beyond the exact retrieved object hashes is not certified here. This does not alter the pinned byte identity.', '', 'The 361.838…km/s experiment-local label is preserved only as a separately typed blueprint boundary, not used as numerical evidence. Its full trajectory contract is not loaded. Actual vector epoch, new real propagation inputs, fresh formal compilation and source-independent physical alignment measurement remain explicit gaps. All classroom numbers are authored synthetic inputs or arithmetic derived from them; no raw datasets were copied.']
w('sources.md','\n'.join(lines))
print('Support artifacts and capstone written')
