"""Build authored course support and assembly; no source mutation or raw data copying."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
P=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text): (R/name).write_bytes((text.rstrip()+'\n').encode('utf-8'))
def h(name): return hashlib.sha256((R/name).read_bytes()).hexdigest()
rows=[]
for i,l in enumerate(P['course_map'],1):
    c=f'C15.{i:02d}'
    rows.append(f'|{c}: {l["title"]}|[lesson-{i:02d}](lesson-{i:02d}.md)|{c}-E1|{c}-W1|{c}-P1|{c}-D1|'+(f'lesson-{i+1:02d}' if i<7 else 'capstone')+f'|C15-CAP-{i:02d}|')
write('course-map.md','''# Course map — Matter States, Hypercharge, and Anomaly Accounting

Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs; course-14 context. Lesson 1 restates the five-label color-first carrier, and all additional assessed operations are introduced locally.

Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → capstone. The mathematical source dependency is backbone M10 → M11, not compiler M10 → M11. The course starts from the declared carrier and does not silently reassess all upstream source proofs.

|Concept|Introduction|Explanation|Worked example|Independently answered practice|Assessment|Later use|Capstone operation|
|---|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'''

Every displayed ID labels actual lesson content. Practice questions have worked answers before capstone use. Capstone.md gives each operation's named inputs and outputs and maps to these anchors. D1 is the first of four diagnostics in each lesson; additional diagnostics extend the same capability.

Units: Lessons 1–3 build the signed census and charge assignments; Lessons 4–5 calculate and solve constraints; Lessons 6–7 check representation/parity and source scope. Cumulative checks occur after Lessons 3, 5 and 7. There is no cycle and no concept first taught in the capstone.

Pacing retains the approved seven lesson IDs, with periods [2,2,2,3,2,2,1], totaling fourteen 55-minute core periods. Each period uses 5 retrieval, 20 teaching/example, 15 practice and 15 independent diagnostic/repair minutes. The capstone takes three additional periods. Session boundaries in each lesson avoid overloading a single period without breaking stable coverage links.

Coverage scope: choosing subsets and exchange signs; six bidegrees and all degree-four products; all q,Y/descent assignments; five local weighted tests and failing trials; cubic factorization/positive square/integer primitive line; complement signs/dual diagonal action/four-doublet count; source-scoped report. General group theory, physical family occupation, Lorentz chirality selection and arbitrary quotient-bundle topology are not hidden calculation requirements.

Approved assumptions are preserved in input-contract.json. All formal quantities calculated here are dimensionless. Source-local signs, color-first order, primitive sign, reference weights and evidence classes are retained. No geometry constants, measurement arrays or unrelated source branches are imported into this finite census course.
''')
write('terminology.md','''# Terminology and notation

|Term/symbol|Meaning in this course|First taught|
|---|---|---|
|H=C3⊕W2|Five-label internal carrier, three color labels followed by two weak labels; ⊕ collects the independent blocks|1|
|c1,c2,c3,w1,w2|Fixed ordered basis labels, not spatial coordinates|1|
|∧ (wedge)|Exterior product; neighbor exchange reverses coefficient, repetition gives zero|1|
|1 versus 0|Empty-selection basis product versus vanishing expression|1|
|degree k; even/odd|Number of selected distinct labels and its remainder modulo two|1|
|binom(n,k), k!|Count of k-subsets; factorial is product of integers 1 through k, 0!=1|1|
|(r,s), r_C,s_W|Counts of chosen color and weak labels, in that order|2|
|m, multiplicity|Number of independent components in a bidegree|2|
|sector/multiplet|Grouped components with a supplied common transformation type|2|
|nu^c,e^c,Q,u^c,d^c,L|Source sector names in census order; superscript c is part of left-Weyl naming, not complement operator C|2|
|a,b|Common color and weak phase weights; unrelated to geometric basis vectors used in other courses|3|
|q=ar+bs; Y=q/6|Dimensionless integer-normalized charge and hypercharge; neither is a measured coulomb value|3|
|t=r mod 3; p=s mod 2|Triality representative 0,1,2 and weak parity representative 0,1|3|
|x=0 mod n|Integer x is divisible by n, including negative multiples and zero|3|
|descent integer/residue|q+2t+3p and its remainder modulo 6, for the supplied symmetry-identification test|3|
|mq, mq³|Sum of individual charges or their cubes over m components; not (mq)³|3|
|SU3, SU2, U1|Names for color, weak and phase symmetries used in supplied tests|4|
|T|Quadratic index: 1/2 for 3,bar3,2 in the relevant mixed test; zero for singlets|4|
|spectator multiplicity|Number of copies from the other symmetry factor|4|
|local anomaly coefficient|Named weighted finite sum supplied by reference theory for the source's left-Weyl inventory|4|
|left-Weyl inventory|Declared common chirality convention for the six source rows; not derived from even exterior degree|4|
|primitive; gcd|Nonzero integral pair with greatest common divisor of absolute entries equal to 1|5|
|global sign convention|Simultaneous choice of weight signs, here color negative/weak positive|5|
|Ω, top form|c1∧c2∧c3∧w1∧w2 with this orientation|5|
|θ; determinant lock|Continuous common phase parameter; top-form preservation imposes 3a+2b=0|5|
|C(α)|Signed complement chosen so α∧C(α)=Ω for a positive canonical basis product; extended linearly|6|
|(3,2),bar3,1|Color-first representation types; 3 triplet, bar3 dual, 2 weak doublet, 1 singlet|6|
|λi, diag|Individual color multipliers; diag lists them without mixing components|6|
|i|Complex number satisfying i²=−1; used only for an explicitly taught phase example|6|
|Ω_C; d1,d2,d3|Color top form and oriented dual wedges|6|
|Witten parity|Parity of the number of weak doublet copies, here 3+1=4|6|
|Lorentz chirality|Separate spacetime transformation label, not internal subset parity|1,6|
|residual vector|All named coefficients minus their zero targets, retained with inputs and full rows|7|
|source fact; derived result; interpretation|What a record says; what displayed operations establish; meaning attached under a declared contract|7|
|Z1,Z2,Z3,Z6|Integration's admitted global-form labels; no topology calculation required|7|
|backbone versus compiler M labels|Separate module namespaces; shared numbers do not transfer authority|7|

Reserved cross-course symbols M_cell, R_cell, G_phase, O_K and B retain their input-contract meanings but are not used in this course's calculations. Geometric a,b,c vectors must not be confused with the locally declared scalar charge weights a,b. Internal degree, weak-doublet parity, detector parity, A1 carry parity, projective signs and family labels remain distinct.
''')
V=json.loads((R/'worked-example-verification.json').read_text(encoding='utf-8'))
source_rows=['|'+s['id']+'|'+s['path']+'|'+s['sha256']+'|fresh byte hash matches|' for s in V['sources']]
pointer_rows=['|'+key+'|S02#'+value+'|' for key,value in V['source_pointers'].items()]
write('sources.md','''# Compact source and evidence record

All source access was read-only. No source snapshot, database export or large array is included. The finite examples reproduce the stated algebra; off-line weight trials are clearly synthetic tests. No empirical observations are introduced.

|ID|Exact local path|SHA-256|Verification|
|---|---|---|---|
'''+ '\n'.join(source_rows)+'''

S02 is the substantive primary source: /backbone_sequence/10 (M11, requires M10) gives definitions, six-sector census and anomaly calculation; /branch_proofs/6 is BR-06, the source-local root-exterior theorem branch. Its reported endpoint is closed_exact_gauge_matter_theorem under the source's full premises. We reproduce the finite census and algebra here; that replay is not a fresh verification of every upstream premise. S01,S03,S04,S05 are retained packet provenance/context with verified bytes, not sources of silently substituted constants or alternative arithmetic branches.

|Formula ID|Exact JSON pointer|
|---|---|
'''+ '\n'.join(pointer_rows)+'''

X022 supplies exterior block factorization. X023 supplies general anomaly factors; X024 the primitive line; X026 the descent congruence; X027 complement duality and its chirality boundary. F033/F034 supply the even matter carrier and multiplets; F035 and F036 explicitly bound local anomalies and Witten count. Formula records sometimes refer to shared D09 rather than a full new proof body. Those larger status claims remain source-reported; the elementary operations printed in the lessons are independently recomputed.

## Accepted-integration provenance, kept separate

I01 logical path applications/kfield_standard_model/collaborator_record/project_record.json; retrieved alias kfield_standard_model/project_record.json; SHA-256 3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c. Source-attributed RAG lines 1–142 contain the global-form hazard and open obligations (packet pointers /hazards/3, /open_obligations/1, /open_obligations/2). Fresh retrieval confirmed the excerpt: retain Z1,Z2,Z3,Z6, with unique physical selection unresolved. This is a reported excerpt digest, not a fresh local byte hash of the remote artifact.

I02 logical path kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json; SHA-256 a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a. Fresh RAG excerpt lines 1–101 confirms /direct_authority_modules = M03,M07,M08; /agda/certificate reports KField.StandardModelCompilerAdjudication.p12-standard-model-compiler-adjudication; /known_science_replay reports anomaly zeros and four doublets. These compiler labels are not mathematical-backbone labels. No fresh Agda execution is claimed.

Capabilities was called at task start; its response described read-only operations but supplied no paired corpus identity. The two subsequent RAG retrievals supplied corpus_generation sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7 and manifest_sha256 5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7, matching the packet. RAG index SHA-256 aca56e6b5b2b717459cea9790e6142ea9e8058f74d135710906926e9065ad54a; rerank false. Exact local source bytes, rather than graph labels, ground the finite course.

## Verification and limits

verify_examples.py checks all five local hashes, directly compares the M11 census, enumerates all sixteen even subsets and their charges/descent, tests all 32 signed complement involutions, and compares direct ledgers against polynomial formulas on 121 small integral pairs using exact rational arithmetic. General identities are also derived by distribution and completed squares in Lessons 4–5; grid testing alone is not their proof. Worked-example-verification.json records compact component assignments, contributions and failed trial vectors. Independent-audit.json supplies a separate content audit.

No missing source prevents the finite curriculum. Broader upstream proof closure, fresh compiler authority, physical chirality selection, unique physical global-form selection and arbitrary non-liftable quotient-bundle anomaly proofs are outside the replay and remain explicitly scoped. The course does not claim those gaps were closed.
''')
order=[f'lesson-{i:02d}' for i in range(1,8)]
write('course.md','# Matter States, Hypercharge, and Anomaly Accounting\n\nSeven lessons, fourteen core periods. See teacher-guide.md, terminology.md, sources.md and capstone.md for supporting materials.\n\n'+'\n\n'.join(f'<!-- BEGIN: {x} -->\n'+(R/(x+'.md')).read_text(encoding='utf-8').rstrip('\n')+f'\n<!-- END: {x} -->' for x in order))
# Recovery checkpoint update: content awaits final support audit, never fabricate completion here.
specs=[('map','course-map','course-map.md',[])]+[(x,'lesson',x+'.md',['map'] if i==0 else [order[i-1]]) for i,x in enumerate(order)]+[('glossary','terminology','terminology.md',order),('teacher','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('sources','supplement','sources.md',[]),('replay','supplement','worked-example-verification.json',['sources']),('replay-script','supplement','verify_examples.py',[]),('support-script','supplement','build_support.py',[]),('assembly','assembly','course.md',order),('audit','audit','audit_report.json',order)]
checkpoints=[{'id':i,'kind':k,'path':p,'dependencies':deps,'status':'drafted','sha256':h(p),'summary':f'{k} artifact saved; final audit pending'} for i,k,p,deps in specs]
manifest={'schema_version':'1.0','topic':P['topic'],'audience':P['audience'],'assumptions':P['assumptions'],'ordered_deliverables':[x['path'] for x in checkpoints]+['completion_report.json'],'checkpoints':checkpoints,'dependencies':{x['id']:x['dependencies'] for x in checkpoints},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':{'critical':0,'major':0,'minor':0},'blockers':[],'next_action':'Independent support audit; finalize and run validator'}
write('manifest.json',json.dumps(manifest,indent=2,ensure_ascii=False))
print('Saved support artifacts, verbatim assembly and drafted recovery hashes.')
