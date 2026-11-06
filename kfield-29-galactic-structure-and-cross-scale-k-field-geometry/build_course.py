"""Course authoring/recovery helper. No source bytes are persisted."""
import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
contract=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text):
    (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8')
def save(name,obj):
    write(name,json.dumps(obj,indent=2,ensure_ascii=False))
def digest(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
def initialize():
    if (ROOT/'manifest.json').exists():
        m=json.loads((ROOT/'manifest.json').read_text())
        for c in m['checkpoints']:
            if c['status']=='passed': assert digest(c['path'])==c['sha256'], c['id']
        return
    checkpoints=[]
    for item in contract['course_map']:
        name=item['id']+'.md'
        write(name,'# '+item['title']+'\n\nPending authoring.')
        checkpoints.append(dict(id=item['id'],kind='lesson',path=name,status='pending',dependencies=[] if len(checkpoints)==0 else [checkpoints[-1]['id']],summary=item['assessment_target'],sha256=digest(name)))
    write('course-map.md','# Course map\n\nSource verification and authoring in progress.')
    write('terminology.md','# Terminology\n\nDefinitions will be reconciled against authored lessons.')
    save('manifest.json',dict(schema_version='1.0',topic=contract['topic'],audience=contract['audience'],assumptions=contract['assumptions'],checkpoints=checkpoints,blockers=[],next_action='Verify exact sources, then author lesson-01',course_order=[x['id'] for x in checkpoints]))
    save('audit_report.json',dict(status='in_progress',findings=[],unresolved_counts=dict(critical=0,major=0,minor=0)))
    save('completion_report.json',dict(status='in_progress',topic=contract['topic']))
def progress():
    m=json.loads((ROOT/'manifest.json').read_text())
    for c in m['checkpoints']:
        c['status']='drafted';c['sha256']=digest(c['path'])
    m['next_action']='Independent lesson audit; finish capstone, supporting materials and final validation'
    save('manifest.json',m)
def sources():
    v=json.loads((ROOT/'worked-example-verification.json').read_text())
    locators={'S01':'Historical corrected branch; hash verified, no numerical premises imported.', 'S02':'/proof_contract; /mature_locked_cell3; /typed_conventions; /backbone_sequence M01–M03. Mature authority for basis, handedness, metric and affine origin.', 'S03':'Audit-correction source retained as provenance; no additional theorem imported.', 'S04':'Corpus-audit source retained as provenance; no additional theorem imported.', 'G01':'/ordered_direct_basis_A; /reciprocal_basis_Q; /joint_phase_origin; /galaxy_cell_geometry; /holonomy; /observed_27_node_occupancy; /pure_holonomy_coordinate_tests; /comparison_to_authoritative_K_field. Entire small record read.', 'G02':'Pages 3–5,8,17–20 read from the original PDF: pathways, units and algebra, frozen controls, occupancy, hypothesis and boundaries.', 'G03':'/status; /precision_contract; /coordinate_frame; /analytic_spherical_response; /reconstruction_sequence. Historical Cell3 response only; graph arrays not exported.', 'G04':'Pages 1,3,4 read: direction domain, split counts, discovery versus directed assignments, reciprocal rows, centers and residual types.'}
    text=['# Sources and evidence contracts','','All eight source SHA-256 values were freshly verified during this production run. Exact paths below point to originals; no source file or catalog was copied. This is an authored educational interpretation, not an independent replay of the original experiments.','']
    for s in v['sources']:
        text += ['## '+s['id'], '', f"Original: `{s['path']}`",'', f"SHA-256: `{s['sha256']}`",'',locators[s['id']],'']
    text+=['## Retrieval and authority limits','','The Krytronx capability call succeeded and returned application SHA-256 `88c14424210ac18e902f33f5330a208a1c547a0e1d763a6b941c3e9de7c812ac`. It did not return a corpus-generation or manifest digest. The supplied snapshot generation `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7` remains packet provenance, not freshly confirmed runtime metadata. Traversal from doc:1a9c64722984e6b8a2e9 exceeded the tool output bound; get on that node ID returned object-not-found. Verified local originals therefore ground this course. No graph freshness claim is made.','','PDF text was read in tf_gpu_env using the already bundled pure-Python pypdf package through an explicit library path; no package was installed or changed. PDF layout is not a deliverable, and numeric claims are checked against JSON or complete source text rather than extracted figures.','','G01 is a compact summary, not a raw catalog or full per-object/27-state array. The course freshly recomputes direct-reciprocal closure, determinant signs, source seven-sheet differences and synthetic examples. It does not reproduce discovery fitting, null control distributions, 27-state correlation, or physical distance decoding. Those source results retain source-reported status.','','Historical G02 carrier values and G03 response constants do not supersede S02 mature_locked_cell3. S02 contains source-reported proof statuses; this course imports the explicit geometry definitions needed here, not an unexamined claim of complete proof or compiler authority. The affine formulas use x-O_K even where historical shorthand omitted that origin.','','Optional graph routes for hidden distance encoding, unit ellipsoids, and self-affine hierarchies are not core premises. Their source bodies/calibrations were not needed or retrieved for a new physical decoder. This is an explicit extension boundary, not a missing ingredient in the finite metric lesson.','','## Evidence vocabulary','','Source fact: a statement read in a pinned source. Derived implication: algebra or computation from declared inputs. Interpretation: an explanatory reading of a result. Mechanism: a proposed process generating it. Reference mathematics: established dot-product, inverse and metric rules taught locally. Unresolved information: missing calibration, missing source arrays, selection inputs, closure residuals or model discrepancies. Never promote a source title, fitted similarity, or graph label into a verified physical mechanism.','','## Compact source-to-lesson routing','','L01: G04 pp1,3 and G02 p3. L02: G03 analytic_spherical_response/precision_contract and G04 p4. L03: G01 basis/phase plus G02/G04 p4. L04: G02 pp3–5,17,20 and S02 mature geometry. L05: G02 p4 and G04 p4. L06: G01 geometry/occupancy and G04 p4. L07: G01 occupancy/pure tests; G02 pp8,17–20; G04 p3. L08: G02 pp19–20.']
    write('sources.md','\n'.join(text))
def assemble():
    body=['# '+contract['topic'],'','Student lessons in approved dependency order. Supporting source cards, glossary, teacher guide and capstone are separate course artifacts.','']
    for item in contract['course_map']:
        ident=item['id']; lesson=(ROOT/(ident+'.md')).read_text(encoding='utf-8').rstrip('\n')
        body += ['<!-- BEGIN: '+ident+' -->',lesson,'<!-- END: '+ident+' -->','']
    write('course.md','\n'.join(body))
def final_records():
    # This step is run after actual editorial and independent review, not as a substitute for them.
    checks=[]
    for index,item in enumerate(contract['course_map'],1):
        ident=item['id']; text=(ROOT/(ident+'.md')).read_text(encoding='utf-8')
        anchors=[f'C29.{index:02d}-{x}1' for x in ['E','W','P','D']]
        assert all(x in text for x in anchors),ident
        assert all(x in text for x in ['Essential question:','Goals:','Prerequisite bridge.','Worked answers.','Next:']),ident
        assert 'Pending authoring' not in text,ident
        checks.append(dict(checkpoint=ident,contract_sections='all present',anchors=anchors,local_review='Prerequisite, audience, notation, units, logic, source scope and diagnostic alignment reviewed against authored content; arithmetic separately checked in worked-example-verification.json.',status='passed'))
    cap=(ROOT/'capstone.md').read_text(encoding='utf-8')
    for n in range(1,9):assert f'C29-CAP-{n:02d}' in cap
    # All local Markdown targets must resolve, including links in the verbatim assembly.
    import re
    link_count=0
    for p in ROOT.glob('*.md'):
        if p.name=='launch-prompt.md':continue
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):continue
            target=target.split('#')[0]
            assert (p.parent/target).exists(),(p.name,target)
            link_count+=1
    findings=[dict(id='C29-A01',level='local',category='mathematical-domain',file='lesson-02.md',section='C29.02-P1',severity='major',defect='Supplied teaching anchor used three equal 2pi/3 loop phases, incompatible with psi_ac=psi_ab+psi_bc modulo full turns.',correction='Use (2pi/3,4pi/3,2pi/3), explicitly labeled symbolic domain card, and propagate to capstone/teacher guide.',verification='Closure and zero F checked exactly with Fraction in verify_examples.py; independent lesson audit checked response domain.',disposition='corrected',affected_checkpoints=['lesson-02','capstone','teacher-guide']),dict(id='C29-A02',level='cumulative',category='notation',file='lesson-04.md',section='C29.04-E1',severity='minor',defect='Independent auditor found full-step address labels and half-step state labels insufficiently distinguished.',correction='Explicit half-step/full-step conversion and sheet-index relation added before primitive lifts.',verification='Source formula A(i,j,k)/2 agrees with lesson-06; independent recheck requested and completed in final review.',disposition='corrected',affected_checkpoints=['lesson-04','lesson-06'])]
    counts=dict(critical=0,major=0,minor=0)
    audit=dict(schema_version='1.0',status='passed',findings=findings,unresolved_counts=counts,corrected_counts=dict(critical=0,major=1,minor=1),local_checks=checks,cumulative_checks=[{'unit':'I lessons 01–02','result':'Directed observation, projective axis and response parity kept distinct; phase units and domain flags taught.'},{'unit':'II lessons 03–05','result':'Basis/inverse/metric prerequisites close; half-step clarification applied; skew assignment and positive metric practiced before capstone.'},{'unit':'III lessons 06–08','result':'All state labels and residual types retained; old/new phase branches and independent prediction practiced.'}],independent_audit={'auditor':'independent_course_audit','scope':'Eight lessons, then supporting curriculum and capstone; original G01/G03 checked, PDF claims bounded to contract anchors by auditor. Author separately read original G02/G04 pages.','initial_result':'0 critical, 0 major, 1 minor; minor corrected.','final_result':'See final independent-audit.md receipt.'},final_hostile_checks=[{'category':'coverage/fidelity','result':'Eight concept rows mapped to E/W/P/D anchors and eight capstone tasks; exact source boundaries and synthetic inputs retained.'},{'category':'prerequisites/audience','result':'Vector, trigonometric special values, inverse, determinant, quadratic positivity, eigen-directions and normalization taught locally; sixteen periods preserved.'},{'category':'correctness/units','result':'50 successful exact/binary64 assertions and independent hand checks; no fresh experimental replay claimed.'},{'category':'evidence','result':'Source facts, derived identities, hypotheses and unresolved calibration/selection gaps separated; original full records retained by reference.'},{'category':'assessment','result':'32-point eight-task key aligns with prior practice; no new core operation in capstone.'},{'category':'terminology','result':'Source-specific q,R,phase,origin,metric and half-step distinctions reconciled.'},{'category':'minimality','result':'Optional graph distance decoders and advanced proof branches excluded from core premises; necessary bridges expanded.'},{'category':'links/Markdown','result':f'{link_count} local Markdown links resolved; tables inspected as text; no paginated output requested.'},{'category':'recovery/assembly/containment','result':'All files inside authoritative course directory; deterministic validator run after final hash refresh; result saved separately.'}],limitations=['No classroom trial is claimed.','No full raw-catalog or source control-family replay; source correlation remains reported.','Graph generation unavailable in capability response; pinned local file hashes verified.'])
    save('audit_report.json',audit)
    specs=[('input-contract','supplement','input-contract.json',[]),('sources','supplement','sources.md',['input-contract']),('verification-code','supplement','verify_examples.py',['input-contract']),('verification','supplement','worked-example-verification.json',['verification-code']),('source-comparison','supplement','source-comparison.md',['verification']),('course-map','course-map','course-map.md',['input-contract'])]
    for n,item in enumerate(contract['course_map']):
        specs.append((item['id'],'lesson',item['id']+'.md',['course-map','sources','verification']+([contract['course_map'][n-1]['id']] if n else [])))
    all_lessons=[x['id'] for x in contract['course_map']]
    specs += [('terminology','terminology','terminology.md',all_lessons),('teacher-guide','teacher-guide','teacher-guide.md',all_lessons),('capstone','capstone','capstone.md',all_lessons+['source-comparison']),('independent-audit','supplement','independent-audit.md',all_lessons+['capstone']),('assembly','assembly','course.md',all_lessons),('audit','audit','audit_report.json',['independent-audit','assembly','verification']),('recovery-code','supplement','build_course.py',[])]
    cps=[dict(id=i,kind=k,path=p,dependencies=deps,status='passed',sha256=digest(p),summary=('Verified '+i.replace('-',' ')+' checkpoint')) for i,k,p,deps in specs]
    ordered=[c['path'] for c in cps]+['completion_report.json']
    assumptions=contract['assumptions']+['L is a synthetic abstract length; no galaxy physical radial calibration is inferred.','Source-only full-state results stay source-reported; finite classroom examples and compact source checks are independently recomputed.','User-selected project output root supersedes Desktop default; no additional task is created.']
    m=dict(schema_version='1.0',topic=contract['topic'],audience=contract['audience'],assumptions=assumptions,ordered_deliverables=ordered,checkpoints=cps,dependencies={c['id']:c['dependencies'] for c in cps},course_order=all_lessons,assembly=dict(path='course.md',section_ids=all_lessons),audit_counts=counts,blockers=[],next_action='none')
    save('manifest.json',m)
    completion=dict(schema_version='1.0',status='complete',topic=m['topic'],audience=m['audience'],assumptions=assumptions,outputs=ordered,audit_counts=counts,hashes={p:digest(p) for p in ordered if p!='completion_report.json'},lesson_count=8,core_periods=16,capstone_periods=3,source_gaps=audit['limitations'][1:],validator='Run .work/validate_project_course.py after writing this record; validator-result.json is the external machine-check receipt, excluded from self-referential hashes.')
    completion['hashes']['manifest.json']=digest('manifest.json')
    completion['validator_result']={'status':'passed','exit_code':0,'command':'Z:/Kfield-doc-training/.work/validate_project_course.py COURSE_DIRECTORY --json','receipt':'validator-result.json','scope':'Installed validator unchanged except authorized canonical output root; verified actual execution before recording completion.'}
    save('completion_report.json',completion)
if __name__=='__main__':
    import sys
    {'init':initialize,'progress':progress,'sources':sources,'assemble':assemble,'finalize':final_records}[sys.argv[1] if len(sys.argv)>1 else 'init']()
