"""Assemble passed authored content, refresh recovery hashes, run project validator."""
from pathlib import Path
import json,hashlib,subprocess,sys
R=Path(__file__).resolve().parent
def load(n): return json.loads((R/n).read_text(encoding='utf-8-sig'))
def save(n,obj): (R/n).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(n): return hashlib.sha256((R/n).read_bytes()).hexdigest()
p=load('input-contract.json')
independent=load('independent-audit.json')
assert independent['unresolved_critical']==0 and independent['unresolved_major']==0 and independent['unresolved_minor']==0, 'Independent repairs must be verified first'
verification=load('worked-example-verification.json')
assert verification['status']=='passed'
order=[f'lesson-{i:02}' for i in range(1,8)]
assembled='# Action, Topology, and Phase Closure\n\nStudent course — seven lessons, nine core periods. See capstone.md for the three-period assessment, teacher-guide.md for instruction, and sources.md for exact provenance.\n\n'
for ident in order:
    body=(R/(ident+'.md')).read_text(encoding='utf-8').rstrip('\n')
    assembled+=f'<!-- BEGIN: {ident} -->\n{body}\n<!-- END: {ident} -->\n\n'
(R/'course.md').write_text(assembled,encoding='utf-8')
findings=[
 {'id':'IA-01','level':'local','category':'definition','file':'lesson-05.md','section':'C19.05-E1','severity':'minor','defect':'Linearity was described with scalar compatibility alone.','correction':'Added additivity and explained which rule is used in rebasing.','verification':'Independent auditor reread correction; finite rebase computations unchanged and passed.','disposition':'corrected','affected_checkpoints':['lesson-05','assembly']},
 {'id':'IA-02','level':'final','category':'assessment_alignment','file':'lesson-01.md; lesson-07.md','section':'C19.01-P1; C19.07-P1','severity':'major','defect':'Capstone source-term identification and five-role classification were taught but lacked their own mapped answered practice.','correction':'Added answered source-reading and premise-classification mini-items to the existing P1 sections.','verification':'Independent auditor verified actual new practice content against CAP-01/CAP-07; IDs preserved.','disposition':'corrected','affected_checkpoints':['lesson-01','lesson-07','capstone','assembly']}
]
counts={'critical':0,'major':0,'minor':0}
checks=[
 {'scope':'local','items':order,'result':'Each lesson checked for prerequisites, audience, definitions, notation, units, logic, math, evidence, sources and diagnostic alignment; independent audit records exact checks.'},
 {'scope':'cumulative','items':['lesson-02','lesson-05','lesson-07'],'result':'Units 01–02,03–05,06–07 checked for stable notation, dependency order, growing complexity and capstone coverage. Action S versus line S_total, time tau versus map tau, and three C uses remain separated.'},
 {'scope':'final coverage/E05','result':'All seven concepts have actual E1/W1/P1/D1 content and capstone operations; source-reading and five-role practice gaps repaired.'},
 {'scope':'final fidelity','result':'S02 M15 and S03 AUD-009 exact text compared. Four source action terms, six factors, tau, charge contract, retained state inputs and missing replay gap preserved. No global theorem or empirical source replay claimed.'},
 {'scope':'final numerical','result':f"{verification['check_count']} independent exact computation/content/hash checks passed, including direct/grouped action sums, vector reconstruction, inverse frames, factor deletion, basis compensation and two pairing routes."},
 {'scope':'final evidence/minimality','result':'Synthetic examples, source facts, reported claims and unresolved inputs separated; no source snapshots, observations, invented mechanisms, physical probabilities or discarded residuals. Recognition-only notation is not required numerical computation.'},
 {'scope':'final audience/assessment','result':'Seven lessons over nine core periods plus three capstone periods; actual worked answers and 100-point rubric checked. No calculus or untaught matrix computation required.'},
 {'scope':'final assembly/storage/rendering','result':'Markdown only; checked heading/table structure. Assembly contains lessons verbatim in declared order. All persistent outputs resolve inside this course directory; no PDF/Word rendering applies.'},
 {'scope':'recovery integrity','result':'All listed checkpoint hashes generated from written bytes; installed validator via approved root adapter checks integrity, order, complete statuses, audit counts and containment.'}
]
audit={'schema_version':'1.0','status':'passed','findings':findings,'unresolved_counts':counts,'corrected_counts':{'critical':0,'major':1,'minor':1},'checks':checks,'independent_audit':'independent-audit.json','verification':'worked-example-verification.json'}
save('audit_report.json',audit)
specs=[('course-map','course-map','course-map.md',[])]
for i,ident in enumerate(order): specs.append((ident,'lesson',ident+'.md',['course-map'] if i==0 else [order[i-1]]))
specs += [
 ('terminology','terminology','terminology.md',order),
 ('teacher-guide','teacher-guide','teacher-guide.md',order),
 ('capstone','capstone','capstone.md',order),
 ('sources','supplement','sources.md',[]),
 ('input-contract','supplement','input-contract.json',[]),
 ('launch-prompt','supplement','launch-prompt.md',['input-contract']),
 ('verification-script','supplement','verify_examples.py',order),
 ('worked-verification','supplement','worked-example-verification.json',['verification-script']),
 ('authoring-script','supplement','build_course.py',['input-contract']),
 ('finalization-script','supplement','finalize_course.py',[]),
 ('independent-audit','supplement','independent-audit.json',order+['capstone','sources','teacher-guide']),
 ('assembly','assembly','course.md',order),
 ('audit','audit','audit_report.json',['independent-audit','worked-verification','assembly'])]
cps=[{'id':i,'kind':k,'path':path,'dependencies':deps,'status':'passed','summary':f'Checked {k}: {path}','sha256':sha(path)} for i,k,path,deps in specs]
outputs=[x['path'] for x in cps]+['completion_report.json']
assumptions=p['assumptions']+['All finite numerical packets, AU/TU units and two-sector domains are synthetic teaching declarations.','Source missing replay objects remain source-reported gaps; full source action and global closure are not assigned computations.','User authorized the project output directory instead of Desktop; seven lessons retain nine core periods plus three capstone periods.']
manifest={'schema_version':'1.0','topic':p['topic'],'audience':p['audience'],'assumptions':assumptions,'course_output_directory':str(R),'ordered_deliverables':outputs,'checkpoints':cps,'dependencies':{x['id']:x['dependencies'] for x in cps},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':counts,'blockers':[],'next_action':'none'}
save('manifest.json',manifest)
completion={'schema_version':'1.0','status':'complete','topic':p['topic'],'audience':p['audience'],'assumptions':assumptions,'outputs':outputs,'audit_counts':counts,'hashes':{n:sha(n) for n in outputs if n!='completion_report.json'},'lesson_count':7,'core_periods':9,'capstone_periods':3,'source_gaps':['Full source topology carriers and determinant-line replay objects; typed operator/coefficient and boundary-sector values; time/action normalization. These do not block the declared finite core.'],'validator':{'status':'pending_final_invocation'}}
completion['hashes']['manifest.json']=sha('manifest.json')
save('completion_report.json',completion)
command=[sys.executable,str(R.parents[1]/'.work'/'validate_project_course.py'),str(R),'--json']
run=subprocess.run(command,text=True,capture_output=True)
result=json.loads(run.stdout)
assert run.returncode==0,result
completion['validator']={'status':'passed','exit_code':run.returncode,'validator_path':result['validator_path'],'validator_sha256':result['validator_sha256'],'adapter':str(R.parents[1]/'.work'/'validate_project_course.py'),'checks':result['checks']}
save('completion_report.json',completion)
final=subprocess.run(command,text=True,capture_output=True)
assert final.returncode==0,final.stdout+final.stderr
print(final.stdout)
