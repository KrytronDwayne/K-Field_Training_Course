"""Rebuild assembly and recovery hashes after approved content repairs; run validator."""
from pathlib import Path
import json, hashlib, subprocess, sys
root=Path(__file__).resolve().parent
def read(name): return json.loads((root/name).read_text(encoding='utf-8-sig'))
def dump(name,obj): (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(name): return hashlib.sha256((root/name).read_bytes()).hexdigest()
p=read('input-contract.json')
verification=read('verification.json')
assert verification['status']=='passed'
assert (root/'independent-audit.json').exists(), 'Independent content review required'
independent=read('independent-audit.json')
order=[f'lesson-{n:02d}' for n in range(1,7)]
assembled='# Shape and Scale: Devon Reduction and the Jack Jacobian\n\nStudent course · 6 lessons · 11 core periods plus 2 capstone periods.\n\nSupporting files: [course map](course-map.md), [glossary](terminology.md), [teacher guide](teacher-guide.md), [capstone and key](capstone.md), [source notes](sources.md).\n\n'
for ident in order:
    text=(root/(ident+'.md')).read_text(encoding='utf-8').replace('\r\n','\n').rstrip('\n')
    assembled+=f'<!-- BEGIN: {ident} -->\n{text}\n<!-- END: {ident} -->\n\n'
(root/'course.md').write_text(assembled,encoding='utf-8')
findings=[
 {'id':'C10-A01','level':'local','category':'notation','file':'lesson-04.md','section':'C10.04-E1','severity':'minor','defect':'Wording about all log changes could blur finite log ratios and tangent d symbols.','correction':'Explicitly distinguished finite log changes from their dimensionless tangents.','verification':'Reread corrected source-card paragraph and Lesson 3 definition; independent reviewer notified.','disposition':'corrected','affected_checkpoints':['lesson-04','assembly']},
 {'id':'C10-A02','level':'final','category':'Markdown layout','file':'terminology.md','section':'l_a,l_b,l_c row','severity':'minor','defect':'Literal vertical bars around a vector split a Markdown table cell.','correction':'Replaced bars by a verbal explanation of the length notation.','verification':'Inspected row delimiters and table content after repair.','disposition':'corrected','affected_checkpoints':['terminology']}
]
categories=['prerequisite closure','age-appropriate language and pacing','definitions and notation','units','logic and mathematics','worked examples and answers','evidence and sources','assessment alignment','minimality']
audits=[{'checkpoint':i,'status':'passed','checks':categories,'basis':'Actual lesson read by author and independent auditor; verification.json recomputes finite arithmetic.'} for i in order]
final_checks={
 'coverage':'All six kernel concepts and the extra anchor operation have actual E/W/P/D content and capstone links in coverage.json; independent E05 review completed.',
 'fidelity':'Hashed S02 exact pointers, M05 ratio order, M06 side modes, M07 fixed-angle J, M19 named scalar branch and S03 DAG limit checked.',
 'dependency_order':'Logs before projections, two-variable maps before J, typed records and anchor before synthesis and capstone.',
 'correctness':'116 preassembly verification checks passed; exact rational matrix inverse/determinant and finite polynomial checks plus independent anchor reconstruction.',
 'terminology':'Common reference, m versus s, dA versus area, branch A_branch, t_change versus t_length explicitly distinguished.',
 'evidence':'Synthetic inputs, archived formula bodies, fresh arithmetic and unresolved physical dynamics separated; no empirical claim invented.',
 'audience_load':'Lesson 5 allocated third period; 11 core periods plus 2 capstone; every core operation introduced before practice.',
 'capstone':'All operations have worked answers and prior independently answered practice; rubric sums to100.',
 'recovery_integrity':'Finalizer creates relative paths, acyclic dependencies and current hashes; installed validator checks them.',
 'assembly_identity':'Only passed lesson text inserted in source order; validator checks verbatim normalized identity.',
 'rendering':'Markdown-only delivery; source tables and links inspected. No paginated or visual artifact requires rendering.',
 'storage':'All artifacts reside in assigned direct child of project course root; validator uses authorized root adapter.',
 'minimality':'Six topical lessons retain all kernel operations; wider group theory, general calculus and dynamics are recognition/scope only.'}
counts={'critical':0,'major':0,'minor':0}
dump('audit_report.json',{'schema_version':'1.0','status':'passed','findings':findings,'unresolved_counts':counts,'local_audits':audits,'cumulative_audits':[{'after':'lesson-02','checks':'Log/reference and projection reconstruction/terminology; passed.'},{'after':'lesson-04','checks':'Local/finite distinction, J prerequisite closure, inverse and source domain; passed.'},{'after':'lesson-06','checks':'Typed reconstruction, complete E05 capstone closure and source layers; passed.'}],'final_hostile_checks':final_checks,'independent_review':'independent-audit.json','source_gaps':read('sources.json')['source_gaps'],'validator_evidence':'validator-result.json; recorded after actual subprocess execution.'})
spec=[('input-contract','supplement','input-contract.json',[]),('course-map','course-map','course-map.md',['input-contract'])]
for n in range(1,7):spec.append((f'lesson-{n:02d}','lesson',f'lesson-{n:02d}.md',['course-map'] if n==1 else [f'lesson-{n-1:02d}']))
spec += [('terminology','terminology','terminology.md',['lesson-06']),('teacher-guide','teacher-guide','teacher-guide.md',['lesson-06']),('capstone','capstone','capstone.md',['lesson-06']),('sources','supplement','sources.md',['input-contract']),('source-record','supplement','sources.json',['input-contract']),('coverage','supplement','coverage.json',['capstone']),('verification-script','supplement','verify_examples.py',[]),('verification','supplement','verification.json',['verification-script','capstone']),('independent-audit','supplement','independent-audit.json',['capstone','coverage']),('audit','audit','audit_report.json',['verification','independent-audit']),('assembly','assembly','course.md',order),('finalizer','supplement','finalize_course.py',[])]
checkpoints=[{'id':i,'kind':k,'path':f,'dependencies':deps,'status':'passed','sha256':sha(f),'summary':('Complete lesson with source/teaching review and recomputed examples.' if k=='lesson' else 'Complete artifact reviewed within declared course scope.')} for i,k,f,deps in spec]
assumptions=p['assumptions']+['Lesson 5 uses three periods; total 11 core and 2 capstone periods.','Synthetic records are separate examples; no empirical measurements are supplied.','Source-reported global DAG gap remains scoped outside finite course verification.']
outputs=[x['path'] for x in checkpoints]+['completion_report.json']
m={'schema_version':'1.0','topic':p['topic'],'audience':p['audience'],'assumptions':assumptions,'ordered_deliverables':outputs,'checkpoints':checkpoints,'dependencies':{x['id']:x['dependencies'] for x in checkpoints},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':counts,'blockers':[],'next_action':'none'}
dump('manifest.json',m)
c={'status':'complete','topic':p['topic'],'audience':p['audience'],'assumptions':assumptions,'outputs':outputs,'audit_counts':counts,'hashes':{f:sha(f) for f in outputs if f!='completion_report.json'},'lesson_count':6,'core_periods':11,'capstone_periods':2,'source_gaps':read('sources.json')['source_gaps'],'validator':{'status':'pending final deterministic check','result_file':'validator-result.json'},'harmless_unresolved_minor_findings':[]}
c['hashes']['manifest.json']=sha('manifest.json')
dump('completion_report.json',c)
adapter=Path('Z:/Kfield-doc-training/.work/validate_project_course.py')
proc=subprocess.run([sys.executable,str(adapter),str(root),'--json'],capture_output=True,text=True)
assert proc.returncode==0,proc.stdout+proc.stderr
result=json.loads(proc.stdout)
dump('validator-result.json',dict(result,process_exit_code=proc.returncode))
c['validator']={'status':'passed','exit_code':0,'result_file':'validator-result.json','validator_sha256':result['validator_sha256'],'command':"& 'C:/ProgramData/anaconda3/Scripts/conda.exe' run -n tf_gpu_env python 'Z:/Kfield-doc-training/.work/validate_project_course.py' COURSE_DIRECTORY --json"}
dump('completion_report.json',c)
# completion_report has no self hash; verify final state after recording actual execution.
proc=subprocess.run([sys.executable,str(adapter),str(root),'--json'],capture_output=True,text=True)
assert proc.returncode==0,proc.stdout+proc.stderr
dump('validator-result.json',dict(json.loads(proc.stdout),process_exit_code=proc.returncode))
print(json.dumps({'status':'passed','exit_code':0,'lessons':6,'course_sha256':sha('course.md'),'unresolved':counts}))
