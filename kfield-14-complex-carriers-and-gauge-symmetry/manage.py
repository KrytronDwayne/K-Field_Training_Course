import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(path,text): (ROOT/path).write_text(text.rstrip()+'\n',encoding='utf-8')
def dump(path,obj): write(path,json.dumps(obj,indent=2,ensure_ascii=False))
def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def initialize():
    if (ROOT/'manifest.json').exists():
        m=json.loads((ROOT/'manifest.json').read_text())
        for c in m['checkpoints']:
            if c.get('sha256'): assert sha(c['path'])==c['sha256'],c['id']
        return
    specs=[('map','course-map','course-map.md',[])]+[(f'lesson-{n:02}','lesson',f'lesson-{n:02}.md',['map'] if n==1 else [f'lesson-{n-1:02}']) for n in range(1,8)]+[('terms','terminology','terminology.md',['lesson-07']),('teacher','teacher-guide','teacher-guide.md',['lesson-07']),('capstone','capstone','capstone.md',['lesson-07']),('sources','supplement','sources.md',[]),('verification','supplement','verification.json',['lesson-07']),('assembly','assembly','course.md',[f'lesson-{n:02}' for n in range(1,8)]),('audit','audit','audit_report.json',['assembly','capstone'])]
    cps=[dict(id=i,kind=k,path=p,dependencies=d,status='pending',summary='Awaiting authored content and checks') for i,k,p,d in specs]
    for c in cps:
        if c['path'].endswith('.md'): write(c['path'],'# Pending: '+c['id'])
    dump('audit_report.json',dict(status='pending',findings=[],unresolved_counts=dict(critical=0,major=0,minor=0)))
    dump('completion_report.json',dict(status='in_progress'))
    dump('manifest.json',dict(schema_version='1.0',topic=packet['topic'],audience=packet['audience'],assumptions=packet['assumptions'],ordered_deliverables=[c['path'] for c in cps]+['completion_report.json'],checkpoints=cps,dependencies={c['id']:c['dependencies'] for c in cps},course_order=[f'lesson-{n:02}' for n in range(1,8)],assembly=dict(path='course.md',section_ids=[f'lesson-{n:02}' for n in range(1,8)]),audit_counts=dict(critical=0,major=0,minor=0),blockers=[],next_action='Author lessons from verified sources'))
if __name__=='__main__': initialize()
