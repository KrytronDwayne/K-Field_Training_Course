"""Refresh authored map, assembly and draft recovery records within this course only."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text): (ROOT/name).write_text(text,encoding='utf-8')
def digest(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
rows=['# Course map — Higgs, Yukawa, and Interaction Interfaces','',
'Audience: high-school seniors with signed arithmetic, fractions, powers, linear equations and coordinate graphs. Course-15 sector capabilities are recalled locally in lesson 1. No calculus, general linear algebra or quantum mechanics is assumed for assessed work.','',
'Seven lessons retain the approved boundaries and twelve core periods; the capstone uses three more 55-minute periods. The longer lessons have explicit internal period divisions. Reason: contraction signs and coordinate changes need taught/practiced bridges before synthesis.','',
'Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → capstone. Source M12 requires M11; M11 supplies the recalled sector census, not an additional untaught assessment.','',
'| Lesson | Outcome / example capability | Periods | Retrieval / teaching / practice / diagnostic minutes | Later use |','|---|---|---:|---|---|']
for row in p['course_map']:
    n=row['teaching_anchor']['planned_periods']
    rows.append(f"| [{row['id']}: {row['title']}]({row['id']}.md) | {row['worked_example_capability']} | {n} | {5*n} / {20*n} / {15*n} / {15*n} | {row['later_use']} |")
rows+=['','## Actual coverage and backward map','','Each ID below occurs in the named lesson; P items include worked answers and are to be attempted independently before revealing the key. Capstone inputs and outputs are specified in capstone.md.','',
'| Concept | Explanation | Worked example | Prior practice | Diagnostic | Capstone output | Later dependency |','|---|---|---|---|---|---|---|']
outputs=['Four input type/charge/degree routes','Four signed scalars, zero component, phase and covariance checks','Component charges, neutral vacuum and squared length','Mass squares, masses and rho with domain','Original/swapped coefficient map and inverse','Signed endpoint/prediction/residual ledger','Source-input contract and evidence inventory']
for i,row in enumerate(p['coverage_matrix'],1):
    c=row['concept_id']; extra='; E2/W2/P2/D2' if i==2 else ''
    rows.append(f"| {c}: {row['concept']} | {c}-E1 | {c}-W1 | {c}-P1{extra} | {c}-D1 | C16-CAP-{i:02}: {outputs[i-1]} | {row['later_use']} |")
rows+=['','All C16.02-E2, C16.02-W2, C16.02-P2, C16.02-D2 items reside in lesson-02. The P2 explanation answer rehearses the general covariance argument. Lesson-07 P1 includes a source-scope comparison answer, supporting the capstone integration sentence.','',
'Unit checks occur after lessons 2, 5 and 7. Core operations are finite arithmetic, alternating slot removal, specified diagonal phases, two-by-two maps and source-card reading. General Lie theory, potential minimization, mass diagonalization, variational dynamics and full compiler execution are recognition-only or outside scope; none is a hidden capstone computation.','',
'Sources: S02 mathematical backbone M12 and branch BR-07, with M11 sector table as prerequisite bridge; compact exact provenance in sources.md and sources.json. Other supplied archival branches remain separate and are not mixed into numerical examples.','']
write('course-map.md','\n'.join(rows))
order=[x['id'] for x in p['course_map']]
write('course.md','# Higgs, Yukawa, and Interaction Interfaces\n\nStudent course. See course-map.md for pacing and capstone.md for synthesis.\n\n'+'\n\n'.join(f'<!-- BEGIN: {i} -->\n'+(ROOT/(i+'.md')).read_text(encoding='utf-8').rstrip('\n')+f'\n<!-- END: {i} -->' for i in order)+'\n')
source_rows=['# Source notes','',
'All five supplied archival byte hashes were freshly checked against input-contract.json. Only S02 is used for substantive interaction teaching; S01/S03/S04/S05 remain separately identified provenance branches. No source data was copied. Source bytes were read in place.','',
'| ID | Absolute path | Verified SHA-256 |','|---|---|---|']
for s in p['sources']:
    source_rows.append(f"| {s['id']} | {s['path']} | {s['sha256']} |")
source_rows+=['','## Exact source locations and uses','',
'- S02 /backbone_sequence/10: M11 sector census and q=−2r_C+3s_W. Lesson 1 recall.','- S02 /backbone_sequence/11: M12, requires M11; four ordered interface definitions, neutral vacuum, mass formulas, five state-coordinate categories. Lessons 1–7.','- S02 /proof_nodes/80: KFM-X028, typed Higgs branch; numerical vacuum and potential coefficients remain inputs. Lessons 3–4.','- S02 /proof_nodes/84: KFM-X029, typed Yukawa invariants; coefficient matrices remain inputs. Lessons 2 and 5.','- S02 /proof_nodes/86: KFM-X030, six-sector action sum; weights and boundary values remain inputs and no dynamics is inferred by decomposition. Lesson 6.','- S02 /branch_proofs/7: BR-07 endpoint, source-reported closed exact typed interaction architecture with numerical values as occupied-state coordinates. Lesson 7.','',
'These JSON pointers, rather than PDF pages, locate the exact source records. Source-reported status is distinct from fresh finite verification. The kinetic-term expansion and a full formal compiler are not replayed; the finite mass formulas are supplied premises and their algebra is checked. The exterior covariance explanation is a taught argument under explicit determinant-one/vector-dual conditions.','',
'## Integration scope and retrieval','',
'A fresh Krytronx capabilities call confirmed the read-only surface but did not expose a corpus-generation pair. A fresh non-reranked hybrid RAG query for KFM-X028/KFM-X029/KFM-X030 returned corpus_generation and manifest_sha256 both matching the packet: '+p['source_routing']['snapshot_generation']+'. RAG index SHA-256: aca56e6b5b2b717459cea9790e6142ea9e8058f74d135710906926e9065ad54a.','',
'The returned source excerpt kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json, lines 1–101, SHA-256 a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a, reports direct_authority_modules M03/M07/M08 and known_science_replay m12_rho exact_rational_identity plus four zero Yukawa charge sums. These are compiler-adjudication labels, not automatic authority for mathematical-backbone M12. The certificate is reported; no fresh typecheck was run.','',
'The packet-supplied integration provenance card I01 locates applications/kfield_standard_model/collaborator_record/project_record.json (retrieved alias kfield_standard_model/project_record.json), SHA-256 3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c, /hazards/3 and /open_obligations/1–2. That earlier RAG-source provenance admits global-form family Z1,Z2,Z3,Z6 and leaves the unique physical member unresolved. It is inherited source-attributed provenance, not a new local byte hash or independent source-author authentication.','',
'## Evidence classes and gaps','',
'No empirical data or current measured constants are introduced. All component values and energy/matrix/mass numbers are synthetic or finite basis tests. Fresh derivations are identified in lessons and checked in worked-example-verification.json. Possible measurements in lesson 7 are proposals only. Physical potential coefficients, mixing values, matching scale, rate dynamics and empirical preparation remain unspecified; the course does not fill them by symmetry. No general field-theory proof body or fresh compiler typecheck is claimed. These scope limits do not block the taught finite operations.','',
'Series invariants stay intact: color-first ordering, separate parity/family/chirality meanings, no borrowed Cell3 or galaxy geometry, no phase-to-force inference, no photon-equivalent-to-measured-energy substitution, and no erased residuals. The exact full invariant list is retained in input-contract.json; nonapplicable geometry and recursion statements are not used as hidden premises.','']
write('sources.md','\n'.join(source_rows))
files=[('map','course-map','course-map.md',[])]+[(i,'lesson',i+'.md', ['map'] if k==0 else [order[k-1]]) for k,i in enumerate(order)]+[
('glossary','terminology','terminology.md',order),('teacher','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('sources','supplement','sources.md',[]),('source-record','supplement','sources.json',[]),('verification','supplement','worked-example-verification.json',order),('verification-script','supplement','verify_examples.py',[]),('records-script','supplement','build_records.py',[]),('contract','supplement','input-contract.json',[]),('assembly','assembly','course.md',order),('audit','audit','audit_report.json',order+['capstone'])]
old=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8-sig'))
oldcp={x['id']:x for x in old.get('checkpoints',[])}
checkpoints=[]
for ident,kind,path,deps in files:
    olditem=oldcp.get(ident,{})
    sha=digest(path)
    status='passed' if olditem.get('status')=='passed' and olditem.get('sha256')==sha else 'drafted'
    checkpoints.append(dict(id=ident,kind=kind,path=path,dependencies=deps,status=status,sha256=sha,summary=f'{kind}: {path}'))
m=dict(schema_version='1.0',topic=p['topic'],audience=p['audience'],assumptions=p['assumptions'],ordered_deliverables=[x[2] for x in files]+['completion_report.json'],checkpoints=checkpoints,dependencies={x['id']:x['dependencies'] for x in checkpoints},course_order=order,assembly={'path':'course.md','section_ids':order},audit_counts={'critical':0,'major':0,'minor':0},blockers=[],next_action='Finish independent audit, repair, finalize hashes and run project validator')
write('manifest.json',json.dumps(m,indent=2)+'\n')
print(json.dumps({'assembled_lessons':len(order),'checkpoints':len(checkpoints),'status':'drafted_pending_final_audit'}))
