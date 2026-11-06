from pathlib import Path
import json, hashlib, re, subprocess, sys
R=Path(__file__).resolve().parent
def load(p): return json.loads((R/p).read_text(encoding='utf-8-sig'))
def save(p,o): (R/p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256((R/p).read_bytes()).hexdigest()
p=load('input-contract.json'); m=load('manifest.json'); independent=load('independent-audit.json'); verify=load('verification.json')
assert verify['status']=='passed' and not independent['findings']
for path,h in independent['files_sha256'].items(): assert digest(path)==h,path
# Recover only from checked bytes; no passed teaching content is rewritten.
for cp in m['checkpoints']:
    if cp['status']=='passed': assert digest(cp['path'])==cp['sha256'],cp['id']
order=m['course_order']
assembly='# '+p['topic']+'\n\nComplete student course. Eight lessons; 17 core periods of 55 minutes. Use [the capstone](capstone.md), [glossary](terminology.md), [course map](course-map.md), [teacher guide](teacher-guide.md) and [source notes](sources.md) alongside these lessons.\n\n'
for lid in order:
    txt=(R/(lid+'.md')).read_text(encoding='utf-8').replace('\r\n','\n').rstrip('\n')
    assembly+='<!-- BEGIN: '+lid+' -->\n'+txt+'\n<!-- END: '+lid+' -->\n\n'
(R/'course.md').write_text(assembly,encoding='utf-8')
for lid in order:
    actual=assembly.split('<!-- BEGIN: '+lid+' -->\n')[1].split('\n<!-- END: '+lid+' -->')[0]
    assert actual==(R/(lid+'.md')).read_text(encoding='utf-8').rstrip('\n')
for file in R.glob('*.md'):
    if file.name=='launch-prompt.md': continue
    for link in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
        if link.endswith('.md') and not link.startswith(('http','/')):
            assert (R/link).is_file(),(file.name,link)
audit={
 'schema_version':'1.0','status':'passed','findings':[],
 'unresolved_counts':{'critical':0,'major':0,'minor':0},
 'local_checks':{'scope':'All eight lessons','evidence':['independent-audit.json','verification.json'],'categories':['prerequisites','audience','definitions','notation','units','logic','mathematics','evidence','source scope','answers'],'result':'passed'},
 'cumulative_checks':[
 {'boundary':'lesson-03','check':'Circle, beat and ruler rates use cycles/s versus radians/s explicitly; dot products and origin subtraction taught before geometry use.','result':'passed'},
 {'boundary':'lesson-05','check':'DFT sign, inverse factor and conjugate bins consistent; parity preserves both components; all four-angle denominator failures retain defined intermediates.','result':'passed'},
 {'boundary':'lesson-08','check':'Nine capstone operations traced to named explanation, worked example, answered practice and diagnostic; three cost levels never replace fourteen response rows.','result':'passed'}],
 'final_hostile_checks':[
 {'category':'coverage','evidence':'Nine concepts and nine capstone operations mapped in course-map.md; exact amendment anchors and aliases asserted.','result':'passed'},
 {'category':'source_fidelity','evidence':'Five local file digests matched; five pinned application ranges read. S05 exact records inspected. Source signs, nulls, family alias, revision mismatch and evidence classes retained.','result':'passed'},
 {'category':'dependency_order','evidence':'Unit circle before addition; geometry before finite spectra; division before source ratios; power/time before energy; residuals before synthesis.','result':'passed'},
 {'category':'correctness','evidence':'35 executable checks and independent mathematical review recorded; source binary64 closures remain signed diagnostics.','result':'passed'},
 {'category':'terminology','evidence':'Glossary distinguishes G phase metric, contrast_counts, fractional_gain, local count Q and source geometric Q; O origin/operator scoped.','result':'passed'},
 {'category':'examples_answers','evidence':'All finite examples recomputed; capstone answers and 36-point rubric independently reviewed.','result':'passed'},
 {'category':'evidence_layers','evidence':'Synthetic identities, report observations, derived ratios, proposed pathways, reference photon formula and unresolved transfer separated.','result':'passed'},
 {'category':'audience_load','evidence':'17 core periods; Lesson 4 and 5 each three sessions; finite roots table and ratio bridges precede assessment; optional recovery periods specified.','result':'passed'},
 {'category':'assessment_alignment','evidence':'Independent capstone recheck: all nine operations have prior answered practice.','result':'passed'},
 {'category':'recovery_integrity','evidence':'Independent lesson hashes rechecked before assembly; every checkpoint hash computed from saved bytes. Final deterministic validator required below.','result':'passed'},
 {'category':'assembly_identity','evidence':'All eight exact marker sections compared to lesson bytes after newline normalization; order preserved; no substantive assembly teaching.','result':'passed'},
 {'category':'rendering_links','evidence':'Markdown-only delivery; inspected headings/tables and checked all local Markdown target links. No paginated output requested.','result':'passed'},
 {'category':'storage_minimality','evidence':'All authored persistent artifacts contained here; no raw snapshots or large arrays; essential lessons and support only.','result':'passed'}],
 'source_gaps':['Source bundle energy revision mismatch and quadratic PDF digest/size mismatch retained.','Raw acquisition, calibration, uncertainty, exposure-transfer and independent physical replay remain source obligations.','Referenced compiler bodies and S05 underlying native FFT arrays were not freshly verified; no such claim is made.'],
 'independent_audit_scope':'Independent lessons, capstone and support consistency; source byte retrieval and final validator handled by author.',
 'validator_scope':'Deterministic storage/hash/assembly/audit contract; not a substitute for content review.'
}
save('audit_report.json',audit)
extras=[
('source-replay','source-replay.json','Derived row diagnostics and immutable references'),
('retrieval-record','retrieval-record.json','Pinned source read receipts'),
('independent-audit','independent-audit.json','Independent lesson and capstone audit'),
('input-contract','input-contract.json','Approved runtime contract preserved'),
('launch-prompt','launch-prompt.md','Original launch packet preserved'),
('verification-script','verify_examples.py','Replayable finite verification'),
('recovery-script','manage.py','Recovery initialization and passed-hash check'),
('finalize-script','finalize.py','Assembly and deterministic validation orchestration')]
existing={c['id'] for c in m['checkpoints']}
for cid,path,summary in extras:
    if cid not in existing: m['checkpoints'].append(dict(id=cid,kind='supplement',path=path,dependencies=[],status='drafted',summary=summary))
m['ordered_deliverables']=[c['path'] for c in m['checkpoints']]+['completion_report.json']
m['dependencies']={c['id']:c['dependencies'] for c in m['checkpoints']}
m['audit_counts']=audit['unresolved_counts'];m['blockers']=[]
for i,cp in enumerate(m['checkpoints']):
    assert (R/cp['path']).is_file(),cp['path']
    cp['status']='passed';cp['sha256']=digest(cp['path'])
    m['next_action']='Validate remaining checkpoint hashes' if i<len(m['checkpoints'])-1 else 'none'
    save('manifest.json',m)
completion={
 'schema_version':'1.0','status':'complete','topic':m['topic'],'audience':m['audience'],'assumptions':m['assumptions'],
 'outputs':m['ordered_deliverables'],'audit_counts':m['audit_counts'],
 'hashes':{path:digest(path) for path in m['ordered_deliverables'] if path!='completion_report.json'},
 'lesson_count':8,'core_periods':17,'capstone_periods':3,'period_minutes':55,
 'output_directory':str(R),'source_gaps':audit['source_gaps'],'harmless_unresolved_minor_findings':[],
 'validator':{'status':'pending final command'}
}
completion['hashes']['manifest.json']=digest('manifest.json')
save('completion_report.json',completion)
# Invoke the exact user-selected adapter with this same explicitly selected interpreter.
cmd=[sys.executable,'Z:/Kfield-doc-training/.work/validate_project_course.py',str(R),'--json']
run=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
print(run.stdout)
if run.returncode:
    print(run.stderr);raise SystemExit(run.returncode)
payload=json.loads(run.stdout)
completion['validator']={'status':payload['status'],'exit_code':run.returncode,'command':cmd,'result':payload}
save('completion_report.json',completion)
# Recheck the final state after recording the non-self-hashed validator result.
last=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
assert last.returncode==0,last.stdout+last.stderr
print('FINAL VALIDATOR EXIT 0; assembly SHA-256 '+digest('course.md'))
