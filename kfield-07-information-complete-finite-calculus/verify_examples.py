"""Independent exact arithmetic replay of the authored finite teaching examples."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,sys,hashlib
R=Path(__file__).resolve().parent
checks=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    checks.append({'id':name,'result':'passed','actual':str(actual),'expected':str(expected)})
def vec(v): return tuple(map(F,v))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,b): return tuple(x*y for x,y in zip(a,b))
def E(a): return tuple(m for i in range(0,len(a),2) for m in [(a[i]+a[i+1])/2]*2)
def Q(a): return sub(a,E(a))
def rhs(f,g,op=E):
    ef,eg=op(f),op(g)
    qf,qg=sub(f,ef),sub(g,eg)
    return sub(add(add(mul(ef,qg),mul(qf,eg)),mul(qf,qg)),op(mul(qf,qg)))
def est(a): x,y,z=a; return (x,x,z+y-x)
def decode(a,ds):
    out=[a]
    for d in ds: out.append(out[-1]+d)
    return tuple(out)
for name,v,expected in [('C07.01-W1',(2,5,4,9),(3,-1,5)),('C07.01-P1',(3,7,6,10),(4,-1,4))]:
    delta=tuple(v[i+1]-v[i] for i in range(3))
    check(name+'-differences',delta,expected)
    check(name+'-inverse',decode(v[0],delta),v)
check('C07.01-D1-rate',F(9-5,3-1),F(2))
check('C07.01-D2',decode(-2,(3,0,-1)),(-2,1,1,0))
for name,fs,ft,gs,gt,terms in [('C07.02-W1',2,5,4,6,(4,12,6)),('C07.02-P1',3,1,2,5,(9,-4,-6)),('C07.02-D1',1,1,2,4,(2,0,0)),('C07.02-D2',-1,2,3,2,(1,9,-3))]:
    df,dg=ft-fs,gt-gs
    check(name+'-terms',(fs*dg,gs*df,df*dg),terms)
    check(name+'-direct',sum(terms),ft*gt-fs*gs)
    check(name+'-endpoint',fs*dg+df*gt,ft*gt-fs*gs)
for name,raw,means,details in [('C07.03-W1',(2,5,4,9),(F(7,2),F(13,2)),(F(3,2),F(5,2))),('C07.03-P1',(3,7,6,10),(5,8),(2,2)),('C07.03-D2',(7,3),(5,),(-2,))]:
    a=vec(raw);m=tuple((a[i]+a[i+1])/2 for i in range(0,len(a),2));d=tuple((a[i+1]-a[i])/2 for i in range(0,len(a),2))
    check(name+'-means',m,means);check(name+'-detail',d,details)
    check(name+'-decode',tuple(t for mi,di in zip(m,d) for t in (mi-di,mi+di)),a)
for name,f,g,expected in [('C07.04-W1',(2,4,1,5),(1,3,2,4),(-5,5,-9,9)),('C07.04-P1',(0,2,2,4),(1,1,0,2),(-1,1,-4,4))]:
    f,g=vec(f),vec(g)
    check(name+'-direct',Q(mul(f,g)),vec(expected))
    check(name+'-RHS',rhs(f,g),vec(expected))
check('C07.04-P1-factor',E(mul(vec((2,2,-1,-1)),vec((0,2,2,4)))),vec((2,2,-3,-3)))
f=vec((0,1,0));b=vec((1,1,0))
check('C07.04-D1-factor-left',est(mul(b,f)),vec((0,0,1)))
check('C07.04-D1-factor-right',mul(b,est(f)),vec((0,0,0)))
check('C07.04-D1-direct',sub(mul(f,f),est(mul(f,f))),vec((0,1,-1)))
check('C07.04-D1-RHS',rhs(f,f,est),vec((0,1,-3)))
check('C07-CAP-04-mismatch',sub(rhs(f,f,est),sub(mul(f,f),est(mul(f,f)))),vec((0,0,-2)))
# A finite grid is a stress test, not a substitute for the generic proof in lesson 04.
grid=list(product((-1,0,1),repeat=4))
for raw in grid:
    f=vec(raw)
    assert E(E(f))==E(f)
    for rawg in grid:
        g=vec(rawg)
        assert rhs(f,g)==Q(mul(f,g))
checks.append({'id':'block-identity-grid','result':'passed','cases':len(grid)**2,'scope':'exact rational stress test; generic proof is in lesson-04 E1/E2'})
for name,x,m0,expected0,expected1 in [('C07.05-W1',(2,5,4,9),(1,1,1,1),(1,4,3,8),(F(-3,2),F(3,2),F(-5,2),F(5,2))),('C07.05-P1',(3,7,6,10),(2,2,2,2),(1,5,4,8),(-2,2,-2,2)),('C07.05-D2',(4,4),(1,2),(3,2),(F(1,2),F(-1,2)))]:
    x,m0=vec(x),vec(m0);r0=sub(x,m0);m1=E(r0);r1=sub(r0,m1)
    check(name+'-r0',r0,vec(expected0));check(name+'-r1',r1,vec(expected1));check(name+'-inverse',add(add(m0,m1),r1),x)
def K(a): return (a[0]+a[1],2*a[0]+2*a[1])
for name,j,t,expected in [('C07.06-W1',(6,12),4,(2,4)),('C07.06-D1',(8,16),3,(5,3))]:
    psi=(j[0]-t,t);check(name+'-input',psi,expected);check(name+'-output',K(psi),j)
for a in range(-4,5):
    for t in (F(-3,2),F(0),F(2,3),F(4)):
        assert K((a-t,t))==(a,2*a)
check('C07.06-kernel',K((-1,1)),(0,0))
for name,j in [('C07.06-P1',(6,13)),('C07.06-D2',(8,17))]:
    c=j[1]-2*j[0]; fit=(j[0],2*j[0]);rho=(0,c)
    check(name+'-compatibility',c,1);check(name+'-output-recovery',add(fit,rho),j)
check('C07.06-L-inverse',(3,F(8,2)),(3,4))
for name,x,m0 in [('C07.07-W1',(2,5,4,9),(1,1,1,1)),('C07.07-P1',(3,7,6,10),(2,2,2,2))]:
    x,m0=vec(x),vec(m0);r0=sub(x,m0);m=tuple(E(r0)[i] for i in (0,2));d=tuple((r0[i+1]-r0[i])/2 for i in (0,2));anchor=m[0];delta=m[1]-m[0]
    decodedm=(anchor,anchor+delta);decodedr=tuple(t for a,b in zip(decodedm,d) for t in (a-b,a+b));decodedx=add(m0,decodedr)
    check(name+'-delta',delta,F(3));check(name+'-full-inverse',decodedx,x);check(name+'-error',sub(decodedx,x),vec((0,0,0,0)))
check('C07.07-D3',add(vec((3,5,5,1)),vec((2,2,2,2))),vec((5,7,7,3)))
packet=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
texts={f'lesson-{i:02}':(R/f'lesson-{i:02}.md').read_text(encoding='utf-8') for i in range(1,8)}
for i in range(1,8):
    text=texts[f'lesson-{i:02}'];cid=f'C07.{i:02}'
    for suffix in ('E1','W1','P1','D1','D2','D3'): assert cid+'-'+suffix in text,(cid,suffix)
    for label in ('Essential question:','Goals:','Prerequisite bridge:','Claim scope:','Next dependency:'): assert label in text,(cid,label)
for cid in ['EG-A1','EG-A2','EG-A3','EG-A4','EG-A5','EG-A6']:
    assert cid in texts['lesson-01'] and cid in texts['lesson-07'] and cid in (R/'capstone.md').read_text()
for row in packet['coverage_matrix']:
    for item in row.get('all_required_teaching_item_ids',[]): assert item in '\n'.join(texts.values()),item
checks.append({'id':'teaching-contract-and-required-IDs','result':'passed','scope':'Presence only; independent teaching audit evaluates substance.'})
result={'status':'passed','runtime':sys.executable,'arithmetic':'fractions.Fraction exact arithmetic','checks':checks,'check_count':len(checks),'source_data_copied':False}
(R/'worked-example-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','runtime':sys.executable,'checks':len(checks),'grid_cases':len(grid)**2}))
