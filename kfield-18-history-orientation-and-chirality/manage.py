"""Course recovery and assembly utility; no source content is copied."""
import json, pathlib, hashlib, sys
P=pathlib.Path(__file__).resolve().parent
def read(name): return json.loads((P/name).read_text(encoding='utf-8-sig'))
def save(name,obj): (P/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(name): return hashlib.sha256((P/name).read_bytes()).hexdigest()
C=read('input-contract.json')
items=[('course-map','course-map','course-map.md',[])]+[(r['id'],'lesson',r['id']+'.md',['course-map'] if i==0 else [C['course_map'][i-1]['id']]) for i,r in enumerate(C['course_map'])]+[('terminology','terminology','terminology.md',[]),('sources','supplement','sources.md',[]),('verification','supplement','verification.json',[]),('teacher-guide','teacher-guide','teacher-guide.md',['lesson-07']),('capstone','capstone','capstone.md',['lesson-07']),('assembly','assembly','course.md',[r['id'] for r in C['course_map']]),('audit','audit','audit_report.json',['assembly','capstone'])]
if sys.argv[1]=='init':
 assert not (P/'manifest.json').exists()
 cps=[]
 for id,kind,path,deps in items:
  cps.append(dict(id=id,kind=kind,path=path,dependencies=deps,status='pending',summary='Awaiting authored content and audit'))
  if path.endswith('.md'): (P/path).write_text('# '+id+'\n\nPending production.\n',encoding='utf-8')
 m=dict(schema_version='1.0',topic=C['topic'],audience=C['audience'],assumptions=C['assumptions'],ordered_deliverables=[x[2] for x in items]+['completion_report.json'],checkpoints=cps,dependencies={x['id']:x['dependencies'] for x in cps},course_order=[r['id'] for r in C['course_map']],assembly={'path':'course.md','section_ids':[r['id'] for r in C['course_map']]},audit_counts={'critical':0,'major':0,'minor':0},blockers=[],next_action='Author lessons in dependency order')
 save('manifest.json',m)
 save('audit_report.json',dict(status='pending',findings=[],unresolved_counts=m['audit_counts']))
 save('completion_report.json',dict(status='in_progress',topic=C['topic']))
 print('Initialized recovery authorities.')
elif sys.argv[1]=='draft':
 m=read('manifest.json')
 for cp in m['checkpoints']:
  f=P/cp['path']
  if f.exists() and 'Pending production.' not in f.read_text(encoding='utf-8'):
   cp.update(status='drafted',sha256=sha(cp['path']),summary='Authored; final review pending')
 m['next_action']='Independent audit and numerical verification'
 save('manifest.json',m)
elif sys.argv[1]=='assemble':
 m=read('manifest.json')
 text='# History, Orientation, and Chirality\n\nStudent course. See capstone.md for the synthesis assessment and sources.md for provenance.\n\n'
 for id in m['course_order']:
  text+='<!-- BEGIN: '+id+' -->\n'+(P/(id+'.md')).read_text(encoding='utf-8').rstrip('\n')+'\n<!-- END: '+id+' -->\n\n'
 (P/'course.md').write_text(text,encoding='utf-8')
elif sys.argv[1]=='finalize':
 m=read('manifest.json'); a=read('audit_report.json')
 assert a['status']=='passed' and a['unresolved_counts']['critical']==a['unresolved_counts']['major']==0
 for cp in m['checkpoints']:
  assert (P/cp['path']).is_file()
  cp.update(status='passed',sha256=sha(cp['path']),summary='Content reviewed; calculations, source scope and teaching links verified; see audit_report.json')
 m.update(audit_counts=a['unresolved_counts'],blockers=[],next_action='none')
 save('manifest.json',m)
 save('completion_report.json',dict(status='complete',topic=m['topic'],audience=m['audience'],assumptions=m['assumptions'],outputs=m['ordered_deliverables'],audit_counts=m['audit_counts'],hashes={name:sha(name) for name in m['ordered_deliverables'] if name!='completion_report.json'}|{'manifest.json':sha('manifest.json')},source_gaps=['Source B_8 alphabet and radial T_0 replay definitions remain VERIFIED_NOT_LOADED under S03 AUD-009; finite exercises do not replace them.'],validator='Run project-root adapter after finalization; see validator-result.json'))
 print('Hashes refreshed; validator still required.')
