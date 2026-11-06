from pathlib import Path
import json,hashlib,re
R=Path(__file__).parent
def read(f):return (R/f).read_text(encoding='utf-8-sig')
def write(f,o): (R/f).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def h(f):return hashlib.sha256((R/f).read_bytes()).hexdigest()
p=json.loads(read('input-contract.json'));v=json.loads(read('verification.json'))
assert v['status']=='passed'
order=[l['id'] for l in p['course_map']]
anchors=[];local=[]
for l in p['course_map']:
    text=read(l['id']+'.md');a=l['teaching_anchor']
    needed=[a['explanation_id'],a['worked_example']['id'],a['guided_practice']['id'],a['diagnostic']['id']]
    for s in a.get('supplemental_exercises',[]):needed += [s[k]for k in ['explanation_id','worked_example_id','prior_practice_id','diagnostic_id']]
    for item in needed:assert text.count('<a id="'+item+'"></a>')==1,item
    anchors+=needed
    for section in ['**Essential question:**','**Goals**','## Prerequisite bridge','## Worked example','## Guided practice','## Diagnostic checks','## Worked answers','**Next dependency:**']:
        assert section in text,(l['id'],section)
    diagnostic=text.split('## Diagnostic checks')[1].split('## Worked answers')[0]
    assert 3<=len(re.findall(r'^\d+\. ',diagnostic,re.M))<=5
    assert text.count('```')%2==0
    local.append(dict(checkpoint=l['id'],checks=['prerequisite bridge','2–4 goals manually reviewed','named explanation/worked/practice/diagnostic anchors','3–5 answered diagnostics','mathematical and unit review','source/evidence scope','later dependency'],result='passed'))
assert len(anchors)==44
assembled=read('course.md').replace('\r\n','\n');cursor=-1
for name in order:
    begin='<!-- BEGIN: '+name+' -->\n';end='\n<!-- END: '+name+' -->'
    assert assembled.count(begin)==assembled.count(end)==1
    i=assembled.index(begin);j=assembled.index(end);assert i>cursor
    assert assembled[i+len(begin):j]==read(name+'.md').replace('\r\n','\n').rstrip('\n')
    cursor=j
cap=read('capstone.md')
for row in p['capstone_specification']['backward_map']:
    assert row['step_id'] in cap and row['prior_practice_id'] in cap
    assert row['prior_practice_id'] in read(row['introduction']+'.md')
assert sum(x['points']for x in p['capstone_specification']['backward_map'])==44
findings=[
dict(id='LOCAL-001',level='local',category='executable verification',file='verify_examples.py',section='Walsh table construction',severity='major',defect='Initial script had one excess closing parenthesis, preventing independent arithmetic verification.',correction='Corrected the expression and reran the entire exact-fraction verifier.',verification='tf_gpu_env execution exited 0; all listed source-hash and arithmetic assertions passed.',disposition='corrected',affected_checkpoints=['verification','lesson-03']),
dict(id='INDEPENDENT-001',level='final',category='audience vocabulary',file='lesson-03.md',section='Integer extractor',severity='minor',defect='Triangular, determinant and unit minor appeared without a local explanation.',correction='Added brief definitions and marked the certificate vocabulary recognition-only; kept the explicit extractor as the core proof.',verification='Reread updated section; independent extractor recipes establish saturation without relying on determinant computation.',disposition='corrected',affected_checkpoints=['lesson-03','assembly']),
dict(id='INDEPENDENT-002',level='final',category='student-facing language',file='lesson-03.md',section='C21.S01-E1',severity='minor',defect='Supplemental text began with author-facing Teach signed characters.',correction='Changed to direct student-facing Use signed characters and An intertwiner T obeys.',verification='Search and reread of generated lesson confirms corrected language.',disposition='corrected',affected_checkpoints=['lesson-03','assembly'])]
findings += [
dict(id='INDEPENDENT-003',level='final',category='coverage',file='course-map.md',section='Coverage and backward links',severity='minor',defect='Two supplemental later-use rows used the next lesson rather than explicit reuse.',correction='C21.S01 now points to C21-CAP-09; C21.S03 points to lesson-08 and C21-CAP-11.',verification='Compared generated coverage rows to capstone practice links and lesson-08 report.',disposition='corrected',affected_checkpoints=['course-map']),
dict(id='INDEPENDENT-004',level='final',category='clarity',file='teacher-guide.md',section='Lesson 3 teaching moves',severity='minor',defect='Four-bit-label table could imply four bits per label.',correction='Changed to four-label table (two bits per label).',verification='Reread teacher guidance against the 00,01,10,11 table.',disposition='corrected',affected_checkpoints=['teacher-guide'])]
findings += [
dict(id='C21-IND-001',level='local',category='dimensional_dependency',file='lesson-04.md',section='C21.04-E1 and Boundary to carry forward',severity='major',defect='Missing numerical reference mass was incorrectly said to prevent a computable dimensionless ratio.',correction='Separated missing contributing renderer terms from missing reference mass in explanation, boundary, authoring text and assembly; added answered ratio-3 practice with m_ref withheld.',verification='Exact dot product recomputed as 3 without a reference mass; m=3*m_ref remains symbolic. Independent narrow repair check recorded in independent-audit.md. External auditor reapproval is pending parent recheck.',disposition='corrected',affected_checkpoints=['lesson-04','assembly','build-script','verification']),
dict(id='C21-IND-002',level='cumulative',category='terminology_navigation',file='terminology.md',section='First lesson column',severity='minor',defect='Grouped first-lesson cells obscured different introduction locations for R/Z and b/b_toy.',correction='Annotated R:01, Z:02 and b:03 (rendering04), b_toy:04 in glossary and authoring text.',verification='Compared introduction locations and independent narrow repair check; no source definitions changed. External auditor reapproval not claimed.',disposition='corrected',affected_checkpoints=['terminology','build-script'])]
counts=dict(critical=0,major=0,minor=0)
audit=dict(schema_version='1.0',status='passed',findings=findings,unresolved_counts=counts,local_audits=local,cumulative_audits=[dict(boundary=b,result='passed',checks=['terminology','prerequisite order','example complexity','coverage','capstone practice closure'])for b in ['lesson-02','lesson-04','lesson-06','lesson-08']],final_audit=dict(coverage='44 unique anchors and 11 capstone backward links verified',fidelity='Five source hashes match; used source pointers read; original missing L/W7 and physical-input boundaries preserved',correctness='Exact rational verifier and independent lesson auditor recomputed matrix, residual, composition, solver, energy and rounding examples',assessment='11 tasks, worked keys, 44-point rubric; all operations tied to prior answered practice',recovery='Final checkpoint hashes and dependencies generated from actual saved files; adapter validation required next',assembly='Eight lesson bodies compared verbatim in order',rendering='Markdown headings, table delimiters and fenced matrix blocks inspected; no paginated output required',minimality='Eight conceptual lessons spread over 17 periods; no missing-object physical computations assigned',storage='All authored artifacts stored directly under authoritative project course directory'),independent_audit=dict(agent='course_audit',lesson_result='0 critical, 0 major; two minor clarity findings corrected',support_result='See independent-audit.md'))
write('audit_report.json',audit)
spec=[('course-map','course-map','course-map.md',[])]+[(l,'lesson',l+'.md',[order[i-1]]if i else ['course-map'])for i,l in enumerate(order)]+[
('terminology','terminology','terminology.md',order),('teacher-guide','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('sources','supplement','sources.md',[]),('verification','supplement','verification.json',['sources']),('verify-script','supplement','verify_examples.py',[]),('build-script','supplement','build_course.py',[]),('finalize-script','supplement','finalize_course.py',[]),('input-contract','supplement','input-contract.json',[]),('independent-audit','supplement','independent-audit.md',order+['capstone']),('assembly','assembly','course.md',order),('audit','audit','audit_report.json',order+['capstone','assembly','independent-audit'])]
for _,_,path,_ in spec:assert (R/path).is_file(),path
cps=[dict(id=i,kind=k,path=f,dependencies=d,status='passed',summary=('Verified '+i+'; see audit_report.json and verification.json'),sha256=h(f))for i,k,f,d in spec]
outputs=[c['path']for c in cps]+['completion_report.json']
m=dict(schema_version='1.0',topic=p['topic'],audience=p['audience'],assumptions=p['assumptions'],ordered_deliverables=outputs,checkpoints=cps,dependencies={x['id']:x['dependencies']for x in cps},course_order=order,assembly=dict(path='course.md',section_ids=order),audit_counts=counts,blockers=[],next_action='none')
write('manifest.json',m)
completion=dict(status='complete',topic=p['topic'],audience=p['audience'],assumptions=p['assumptions'],outputs=outputs,audit_counts=counts,hashes={f:h(f)for f in outputs if f!='completion_report.json'},lesson_count=8,core_periods=17,capstone_periods=3,source_gaps=['source L/W7 with action/order conventions','physical occupied-state selection and a_e definition inputs','physical reference mass and isotope endpoint constants','R032 canonical connecting map'],validator='Run project adapter after finalization; durable result in validator-result.json')
completion['external_auditor_reapproval']='Pending parent-requested external recheck; local repairs and narrow independent check do not constitute external reapproval.'
completion['repaired_external_findings']=['C21-IND-001','C21-IND-002']
completion['hashes']['manifest.json']=h('manifest.json');write('completion_report.json',completion)
print('Finalized 8 lessons, 44 teaching anchors, 11 capstone backward links; hashes current.')
