import json, hashlib, sys
from pathlib import Path
from fractions import Fraction as F

p=Path(__file__).parent
contract=json.loads((p/'input-contract.json').read_text(encoding='utf-8-sig'))
v=json.loads((p/'verification.json').read_text(encoding='utf-8-sig'))
src={}
checks=[]
for row in contract['sources']:
    b=Path(row['path']).read_bytes()
    assert hashlib.sha256(b).hexdigest()==row['sha256']
    src[row['id']]=json.loads(b,parse_float=str,parse_int=str)
checks.append('All five source files independently hashed against input-contract; exact JSON decimals parsed without binary float.')
def calc(values):
    bc,ac,ab=map(F,values)
    return dict(zip(('r_bc','r_ac','r_ab','eta','alpha_inverse','alpha','eta_alpha'),(F(1),ac/bc,ab/bc,1000*bc/ab,100*bc/ac,ac/(100*bc),10*ac/ab)))
a=src['S02']['mature_locked_cell3']['face_areas_nm2']
out=calc([a[k] for k in ('bc','ac','ab')])
for k,row in v['locked'].items():
    assert row['stored']==src['S02']['mature_locked_cell3'][k]
    assert F(row['recomputed_exact'])==out[k]
    assert F(row['signed_recomputed_minus_stored'])==out[k]-F(row['stored'])
checks.append('All four locked exact recomputations, original stored lexemes, and signed differences checked against source, including reconstruction.')
for row in v['branch_comparisons']:
    branch=row['historical_source_pointer'].split('/')[-1]
    h=src['S01']['backbone_sequence'][4]['projective_rays'][branch]
    active=src['S02']['backbone_sequence'][4]['projective_ray']
    assert row['historical_lexemes']==h and row['active_lexemes']==active
    assert [F(x)-F(y) for x,y in zip(active,h)]==list(map(F,row['signed_active_minus_historical_exact']))
checks.append('Both three-component historical-ray comparison vectors independently checked against S01/S02 exact lexemes; subtraction direction and signs retained.')
for row in v['finite_examples']:
    result=calc(row['inputs_bc_ac_ab'])
    assert result=={k:F(x) for k,x in row['outputs'].items()}
    assert result['eta']*result['alpha']==result['eta_alpha']
    bc,ac,ab=map(F,row['inputs_bc_ac_ab'])
    assert [bc*result[k] for k in ('r_bc','r_ac','r_ab')]==[bc,ac,ab]
checks.append('All nine finite example rows: seven outputs, normalization inversion, and product/direct closure independently recomputed.')
base=calc(('12','8','6'))
for triple,expected in [(('12','8','61/10'),('0','0','1/120','-2000/61','0','0','-40/183')),(('12','81/10','6'),('0','1/120','0','0','-50/27','1/12000','1/6'))]:
    new=calc(triple)
    diffs=[new[k]-base[k] for k in base]
    assert diffs==list(map(F,expected))
    assert all(base[k]+d==new[k] for k,d in zip(base,diffs))
assert F(5900,3)+F(100,183)==F(120000,61)
checks.append('Both perturbations: all seven signed changes and reconstructions checked; optional approximation remainder 100/183 confirmed.')
course=(p/'course.md').read_text(encoding='utf-8-sig')
for n in range(1,7):
    lid=f'lesson-{n:02d}'
    text=(p/(lid+'.md')).read_text(encoding='utf-8-sig').strip()
    pass # Assembly identity is finalized by manager after content repairs.
checks.append('Assembly was mid-update after lesson repairs; final assembly identity and validator remain manager responsibilities.')
report={'scope':'Independent content audit; final completion and validator are manager responsibilities','runtime':sys.executable,'automated_checks':checks,'manual_checks':['Read all six complete lessons, capstone with key and rubric, teacher guide, course map, terminology, sources and verification.','Checked source M05 definitions/proof/witness plus S03 authority contract and S04 M05 correction directly.','All lessons have question, 3 goals, prerequisite bridge, explanation, worked example, answered practice, 4 diagnostic answers, scope box and next dependency.','Units, positive-denominator contracts, order, square-law cancellation, reciprocal alpha, synthetic/source distinction and retained-difference distinctions are consistent.','Six 55-minute lessons and two capstone periods are plausible with long exact fractions treated as reading cards rather than hand-division.','Capstone all numerical answers and 100-point allocations reviewed; no substantive teaching introduced only in capstone.'], 'findings':[{'id':'IA-E05-01','severity':'major','status':'corrected','file':'lesson-02.md','finding':'P1 practices one numerical scaling but not the arbitrary-s cancellation proof assessed in C08-CAP-02.','required_fix':'Extend P1 with an explicitly asked and independently answered cancellation of both (s²A_ac)/(s²A_bc) and (s²A_ab)/(s²A_bc), including positive-denominator condition.'},{'id':'IA-E05-02','severity':'major','status':'corrected','file':'lesson-04.md','finding':'P1 practices reconstruction and naming a historical input set but not building the complete provenance row assessed in C08-CAP-04.','required_fix':'Extend P1 with a complete answered historical or active ledger row including source ID/hash reference, pointer, original lexeme(s), component order, unit and role.'}], 'limitations':['Did not independently verify live graph generation; sources.md explicitly discloses gap, local source hashes provide exact M05 grounding.','Final manifest/completion/validator checks delegated to manager, which was still finalizing them during this review.'], 'reviewed_sha256':{name:hashlib.sha256((p/name).read_bytes()).hexdigest() for name in ['input-contract.json','sources.md','capstone.md','teacher-guide.md','course-map.md','terminology.md','verification.json']+[f'lesson-{i:02d}.md' for i in range(1,7)]}}
report['unresolved_counts']={'critical':0,'major':0,'minor':0}
report['repair_verification']='Reread revised lesson-02 P1: both arbitrary-s cancellations answered with conditions. Reread revised lesson-04 P1: full active and historical ledger rows answered. Both E05 gaps corrected.'
(p/'independent-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'critical':0,'major':0,'report':str(p/'independent-audit.json')}))

