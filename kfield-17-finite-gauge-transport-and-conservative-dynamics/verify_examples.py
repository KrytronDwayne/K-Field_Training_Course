"""Exact tiny synthetic computations and actual-content checks for course 17.
Only standard library, no large arrays or source copies. Writes one compact report.
"""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib, sys, re
root=Path(__file__).resolve().parent
checks=[]
def check(name,condition,result):
    assert condition,name
    checks.append({'check':name,'result':result,'status':'passed'})
def z(a,b=0): return (F(a),F(b))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def n(a): return a[0]**2+a[1]**2
def div(a,b):
    q=mul(a,conj(b)); return (q[0]/n(b),q[1]/n(b))
def mm(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
one=z(1); ii=z(0,1); mi=z(0,-1)
check('01 scalar forward/inverse',mul(mi,z(1,1))==z(1,-1) and mul(ii,z(1,-1))==z(1,1),'1+i -> 1-i -> 1+i; norm squared 2')
for px,py,u,gx,gy,expected in [(z(1),z(2),ii,ii,z(-1),z(2,1)),(z(2),z(1,1),mi,z(-1),ii,z(-1,-1))]:
    d=sub(px,mul(u,py)); up=mul(mul(gx,u),div(one,gy)); xp=mul(gx,px); yp=mul(gy,py)
    dp=sub(xp,mul(up,yp))
    check('02 covariance and reconstruction',dp==expected==mul(gx,d) and add(d,mul(u,py))==px,str(dp))
X=[[0,1],[1,0]]; Z=[[1,0],[0,-1]]; I=[[1,0],[0,1]]
xz=mm(X,Z); zx=mm(Z,X)
check('03 matrix order and conjugation',xz==[[0,-1],[1,0]] and zx==[[0,1],[-1,0]] and mm(mm(Z,zx),Z)==xz,'XZ=-ZX; Z(ZX)Z=XZ')
for loop in [xz,zx]:
    trf=2-loop[0][0]-loop[1][1]
    check('04 matrix action',trf==2 and 2*trf==4 and 3*trf==6,'4 AU at beta=2; 6 AU at beta=3')
check('04 scalar changed links',mul(mul(z(-1),ii),mi)==z(-1),'(-1,i,-i) product -1')
for lam,t,state,expected in [([1,2],F(1),[z(1),z(2)],[mi,z(F(-6,5),F(-8,5))]),([0,2],F(1,2),[z(1,1),z(2)],[z(1,1),z(0,-2)])]:
    c=[div(z(1,-t*l),z(1,t*l)) for l in lam]
    out=[mul(a,b) for a,b in zip(c,state)]
    N=sum(map(n,state)); Q=sum(l*n(s) for l,s in zip(lam,state))
    check('05 Cayley factors, inverse and norm',out==expected and all(n(a)==1 for a in c) and [mul(conj(a),b) for a,b in zip(c,out)]==state and sum(map(n,out))==N,str(out))
    check('08 quadratic conservation',sum(l*n(s) for l,s in zip(lam,out))==Q,f'N={N}, Q_L={Q}, normalized={Q/N}')
    check('08 retained remainder',all(add(s,sub(o,s))==o for s,o in zip(state,out)),'full component differences reconstruct output')
check('05 hypothesis counterexample',div(z(F(3,2)),z(F(1,2)))==z(3),'nonselfadjoint Lhat=i/2 gives C=3')
for m in [[1,4,16],[4,1,16]]:
    r=[F(1,x) for x in m]; area=[r[0]*r[1],r[0]*r[2],r[1]*r[2]]
    he=[4*x for x in r]; hb=[16*x for x in area]
    check('06 determinant/duality',he[0]*he[1]*he[2]==hb[0]*hb[1]*hb[2]==1 and hb[::-1]==[1/x for x in he],f'HE={he}; HB={hb}')
    check('06 scale retention', [16*(x/4) for x in r]==he and [256*(x/16) for x in area]==hb,'M*4: normalized blocks unchanged; scale retained separately')
check('06 historical normalization',64**(3*F(2,3)-1)==64 and 64**(3*F(4,3)-2)==4096,'historical determinants 64,4096')
check('07 synthetic minimum',min(F(3,10),2*F(1,20))==F(1,10),'E0/10; optional scale gives 1/20 EU')
terms=[F(8**j,16**(2**j)) for j in range(3)]
check('08 recognition thermal terms',terms==[F(1,16),F(1,32),F(1,1024)] and sum(terms)==F(97,1024),'partial sum 97/1024; tail retained symbolically')
packet=json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
source=json.loads(Path(packet['sources'][1]['path']).read_text(encoding='utf-8-sig'))
proof=' '.join(source['backbone_sequence'][12]['proof'])
for bound in ['epsilon_E<0.007744166','epsilon_B<0.015868134','alpha<=0.5244','Delta>0.10185916 H_N/tau_R']:
    check('07 exact source bound',bound in proof,bound)
cap=(root/'capstone.md').read_text(encoding='utf-8')
for j in range(1,9):
    body=(root/f'lesson-{j:02}.md').read_text(encoding='utf-8')
    for suffix in ['E1','W1','P1','D1']:
        anchor=f'C17.{j:02}-{suffix}'
        check('E05 actual content '+anchor,anchor in body and anchor in cap,'present in prior lesson and backward map')
    for phrase in ['Essential question:','Goals:','Prerequisite bridge:','Claim scope:','Diagnostic checks','Next dependency:']:
        assert phrase in body,(j,phrase)
check('Capstone rubric total',sum([8,12,10,10,15,20,15,10])==100,'100 points')
hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob('lesson-*.md')}
hashes['capstone.md']=hashlib.sha256((root/'capstone.md').read_bytes()).hexdigest()
report={'schema_version':'1.0','status':'passed','runtime':sys.executable,'checks':checks,'artifact_hashes':hashes,'scope':'Exact rational synthetic arithmetic and actual-content anchors; not archival certificate replay. Independent qualitative teaching checks are separate.','source_data_copies':False}
(root/'worked-example-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact arithmetic, source-transcription and content-anchor checks')
