"""Assemble saved lessons and refresh recovery after completed content audits."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def write(p,s):(ROOT/p).write_text(s,encoding='utf-8')
def save(p,obj):write(p,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
packet=load('input-contract.json');review=load('independent-audit.json');verify=load('verification.json')
assert review['unresolved_counts']['critical']==review['unresolved_counts']['major']==0
assert verify['status']=='passed'
order=[f'lesson-{i:02}' for i in range(1,7)]
intro='# '+packet['topic']+'\n\nSix student lessons, followed by the separately linked two-period capstone. Classroom arithmetic uses a synthetic analogue in LU; source cards preserve locked Cell3 nm values.\n\nSupporting materials: [course map](course-map.md), [glossary](terminology.md), [teacher guide](teacher-guide.md), [capstone and answer key](capstone.md), [sources](sources.md), [canonical card](canonical-card.md).\n\n'
write('course.md',intro+'\n\n'.join('<!-- BEGIN: '+s+' -->\n'+(ROOT/(s+'.md')).read_text(encoding='utf-8').rstrip('\n')+'\n<!-- END: '+s+' -->' for s in order)+'\n')
findings=[]
idmap={'terminology':'terms','course-map':'map'}
for f in review['findings']:
    findings.append(dict(id=f['id'],level=f['audit_level'],category=f['category'],file=f['file'],section=f['section'],severity=f['severity'],defect=f['defect'],correction=f['correction'],verification=f['verification_method']+' '+f['verification_result'],disposition=f['disposition'],affected_checkpoints=[idmap.get(x,x) for x in f['affected_checkpoint_ids']]))
findings.append(dict(id='LOCAL-01',level='local',category='verification_arithmetic',file='verify_examples.py',section='squared spacing for doubled label',severity='major',defect='Initial exact checker used integer norm-squared constants, allowing Python division to introduce floating values and causing 0.20000000000000004 != 0.2.',correction='Represent every squared norm as Fraction before division, including 1 and 5.',verification='Reran the complete exact checker successfully; doubled-label squared spacing equals Fraction(1,5).',disposition='corrected',affected_checkpoints=['verification']))
counts={s:sum(f['severity']==s and f['disposition']=='unresolved' for f in findings) for s in ['critical','major','minor']}
checks=[
 {'level':'local','scope':order,'method':'Full text review plus exact component recomputation; bridge, definitions, units, logic, evidence scope, four diagnostic answers and next dependencies inspected.','result':'passed'},
 {'level':'cumulative','scope':['lesson-01','lesson-02'],'method':'q -> x -> q and q=z+u checks; negative floor and exact endpoint rules verified.','result':'passed'},
 {'level':'cumulative','scope':['lesson-03','lesson-04'],'method':'Three dot pairings for each g; affine plane origin; nonzero h; orientation and doubled-level family checked. Canonical and stale source branches inspected in place.','result':'passed'},
 {'level':'cumulative','scope':['lesson-05','lesson-06','capstone'],'method':'Physical and address dots, both cross-term signs, cosine practice, exact reconstruction and retained display residuals; E05 input/output/practice links inspected.','result':'passed'},
 {'level':'final','scope':['coverage','fidelity','dependency','correctness','terminology','examples','evidence','audience','assessment','minimality'],'method':'Independent reviewer read all six lessons and supporting materials; findings corrected at earliest teaching source. Independent verification and manager exact checks retained separately.','result':'passed'},
 {'level':'final','scope':['rendering'],'method':'Markdown delivery reviewed for table delimiters, equation legibility and local links. No paginated outputs requested, so PDF render gate is not applicable.','result':'passed'},
 {'level':'final','scope':['recovery','assembly','containment'],'method':'Exact marker assembly from saved lesson bytes; SHA-256 refreshed for every deliverable. Installed deterministic validator with authorized project-root adapter is the final execution gate.','result':'prepared_for_validator'}]
save('audit_report.json',dict(status='passed',findings=findings,unresolved_counts=counts,checks=checks,independent_report='independent-audit.json',verification_reports=['verification.json','independent-verification.json'],limitations=['Pacing has not been tested with a live class.','Capabilities response did not expose corpus-generation digest; direct archival source hashes are verified.']))
specs=[('map','course-map','course-map.md',[])]+[(s,'lesson',s+'.md',[order[i-1]] if i else ['map']) for i,s in enumerate(order)]
specs += [('terms','terminology','terminology.md',order),('teacher','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('sources','supplement','sources.md',[]),('canonical-card','supplement','canonical-card.md',['sources']),('verification','supplement','verification.json',order),('independent-verification','supplement','independent-verification.json',order),('independent-audit','supplement','independent-audit.json',order+['capstone']),('assembly','assembly','course.md',order),('audit','audit','audit_report.json',['assembly','capstone','independent-audit'])]
for ident,path in [('input','input-contract.json'),('launch','launch-prompt.md'),('builder','build_course.py'),('checker','verify_examples.py'),('independent-checker','independent_verify.py'),('finalizer','finalize_course.py')]:specs.append((ident,'supplement',path,[]))
cps=[dict(id=i,kind=k,path=p,dependencies=d,status='passed',summary=('Lesson locally and independently audited; required operations and answers checked' if k=='lesson' else 'Saved and reviewed supporting artifact; integrity tracked by SHA-256'),sha256=sha(p)) for i,k,p,d in specs]
outputs=[c['path'] for c in cps]+['completion_report.json']
m=dict(schema_version='1.0',topic=packet['topic'],audience=packet['audience'],assumptions=packet['assumptions'],ordered_deliverables=outputs,checkpoints=cps,dependencies={c['id']:c['dependencies'] for c in cps},course_order=order,assembly=dict(path='course.md',section_ids=order),audit_counts=counts,blockers=[],next_action='none')
save('manifest.json',m)
save('completion_report.json',dict(status='complete',topic=m['topic'],audience=m['audience'],assumptions=m['assumptions'],outputs=outputs,audit_counts=counts,hashes={p:sha(p) for p in outputs if p!='completion_report.json'}|{'manifest.json':sha('manifest.json')},lesson_count=6,capstone_periods=2,source_gaps=['No gap in required M02 teaching content. The packet corpus-generation digest was not returned by capabilities and is not asserted freshly verified.'],validation=dict(status='awaiting_final_execution',command='conda run -n tf_gpu_env python Z:/Kfield-doc-training/.work/validate_project_course.py COURSE_DIRECTORY --json'),harmless_limitations=['Pacing is planned, not learner-trial timing.']))
print('Audited lessons assembled; hashes and completion candidate refreshed. Run final validator.')
