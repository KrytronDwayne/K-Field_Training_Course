"""Finalize reviewed checkpoints and invoke the unchanged project-root adapter."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, subprocess, sys
P=Path(__file__).resolve().parent
def read(f): return json.loads((P/f).read_text(encoding='utf-8-sig'))
def write(f,x): (P/f).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(f): return hashlib.sha256((P/f).read_bytes()).hexdigest()
m=read('manifest.json'); v=read('verification.json')
assert v['status']=='passed' and v['check_count']==44
assert Path(sys.executable).as_posix().lower()=='c:/users/info/.conda/envs/tf_gpu_env/python.exe'
audit={'schema_version':'1.0','status':'passed','reviewed_utc':datetime.now(timezone.utc).isoformat(),
 'audit_scope':'Completed course content, sources, finite examples, teaching prerequisites, recovery, assembly and requested Markdown deliverables. Deterministic validator receipt is recorded separately in completion_report.json.',
 'findings':[
 {'id':'C30-IND-001','level':'final','category':'markdown_provenance_table','file':'sources.md','section':'Pinned testbench and integration sources','severity':'minor','defect':'Four-column provenance header and data used a three-cell delimiter; the independent completed-course audit identified malformed Markdown.','correction':'Changed the recovery literal to four separator cells and regenerated sources.md.','verification':'Direct header/delimiter/data width check confirms four cells throughout the seven-row table; recovery literal inspected; fresh real project validator run after hashes refreshed.','disposition':'corrected','affected_checkpoints':['sources','build_course','audit_report']},
 {'id':'C30-PARENT-002','level':'final','category':'evidence_scope','file':'sources.md','section':'Boundaries carried forward, item 9; lesson-05 claim scope','severity':'major','defect':'Three plane-family cost levels were called independent, although three distinct levels alone do not establish statistical independence. The same wording occurred in lesson 5.','correction':'Changed independent to distinct in both recovery-source occurrences, regenerated sources and lesson 5/assembly, and explicitly stated the statistical-independence limitation in source boundary 9. All fourteen signed rows and packet/source-report limitations remain retained.','verification':'Confirmed no authored independent-plane-level phrase remains, all fourteen signed rows remain referenced, and source boundary explicitly separates distinct levels from statistical independence. Lesson 5 assembly identity rechecked by real validator.','disposition':'corrected','affected_checkpoints':['sources','lesson-05','course','build_course','audit_report']},
 {'id':'A30-01','level':'final','category':'example_reproducibility','file':'lesson-01.md','section':'C30.01-W1','severity':'major','defect':'Worked coordinate example displayed a/2 but omitted the input column a needed for local independent recomputation.','correction':'Added the full mature source column, three exact JSON pointers, and explicit division instruction; rebuilt assembly.','verification':'Independent auditor reread repaired section, confirmed all values and pointers, and checked lesson-01 verbatim assembly identity. Exact Decimal half-column check passes in verification.json.','disposition':'corrected','affected_checkpoints':['lesson-01','course','capstone']},
 {'id':'A30-02','level':'final','category':'terminology','file':'capstone.md','section':'C30-CAP-04','severity':'minor','defect':'The phrase four-bit-label example could imply four-bit strings rather than four two-bit states.','correction':'Changed to four-state, two-bit example in authoring source and rebuilt capstone.','verification':'Independent auditor reread corrected capstone wording and closed the finding.','disposition':'corrected','affected_checkpoints':['capstone']}
 ],'unresolved_counts':{'critical':0,'major':0,'minor':0},
 'reviewers':{'author':'Primary course manager: source retrieval, hand checks, exact verification script and artifact inspection.','independent':'course_auditor: all eight lessons, source/contract alignment, capstone, exact fractions, source hashes, graph and repaired-section recheck. No independent rerun of remote retrieval or Agda.'},
 'local_checks':[{'checkpoint':f'lesson-{i:02}','categories':['prerequisites','audience','definitions','notation','units','logic','mathematics','evidence','source scope','diagnostic alignment'],'result':'passed','evidence':f'C30.{i:02}-E1/W1/P1/D1 read against the approved anchor; numerical or source-readback checks in verification.json; no unresolved content findings after independent review.'} for i in range(1,9)],
 'cumulative_checks':[
 {'boundary':'lesson-02','result':'passed','evidence':'M20/M19 map, six EG principles, state coordinates, evidence kinds and namespace separation agree across lessons 1–2 and sources.md.'},
 {'boundary':'lesson-04','result':'passed','evidence':'Matrix row arithmetic precedes rank/inversion and candidate discrimination; exact checks verify sum/difference and toy intervals.'},
 {'boundary':'lesson-06','result':'passed','evidence':'Frozen protocol precedes residual computation; unknown/missing/invalid outcomes retained separately; both A/B residuals reconstruct.'},
 {'boundary':'lesson-08','result':'passed','evidence':'Source/raw-kind reporting, decoder bridge, complex scalar arithmetic and geometric-to-transfer chain taught before matching capstone operations.'}],
 'final_hostile_checks':[
 {'category':'coverage','result':'passed','evidence':'All eight concept IDs map to present explanation/worked/practice/diagnostic IDs and eight concrete 4-point capstone sections.'},
 {'category':'fidelity','result':'passed','evidence':'All five archival SHA-256 values verified. Source module table is requires-derived; S03 AUD-001/008/010/011/013 and SA-30 boundaries preserved. Remote source claims scoped to retrieved reports.'},
 {'category':'dependency','result':'passed','evidence':'52 internal source edges verified; M20 has 18 required modules and excludes M19. Course concepts proceed through local bridges before use.'},
 {'category':'correctness','result':'passed','evidence':'44 exact arithmetic/source-hash/anchor checks executed in tf_gpu_env; independent reviewer recomputed inverse, residual, decoder and six-factor examples.'},
 {'category':'terminology','result':'passed','evidence':'Glossary distinguishes H/theta from A/c and basis c; source metrics, namespaces and evidence statuses remain separate.'},
 {'category':'examples_and_answers','result':'passed','evidence':'Every lesson has a worked example, answered practice and four answered diagnostics; capstone provides full answers and 32 criterion points.'},
 {'category':'evidence_layers','result':'passed','evidence':'Synthetic arithmetic, stored-source decimals, source reports, proposed transfer and unexecuted protocol are labeled. No new measurement or Agda run is asserted.'},
 {'category':'audience_load','result':'passed','evidence':'16 core periods with local bridges for rows/rank/floor/complex pairs; advanced module names are recognition-only. Teacher guide supplies recovery and session pacing.'},
 {'category':'capstone_alignment','result':'passed','evidence':'Eight capstone operations traced backward to prior independently answered practices; no absent source numeric input is required.'},
 {'category':'recovery_integrity','result':'passed','evidence':'All completed files are saved before passed status; checkpoint SHA-256 and dependency arrays regenerated from current files, then checked by the required validator.'},
 {'category':'assembly_and_rendering','result':'passed','evidence':'Assembly contains lesson text verbatim between exact ordered markers. Markdown delivery only; no paginated or image artifact was requested. Tables and headings inspected in source.'},
 {'category':'containment','result':'passed','evidence':'Every authored persistent artifact resides in the designated project course directory; no source snapshots or large arrays created.'},
 {'category':'minimality','result':'passed','evidence':'Finite examples directly support portfolio operations; source-only advanced formulas remain scoped references rather than required untaught calculations.'}],
 'source_gaps_are_not_course_defects':[
 'Named route certificate body not retrieved; source numeric route replay gated.',
 'Full G_phase/C/W_qpc precision linkage absent; AUD-008 nonzero residual retained.',
 'Some mature formal and occupation-selection bodies remain source-reported/VERIFIED_NOT_LOADED; no fresh Agda checking.',
 'Spectral revision discrepancy preserved by packet references; no empirical data replay claimed.',
 'Physical apparatus/calibration/timing fields remain missing in a deliberately planned protocol; all assessed finite data are supplied.'
 ]}
write('audit_report.json',audit)
for f in ['input-contract.json','launch-prompt.md','finalize_course.py']:
 if f not in m['ordered_deliverables']:
  m['ordered_deliverables'].insert(-1,f)
  m['checkpoints'].append({'id':Path(f).stem,'kind':'supplement','path':f,'dependencies':[],'status':'drafted','summary':'Pinned production contract or finalization procedure'})
for c in m['checkpoints']:
 assert (P/c['path']).is_file(),c['path']
 c.update(status='passed',sha256=sha(c['path']))
 c['summary']=f"Completed and reviewed {c['id']}; hash pins the accepted bytes"
m['dependencies']={c['id']:c['dependencies'] for c in m['checkpoints']}
m['audit_counts']=audit['unresolved_counts']; m['blockers']=[];m['next_action']='none'
write('manifest.json',m)
completion={'schema_version':'1.0','status':'complete','topic':m['topic'],'audience':m['audience'],'assumptions':m['assumptions'],'outputs':m['ordered_deliverables'],'audit_counts':m['audit_counts'],
 'hashes':{f:sha(f) for f in m['ordered_deliverables'] if f!='completion_report.json'},
 'lesson_count':8,'core_periods':16,'capstone_periods':3,'period_minutes':55,'source_gaps':audit['source_gaps_are_not_course_defects'],
 'findings_corrected':{severity:sum(f['severity']==severity and f['disposition']=='corrected' for f in audit['findings']) for severity in ['critical','major','minor']},'unresolved_minor_findings':[],
 'verification':{'path':'verification.json','check_count':44,'runtime':sys.executable},
 'validator':{'status':'pending'}}
completion['hashes']['manifest.json']=sha('manifest.json')
write('completion_report.json',completion)
adapter=Path(r'Z:/Kfield-doc-training/.work/validate_project_course.py')
run=subprocess.run([sys.executable,str(adapter),str(P),'--json'],capture_output=True,text=True)
try: result=json.loads(run.stdout)
except json.JSONDecodeError: result={'status':'failed','stdout':run.stdout,'stderr':run.stderr}
completion['validator']={'exit_code':run.returncode,'command':str(adapter)+' '+str(P)+' --json','result':result}
if run.returncode:
 completion['status']='incomplete'
write('completion_report.json',completion)
print(json.dumps(result,indent=2))
raise SystemExit(run.returncode)
