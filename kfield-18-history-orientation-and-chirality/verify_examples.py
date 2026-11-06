"""Independent standard-library recomputation of finite course examples.

Reads original sources to hash/resolve pointers; saves no source snapshots.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as F
from itertools import product
P=pathlib.Path(__file__).resolve().parent
C=json.loads((P/'input-contract.json').read_text(encoding='utf-8-sig'))
checks=[]
def check(name,actual,expected):
 assert actual==expected, (name,actual,expected)
 checks.append({'id':name,'status':'passed','result':str(actual)})
def diag(*v): return [[x if i==j else 0 for j in range(len(v))] for i,x in enumerate(v)]
def mat(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,v): return [sum(x*y for x,y in zip(row,v)) for row in a]
def adj(a): return [[complex(x).conjugate() for x in row] for row in zip(*a)]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def norm(v): return sum(abs(x)**2 for x in v)
def plus(a,b): return [x+y for x,y in zip(a,b)]
check('runtime',str(pathlib.Path(sys.executable)).lower(),r'C:\Users\info\.conda\envs\tf_gpu_env\python.exe'.lower())
words=[''.join(w) for n in range(3) for w in product('ab',repeat=n)]
check('C18.01-W1',words,['','a','b','aa','ab','ba','bb'])
check('C18.01-P1',['b'+w for w in ('','a','b')],['b','ba','bb'])
check('C18.01-diagnostic-2',len(list(product('ab',repeat=3))),8)
S=[[0,0,0],[1,0,0],[0,1,0]]; Sd=adj(S); I=diag(1,1,1)
check('C18.02-W1-input',mat(Sd,S),diag(1,1,0))
check('C18.02-W1-output',mat(S,Sd),diag(0,1,1))
check('C18.S01-W1-terminal',sub(I,mat(Sd,S)),diag(0,0,1))
check('C18.S01-W1-root',sub(I,mat(S,Sd)),diag(1,0,0))
for name,v,out,term in [('C18.02-P1',[2,3,4],[0,2,3],[0,0,4]),('C18.S01-P1/CAP-02',[1,-2,5],[0,1,-2],[0,0,5])]:
 check(name+'-shift',mv(S,v),out)
 check(name+'-reconstruct',plus(mv(Sd,out),term),v)
 check(name+'-norm',norm(out)+norm(term),norm(v))
T=[[0,0],[1,0],[0,1]]; Td=adj(T)
check('rectangular-input',mat(Td,T),diag(1,1))
check('rectangular-output',mat(T,Td),diag(0,1,1))
for v in ([5,2,3],[-2,0,6]):
 projected=mv(mat(T,Td),v); residual=mv(sub(I,mat(T,Td)),v)
 check('C18.03-reconstruction-'+str(v),plus(projected,residual),list(v))
 check('C18.03-norm-'+str(v),norm(projected)+norm(residual),norm(v))
check('C18.03-counterexample',mv(S,[0,0,1]),[0,0,0])
power=I; qs=[]
for n in range(4):
 q=mat(mat(power,diag(1,0,0)),adj(power)); qs.append(q)
 check('q-'+str(n),q,diag(*[int(i==n) for i in range(3)]))
 check('q-idempotent-'+str(n),mat(q,q),q)
 check('q-adjoint-'+str(n),adj(q),q)
 power=mat(S,power)
for n in range(4):
 for m in range(n): check('q-orthogonal-'+str(n)+str(m),mat(qs[n],qs[m]),diag(0,0,0))
for v in ([1,2,3],[-1,4,0],[2,-1,7]):
 check('C18.04-reconstruction-'+str(v),[sum(mv(q,v)[i] for q in qs) for i in range(3)],list(v))
check('C18.05-W1',1*2*(-3),-6)
check('C18.05-P1', [2*1*(-4),4*2*(-8),4*2*8],[-8,-64,64])
check('C18.05-scale-three',3*6*(-9),-162)
G=diag(1,-1); X=[[0,1],[1,0]]
check('C18.06-anticommutator',[[x+y for x,y in zip(r,s)] for r,s in zip(mat(G,X),mat(X,G))],diag(0,0))
Pi=diag(1,0,0,1); I4=diag(1,1,1,1)
check('Pi-idempotence',mat(Pi,Pi),Pi)
for v in ([1,2,3,4],[2,-1,0,3],[0,5,-2,0]):
 a=mv(Pi,v); b=mv(sub(I4,Pi),v)
 check('C18.06-reconstruction-'+str(v),plus(a,b),list(v))
 check('C18.06-norm-'+str(v),norm(a)+norm(b),norm(v))
for m in (1,2,3):
 count=sum(2*l+1 for l in range(m+1))
 check('angular-'+str(m),count,(m+1)**2)
 check('spin-'+str(m),2*count,2*(m+1)**2)
check('C2-values',[l*(l+1) for l in range(4)],[0,2,6,12])
check('spin-split-ell2',[2*F(5,2)+1,2*F(3,2)+1],[6,4])
Y=[[0,-1j],[1j,0]]
check('C18.S03-W1-commutator',sub(mat(X,Y),mat(Y,X)),diag(2j,-2j))
A=diag(1,-1); B=[[0,1+1j],[1-1j,0]]
check('C18.S03-P1-commutator',sub(mat(A,B),mat(B,A)),[[0,2+2j],[-2+2j,0]])
check('real-noncommuting',sub(mat(G,X),mat(X,G)),[[0,2],[-2,0]])
check('pointwise-commutator',sub(mat(diag(1,2),diag(3,4)),mat(diag(3,4),diag(1,2))),diag(0,0))
# Exact cubic-phase arithmetic: pair (a,b) represents a+b*omega, omega^2=-1-omega.
def cm(u,v):
 a,b=u; c,d=v
 return (a*c-b*d,a*d+b*c-b*d)
one=(F(1),F(0)); om=(F(0),F(1)); om2=cm(om,om)
check('omega-cube',cm(om2,om),one)
s=[F(2),F(1),F(1,2)]; inv=[1/x for x in s]
check('CP-S-square',[x*x for x in s],[F(4),F(1),F(1,4)])
d=[one,om,om2]
yd=[cm(cm(x,(y,0)),x) for x,y in zip(d,inv)]
yu=[(x,F(0)) for x in s]
yp=[cm(x,y) for x,y in zip(yu,yd)]
check('CP-product',yp,[one,om2,om])
check('CP-determinant',cm(cm(yp[0],yp[1]),yp[2]),one)
check('CP-diagonal-commuting',[cm(x,y) for x,y in zip(yd,yu)],yp)
source_records=[]
pointers={'S02':['/backbone_sequence/13','/backbone_sequence/2','/backbone_sequence/10','/branch_proofs/5','/proof_nodes/4','/proof_nodes/18','/proof_nodes/25','/branch_proofs/10','/proof_nodes/9','/proof_nodes/76'],'S03':['/findings/8']}
for src in C['sources']:
 data=pathlib.Path(src['path']).read_bytes(); digest=hashlib.sha256(data).hexdigest()
 check('source-hash-'+src['id'],digest,src['sha256'])
 obj=json.loads(data.decode('utf-8-sig'))
 for pointer in pointers.get(src['id'],[]):
  node=obj
  for part in pointer.strip('/').split('/'): node=node[int(part)] if isinstance(node,list) else node[part]
  assert node
  checks.append({'id':src['id']+pointer,'status':'passed','result':'Exact JSON pointer resolves; body read separately for source audit'})
 source_records.append({**src,'actual_sha256':digest,'hash_verified':True,'used_pointers':pointers.get(src['id'],[])})
for row in C['course_map']:
 txt=(P/(row['id']+'.md')).read_text(encoding='utf-8')
 for concept in row['concept_ids']:
  for suffix in ('E1','W1','P1','D1'): check('teaching-anchor-'+concept+'-'+suffix,concept+'-'+suffix in txt,True)
 check('lesson-diagnostic-count-'+row['id'],sum(1 for line in txt.split('## Diagnostic checks')[1].split('**Worked answers:**')[0].splitlines() if line[:2] in ('1.','2.','3.','4.','5.')),4)
cap=(P/'capstone.md').read_text(encoding='utf-8')
for row in C['capstone_specification']['backward_map']:
 txt=(P/(row['introduction']+'.md')).read_text(encoding='utf-8')
 check('capstone-step-'+row['step_id'],row['step_id'] in cap,True)
 for key in ('explanation_id','worked_example_id','prior_practice_id','diagnostic_id'): check(row['step_id']+'-'+key,row[key] in txt,True)
report={'status':'passed','runtime':sys.executable,'method':'Independent matrix/vector operations, exact Fraction cubic-phase arithmetic, source hashes/pointers and explicit teaching-anchor checks; no external packages','check_count':len(checks),'checks':checks,'sources':source_records,'scope':'Finite arithmetic and identifier validation, supplemented by independent human-style agent teaching/source audit; not a replay of source missing bodies'}
(P/'verification.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS:',len(checks),'checks; all five source hashes match.')
