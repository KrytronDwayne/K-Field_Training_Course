from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
p=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(n,s): (R/n).write_text(s.strip()+'\n',encoding='utf-8')
def dump(n,o): write(n,json.dumps(o,indent=2,ensure_ascii=False))
rows=[]
for i,l in enumerate(p['course_map'],1):
    c=f'C22.{i:02}'
    rows.append(f'|{c}|[{l["title"]}](lesson-{i:02}.md)|{c}-E1|{c}-W1|{c}-P1|{c}-D1|C22-CAP-{i:02}|'+(f'lesson-{i+1:02}' if i<7 else 'capstone')+'|')
write('course-map.md','''# Inverse Limits, Continuum Rendering, and Detail — course map

Audience: high-school seniors able to calculate with signed numbers, fractions, powers, linear equations and coordinate lists. Series prerequisites are courses 06, 07 and 18; their needed address and linear-operation capabilities are explicitly rebuilt here. No calculus, abstract algebra or university linear algebra is assumed.

Outcome: construct compatible ternary prefixes, distinguish address and real closeness, render finite approximations with a certified tail, preserve finer information, and specify infinite-operator obligations.

The dependency chain is lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → capstone. Unit A (01–03) constructs addresses, Unit B (04–05) renders and observes, Unit C (06–07) retains detail and bounds operator claims. M18 requires mathematical-backbone M03 and M04; the local bridges teach the relevant residue and finite-calculus capabilities. Compiler module names are a separate namespace.

|Concept|Introduction|Explanation|Worked example|Answered practice|Diagnostics|Capstone|Later use|
|---|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'''

Every listed ID appears as actual lesson content. Each practice has a separate worked answer. Capstone inputs and outputs are explicit in capstone.md; its seven tasks use these same operations without new theory. Lesson 04 retains aliases C22-TAIL-EX1, C22-TAIL-P1, C22-TAIL-D1 for amendment EA-22-E09-6.

Pacing follows the approved expanded blueprint: 1,1,2,3,1,2,2 periods for lessons 01–07, respectively, totaling 12 × 55 = 660 minutes. Three capstone periods add 165 minutes, for 825 minutes overall. Multiple periods within a lesson retain its checkpoint ID so its proofs and practice stay together. No coverage is removed. Each period allocates 5 minutes retrieval, 20 teaching/worked example, 15 practice, and 15 independent checks/repair. Advance after the relevant practice and diagnostics can be explained; extra reteaching time is recorded by the teacher rather than silently dropping later tasks.

Source boundaries: all concrete numbers are explicitly synthetic mathematics, except the quoted source definitions and their provenance. Source-reported statements, independently derived finite consequences and unprovided operator details remain separate. No empirical observation or mechanism is invented. Details and unresolved tails are primary retained information.
''')
write('terminology.md',r'''
# Terminology and notation

|Term or symbol|Meaning and local convention|Introduced|
|---|---|---|
|Z; Z/3^d Z|Integers; their residues modulo 3^d|01|
|d, N, j|Positive depth, truncation depth, digit index; dimensionless|01,04|
|u_j|Balanced digit −1,0,1, or ordered triple of these; least significant first in addresses|01|
|t_d, a_d|Signed weighted digit sum; its nonnegative residue|01|
|A_d|Three-coordinate address set (Z/3^d Z)^3, with 27^d elements|01,03|
|π_d|Coordinatewise reduction from depth d+1 to d|01|
|Compatibility|Every deeper residue reduces to its stored shallower residue|01|
|δ, k|Address distance 3^(−k) for exactly k shared low-order digits; zero for identical complete histories|02|
|A∞, Z₃³|Set of complete compatible triple histories; not a finite residue set|03|
|Inverse limit|Whole compatible ladder under reduction maps|03|
|r, S_N|In the geometric-sum derivation only: scalar ratio and finite sum r+…+r^N|04|
|Σ|Sum over the stated index range; infinite sum is a limit of partial sums|04|
|z_N, z|Dimensionless normalized rendered partial vector and its real limit|04|
|B, r_N, r|Declared length-valued matrix; rendered displacement Bz_N and limit Bz. This r is not the geometric ratio|04|
|LU|Synthetic length unit, not a measured Cell3 calibration|04|
|O_K, x|Declared physical origin and absolute position; x−O_K is displacement|04|
|Infinity norm|Largest absolute coordinate; matrix version is largest absolute row sum|04|
|Absolute tail bound|Upper bound on remaining absolute contribution, retained with exact rule or unresolved continuation|04|
|Ordered pair|History and image retained together; equal images need not mean equal histories|04|
|f_d, g₂, composition ∘|Finite-prefix functions; composition means apply the right function first|05|
|Cylinder, pullback|Histories sharing a finite prefix; observation evaluated after reduction|05|
|P₀, P₁|Four-cell global and adjacent-pair averaging, equal weights|06|
|Q₀, Q₁|P₁−P₀ and I−P₁, retained between-pair and within-pair detail|06|
|I; transpose; projector|Identity map; row/column swap; operation P satisfying P²=P|06|
|Dot product, orthogonal|Sum of coordinate products; dot product zero|06|
|Filtration|Sequence of nested coarse spaces; infinite reconstruction requires a convergence contract|06|
|E, Q|A specified block averaging and I−E; product rules require explicit extra properties|06|
|Δf|f_t−f_s, signed finite difference across two labeled endpoints|06|
|ℓ², sequence 2-norm|Real square-summable sequence space; square root of sum of squared entries|07|
|Carrier, domain, action|Ambient objects; allowed inputs for one operator; its transformation rule|07|
|D, Dom(D)|Action (Dx)_n=nx_n; domain where Σn²x_n² is finite|07|
|Convergence mode|Criterion specifying what it means to approach a limit, e.g. ℓ² norm|07|
|Unbounded|No one finite constant bounds output norm by constant × input norm on the domain|07|
|Self-adjointness|Advanced operator property involving the adjoint and its domain; recognition only|07|

Reserved wider-series notation: M_cell=BᵀB and R_cell=M_cell^−1 are the Cell3 Gram metric and its inverse, whereas G_phase is a separate phase metric. None is required in core computations here. B in the illustrative diagonal example is explicitly synthetic, not the mature ordered ICRS Cell3 basis. The latter has intentional negative determinant and half-open cells [−1/2,1/2)^3; neither its numerical constants nor ownership rule is substituted by our examples. Address reduction is not nearest-integer rounding. No half-tie convention is needed for a residue operation.

Source vocabulary and status: “reported” identifies an archival assertion; “derived” identifies the course's explicit mathematical consequence; “synthetic” identifies authored inputs; “not supplied” identifies a missing contract or body, not a refutation. Compiler M03/M07/M08 authority is not automatically mathematical-backbone authority. No parity, chirality, metric, physical velocity or energy branch is merged here.
''')
write('teacher-guide.md',r'''
# Teacher guide

This short course supports an independent 15-period sequence including capstone. Supply paper for two simultaneous ledgers: the signed digits/detail components and the visible coarse or rendered result. Calculators are optional; fractions are preferred so endpoint equality and tail thresholds can be checked exactly. This is a mathematical source-reading course; it does not ask students to manufacture experimental evidence.

Before lesson 01 ask learners to compute −6 mod27 by adding 27, 3⁴, and (2+6)/2. Answers are 21,81,4. A learner who cannot explain these should receive an arithmetic bridge before advancing. The lesson explicitly teaches residues, so the first question is a readiness conversation rather than a presumed prerequisite test.

|Lesson and periods|Teaching focus|What to inspect before advancing|Repair when needed|
|---|---|---|---|
|01: 1|Signed prefixes and reduction|All four practice reductions plus failed proposal retained|Compute signed sums before residues; label each modulus|
|02: 1|Two meanings of distance|Learner names which distance is being used|Repeated division by3; compare with number-line subtraction|
|03: 2|Complete rule, then triples|General compatibility argument and 27 extensions|Separate finite table from “for every j” rule|
|04: 3|Finite subtraction proof; matrix bound; endpoint histories|Minimal tolerance depth, units, distinct histories|List consecutive powers; use a row sum by hand; retain signed tail|
|05: 1|Cylinder and pullback|Same output does not collapse input ledger|Use 7,16,25 as a counterexample table|
|06: 2|Means, matrices; projector/reconstruction checks|All three disjoint sectors saved; P₀P₁=P₀|Reconstruct entrywise before discussing infinite notation|
|07: 2|Block convergence; domains and source cards|Distinguishes x∈ℓ² from x∈Dom(D)|Compare input-square and weighted-square columns|
|Capstone: 3|Input/source ledger; calculation; independent repair|All seven operation IDs and retained information|Return to the mapped practice, not new untaught methods|

Use the 5/20/15/15-minute structure in each core period. Across 12 periods this is retrieval 60, teaching 240, practice 180, checks/repair 180 minutes. Diagnostic answers appear in each lesson so teachers can cover them during independent work, then uncover them for repair. A correct number without its depth, units or rule is incomplete when those labels change its meaning.

Unit A cumulative check: ask for the four levels of the all-negative rule and the distinction between depth 4 and an infinite sequence. Unit B: ask why the two endpoint histories share an image but are address-distance 1, and why the physical depth differs from the normalized depth for the synthetic B. Unit C: reconstruct the four-entry vector, then explain why this finite identity does not settle a missing infinite operator domain. These checks consume already scheduled diagnostic time.

Keep lesson 06's names precise: P₀,P₁ are nested averages, whereas P₀,Q₀,Q₁ are the three disjoint sectors. Their mixed-product claims differ. The optional product source bridge derives every term using explicit block-averaging properties; no product rule is inferred from Q=I−E alone. It is a recognition and finite-verification bridge, not an assessment of an unloaded infinite algebra.

Lesson 07 permits an elementary proof of convergence through block bounds. Do not require the exact value of Σ1/n², calculus, complex inner products or an adjoint calculation. Self-adjointness is a source-scope word only. No student must supply a missing archival operator: “not supplied” with an exact checklist is the correct report.

Capstone periods: first 55 minutes establish input ledger/source card and complete tasks 01–03; second 55 minutes handle rendering, observations and details (04–06); third 55 minutes finish domain/source classification (07), independently recompute and repair. The 28-point rubric in capstone.md gives four points per operation. A corrected record keeps the original proposal and labels the correction rather than overwriting evidence.

Accessibility: allow spoken explanations alongside exact arithmetic, use a color per coordinate while retaining written coordinate labels, and provide large tables for digits/moduli. More time is preferable to dropping a detail sector. Extension learners may prove a matrix identity by multiplication; every core result is already accessible through averaging rules.

Recovery for authors: manifest.json is the checkpoint authority; verify each file hash before trusting passed status. The deterministic validator checks integrity and assembly, while audit_report.json and independent-audit.json record content checks. Rebuild only defects and their dependents. Re-run verify_examples.py after mathematical edits, update assembly/hashes using finalize_course.py, and run the project validator command recorded in completion_report.json.
''')
tasks=[
('From balanced digits (0,1,−1,0,1), produce signed sums and residues at moduli 3,9,27,81,243; test all reductions. Also test the proposal (1,8) at moduli3,9. Embed the valid history as triples with two zero coordinates. State the continuation status.',
 'Signed sums 0,3,−6,−6,75; residues 0,3,21,75,75. The reductions are 0,3,21,75 respectively. The triple rows are (0,0,0),(3,0,0),(21,0,0),(75,0,0),(75,0,0). The proposal fails: 8 mod3=2≠1; keep its input and failed equation. No continuation was specified.'),
('Find real and address distances between 4 and13. Find triple address distance between (1,4,0) and (28,13,0). Name what each distance measures.',
 'Difference 9=3² gives real distance9 and address distance1/9. Triple coordinate address distances are 1/27,1/9,0, maximum1/9. Real distance uses number-line separation; address distance uses shared low-order residues. All are dimensionless in this exercise.'),
('Specify an exact infinite triple by using all −1 digits in its first coordinate and all0 digits in the other two. Produce its first four levels, verify compatibility generally, and count next triples for a prefix with no fixed continuation.',
 'First signed coordinates −1,−4,−13,−40 give residue triples (2,0,0),(5,0,0),(14,0,0),(41,0,0). At general depth t_d=−(3^d−1)/2; t_(d+1)−t_d=−3^d, so every reduction holds. A prefix without the prescribed continuation has 3³=27 next triples. The all-negative rule selects one of them at each level.'),
('For the exact triple rule in task03, compute z₂ and r₂ using B=diag(2,3,4) LU. Give its signed limiting remainder and certify a uniform physical tail≤1/1000 LU by the smallest guaranteed depth. Separately choose depth for Σ2^(−j) tail≤1/32. Compare full normalized images of h=(1,−1,−1,…) and k=(0,1,1,…) in the first coordinate, zeros elsewhere; preserve both histories.',
 'z₂=(−2/9,0,0), r₂=(−4/9,0,0) LU. The all-negative limit is z=(−1/4,0,0), r=(−1/2,0,0) LU; signed remaining displacement is (−1/18,0,0) LU. The general norm bound is ||B||∞/(4·3^N)=1/3^N LU, so N=7 since 1/729>1/1000≥1/2187. Binary tail≤1/32 first at N=5. The endpoint sum from j=2 onward is1/6, giving z(h)=z(k)=(1/12,0,0). They differ at their first residue and remain different histories paired with the same image. Store exact rule, depth, partial values, bounds and signed known remainder.'),
('Evaluate g₂(a)=a mod9 for depth3 addresses 7,16,25. Supply their balanced third digits and explain what remains invisible. Apply this first-coordinate observation to (a,0,0) while retaining every coordinate.',
 'Outputs 7,7,7. Full three-digit prefixes are (1,−1,1),(1,−1,−1),(1,−1,0); third digits1,−1,0. The observation reads depth2 and hides the third and later digits. Keep three separate input triples (7,0,0),(16,0,0),(25,0,0), outputs and unresolved continuations.'),
('For v=(2,0,6,4), compute P₀v,Q₀v,Q₁v, reconstruct P₁v then v, and state which infinite-reconstruction assumptions this calculation does not supply.',
 'P₀v=(3,3,3,3), Q₀v=(−2,−2,2,2), Q₁v=(1,−1,1,−1). The first two sum to(1,1,5,5)=P₁v; all three sum to v. Entries are dimensionless and signed. An infinite version still needs an ambient space, limiting subspace and convergence mode; retain every sector and any complementary component.'),
('For the explicitly defined D on real ℓ², test y_n=1/n² and compute Dy. Use the Lesson07 source card to report what is and is not supplied for a proposed archival operator H. Classify the source renderer, the synthetic D calculation, and any proposed physical mechanism separately.',
 'The input-square sum Σ1/n⁴≤Σ1/n²<∞. The weighted sum Σn²/n⁴=Σ1/n²<∞ by the taught dyadic-block bound, so y∈Dom(D), Dy=(1/n)∈ℓ². The M18 card supplies an address object and renderer; it does not supply a particular H carrier/domain/action/inner product/convergence mode. Mark these not supplied for H. Renderer definitions are source facts, its bound is derived mathematics, D is a synthetic mathematical example, and no empirical or physical mechanism is established or required by these calculations.')]
cap=['# Capstone — A history-preserving continuum report','''Deliver a single report containing the seven numbered tasks below, your input ledger, calculations, source card and retained-information ledger. Use fractions and distinguish dimensionless coordinates from LU displacements. The mathematical examples are synthetic; source definitions are identified in sources.md. You may consult lessons and glossary. Three 55-minute sessions are allocated in the teacher guide. No external data or software is required.

Each task has four points: one for declared inputs and scope; one for correct operation; one for reconstruction or source classification; one for retained information and boundaries. The task-specific key below explains what earns each point. Total:28 points. An arithmetic correction must leave a labeled record of the original input or failed proposal.''']
for i,(task,ans) in enumerate(tasks,1):
 c=f'C22.{i:02}'
 cap.append(f'## C22-CAP-{i:02}\n\n{task}\n\nPrerequisite trail: [lesson-{i:02}](lesson-{i:02}.md), {c}-E1 → {c}-W1 → answered {c}-P1; check {c}-D1. Output: the named calculations and retained-information statement for this operation.')
cap.append('## Full answer key and marking rubric\n\nUse after independent work. Award a point when its corresponding operation is correct or is corrected with a reproducible explanation; unsupported numerical answers do not earn the scope/retention points.')
criteria=[
 ['Declare digit order, moduli and dimensionless triples','Compute both signed sums and residues','Show all reductions and identify failed8 mod3','Keep failed proposal, zeros and unresolved continuation'],
 ['Name the two distance conventions','Compute9 and1/9','Compute triple maximum1/9','Retain identical third coordinate and distinguish shared prefix from real separation'],
 ['Specify full rules for all three coordinates','Produce four signed/residue levels','Give general difference −3^d and27 extension count','Distinguish selected exact rule from unresolved-prefix alternatives'],
 ['Declare synthetic B, LU, rule and tolerance','Compute partial image and choose depths7 and5','Derive endpoint equality and signed remainder','Retain both histories, depth ledger and uniform-bound scope'],
 ['Declare g₂ and depth3 input triples','Compute outputs7','Recover three distinct third digits','Retain all input rows and unresolved finer continuations'],
 ['Declare vector and finite equal-weight operations','Compute all three sectors','Reconstruct P₁v and v','Retain signed entries and name infinite-scope obligations'],
 ['Declare ℓ², D action and domain','Bound input and weighted square sums','Compute Dy and classify H missing contracts','Keep source/derived/synthetic/mechanism categories separate']]
for i,((task,ans),rub) in enumerate(zip(tasks,criteria),1):
 cap.append(f'### C22-CAP-{i:02} answer\n\n{ans}\n\n'+'\n'.join(f'- 1 point: {c}.' for c in rub))
cap.append('''## Backward audit and final report check

No new technique appears in this assessment. Task04 applies Lesson04's all-positive computation to an all-negative rule using signed arithmetic already practiced in Lesson03. The other calculations use the answered practice packets directly; integration and information accounting supply the synthesis. Before submission check the residue ladder, reproduce the geometric bound by subtraction, sum the three detail sectors entrywise and review H against all five contract fields. The source card's omissions stay omissions; filling them with the example D would change the subject.''')
write('capstone.md','\n\n'.join(cap))
source_rows=[]
for s in p['sources']:
 path=Path(s['path']); actual=hashlib.sha256(path.read_bytes()).hexdigest(); assert actual==s['sha256']
 source_rows.append({'id':s['id'],'path':str(path),'sha256':actual,'verified_match':True,'evidence_class':'archival source; reported status distinct from fresh course verification'})
dump('source-verification.json',{'sources':source_rows,'primary_pointer':'S02#/backbone_sequence/17','additional_pointers':['S02#/backbone_sequence/2/recursions/ternary_address','S02#/backbone_sequence/3','S03#/findings/5','S03#/findings/9'],'graph_generation':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','graph_manifest_sha256':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','retrieval':'Capabilities, sparse RAG without rerank, root traversal; exact definitions read from hash-matched local archival JSON. Graph search surfaced integration records, not used as proof authority.','limitations':['M18 provides no specific infinite history-operator domain/action; course uses an explicitly synthetic D.','No archival infinite-filtration ambient space/convergence proof is reconstructed by the finite four-cell example.']})
write('sources.md','''# Sources and evidence ledger

The five approved archival files were read in place and all SHA-256 values matched. No source snapshots were saved. JSON pointers below identify exact source-local passages; page numbers do not apply to these JSON documents. Sources S01,S04,S05 are integrity-verified context, not premises of the lesson calculations. S02 is the mature source and S03 supplies audit boundaries. Historical/corrected branches are not silently mixed.

'''+ '\n\n'.join(f'**{s["id"]}** — `{s["path"]}`\n\nSHA-256: `{s["sha256"]}`.' for s in source_rows)+'''

|Pointer|Content used|Evidence and teaching disposition|
|---|---|---|
|S02 /backbone_sequence/17/definitions|A_d, bonding maps, inverse limit, renderer|Source definitions; lessons01–05 derive explicit finite consequences|
|S02 /backbone_sequence/17/proof/0, /backbone_sequence/17/proof/1, /backbone_sequence/17/proof/2|Compatibility and absolute tail|Source mathematical claims; independently recomputed examples and geometric derivation|
|S02 /backbone_sequence/17/proof/3|Cylinder pullback|Explained and checked in lesson05|
|S02 /backbone_sequence/17/proof/4|Retained-detail filtration|Finite bridge only; ambient space/convergence needed for an infinite identity|
|S02 /backbone_sequence/17/result|Ordered pair of exact address history and real image|Preserved in every rendering report; no injectivity assumed|
|S02 /backbone_sequence/2/recursions/ternary_address|Coordinate reduction and27^d cardinality|Reconstructed locally; dyadic recursion stays separate|
|S02 /backbone_sequence/3/proof/0, /backbone_sequence/3/proof/1, /backbone_sequence/3/proof/2, /backbone_sequence/3/proof/3, /backbone_sequence/3/proof/4|Finite difference and detail product|Finite expansion retained; extra E properties explicitly supplied for our finite model|
|S03 /findings/5 (AUD-006)|Q=I−E alone is insufficient for product identity|Lesson06 states linearity, idempotence and block-constant property and derives every term|
|S03 /findings/9 (AUD-010)|Propagate constituent logical boundaries|Finite checks, source claims, infinite obligations and optional mechanisms remain separated|

The M18 requires array names mathematical-backbone M03 and M04. Relevant capabilities are rebuilt in the lessons. It does not require M19. The compiler integration surfaced by graph retrieval has its own module namespace and does not promote this course's source claims into compiler authority. Graph generation and manifest were both 5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7; sparse search ran with rerank=false. The capabilities response enumerated read-only routes without a corpus-generation field; the search response supplied the generation. Root traversal is discovery context only.

Evidence layers: these lessons contain source facts and derived mathematical implications. The digit sequences, diagonal B, four-cell vectors and D are authored synthetic examples. There are no empirical observations, statistical implications from measurements, or established physical mechanisms asserted by this course. Proposed mechanisms remain outside these mathematical results. A source-reported proof label is not substituted for a missing body.

Known scope gaps are intentionally assessed: M18 does not supply a particular infinite history-operator action/domain, and its brief filtration statement does not in this course specify an ambient function space or convergence mode. The course teaches the corresponding checklist rather than inventing them. These gaps do not block any finite core assessment.
''')
print('Course map, glossary, teacher guide, capstone and provenance saved.')
