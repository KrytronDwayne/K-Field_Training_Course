"""Build small synthetic registry and course supports; refresh only derived supports."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import itertools,json,hashlib,sys
R=Path(__file__).resolve().parent
c=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(n,t): (R/n).write_text(t.strip()+'\n',encoding='utf-8')
def dump(n,o): write(n,json.dumps(o,indent=2,ensure_ascii=False))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def triple(v): return '('+','.join(str(x) for x in v)+')'
O=(F(2),F(-1),F(4))
B=((1,1,0),(0,2,0),(0,0,-3))
rows=[]
for i,L in enumerate(itertools.product((-1,0,1),repeat=3),1):
    q=tuple(F(x,2) for x in L)
    p=tuple(O[j]+sum(B[j][k]*q[k] for k in range(3)) for j in range(3))
    d=tuple(p[j]-O[j] for j in range(3))
    recovered=(2*d[0]-d[1],d[1],-2*d[2]/3)
    residual=tuple(recovered[j]-L[j] for j in range(3))
    nz=next((x for x in L if x),None)
    s=None if nz is None else (1 if nz>0 else -1)
    v=(0,0,0) if s is None else tuple(s*x for x in L)
    z=tuple((x+F(1,2))//1 for x in q)
    u=tuple(q[j]-z[j] for j in range(3))
    lam=sum(L)
    assert recovered==L and residual==(0,0,0)
    assert tuple(z[j]+u[j] for j in range(3))==q
    assert all(-F(1,2)<=x<F(1,2) for x in u)
    assert d[0]-d[2]/3==F(lam,2)
    if s is not None: assert tuple(s*x for x in v)==L
    rows.append(dict(id=f'N{i:02}',L=L,q=q,p=p,lambda_=lam,chi=1 if lam%2==0 else -1,r3=lam%3,v=v,s=s,z=z,u=u,R_L=residual))
assert len({r['L'] for r in rows})==27
sheet=Counter(r['lambda_'] for r in rows)
assert [sheet[k] for k in range(-3,4)]==[1,3,6,7,6,3,1]
assert Counter(r['chi'] for r in rows)=={1:13,-1:14}
assert Counter(r['r3'] for r in rows)=={0:9,1:9,2:9}
pairs={r['v'] for r in rows if r['s'] is not None}
assert len(pairs)==13
for v in pairs:
    members=[r for r in rows if r['v']==v]
    assert len(members)==2 and {r['s'] for r in members}=={-1,1}
    assert tuple(sum(r['p'][j] for r in members) for j in range(3))==tuple(2*x for x in O)

table=['# Complete worked registry','',
'Classroom analogue only; not Cell3 and not measured data. O=(2,−1,4) U; B rows (1,1,0),(0,2,0),(0,0,−3), with columns a,b,c. Every position has unit U; other columns are dimensionless. Fractions are exact. Row order is L₁, then L₂, then L₃, each increasing −1,0,1.','',
'The first table retains every node and its typed labels. The second retains the cell-owner decomposition and inverse closure residual for the same row IDs. A dash in s means not applicable at the center; it does not mean zero or an unknown direction.','',
'|ID|L|q|p / U|λ|χ|r₃|v|s|','|---|---|---|---|---|---|---|---|---|']
for r in rows: table.append('|'+ '|'.join([r['id'],triple(r['L']),triple(r['q']),triple(r['p']),str(r['lambda_']),str(r['chi']),str(r['r3']),triple(r['v']),str(r['s']) if r['s'] is not None else '—'])+'|')
table+=['','|ID|z|u=q−z|R_L=L_recovered−L|','|---|---|---|---|']
for r in rows: table.append('|'+ '|'.join([r['id'],triple(r['z']),triple(r['u']),triple(r['R_L'])])+'|')
table+=['','Checks: 27 distinct addresses; geometric counts center 1, faces 6, edges 12, vertices 8; sheet counts 1,3,6,7,6,3,1; χ=+1 count 13 and χ=−1 count 14; r₃ counts 9,9,9. There are 13 noncentral pairs and a separate center. All 27 inverse residual triples are zero; all 27 ownership reconstructions and affine sheet identities hold exactly. Every noncentral pair sums to 2O. See verification.json and verify_examples.py for a second enumeration and arithmetic route.']
write('registry.md','\n'.join(table))
dump('registry.json',{'scope':'synthetic classroom analogue; exact rational entries represented as strings','units':'p and O in U; B in U; other fields dimensionless','origin':[str(x) for x in O],'basis_rows':B,'rows':[{k:([str(x) for x in v] if isinstance(v,tuple) else v) for k,v in r.items()} for r in rows]})

write('capstone.md','''# Capstone — Build a reversible 27-node registry

Work in two 55-minute periods. Use Lessons 1–6 and a blank table before opening the full answer registry. You may use a calculator or a small script, but explain the counting and reconstruction checks in words. No coding skill is required. All constants below describe the classroom analogue, not Cell3 or observations.

**Inputs:** L entries −1,0,1; O=(2,−1,4) U; basis columns a=(1,0,0), b=(1,2,0), c=(0,0,−3) U. Use the half-basis map and the half-open owner convention from Lesson 2. Keep the centered-window boundaries. Use g_λ=(1,0,−1/3)/U. The output is all 27 rows plus a check ledger and a brief information-preservation explanation.

## Tasks and prior preparation

|Step|Concrete input → output|Earlier explanation and answered practice|
|---|---|---|
|C05-CAP-01|Three coordinate menus → 27 distinct L and center/face/edge/vertex tally|C05.01-E1, W1 and P1 in Lesson 1|
|C05-CAP-02|L,O,B → q,p,z,u in every row; one boundary explanation|C05.02-E1/E2, W1 and P1 in Lesson 2|
|C05-CAP-03|Each L and p → λ, seven counts and one written affine identity check|C05.03-E1/E2, W1 and P1 in Lesson 3|
|C05-CAP-04|Each λ → χ; explain unchanged χ under negation|C05.04-E1, W1 and P1 in Lesson 4|
|C05-CAP-05|Each nonzero L → v,s; center singleton; reconstruct L and both pair points|C05.05-E1, W1, P1 and P2 in Lesson 5|
|C05-CAP-06|Completed rows → inverse residual triples, uniqueness and pair checks, retained correction ledger|C05.06-E1/E2, W1, P1 and P2 in Lesson 6|
|C05-CAP-07|Each λ → r₃; three counts and comparison with χ counts|C05.04-E2, W2 and P2 in Lesson 4|

For step 6, retain every original row. If you find an error, add a note recording the old field, corrected field, reason and closure residual before and after. If no error occurs, explicitly report no corrections and still provide the per-row zero residuals. Explain which information survives a pair-only quotient and which extra field makes it invertible. Do not replace the complete registry by totals.

## Full answer key

The two tables in [registry.md](registry.md) are the full row-by-row answer, including every q,p,λ,χ,r₃,v,s,z,u and inverse residual. [registry.json](registry.json) is the same small synthetic record in machine-readable form. Compare by L, not merely row order. Equivalent exact fractions and a different declared enumeration order are acceptable.

**C05-CAP-01:** Three independent choices give 3³=27 unique rows. Zero, one, two and three nonzero entries give 1,6,12,8 rows respectively: center, face centers, edge centers, vertices. The sum is 27. A row count alone would miss a duplicate-and-omission error.

**C05-CAP-02:** For every row use q=L/2 and p=(2+(L₁+L₂)/2,−1+L₂,4−3L₃/2) U. Set each owner component to 1 only when the corresponding L entry is +1; otherwise set it to 0. Then u=q−z. At L=(1,0,0), p=(5/2,−1,4) U, z=(1,0,0), u=(−1/2,0,0). This node is on the centered window's boundary, yet belongs to the positive neighbor's half-open cell. Keeping z and u reconstructs q.

**C05-CAP-03:** λ=−3,−2,−1,0,1,2,3 has populations 1,3,6,7,6,3,1. At L=(1,−1,1), p−O=(0,−1,−3/2) U. Dotting with g_λ gives 1/2, equal to λ/2. Generally the dot product equals (L₁+L₂)/2+L₃/2. Omitting O changes it by 2/3 in this analogue.

**C05-CAP-04:** χ is +1 on −2,0,2 and −1 on −3,−1,1,3. Counts are 13 and 14. The negative of an even integer remains even and the negative of an odd integer remains odd, so χ is unchanged for opposite nodes. It cannot substitute for orientation s.

**C05-CAP-05:** The 13 representatives are listed in Lesson 5 P2 and appear in the registry, each twice. Each noncentral member is L=s v. For example v=(0,1,1) gives p(+v)=(5/2,0,5/2) U and p(−v)=(3/2,−2,11/2) U. Their sum equals 2O. Center L=0 has p=O, v=0, s=N/A and occurs once. Including the singleton gives 14 classes. A pair-only view retains the representative, the unoriented pair and antipodally even quantities, including χ and λ². It loses which member was selected and generally the signed λ, the member's r₃, position and displacement. Adding s to v restores the member; retaining O and B restores position. At λ=0 or r₃=0 some labels coincide, but member direction still needs s.

**C05-CAP-06:** For each stored p, subtract O, then compute L_recovered=(2dₓ−dᵧ,dᵧ,−2d_z/3). Every R_L=L_recovered−L is (0,0,0) in the answer table. Verify q=z+u for all rows and −1/2≤u_i<1/2, check that each pair has signs −1 and +1, and check pair position sums 2O. An erroneous stored p_z=3 in the row L=(1,−1,1) would give R_L=(0,0,−1/3); the correction note would retain that discrepancy and set p_z to 5/2 with a subsequent zero residual. The supplied answer registry needed no row corrections. This deliberate error is a teaching example, not an observed acquisition fault.

**C05-CAP-07:** r₃=0 groups sheets −3,0,3 (1+7+1=9); r₃=1 groups −2,1 (3+6=9); r₃=2 groups −1,2 (6+3=9). The seven-sheet, two-polarity and three-remainder partitions each account for the same 27 rows, with different information retained. None replaces the address.

## Rubric — 100 points

|Step|Points|Full-credit evidence and partial-credit rule|
|---|---|---|
|01|15|10 for all 27 distinct triples (deduct 1 per missing/duplicate intended row to zero); 5 for justified 1/6/12/8 tally|
|02|20|12 for complete correct q,p (deduct 1 per erroneous row to zero); 4 for z,u; 4 for boundary explanation with origin and units|
|03|15|5 for row λ values; 5 for complete seven counts; 5 for a correct affine identity with O subtraction|
|04|10|5 for row χ and counts; 5 for the antipodal parity explanation|
|05|15|8 for v,s and separate center; 4 for reconstruction and pair midpoint; 3 for the information-loss explanation|
|06|15|5 for complete retained rows/uniqueness check; 5 for per-row inverse/ownership checks; 5 for pair check and explicit discrepancy/correction accounting|
|07|10|5 for r₃ per row; 5 for 9/9/9 reconciliation and distinction from parity|

For any non-row subcriterion award half its points when the method is correct but a local arithmetic error remains, and zero when absent or conceptually incorrect. Do not deduct twice for a propagated arithmetic error: mark later method work on its own merits. Give repair feedback for missing origin, omitted orientation, or dropped rows regardless of score; successful mastery requires those conceptual errors to be corrected.

**Source and evidence scope:** Node and sheet definitions come from S02 M03, with the affine correction SA-05. Cell ownership comes from S02 M02. All numerical positions here use the supplied synthetic analogue. Counting and rational identities are derivations, not empirical measurements. There are no new physical mechanisms or statistical conclusions in this task. Every owned-cell residual and inverse closure residual is retained separately.
''')

write('terminology.md','''# Terminology and notation

|Term or symbol|Meaning, type and units|Introduced|
|---|---|---|
|L=(L₁,L₂,L₃)|Dimensionless signed address, entries −1,0,1; subscript indicates entry|Lesson 1|
|Cartesian product|All ordered combinations from coordinate menus|Lesson 1|
|Window|27 half-step nodes; distinct from 27 complete cell volumes|Lessons 1–2|
|Vertex / edge center / face center / center|Three / two / one / zero nonzero entries in L|Lesson 1|
|Vector|Ordered components describing displacement; entrywise addition and scaling|Lesson 2|
|B=[a b c]|Ordered basis columns, units of length; classroom rows are printed explicitly|Lesson 2|
|O_K; classroom O|Declared origin position; O abbreviates O_K only in the analogue|Lesson 2|
|q=L/2|Dimensionless half-address|Lesson 2|
|p|Position O+Bq, unit U in the analogue|Lesson 2|
|d=p−O|Displacement from origin, unit U|Lesson 2|
|U|Arbitrary classroom length unit; never nm or a Cell3 numerical constant|Lesson 2|
|z|Dimensionless integer cell-owner triple, floor(q+1/2)|Lesson 2|
|floor(t)|Greatest integer ≤t; evaluated entrywise for triples|Lesson 2|
|u=q−z|Dimensionless retained within-cell coordinate in [−1/2,1/2)³|Lesson 2|
|Half-open|Left boundary included, right boundary excluded|Lesson 2|
|λ|Integer sheet label L₁+L₂+L₃, from −3 through 3|Lesson 3|
|Permutation|Rearrangement; identical entries do not create different rows|Lesson 3|
|Dot product g·d|Sum of three corresponding component products|Lesson 3|
|g_λ|Reciprocal sheet vector whose dot product with each basis column is 1; unit inverse length|Lesson 3|
|B⁻ᵀ|Recognition notation for inverse-transpose; not a required computation|Lesson 3|
|χ|Node polarity (−1)^λ: +1 even, −1 odd; dimensionless|Lesson 4|
|r₃|λ mod 3: unique remainder 0,1,2 in λ=3k+r₃; dimensionless|Lesson 4|
|k|An integer used locally to express parity or division remainder; not a node address|Lesson 4|
|Antipodal|L and −L, with physical points reflected about O|Lesson 5|
|Equivalence class / quotient|Grouped members / collection of groups under a declared relation|Lesson 5|
|v|Canonical pair representative, first nonzero entry positive; center v=0|Lesson 5|
|s|Member orientation ±1 with L=s v for noncentral rows; N/A at center|Lesson 5|
|Even / odd function under negation|Value preserved / sign reversed by L→−L|Lesson 5|
|Singleton|One-member center class|Lesson 5|
|Registry|All typed per-node records plus checks; not just aggregates|Lesson 6|
|R_L|L_recovered−L, dimensionless inverse closure discrepancy; retained per row|Lesson 6|

Reserved source notation stays outside the core calculations: M_cell=BᵀB is the Cell3 Gram metric, R_cell its inverse; G_phase is a distinct phase metric. None is being replaced by the classroom B or by a reciprocal normal. Detector parity, A1 carry parity, chirality and family labels are not alternate names for χ. Source compiler M03 and mathematical backbone M03 are different naming systems. The present source references mean the mathematical backbone module.
''')

mapping=['# Course map — Lucas Geometry: 27 Nodes, Polarity, and Sheets','',
'Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, powers, linear equations, ordered coordinate triples, and Course 04 capabilities. The lessons locally reteach all operations actually required, including basis-column multiplication, inverse solving, dot products, remainders and pair reconstruction. No calculus, abstract algebra, complex phase calculation or coding is required.','',
'Six 55-minute lessons plus two 55-minute capstone periods. Units: I, enumeration and affine mapping (Lessons 1–2); II, sheets and classes (3–4); III, reversible pairing and registry (5–6). Cumulative checks occur at 2, 4 and 6. There is no boundary change from the approved map. Lesson 6 uses representative rows; full enumeration is carried out across capstone periods.','',
'|Concept|Explanation|Worked example|Answered practice|Diagnostic|Later use|','|---|---|---|---|---|---|']
for i in range(1,7):
    cid=f'C05.{i:02}'
    mapping.append(f'|{cid}|Lesson {i}: {cid}-E1'+('/E2' if i in (2,3,4,5,6) else '')+f'|{cid}-W1|{cid}-P1|{cid}-D1|'+(f'Lesson {i+1}' if i<6 else 'Capstone')+'|')
mapping+=['|C05.04 remainder bridge|Lesson 4: C05.04-E2|C05.04-W2|C05.04-P2|C05.04-D2|Lessons 5–6, C05-CAP-07|','',
'The full capstone backward map with named inputs and outputs is in capstone.md. Additional closure practice C05.05-P2 enumerates all pair representatives; C05.06-P2 computes a nonzero discrepancy and records a repair. E05 references identify actual sections, rather than generic placeholders.','',
'Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → capstone. Source dependency: mathematical M03 requires M02; M02 requires M01. This course uses their finite operations and the approved classroom analogue, without introducing unrelated module claims.','',
'Assumptions: the supplied analogue is authorized for all numerical practice; exact fractions suffice; pacing is an instructional design estimate, not a classroom trial; the full registry answer is withheld until students attempt construction. Recognition-only notation B⁻ᵀ is explained verbally and never assessed as matrix inversion.','',
'Source amendments: SA-05 is applied in Lessons 2–4 and propagated through registry and capstone. Use p=O_K+B L/2 and g_λ·(p−O_K)=λ/2. Keep λ, χ, r₃ and directed signs separate. All other supplied invariants remain in input-contract.json and govern any later extension.']
write('course-map.md','\n'.join(mapping))

write('teacher-guide.md','''# Teacher guide

Teach the complete course in eight 55-minute periods: six core lessons and two capstone periods. Students need signed arithmetic, fractions, coordinate triples and one-step linear equations. Start Lesson 1 by asking students to distinguish (1,0,0) from (0,1,0); start Lesson 2 by having them halve a negative number. These are readiness checks, not exclusion gates. If a student needs support, model one coordinate at a time and let the student explain the second.

The core lesson budget is 20 minutes of explanation and worked example, 15 of guided practice, 15 of diagnostics with feedback, and 5 for connecting to the next lesson. Lesson 4 divides explanation evenly between parity and remainders, with 7 and 8 minutes of respective practice. These timings are estimates; the authored core uses finite hand calculations. Do not add inverse-transpose derivation, complex exponentials or infinite recursion to the assessed core.

|Lesson|Teaching emphasis|Likely error and repair|Exit evidence|
|---|---|---|---|
|1|Nested lists and product count|Adding three menu lengths: draw one 3×3 block, then make three blocks|Explain distinctness and 1+6+12+8|
|2|Column steps, origin, half-address and ownership|Using BL or omitting O: check the center; confusing window with ownership: compare ±1/2|Map, invert and assign owner in D1/D3/D5|
|3|Enumerate sums before interpreting planes|Dropping center or O: list λ=0; evaluate both dot products in E2|Seven totals and affine check|
|4|Two distinct integer groupings|Negative remainder or negative λ treated as negative χ: solve λ=3k+r₃ and λ=2k separately|Explain 9/9/9 versus 13/14|
|5|Pair plus orientation reconstruction|χ used as s: compare two antipodes; center counted twice: solve L=−L|Reconstruct sv and count 13+1 classes|
|6|Independent checks and retained residuals|Totals mistaken for complete validation: change p without changing λ|Compute a nonzero R_L in P2 and preserve it|

At the end of Lesson 2, check that students can move both ways between L and p and explain z+u. At the end of Lesson 4, ask a student to give two nodes sharing χ and two sheet numbers sharing r₃ but differing in χ. At the end of Lesson 6, ask for one error that a count check misses and one error that an inverse check misses. These cumulative checks cover notation stability, prerequisite closure and capstone readiness. Repair the earliest misconception and repeat the affected check.

Capstone period 1: 5 minutes interpreting inputs, 15 for enumeration and q, 25 for p and z/u, 10 for peer comparison by address. Period 2: 15 minutes for λ/χ/r₃, 10 for v/s, 20 for inverse/pair/count checks, 10 for the information-preservation explanation and rubric feedback. Provide a blank 27-row table or allow students to construct it. A pair of students may divide arithmetic, but each student must independently reconstruct one row, explain one boundary case and show why s cannot be replaced by χ. The supplied full registry is the complete key; retain an independent attempt before distributing it.

All lesson practices and diagnostics have worked answers in their own files. The capstone rubric totals 100 points and avoids double-penalizing propagated arithmetic. A high numerical score does not waive repair of an omitted origin, discarded row, or missing direction sign. Additional practice can reuse the same procedure with another row from the 27-row window; no untaught operation is necessary.

Evidence language: call source statements source definitions or source-reported statuses; call the finite counts derived results; call the chosen numerical geometry a classroom analogue. No experimental observations are introduced. A proposed physical mechanism would be a new layer requiring its own premises, so it is not an assessed conclusion here. Preserve all discrepancies and correction histories. The source's broad mature-core status is not a fresh verification result from this course.

Recovery and maintenance: manifest.json is the authority after its hashes have been checked. Lesson text is assembled verbatim in course.md. Do not edit course.md independently; repair a source lesson, rebuild assembly, recompute affected checks, then refresh hashes. build_course.py contains the initial authored draft; do not rerun it over audited lesson repairs. finish_course.py rebuilds supports and the synthetic registry. verify_examples.py independently checks that registry. finalize_course.py refreshes assembly, audit and manifest only after review. The installed deterministic validator is run using the parent-approved project-root adapter. No rendered document is requested; Markdown tables and links are the delivery format.
''')

sources=[]
for s in c['sources']:
    actual=sha(Path(s['path']))
    assert actual==s['sha256'],s['id']
    sources.append(dict(s,actual_sha256=actual,hash_verified=True,content_use='Core definitions read at S02 M02/M03; authority/canonical record read at S03; other files pinned as archival context only, not independent proof.'))
dump('sources.json',{'sources':sources,'generation':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','manifest_sha256':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','retrieval':'Capabilities read; hybrid RAG no rerank; depth-one root traversal. Exact required definitions read in place from pinned local JSON.','pointers':['S02#/backbone_sequence/1/definitions','S02#/backbone_sequence/1/boundary_rule','S02#/backbone_sequence/2/definitions','S02#/backbone_sequence/2/sheet_populations','S02#/backbone_sequence/2/typed_finite_objects','S02#/backbone_sequence/2/proof/0','S03#/authority_contract','S03#/authoritative_status/mature_core','S03#/canonical_locked_values'],'source_gaps':[],'scope_limitations':['Full mature proof corpus and compiler integration not reverified; no such claim is needed for this finite course.','Graph labels and search snippets were discovery context, not formal authority.']})
notes=['# Compact source notes','',
'Exact local sources were read in place; no source snapshots or bulk data copies were created. All five supplied SHA-256 pins match. The course core is grounded in S02 mathematical backbone M02 and M03, with the approved SA-05 affine correction.','',
'|ID|Exact path|SHA-256|','|---|---|---|']
for s in sources: notes.append(f"|{s['id']}|{s['path']}|`{s['actual_sha256']}`|")
notes+=['','|Pointer|Use and evidence class|','|---|---|',
'|S02 /backbone_sequence/1/definitions and /boundary_rule|Source-defined affine ownership, q and z; finite classroom checks are freshly recomputed|',
'|S02 /backbone_sequence/2/definitions|Source-defined L,p,λ,χ and reciprocal sheet vector|',
'|S02 /backbone_sequence/2/sheet_populations|Source-reported 1,3,6,7,6,3,1; independently counted here|',
'|S02 /backbone_sequence/2/typed_finite_objects|Source distinction between 27 nodes and 27 complete cells; 8/12/6/1 classification|',
'|S02 /backbone_sequence/2/proof/0 and /proof/1|Printed origin-free sheet/phase formulas; retain as provenance and use approved affine correction in active teaching|',
'|S03 /authority_contract and /authoritative_status/mature_core|Source reports VERIFIED_FROZEN for M01–M18; that report is not a new course-run verification of all those modules|',
'|S03 /canonical_locked_values|Authoritative Cell3 branch, ICRS columns, negative determinant, half-open cells. No historical numeric witness is substituted into exercises|','',
'S01, S04 and S05 are hash-verified contextual sources; they are not used as separate evidence for a claim that was not read there. S02 M02 also contains older reciprocal-witness decimals; S03 AUD-005 distinguishes those superseded witnesses. The course does not calculate with either set of reciprocal decimals. It uses only the supplied exact synthetic basis for numerical work, explicitly labeled in every relevant artifact.','',
'SA-05 is a parent-approved source-fidelity amendment. Its origin correction is also verified directly: p−O=B L/2 gives g_λ·(p−O)=λ/2 because g_λ dots each column to 1. The uncorrected printed expression differs by g_λ·O; our nonzero-origin example exposes the difference. No source file was changed.','',
'Knowledge-graph retrieval: capabilities, hybrid search without reranking, and depth-one traversal from repository:KrytronDwayne/K-Field_Private were read. Active generation and manifest digest matched the runtime pin: sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7. Search returned integration and Lucas Lab context, not the required full mathematical backbone; therefore exact teaching definitions were read from the pinned local files. Graph labels and reported formal bindings were not promoted into proof claims.','',
'Evidence ledger: observations—none newly supplied in this finite course; source facts—definitions and reported statuses above; derived implications—counts, maps and pair properties recomputed here; interpretation—choice of registry fields and canonical representative; proposed mechanisms—none asserted; reference mathematics—integer arithmetic and finite coordinate geometry taught locally; unresolved information—no missing core definition, while broader mature proof bodies and integration adjudications remain outside this course verification.','',
'Historical and corrected source branches are never merged. Numerical Cell3 constants are not needed for the core tasks. The classroom analogue is not a replacement geometry and implies no physical scale or empirical validation. No phase, energy, force, galaxy metric or recursion-system claims are inferred from these finite counts.']
write('sources.md','\n'.join(notes))
print('Registry and support artifacts built; all generator assertions passed. Runtime:',sys.executable)
