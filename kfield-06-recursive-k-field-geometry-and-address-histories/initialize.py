from pathlib import Path
import json,hashlib,sys
print(sys.executable)
p=Path(r'Z:/Kfield-doc-training/K-Field_Training_Course/kfield-06-recursive-k-field-geometry-and-address-histories')
if (p/'manifest.json').exists():
    raise SystemExit('Recovery state already exists; inspect manifest and hashes rather than reinitialize.')
c=json.loads((p/'input-contract.json').read_text(encoding='utf-8-sig'))
def put(n,x): (p/n).write_text(json.dumps(x,indent=2) if isinstance(x,dict) else x,encoding='utf-8')
ids=[x['id'] for x in c['course_map']]
cp=[dict(id=i,kind='lesson',status='pending',path=i+'.md',dependencies=ids[max(0,k-1):k],summary='Awaiting authored lesson') for k,i in enumerate(ids)]
put('manifest.json',dict(schema_version='1.0',topic=c['topic'],audience=c['audience'],assumptions=c['assumptions'],checkpoints=cp,course_order=ids,blockers=[],next_action='Verify sources and author lesson-01'))
put('course-map.md','# Course map\n\nDrafting from approved input contract.\n')
put('terminology.md','# Terminology\n\nDefinitions will be populated from actual lessons.\n')
put('audit_report.json',dict(status='pending',findings=[],unresolved_counts=dict(critical=0,major=0,minor=0)))
put('completion_report.json',dict(status='in_progress',topic=c['topic']))
for i in ids: put(i+'.md','# '+i+'\n\nPending.\n')
for s in c['sources']:
 q=Path(s['path']); b=q.read_bytes(); print(s['id'],len(b),hashlib.sha256(b).hexdigest(),hashlib.sha256(b).hexdigest()==s['sha256'])
 x=json.loads(b)
 print('ROOT KEYS',list(x))
 if s['id']=='S02':
  for k in ['backbone_sequence','supergroup_uniqueness']:
   z=x[k]; print(k,json.dumps(z[1:3] if k=='backbone_sequence' else z,indent=2))
print('L1',json.dumps(c['course_map'][0],indent=2))
