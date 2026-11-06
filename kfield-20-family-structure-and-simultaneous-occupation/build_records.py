"""Course-local recovery and support generation; no source snapshots or external writes."""
import json, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
packet = json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name, text):
    (ROOT/name).write_text(text, encoding='utf-8', newline='\n')
def save(name, value):
    write(name, json.dumps(value, indent=2, ensure_ascii=False)+'\n')
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

source_records=[]
for source in packet['sources']:
    actual=digest(Path(source['path']))
    assert actual==source['sha256'], source['id']
    source_records.append({**source,'actual_sha256':actual,'hash_match':True})
source_records[1]['used_pointers']=['/backbone_sequence/15','/proof_nodes/78','/proof_nodes/81','/proof_nodes/78/shared_proof_steps/0','/proof_operations/9']
source_records[2]['used_pointers']=['/findings/6','/findings/8']
for i in (0,3,4):
    source_records[i]['scope']='Hash-verified supplied context; no additional substantive course claim attributed to this file.'
save('source-provenance.json',{
    'schema_version':'1.0','sources':source_records,
    'evidence_class':'Source documents and source-local claims; not fresh proof replay.',
    'graph':{
        'capabilities_called':True,
        'capabilities_generation':'Not exposed by capabilities response; read from subsequent RAG response.',
        'corpus_generation':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7',
        'manifest_sha256':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7',
        'query':'exact_simultaneous_family_occupation KFM-F038 M16','rerank':False,
        'integration_record':{
            'path':'kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json',
            'sha256':'a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a',
            'locator':'lines 1-101, returned RAG passage','trust':'source',
            'scope':'Reported accepted adjudication and known_science_replay counts; not fresh compiler or occupation-selection proof replay.'}},
    'retrieval_gaps':['Exact source L and P_v not loaded; classroom model explicitly synthetic.','Connecting physical-carrier selection proof not loaded; preserve M16/F038 claim, D10 guard and AUD-007 with no automatic source-status downgrade.']})

sources='# Sources and evidence boundaries\n\nAll five supplied file hashes were checked directly. Only compact provenance is retained; no source data was copied. Array indices in JSON pointers are zero-based.\n\n'
for s in source_records:
    sources+=f"## {s['id']}\n\nPath: `{s['path']}`\n\nSHA-256: `{s['sha256']}` — matched.\n\n"
    sources+=('Pointers used: '+', '.join('`'+p+'`' for p in s['used_pointers'])+'.\n\n') if 'used_pointers' in s else s['scope']+'\n\n'
sources+='''## Source-specific meaning

S02 mathematical-backbone M16 requires M11 and M14. Its definitions supply the 27-node lambda construction; its family projector supplies the 16-by-3-by-rank-one factorization. The internal dimension 16 and common transported history projector are declared premises here. We teach the finite operations needed to use them; no missing Clifford or history-transport proof is assigned as an implicit student prerequisite. Series courses 15 and 18 remain the placement prerequisites, not replacements for source dependency labels.

S02 F038 reports exact simultaneous family occupation. Its shared D10 record carries the physical-occupation guard. S03 AUD-007 records the conflict and prescribes recovering the physical-carrier selection proof, removing the obsolete guard only if discharged. Source-local VERIFIED_NOT_LOADED must not automatically downgrade the mature VERIFIED_FROZEN gate. We have not loaded the connecting proof. AUD-009 separately records missing replay objects, including lift L and P_v; the fully specified nine-translation example is a classroom analogue.

The Krytronx capabilities operation was called read-only; it did not itself expose generation fields. The subsequent RAG response supplied corpus generation and manifest digest `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7`, matching the packet. Reranking was disabled. Its retrieved passage from `kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json`, lines 1–101, source SHA-256 `a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a`, reports accepted adjudication, replay rank 48 and occupation [1,1,1], and direct-authority compiler modules M03, M07, M08. This is source evidence, not our compiler replay. Compiler labels are not silently identified with backbone labels. It does not resolve the missing source selection proof in this course.

No empirical measurements, measured densities, physical masses or mixing numbers are created here. Finite arithmetic is freshly recomputed; source statuses remain reported; the selection mechanism and exact source lift replay remain retrieval gaps. Geometry, metric, handedness, detector parity, global gauge forms and motion conventions in the packet are preserved as boundaries: none is used to supply an extra premise for this topical calculation. Family indices, history indices, lambda classes, projective channels and gauge representations remain distinct. No source branch or residual is erased.
'''
write('sources.md',sources)

mapping='# Course map — Family Structure and Simultaneous Occupation\n\nSeven lesson checkpoints, 15 core periods and three capstone periods, each 55 minutes (990 minutes total). Dense checkpoints retain their supplied multi-period boundaries. This is a complete topical course for seniors, not a semester survey.\n\nEntry capabilities: signed arithmetic, fractions, powers, solving linear equations and reading coordinates; series placement follows courses 15 and 18. Locally taught bridges include modular residues, vectors and norms, matrix multiplication, complex conjugation, Fourier inversion, trace, independence, rank and scalar Schur substitution. No calculus or prior university linear algebra is assumed.\n\nDependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → capstone. Backbone M16 source requires M11 and M14; it does not require M19 extension branches.\n\n| Checkpoint | Periods | Introduced and assessed capability | Later use |\n|---|---:|---|---|\n'
for l in packet['course_map']:
    mapping+=f"| [{l['id']}]({l['id']}.md) — {l['title']} | {l['teaching_anchor']['planned_periods']} | {l['assessment_target']} | {l['later_use']} |\n"
mapping+='\n## Exact coverage and capstone backward map\n\nEvery ID below labels actual content, including answered practice. The capstone introduces no new operation. Supplemental Weyl and Schur operations are preserved alongside the rank bridge.\n\n| Concept | Introduction/explanation | Worked example | Prior answered practice | Diagnostic | Capstone / later use |\n|---|---|---|---|---|---|\n'
for i in range(1,8):
    c=f'C20.{i:02d}'
    mapping+=f'| {c} | [lesson-{i:02d}](lesson-{i:02d}.md), {c}-E1 | {c}-W1 | {c}-P1 | {c}-D1 | C20-CAP-{i:02d}; '+(f'lesson-{i+1:02d}' if i<7 else 'capstone')+' |\n'
for c,l,cap in [('C20.S01','lesson-03','08'),('C20.S02','lesson-07','09')]:
    mapping+=f'| {c} | [{l}]({l}.md), {c}-E1 | {c}-W1 | {c}-P1 | {c}-D1 | C20-CAP-{cap}; capstone |\n'
mapping+='''
Legacy bridge C20-RANK-EX1, C20-RANK-P1 and C20-RANK-D1 appear explicitly in lesson 4, are prepared by the matrix/independence bridge in lesson 3, and support lesson 5 plus capstone part 4. SA-20 is taught together in lessons 5–7 and assessed in capstone part 6. The E05 content gate checks actual IDs and teaching, not blueprint promises. E07's example supplements, rather than replaces, the Weyl and Schur rows.

Unit boundaries: lessons 1–2 (finite classes and retained detail); lessons 3–4 (reversible coordinates and image accounting); lessons 5–7 (source projector, occupation premises and numerical-input scope). Cumulative checks at these boundaries examine stable terminology, dependency order, example complexity and readiness for the mapped capstone operations.

Core boundary: students compute supplied finite examples and read exact source cards. They do not replay a missing source lift certificate, a Clifford/chirality derivation, global determinant-line proof, physical-selection proof or continuum limit. Those are not silently claimed as completed teaching outcomes.
'''
write('course-map.md',mapping)

write('teacher-guide.md','''# Teacher guide

Teach the actual finite reasoning and ask students to point to the premise behind each count. Course placement follows courses 15 and 18; all operations needed for this course are nevertheless introduced in its lessons. Entry check: compute −5+8, 2/3 divided by 5/3, solve 3u+2=8 and locate a coordinate triple. Answers: 3, 2/5, u=2, and an ordered three-coordinate address. Repair fraction division and signed arithmetic before the core course; do not hide them inside a trace calculation.

## Pacing and classroom use

| Lesson | 55-minute periods | Session emphasis and readiness check |
|---|---:|---|
| 1 | 1 | Enumerate residues and all classes; student explains nine choices per class |
| 2 | 2 | Mean/detail first; norm and independent coordinates second; reconstruct all entries |
| 3 | 4 | A matrices/lift; B complex arithmetic/Fourier; C shift/phase and trace; D full Weyl practice; retain all nine coordinates |
| 4 | 2 | Column equations/projector; product basis/dimension versus rank |
| 5 | 2 | Typed source-factor table; history alternatives and orthogonality conditions |
| 6 | 1 | Claim/guard/correction card; explain missing selection dependency without erasing the source claim |
| 7 | 3 | Numerical scope; Schur substitution/reconstruction; singular cases and repair |
| Capstone | 3 | Parts 1–3; parts 4–6; parts 7–9 and checking |

Within each core period allow about 5 minutes retrieval, 20 explanation/worked example, 15 guided practice and 15 independent diagnosis/repair. The written lessons include full answers so learners can check after attempting. Reveal answer sections after the attempt or use a separate viewing window; the supplied Markdown is deliberately a complete reference. Use the extra sessions for students to derive each displayed table themselves. These are planned durations, not measured classroom completion times. Slow a session when a readiness check fails; do not remove Weyl or Schur practice to recover time.

## Targeted teaching and repair

In lesson 1 a negative remainder error is repaired by writing n=3q+r with 0≤r<3. Keep the table's pair order. In lesson 2 distinguish mean m from normalized coefficient 3m; ask learners to reconstruct a specific entry. Averages without detail and detail without means are incomplete representations.

In lesson 3 explicitly read row-by-column multiplication aloud. Demonstrate conjugation with i before ω. Have students verify ω², ω³ and 1+ω+ω², then compute one Fourier inverse coordinate at a time. Trace is a sum of three diagonal entries, not a determinant. For Weyl extraction use the entrywise formula to see why six coefficients vanish; listing only nonzero coefficients does not complete the required table. D/P order is part of the basis convention. The 243 lift output slots carry only 27 independently chosen input coordinates.

In lesson 4 require the equations α/2=0 and β=0 to justify independence; counting visible columns is not enough. The two-by-three label table precedes the projector count. In lesson 5 the restriction to one family has rank 16, while its history factor has rank one. Ask a student to say which one they mean each time. Rank-one projectors at different histories need an additional orthogonality condition. The finite q₃=0 example is deliberately declared as a teaching branch, not a recovered source definition.

In lesson 6 retain the five source records together. Accept neither automatic promotion of a source label into a fresh proof nor automatic downgrade because the proof body is not loaded. The documented AUD-007 conflict is the reason to distinguish mathematical construction from physical-carrier identification. This is not a general consensus disclaimer. The course does not assess belief in a mechanism.

In lesson 7 have students substitute the computed u,w into both original equations. E≠0 and S≠0 are separate tests. E=0 does not imply det K=0. For S=0 keep either the free variable with its reconstruction rule or the incompatible equations. Every original coordinate and residual stays available.

## Assessment alignment

The exact explanation, example, answered-practice and diagnostic IDs for all nine capstone parts are in course-map.md. Capstone parts 7 and 9 intentionally share a scalar system: part 7 assesses scope and a checked state, part 9 assesses derivation, reconstruction and branch handling. This overlap supports synthesis rather than introducing an untaught task. Part 8 uses the already practiced Weyl matrix. Full answers and a 100-point rubric are in capstone.md.

Use diagnostic answers to choose repairs, not to delete a student's discrepant result. Keep initial attempt, correction and the reason. Suggested mastery is 80 points plus successful scope/reconstruction repairs, as described in the rubric. Extensions such as a general matrix-block Schur proof, physical Yukawa derivation or source certificate replay are recognition-only and earn no required core points.

## Recovery and evidence use

Use manifest.json as the checkpoint index and verify hashes before resuming. Source-provenance.json records exact archival paths, hashes, pointers and retrieval boundaries. Verification is replayable using verify_examples.py under tf_gpu_env; verification.json records the checks. The independent review and audit report describe actual checks and repairs. The final course assembles passed lessons verbatim; supporting guides and capstone remain separately accessible. No PDF/Word or rendered artifact was requested, so Markdown is the delivered format.
''')

terms=[
('F₃, X','Residues {0,1,2}; X is their ordered triple set, with 27 nodes.','1'),
('λ, Cᵣ','Coordinate-sum residue; its nine-node class. r is a class/family label.','1'),
('δₓ, eⱼ','Address vectors; one at the named coordinate, zero elsewhere.','2–3'),
('δ_ac','Equality indicator, 1 if a=c and 0 otherwise; not an address vector.','3'),
('Φᵣ','Normalized class indicator, amplitude 1/3 on Cᵣ.','2'),
('m, d','Class mean and ordered zero-sum detail; f=m+d entrywise.','2'),
('U_λ, Wᵣ','Three-dimensional class-constant space and eight-dimensional class-detail spaces. W₂ here is not a weak gauge carrier.','2'),
('Inner product, norm','Conjugate-first product sum; norm squared is sum of absolute squares.','2–3'),
('Dimension','Number of independent coordinates in a space.','2'),
('Matrix, I, transpose','Linear array rule; identity leaves inputs unchanged; transpose swaps rows and columns.','3'),
('†, unitary, isometry','Adjoint = conjugate transpose. Square unitary: U†U=UU†=I. Rectangular isometry: V†V=I, reversible on its image, which need not fill the output space.','3'),
('L, Pᵥ, V','Explicit synthetic translation set, translation map and normalized labelled lift. Exact source objects remain unloaded.','3'),
('i, ω','i²=−1; ω=(−1+i√3)/2, ω³=1, 1+ω+ω²=0.','3'),
('F','Three-channel Fourier matrix Fⱼₖ=ω^(jk)/√3.','3'),
('P, D, B_ab','Shift, phase and Weyl matrix basis DᵃPᵇ. B_ab is not Cell3 B.','3'),
('Y, y_ab, Tr','Supplied matrix, its Weyl coefficients, and diagonal sum.','3'),
('Basis, independence','Building blocks with unique coordinates; only all-zero coefficients give a zero combination.','3–4'),
('Image, ran, rank','Possible outputs of a map; ran is another name for image; rank is image dimension.','3–4'),
('R','Teaching rank-2 orthogonal projector (called P in the packet); not the Cell3 inverse metric R_cell.','4'),
('Complement','(I−R)x; kept with Rx to restore x.','4'),
('⊗, carrier','Tensor/product coordinates indexed by pairs or triples of basis addresses; carrier is the space where a rule acts.','3–5'),
('qₙ, Qₙ, hₙ','Rank-one history projection, full product projection, normalized history image vector. n is not a family label.','5'),
('H','Finite history dimension when explicitly assumed; not specified by the rank-48 claim.','5'),
('Occupation (1,1,1)','Source uniform family/history count under its common projector; not a measured density.','5–6'),
('State, selection','A coordinate assignment; premises connecting physical states to a specified image.','6'),
('VERIFIED_FROZEN / VERIFIED_NOT_LOADED','Source-local statuses; not fresh course certificates.','6'),
('Yukawa, mixing','Reference coupling-matrix term; components across family coordinates. No physical numerical inputs selected here.','7'),
('K, A,B,C,E','Two-equation block matrix and locally scoped entries; not geometry basis, lambda class or mean map.','7'),
('u,w,s_U,s_W','Unknown retained coordinates and supplied right-hand sides.','7'),
('S,r','Schur coefficient A−BC/E and reduced source s_U−Bs_W/E in scalar examples.','7'),
('det, singular','det K=AE−BC; singular means no inverse. Each inverse has its own domain condition.','7'),
('M_cell,R_cell,G_phase,O_K,B','Reserved packet geometry notation: Gram metric, inverse, distinct phase metric, physical origin and ordered Cell3 basis. Not used as numerical inputs here.','Boundary')]
write('terminology.md','# Terminology and notation\n\nAll finite examples are dimensionless. Indices identify addresses, not units. Local meanings are declared before use.\n\n| Term | Meaning and scope | Lesson |\n|---|---|---|\n'+''.join(f'| {a} | {b} | {c} |\n' for a,b,c in terms))

# Recovery update: authored files are drafted until audited and verified.
checkpoints=[]
def cp(id,kind,path,deps):
    checkpoints.append({'id':id,'kind':kind,'path':path,'dependencies':deps,'status':'drafted','sha256':digest(ROOT/path),'summary':f'Authored {kind}; awaiting final verification and independent review.'})
cp('course-map','course-map','course-map.md',[])
for i in range(1,8): cp(f'lesson-{i:02d}','lesson',f'lesson-{i:02d}.md',['course-map'] if i==1 else [f'lesson-{i-1:02d}'])
cp('terminology','terminology','terminology.md',['lesson-07'])
cp('teacher-guide','teacher-guide','teacher-guide.md',['lesson-07'])
cp('capstone','capstone','capstone.md',['lesson-07'])
cp('sources','supplement','sources.md',[])
cp('provenance','supplement','source-provenance.json',['sources'])
save('manifest.json',{'schema_version':'1.0','topic':packet['topic'],'audience':packet['audience'],'assumptions':packet['assumptions'],'ordered_deliverables':[c['path'] for c in checkpoints]+['completion_report.json'],'checkpoints':checkpoints,'dependencies':{c['id']:c['dependencies'] for c in checkpoints},'course_order':[f'lesson-{i:02d}' for i in range(1,8)],'assembly':{'path':'course.md','section_ids':[f'lesson-{i:02d}' for i in range(1,8)]},'audit_counts':{'critical':0,'major':0,'minor':0},'blockers':[],'next_action':'Run independent mathematical verification, finish audit and assemble.'})
print('Draft recovery and support files written within',ROOT)
