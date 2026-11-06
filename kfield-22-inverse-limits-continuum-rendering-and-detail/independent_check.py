from pathlib import Path
from fractions import Fraction as F
import hashlib, json, sys
p=Path(__file__).parent
def residues(ds):
    return [sum(ds[j]*3**j for j in range(i+1))%3**(i+1) for i in range(len(ds))]
assert residues([1,-1,0,1,-1])==[1,7,25,25,187]
assert residues([0,1,-1,0,1])==[0,3,21,75,75]
assert residues([-1]*4)==[2,5,14,41]
assert residues([1]*4)==[1,4,13,40]
assert F(1,128)<=F(1,100)<F(1,64)
assert F(1,2916)<=F(1,1000)<F(1,972)
assert F(1,2187)<=F(1,1000)<F(1,729)
assert F(1,2)*(F(1,3)-F(1,6))==F(1,12)==F(1,2)*F(1,6)
assert [residues(ds)[-1] for ds in ([1,-1,1],[1,-1,-1],[1,-1,0])]==[7,16,25]
P0=[[F(1,4)]*4 for _ in range(4)]
P1=[[F(1,2) if i//2==j//2 else F(0) for j in range(4)] for i in range(4)]
I=[[F(int(i==j)) for j in range(4)] for i in range(4)]
sub=lambda A,B:[[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
Q0=sub(P1,P0);Q1=sub(I,P1)
mul=lambda A,B:[[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
Z=[[F(0)]*4 for _ in range(4)]
sectors=[P0,Q0,Q1]
assert all(mul(A,A)==A for A in sectors)
assert all(mul(A,B)==Z for i,A in enumerate(sectors) for j,B in enumerate(sectors) if i!=j)
assert mul(P0,P1)==P0
mv=lambda A,v:[sum(a*b for a,b in zip(row,v)) for row in A]
assert mv(P0,[2,0,6,4])==[3]*4
assert mv(Q0,[2,0,6,4])==[-2,-2,2,2]
assert mv(Q1,[2,0,6,4])==[1,-1,1,-1]
files={}
for i in range(1,8):
    f=p/f'lesson-{i:02}.md';s=f.read_text(encoding='utf-8')
    assert all(f'C22.{i:02}-{j}1' in s for j in ['E','W','P','D'])
    files[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
source_hashes={}
contract=json.loads((p/'input-contract.json').read_text(encoding='utf-8-sig'))
for src in contract['sources']:
    if src['id'] in ['S02','S03']:
        actual=hashlib.sha256(Path(src['path']).read_bytes()).hexdigest()
        assert actual==src['sha256']
        source_hashes[src['id']]=actual
r={'scope':'Independent authored-lesson audit. Capstone and support artifacts were not available when read; not certified here.','runtime':sys.executable,'reviewed_sha256':files,'source_hashes':source_hashes,'checks':[
{'check':'exact arithmetic','result':'pass','evidence':'Script independently recomputes both five-level digit histories, both constant-digit histories, all three tolerance minima, shared renderer endpoint, cylinder digit ledger, exact rational projector products and practice decomposition.'},
{'check':'E05 actual anchors','result':'pass','evidence':'All 28 E/W/P/D anchors exist. Auditor read substantive content, answers and linked prerequisite operations in all seven lessons.'},
{'check':'source fidelity','result':'pass','evidence':'Directly read S02 /backbone_sequence/17 and S03 /findings/5 and /findings/9; normalized renderer, bound, paired history and conditional-expectation boundary agree. S02/S03 SHA256 checked.'},
{'check':'domain reasoning','result':'pass','evidence':'Manually recomputed block size 2^k, block bound 2^-k, tail bound 2^(1-K), 1/n counterexample and 1/n^2 and 1/n^3 domain tests.'},
{'check':'product rules','result':'pass','evidence':'Manually expanded conditional averaging product with retained centered detail; finite difference terms 3+4+6=13 are correct.'},
{'check':'lesson contract','result':'pass','evidence':'Every lesson has one essential question, 3-4 goals, bridge, locally taught operations, worked example, scope box, four answered diagnostics and next dependency. Synthetic data and units are clearly separated from source claims.'}],
'findings':[{'id':'IA22-001','severity':'minor','status':'open','file':'lesson-07.md','location':'C22.07-E1 inner-product paragraph','finding':'Bounded partial inner products alone do not establish convergence. The conclusion is true but the compressed argument should apply the finite dot-product inequality to tail blocks. Core assessed domain calculations do not depend on this assertion.','suggested_repair':'State that sums of absolute tail products are bounded by the product of square-tail norms, which tends to zero; hence the series is absolutely convergent.'}],
'unresolved_counts':{'critical':0,'major':0,'minor':1},'lessons_modified':False}
lesson7=(p/'lesson-07.md').read_text(encoding='utf-8')
assert 'Choose t=C/B' in lesson7 and 'These nonnegative partial sums increase and stay bounded' in lesson7
r['scope']='Independent seven-lesson and completed capstone/support content audit. Assembly and final validator remain production-manager checks.'
r['findings'][0]['status']='resolved'
r['findings'][0]['resolution']='Re-read repair: expanding sum(a_n-t b_n)^2 proves finite Cauchy-Schwarz; applying it to absolute inputs yields nonnegative increasing bounded partial sums and hence absolute convergence. The B=0 case is handled and scalar B is distinguished from matrix B.'
r['unresolved_counts']={'critical':0,'major':0,'minor':0}
for name in ['capstone.md','course-map.md','teacher-guide.md','terminology.md','sources.md','source-verification.json']:
    files[name]=hashlib.sha256((p/name).read_bytes()).hexdigest()
cap=(p/'capstone.md').read_text(encoding='utf-8')
for i in range(1,8):
    assert f'C22-CAP-{i:02}' in cap
    assert all(f'C22.{i:02}-{j}1' in cap for j in ['E','W','P','D'])
assert F(-1,2)*(F(1,3)+F(1,9))==F(-2,9)
assert F(-1,2)-F(-4,9)==F(-1,18)
r['checks'].extend([
{'check':'IA22-001 repair','result':'pass','evidence':r['findings'][0]['resolution']},
{'check':'capstone answers and E05 alignment','result':'pass','evidence':'Read all seven tasks and keys. CAP01-03/05-07 reuse independently checked answered practice and general compatibility arguments. CAP04 negative rendering gives z2=-2/9, r2=-4/9 LU, limit=-1/2 LU, signed remainder=-1/18 LU; exact rational checks added. Depths 7 and 5, endpoint equality and 28-point rubric agree. All seven trails refer to substantive E/W/P/D content already read; no required new operation.'},
{'check':'supporting artifacts','result':'pass','evidence':'Read course map, teacher guide, terminology, sources and source-verification. Twelve core periods plus three capstone periods total 825 minutes; phase allocations total 55. Source pointers and status distinctions agree with reviewed primary passages; ternary address/dyadic bridge and synthetic matrix/source Cell3 distinctions preserved. Known infinite-operator and filtration gaps remain explicit. Provenance ledger checked against two independently hashed primary sources; graph retrieval transcript not independently replayed.'}
])
(p/'independent-audit.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'unresolved_counts':r['unresolved_counts'],'runtime':sys.executable}))
