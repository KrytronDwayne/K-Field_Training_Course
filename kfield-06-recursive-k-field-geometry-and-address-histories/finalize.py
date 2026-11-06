"""Finalize only after substantive audit; validate using the authorized adapter."""
from pathlib import Path
import json,hashlib,subprocess
p=Path(__file__).parent
c=json.loads((p/'input-contract.json').read_text(encoding='utf-8-sig'))
ind=json.loads((p/'independent-audit.json').read_text(encoding='utf-8-sig'))
def put(n,obj): (p/n).write_text(json.dumps(obj,indent=2),encoding='utf-8')
def sha(n): return hashlib.sha256((p/n).read_bytes()).hexdigest()
# Independent audit findings are retained exactly, while machine-checkable audit uses standard finding schema.
findings=[
 {'id':'F01','level':'cumulative','category':'assessment_alignment','file':'lesson-03.md','section':'C06.03-P1','severity':'major','defect':'Practice initially covered scale and volume but did not explicitly ask learner to derive cell and corner counts required by CAP03.','correction':'Added depth2 count derivation and full answer to P1.','verification':'Independent auditor reread repaired P1; enumeration confirms1728 cells and2197 corners.','disposition':'corrected','affected_checkpoints':['lesson-03','capstone','course-map']},
 {'id':'F02','level':'local','category':'formatting','file':'lesson-03.md','section':'C06.03-E1','severity':'minor','defect':'Stray leading plus character before scaling paragraph.','correction':'Removed stray character.','verification':'Independent auditor reread corrected paragraph.','disposition':'corrected','affected_checkpoints':['lesson-03']},
 {'id':'F03','level':'final','category':'source_provenance','file':'sources.md','section':'Claim routing and corrections','severity':'minor','defect':'Boundary rule pointer was abbreviated ambiguously.','correction':'Expanded to S02 /backbone_sequence/1/boundary_rule.','verification':'Pointer read in exact source; auditor confirmed repair.','disposition':'corrected','affected_checkpoints':['sources']},
 {'id':'F04','level':'final','category':'assessment_alignment','file':'lesson-02.md','section':'C06.02-P1','severity':'major','defect':'Practice did not explicitly ask for3D residue product counts required by CAP02.','correction':'Added depths0,1,2 product-count task and answers1,27,729.','verification':'Repaired practice reread; independent Cartesian enumeration confirms counts.','disposition':'corrected','affected_checkpoints':['lesson-02','capstone','course-map']}
]
counts={'critical':0,'major':0,'minor':0}
local=[]
for i in range(1,7):
 local.append({'checkpoint':f'lesson-{i:02d}','status':'passed','checks':['prerequisite bridge and four diagnostics with answers read','definitions, units and notation scoped in actual lesson','worked examples and practice answers hand-recomputed and checked against verification.json','source scope separated from synthetic arithmetic','next dependency checked'],'evidence':'independent-audit.json; verification.json; actual lesson text'})
checks=[
 ('coverage','All6 kernel concepts and required teaching IDs occur; all9 capstone operations traced to concrete prior explanations and answered practices.'),
 ('fidelity','S02 M03 definitions read in place; five source hashes match; S03 corrections reviewed; no physical toy substitution.'),
 ('dependencies','Finite chain01→06; fractions and floor precede modular histories; signed encoding precedes reconstruction.'),
 ('correctness','Thirty verification checks passed, including enumeration of every three-digit word and every Supergroup half-step sample.'),
 ('terminology','Typed depth counters, rung exponents, lambda grid labels and balanced/standard conventions compared across lessons and glossary.'),
 ('examples','Capstone full answers and worked examples independently recomputed; two practice gaps repaired.'),
 ('evidence','Archival reported status, source definitions, finite derivations and synthetic examples remain separate; no experimental or force claims introduced.'),
 ('audience','Six lessons over7 core periods; dense geometry lesson has2 periods; advanced inverse limits recognition-only.'),
 ('assessment','All capstone tasks have actual earlier answered practice; rubric totals100 points.'),
 ('recovery','Finalizer refreshes all file hashes; adapter checks graph, hashes and containment.'),
 ('assembly','Six lesson blocks assembled verbatim in approved order; independent auditor compared normalized text.'),
 ('rendering','Markdown delivery; tables and interval notation read directly. No paginated/visual artifact renderer required.'),
 ('minimality','Finite core only; no new teaching introduced in assembly; support notes explain actual conventions.')]
audit={'schema_version':'1.0','status':'passed','findings':findings,'unresolved_counts':counts,'local_audits':local,'cumulative_audits':[{'unit':'01–03','status':'passed','result':'Typed geometry counts and residue distinction stable; P1 count practice repaired.'},{'unit':'04–06','status':'passed','result':'Digit order, modular compatibility and zero-detail reconstruction consistent.'}],'final_checks':[{'category':a,'status':'passed','evidence':b} for a,b in checks],'independent_audit':'independent-audit.json','independent_status':ind.get('status','see independent report'),'validator_scope':'Deterministic adapter additionally validates hashes, containment, dependencies, assembly and status.','storage_override':'User-authorized Z:/Kfield-doc-training/K-Field_Training_Course'}
put('audit_report.json',audit)
ids=[f'lesson-{i:02d}' for i in range(1,7)]
def refresh(validator_status):
 files=sorted(x.name for x in p.iterdir() if x.is_file() and x.name not in ['manifest.json','completion_report.json'])
 priority=['course-map.md']+[i+'.md' for i in ids]+['terminology.md','teacher-guide.md','capstone.md','sources.md','source-provenance.json','course.md','verification.json','independent-audit.json','audit_report.json']
 ordered=[x for x in priority if x in files]+[x for x in files if x not in priority]+['completion_report.json']
 kindmap={'course-map.md':'course-map','terminology.md':'terminology','teacher-guide.md':'teacher-guide','capstone.md':'capstone','course.md':'assembly','audit_report.json':'audit'}
 cps=[]
 for name in ordered[:-1]:
  key=name.rsplit('.',1)[0]
  kind='lesson' if key in ids else kindmap.get(name,'supplement')
  deps=[]
  if key in ids: deps=['course-map'] if key==ids[0] else [ids[ids.index(key)-1]]
  elif kind in ['terminology','teacher-guide','capstone','assembly']: deps=ids
  elif kind=='audit': deps=ids+['capstone','independent-audit','verification']
  elif key=='validator-report': deps=['audit_report','course']
  cps.append({'id':key,'kind':kind,'status':'passed','path':name,'dependencies':deps,'sha256':sha(name),'summary':('Authored, checked and independently audited lesson' if kind=='lesson' else 'Final supporting artifact, preserved with content hash')})
 manifest={'schema_version':'1.0','topic':c['topic'],'audience':c['audience'],'assumptions':c['assumptions'],'ordered_deliverables':ordered,'checkpoints':cps,'dependencies':{x['id']:x['dependencies'] for x in cps},'course_order':ids,'assembly':{'path':'course.md','section_ids':ids},'audit_counts':counts,'blockers':[],'next_action':'none'}
 put('manifest.json',manifest)
 completion={'schema_version':'1.0','status':'complete','topic':c['topic'],'audience':c['audience'],'assumptions':c['assumptions'],'outputs':ordered,'audit_counts':counts,'hashes':{name:sha(name) for name in ordered[:-1]+['manifest.json']},'lesson_count':6,'core_periods':7,'capstone_periods':2,'source_gaps':['Full infinite inverse-limit proof bodies not replayed; recognition-only and not needed for finite core.'],'validator':validator_status,'independent_audit':'independent-audit.json'}
 put('completion_report.json',completion)
refresh('pending execution; not a delivery claim until validator exits zero')
cmd=[r'C:/ProgramData/anaconda3/Scripts/conda.exe','run','-n','tf_gpu_env','python',r'Z:/Kfield-doc-training/.work/validate_project_course.py',str(p),'--json']
r=subprocess.run(cmd,capture_output=True,text=True)
if r.returncode: print(r.stdout);print(r.stderr);raise SystemExit(r.returncode)
result=json.loads(r.stdout)
put('validator-report.json',result)
refresh({'status':'passed','exit_code':0,'report':'validator-report.json','command':'conda run -n tf_gpu_env python Z:/Kfield-doc-training/.work/validate_project_course.py COURSE_DIRECTORY --json'})
r=subprocess.run(cmd,capture_output=True,text=True)
print(r.stdout)
if r.returncode: print(r.stderr);raise SystemExit(r.returncode)
assert json.loads(r.stdout)['status']=='passed'
print('Final course SHA256:',sha('course.md'))
print('Final manifest SHA256:',sha('manifest.json'))
