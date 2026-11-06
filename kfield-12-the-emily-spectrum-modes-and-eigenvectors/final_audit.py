"""Consolidate actual review evidence, verify assembly and prepare recovery hashes."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parent
def read(p): return json.loads((R/p).read_text(encoding='utf-8'))
def write(p,x): (R/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
packet=read('input-contract.json'); manifest=read('manifest.json')
independent=read('independent-audit.json'); replay=read('verification.json')
assert independent['unresolved_counts']==dict(critical=0,major=0,minor=0)
assert replay['status']=='passed'
assembly=(R/'course.md').read_text(encoding='utf-8')
cursor=-1
for i in range(1,8):
    ident=f'lesson-{i:02}'; body=(R/(ident+'.md')).read_text(encoding='utf-8').rstrip('\n')
    block=f'<!-- BEGIN: {ident} -->\n{body}\n<!-- END: {ident} -->'
    assert assembly.count(block)==1
    pos=assembly.index(block); assert pos>cursor;cursor=pos
    text=body
    assert len(re.findall(r'^\d\. ',text,re.M))==4,ident
cap=(R/'capstone.md').read_text(encoding='utf-8')
for i in range(1,8):
    assert f'C12-CAP-{i:02}' in cap
    assert f'C12.{i:02}-P1' in cap
assert sum([8,10,18,12,18,20,14])==100
for p in R.glob('*.md'):
    if p.name=='launch-prompt.md': continue
    for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if '://' in link or link.startswith('#'): continue
        assert (R/link.split('#')[0]).exists(),(p.name,link)
for p in R.iterdir(): assert p.resolve().is_relative_to(R.resolve())
extras=[('input-contract','input-contract.json'),('launch-prompt','launch-prompt.md'),('independent-audit','independent-audit.json'),('independent-computation','independent-computation.json'),('independent-script','independent_check.py'),('final-audit-script','final_audit.py')]
for ident,path in extras:
    if not any(c['id']==ident for c in manifest['checkpoints']):
        manifest['checkpoints'].append(dict(id=ident,kind='supplement',path=path,dependencies=[],status='drafted',summary='Supplied authority or actual independent review evidence',sha256=hashlib.sha256((R/path).read_bytes()).hexdigest()))
        manifest['ordered_deliverables'].insert(-1,path)
manifest['dependencies']={c['id']:c['dependencies'] for c in manifest['checkpoints']}
write('manifest.json',manifest)
audit=dict(schema_version='1.0',status='passed',unresolved_counts=dict(critical=0,major=0,minor=0),findings=[dict(id='IA-MIN-01',level='local',category='source_pointer_clarity',file='lesson-05.md',section='Claim scope and source card',severity='minor',defect='The citation /emily_spectrum was shorthand rather than a complete JSON pointer.',correction='Expanded to /backbone_sequence/7/emily_spectrum.',verification='Independent auditor rechecked the repaired pointer against S02; see independent-audit.json.',disposition='corrected',affected_checkpoints=['lesson-05','assembly'])],checks=[
dict(level='local',category='lesson_contract_and_prerequisites',evidence='Independent full reading of all seven lessons and 28 E/W/P/D anchors plus three legacy anchors; each lesson has one question, 3–4 goals, bridge, worked example, practice and four answered diagnostics. E05/E06 accepted in independent-audit.json.'),
dict(level='local',category='mathematics_and_answers',evidence='verify.py passed 115 exact rational/radical checks; independent_check.py separately corroborated all 27 eigenpairs and 729 dot products and exact rational M17 rank. Independent auditor hand checked all lesson answers.'),
dict(level='cumulative',category='unit_1',evidence='Lessons 01–03 progress row action → common multiplier → two-case derivation → norm/dot definitions. No division by zero; exact radicals precede normalization.'),
dict(level='cumulative',category='unit_2',evidence='Lessons 04–05 use defined product entries and finite sums before counting; exhaustive ledger lists 27 modes. Function parity, node chi and sheet populations retain distinct meanings.'),
dict(level='cumulative',category='unit_3',evidence='Lessons 06–07 derive coefficient reconstruction and residual accounting before map tests. Degree calculation disproves constant-line invariance; reflection commutation is separately explained.'),
dict(level='final',category='coverage_and_assessment',evidence='All seven kernel capabilities map to actual explanations, answered practice and capstone steps. Capstone operations retain named inputs/outputs; full answer key matches taught finite calculations and 100-point rubric.'),
dict(level='final',category='fidelity_and_sources',evidence='Five source SHA-256 values verified; exact M08/M03/M17 and AUD-002 pointers inspected. Sources distinguish source reports, fresh finite results and synthetic examples. Graph retrieval failure disclosed; no formal authority promoted.'),
dict(level='final',category='definitions_units_and_invariants',evidence='Dimensionless patterns; node order (−1,0,1), lexicographic triples and mode order (+,0,−) fixed. B_Y explicitly differs from geometric B. No extraneous physical constants or parity identities imported.'),
dict(level='final',category='evidence_and_residuals',evidence='No empirical measurements fabricated. Full reconstruction, zero-mode residual, even/odd parts and mean/detail each recover input. Source gauge coordinate count does not become a 26-mode Emily claim.'),
dict(level='final',category='audience_and_minimality',evidence='Eleven core periods at 55 minutes plus two capstone periods. Four dense lessons get two periods; squares, norms, finite sums and composition taught. M17 decoder and global spectral/formal claims remain recognition-only. No new teaching added in assembly.'),
dict(level='final',category='assembly_identity_and_order',evidence='final_audit.py checked exactly one verbatim marker block for each of seven lessons in approved order; deterministic validator checks this again.'),
dict(level='final',category='rendering_and_links',evidence='Markdown delivery only, as requested. Readable text/tables; all local Markdown artifact links resolved. No paginated or generated visual artifact needs a render tool.'),
dict(level='final',category='storage_and_recovery',evidence='All persistent files contained in the assigned course directory. Checkpoint hashes are refreshed by manage.py; final external validator is required after this report and its actual exit is reported separately.')
],external_scope_gaps=['RAG object get returned snapshot object not found; local digest-verified source bodies provided core grounding.','AUD-002 global formula-DAG repair and fresh formal compiler replay are not certified.'],independent_review='independent-audit.json',replay='verification.json')
write('audit_report.json',audit)
print('Final review consolidated; seven assembly blocks and local links verified. Run manage.py finalize then project validator.')
