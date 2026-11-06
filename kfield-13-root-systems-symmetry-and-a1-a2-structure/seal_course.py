"""Seal the completed, reviewed course and run the unchanged project-root validator."""
from pathlib import Path
import hashlib,json,subprocess,sys
D=Path(__file__).resolve().parent
p=json.loads((D/'input-contract.json').read_text(encoding='utf-8-sig'))
def sha(name):return hashlib.sha256((D/name).read_bytes()).hexdigest()
def dump(name,o):(D/name).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
counts={'critical':0,'major':0,'minor':0}
findings=[]
def finding(i,severity,file,section,defect,correction,verification,affected):
    findings.append(dict(id=i,level='final',category='teaching precision and coverage',file=file,section=section,severity=severity,defect=defect,correction=correction,verification=verification,disposition='corrected',affected_checkpoints=affected))
finding('C13-F01','major','lesson-03.md','C13.03-P1','Drawing was explained and capstone-assessed but not explicitly required in prior practice.','Added a drawing instruction and checkable coordinates for all six tips.','Independent auditor reread actual repaired files and confirmed E05 closure; squared drawing distances checked exactly.',['lesson-03','capstone','assembly'])
finding('C13-F02','minor','lesson-05.md','C13.05-E1','Positive rescaling convention needed explicit distinction from ordinary unoriented projective coordinates.','Declared positive-scale oriented-ray convention and separate sign handling.','Independent source and lesson reread confirmed repair.',['lesson-05','assembly'])
finding('C13-F03','minor','lesson-06.md','C13.06-P1','Matrix construction taught but not explicit in the named capstone prior-practice item.','Added matrix-row construction and three row products with q.','Independent auditor reread and confirmed actual E05 repair; outputs 1,2,-3 match coordinate action.',['lesson-06','capstone','assembly'])
finding('C13-F04','minor','lesson-03.md','C13.03-P1','Prompt requested norm while answer provided squared norm.','Changed prompt to squared norm.','Author reread patched prompt; answer 2 matches dot product, while length would be square root of 2.',['lesson-03','assembly'])
checks=[
{'level':'local','scope':'lessons 01–06','method':'Author and independent auditor read essential question, 3 observable goals, bridge, explanation, example, answered practice, four diagnostics and next dependency; recomputed all numeric keys.','result':'passed'},
{'level':'cumulative','scope':'unit I: lessons 01–02','method':'Checked composition versus translation, sum versus norm invariants, equal parity inverse halves, negative remainders and retained k.','result':'passed'},
{'level':'cumulative','scope':'unit II: lessons 03–04','method':'Checked plane/lattice/root distinctions, Euclidean metric scope, Cartan convention, coordinate reconstruction and three-channel versus three-class distinction.','result':'passed'},
{'level':'cumulative','scope':'unit III: lessons 05–06','method':'Checked address counts versus primitive channels, ray/sign/family/detector separation, retained digit/scale, matrix and intertwiner carrier scopes.','result':'passed'},
{'level':'final','scope':'coverage and E05','method':'Read actual explanations and answered practice against six capstone panels; all 42 lesson item IDs and six capstone IDs mechanically present. Drawing and matrix practice repaired.','result':'passed'},
{'level':'final','scope':'source fidelity','method':'Fresh SHA-256 on all five supplied sources; exact S02 M09 and formula pointers read. Kept archival branch status and supplied integration provenance separately scoped.','result':'passed'},
{'level':'final','scope':'mathematical correctness','method':'verify_examples.py exact Fraction arithmetic and finite enumeration; independent auditor hand recomputation; symbolic proofs retained in lessons.','result':'passed'},
{'level':'final','scope':'audience and minimality','method':'Checked senior prerequisite closure, nine-period plan, first-principles operations, no advanced compiler/physical proof hidden in core assessment, four diagnostics per lesson.','result':'passed'},
{'level':'final','scope':'evidence and residual information','method':'Checked source facts/finite derivations/synthetic examples/unresolved identification labels; quotient displacement, mean, digit, ray scale and original vector retained. No measured data imported.','result':'passed'},
{'level':'final','scope':'assembly and Markdown','method':'Rebuilt verbatim marker sections; checked plain Markdown tables, headings and links. No paginated visual deliverable requested; no render claim. Machine identity/containment checks performed by validator.','result':'passed'}]
audit={'schema_version':'1.0','status':'passed','findings':findings,'unresolved_counts':counts,'checks':checks,'independent_review':{'agent':'independent_audit','scope':'Six lessons, capstone, teacher guide, sources, terminology and map','final_report':'E05 repairs confirmed; zero critical or major, one norm-wording minor subsequently patched and rechecked by author.','fresh_typecheck':False}}
dump('audit_report.json',audit)
order=[f'lesson-{i:02}' for i in range(1,7)]
cp=[]
def checkpoint(id,kind,path,deps,summary):cp.append(dict(id=id,kind=kind,path=path,dependencies=deps,summary=summary,status='passed',sha256=sha(path)))
checkpoint('input','supplement','input-contract.json',[],'Authoritative approved packet, preserved unchanged')
checkpoint('source-verification','supplement','source-verification.json',['input'],'Five archival hashes freshly verified')
checkpoint('sources','supplement','sources.md',['source-verification'],'Exact pointers and evidence boundaries')
checkpoint('course-map','course-map','course-map.md',['input','sources'],'Six-lesson order, E05 coverage, concrete capstone operations')
for i,id in enumerate(order):checkpoint(id,'lesson',id+'.md',['course-map'] if i==0 else [order[i-1]],'Complete senior-facing lesson; local and independent content audit passed')
checkpoint('terminology','terminology','terminology.md',order,'Actual notation and typed distinctions')
checkpoint('teacher-guide','teacher-guide','teacher-guide.md',order,'Nine-period pacing, repairs, cumulative gates')
checkpoint('capstone','capstone','capstone.md',order,'Six panels, full key, 60-point rubric and backward map')
checkpoint('verification-code','supplement','verify_examples.py',order,'Reproducible exact finite verification')
checkpoint('verification','supplement','worked-example-verification.json',['verification-code'],'Passed exact computation in required tf_gpu_env')
checkpoint('author-code','supplement','author_course.py',['input'],'Authored lesson recovery source; do not rerun passed work absent a concrete defect')
checkpoint('assembly-code','supplement','finalize_course.py',['input'],'Assembly/provenance recovery script')
checkpoint('seal-code','supplement','seal_course.py',['input'],'Hashes, audit closure and project validator runner')
checkpoint('assembly','assembly','course.md',order,'All six lessons verbatim in approved order')
checkpoint('audit','audit','audit_report.json',['assembly','verification','sources','capstone','teacher-guide','terminology'],'Hostile content review and four documented repaired findings')
outputs=[c['path'] for c in cp]+['completion_report.json']
manifest={'schema_version':'1.0','topic':p['topic'],'audience':p['audience'],'assumptions':p['assumptions'],'ordered_deliverables':outputs,'checkpoints':cp,'dependencies':{c['id']:c['dependencies'] for c in cp},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':counts,'blockers':[],'next_action':'none','course_output_directory':str(D),'storage_authority':p['storage_override'],'recovery_rule':'Verify checkpoint bytes against hashes before trusting status. Resume earliest missing/failed dependency; regenerate passed work only for a concrete defect.'}
dump('manifest.json',manifest)
completion={'status':'complete','topic':p['topic'],'audience':p['audience'],'assumptions':p['assumptions'],'outputs':outputs,'audit_counts':counts,'hashes':{n:sha(n) for n in outputs if n!='completion_report.json'}|{'manifest.json':sha('manifest.json')},'lesson_count':6,'core_periods':9,'capstone_periods':2,'source_gaps':'None for finite core. Full compiler execution, physical identification, and integration local-byte reauthentication are outside the verified scope and not assessed.','validator':{'status':'pending_final_execution','result_file':'validator-result.json'}}
dump('completion_report.json',completion)
cmd=[sys.executable,'Z:/Kfield-doc-training/.work/validate_project_course.py',str(D),'--json']
r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
assert r.returncode==0,r.stdout+r.stderr
result=json.loads(r.stdout)
dump('validator-result.json',result)
completion['validator']={'status':'passed','exit_code':0,'result_file':'validator-result.json','validator_sha256':result['validator_sha256']}
dump('completion_report.json',completion)
# Re-run after completion result is saved: completion is intentionally not self-hashed.
r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
assert r.returncode==0,r.stdout+r.stderr
dump('validator-result.json',json.loads(r.stdout))
print(r.stdout)
print('course.md SHA-256 '+sha('course.md'))
