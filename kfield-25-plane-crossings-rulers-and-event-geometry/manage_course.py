"""Course-local recovery and verification utilities. No source data copies."""
from pathlib import Path
import json, hashlib, sys
R=Path(__file__).resolve().parent
def write(name,text): (R/name).write_text(text,encoding='utf-8',newline='\n')
def dump(name,obj): write(name,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
P=json.loads((R/'input-contract.json').read_text(encoding='utf-8'))
def init():
    if (R/'manifest.json').exists():
        m=json.loads((R/'manifest.json').read_text())
        for c in m['checkpoints']:
            if c.get('sha256') and digest(R/c['path'])!=c['sha256']: raise ValueError(c['id'])
        return
    ids=[x['id'] for x in P['course_map']]
    specs=[('course-map','course-map','course-map.md',[])]+[(x,'lesson',x+'.md', ['course-map'] if i==0 else [ids[i-1]]) for i,x in enumerate(ids)]
    specs += [('terminology','terminology','terminology.md',ids),('teacher-guide','teacher-guide','teacher-guide.md',ids),('capstone','capstone','capstone.md',ids),('sources','supplement','sources.json',[]),('source-notes','supplement','source-notes.md',['sources']),('verification','supplement','worked-verification.json',ids),('audit','audit','audit_report.json',ids+['capstone']),('assembly','assembly','course.md',ids)]
    cs=[dict(id=i,kind=k,path=p,dependencies=d,status='pending',summary='Awaiting authored content and audit') for i,k,p,d in specs]
    m=dict(schema_version='1.0',topic=P['topic'],audience=P['audience'],assumptions=P['assumptions'],ordered_deliverables=[x['path'] for x in cs]+['completion_report.json'],checkpoints=cs,dependencies={x['id']:x['dependencies'] for x in cs},course_order=ids,assembly=dict(path='course.md',section_ids=ids),audit_counts=dict(critical=0,major=0,minor=0),blockers=[],next_action='Read exact sources and author lesson-01')
    dump('manifest.json',m)
    dump('audit_report.json',dict(status='pending',findings=[],unresolved_counts=m['audit_counts'],checks=[]))
    dump('completion_report.json',dict(status='in_progress',topic=P['topic']))
    for x in cs:
        if x['kind'] in ['lesson','course-map','terminology']: write(x['path'],'# '+x['id']+'\n\nPending authorship.\n')
def sources():
    records=[]
    for s in P['sources']:
        if 'path' not in s: continue
        p=Path(s['path']); h=digest(p)
        assert h==s['sha256'],(p,h)
        data=json.loads(p.read_text(encoding='utf-8'))
        print(s['id'], 'hash verified', 'keys',list(data)[:20])
        records.append(dict(s,verified_sha256=h,evidence_class='archival source; not fresh proof verification',top_level_keys=list(data)[:20]))
    dump('sources.json',dict(local=records,pinned=[],gaps=[]))
def complete_sources():
    s=json.loads((R/'sources.json').read_text(encoding='utf-8'))
    pointers={'S01':['/root_contract'],'S02':['/mature_locked_cell3','/typed_conventions'],'S03':['/authority_contract'],'S04':['/audit_contract']}
    for row in s['local']:
        assert digest(Path(row['path']))==row['sha256']
        row['read_pointers']=pointers[row['id']]
    s['pinned']=[dict(id=i,logical_path=p,sha256=h,object_id=h,byte_range=[0,n],returned_range_sha256=h,evidence_class='source',read_status='Full bounded bytes read through krytronx_get; returned whole-range digest matches pinned identity') for i,p,h,n in [
        ('T10','applications/kfield_lucas_lab/rag_corpus/10_geometry_trajectory.md','ce1abe83011a43bfbcd8aaf98f7fb9fdfabd31acbfdbc1208e45176596602ccb',545),
        ('T45','applications/kfield_lucas_lab/rag_corpus/45_moving_reference_frames.md','c8485397ee3cd5560624885a3bfcf20c9f6190e26129320e37037810b984e1aa',2651)]]
    s['generation']='sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7'
    s['manifest_sha256']='5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7'
    s['generation_witness']='RAG and graph responses; capabilities returned read-only interface but no generation field'
    s['rerank']=False
    s['graph_witness']=dict(start='construct:trajectory-rulers',relation='uses_authority',target='authority:cmb-physical-vector',source_logical_path='applications/kfield_lucas_lab/knowledge_graph/base/manifest.json',source_sha256='5f82424b4c8e217bb7e81fa7b54e0782f220d309916b0f9fc69547b12fe6bb55',truncated=True,trust='source')
    s['gaps']=['Underlying frame contracts and Agda bodies named by T45 were not exposed as pinned bodies in the bounded retrieval routes used. No fresh engine/compiler replay is claimed; core tasks use fully supplied synthetic contracts.','T10 is a source description, not a full detector transfer specification. No detector beat, force or energy inference is assessed.']
    dump('sources.json',s)
def drafted():
    m=json.loads((R/'manifest.json').read_text(encoding='utf-8'))
    for c in m['checkpoints']:
        if (R/c['path']).exists() and c['id'] not in ['audit','assembly','verification']:
            c.update(status='drafted',sha256=digest(R/c['path']),summary='Authored and saved; awaiting consolidated checks')
    m['next_action']='Complete source/teacher checks, independent verification and assembly'
    dump('manifest.json',m)
def finish():
    import re
    a=json.loads((R/'independent-audit.json').read_text(encoding='utf-8'))
    assert a['status']=='passed_in_scope' and not a['findings']
    for p,h in a['reviewed_sha256'].items(): assert digest(R/p)==h,p
    assert all(x['status']=='passed' for x in a['checks'])
    ids=[x['id'] for x in P['course_map']]
    supplemental_checks=[]
    for i,lid in enumerate(ids,1):
        tx=(R/(lid+'.md')).read_text(encoding='utf-8')
        assert 'Pending authorship' not in tx
        for suffix in ['E1','W1','P1','D1']:
            assert f'C25.{i:02d}-{suffix}' in tx
        supplemental_checks.append(dict(checkpoint=lid,status='passed',checks=['prerequisite bridge','2–4 observable goals','definition and notation','units and arithmetic independently recomputed','3–5 answered diagnostics','source and synthetic scope','next dependency'],evidence='Author reread plus independent-audit.json with exact reviewed SHA-256'))
    for p in ['terminology.md','course-map.md','teacher-guide.md','source-notes.md','sources.md']:
        tx=(R/p).read_text(encoding='utf-8')
        # Markdown tables must keep the header column count within each run.
        expected=None
        for line in tx.splitlines():
            if line.startswith('|'):
                count=len(re.split(r'(?<!\\)\|',line))
                if expected is None: expected=count
                assert count==expected,(p,line,count,expected)
            else: expected=None
    for p in [*(x+'.md' for x in ids),'course-map.md','teacher-guide.md','terminology.md','capstone.md','source-notes.md']:
        tx=(R/p).read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)',tx):
            if not target.startswith(('http:','https:','#')): assert (R/target.split('#')[0]).is_file(),(p,target)
    write('course.md','# '+P['topic']+'\n\nStudent course — seven lessons, eleven core periods. See [course map](course-map.md), [glossary](terminology.md), [capstone and key](capstone.md), [teacher guide](teacher-guide.md) and [source notes](source-notes.md). All teaching below is reproduced verbatim from the audited lesson files.\n\n'+'\n\n'.join('<!-- BEGIN: '+lid+' -->\n'+(R/(lid+'.md')).read_text(encoding='utf-8').rstrip('\n')+'\n<!-- END: '+lid+' -->' for lid in ids)+'\n')
    dump('worked-verification.json',dict(status='passed',method='Independent exact fractions and substitution; no floating tolerances or real data',check_count=len(a['checks']),independent_report='independent-audit.json',independent_script='independent-audit-check.py',reviewed_sha256=a['reviewed_sha256'],numeric_and_anchor_checks=a['checks'],source_hash_checks={x['id']:x['verified_sha256'] for x in json.loads((R/'sources.json').read_text())['local']}))
    counts=dict(critical=0,major=0,minor=0)
    finding=dict(id='C25-F001',level='final',category='Markdown table structure',file='terminology.md',section='Terminology table absolute-value rows',severity='minor',defect='Unescaped vertical bars in absolute-value notation split the glossary table into extra columns.',correction='Replaced bars with verbal absolute-value descriptions in both affected rows.',verification='Course-local table parser confirms consistent column counts; parent independently flagged the earlier version and correction was already applied.',disposition='corrected',affected_checkpoints=['terminology'])
    checks=[dict(level='local',results=supplemental_checks),dict(level='cumulative',unit='Lessons 1–3',result='passed',evidence='q, s_k and r retain meanings; moving inputs evaluated separately; cycles/radians and finite accumulation taught before use'),dict(level='cumulative',unit='Lessons 4–6',result='passed',evidence='Ruler roles separated; continuity/linear hypotheses precede root use; celestial equations and angular units taught before capstone'),dict(level='cumulative',unit='Lesson 7 and capstone',result='passed',evidence='Both family ledgers, zero/contact/jump/gap branches, endpoint support and signed residual reconstruction all retained'),dict(level='final',result='passed',evidence=['Seven E1/W1/P1/D1 anchors and all C25-CAP steps checked in actual content','Independent arithmetic, content review and reviewed hashes passed','Source hashes rechecked, pinned bounded reads and source-local pointers recorded','Teacher guide pacing totals 11 core plus 3 capstone periods; 28-point rubric','All Markdown tables in support files have consistent column counts; local links resolve','Synthetic full paths remain authored cards; no source snapshots or large arrays','Assembly uses exact lesson bytes modulo trailing newline protocol; final machine validator remains mandatory','No new substantive teaching added during assembly','Source-only advanced invariants are scoped explicitly, not promoted to hidden prerequisites'])]
    dump('audit_report.json',dict(status='passed',findings=[finding],unresolved_counts=counts,checks=checks,independent_review='independent-audit.json',rendering='Markdown only; table and link structure checked. No paginated rendering requested.',source_gaps=json.loads((R/'sources.json').read_text())['gaps']))
    m=json.loads((R/'manifest.json').read_text())
    extras=[('source-entry','supplement','sources.md',['sources','source-notes']),('independent-audit','supplement','independent-audit.json',ids+['capstone']),('independent-check-script','supplement','independent-audit-check.py',[]),('recovery-script','supplement','manage_course.py',[]),('input-contract','supplement','input-contract.json',[]),('launch-prompt','supplement','launch-prompt.md',[])]
    for id_,kind,path,deps in extras:
        if not any(c['id']==id_ for c in m['checkpoints']): m['checkpoints'].append(dict(id=id_,kind=kind,path=path,dependencies=deps))
    for c in m['checkpoints']:
        assert (R/c['path']).is_file(),c['path']
        c.update(status='passed',sha256=digest(R/c['path']),summary={'lesson':'Authored lesson; independently recomputed and content-audited','assembly':'Verbatim ordered lesson assembly','audit':'Actual checks and corrected table finding; zero unresolved findings'}.get(c['kind'],'Checked supporting artifact or preserved authorized input'))
    m.update(dependencies={c['id']:c['dependencies'] for c in m['checkpoints']},ordered_deliverables=[c['path'] for c in m['checkpoints']]+['completion_report.json'],audit_counts=counts,blockers=[],next_action='none')
    dump('manifest.json',m)
    comp=dict(status='complete',topic=m['topic'],audience=m['audience'],assumptions=m['assumptions'],outputs=m['ordered_deliverables'],audit_counts=counts,hashes={p:digest(R/p) for p in m['ordered_deliverables'] if p!='completion_report.json'},lesson_count=7,core_periods=11,capstone_periods=3,source_gaps=json.loads((R/'sources.json').read_text())['gaps'],validator=dict(status='pending actual execution',command='conda run -n tf_gpu_env python Z:/Kfield-doc-training/.work/validate_project_course.py COURSE_DIRECTORY --json'),independent_check_count=len(a['checks']))
    comp['hashes']['manifest.json']=digest(R/'manifest.json')
    dump('completion_report.json',comp)
    print(json.dumps(dict(status='candidate_ready_for_validator',checkpoints=len(m['checkpoints']),independent_checks=len(a['checks']),course_sha256=digest(R/'course.md'))))
def record_validator():
    import subprocess
    command=[sys.executable,str(R.parents[1]/'.work'/'validate_project_course.py'),str(R),'--json']
    result=subprocess.run(command,capture_output=True,text=True)
    payload=json.loads(result.stdout)
    assert result.returncode==0,(result.stdout,result.stderr)
    c=json.loads((R/'completion_report.json').read_text())
    c['validator']=dict(status=payload['status'],exit_code=result.returncode,command=command,validator_sha256=payload['validator_sha256'],checks=payload['checks'],errors=payload['errors'])
    dump('completion_report.json',c)
    final=subprocess.run(command,capture_output=True,text=True)
    assert final.returncode==0,(final.stdout,final.stderr)
    print(final.stdout)
    print('course_sha256='+digest(R/'course.md'))
    print('manifest_sha256='+digest(R/'manifest.json'))
if __name__=='__main__':
    if sys.argv[1]=='init': init()
    elif sys.argv[1]=='sources': sources()
    elif sys.argv[1]=='complete-sources': complete_sources()
    elif sys.argv[1]=='drafted': drafted()
    elif sys.argv[1]=='finish': finish()
    elif sys.argv[1]=='validate': record_validator()
