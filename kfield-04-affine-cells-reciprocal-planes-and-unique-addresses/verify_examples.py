"""Independent exact checks of the small synthetic teaching examples, no packages."""
from pathlib import Path
from fractions import Fraction as F
from math import floor
import json, sys, hashlib
ROOT=Path(__file__).resolve().parent
assert Path(sys.executable).as_posix().lower()=='c:/users/info/.conda/envs/tf_gpu_env/python.exe'
B=((1,1,0),(0,2,0),(0,0,-3)); O=(2,-1,4)
I=((F(1),F(-1,2),0),(0,F(1,2),0),(0,0,F(-1,3)))
def mv(M,v): return tuple(sum(a*b for a,b in zip(row,v)) for row in M)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def tr(M):return tuple(zip(*M))
def mm(A,B):return tuple(tuple(dot(row,col) for col in tr(B)) for row in A)
checks=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    checks.append({'id':name,'result':'passed','actual':str(actual),'expected':str(expected)})
check('inverse-direct',mm(I,B),((1,0,0),(0,1,0),(0,0,1)))
cases=[('C04.01-W1',(F(1,2),F(-1,2),1),(2,-2,1)),('C04.01-P1',(1,0,-1),(3,-1,7)),('A',(F(1,2),F(-1,2),F(3,2)),(2,-2,F(-1,2))),('B',(F(-3,2),F(49,100),F(51,100)),(F(99,100),F(-1,50),F(247,100))),('C',(F(499,1000),0,0),(F(2499,1000),-1,4))]
for name,q,x in cases:
    check(name+' forward',add(O,mv(B,q)),x)
    check(name+' inverse',mv(I,sub(x,O)),q)
    z=tuple(floor(v+F(1,2)) for v in q);u=sub(q,z)
    assert all(F(-1,2)<=v<F(1,2) for v in u)
    check(name+' reconstruction',add(O,mv(B,add(z,u))),x)
    if name=='A':check('A owner/local',(z,u),((1,0,2),(F(-1,2),)*3))
    if name=='B':check('B owner/local',(z,u),((-1,0,1),(F(-1,2),F(49,100),F(-49,100))))
    if name=='C':check('C owner/local',(z,u),((0,0,0),q))
hs=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(2,0,0)]
expected_g=[(1,F(-1,2),0),(0,F(1,2),0),(0,0,F(-1,3)),(1,0,0),(2,-1,0)]
norm2=[F(5,4),F(1,4),F(1,9),F(1),F(5)]
levels=[F(1,2),F(-1,2),F(3,2),0,1]
for h,g,ng,lv in zip(hs,expected_g,norm2,levels):
    check(str(h)+' reciprocal',mv(tr(I),h),g)
    check(str(h)+' pairings',tuple(dot(g,c) for c in tr(B)),h)
    check(str(h)+' norm squared',dot(g,g),ng)
    check(str(h)+' level',dot(g,(0,-1,F(-9,2))),lv)
    # Unit-normal step is g/(g dot g), avoiding radicals while checking d*n.
    step=tuple(v/ng for v in g)
    check(str(h)+' one-level normal step',dot(g,step),1)
    check(str(h)+' spacing squared',dot(step,step),1/ng)
M=mm(tr(B),B)
check('Gram',M,((1,1,0),(1,5,0),(0,0,9)))
pv=mv(B,(1,0,0));pw=mv(B,(1,1,0))
check('C04.05-P2 physical dot',dot(pv,pw),2)
check('C04.05-P2 cosine squared',F(dot(pv,pw)**2,dot(pv,pv)*dot(pw,pw)),F(1,2))
for q,expected in [((1,1,0),8),((1,-1,0),4)]:
    check(str(q)+' direct length squared',dot(mv(B,q),mv(B,q)),expected)
    check(str(q)+' Gram length squared',dot(q,mv(M,q)),expected)
for name,qdisp,r,expected_owner in [('B',(F(-3,2),F(1,2),F(1,2)),(0,F(-1,100),F(1,100)),(-1,0,1)),('C',(F(1,2),0,0),(F(-1,1000),0,0),(0,0,0))]:
    q=add(qdisp,r)
    check(name+' restored owner',tuple(floor(v+F(1,2)) for v in q),expected_owner)
    check(name+' physical correction',add(add(O,mv(B,qdisp)),mv(B,r)),add(O,mv(B,q)))
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
for s in packet['sources']:
    check(s['id']+' source SHA256',hashlib.sha256(Path(s['path']).read_bytes()).hexdigest(),s['sha256'])
s2=json.loads(Path(packet['sources'][1]['path']).read_text(),parse_float=str)
canonical=s2['backbone_sequence'][1]['result'];card=(ROOT/'canonical-card.md').read_text(encoding='utf-8')
for n in canonical['reciprocal_normals_u_v_w']:
    for value in n:assert value in card,value
for value in canonical['reciprocal_spacings_u_v_w_nm']:assert value in card,value
checks.append({'id':'canonical-card-lexemes','result':'passed','method':'All 12 canonical decimal strings occur unchanged in supplied card; pointer read in place.'})
for c in packet['coverage_matrix']:
    content=(ROOT/(c['introduction']+'.md')).read_text(encoding='utf-8')
    for ident in c['all_required_teaching_item_ids']:assert ident in content,ident
checks.append({'id':'required-teaching-ids','result':'passed','method':'Every required item ID appears in its designated lesson.'})
for i in range(1,7):
    text=(ROOT/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    for section in ['Essential question','Goals','Bridge','Claim scope','Diagnostic checks','Worked answer','Pacing','Next dependency']:assert section in text,(i,section)
checks.append({'id':'lesson-contract-structure','result':'passed','method':'Six lessons contain all required structural sections; semantic audit is separate.'})
result={'status':'passed','runtime':sys.executable,'check_count':len(checks),'checks':checks,'scope':'Exact finite classroom inputs; squared magnitudes verify radical spacing answers without floating rounding. No full locked-geometry proof is claimed.'}
(ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','check_count':len(checks),'runtime':sys.executable}))
