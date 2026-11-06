"""Exact, standard-library finite replay. Writes compact authored verification only."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib,json,sys
R=Path(__file__).resolve().parent
assert Path(sys.executable).as_posix().lower()=='c:/users/info/.conda/envs/tf_gpu_env/python.exe',sys.executable
class Q:
    # Exact a+b sqrt(2); only addition and multiplication are required.
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,x):
        x=x if isinstance(x,Q) else Q(x)
        return Q(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,x): return self+-x
    def __mul__(self,x):
        x=x if isinstance(x,Q) else Q(x)
        return Q(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __eq__(self,x):
        x=x if isinstance(x,Q) else Q(x)
        return self.a==x.a and self.b==x.b
    def __repr__(self): return f'{self.a}+({self.b})sqrt(2)'
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def scale(a,v): return [a*x for x in v]
def add(x,y): return [a+b for a,b in zip(x,y)]
def matvec(A,x): return [dot(row,x) for row in A]
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
rt=Q(0,1); h=F(1,2)
u=[[Q(h),Q(0,h),Q(h)],[Q(0,h),Q(),Q(0,-h)],[Q(h),Q(0,-h),Q(h)]]
lam=[rt,Q(),-rt]
A=[[0,1,0],[1,0,1],[0,1,0]]
for i in range(3):
    check(f'path eigenpair {i}',matvec(A,u[i])==scale(lam[i],u[i]))
    for j in range(3): check(f'path dot {i},{j}',dot(u[i],u[j])==int(i==j))
for x,y in [([1,2,3],[2,4,2]),([2,-1,0],[-1,2,-1]),([1,0,0],[0,1,0]),([-1,3,2],[3,1,3]),([2,0,-2],[0,0,0]),([1,1,1],[1,2,1])]:
    check(f'path action {x}',matvec(A,x)==y)
nodes=list(product(range(-1,2),repeat=3)); inds={n:i for i,n in enumerate(nodes)}
adj=[[j for j,m in enumerate(nodes) if sum(abs(a-b) for a,b in zip(n,m))==1] for n in nodes]
def act(v): return [sum(v[j] for j in ns) for ns in adj]
labels=list(product(range(3),repeat=3)); modes=[]
for t in labels:
    v=[u[t[0]][i+1]*u[t[1]][j+1]*u[t[2]][k+1] for i,j,k in nodes]
    ev=sum(lam[s] for s in t)
    check(f'product eigenpair {t}',act(v)==scale(ev,v)); modes.append(v)
check('all 729 product inner products',all(dot(v,w)==int(i==j) for i,v in enumerate(modes) for j,w in enumerate(modes)))
counts=Counter(sum((1,0,-1)[s] for s in t) for t in labels)
check('seven multiplicities',[counts[m] for m in range(-3,4)]==[1,3,6,7,6,3,1])
check('two-factor counts',[Counter(sum(t) for t in product((-1,0,1),repeat=2))[m] for m in range(-2,3)]==[1,2,3,2,1])
degrees=Counter(map(len,adj)); check('degree populations',degrees=={3:8,4:12,5:6,6:1})
check('open edge count',sum(map(len,adj))//2==54)
check('node sheets',Counter(map(sum,nodes))==counts)
check('node chi',sum(sum(n)%2==0 for n in nodes)==13)
reflection=[inds[tuple(-x for x in n)] for n in nodes]
check('fixed center and pairs',sum(i==j for i,j in enumerate(reflection))==1 and len(nodes)==27)
check('reflection commutes',all({reflection[j] for j in adj[i]}==set(adj[reflection[i]]) for i in range(27)))
sample_records=[]
for f in [[1,2,3],[2,0,0],[4,1,0]]:
    cs=[dot(v,f) for v in u]
    rebuilt=[sum(cs[j]*u[j][i] for j in range(3)) for i in range(3)]
    check(f'reconstruction {f}',rebuilt==f)
    even=[F(a+b,2) for a,b in zip(f,f[::-1])]; odd=[F(a-b,2) for a,b in zip(f,f[::-1])]
    mu=F(sum(f),3); detail=[F(x)-mu for x in f]
    residual=[Q(f[i])-cs[1]*u[1][i] for i in range(3)]
    check(f'parity,mean,residual reconstruction {f}',add(even,odd)==f and [mu+x for x in detail]==f and add(scale(cs[1],u[1]),residual)==f)
    sample_records.append(dict(input=f,coefficients=list(map(str,cs)),residual_zero_mode_only=list(map(str,residual)),mean=str(mu),centered=list(map(str,detail)),even=list(map(str,even)),odd=list(map(str,odd))))
check('specified coefficients first',sample_records[0]['coefficients']==['2+(1)sqrt(2)','0+(-1)sqrt(2)','2+(-1)sqrt(2)'])
check('center product',modes[labels.index((0,0,2))][inds[(0,0,0)]]==Q(0,F(-1,4)) and act(modes[labels.index((0,0,2))])[inds[(0,0,0)]]==Q(F(-1,2)))
check('corner product',modes[labels.index((2,2,1))][0]==Q(0,F(1,8)) and act(modes[labels.index((2,2,1))])[0]==Q(F(-1,2)))
AX=[[1,0],[0,2]]; BY=[[2,0],[0,1]]; T=[[0,1],[1,0]]
for x in [[1,0],[0,1],[3,4],[1,-2],[2,5]]:
    check(f'swap intertwiner and inverse {x}',matvec(BY,matvec(T,x))==matvec(T,matvec(AX,x)) and matvec(T,matvec(T,x))==x)
check('identity fails',matvec(BY,[1,0])!=matvec(AX,[1,0]))
packet=json.loads((R/'input-contract.json').read_text(encoding='utf-8'))
sources=[]
for s in packet['sources']:
    actual=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()
    check('source hash '+s['id'],actual==s['sha256']);sources.append(dict(id=s['id'],path=s['path'],sha256=actual))
source=json.loads(Path(packet['sources'][1]['path']).read_text(encoding='utf-8'))
check('mature spectrum agrees',[x['multiplicity'] for x in source['backbone_sequence'][7]['emily_spectrum']]==[counts[m] for m in range(-3,4)])
decoder=source['backbone_sequence'][16]['channel_matrix_A']
check('M17 matrix shape',len(decoder)==13 and all(len(row)==6 for row in decoder))
work=[list(map(F,row)) for row in decoder]; rank=0
for c in range(6):
    pivot=next((i for i in range(rank,13) if work[i][c]),None)
    if pivot is None: continue
    work[rank],work[pivot]=work[pivot],work[rank]
    d=work[rank][c];work[rank]=[x/d for x in work[rank]]
    for i in range(13):
        if i!=rank:
            factor=work[i][c];work[i]=[x-factor*y for x,y in zip(work[i],work[rank])]
    rank+=1
check('M17 exact rank and syndrome count',rank==6 and 13-rank==7)
for i,row in enumerate(packet['course_map'],1):
    txt=(R/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    for suffix in ['E1','W1','P1','D1']: check(f'actual anchor C12.{i:02}-{suffix}',f'C12.{i:02}-{suffix}' in txt)
    check(f'lesson contract headings {i}',all(x in txt for x in ['Essential question','Goals','Prerequisite bridge','Claim scope','Diagnostic checks','Worked answers','Next dependency']))
for old in ['C12-EIG-EX1','C12-EIG-P1','C12-EIG-D1']: check('legacy '+old,old in (R/'lesson-03.md').read_text(encoding='utf-8'))
result=dict(status='passed',arithmetic='Exact fractions a+b sqrt(2); no tolerance or rounded radicals',python_executable=sys.executable,checks=checks,check_count=len(checks),product_modes=27,product_dot_comparisons=729,multiplicities={str(m):counts[m] for m in range(-3,4)},degree_populations=dict(degrees),parity_dimensions=dict(even=14,odd=13,retained_mean=1,centered_even=13),M17=dict(shape=[13,6],rank=rank,syndrome_dimension=7),examples=sample_records,sources=sources,scope='Finite course claims; no global formula-DAG certification or fresh formal compiler replay.')
(R/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',checks=len(checks),python_executable=sys.executable)))
