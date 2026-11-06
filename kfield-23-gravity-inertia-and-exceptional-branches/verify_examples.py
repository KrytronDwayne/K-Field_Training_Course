"""Independent small finite checks; no packages or source snapshots."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys,json,hashlib,re
R=Path(__file__).resolve().parent
checks=[]
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 checks.append({'check':name,'actual':str(actual),'expected':str(expected),'status':'passed'})
def mul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
A=[[0,1,-1],[-1,0,1],[9,8,-11]]
detA=A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
check('forward determinant ordered F M G',detA,6)
for y,expected in [((0,2,3),(-1,3,-17)),((1,0,2),(-2,1,-13))]:
 f,m,g=(sum(v*z for v,z in zip(row,y)) for row in A)
 check('scalar forward '+str(y),(f,m,g),expected)
 inv=(F(g-8*f+3*m,6),F(g-2*f+9*m,6),F(g-8*f+9*m,6))
 check('scalar inverse '+str(y),inv,y)
check('scalar shift column sums',[sum(row) for row in A],[0,0,6])
q=(F(1,2),F(1,3),F(0)); rho=(F(1,10),F(-1,5),F(0))
qo=tuple(x+y for x,y in zip(q,rho))
check('reciprocal metric length',dot(q,q),F(13,36))
check('reciprocal roundtrip',tuple(x*y for x,y in zip((2,3,4),q)),(1,1,0))
check('reciprocal residual reconstructed',qo,(F(3,5),F(2,15),F(0)))
check('observed reciprocal metric',dot(qo,qo),F(17,45))
check('reciprocal axis squared length',F(1,4)**2,F(1,16))
check('Bragg worked spacing',F(2*2,1)/(2*F(1,2)),4)
check('Bragg practice spacing',F(1*3,1)/(2*F(1,2)),3)
n=(F(3,5),F(4,5),0); v=(5,0,0); a=(0,5,0)
check('normal squared length',dot(n,n),1)
check('practice projections',(dot(v,n),dot(a,n)),(3,4))
check('velocity complement',tuple(x-3*y for x,y in zip(v,n)),(F(16,5),F(-12,5),0))
check('acceleration complement',tuple(x-4*y for x,y in zip(a,n)),(F(-12,5),F(9,5),0))
check('conditional force',2*dot(a,n),8)
for dim,periodic,expected in [(3,False,(27,54,28)),(3,True,(27,81,55)),(2,False,(9,12,4)),(2,True,(9,18,10))]:
 vertices=list(product(range(3),repeat=dim)); edges=set()
 for u in vertices:
  for axis in range(dim):
   if u[axis]<2 or periodic:
    v=list(u);v[axis]=(v[axis]+1)%3
    edges.add(tuple(sorted((u,tuple(v)))))
 check(f'enumerated grid dim={dim} periodic={periodic}',(len(vertices),len(edges),len(edges)-len(vertices)+1),expected)
check('six ternary coordinates',len(list(product(range(3),repeat=6))),729)
rr=[[1,0],[0,-1]]; ss=[[-1,0],[0,1]]; sp=[[-1,0],[0,-1]]; tt=[[0,1],[1,0]]; identity=[[1,0],[0,1]]
check('intertwiner',mul(tt,rr),mul(ss,tt))
check('invertible exchange',mul(tt,tt),identity)
check('worked identity defect',sub(rr,ss),[[2,0],[0,-2]])
check('practice identity defect',sub(rr,sp),[[2,0],[0,0]])
ma=[[0,1],[0,0]];mb=[[0,0],[1,0]]
check('bracket example',sub(mul(ma,mb),mul(mb,ma)),rr)
check('matrix multiplication bridge',mul([[1,2],[0,1]],[[3,0],[4,1]]),[[11,2],[4,1]])
for w,z,e1,e2 in [(-1,-2,(-2,0),(2,-4)),(2,5,(4,1),(8,-3))]:
 check('H1 signed case '+str(w),(2*w,z-2*w),e1)
 check('H2 signed case '+str(w),(2*w*w,z-2*w*w),e2)
for i in range(1,8):
 text=(R/f'lesson-{i:02}.md').read_text(encoding='utf-8')
 for suffix in ['E1','W1','P1','D1']: check(f'actual anchor C23.{i:02}-{suffix}',f'C23.{i:02}-{suffix}' in text,True)
 for link in re.findall(r'\]\(([^)]+\.md)\)',text): check('lesson link '+link,(R/link).is_file(),True)
payload={'status':'passed','runtime':sys.executable,'method':'Independent standard-library exact fractions, matrix products and explicit graph-edge enumeration. No physical data used.','checks':checks}
(R/'verification.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks),'runtime':sys.executable}))
