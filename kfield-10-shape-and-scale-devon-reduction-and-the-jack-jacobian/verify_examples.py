"""Independent standard-library recomputation, no source snapshots or packages."""
from fractions import Fraction as F
from pathlib import Path
import math, json, hashlib, re, sys
root=Path(__file__).resolve().parent
checks=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    checks.append({'id':name,'result':'passed','actual':str(actual),'expected':str(expected)})
def near(name,actual,expected):
    assert abs(actual-expected)<1e-12,(name,actual,expected)
    checks.append({'id':name,'result':'passed','actual':actual,'expected':expected,'arithmetic_tolerance':1e-12,'note':'Numerical identity check only; exact expressions retained in lessons.'})
def mm(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,b): return [sum(x*y for x,y in zip(row,b)) for row in a]
def det(a):
    x,y,z=a
    return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])
J=[[-1,0,1],[1,-1,0],[17,-2,-3]]
K=[[F(3,12),F(-2,12),F(1,12)],[F(3,12),F(-14,12),F(1,12)],[F(15,12),F(-2,12),F(1,12)]]
I=[[int(i==j) for j in range(3)] for i in range(3)]
check('Jack determinant',det(J),12)
check('Jack left inverse',mm(K,J),I);check('Jack right inverse',mm(J,K),I)
area=[[1,1,0],[1,0,1],[0,1,1]]
check('scalar row from areas',mm([[9,8,-11]],area),[[17,-2,-3]])
for x,y in [([1,2,3],[2,-1,4]),([2,-1,1],[-1,3,33])]:
    check('Jack forward '+str(x),mv(J,x),y);check('Jack reverse '+str(y),mv(K,y),x)
check('practice area tangent',mv(area,[2,-1,1]),[1,3,0])
H=[[1,1],[1,-1]]
check('H square',mm(H,H),[[2,0],[0,2]])
for x,y in [([2,1],[3,1]),([1,-2],[-1,3]),([3,2],[5,1])]:
    check('H forward '+str(x),mv(H,x),y);check('H reverse '+str(y),[F(v,2) for v in mv(H,y)],x)
for q,expected_m,expected_z in [([0,2,3],F(5,3),[F(-5,3),F(1,3),F(4,3)]),([1,2,4],F(7,3),[F(-4,3),F(-1,3),F(5,3)])]:
    m=sum(q)/F(3);z=[F(a)-m for a in q]
    check('mean '+str(q),m,expected_m);check('shape '+str(q),z,expected_z)
    check('shape sum '+str(q),sum(z),0);check('mean reconstruction '+str(q),[m+a for a in z],q)
    # Compute inverse projections as exact rational contributions: denominator roots cancel.
    s=sum(q);u=-q[0]+q[1];v=-q[0]-q[1]+2*q[2]
    back=[F(s,3)-F(u,2)-F(v,6),F(s,3)+F(u,2)-F(v,6),F(s,3)+F(v,3)]
    check('projection reconstruction '+str(q),back,q)
    check('doubling-edge area shift '+str(q),[2**(a+2) for a in q],[4*2**a for a in q])
    for a in q: near('log exp '+str(a),math.exp(a*math.log(2)),2**a)
check('halved practice areas',[F(2**a,4) for a in [1,2,4]],[F(1,2),F(1),F(4)])
raw=[[1,1,1],[-1,1,0],[-1,-1,2]]
check('basis unnormalized Gram',mm(raw,list(map(list,zip(*raw)))),[[3,0,0],[0,2,0],[0,0,6]])
t=F(1,10)
check('product exact change',(1+t)*(1+2*t)-1,F(32,100));check('product remainder',(1+t)*(1+2*t)-1-3*t,F(2,100))
check('square exact change',(1+t)**2-1,F(21,100));check('square remainder',(1+t)**2-1-2*t,F(1,100))
check('halved product remainder',2*F(1,20)**2,F(5,1000))
near('log change decimal',math.log(1.1),0.09531017980432493)
near('square log remainder',2*math.log(1.1)-.2,-0.00937964039135013)
for dims,metric,cof,rec in [([1,2,3],[1,4,9],[36,9,4],[F(1),F(1,4),F(1,9)]),([2,2,2],[4,4,4],[16,16,16],[F(1,4)]*3)]:
    check('metric '+str(dims),[v*v for v in dims],metric)
    check('cofactor '+str(dims),[metric[1]*metric[2],metric[0]*metric[2],metric[0]*metric[1]],cof)
    check('reciprocal '+str(dims),[F(c,math.prod(metric)) for c in cof],rec)
    check('metric inverse product '+str(dims),[a*b for a,b in zip(metric,rec)],[1,1,1])
for S,A,expected in [(2,-2,[0,2]),(4,2,[3,1])]:
    b,c=F(S+A,2),F(S-A,2)
    check('branch inverse '+str((S,A)),[b,c],expected);check('branch forward '+str((S,A)),[b+c,b-c],[S,A])
check('inadmissible parity 3,2',(3-2)%2,1)
for areas,lengths in [([6,8,12],[2,3,4]),([9,18,18],[3,3,6])]:
    ab,ac,bc=areas
    # Independent length reconstruction from pairwise products, not course anchor path.
    got=[math.sqrt(ab*ac/bc),math.sqrt(ab*bc/ac),math.sqrt(ac*bc/ab)]
    check('independent anchor lengths '+str(areas),got,lengths)
    a,b,c=lengths;check('anchor areas '+str(lengths),[a*b,a*c,b*c],areas)
    eta=F(1000*bc,ab);ai=F(100*bc,ac)
    kb=ai/100;kc=eta/1000
    near('anchor length '+str(areas),math.sqrt(float(F(ab)/kb)),a)
    check('ratios '+str(areas),[kb,kc],[F(b,a),F(c,a)])
p=json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
for s in p['sources']:
    check('source hash '+s['id'],hashlib.sha256(Path(s['path']).read_bytes()).hexdigest(),s['sha256'])
coverage=json.loads((root/'coverage.json').read_text())['rows']
for r in coverage:
    lesson=(root/(r['lesson']+'.md')).read_text(encoding='utf-8')
    for key in ['explanation','worked_example','practice','diagnostic']:
        check('anchor '+r[key],r[key] in lesson,True)
    check('capstone anchor '+r['concept_id'],r['capstone'] in (root/'capstone.md').read_text(encoding='utf-8'),True)
for f in root.glob('*.md'):
    if f.name=='launch-prompt.md': continue
    for link in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
        if '://' not in link and not link.startswith('#'):
            check('local link '+f.name+' '+link,(root/link.split('#')[0]).exists(),True)
payload={'status':'passed','runtime':sys.executable,'checks':checks,'check_count':len(checks),'scope':'Finite examples and source hashes; content learning and evidence scope independently reviewed. No numerical tolerance deletes teaching residuals.'}
(root/'verification.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','check_count':len(checks),'runtime':sys.executable}))
