"""Independent auditor's exact finite-example checks; standard library only."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, math, re, sys

root = Path(__file__).resolve().parent
contract = json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
checks = []
def check(name, value):
    assert value, name
    checks.append(name)
def vec(*x): return tuple(F(a) for a in x)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(a,b): return tuple(dot(row,b) for row in a)
B=(vec(1,1,0),vec(0,2,0),vec(0,0,-3))
Bi=(vec(1,'-1/2',0),vec(0,'1/2',0),vec(0,0,'-1/3'))
O=vec(2,-1,4)
cols=tuple(zip(*B))
M=tuple(tuple(dot(a,b) for b in cols) for a in cols)
check('Gram matrix',M==((1,1,0),(1,5,0),(0,0,9)))
examples=[(vec('1/2','-1/2',1),vec(2,-2,1)),(vec(1,0,-1),vec(3,-1,7)),(vec('1/2','-1/2','3/2'),vec(2,-2,'-1/2')),(vec('-3/2','49/100','51/100'),vec('99/100','-1/50','247/100')),(vec('499/1000',0,0),vec('2499/1000',-1,4))]
for i,(q,x) in enumerate(examples):
    d=mv(B,q)
    check(f'point {i+1} forward',tuple(o+t for o,t in zip(O,d))==x)
    check(f'point {i+1} inverse',mv(Bi,tuple(t-o for t,o in zip(x,O)))==q)
    z=tuple(math.floor(t+F(1,2)) for t in q)
    u=tuple(t-k for t,k in zip(q,z))
    check(f'point {i+1} local range',all(-F(1,2)<=t<F(1,2) for t in u))
    check(f'point {i+1} reconstruction',tuple(k+t for k,t in zip(z,u))==q)
    for h in (vec(1,0,0),vec(0,1,0),vec(0,0,1),vec(1,1,0),vec(2,0,0),vec(-1,0,0)):
        g=mv(tuple(zip(*Bi)),h)
        check(f'point {i+1} pairing {h}',tuple(dot(g,a) for a in cols)==h)
        check(f'point {i+1} level {h}',dot(g,d)==dot(h,q))
        # g/|g|^2 is the exact normal displacement between successive levels.
        step=tuple(t/dot(g,g) for t in g)
        check(f'point {i+1} spacing displacement {h}',dot(g,step)==1)
for q,expected in [(vec(1,1,0),8),(vec(1,-1,0),4)]:
    check(f'Gram length {q}',dot(q,mv(M,q))==dot(mv(B,q),mv(B,q))==expected)
check('rounding residual',vec('1/2',0,0)[0]+F(-1,1000)==F(499,1000))
check('near boundary owners',[math.floor(q+F(1,2)) for q in [F(499,1000),F(1,2),F(-1,2),F(-3,2)]]==[0,1,0,-1])
for source in contract['sources']:
    check('source hash '+source['id'],hashlib.sha256(Path(source['path']).read_bytes()).hexdigest()==source['sha256'])
s2=json.loads(Path(contract['sources'][1]['path']).read_text(encoding='utf-8-sig'),parse_float=str)
s3=json.loads(Path(contract['sources'][2]['path']).read_text(encoding='utf-8-sig'))
card=(root/'canonical-card.md').read_text(encoding='utf-8')
for field in ['reciprocal_normals_u_v_w','reciprocal_spacings_u_v_w_nm']:
    values=s2['backbone_sequence'][1]['result'][field]
    for row in values:
        for lexeme in (row if isinstance(row,list) else [row]):
            check('canonical lexeme '+lexeme,lexeme in card)
check('superseded source disposition',s3['findings'][4]['classification']=='SUPERSEDED_NUMERIC_WITNESS')
for row in contract['coverage_matrix']:
    lesson=(root/(row['introduction']+'.md')).read_text(encoding='utf-8')
    for item in row['all_required_teaching_item_ids']:
        check('required item '+item,item in lesson)
    diagnostic=lesson.split('## Diagnostic checks')[1].split('**Worked answers:**')[0]
    check('diagnostic count '+row['introduction'],3<=len(re.findall(r'^\d+\.',diagnostic,re.M))<=5)
report={'role':'independent finite-example and instructional auditor','python_executable':sys.executable,'automated_checks_passed':len(checks),'checks':checks,'status':'passed'}
(root/'independent-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','check_count':len(checks),'python_executable':sys.executable}))
