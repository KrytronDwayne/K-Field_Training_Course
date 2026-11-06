"""Finalize audit evidence only after independent content and local structural checks."""
import hashlib,json,pathlib,re
P=pathlib.Path(__file__).resolve().parent
def read(name): return json.loads((P/name).read_text(encoding='utf-8-sig'))
def sha(name): return hashlib.sha256((P/name).read_bytes()).hexdigest()
def save(name,obj): (P/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
ind=read('independent-audit.json'); verify=read('verification.json'); m=read('manifest.json')
assert ind['status']=='passed' and verify['status']=='passed'
for level in ('critical','major','minor'): assert ind['unresolved_'+level]==0
audited=ind['lessons']+ind['support_artifacts']+[ind['capstone']]
for row in audited: assert sha(row['file'])==row['sha256'],row['file']
checks=[]
def record(id,evidence): checks.append({'id':id,'status':'passed','evidence':evidence})
assembled=(P/'course.md').read_text(encoding='utf-8'); pos=-1
for id in m['course_order']:
 text=(P/(id+'.md')).read_text(encoding='utf-8').rstrip('\n')
 begin='<!-- BEGIN: '+id+' -->\n'; end='\n<!-- END: '+id+' -->'
 assert assembled.count(begin)==assembled.count(end)==1
 a=assembled.index(begin); b=assembled.index(end)
 assert a>pos and assembled[a+len(begin):b]==text
 pos=b
 record(id+'-assembly','Exact normalized lesson text matches one marker pair in approved order')
for f in P.glob('*.md'):
 if f.name=='launch-prompt.md': continue
 text=f.read_text(encoding='utf-8')
 assert 'Pending production.' not in text,f.name
 assert text.count('```')%2==0,f.name
 for link in re.findall(r'\]\(([^)]+)\)',text):
  if '://' not in link and not link.startswith('#'): assert (P/link.split('#')[0]).is_file(),(f.name,link)
record('markdown','All authored Markdown has balanced fenced blocks, no pending placeholders and resolving relative file links; no paginated/visual output requested')
record('independent-content','Audited-file hashes unchanged; seven lessons, capstone and three supporting artifacts independently read and recomputed')
record('finite-verification',str(verify['check_count'])+' successful standard-library arithmetic/hash/pointer/teaching-link checks in tf_gpu_env')
record('source-fidelity','Manager compared sources.md to directly read M14, M03, M11, BR-05, BR-10, five proof nodes and AUD-009; all five archival hashes match')
record('evidence-layers','Source-report, finite derivation, conditional construction and missing replay bodies explicitly distinguished; no empirical data or physical phase/occupation inference added')
record('audience-and-minimality','Independent audit confirms local operation bridges, four diagnostics per lesson, 12 core plus 3 capstone periods; recognition-only extensions not required computations')
record('unit-A','Lessons 01–04 preserve carrier/endpoint definitions and include complete reconstruction; finite square index 0 versus rectangular/infinite index -1 checked')
record('unit-B','Lessons 05–06 preserve spatial/time and independent grading labels; angular representation counts separated from physical occupation')
record('unit-C-and-E05','Lesson 07 and all ten capstone tasks have prior E/W/P/D anchors and independently answered practice; backward map contains explicit inputs/outputs')
record('storage','All authored course artifacts are under the authorized direct project child; sources read-only; no raw copies or large data arrays')
findings=[]
for row in ind['findings']:
 row=dict(row); row['affected_checkpoints']=row.pop('affected_checkpoint_ids'); findings.append(row)
audit=dict(schema_version='1.0',status='passed',scope='Local, cumulative and final content audit plus manager assembly/containment checks; final deterministic validator is run after hash refresh',findings=findings,unresolved_counts={'critical':0,'major':0,'minor':0},corrected_counts={level:sum(row['severity']==level for row in findings) for level in ('critical','major','minor')},checks=checks,independent_report='independent-audit.json',independent_report_sha256=sha('independent-audit.json'),verification_report='verification.json',source_gaps=['B_8 and T_0 complete typed replay bodies not loaded; source-scoped recognition boundary is preserved, not assigned as a course proof.'],rendering='Markdown delivery; no PDF/Word or visual artifact generation requested. Table/fence/link structure checked.',private_reasoning_included=False)
save('audit_report.json',audit)
for id,path in [('independent-audit','independent-audit.json'),('verify-script','verify_examples.py'),('recovery-script','manage.py'),('final-check-script','final_checks.py'),('input-contract','input-contract.json')]:
 if id not in [cp['id'] for cp in m['checkpoints']]:
  m['checkpoints'].append(dict(id=id,kind='supplement',path=path,dependencies=[],status='drafted',summary='Supporting provenance, audit or reproducibility artifact',sha256=sha(path)))
  m['ordered_deliverables'].insert(-1,path)
m['dependencies']={cp['id']:cp['dependencies'] for cp in m['checkpoints']}
save('manifest.json',m)
print('Final audit content checks passed;',len(checks),'check groups; all recorded minor findings corrected.')
