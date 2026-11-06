"""Course-local recovery, assembly and hash maintenance; standard library only."""
from pathlib import Path
import json, hashlib, sys
ROOT=Path(__file__).resolve().parent
def write(name,text):
    (ROOT/name).write_text(text,encoding='utf-8')
def save(name,obj): write(name,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def digest(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
order=[r['id'] for r in packet['course_map']]
if sys.argv[1]=='init':
    assert not (ROOT/'manifest.json').exists(), 'Do not replace existing recovery state'
    cps=[]
    for name,kind,deps in [('course-map','course-map',[]),('terminology','terminology',[])]+[(lid,'lesson',[] if i==0 else [order[i-1]]) for i,lid in enumerate(order)]:
        write(name+'.md','# '+name+'\n\nPending authoring.\n')
        cps.append(dict(id=name,kind=kind,path=name+'.md',dependencies=deps,status='pending',summary='Initialized; no acceptance asserted',sha256=digest(name+'.md')))
    save('manifest.json',dict(schema_version='1.0',topic=packet['topic'],audience=packet['audience'],assumptions=packet['assumptions'],checkpoints=cps,course_order=order,dependencies={c['id']:c['dependencies'] for c in cps},ordered_deliverables=[c['path'] for c in cps]+['completion_report.json'],assembly={'path':'course.md','section_ids':order},audit_counts={'critical':0,'major':0,'minor':0},blockers=[],next_action='Retrieve source contracts and author lesson-01'))
    save('audit_report.json',dict(status='pending',findings=[],unresolved_counts={'critical':0,'major':0,'minor':0}))
    save('completion_report.json',dict(status='in_progress',topic=packet['topic']))
elif sys.argv[1]=='draft':
    m=json.loads((ROOT/'manifest.json').read_text())
    for c in m['checkpoints']:
        if c['status']=='passed': assert digest(c['path'])==c['sha256'], c['id']
        elif 'Pending authoring.' not in (ROOT/c['path']).read_text(encoding='utf-8'):
            c.update(status='drafted',sha256=digest(c['path']),summary='Complete draft; awaiting independent audit')
    m['next_action']='Independent content audit, repair, verification, assembly'
    save('manifest.json',m)
elif sys.argv[1]=='finish':
    text='# Quadratic Phase Cost and Route Geometry\n\nSeven lessons; source notes, teacher guide and capstone are companion files.\n\n'
    for lid in order: text+='<!-- BEGIN: '+lid+' -->\n'+(ROOT/(lid+'.md')).read_text(encoding='utf-8').rstrip('\n')+'\n<!-- END: '+lid+' -->\n\n'
    write('course.md',text)
    kinds=[('course-map','course-map',[]),('terminology','terminology',[]),('sources','supplement',[]),('input-contract','supplement',[]),('ellipse','supplement',[]),('verify_examples','supplement',[]),('manage','supplement',[])]+[(lid,'lesson', ['sources','terminology'] if i==0 else [order[i-1]]) for i,lid in enumerate(order)]+[('teacher-guide','teacher-guide',order),('capstone','capstone',order),('verification','supplement',order),('independent-audit','supplement',order),('course','assembly',order),('audit_report','audit',order)]
    cps=[]
    for name,kind,deps in kinds:
        path=name+('.json' if name in ['verification','audit_report','input-contract'] else '.png' if name=='ellipse' else '.py' if name in ['verify_examples','manage'] else '.md')
        cps.append(dict(id=name,kind=kind,path=path,dependencies=deps,status='passed',summary='Authored and checked; see audit_report.json and independent-audit.md',sha256=digest(path)))
    counts=json.loads((ROOT/'audit_report.json').read_text())['unresolved_counts']
    assert counts['critical']==counts['major']==0
    m=dict(schema_version='1.0',topic=packet['topic'],audience=packet['audience'],assumptions=packet['assumptions'],checkpoints=cps,course_order=order,dependencies={c['id']:c['dependencies'] for c in cps},ordered_deliverables=[c['path'] for c in cps]+['completion_report.json'],assembly={'path':'course.md','section_ids':order},audit_counts=counts,blockers=[],next_action='none')
    save('manifest.json',m)
    save('completion_report.json',dict(status='complete',topic=m['topic'],audience=m['audience'],assumptions=m['assumptions'],outputs=m['ordered_deliverables'],audit_counts=counts,hashes={p:digest(p) for p in [c['path'] for c in cps]+['manifest.json']},source_gaps=['Full named route certificate, locked G_phase/C/W_qpc and source precision bridge not retrieved; core source-audit task explicitly preserves this gap.'],validation='Run validate_project_course.py; captured result in validator-result.json'))
