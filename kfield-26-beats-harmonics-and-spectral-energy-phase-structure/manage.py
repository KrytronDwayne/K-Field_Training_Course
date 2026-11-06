from pathlib import Path
import json, hashlib, sys
ROOT=Path(__file__).resolve().parent
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def write(p,o): (ROOT/p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
packet=read('input-contract.json')
if not (ROOT/'manifest.json').exists():
    cps=[dict(id='course-map',kind='course-map',path='course-map.md',dependencies=[],status='pending',summary='Coverage and dependency map')]
    for i,l in enumerate(packet['course_map']):
        cps.append(dict(id=l['id'],kind='lesson',path=l['id']+'.md',dependencies=['course-map' if i==0 else packet['course_map'][i-1]['id']],status='pending',summary=l['title']))
        (ROOT/(l['id']+'.md')).write_text('# '+l['title']+'\n\nPending authoring.\n',encoding='utf-8')
    for name,kind in [('terminology','terminology'),('teacher-guide','teacher-guide'),('capstone','capstone'),('course','assembly'),('sources','supplement'),('verification','supplement'),('audit_report','audit')]:
        ext='.json' if name in ['verification','audit_report'] else '.md'
        cps.append(dict(id=name,kind=kind,path=name+ext,dependencies=['lesson-08'],status='pending',summary=name))
    m=dict(schema_version='1.0',topic=packet['topic'],audience=packet['audience'],assumptions=packet['assumptions'],ordered_deliverables=[c['path'] for c in cps]+['completion_report.json'],checkpoints=cps,dependencies={c['id']:c['dependencies'] for c in cps},course_order=[l['id'] for l in packet['course_map']],assembly=dict(path='course.md',section_ids=[l['id'] for l in packet['course_map']]),audit_counts=dict(critical=0,major=0,minor=0),blockers=[],next_action='Author lesson-01 and verify source contracts')
    write('manifest.json',m)
    write('audit_report.json',dict(status='pending',findings=[],unresolved_counts=m['audit_counts']))
    write('completion_report.json',dict(status='in_progress',topic=packet['topic']))
    for p in ['course-map.md','terminology.md']: (ROOT/p).write_text('# '+p[:-3]+'\n\nInitialized; pending authoring.\n',encoding='utf-8')
    print('Recovery authorities initialized')
else:
    m=read('manifest.json')
    for c in m['checkpoints']:
        if c['status']=='passed': assert digest(c['path'])==c['sha256'], c['id']
    print('Existing passed checkpoint hashes verified')
