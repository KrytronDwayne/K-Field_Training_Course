from pathlib import Path
import json, hashlib
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parent
def write(p,s): (ROOT/p).write_text(s,encoding='utf-8')
def save(p,o): write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
lessons=[f'lesson-{i:02}' for i in range(1,7)]
def initialize():
    if (ROOT/'manifest.json').exists():
        m=json.loads((ROOT/'manifest.json').read_text())
        for c in m['checkpoints']:
            if c.get('sha256'): assert digest(ROOT/c['path'])==c['sha256'],c['id']
        return
    cps=[]
    specs=[('map','course-map','course-map.md',[])]+[(s,'lesson',s+'.md',[lessons[i-1]] if i else ['map']) for i,s in enumerate(lessons)]+[('terms','terminology','terminology.md',lessons),('teacher','teacher-guide','teacher-guide.md',lessons),('capstone','capstone','capstone.md',lessons),('sources','supplement','sources.md',[]),('verification','supplement','verification.json',lessons),('assembly','assembly','course.md',lessons),('audit','audit','audit_report.json',['assembly','capstone'])]
    for ident,kind,path,deps in specs:
        cps.append(dict(id=ident,kind=kind,path=path,dependencies=deps,status='pending',summary='Awaiting production and verification'))
        if not (ROOT/path).exists(): write(path,'# Pending\n' if path.endswith('.md') else '{}\n')
    m=dict(schema_version='1.0',topic=packet['topic'],audience=packet['audience'],assumptions=packet['assumptions'],ordered_deliverables=[c['path'] for c in cps]+['completion_report.json'],checkpoints=cps,dependencies={c['id']:c['dependencies'] for c in cps},course_order=lessons,assembly=dict(path='course.md',section_ids=lessons),audit_counts=dict(critical=0,major=0,minor=0),blockers=[],next_action='Verify sources and draft lesson-01')
    save('manifest.json',m); save('audit_report.json',dict(status='pending',findings=[],unresolved_counts=m['audit_counts']));save('completion_report.json',dict(status='in_progress'))
def sources():
    rows=[]
    for s in packet['sources']:
        actual=digest(Path(s['path'])); assert actual==s['sha256'],s['id']
        rows.append(f"| {s['id']} | `{s['path']}` | `{actual}` |")
    s2=json.loads(Path(packet['sources'][1]['path']).read_text(encoding='utf-8'),parse_float=str)
    s3=json.loads(Path(packet['sources'][2]['path']).read_text(encoding='utf-8'),parse_float=str)
    result=s2['backbone_sequence'][1]['result']; stale=s2['backbone_sequence'][1]['reciprocal_witness']
    cards=[]
    for i,axis in enumerate(['u','v','w']):
        cards.append(f"| {axis} | ({', '.join(result['reciprocal_normals_u_v_w'][i])}) | {result['reciprocal_spacings_u_v_w_nm'][i]} |")
    table='| Axis | Canonical unit normal, ICRS components | Canonical spacing (nm) |\n|---|---|---|\n'+'\n'.join(cards)
    write('sources.md','# Source register and branch contract\n\nAll five supplied files were read in place for SHA-256 verification; no raw snapshots were saved. S02 and S03 supply the exact passages taught here. S01, S04 and S05 are provenance context, not additional mathematical premises.\n\n| ID | Absolute source path | Verified SHA-256 |\n|---|---|---|\n'+'\n'.join(rows)+'''\n\n## Exact pointers and evidence scope

- S02 `/proof_contract`: ICRS columns [a b c], intentional negative determinant, half-open boundary and information retention.
- S02 `/backbone_sequence/1`: M02, requiring M01; definitions of affine address, owner, local coordinate and reciprocal vectors. Its printed proof omits the origin in one plane equation; the course consistently uses the explicit affine form mandated by SA-04: g_h dot (x-O_K)=m.
- S02 `/backbone_sequence/1/result/reciprocal_normals_u_v_w` and `/backbone_sequence/1/result/reciprocal_spacings_u_v_w_nm`: canonical active decimals below, preserved lexically in u,v,w order.
- S02 `/mature_locked_cell3`: matching canonical fields; B_nm contains matrix rows, whose columns are a,b,c. The normals array instead lists one normal per row in u,v,w order. Do not transpose one merely because the other is a matrix.
- S02 `/backbone_sequence/1/reciprocal_witness`: superseded branch. S03 `/findings/4` identifies AUD-005, SUPERSEDED_NUMERIC_WITNESS. It requires matching canonical spacings and normals; displaced values are provenance, not measured residuals.

'''+table+f'''\n\nSuperseded comparison card: u spacing `{stale['u']['spacing_nm']}` nm, S02 `/backbone_sequence/1/reciprocal_witness/u/spacing_nm`. Canonical u spacing `{result['reciprocal_spacings_u_v_w_nm'][0]}` nm. Their difference records a branch change, not a sensor fluctuation. The canonical field is active even though the discrepancy is small.

Source evidence class: archival mathematical definitions, numerical witnesses and source-reported proof status. This course freshly derives the finite synthetic identities; it does not newly verify the source's entire closure theorem. No empirical measurements or physical mechanism are asserted by the toy examples. The locked numerical cards are read at stored precision, not treated as exact rational measurements.

Krytronx capabilities was called read-only. Its response exposed canonical application digest `88c14424210ac18e902f33f5330a208a1c547a0e1d763a6b941c3e9de7c812ac` but no corpus-generation digest. Therefore the packet's frozen generation `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7` remains packet-reported, not freshly confirmed by that response. Exact teaching content is grounded in the directly hash-verified archival files, without a graph-freshness assertion.

The source marks its contents Proprietary Confidential Information and Trade Secret of Krytronx, LLC; retain that source classification and do not publish this course without appropriate authority.
''')
    return table
if __name__=='__main__':
    initialize()
    table=sources()
    write('canonical-card.md',table+'\n')
    print('Recovery initialized; five source hashes verified; canonical teaching card generated.')
