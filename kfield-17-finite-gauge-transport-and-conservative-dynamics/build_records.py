"""Recovery/assembly steward. Run only inside the designated course folder.
No source snapshots, external writes, dependencies or package changes.
Draft mode records progress; --final requires independently passed content reviews.
"""
from pathlib import Path
import hashlib, json, sys

root=Path(__file__).resolve().parent
packet=json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
assert root.resolve()==Path(packet['course_output_directory']).resolve()
def write(name,text): (root/name).write_text(text.rstrip()+'\n',encoding='utf-8')
def dump(name,data): write(name,json.dumps(data,ensure_ascii=False,indent=2))
def digest(name): return hashlib.sha256((root/name).read_bytes()).hexdigest()
final='--final' in sys.argv
lessons=packet['course_map']
ids=[x['id'] for x in lessons]

# Verify independent checkpoints before accepting their status.
review=json.loads((root/'independent-lesson-audit.json').read_text())
for c in review['checks']:
    assert digest(c['path'])==c['sha256'], 'Independent audit stale: '+c['path']
    assert c['result']=='passed'

maptext='''# Course map — Finite Gauge Transport and Conservative Dynamics

Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, powers, linear equations and coordinate graphs. Courses 07 and 14 supply context; complex arithmetic, adjoints, matrix multiplication and metric operations are rebuilt locally. There is no dependency on an unavailable earlier course file for a required calculation.

The eight-lesson dependency chain is lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → lesson-08 → capstone. Thirteen 55-minute core periods plus three capstone periods give 880 planned minutes. Multi-period lessons retain their stable IDs so every approved anchor is preserved. The unit boundaries are after lessons 04, 06 and 08.

Each period allocates retrieval 5, teaching/worked example 20, answered practice 15 and diagnostics/repair 15 minutes. Counts are plans, not classroom observations.

| Lesson | Topic | Periods | Teaching/practice/check minutes, plus retrieval | Later use |
|---|---|---:|---|---|
'''
for l in lessons:
    n=l['teaching_anchor']['planned_periods']
    maptext+=f"| [{l['id']}]({l['id']}.md) | {l['title']} | {n} | {20*n}/{15*n}/{15*n}, plus {5*n} | {l['later_use']} |\n"
maptext+='''
## E05 coverage with actual content anchors

Each E1 is a student-facing explanation, W1 a worked example, P1 an attempted practice with worked answer, and D1 an answered diagnostic. The capstone uses the prior practice operations, not an untaught recognition-only extension.

| Concept | Introduction | Explanation | Worked | Practice | Assessment | Later use | Capstone |
|---|---|---|---|---|---|---|---|
'''
for i,l in enumerate(lessons,1):
    c=f'C17.{i:02}'
    maptext+=f"| {c}: {l['title']} | {l['id']} | {c}-E1 | {c}-W1 | {c}-P1 | {c}-D1 | {l['later_use']} | C17-CAP-{i:02} |\n"
maptext+='''
The capstone backward map specifies input and output operations in capstone.md. Its eight steps cover transport/recovery, covariant comparison, ordered loop, invariant action, Cayley hypotheses and reversal, typed Hodge blocks, certificate reading and a separately synthetic minimum, and finite conservation with retained remainders.

## Fidelity and boundaries

The mature Hodge branch uses exponents 1/3 and 2/3. Historical exponents remain separately labeled. The example J is explicitly supplied, never represented as an unloaded archival convention. The finite-rung bound is source-scoped reading because complete replay inputs are unavailable. The thermal-series paragraph is recognition-only; no infinite convergence or continuum theorem is assigned.

Lesson 08 refines the blueprint's informal word expectation: Q_L is the unnormalized quadratic value, while Q_L/N is the normalized expectation for N>0. This closes a notation risk without removing any approved operation. No required concept or anchor was dropped.
'''
write('course-map.md',maptext)

term='''# Terminology and notation

Symbols are scoped to their lessons. All toy links and states are dimensionless. LU, TU and AU denote illustrative length, time and action units, and EU=AU/TU denotes energy units. They are not experimental calibrations.

| Term/symbol | Operational meaning and units | First use |
|---|---|---|
| i; conjugate | i²=−1; conjugate of a+bi is a−bi | 01 |
| State ψ | Column of components in a declared local frame | 01 |
| Frame/site | Coordinate convention/location label; x and y are labels here | 01 |
| U_xy | Link from y to x; rightmost factor acts first | 01 |
| diag; I | Diagonal matrix; identity of the stated dimension | 01 |
| T; † | Transpose; conjugate transpose (adjoint) | 01 |
| Inverse U⁻¹ | Two-sided map undoing U | 01 |
| Unitary | U†U=UU†=I; preserves Euclidean complex norm | 01 |
| Norm squared N | ψ†ψ, sum of squared component moduli | 01 |
| G_x; prime | Frame change at x; prime means changed coordinates, not derivative | 02 |
| d_x | ψ_x−U_xyψ_y, full retained finite difference | 02 |
| Covariant | Follows its stated transformation rule, e.g. d′_x=G_xd_x | 02 |
| Invariant | Unchanged under the specified operation | 02 |
| Holonomy U_loop | Ordered net loop map with a basepoint | 03 |
| X; Z | Synthetic swap and diag(1,−1) maps | 03 |
| Conjugation | G U G⁻¹; preserves trace | 03 |
| Plaquette | Elementary closed lattice face; example loop is an algebraic analogue | 03 |
| Tr; Re | Diagonal sum; real part | 04 |
| F | I−U_loop, retained matrix comparison | 04 |
| β; S | Positive action coefficient in AU; β ReTr(I−U_loop) in AU | 04 |
| det | Determinant; diagonal product, or ad−bc for a 2 by 2 matrix | 05 |
| Lhat | Self-adjoint finite matrix in TU⁻¹ for the synthetic evolution | 05 |
| τ_C; C | Real Cayley time in TU; dimensionless rational update | 05 |
| Self-adjoint | Lhat†=Lhat, distinct from unitarity | 05 |
| M_cell; R_cell | Gram metric BᵀB in LU²; its inverse in LU⁻² | 06 |
| B | Ordered real basis columns; toy examples do not replace locked ICRS Cell3 B | 06 |
| δ; V | det(M_cell)=V² in LU⁶; positive volume in LU³ | 06 |
| G_phase; G_eff | Distinct phase/effective metrics, not substituted for M_cell | 06 |
| Bivector; wedge²R | Oriented area coordinates; map on pairs (12,13,23), LU⁻⁴ | 06 |
| Minor | Determinant of a selected submatrix | 06 |
| J | Declared example pairing [[0,0,1],[0,−1,0],[1,0,0]] | 06 |
| H_E; H_B | Dimensionless mature electric/magnetic Hodge blocks | 06 |
| Rung; compiler | Hierarchy level; specified finite model construction | 07 |
| Certificate; hash | Calculation record; byte fingerprint, not proof of its content | 07 |
| ε_E; ε_B; α | Source-reported enclosure/contraction bounds | 07 |
| Δ; H_N; τ_R; E0 | Gap in energy units; action scale; positive time scale; E0=H_N/τ_R | 07 |
| d_root; c_* | Normalized synthetic root bound; positive detail lower bound | 07 |
| min | Smaller of the supplied arguments | 07 |
| Q_L | Unnormalized ψ†Lhatψ in TU⁻¹; not distance Q, Q_g or Q_nu | 08 |
| Q_L/N | Normalized expectation for N>0 | 08 |
| r | Retained component-wise remainder ψ_new−ψ_ref | 08 |
| β_T; exp; ln | Recognition-only thermal parameter; exponential; its inverse logarithm | 08 |
| T (thermal paragraph only) | Uncomputed tail; distinct from transpose superscript T | 08 |

Source notation safeguards: O_K denotes the declared physical origin in affine identities using x−O_K; it is not used as a substitute for a site label. Cell ownership [-1/2,1/2)^3 is distinct from nearest-integer tie rules, neither of which is assessed here. Detector parity, carry parity, projective signs, chirality and family labels are not equated by our minus signs. Our two-component space is not claimed to be the source's color-first C₃ direct-sum W₂ carrier. Mathematical-backbone module names and integration compiler labels are separate namespaces.
'''
write('terminology.md',term)

source_rows=[]
for s in packet['sources']:
    p=Path(s['path']); actual=hashlib.sha256(p.read_bytes()).hexdigest()
    assert actual==s['sha256'],s['id']+' source hash mismatch'
    source_rows.append({**s,'actual_sha256':actual,'hash_match':True})
provenance={'schema_version':'1.0','source_files':source_rows,
 'source_pointers':['S02#/backbone_sequence/12','S02#/hodge_normalization_theorem','S04#/hodge_correction_proof','S03#/findings/8','S01#/backbone_sequence/12/definitions'],
 'evidence_class':'Local hash-verified archival source statements; finite teaching algebra independently checked; no empirical data.',
 'graph':{'capabilities':'Read-only call succeeded; capabilities did not itself expose generation.',
 'retrieval':'Sparse RAG M13 Cayley Hodge finite gauge transport, rerank=false. Returned integration compiler and moving-frame material, not a missing finite-rung replay object. No proof promotion or namespace merger.',
 'corpus_generation':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7',
 'manifest_sha256':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7',
 'identity_source':'project_rag_search response metadata; matches runtime packet'},
 'gaps':['Full fixed-rung compiler matrices, coefficients, interval method/precision and pinned certificate replay object unavailable in read packet.','Archival J basis convention not loaded; teaching J explicitly synthetic.'],
 'source_snapshot_copies_created':False}
dump('source-provenance.json',provenance)
st='''# Compact source notes

All five exact files below were read-only and their SHA-256 values matched the launch packet. JSON pointers locate source statements without copying the archive. Hash verification checks identity; it does not promote a reported proof status. The lesson algebra and tiny synthetic examples have separate verification records.

'''
for s in source_rows:
    st+=f"- **{s['id']}**: `{s['path']}`\n  SHA-256: `{s['sha256']}`.\n"
st+='''
## Claim routing

| Claim | Exact pointer | Evidence and use |
|---|---|---|
| Ordered loops, trace action, Cayley form | S02 /backbone_sequence/12/definitions and /proof | Archival construction; finite toy identities recomputed |
| M13 requirements M04, M10, site-indexed compact-group links and positive coefficients | S02 /backbone_sequence/12/requires | Source dependency list; we teach the needed finite operations locally, without replacing full source modules |
| Mature Hodge exponents 1/3 and 2/3 | S02 /hodge_normalization_theorem; S04 /hodge_correction_proof | Source formulas; diagonal derivation and examples independently checked |
| Historical exponents 2/3 and 4/3 | S01 /backbone_sequence/12/definitions | Historical branch, separately tested and never used as mature normalization |
| Four finite compiler bounds and recursive/thermal claims | S02 /backbone_sequence/12/proof | Source-reported, precise signs/digits retained; no full certificate replay |
| Exact-finite versus optional comparisons | S02 /backbone_sequence/12/status_partition | Source's own scope partition, not a new universal certification |
| Missing J convention and fixed-rung replay inputs | S03 /findings/8 (AUD-009) | Retrieval gap; VERIFIED_NOT_LOADED is a source status |
| S05 | Hash verification only | Supplied archive context; no S05 physical claim needed for this course |

The local pinned source was the decisive exact grounding. Read-only Krytronx capabilities and sparse RAG retrieval were also consulted. RAG response metadata confirmed generation and manifest digest `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7`. The search returned different integration/compiler and reference-frame contexts, not a full M13 replay certificate. They were not substituted for the mathematical-backbone M13. There was no graph node relevant enough to warrant promoting or traversing it as certificate evidence.

All state columns, small matrices, action coefficients, metric J, and example scales are explicitly synthetic. The fixed-rung certificate is a reading exercise; actual compiler/rung identifier, matrices, native coefficient list, interval method, working precision and hashed replay object/command remain unavailable. Source decimal bounds are not working-precision settings. The example J supplies a convention for hand calculations and does not repair the source retrieval gap.

No source-data snapshots, bulk exports, experimental observations or physical mechanisms were invented. Existing source branches are retained by exact pointers and their roles. No physical geometry constants are mixed into the teaching matrices. Further corpus recovery can extend the source card without changing the finite examples or treating a graph label as proof.
'''
write('sources.md',st)

assembled='# Finite Gauge Transport and Conservative Dynamics\n\nEight student lessons. See course-map.md for pacing and capstone.md for synthesis and assessment.\n\n'
for ident in ids:
    assembled+=f'<!-- BEGIN: {ident} -->\n'+(root/(ident+'.md')).read_text(encoding='utf-8').rstrip('\n')+f'\n<!-- END: {ident} -->\n\n'
write('course.md',assembled)

counts={'critical':0,'major':0,'minor':0}
audit={'schema_version':'1.0','status':'passed' if final else 'in_progress','unresolved_counts':counts,
 'findings':[{'id':'A17-001','level':'local','category':'notation','file':'lesson-08.md','section':'C17.08-E1 and capstone 08','severity':'major',
 'defect':'Blueprint loosely called unnormalized values 9 and 8 expectations; without normalization students could equate them to normalized expectation.',
 'correction':'Teach Q_L=psi-adjoint Lhat psi and Q_L/N separately; preserve original finite quadratic checks and add normalized values 9/5 and 4/3.',
 'verification':'Exact arithmetic independently recomputed in independent-lesson-check.py; auditor confirmed distinction and capstone uses both quantities.',
 'disposition':'corrected','affected_checkpoints':['lesson-08','capstone','terminology','assembly']}],
 'local_review':'independent-lesson-audit.json pins all eight lesson hashes and reports actual content and exact arithmetic checks.',
 'cumulative_checks':[{'boundary':'lesson-04','result':'passed','checks':'Shared link direction, rightmost-first path, conjugation and trace/action dependency checked across lessons 01-04.'},{'boundary':'lesson-06','result':'passed','checks':'Complex division and adjoints taught before Cayley; metric-weighted comparison precedes area factors. Units and mature/historical exponents kept separate.'},{'boundary':'lesson-08','result':'passed','checks':'Certificate reading and synthetic minimum precede capstone; norm versus quadratic versus normalized expectation distinguished. Thermal comparison stays recognition-only.'}],
 'final_review':'Independent capstone audit plus manager final scope/coverage/identity review; deterministic validator is run after records are refreshed.' if final else 'Pending final capstone/content review and deterministic validation.',
 'rendering':'Markdown only, no paginated artifact requested; tables/headings/code blocks inspected as text. No PDF visual rendering claimed.',
 'source_gaps':provenance['gaps']}
if final:
    ca=json.loads((root/'independent-capstone-audit.json').read_text())
    # Content reviewer uses explicit unresolved severity fields.
    assert ca['unresolved_critical']==0 and ca['unresolved_major']==0 and ca['unresolved_minor']==0
    for item in ca['files']:
        assert digest(item['path'])==item['sha256'],'Final independent audit stale: '+item['path']
    for finding in ca['findings']:
        audit['findings'].append({'id':finding['id'],'level':finding.get('level',finding.get('audit_level','final')),'category':finding['category'],'file':finding['file'],'section':finding['section'],'severity':finding['severity'],'defect':finding['defect'],'correction':finding['correction'],'verification':finding['verification'],'disposition':finding['disposition'],'affected_checkpoints':finding.get('affected_checkpoints',finding.get('affected_checkpoint_ids',[]))})
    audit['final_content_review']='independent-capstone-audit.json; current file hashes checked before acceptance'
dump('audit_report.json',audit)

paths=[('course-map','course-map','course-map.md',[])]
for i,ident in enumerate(ids): paths.append((ident,'lesson',ident+'.md',[ids[i-1]] if i else ['course-map']))
paths += [('terminology','terminology','terminology.md',ids),('teacher-guide','teacher-guide','teacher-guide.md',ids),('capstone','capstone','capstone.md',ids),('sources','supplement','sources.md',[]),('provenance','supplement','source-provenance.json',[]),('verification','supplement','worked-example-verification.json',ids),('independent-lessons','supplement','independent-lesson-audit.json',ids),('independent-check','supplement','independent-lesson-check.py',[]),('assembly','assembly','course.md',ids),('audit','audit','audit_report.json',['assembly','capstone']),('record-builder','supplement','build_records.py',[])]
if (root/'independent-capstone-audit.json').exists(): paths.append(('independent-capstone','supplement','independent-capstone-audit.json',['capstone','teacher-guide']))
if (root/'verify_examples.py').exists(): paths.append(('example-checker','supplement','verify_examples.py',[]))
checkpoints=[]
for ident,kind,path,deps in paths:
    exists=(root/path).exists()
    status='passed' if final else ('passed' if kind=='lesson' else 'drafted')
    checkpoints.append({'id':ident,'kind':kind,'path':path,'dependencies':deps,'status':status if exists else 'pending','sha256':digest(path) if exists else None,'summary':f'{kind}: {path}; authored content and verification record.'})
ordered=[x[2] for x in paths]+['completion_report.json']
assumptions=packet['assumptions']+['Thirteen core periods and three capstone periods are planning estimates.','Full fixed-rung certificate unavailable: assessed as exact source-scoped reading only.','Declared synthetic J and metrics do not replace source-locked Cell3 objects.']
manifest={'schema_version':'1.0','topic':packet['topic'],'audience':packet['audience'],'assumptions':assumptions,'ordered_deliverables':ordered,'checkpoints':checkpoints,'dependencies':{c['id']:c['dependencies'] for c in checkpoints},'course_order':ids,'assembly':{'path':'course.md','section_ids':ids},'audit_counts':counts,'blockers':[],'next_action':'none' if final else 'Finish independent capstone review, verify arithmetic, inspect final coverage and run validator.'}
dump('manifest.json',manifest)
completion={'schema_version':'1.0','status':'complete' if final else 'in_progress','topic':packet['topic'],'audience':packet['audience'],'assumptions':assumptions,'outputs':ordered,'audit_counts':counts,'hashes':{p:digest(p) for p in ordered if p!='completion_report.json' and (root/p).exists()},'lesson_count':8,'core_periods':13,'capstone_periods':3,'source_gaps':provenance['gaps'],'validator_note':'Completion is subject to successful final deterministic validator; result is recorded separately after execution.'}
completion['hashes']['manifest.json']=digest('manifest.json')
dump('completion_report.json',completion)
print('Recovery records refreshed; mode='+('final-candidate' if final else 'draft'))
