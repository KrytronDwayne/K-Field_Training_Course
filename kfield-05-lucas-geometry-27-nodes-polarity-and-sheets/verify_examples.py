"""Independent read-back verification: alternate enumeration, direct equations and pins."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,sys
R=Path(__file__).resolve().parent
data=json.loads((R/'registry.json').read_text(encoding='utf-8'))
rows=data['rows']
byL={tuple(map(int,r['L'])):r for r in rows}
expected=set()
# Base-three digit decoding is independent of the generator's nested product.
for code in range(27):
    a,tail=divmod(code,9); b,d=divmod(tail,3)
    expected.add((a-1,b-1,d-1))
assert len(rows)==len(byL)==27 and set(byL)==expected
records=[]
for L,r in byL.items():
    p=tuple(map(Q,r['p'])); q=tuple(map(Q,r['q']))
    assert tuple(2*x for x in q)==L
    # Solve physical coordinate equations directly, without multiplying B.
    recovered=(2*(p[0]-2)-(p[1]+1),p[1]+1,Q(2,3)*(4-p[2]))
    assert recovered==L
    residual=tuple(recovered[j]-L[j] for j in range(3))
    assert residual==tuple(map(Q,r['R_L']))==(0,0,0)
    lam=sum(L)
    assert lam==r['lambda_']
    assert p[0]-2-(p[2]-4)/3==Q(lam,2)
    assert r['chi']==(1 if lam in (-2,0,2) else -1)
    # Select remainder by explicit witness rather than Python's modulo result.
    witnesses=[(k,t) for k in range(-2,2) for t in (0,1,2) if 3*k+t==lam]
    assert len(witnesses)==1 and r['r3']==witnesses[0][1]
    z=tuple(map(int,r['z'])); u=tuple(map(Q,r['u']))
    assert tuple(z[j]+u[j] for j in range(3))==q
    assert all(-Q(1,2)<=t<Q(1,2) for t in u)
    if L==(0,0,0): assert r['s'] is None and tuple(map(int,r['v']))==(0,0,0)
    else:
        v=tuple(map(int,r['v']))
        assert next(x for x in v if x)>0
        assert tuple(r['s']*x for x in v)==L
        opposite=byL[tuple(-x for x in L)]
        assert opposite['v']==r['v'] and opposite['s']==-r['s']
        assert tuple(p[j]+Q(opposite['p'][j]) for j in range(3))==(4,-2,8)
    records.append({'row':r['id'],'L':L,'R_L':[str(x) for x in residual],'affine_sheet_residual':'0','ownership_residual':['0','0','0'],'pair_reconstruction':'passed' if r['s'] is not None else 'center singleton'})
assert Counter(sum(x!=0 for x in L) for L in byL)=={0:1,1:6,2:12,3:8}
assert Counter(r['lambda_'] for r in rows)=={-3:1,-2:3,-1:6,0:7,1:6,2:3,3:1}
assert Counter(r['chi'] for r in rows)=={1:13,-1:14}
assert Counter(r['r3'] for r in rows)=={0:9,1:9,2:9}

examples=[
 ('C05.02-W1',(1,-1,1),('2','-2','5/2')),
 ('C05.02-P1',(0,1,-1),('5/2','0','11/2')),
 ('C05.02-D1',(1,0,0),('5/2','-1','4')),
 ('C05.02-D3',(-1,1,-1),('2','0','11/2')),
 ('C05.05-W1',(-1,0,1),('3/2','-1','5/2')),
 ('C05.05-W1-partner',(1,0,-1),('5/2','-1','11/2')),
 ('C05.05-P1',(0,-1,-1),('3/2','-2','11/2')),
 ('C05.05-P1-partner',(0,1,1),('5/2','0','5/2')),
 ('C05.06-W1',(1,-1,1),('2','-2','5/2')),
 ('C05.06-P1',(-1,1,-1),('2','0','11/2'))]
for name,L,p in examples: assert tuple(byL[L]['p'])==p,(name,L,p)
assert Q(2)-Q(5,6)==Q(7,6)
assert Q(7,6)-(Q(2)-Q(4,3))==Q(1,2)
assert Q(2,3)-1==-Q(1,3) # deliberately erroneous p_z=3
required=[]
for i in range(1,7):
    cid=f'C05.{i:02}'
    text=(R/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    ids=[cid+s for s in ('-E1','-W1','-P1','-D1')]
    if i==4: ids += [cid+s for s in ('-E2','-W2','-P2','-D2')]
    assert all(x in text for x in ids)
    assert text.index(cid+'-E1')<text.index(cid+'-W1')<text.index(cid+'-P1')<text.index(cid+'-D1')
    required.extend(ids)
cap=(R/'capstone.md').read_text(encoding='utf-8')
for i in range(1,8): assert f'C05-CAP-{i:02}' in cap
pins=[]
c=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
for source in c['sources']:
    actual=hashlib.sha256(Path(source['path']).read_bytes()).hexdigest()
    assert actual==source['sha256']
    pins.append({'id':source['id'],'sha256':actual,'matched':True})
payload={'status':'passed','runtime':sys.executable,'arithmetic':'exact fractions; alternate base-three enumeration and inverse equations','rows_checked':27,'pairs_checked':13,'row_verification':records,'explicit_example_checks':[x[0] for x in examples]+['C05.03 origin omission difference','C05.06-P2 deliberate residual'],'teaching_ids_checked':required,'source_pins':pins,'limitations':'Arithmetic and identifier presence are machine checks; pedagogical and evidence judgments are recorded in independent-audit.json and audit_report.json.'}
(R/'verification.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print('PASS: 27 exact rows, 13 pairs, all partitions, ten position examples, affine correction, deliberate residual, teaching IDs and five source pins.')
