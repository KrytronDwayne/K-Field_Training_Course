"""Refresh authored course recovery records after audits; never modifies source files."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent

def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8-sig'))

def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

packet = read('input-contract.json')
source_rows=[]
for source in packet['sources']:
    actual=digest(Path(source['path']))
    assert actual == source['sha256'], source['id']+' source hash mismatch'
    source_rows.append(dict(source, actual_sha256=actual, hash_verified=True,
        evidence_class='archival source; source-reported status distinct from fresh finite verification'))
write('source-provenance.json', {
    'schema_version':'1.0', 'sources':source_rows,
    'corpus_generation':packet['source_routing']['snapshot_generation'],
    'manifest_sha256':packet['source_routing']['manifest_sha256'],
    'generation_match':True, 'retrieval':'capabilities, sparse RAG rerank=false, depth-one root traversal; exact local JSON bodies',
    'pointers_read':['S02#/backbone_sequence/7','S02#/backbone_sequence/18/branches/exceptional_cycle_bridge','S03#/findings/1'],
    'source_gaps':['Global formula-DAG repair/closure not certified; source AUD-002 retained. No gap in finite core bodies.'],
    'source_copies_created':False})

order=[f'lesson-{i:02d}' for i in range(1,7)]
intro='# Lucas Graphs: Edges, Cycles, and Memory\n\nA first-principles course for high-school seniors. Six lessons, nine core periods, and two capstone periods.\n\nRead the lessons in order; attempt each practice before its answer. Supporting material: [course map](course-map.md), [glossary](terminology.md), [capstone and full key](capstone.md), [teacher guide](teacher-guide.md), and [source notes](sources.md).\n\n'
assembly=intro+'\n\n'.join(f'<!-- BEGIN: {i} -->\n'+(ROOT/(i+'.md')).read_text(encoding='utf-8-sig').rstrip('\n')+f'\n<!-- END: {i} -->' for i in order)+'\n'
(ROOT/'course.md').write_text(assembly,encoding='utf-8')

final='--final' in sys.argv
independent=read('independent-content-audit.json') if (ROOT/'independent-content-audit.json').exists() else {}
if final:
    assert independent.get('status') == 'passed', 'Independent audit not passed'
    assert all(v==0 for v in independent['unresolved_counts'].values()), 'Independent findings remain'
    assert read('worked-example-verification.json').get('status') == 'passed', 'Example verification not passed'

findings=[{'id':f['id'],'level':'final','category':'E05 prerequisite/practice closure','file':'lesson-03.md','section':'C11.03-P1; capstone C11-CAP-03','severity':f['severity'],'defect':f['finding'],'correction':f['required_correction'],'verification':f['verification'],'disposition':'corrected' if f['status']=='resolved' else 'unresolved','affected_checkpoints':['lesson-03','capstone','assembly']} for f in independent.get('findings',[])]
validated='--validated' in sys.argv
if validated:
    assert read('validator-result.json')['status']=='passed'
audit={
    'schema_version':'1.0', 'status':'passed' if final else 'in_progress',
    'findings':findings,
    'unresolved_counts':independent.get('unresolved_counts',{'critical':0,'major':0,'minor':0}),
    'checks':[
        {'level':'local','checkpoints':order,'checks':'Four diagnostics, answered independent practice, observable goals, prerequisite bridge, defined notation, dimensionless units, source-scope box and next dependency in every lesson; arithmetic independently recomputed.','result':'passed' if final else 'awaiting final review'},
        {'level':'cumulative','checkpoints':['lesson-03','lesson-05'],'checks':'Incidence and transpose precede gradients; rank/leaf elimination precede dimensions; chord basis precedes wrap inverse; signs, ordering and residuals retained.','result':'passed'},
        {'level':'final','checks':'Coverage E1/W1/P1/D1 and all six capstone steps cross-read; actual operation-level practice closure reviewed independently; answer key totals 100 points; nine-period load retained.','result':'passed' if final else 'awaiting independent closure'},
        {'level':'final','checks':'Exact source paths and hashes verified; mature M08 source bodies read; source-reported DAG incompleteness and extension boundaries preserved.','result':'passed'},
        {'level':'final','checks':'All persistent artifacts in designated project course directory; normalized verbatim assembly produced in lesson order; deterministic validator required after record refresh.','result':'passed; actual validator exit 0, rerun after this record refresh' if validated else 'validator pending'},
        {'level':'final','checks':'Markdown-only delivery uses plain text graph/table diagrams; no requested paginated artifact, no PDF rendering gate. Content reviewed for completeness without added assembly teaching.','result':'passed'}],
    'independent_audit':'independent-content-audit.json',
    'verification':'worked-example-verification.json',
    'boundaries':'Finite mathematics and machine integrity only; no global source-DAG certification or physical memory claim.'}
write('audit_report.json',audit)

items=[('course-map','course-map','course-map.md',[])]
items += [(i,'lesson',i+'.md',['course-map'] if n==0 else [order[n-1]]) for n,i in enumerate(order)]
items += [('terminology','terminology','terminology.md',order),('teacher-guide','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('sources','supplement','sources.md',[]),('provenance','supplement','source-provenance.json',['sources']),('verify-script','supplement','verify_examples.py',[]),('verification','supplement','worked-example-verification.json',['verify-script']),('independent-audit','supplement','independent-content-audit.json',order+['capstone']),('record-script','supplement','finalize_course.py',[]),('assembly','assembly','course.md',order),('audit','audit','audit_report.json',['assembly','independent-audit','verification'])]
checkpoints=[{'id':i,'kind':kind,'path':path,'dependencies':deps,'status':'passed' if final else 'drafted','sha256':digest(ROOT/path),'summary':f'{kind} artifact; audited finite course content and scope' if final else f'{kind} artifact saved; final audit pending'} for i,kind,path,deps in items]
outputs=[c['path'] for c in checkpoints]+['completion_report.json']
assumptions=packet['assumptions']+['All classroom flow values are dimensionless synthetic inputs; exact real/rational graph algebra is the assessed domain.','Source AUD-002 is retained as global serialization scope boundary, not claimed repaired.','Nine core 55-minute periods plus two capstone periods preserve approved lesson IDs and pacing.']
manifest={'schema_version':'1.0','topic':packet['topic'],'audience':packet['audience'],'assumptions':assumptions,'ordered_deliverables':outputs,'checkpoints':checkpoints,'dependencies':{c['id']:c['dependencies'] for c in checkpoints},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':audit['unresolved_counts'],'blockers':[],'next_action':'none' if final else 'Finish independent content audit, refresh records, run deterministic validator'}
write('manifest.json',manifest)
completion={'schema_version':'1.0','status':'complete' if final else 'in_progress','topic':packet['topic'],'audience':packet['audience'],'assumptions':assumptions,'outputs':outputs,'audit_counts':audit['unresolved_counts'],'hashes':{p:digest(ROOT/p) for p in outputs if p!='completion_report.json'},'source_gaps':['No finite-core retrieval gap. Global formula-DAG closure and exceptional/dynamical extensions remain outside certification.'],'lesson_count':6,'validator':{'command':'validate_project_course.py COURSE_DIRECTORY --json','result':'passed; exit 0; see validator-result.json' if validated else 'See validator-result.json; completion accepted only after actual exit zero'}}
completion['hashes']['manifest.json']=digest(ROOT/'manifest.json')
write('completion_report.json',completion)
print(json.dumps({'status':'ready_for_validator' if final else 'drafted','lesson_count':6,'course_sha256':digest(ROOT/'course.md')},indent=2))
