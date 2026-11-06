"""Local course recovery, assembly and hashing. No source data are copied."""
from pathlib import Path
import json, hashlib, sys
R=Path(__file__).resolve().parent
def read(p): return json.loads((R/p).read_text(encoding='utf-8'))
def write(p,x): (R/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256((R/p).read_bytes()).hexdigest()
packet=read('input-contract.json')
if sys.argv[1]=='init':
    assert not (R/'manifest.json').exists(), 'Existing recovery state must be verified, not replaced.'
    specs=[('course-map','course-map','course-map.md',[])]+[(f'lesson-{i:02}', 'lesson',f'lesson-{i:02}.md',['course-map'] if i==1 else [f'lesson-{i-1:02}']) for i in range(1,8)]+[('terminology','terminology','terminology.md',['lesson-07']),('teacher-guide','teacher-guide','teacher-guide.md',['lesson-07']),('capstone','capstone','capstone.md',['lesson-07']),('sources','supplement','sources.md',[]),('verification','supplement','verification.json',['lesson-07']),('verify-script','supplement','verify.py',[]),('manager','supplement','manage.py',[]),('amendments','supplement','amendments.json',[]),('assembly','assembly','course.md',[f'lesson-{i:02}' for i in range(1,8)]),('audit','audit','audit_report.json',['assembly','capstone'])]
    cps=[dict(id=i,kind=k,path=p,dependencies=d,status='pending',summary='Awaiting authoring and verification',sha256=None) for i,k,p,d in specs]
    m=dict(schema_version='1.0',topic=packet['topic'],audience=packet['audience'],assumptions=packet['assumptions'],ordered_deliverables=[x['path'] for x in cps]+['completion_report.json'],checkpoints=cps,dependencies={x['id']:x['dependencies'] for x in cps},course_order=[f'lesson-{i:02}' for i in range(1,8)],assembly=dict(path='course.md',section_ids=[f'lesson-{i:02}' for i in range(1,8)]),audit_counts=dict(critical=0,major=0,minor=0),blockers=[],next_action='Read exact sources and author lesson-01')
    write('manifest.json',m)
    write('audit_report.json',dict(status='pending',findings=[],unresolved_counts=m['audit_counts']))
    write('completion_report.json',dict(status='in_progress',topic=m['topic']))
    for p in ['course-map.md','terminology.md']+[f'lesson-{i:02}.md' for i in range(1,8)]: (R/p).write_text('# Pending authoring\n',encoding='utf-8')
    write('amendments.json',packet['applied_audit_amendments'])
elif sys.argv[1]=='checkpoint':
    m=read('manifest.json')
    for ident in sys.argv[2:]:
        c=next(c for c in m['checkpoints'] if c['id']==ident)
        c.update(status='drafted',sha256=digest(c['path']),summary='Complete draft saved; independent verification pending')
    m['next_action']='Continue dependency-ordered authoring and audit'
    write('manifest.json',m)
elif sys.argv[1]=='assemble':
    m=read('manifest.json')
    s='# '+m['topic']+'\n\nStudent course · 11 core periods and 2 capstone periods of 55 minutes.\n\n'
    for ident in m['course_order']:
        s+=f'<!-- BEGIN: {ident} -->\n'+(R/(ident+'.md')).read_text(encoding='utf-8').rstrip('\n')+f'\n<!-- END: {ident} -->\n\n'
    (R/'course.md').write_text(s,encoding='utf-8')
elif sys.argv[1]=='finalize':
    m=read('manifest.json'); a=read('audit_report.json')
    assert a['status']=='passed'
    for c in m['checkpoints']:
        c.update(status='passed',sha256=digest(c['path']),summary='Authored and checked; see audit_report.json and verification.json')
    m.update(audit_counts=a['unresolved_counts'],blockers=[],next_action='none')
    write('manifest.json',m)
    write('completion_report.json',dict(status='complete',topic=m['topic'],audience=m['audience'],assumptions=m['assumptions'],outputs=m['ordered_deliverables'],audit_counts=m['audit_counts'],hashes={p:digest(p) for p in m['ordered_deliverables'] if p!='completion_report.json'}|{'manifest.json':digest('manifest.json')},source_gaps=['AUD-002 global formula-DAG repair and fresh formal compiler replay are not certified; finite course computations are independently replayed.'],validator='Run validate_project_course.py after finalization; external exit result is authoritative.'))
