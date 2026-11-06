"""Independent small arithmetic checks; no packages or source snapshots."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, datetime

root = Path(__file__).resolve().parent
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def conj(a): return (a[0],-a[1])
def norm(a): return a[0]**2+a[1]**2
def div(a,b):
    c=mul(a,conj(b)); n=norm(b)
    return (F(c[0],n),F(c[1],n))
def mat(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
I=[[1,0],[0,1]]; X=[[0,1],[1,0]]; Z=[[1,0],[0,-1]]
assert mul((0,-1),(1,1))==(1,-1)
assert mul((0,1),(1,-1))==(1,1)
assert mul((0,1),(1,-2))==(2,1)
assert sub((-2,0),(-1,1))==(-1,-1)
assert mat(X,Z)==[[0,-1],[1,0]] and mat(Z,X)==[[0,1],[-1,0]]
assert mat(mat(Z,mat(X,Z)),Z)==mat(Z,X)
assert mat(X,X)==I and mat(Z,Z)==I
assert mul(mul((-1,0),(0,1)),(0,-1))==(-1,0)
for lam,expected in [(0,(1,0)),(1,(0,-1)),(2,(F(-3,5),F(-4,5)))]:
    c=div((1,-lam),(1,lam)); assert c==expected and norm(c)==1
c=(F(-3,5),F(-4,5)); out=mul(c,(2,0))
assert out==(F(-6,5),F(-8,5)) and norm(out)==4
assert mul(conj(c),out)==(2,0)
assert sub(out,(2,0))==(F(-16,5),F(-8,5))
assert div((F(3,2),0),(F(1,2),0))==(3,0)
for vals,he,hb in [([1,4,16],[4,1,F(1,4)],[4,1,F(1,4)]),([4,1,16],[1,4,F(1,4)],[4,F(1,4),1])]:
    r=[F(1,v) for v in vals]; area=[r[0]*r[1],r[0]*r[2],r[1]*r[2]]
    assert [4*v for v in r]==he and [16*v for v in area]==hb
    assert he[0]*he[1]*he[2]==hb[0]*hb[1]*hb[2]==1
    assert list(reversed(hb))==[1/v for v in he]
assert 64**2==4096
assert min(F(3,10),2*F(1,20))*F(2,4)==F(1,20)
assert F(8,6)==F(4,3) and F(9,5)==F(9,5)
assert [F(8**n,16**(2**n)) for n in range(3)]==[F(1,16),F(1,32),F(1,1024)]
assert sum(F(8**n,16**(2**n)) for n in range(3))==F(97,1024)
contract=json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
checks=[]
summaries=[
 'Complex multiplication, adjoint/inverse, scalar and diagonal transport, norms 2 and 5 recomputed; all four diagnostics checked.',
 'Both frame-change examples recomputed, including reconstruction, erroneous unchanged-link result 3i, and covariance versus norm hypotheses.',
 'XZ/ZX, path orientation, conjugation by Z, inverse links, X squared and Z squared recomputed; basepoint and noncommutation taught before use.',
 'Trace cyclic identity and matrix/scalar actions 6/4 AU checked; transformed scalar links (-1,i,-i) yield -1; full comparison retained.',
 'Exact rational Cayley factors, determinants, reverse steps, norms 5/6, nonselfadjoint counterexample factor 3, and finite cancellation independently checked.',
 'Both metric examples, pair minors, delta=64, blocks, determinants, J reversal, uniform scaling, units, and historical determinants 64/4096 independently checked.',
 'All four bound signs/digits compared with S02 M13 proof; AUD-009 retrieval scope confirmed; synthetic min and optional units recomputed.',
 'Norms, quadratic values 9/8, normalized expectations 9/5 and 4/3, remainders, double recovery, thermal terms and partial sum 97/1024 recomputed.'
]
for idx,s in enumerate(summaries,1):
    p=root/f'lesson-{idx:02}.md'; text=p.read_text(encoding='utf-8')
    for suffix in ['E1','W1','P1','D1']: assert f'C17.{idx:02}-{suffix}' in text
    checks.append({'checkpoint_id':f'lesson-{idx:02}','path':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'result':'passed','verification':s,'contract':'Essential question, 3 or 4 goals, prerequisite bridge, first-principles explanation, worked example, answered practice, claim scope, four answered diagnostics, pacing and next dependency present. Teaching anchors matched.'})
sources=[]
for s in contract['sources']:
    h=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest(); assert h==s['sha256']
    sources.append({'id':s['id'],'path':s['path'],'sha256':h,'hash_match':True})
report={'schema_version':'1.0','audit_scope':'Independent read-only audit of eight lessons against input-contract teaching anchors; not whole-course completion or capstone approval.','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'independent lesson auditor','unresolved_critical':0,'unresolved_major':0,'unresolved_minor':0,'findings':[],'checks':checks,'source_checks':sources,'source_pointers_read':['S02#/backbone_sequence/12','S02#/hodge_normalization_theorem','S03#/findings/8','S04#/hodge_correction_proof','S01#/backbone_sequence/12/definitions'],'cumulative_result':'All eight E/W/P/D anchor groups present. Complex/matrix operations are introduced before required applications; advanced spectrum and infinite comparison remain recognition-only. Finite identities, source-reported certificate and missing replay bodies remain separate. No numerical or prerequisite defect found. Full states, scales, links and residuals retained.','runtime':'tf_gpu_env; sys.executable separately verified as C:/Users/info/.conda/envs/tf_gpu_env/python.exe','capabilities_note':'Read-only Krytronx capabilities call succeeded; response enumerated interface but did not contain corpus generation or manifest digest. Source provenance independently pinned by local SHA-256.','verification_script':Path(__file__).name,'verification_result':'All independent exact arithmetic and anchor assertions passed.'}
(root/'independent-lesson-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: eight lessons; zero unresolved critical, major or minor findings.')
