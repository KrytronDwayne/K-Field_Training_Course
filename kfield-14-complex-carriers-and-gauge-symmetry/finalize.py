"""Assemble exact lesson files and validate the completed checkpoint set."""
import re,subprocess,sys
from manage import *

verification=json.loads((ROOT/'verification.json').read_text())
assert verification['status']=='passed'
for p,h in verification['lesson_hashes'].items(): assert sha(p)==h,p
for line in (ROOT/'terminology.md').read_text(encoding='utf-8').splitlines():
    if line.startswith('|'): assert len(re.split(r'(?<!\\)\|',line))==5,line
order=[f'lesson-{n:02}' for n in range(1,8)]
write('course.md','# Complex Carriers and Gauge Symmetry\n\nSeven student lessons. See teacher-guide.md for pacing, capstone.md for synthesis and worked answers, terminology.md for notation, and sources.md for exact provenance.\n\n'+'\n\n'.join(f'<!-- BEGIN: {i} -->\n'+(ROOT/(i+'.md')).read_text(encoding='utf-8').rstrip('\n')+f'\n<!-- END: {i} -->' for i in order))
findings=[dict(id='C14-A01',level='local',category='prerequisite closure',file='lesson-01.md',section='C14.01-P1; lesson-05 root bridge',severity='major',defect='Initial draft omitted the approved exact zeta unit-phase practice in Lesson 1.',correction='Added exact conjugate-times-zeta calculation in Lesson 1 and exact zeta squared/cubed/sixth powers in Lesson 5.',verification='Independent auditor re-read both additions; verify_examples.py checks Q(sqrt(-3)) products exactly, including six distinct roots.',disposition='corrected',affected_checkpoints=['lesson-01','lesson-05','capstone','assembly']),dict(id='C14-A02',level='final',category='Markdown rendering',file='terminology.md',section='modulus and norm rows',severity='minor',defect='Unescaped modulus/norm pipes created extra Markdown table columns.',correction='Escape internal pipe characters when writing every glossary table cell.',verification='Finalizer checks every glossary table row has exactly three cells using unescaped delimiter parsing; content inspected.',disposition='corrected',affected_checkpoints=['terms'])]
audit=dict(schema_version='1.0',status='passed',findings=findings,unresolved_counts=dict(critical=0,major=0,minor=0),independent_review=dict(agent='/root/audit_course14',scope='Seven lessons, input teaching anchors, capstone, teacher guide, course map, terminology, source notes, actual S02/S03 excerpts and all five local source hashes',result='One major bridge omission corrected and confirmed; one minor table issue corrected by manager; no other critical or major findings',math='Auditor independently ran tf_gpu_env arithmetic checks for rotations, V dagger-product, six kernel rows and toy maps; manually checked capstone and 100-point rubric'),local_checks=[dict(checkpoint=i,result='passed',checked=['prerequisites','senior language and load','definitions','notation','dimensionless units','logic','worked mathematics and answers','evidence scope','source fidelity','four diagnostics and next dependency']) for i in order],cumulative_checks=[dict(boundary='lesson-03',result='passed',evidence='Complex arithmetic precedes matrix operations; matrices precede typed projectors and explicit P. Both projections retained.'),dict(boundary='lesson-05',result='passed',evidence='Determinants and weights precede map domain, toy composition, kernel equations and exact six-row enumeration. Source/local order maintained.'),dict(boundary='lesson-07',result='passed',evidence='All seven capstone operations map to prior answered practice; source scope and module namespaces remain distinct.')],final_checks=[dict(category='coverage',result='passed',evidence='All seven C14 concepts have E1,W1,P1,D1 anchors plus named capstone later use.'),dict(category='subject fidelity',result='passed',evidence='S02 M10, typed conventions and S03 AUD-004 read directly; fresh local hashes match; integration source excerpts retrieved.'),dict(category='correctness',result='passed',evidence=f"{len(verification['checks'])} exact arithmetic, structural and source-hash checks passed, plus independent review."),dict(category='audience and assessment',result='passed',evidence='Twelve core periods and three capstone periods; new operations taught; recognition-only extensions excluded from grading.'),dict(category='evidence and residual accounting',result='passed',evidence='Synthetic examples identified; phase, projections and kernel labels retained; mature and integration scopes both recorded.'),dict(category='assembly and recovery',result='passed',evidence='Verbatim markers produced directly from lesson files; SHA-256s generated from saved bytes. Installed validator checks final identity and containment.'),dict(category='format and minimality',result='passed',evidence='Markdown only; glossary delimiters corrected; four diagnostics per lesson, no new teaching during assembly. Paginated rendering not applicable.')],source_gaps=['No fresh full proof-body verification for wider branch status or connected-group classification.','Integration records freshly retrieved as source-attributed excerpts; no fresh local-byte hash or Agda typecheck.','Unique physical global form remains unresolved in the integration.'])
dump('audit_report.json',audit)
m=json.loads((ROOT/'manifest.json').read_text())
for ident,path in [('input','input-contract.json'),('manager-script','manage.py'),('support-script','build_support.py'),('verification-script','verify_examples.py'),('finalizer-script','finalize.py')]:
    if not any(c['id']==ident for c in m['checkpoints']):
        m['checkpoints'].append(dict(id=ident,kind='supplement',path=path,dependencies=[],summary='Retained input or reproducible build/verification support'))
for c in m['checkpoints']:
    c.update(status='passed',sha256=sha(c['path']))
    if c['kind']=='lesson':c['summary']='Complete lesson; exact examples and independent local educational review passed'
    elif c['id']=='audit':c['summary']='Independent findings repaired; final content audit passed'
    else:c['summary']='Complete saved artifact; reviewed and hash checked'
m.update(ordered_deliverables=[c['path'] for c in m['checkpoints']]+['completion_report.json'],dependencies={c['id']:c['dependencies'] for c in m['checkpoints']},audit_counts=audit['unresolved_counts'],blockers=[],next_action='none')
dump('manifest.json',m)
completion=dict(schema_version='1.0',status='complete',topic=m['topic'],audience=m['audience'],assumptions=m['assumptions'],outputs=m['ordered_deliverables'],audit_counts=m['audit_counts'],hashes={p:sha(p) for p in m['ordered_deliverables'] if p!='completion_report.json'},lesson_count=7,core_periods=12,capstone_periods=3,source_gaps=audit['source_gaps'],validator=dict(status='pending_final_execution'))
completion['hashes']['manifest.json']=sha('manifest.json')
dump('completion_report.json',completion)
cmd=[sys.executable,str(ROOT.parents[1]/'.work'/'validate_project_course.py'),str(ROOT),'--json']
result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
if result.returncode:
    completion['status']='validation_failed';dump('completion_report.json',completion)
    print(result.stdout);print(result.stderr);raise SystemExit(result.returncode)
receipt=json.loads(result.stdout)
completion['validator']=dict(status=receipt['status'],exit_code=result.returncode,command=cmd,validator_sha256=receipt['validator_sha256'],checks=receipt['checks'])
dump('completion_report.json',completion)
# Rerun against the actual final completion bytes after recording the result.
final=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
print(final.stdout)
if final.returncode:print(final.stderr)
raise SystemExit(final.returncode)
