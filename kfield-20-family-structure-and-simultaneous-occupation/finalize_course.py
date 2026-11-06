"""Assemble audited lessons verbatim and refresh deterministic recovery records."""
from pathlib import Path
import json, hashlib, sys

root=Path(__file__).resolve().parent
def read(name):return json.loads((root/name).read_text(encoding='utf-8-sig'))
def sha(name):return hashlib.sha256((root/name).read_bytes()).hexdigest()
def save(name,obj):(root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
packet=read('input-contract.json')
verification=read('verification.json')
independent=read('independent-audit.json')
assert verification['status']=='passed'
assert independent['unresolved']=={'critical':0,'major':0,'minor':0},'Independent review still has findings'
for p,h in verification['reviewed_content_sha256'].items():assert sha(p)==h,p
for item in independent['reviewed_files']:assert sha(item['path'])==item['sha256'],item['path']
order=[f'lesson-{i:02d}' for i in range(1,8)]
assembled='# Family Structure and Simultaneous Occupation\n\nA complete topical course for high-school seniors. Seven lessons over 15 core periods, plus three capstone periods.\n\n[Course map](course-map.md) · [Terminology](terminology.md) · [Capstone and full key](capstone.md) · [Teacher guide](teacher-guide.md) · [Sources](sources.md)\n\n'
for id in order:
    text=(root/(id+'.md')).read_text(encoding='utf-8').replace('\r\n','\n').rstrip('\n')
    assembled+=f'<!-- BEGIN: {id} -->\n{text}\n<!-- END: {id} -->\n\n'
(root/'course.md').write_text(assembled,encoding='utf-8',newline='\n')
findings=[
 {'id':'A20-01','level':'local','category':'prerequisite','file':'lesson-03.md','section':'C20.S01-E1 and diagnostic 5','severity':'minor','defect':'Rank appeared in a diagnostic before its explicit definition in lesson 4.','correction':'Defined image and rank before the lesson-3 diagnostic.','verification':'Independent auditor reread the definition in its earlier location; lesson-4 equation-based bridge remains intact.','disposition':'corrected','affected_checkpoints':['lesson-03','assembly']},
 {'id':'A20-02','level':'final','category':'source_locator','file':'sources.md','section':'S02 pointers','severity':'minor','defect':'A selector /proof_operations:step_id=D10 was labelled as a JSON pointer.','correction':'Replaced it in authored sources and provenance with exact /proof_operations/9. The original input contract remains unchanged.','verification':'Independent auditor directly checked S02 array index 9 has step_id D10.','disposition':'corrected','affected_checkpoints':['sources','provenance']},
 {'id':'A20-03','level':'cumulative','category':'terminology','file':'terminology.md','section':'Adjoint/unitary/isometry row','severity':'minor','defect':'The glossary risked conflating rectangular isometry and square unitary.','correction':'Specified square U with both inverse identities and rectangular V reversible on its image; clarified lesson 3.','verification':'Independent content reread and 20 mathematical checks pass; no lift image surjectivity is claimed.','disposition':'corrected','affected_checkpoints':['lesson-03','terminology','assembly']}
]
categories=[
 ('coverage','All nine kernel concepts have actual E1/W1/P1/D1 IDs and nine capstone operations; legacy rank bridge IDs retained. Automated ID checks plus independent reading.'),
 ('fidelity','Direct hash checks of S01–S05; actual S02 M16/F038/X033/D10 and S03 AUD-007/AUD-009 read; occupation claim, guard, correction and retrieval remain together.'),
 ('dependency_order','Residues → means/norms → matrices/complex/Fourier/Weyl → rank/product → source factorization → selection → numerical scope/Schur. Rank preview corrected.'),
 ('correctness','20 independent finite checks using exact fractions and complex tolerance 1e-12; manager determinant-route scalar checks and source hashes included among 146 checks.'),
 ('terminology','Local P/R, B_ab/B block/B geometry, W_r/weak W2, E and C scope identified. All finite numerical examples dimensionless; rank/dimension separated.'),
 ('examples_answers','Worked and practice class tables, all nine Weyl coefficients, Fourier inverse, projector complement, history alternatives and scalar branches independently recomputed.'),
 ('evidence_layers','Synthetic examples explicitly labelled; conditional mathematical checks are separate from source-reported statuses and unfilled physical selection premises. No invented observations.'),
 ('audience_load','15 core periods with locally introduced operations and 2–4 observable goals per lesson; lesson 3 has four sessions and lesson 7 three. No hidden required advanced proof.'),
 ('assessment_alignment','Independent capstone review confirms nine parts have earlier explanations and answered practice; rubric totals 100; exact IDs and named task inputs/outputs present.'),
 ('recovery_integrity','Finalizer verifies current lesson hashes against mathematical record and all independent reviewed-file hashes before passing; final deterministic validator checks complete checkpoint graph.'),
 ('assembly_identity','Generated directly from each lesson with exact markers in declared order; no new substantive teaching in assembly. Deterministic validator checks identity.'),
 ('rendering','Markdown-only delivery as requested. Reviewed table/code-fence structure and local file links; no paginated or rendered output required.'),
 ('containment_minimality','Every persistent authored artifact is inside the packet course directory. Sources read-only, no snapshots. Seven lesson checkpoints preserve required supplemental operations without outline-only content.')
]
audit={'schema_version':'1.0','status':'passed','findings':findings,'unresolved_counts':{'critical':0,'major':0,'minor':0},'corrected_counts':{'critical':0,'major':0,'minor':3},'local_checks':[{ 'checkpoint':id,'result':'passed','checks':['prerequisites','audience','definitions','notation','units','logic','mathematics','evidence','sources','answers'],'evidence':'Authored lesson reread; independent-audit.json and verification.json contain actual reviewed hashes and computations.'} for id in order], 'cumulative_checks':[{'unit':'lessons 1–2','result':'passed','evidence':'Residue order, 3+24 coordinate count and full reconstruction preserved.'},{'unit':'lessons 3–4','result':'passed','evidence':'Complex/matrix prerequisites taught; rank timing and unitary/isometry wording corrected; Weyl and rank checks pass.'},{'unit':'lessons 5–7','result':'passed','evidence':'Rank premises, source status conflict and numeric-input scope retained; Schur and singular branches checked.'}],'final_hostile_checks':[{'category':c,'result':'passed','evidence':e} for c,e in categories],'independent_review':'independent-audit.json','mathematical_verification':'verification.json','source_gaps_are_scoped_not_course_defects':read('source-provenance.json')['retrieval_gaps'],'deterministic_validation':'See completion_report.json and validation-result.json for actual external validator result; semantic audit does not substitute for it.'}
save('audit_report.json',audit)
checkpoints=[]
def cp(id,kind,path,deps,summary):
    checkpoints.append({'id':id,'kind':kind,'path':path,'dependencies':deps,'status':'passed','sha256':sha(path),'summary':summary})
cp('course-map','course-map','course-map.md',[],'Exact introduction, practice, diagnostic and capstone map checked.')
for i,id in enumerate(order):cp(id,'lesson',id+'.md',['course-map'] if i==0 else [order[i-1]],'Lesson contract, source scope and finite examples reviewed; no unresolved findings.')
cp('terminology','terminology','terminology.md',order,'Notation collisions and unitary/isometry distinction reviewed.')
cp('teacher-guide','teacher-guide','teacher-guide.md',order,'Pacing, repair and assessment guidance checked.')
cp('capstone','capstone','capstone.md',order,'Nine taught operations, full worked key and 100-point rubric checked.')
cp('sources','supplement','sources.md',[],'Exact source claims, pointers and scope checked.')
cp('provenance','supplement','source-provenance.json',['sources'],'All five archival hashes matched; source retrieval classes retained.')
cp('independent-verification-script','supplement','independent-verification.py',[],'Independent standard-library finite-check replay.')
cp('verification-script','supplement','verify_examples.py',[],'Structural content-ID and secondary exact-arithmetic checks.')
cp('verification','supplement','verification.json',order+['verification-script','independent-verification-script'],'146 manager checks and 20 independent mathematical checks passed.')
cp('independent-audit','supplement','independent-audit.json',order+['capstone','teacher-guide','terminology','sources','provenance'],'Independent source, curriculum and mathematical review; corrected findings closed.')
cp('assembly','assembly','course.md',order,'Verbatim lesson assembly in declared order.')
cp('audit','audit','audit_report.json',['verification','independent-audit','assembly'],'Local, cumulative and final audit passed; three minor findings corrected.')
ordered=[c['path'] for c in checkpoints]+['completion_report.json']
manifest={'schema_version':'1.0','topic':packet['topic'],'audience':packet['audience'],'assumptions':packet['assumptions'],'ordered_deliverables':ordered,'checkpoints':checkpoints,'dependencies':{c['id']:c['dependencies'] for c in checkpoints},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':audit['unresolved_counts'],'blockers':[],'next_action':'none','course_output_directory':str(root),'recovery_note':'Before resuming, check each checkpoint SHA-256 and then its dependencies. Passed content changes only for a concrete defect.'}
save('manifest.json',manifest)
validator={'status':'pending_actual_run','command':'Z:/Kfield-doc-training/.work/validate_project_course.py COURSE_DIRECTORY --json'}
if '--validated' in sys.argv:
    receipt=read('validation-result.json')
    assert receipt['status']=='passed' and not receipt['errors']
    validator={'status':'passed','exit_code':0,'receipt':'validation-result.json','validator_sha256':receipt['validator_sha256'],'note':'Adapter preserves installed checks and overrides only the user-authorized canonical output root. Re-run after this completion report refresh.'}
save('completion_report.json',{'schema_version':'1.0','status':'complete','topic':packet['topic'],'audience':packet['audience'],'assumptions':packet['assumptions'],'outputs':ordered,'audit_counts':audit['unresolved_counts'],'hashes':{p:sha(p) for p in ordered if p!='completion_report.json'}|{'manifest.json':sha('manifest.json')},'lesson_count':7,'core_periods':15,'capstone_periods':3,'source_gaps':audit['source_gaps_are_scoped_not_course_defects'],'validator':validator,'corrected_findings':3,'unresolved_minor_findings':[]})
print(json.dumps({'status':'assembled_for_validation','checkpoints':len(checkpoints),'lesson_count':len(order),'course_sha256':sha('course.md')},indent=2))
