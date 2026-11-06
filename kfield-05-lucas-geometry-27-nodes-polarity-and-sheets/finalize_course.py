"""Refresh recovery, verbatim assembly, and audit from completed reviewed artifacts."""
from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,o): (R/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
c=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
v=json.loads((R/'verification.json').read_text(encoding='utf-8'))
ia=json.loads((R/'independent-audit.json').read_text(encoding='utf-8-sig'))
assert v['status']=='passed'
assert ia['unresolved_critical']==ia['unresolved_major']==0
for name,digest in ia['reviewed_sha256'].items(): assert sha(R/name)==digest,name
order=[f'lesson-{i:02}' for i in range(1,7)]
intro='''# Lucas Geometry: 27 Nodes, Polarity, and Sheets

A complete short course for high-school seniors: six 55-minute core lessons and two capstone periods. Read lessons in order. Numerical work uses a declared classroom analogue; source definitions and freshly derived finite results are distinguished throughout.

[Course map](course-map.md) · [Terminology](terminology.md) · [Capstone and full answer key](capstone.md) · [Teacher guide](teacher-guide.md) · [Source notes](sources.md) · [Complete worked registry](registry.md)

The following six lessons are assembled verbatim from their separately audited files.
'''
assembly=intro
for name in order:
    body=(R/(name+'.md')).read_text(encoding='utf-8').rstrip('\n')
    assembly+='\n<!-- BEGIN: '+name+' -->\n'+body+'\n<!-- END: '+name+' -->\n'
(R/'course.md').write_text(assembly,encoding='utf-8')
# Markdown link and table integrity checks; no paginated rendering was requested.
link_count=0
for p in R.glob('*.md'):
    if p.name=='launch-prompt.md': continue
    text=p.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if '://' in target or target.startswith('#'): continue
        assert (p.parent/target.split('#')[0]).is_file(),(p.name,target)
        link_count+=1
    table_width=None
    for line in text.splitlines():
        if line.startswith('|') and line.endswith('|'):
            width=line.count('|')
            if table_width is None: table_width=width
            assert width==table_width,(p.name,line)
        else: table_width=None

counts={'critical':0,'major':0,'minor':0}
findings=[{'id':'F-01','level':'local','category':'source_fidelity','file':'sources.md','section':'SA-05 and S02 /backbone_sequence/2/proof/0','severity':'major','defect':'The inspected source defines p=O_K+B L/2 but prints g_lambda dot p=lambda/2, omitting the origin term. Direct use at nonzero origin gives the wrong value.','correction':'Applied the approved SA-05 correction g_lambda dot (p-O_K)=lambda/2 throughout Lessons 2-4 and capstone; retained the printed-source discrepancy in provenance. No source mutation.','verification':'For L=(1,-1,1), corrected value 1/2; uncorrected value 7/6 differs by g dot O=2/3. All 27 affine residuals are exactly zero in verification.json.','disposition':'corrected','affected_checkpoints':['lesson-02','lesson-03','lesson-04','capstone','sources']}]
checks=[]
for i in range(1,7):
    checks.append({'id':f'LOCAL-{i:02}','level':'local','checkpoint':f'lesson-{i:02}','categories':['prerequisite','audience','definition','notation','unit','logic','mathematics','evidence','source','assessment'],'result':'passed','evidence':'Manager authored/reviewed complete text and answers; independent-audit.json confirms actual teaching and mathematical checks against hashed lesson text. Exact finite values and required IDs checked in verification.json.'})
checks += [
 {'id':'UNIT-I','level':'cumulative','result':'passed','evidence':'Lessons 1-2: enumeration precedes mapping; L, q, p, z and u are introduced separately; boundary and inverse tasks have answered practice.'},
 {'id':'UNIT-II','level':'cumulative','result':'passed','evidence':'Lessons 3-4: dot product introduced before use; seven sheets precede two polarity and three remainder partitions; negatives handled explicitly; no complex exponential prerequisite.'},
 {'id':'UNIT-III','level':'cumulative','result':'passed','evidence':'Lessons 5-6: canonical representative and s introduced before registry use; all 27 rows retained; owner residual and inverse discrepancy distinguished; capstone operations have prior worked and independently answered practice.'},
 {'id':'FINAL-COVERAGE','level':'final','result':'passed','evidence':'Independent auditor accepted completed E05 content and all seven capstone mappings; six required concepts and mod-three bridge have actual E/W/P/D sections.'},
 {'id':'FINAL-MATH','level':'final','result':'passed','evidence':'Independent Fraction read-back checks all 27 rows, 13 pairs, sheet/parity/remainder/geometric counts and inverse identities. Auditor independently checked all 54 rendered-as-Markdown table rows against JSON.'},
 {'id':'FINAL-SOURCE','level':'final','result':'passed','evidence':'Five source hashes matched. S02 M02/M03 inspected in place; source status labels remain reports. Synthetic geometry and source Cell3 are explicitly separated; no historical numerical branch used as active constant.'},
 {'id':'FINAL-LOAD','level':'final','result':'passed','evidence':'Every lesson has four diagnostic checks, three goals, one essential question, worked answers and a bridge. Six 55-minute budgets plus two capstone periods; matrix inverse transpose is recognition-only. Pacing is estimated, not empirically classroom-tested.'},
 {'id':'FINAL-RETENTION','level':'final','result':'passed','evidence':'All original synthetic rows retained. v plus s reconstructs noncentral L; center separate; z plus u reconstructs q; R_L retained in each row. Deliberate failed comparison and repair explained.'},
 {'id':'FINAL-MARKDOWN','level':'final','result':'passed','evidence':f'Manager read complete registry tables; {link_count} relative links resolve; every Markdown table has consistent cell counts. No PDF, Word or paginated output requested.'},
 {'id':'FINAL-ASSEMBLY','level':'final','result':'passed','evidence':'Assembly constructed from unchanged lesson bytes with exact checkpoint marker order; deterministic validator checks identity and hashes separately.'},
 {'id':'FINAL-MINIMALITY','level':'final','result':'passed','evidence':'Six lessons follow approved finite dependency chain; no new teaching in assembly, no source snapshots, no advanced recognition-only work assessed, no missing registry rows.'}]
dump('audit_report.json',{'schema_version':'1.0','status':'passed','findings':findings,'unresolved_counts':counts,'corrected_counts':{'critical':0,'major':1,'minor':0},'checks':checks,'independent_audit':'independent-audit.json','verification':'verification.json','limitations':['Pacing has not been classroom-tested.','No broader mature corpus or integration proof replay is claimed.','Deterministic validator result is recorded in completion_report.json after execution.']})

specs=[('course-map','course-map','course-map.md',[],'Prerequisites, coverage IDs and lesson order'),('sources','supplement','sources.md',[],'Compact source provenance and affine correction'),('source-pins','supplement','sources.json',['sources'],'Five verified SHA-256 pins and exact pointers')]
for i,name in enumerate(order): specs.append((name,'lesson',name+'.md',['course-map','sources'] if i==0 else [order[i-1],'sources'],'Complete student lesson with worked answers and local checks'))
specs += [
 ('terminology','terminology','terminology.md',order,'Terms and units used in actual lessons'),
 ('teacher-guide','teacher-guide','teacher-guide.md',order,'Pacing, diagnosis, cumulative checks and maintenance'),
 ('registry','supplement','registry.md',['lesson-06'],'Complete human-readable 27-row worked answer'),
 ('registry-json','supplement','registry.json',['lesson-06'],'Small exact synthetic registry with all residuals'),
 ('capstone','capstone','capstone.md',['lesson-06','registry'],'Seven operations, full key and 100-point rubric'),
 ('verification-script','supplement','verify_examples.py',['registry-json'],'Independent finite arithmetic and source-pin read-back checks'),
 ('verification','supplement','verification.json',['verification-script'],'Actual passed exact arithmetic and ID-check record'),
 ('independent-audit','supplement','independent-audit.json',order+['capstone','registry'],'Independent completed-content E05 and mathematical review'),
 ('initial-authoring','supplement','build_course.py',[],'Initial authored draft source; do not rerun over later lesson repairs'),
 ('support-builder','supplement','finish_course.py',['initial-authoring'],'Rebuild synthetic registry and course supports'),
 ('finalizer','supplement','finalize_course.py',[],'Recovery and verbatim assembly refresh procedure'),
 ('assembly','assembly','course.md',order,'Every lesson inserted verbatim in approved order'),
 ('audit','audit','audit_report.json',['independent-audit','verification','assembly'],'Final hostile review and corrected source finding')]
checkpoints=[{'id':i,'kind':k,'path':p,'dependencies':deps,'status':'passed','sha256':sha(R/p),'summary':s} for i,k,p,deps,s in specs]
outputs=[x['path'] for x in checkpoints]+['completion_report.json']
assumptions=c['assumptions']+['Classroom basis from approved teaching blueprint is used for all numerical examples; it is not Cell3 or measured data.','Pacing is a design estimate; no student classroom trial was performed.']
manifest={'schema_version':'1.0','topic':c['topic'],'audience':c['audience'],'assumptions':assumptions,'ordered_deliverables':outputs,'checkpoints':checkpoints,'dependencies':{x['id']:x['dependencies'] for x in checkpoints},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':counts,'blockers':[],'next_action':'none','course_output_directory':str(R),'storage_authority':'User-approved project output root overrides Desktop default','input_contract_sha256':sha(R/'input-contract.json')}
dump('manifest.json',manifest)
completion={'status':'complete','topic':c['topic'],'audience':c['audience'],'assumptions':assumptions,'outputs':outputs,'audit_counts':counts,'hashes':{p:sha(R/p) for p in outputs if p!='completion_report.json'},'lesson_count':6,'core_periods':6,'capstone_periods':2,'source_gaps':[],'scope_limitations':['No broader proof corpus replay; finite core definitions and operations are fully available.'],'validator':{'status':'pending_final_execution','command':'conda run -n tf_gpu_env python Z:/Kfield-doc-training/.work/validate_project_course.py COURSE_DIRECTORY --json'},'completion_note':'Course content is complete; delivery success requires the subsequent deterministic validator exit zero.'}
completion['hashes']['manifest.json']=sha(R/'manifest.json')
dump('completion_report.json',completion)
print('Reviewed artifacts hashed; verbatim assembly and recovery records refreshed. Run deterministic validator next.')
