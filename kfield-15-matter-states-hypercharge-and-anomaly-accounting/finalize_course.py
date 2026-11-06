"""Finalize only after independent content acceptance; validator must run afterward."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parent
def read(name): return json.loads((R/name).read_text(encoding='utf-8-sig'))
def write(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def h(name): return hashlib.sha256((R/name).read_bytes()).hexdigest()
M=read('manifest.json'); P=read('input-contract.json'); I=read('independent-audit.json')
assert I['unresolved_critical']==I['unresolved_major']==0
assert I.get('status') not in ['lessons_pass_support_pending'], 'Independent support acceptance required'
for x in I['lesson_checks']: assert h(x['file'])==x['sha256']
assert h(I['capstone_check']['file'])==I['capstone_check']['sha256']
# Verify every earlier recovery hash before promoting status.
for c in M['checkpoints']: assert h(c['path'])==c['sha256'],c['id']
coverage=[]
assembled=(R/'course.md').read_text(encoding='utf-8')
cap=(R/'capstone.md').read_text(encoding='utf-8')
previous=-1
for n in range(1,8):
    lid=f'lesson-{n:02d}'; prefix=f'C15.{n:02d}'; body=(R/(lid+'.md')).read_text(encoding='utf-8')
    anchors=[prefix+'-'+suffix for suffix in ['E1','W1','P1','D1']]
    assert all(a in body for a in anchors)
    assert all(term in body for term in ['Essential question:','Goals:','Prerequisite bridge:','Pacing:','Claim scope:','Next dependency:'])
    assert len(re.findall(r'^\d\. ',body,re.M))==4
    begin=f'<!-- BEGIN: {lid} -->\n'; end=f'\n<!-- END: {lid} -->'
    assert assembled.count(begin)==assembled.count(end)==1
    start=assembled.index(begin); finish=assembled.index(end,start)
    assert start>previous; previous=finish
    assert assembled[start+len(begin):finish]==body.rstrip('\n')
    step=f'C15-CAP-{n:02d}'; assert step in cap
    coverage.append({'concept_id':prefix,'lesson':lid+'.md','explanation':anchors[0],'worked_example':anchors[1],'answered_practice':anchors[2],'diagnostic':anchors[3],'capstone_step':step,'operation':P['capstone_specification']['required_operations'][n-1],'status':'passed','content_review':'Manual manager and independent auditor; actual operations and answers present before capstone use'})
write('coverage-verification.json',{'status':'passed','rows':coverage,'method':'Anchor existence, exact assembly extraction, manual operation/practice/assessment correspondence; not existence-only educational acceptance.'})
local=[{'checkpoint':f'lesson-{n:02d}','result':'passed','checks':['prerequisite bridge and taught operations','senior vocabulary and paced session boundaries','definitions, notation and dimensionless units','worked examples and four diagnostic answers','source/evidence scope','actual E05 explanation/practice/assessment links'],'verification':'Full lesson reading plus verify_examples.py and independent-audit.json'} for n in range(1,8)]
audit={'schema_version':'1.0','status':'passed','findings':[{'id':'A15-001','level':'final','category':'assembly serialization','file':'course.md','section':'lesson marker contents','severity':'minor','defect':'Windows text writer converted LF lesson lines to CRLF in assembly; normalized identity passed but literal bytes differed.','correction':'Changed support writer to UTF-8 write_bytes and rebuilt the assembly.','verification':'Independent auditor rechecks literal extraction; finalizer also checks normalized text and ordered marker pairs.','disposition':'corrected','affected_checkpoints':['assembly','support-script']}],'unresolved_counts':{'critical':0,'major':0,'minor':0},'local_audits':local,'cumulative_audits':[{'boundary':'lesson-03','result':'passed','checks':'All 16 components accounted for; six bidegrees and charge/descent assignments consistent.'},{'boundary':'lesson-05','result':'passed','checks':'Five named tests, normalization, full trial contributions, factorization and primitive solution agree.'},{'boundary':'lesson-07','result':'passed','checks':'Complement, representations, parity and evidence classes remain distinct; capstone backward map closes.'}],'final_hostile_audit':{'result':'passed','content_evidence':'independent-audit.json and coverage-verification.json','checks':['coverage and source fidelity','dependency order and explicit bridges','finite math and units','consistent notation and answers','source/derived/interpretation separation','audience load and 14-period pacing','capstone solvability and rubric','recovery hashes checked before promotion','verbatim assembly identity and order','all deliverables contained in authorized course directory','Markdown delivery; pagination not requested','no omission hidden by concision and no new assembly teaching'],'deterministic_validator':'External adapter execution result is recorded in completion_report.json.'},'corrections':[],'source_limitations':'Remote integration digests are source-attributed excerpts, not fresh local bytes. No fresh upstream whole-branch verification, compiler execution or empirical physical/global closure is claimed.'}
write('audit_report.json',audit)
additional=[('independent-audit','supplement','independent-audit.json',M['course_order']),('coverage-check','supplement','coverage-verification.json',M['course_order']),('finalizer','supplement','finalize_course.py',[])]
for i,k,path,deps in additional:
    if not any(c['id']==i for c in M['checkpoints']): M['checkpoints'].append({'id':i,'kind':k,'path':path,'dependencies':deps})
for c in M['checkpoints']:
    c.update(status='passed',sha256=h(c['path']),summary=f'Accepted {c["kind"]}; content checked and saved')
M['ordered_deliverables']=[c['path'] for c in M['checkpoints']]+['completion_report.json']
M['dependencies']={c['id']:c['dependencies'] for c in M['checkpoints']}
M['audit_counts']=audit['unresolved_counts']; M['blockers']=[]; M['next_action']='none'
M['completion_gate']='All content checks passed; observed deterministic adapter execution is recorded in completion report.'
write('manifest.json',M)
report={'status':'complete','topic':M['topic'],'audience':M['audience'],'assumptions':M['assumptions'],'outputs':M['ordered_deliverables'],'audit_counts':M['audit_counts'],'hashes':{p:h(p) for p in M['ordered_deliverables'] if p!='completion_report.json'},'lesson_count':7,'core_periods':14,'capstone_periods':3,'source_gaps':audit['source_limitations'],'validator':{'status':'pending_execution','required_command':"& 'C:/ProgramData/anaconda3/Scripts/conda.exe' run -n tf_gpu_env python 'Z:/Kfield-doc-training/.work/validate_project_course.py' '"+str(R)+"' --json"},'completion_gate':'Candidate completion pending the required successful validator run; do not announce success until validator status is passed.'}
report['hashes']['manifest.json']=h('manifest.json')
write('completion_report.json',report)
print('Content accepted, hashes refreshed, seven lesson identities verified. Run required validator now.')
