"""Finalize only after content audit; run validator separately after this script."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent
def read(n): return json.loads((ROOT/n).read_text(encoding='utf-8-sig'))
def write(n,x): (ROOT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(n): return hashlib.sha256((ROOT/n).read_bytes()).hexdigest()
findings=[
dict(id='F16-001',level='local',category='definition',file='lesson-03.md',section='Bridge',severity='minor',defect='Two weak slots wording could imply bidegree (0,2).',correction='Changed to two available weak basis directions and degree (0,1).',verification='Independent auditor reread actual repair; consistent with lesson-01 H type.',disposition='corrected',affected_checkpoints=['lesson-03','assembly']),
dict(id='F16-002',level='final',category='E05 prerequisite practice',file='lesson-02.md',section='C16.02-P2',severity='major',defect='Capstone required general covariance argument but prior practice only answered finite phase cases.',correction='Added explicit covector-evaluation and determinant argument prompt and full practice answer.',verification='Independent auditor reread repaired P2; evaluation cancellation and top-form reasoning taught in E2 and answered before CAP-02.',disposition='corrected',affected_checkpoints=['lesson-02','capstone','assembly','map']),
dict(id='F16-003',level='final',category='E05 prerequisite practice',file='lesson-07.md',section='C16.07-P1',severity='major',defect='Capstone required integration-scope sentence but P1 did not independently practice that source-card operation.',correction='Added source-scope comparison prompt and worked answer after the source card.',verification='Independent auditor reread repaired P1; source card is provided before answer and CAP-07 operation has answered prior practice.',disposition='corrected',affected_checkpoints=['lesson-07','capstone','assembly','map']),
dict(id='F16-004',level='cumulative',category='terminology',file='terminology.md',section='diag(a,b), I row',severity='minor',defect='First-use column listed lesson 3 although diagonal notation occurs in lesson 2.',correction='Split first-use entry into lesson 2 five-slot diag and lesson 3 two-slot diag/I.',verification='Actual glossary row checked against lesson-02 E2 and lesson-03 E1.',disposition='corrected',affected_checkpoints=['glossary'])]
verification=read('worked-example-verification.json')
assert verification['status']=='passed' and all(x['passed'] for x in verification['checks'])
m=read('manifest.json')
order=m['course_order']
assembled=(ROOT/'course.md').read_text(encoding='utf-8')
positions=[]
for ident in order:
    begin=f'<!-- BEGIN: {ident} -->\n'; end=f'\n<!-- END: {ident} -->'
    assert assembled.count(begin)==assembled.count(end)==1
    start=assembled.index(begin); finish=assembled.index(end,start)
    assert assembled[start+len(begin):finish]==(ROOT/(ident+'.md')).read_text(encoding='utf-8').rstrip('\n')
    positions.append(start)
assert positions==sorted(positions)
counts={'critical':0,'major':0,'minor':0}
audit=dict(schema_version='1.0',status='passed',findings=findings,unresolved_counts=counts,
    corrected_counts={'critical':0,'major':2,'minor':2},
    independent_review={'reviewer':'/root/independent_audit','scope':'Read actual lessons 1–7, teaching anchors, capstone, terminology and teacher guide; independently recomputed arithmetic and read exact S02 pointers; repairs reread.','result':'No unresolved critical or major teaching/math findings after E05 repairs.','fresh_source_hash':'S02 SHA-256 verified independently; author verified all five supplied sources.','compiler_execution':False},
    local_checks=[{'checkpoint':i,'checks':['prerequisite bridge','2–4 observable goals','one essential question','worked example and answered practice','3–5 answered diagnostics','notation and units','evidence/source scope','next dependency'],'result':'passed by actual content review; arithmetic independently checked in worked-example-verification.json'} for i in order],
    cumulative_checks=[{'boundary':'after lesson-02','result':'Sector Q distinct from Q_electric; q/Y_h and vector/dual types stable; four interfaces practiced; phase operations taught locally.'},{'boundary':'after lesson-05','result':'Mass and squared-mass units distinct; rho denominator excluded; Y_h/Y_Yuk separated; swap has inverse and preserves both coordinate maps.'},{'boundary':'after lesson-07','result':'Every capstone operation has earlier explanation and answered practice, including added covariance and integration-scope practice. Residual and endpoint preservation carried into contract.'}],
    final_hostile_checks={
        'coverage':'Seven kernel concepts, all required E/W/P/D IDs and seven capstone steps present; ID existence checked by script, operation meaning by independent reviewer.',
        'fidelity':'Source M12 requires M11; definitions and formula order match exact S02 records. Compiler integration scope remains separate; physical inputs unfilled.',
        'dependency_order':'Sequential seven-lesson chain; complex phase, contraction, matrix, unit and domain bridges precede use.',
        'correctness':f"{len(verification['checks'])} scripted checks passed: inversion counts, contraction signs, exact rational mass/energy algebra, map composition and source hashes; independent manual recomputation agrees.",
        'terminology':'Actual glossary reviewed against lesson usage; ambiguous slot wording and first-use row corrected.',
        'evidence':'No empirical data invented; synthetic examples labeled; source reports distinct from finite replay and proposed observations; no full kinetic-term or compiler proof claimed.',
        'audience':'12 core periods with explicit teaching/practice/check allocations; no general Lie theory, variational calculation or diagonalization assessed.',
        'assessment':'100-point rubric recomputed; all seven tasks have named input/output and taught/answered prior practice; two initial E05 gaps corrected.',
        'recovery':'All deliverable checkpoint paths relative; SHA-256 refreshed after content repairs; canonical project root explicitly user authorized.',
        'assembly':'Seven marker pairs uniquely present; exact normalized lesson identity and order asserted by this script; no new substantive assembly content.',
        'rendering':'Markdown only. Tables, headings and links inspected as text; paginated rendering not applicable.',
        'minimality':'Each lesson supplies instruction, finite example, independent practice and diagnostics; recognition-only boundaries do not become hidden assessed tasks.'},
    limitations=['Deterministic validator establishes storage/hash/assembly/audit consistency, not substantive truth by itself.','No formal compiler typecheck or real-world parameter inference performed.'])
write('audit_report.json',audit)
extra={'id':'finalize-script','kind':'supplement','path':'finalize_records.py','dependencies':[],'status':'passed','sha256':sha('finalize_records.py'),'summary':'Refresh audited completion and hashes; validator runs separately.'}
if not any(c['id']==extra['id'] for c in m['checkpoints']):
    m['checkpoints'].append(extra)
    m['ordered_deliverables'].insert(-1,extra['path'])
for c in m['checkpoints']:
    c['sha256']=sha(c['path']); c['status']='passed'
m['dependencies']={c['id']:c['dependencies'] for c in m['checkpoints']}
m['audit_counts']=counts; m['blockers']=[]; m['next_action']='none'
write('manifest.json',m)
completion=dict(schema_version='1.0',status='complete',topic=m['topic'],audience=m['audience'],assumptions=m['assumptions'],outputs=m['ordered_deliverables'],audit_counts=counts,
    hashes={name:sha(name) for name in m['ordered_deliverables'] if name!='completion_report.json'},
    lesson_count=7,core_periods=12,capstone_periods=3,period_minutes=55,
    source_gaps=read('sources.json')['source_gaps'],
    validator={'status':'pending_external_run','command':"& 'C:/ProgramData/anaconda3/Scripts/conda.exe' run -n tf_gpu_env python 'Z:/Kfield-doc-training/.work/validate_project_course.py' 'Z:/Kfield-doc-training/K-Field_Training_Course/kfield-16-higgs-yukawa-and-interaction-interfaces' --json"},
    harmless_unresolved_minor_findings=[])
completion['hashes']['manifest.json']=sha('manifest.json')
write('completion_report.json',completion)
print(json.dumps({'content_audit':'passed','lessons':7,'unresolved':counts,'next_required_action':'Run actual project validator and record its result before reporting success.'}))
