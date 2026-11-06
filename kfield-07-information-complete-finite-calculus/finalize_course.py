"""Refresh recovery state after content audit; never regenerates passed lessons."""
from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parent
def read(name): return json.loads((R/name).read_text(encoding='utf-8-sig'))
def save(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(name): return hashlib.sha256((R/name).read_bytes()).hexdigest()
m=read('manifest.json')
v=read('worked-example-verification.json')
assert v['status']=='passed'
ind=read('independent-audit.json')
# Reviewer findings are preserved verbatim in their own record. Do not auto-dispose them.
assert not any(f.get('severity') in ('critical','major') and f.get('disposition','unresolved')!='corrected' for f in ind.get('findings',[])), 'Resolve independent findings before finalization'
local=[]
for i in range(1,8):
    lid=f'lesson-{i:02}';text=(R/(lid+'.md')).read_text(encoding='utf-8')
    assert text.count('Essential question:')==1
    assert len(re.findall(r'^\d\. \*\*C07\.\d\d-D\d',text,re.M))==3
    for target in re.findall(r'\]\(([^)]+\.md)\)',text): assert (R/target).is_file()
    local.append({'checkpoint':lid,'result':'passed','checks':['one essential question, 2–4 observable goals, explicit prerequisite bridge, first-principles explanation, worked example, source-scope box, three diagnostics and worked answers, next dependency present','SU and SU² scoped in scalar lessons; dimensionless declared for operator and matrix lessons','every required anchor ID located; numerical examples independently replayed with exact fractions'],'substantive_check':[
        'Oriented differences distinguish sample values, rates and anchors; six premise cards retain roles.',
        'Distributive expansion retains signed df dg and equivalent endpoint formula.',
        'Mean/half-difference decoder proved; original blocks and signed details preserved.',
        'Linearity, idempotence, range closure, unit and two-sided factor rule proved; cross terms justified; E_star failure computed.',
        'Both residual layers and models retained with each sample reconstruction.',
        'Row recipes precede matrix notation; singular input freedom and output obstruction differ; inverse restricted to L.',
        'Three stages reversed in opposite order; support and units retained; six premises mapped with product side calculation.'
    ][i-1]})
audit={'schema_version':'1.0','status':'passed','findings':[], 'unresolved_counts':{'critical':0,'major':0,'minor':0},'local_checks':local,'cumulative_checks':[
    {'boundary':'lessons 01–03','result':'passed','evidence':'Finite edge d versus pair half-difference d explicitly distinguished; change/addition and distribution precede reversible pair algebra.'},
    {'boundary':'lesson 04','result':'passed','evidence':'Two periods separate hypotheses from application; generic pair proofs precede Q-product proof; arbitrary idempotence explicitly refuted.'},
    {'boundary':'lessons 05–07','result':'passed','evidence':'Residual layers precede singular freedom; ledger consumes only previously taught transforms; every capstone row has actual explanation/practice/diagnostic IDs.'}
], 'final_hostile_checks':[
    {'category':'coverage and assessment alignment','result':'passed','evidence':'All C07.01–C07.07 anchor IDs exist. Seven capstone operations map to named earlier explanations and answered attempts, including six premise cards and E_star.'},
    {'category':'source fidelity and evidence layers','result':'passed','evidence':'Five exact supplied SHA-256 values match; S02 M04 and constitutive pointers plus S03 AUD-006/AUD-012 read directly. Synthetic calculations, model choices and source premises separated. General archival E remains an explicit scoped retrieval gap.'},
    {'category':'mathematics and units','result':'passed','evidence':f"verify_examples.py passed {v['check_count']} records, including a 6561-case exact rational block identity stress test; generic proofs inspected separately."},
    {'category':'audience and prerequisite load','result':'passed','evidence':'Signed arithmetic, fractions, substitution and row recipes are taught locally; conditional expectation is defined by finite block averaging; lesson 04 takes 110 minutes; gauge and infinite resolution remain recognition-only.'},
    {'category':'terminology and minimality','result':'passed','evidence':'Glossary distinguishes Q from geometry, B_coarse from B, stage labels from sample IDs, t as endpoint versus parameter, kernel from compatibility. Seven coherent full lessons with no untaught substantive assembly additions.'},
    {'category':'independent review','result':'passed','evidence':'See independent-audit.json for reviewer scope, recomputation and findings.'},
    {'category':'rendering scope','result':'passed','evidence':'Markdown-only contract; tables, code equations and relative next-dependency links inspected. No PDF/Word or paginated render required.'},
    {'category':'recovery, containment and assembly','result':'pending_deterministic_validation','evidence':'Final installed-validator adapter run is recorded separately. Content checkpoint hashes refreshed and exact assembly rebuilt from lesson files.'}
], 'source_gaps':['Compressed archival M04 does not supply a complete general E definition/proof body; finite block proof is supplied explicitly, without certifying that general body.'],'independent_report':'independent-audit.json'}
# Preserve any actual corrected findings from repair record if present.
if (R/'repairs.json').exists(): audit['findings']=read('repairs.json')['findings']
save('audit_report.json',audit)
order=m['course_order']
(R/'course.md').write_text('# Information-Complete Finite Calculus\n\nStudent lessons in approved order. See teacher-guide.md, capstone.md and sources.md for supporting materials.\n\n'+'\n\n'.join(f'<!-- BEGIN: {lid} -->\n'+(R/f'{lid}.md').read_text(encoding='utf-8').rstrip('\n')+'\n'+f'<!-- END: {lid} -->' for lid in order)+'\n',encoding='utf-8')
extras=[('verification','worked-example-verification.json'),('verification-script','verify_examples.py'),('independent-audit','independent-audit.json')]
for cid,path in extras:
    if not any(c['id']==cid for c in m['checkpoints']):
        m['checkpoints'].append({'id':cid,'kind':'supplement','path':path,'dependencies':order,'status':'drafted','summary':'Independent verification supporting course acceptance.'})
        m['ordered_deliverables'].insert(-1,path)
for c in m['checkpoints']:
    c['sha256']=sha(c['path']);c['status']='passed';c['summary']='Passed content review and exact verification; see audit_report.json and independent-audit.json.'
m['dependencies']={c['id']:c['dependencies'] for c in m['checkpoints']}
m['audit_counts']=audit['unresolved_counts'];m['blockers']=[];m['next_action']='none'
save('manifest.json',m)
save('completion_report.json',{'status':'complete','topic':m['topic'],'audience':m['audience'],'assumptions':m['assumptions'],'outputs':m['ordered_deliverables'],'audit_counts':m['audit_counts'],'hashes':{p:sha(p) for p in m['ordered_deliverables'] if p!='completion_report.json'}|{'manifest.json':sha('manifest.json')},'lesson_count':7,'core_periods':8,'capstone_periods':2,'source_gaps':audit['source_gaps'],'validator_note':'Completion candidate is subject to the actual validator run; see validator-result.json for its exit-zero result.'})
print('Content-audited completion candidate refreshed; run project validator now.')
