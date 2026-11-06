"""Small exact checks; no source snapshots, external packages or large arrays."""
from fractions import Fraction as F
import sys
from manage import *
checks=[]
def check(name,condition,detail):
    assert condition,name
    checks.append(dict(id=name,status='passed',method=detail))
# Exact rational complex arithmetic, stored as (real,imaginary).
def z(a=0,b=0): return (F(a),F(b))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def norm(a): return mul(conj(a),a)[0]
def scale(a,s): return (a[0]*s,a[1]*s)
def dagger(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def mm(A,B):
    return [[sumz([mul(A[i][k],B[k][j]) for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]
def sumz(xs):
    r=z()
    for x in xs:r=add(r,x)
    return r
def mv(A,v):return [sumz([mul(a,b) for a,b in zip(row,v)]) for row in A]
def diag(xs):return [[x if i==j else z() for j in range(len(xs))] for i,x in enumerate(xs)]
def nvec(v):return sum(map(norm,v))
I=diag([z(1),z(1)]); imaginary=z(0,1)
check('L1-W1',mul(imaginary,z(1,1))==z(-1,1) and norm(z(1,1))==norm(z(-1,1))==2,'Exact Fraction pair multiplication and squared norm')
check('L1-P1',mul(imaginary,z(2,-1))==z(1,2) and mul(z(0,-1),z(1,2))==z(2,-1) and norm(z(2,-1))==norm(z(1,2))==5,'Independent forward/inverse and squared modulus')
check('L1-diagnostics',norm(z(-3,2))==13 and mul(imaginary,z(1,-2))==z(2,1) and mul(z(1,1),z(1,1))==z(0,2),'Direct arithmetic, not text comparisons')
U=diag([imaginary,z(0,-1)]); uv=[z(1,1),z(2,-1)]; out=mv(U,uv)
check('L2-U',mm(dagger(U),U)==I and out==[z(-1,1),z(-1,-2)] and mv(dagger(U),out)==uv and nvec(out)==7,'Dagger matrix products, two components, norm and inverse')
# V=A/sqrt(2); exact checks use A†A/2 and unscaled vector products.
A=[[z(1),imaginary],[imaginary,z(1)]]
check('L2-V-unitary',[[scale(x,F(1,2)) for x in row] for row in mm(dagger(A),A)]==I and mm(A,dagger(A))==diag([z(2),z(2)]),'Cancel sqrt(2) factors exactly, verify both orders')
for inp,expected in [([z(1),imaginary],[z(),z(0,2)]),([z(2),z()],[z(2),z(0,2)])]:
    raw=mv(A,inp)
    check('L2-V-action-'+str(inp),raw==expected and [scale(x,F(1,2)) for x in mv(dagger(A),raw)]==inp and nvec(raw)/2==nvec(inp),'Raw A action; recover with A†/2; compare norm with factor 1/2')
check('L2-transpose-control',[[scale(x,F(1,2)) for x in row] for row in mm(A,A)]==[[z(),imaginary],[imaginary,z()]],'A is symmetric; transpose-only product is not identity')
check('L2-inner-product',sumz([mul(conj(a),b) for a,b in zip([z(1),imaginary],[imaginary,z(1)])])==z(),'Conjugate-first convention')
P=[[z(int(j==k)) for j in range(5)] for k in [2,3,4,0,1]]
old=[imaginary,z(-1),z(2),z(),z(1,1)]
new=mv(P,old);Pc=diag([z(1),z(1),z(1),z(),z()]);Pw=diag([z(),z(),z(),z(1),z(1)])
check('L3-permutation',new==[z(2),z(),z(1,1),imaginary,z(-1)] and mv(dagger(P),new)==old,'Explicit five-row P and inverse')
check('L3-projectors',mm(Pc,Pw)==[[z()]*5 for _ in range(5)] and [add(a,b) for a,b in zip(mv(Pc,new),mv(Pw,new))]==new,'Both complementary components retained')
check('L3-charge',mm(mm(P,diag([z(3),z(3),z(-2),z(-2),z(-2)])),dagger(P))==diag([z(-2),z(-2),z(-2),z(3),z(3)]),'Exact conjugation of charge matrix')
check('L4-determinants',mul(imaginary,z(0,-1))==z(1) and F(2)*F(1,2)==1 and 2*2-1*3==1,'Independent diagonal and 2x2 determinants')
check('L4-lock-and-controls',3*(-2)+2*3==0 and 3*2+2*(-3)==0 and 3*4+2*(-6)==0 and norm(z(2))==4,'Weight exponents and determinant-one nonunitary control')
# Q(sqrt(-3)) exact arithmetic: pair a+b*s with s²=-3.
def smul(a,b):return (a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def spow(a,n):
    v=(F(1),F(0))
    for _ in range(n):v=smul(v,a)
    return v
root=(F(1,2),F(1,2))
check('L1-zeta-unit',smul(root,(root[0],-root[1]))==(1,0),'Exact Q(sqrt(-3)) conjugate product; no rounded roots')
check('L5-zeta-powers',spow(root,2)==(F(-1,2),F(1,2)) and spow(root,3)==(-1,0) and spow(root,6)==(1,0) and len({spow(root,k) for k in range(6)})==6,'Exact quadratic-field expansion of all six powers')
kernel=[]
for k in range(6):
    c=(2*k)%6; w=(-3*k)%6
    ds=[3*c%6,2*w%6]; actions=[(-2*k+c)%6,(3*k+w)%6]
    check('L5-kernel-'+str(k),ds==[0,0] and actions==[0,0],'Integer root exponents for both determinants and action blocks')
    kernel.append(dict(k=k,z_exponent=k,color_exponent=c,weak_exponent=w,determinant_exponents=ds,action_exponents=actions))
for mod,expected in [(3,[0,3]),(2,[0,2,4])]:
    check('L5-toy-'+str(mod),[k for k in range(6) if k%mod==0]==expected and all(((a+b)%6)%mod==((a%mod+b%mod)%mod) for a in range(6) for b in range(6)),'Enumerate all inputs and all 36 composition pairs')
    check('L5-recovery-'+str(mod),all((k%mod)+mod*(k//mod)==k for k in range(6)),'Retained remainder and within-class label reconstruct all inputs')
for inp,phases,expected in [([z(1),z(1)],[imaginary,z(0,-1)],[imaginary,z(0,-1)]),([z(2),imaginary],[z(-1),imaginary],[z(-2),z(-1)]),([z(1),z(2)],[imaginary,z(1)],[imaginary,z(2)])]:
    T=diag(phases); out=mv(T,inp)
    check('L6-local-'+str(inp),out==expected and nvec(out)==nvec(inp) and mv(dagger(T),out)==inp,'Independent local action, norm and inverse')
check('capstone-rubric',sum([10,15,15,15,25,10,10])==100,'Sum seven item weights')
for n in range(1,8):
    txt=(ROOT/f'lesson-{n:02}.md').read_text(encoding='utf-8')
    ids=[f'C14.{n:02}-{suffix}' for suffix in ['E1','W1','P1','D1']]
    check(f'lesson-{n:02}-anchors',all(x in txt for x in ids) and all(x in txt for x in ['Essential question:','Goals:','Prerequisite bridge:','Claim scope:','Worked answers:','Next dependency:']),'Structural presence only; independent human-like content review is separate')
source_checks=[]
for s in packet['sources']:
    actual=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()
    check(s['id']+'-hash',actual==s['sha256'],'Fresh local read-only SHA-256')
    source_checks.append(dict(id=s['id'],sha256=actual))
dump('verification.json',dict(status='passed',python_executable=sys.executable,arithmetic='fractions.Fraction; exact rational complex pairs; Q(sqrt(-3)); integer exponents modulo 6',checks=checks,kernel=kernel,source_hashes=source_checks,lesson_hashes={f'lesson-{n:02}.md':sha(f'lesson-{n:02}.md') for n in range(1,8)},limitations=['General surjectivity and group classification are source-read recognition, not machine-proved here.','Formal certificate execution and physical global-form selection not performed.','Structural anchor checks do not substitute for independent educational audit.']))
print(json.dumps(dict(status='passed',checks=len(checks),python_executable=sys.executable)))
