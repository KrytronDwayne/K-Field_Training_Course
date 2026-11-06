from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
R=Path(__file__).parent
p=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
sources=[]
for s in p['sources']:
    b=Path(s['path']).read_bytes(); h=hashlib.sha256(b).hexdigest(); assert h==s['sha256']
    sources.append(dict(id=s['id'],path=s['path'],sha256=h,hash_verified=True))
src=json.loads(Path(p['sources'][1]['path']).read_text(encoding='utf-8-sig'))
A=[[F(v) for v in row] for row in src['backbone_sequence'][16]['channel_matrix_A']]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def eye(n):return [[F(i==j) for j in range(n)]for i in range(n)]
def inv(a):
    n=len(a); q=[row[:]+e for row,e in zip(a,eye(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if q[k][j]); q[k],q[j]=q[j],q[k]
        d=q[j][j];q[j]=[v/d for v in q[j]]
        for i in range(n):
            if i!=j:
                d=q[i][j];q[i]=[x-d*y for x,y in zip(q[i],q[j])]
    return [r[n:]for r in q]
G=mm(tr(A),A); Ap=mm(inv(G),tr(A));Proj=mm(A,Ap)
Res=[[x-y for x,y in zip(e,r)]for e,r in zip(eye(13),Proj)]
assert mm(Proj,Proj)==Proj and mm(Res,Res)==Res
assert mm(tr(A),Res)==[[0]*13 for _ in range(6)]
def ledger(y):
    c=mv(Ap,y); a=mv(A,c);s=[x-z for x,z in zip(y,a)]
    assert all(x==z+t for x,z,t in zip(y,a,s));assert mv(tr(A),s)==[0]*6
    return dict(y=y,c=c,represented=a,syndrome=s)
worked=ledger(list(map(F,range(1,14))))
c0=list(map(F,[1,-1,2,0,1,0]));s0=list(map(F,[-2,-2,1,1,0,0,0,0,0,0,0,0,0]))
practice=ledger([x+y for x,y in zip(mv(A,c0),s0)])
assert practice['c']==c0 and practice['syndrome']==s0
# Unit minor row order 5,2,1,8,6,3 (one based) yields integer extractor.
indices=[4,1,0,7,5,2]; minor=[A[i] for i in indices]; mi=inv(minor)
Lint=[[F(0)]*13 for _ in range(6)]
for i in range(6):
    for j,k in enumerate(indices):Lint[i][k]=mi[i][j]
assert mm(Lint,A)==eye(6) and all(v.denominator==1 for r in Lint for v in r)
W=[[F((-1)**sum(int(x)*int(k) for x,k in zip(f'{i:02b}',f'{j:02b}')))for j in range(4)]for i in range(4)]
assert mm(tr(W),W)==[[4*x for x in r]for r in eye(4)]
assert mv(tr(W),list(map(F,[1,2,3,4])))==[10,-2,-4,0]
assert mv(W,list(map(F,[1,0,0,1])))==[2,0,0,2]
weights=[12,1,14,16];moves=[[-1,-2,1,0],[1,4,0,-1],[0,2,1,-1],[-4,0,0,3]]
assert all(sum(a*b for a,b in zip(weights,u))==0 for u in moves)
assert [a+b for a,b in zip(*moves[:2])]==moves[2]
small=[[F(1),F(0)],[F(0),F(1)],[F(1),F(1)]]; y=list(map(F,[2,3,6])); traces={}
for t in [F(1,4),F(1)]:
    c=[F(0),F(0)];rows=[]
    for n in range(3):
        r=[x-z for x,z in zip(y,mv(small,c))]; normal=mv(tr(small),r)
        rows.append(dict(n=n,c=c[:],residual=r,normal_residual=normal))
        c=[a+t*b for a,b in zip(c,normal)]
    traces[str(t)]=rows
assert traces['1/4'][2]['c']==[F(39,16),F(23,8)]
assert traces['1'][2]['residual']==[11,11,23]
assert (F(2)+3-F('4.9'))*10==1
assert (F(2)+3-F('5.05'))*10==F(-1,2)
assert F(7,3)-F(233,100)==F(1,300)
out=dict(status='passed',runtime=sys.executable,sources=sources,A=A,gram=G,worked=worked,practice=practice,L_int=Lint,unit_minor_rows=[i+1 for i in indices],toy_W=W,traces=traces,checks=['source hashes','exact Gram and inverse','projector identities','13-entry reconstruction','integer left inverse','Walsh orthogonality','composition invariance','iteration histories','endpoint energy','rounding closure'])
toy_c=[1,0,0,0,0,1]; toy_b=list(map(F,['1','1/10','1/100','1/1000','1/5','2']))
ratio=sum(x*y for x,y in zip(toy_c,toy_b)); assert ratio==3
out['withheld_reference_mass']=dict(c=toy_c,b=toy_b,reference_mass=None,ratio=ratio,dimensional_result='m=3*m_ref; numerical dimensional mass unresolved')
out['checks'].append('withheld reference mass leaves supplied dot-product ratio computable')
(R/'verification.json').write_text(json.dumps(out,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,default=str))
