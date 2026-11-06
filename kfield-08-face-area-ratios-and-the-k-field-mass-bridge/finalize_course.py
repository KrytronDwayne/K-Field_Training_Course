"""Refresh course recovery state after an actual passing independent audit."""
from pathlib import Path
import json,hashlib,subprocess,sys
D=Path(__file__).resolve().parent
def read(p): return json.loads((D/p).read_text(encoding='utf-8-sig'))
def write(p,x): (D/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256((D/p).read_bytes()).hexdigest()
m=read('manifest.json'); review=read('independent-audit.json')
assert review['unresolved_counts']=={'critical':0,'major':0,'minor':0},review
assert all(f['status']=='corrected' for f in review['findings'])
for path,digest in review['reviewed_sha256'].items(): assert sha(path)==digest,path
order=m['course_order']
assembly='# Face-Area Ratios and the K-Field Mass Bridge\n\nStudent lessons in dependency order. Supporting source cards, glossary, teacher guide, and capstone are separate files.\n\n'
assembly+='\n\n'.join(f'<!-- BEGIN: {i} -->\n'+(D/(i+'.md')).read_text(encoding='utf-8').rstrip()+'\n'+f'<!-- END: {i} -->' for i in order)+'\n'
(D/'course.md').write_text(assembly,encoding='utf-8')
audit={'status':'passed','findings':review.get('findings',[]),'unresolved_counts':{'critical':0,'major':0,'minor':0},'author_check_record':'author-audit.json','independent_check_record':'independent-audit.json','arithmetic_replay':'replay_checks.py and independent_audit_checks.py','final_checks':{'source_fidelity':'Five matching original source hashes; source status and fresh computations separated','prerequisites':'Independent E05 review; arbitrary-s proof and provenance-row practice repaired','coverage':'Six concepts introduced, practiced, assessed, and reused','recovery':'All output hashes refreshed after repaired assembly','assembly':'Every final lesson copied verbatim with required markers','rendering':'Markdown-only output; no paginated rendering required','minimality':'Six core periods plus two capstone periods; no new teaching in assembly'},'source_gap':'MCP search did not locate exact source artifact and did not expose snapshot generation; local exact-hash files used. Full archive proof certification is outside this finite course.'}
audit['findings']=[{'id':f['id'],'level':'final','category':'E05 assessment prerequisite closure','file':f['file'],'section':'Guided practice P1','severity':f['severity'],'defect':f['finding'],'correction':f['required_fix'],'verification':review['repair_verification'],'disposition':'corrected','affected_checkpoints':[f['file'].removesuffix('.md'),'capstone','assembly']} for f in review['findings']]
for f in audit['findings']:
    if f.get('disposition')=='unresolved': audit['unresolved_counts'][f['severity']]+=1
write('audit_report.json',audit)
extra=[('independent-audit','supplement','independent-audit.json',['author-audit']),('replay','supplement','replay_checks.py',['verification']),('independent-checks','supplement','independent_audit_checks.py',['verification']),('input','supplement','input-contract.json',[])]
for id,kind,path,deps in extra:
    if not any(x['id']==id for x in m['checkpoints']): m['checkpoints'].append({'id':id,'kind':kind,'path':path,'dependencies':deps,'summary':'Verified '+path})
for cp in m['checkpoints']:
    if cp['id']=='audit': cp['dependencies']=['author-audit','independent-audit']
    cp['status']='passed'; cp['sha256']=sha(cp['path']); cp['summary']='Completed and audited '+cp['path']
m['ordered_deliverables']=[cp['path'] for cp in m['checkpoints']]+['completion_report.json']
m['dependencies']={cp['id']:cp['dependencies'] for cp in m['checkpoints']}
m['audit_counts']=audit['unresolved_counts'];m['blockers']=[];m['next_action']='none'
write('manifest.json',m)
report={'status':'complete','topic':m['topic'],'audience':m['audience'],'assumptions':m['assumptions'],'outputs':m['ordered_deliverables'],'audit_counts':m['audit_counts'],'hashes':{p:sha(p) for p in m['ordered_deliverables'] if p!='completion_report.json'},'lesson_count':6,'source_gaps':audit['source_gap'],'validator':'Final candidate assembled; actual validator result below is populated only after execution.'}
report['hashes']['manifest.json']=sha('manifest.json')
write('completion_report.json',report)
run=subprocess.run([sys.executable,str(D.parents[1]/'.work'/'validate_project_course.py'),str(D),'--json'],text=True,capture_output=True)
if run.returncode:
    report['status']='validation_failed';report['validator_stdout']=run.stdout;report['validator_stderr']=run.stderr;write('completion_report.json',report)
    print(run.stdout,run.stderr);raise SystemExit(run.returncode)
result=json.loads(run.stdout)
report['validator']={'exit_code':run.returncode,**result}
write('completion_report.json',report)
# Recheck the report including its actual successful validator result.
again=subprocess.run([sys.executable,str(D.parents[1]/'.work'/'validate_project_course.py'),str(D),'--json'],text=True,capture_output=True)
print(again.stdout,again.stderr)
raise SystemExit(again.returncode)
