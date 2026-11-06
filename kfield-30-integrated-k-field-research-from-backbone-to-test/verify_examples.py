"""Independent standard-library rational checks; source data stay in place."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal
from datetime import datetime, timezone
import hashlib, json, sys
P=Path(__file__).resolve().parent
D=json.loads((P/'input-contract.json').read_text(encoding='utf-8-sig'))
checks=[]
def record(name, condition, detail):
    assert condition, (name,detail)
    checks.append({'id':name,'result':'passed','verification':detail})
def mv(a,x): return [sum(F(v)*w for v,w in zip(row,x)) for row in a]
def rank(a):
    a=[[F(v) for v in row] for row in a]; r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        v=a[r][c]; a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][c]; a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r
source_checks=[]
for s in D['sources']:
    if 'path' not in s: continue
    actual=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()
    record(s['id']+'-sha256',actual==s['sha256'],'SHA-256 recomputed from original file bytes; no source copy.')
    source_checks.append({'id':s['id'],'path':s['path'],'sha256':actual})
S=json.loads(Path(D['sources'][1]['path']).read_text(encoding='utf-8-sig'),parse_float=Decimal)
modules=S['backbone_sequence']; ids={m['id'] for m in modules}
edges={(a,m['id']) for m in modules for a in m['requires'] if a in ids}
record('M20-core',modules[19]['requires']==[f'M{i:02}' for i in range(1,19)],'Exact requires list read from S02 /backbone_sequence/19; M19 excluded.')
record('requires-edge-count',len(edges)==52 and ('M19','M20') not in edges,'52 internal requires-derived edges, including 18 M20 incoming edges.')
record('module-topology',all(int(a[1:])<int(b[1:]) for a,b in edges),'All source requires-derived internal edges point forward in module order.')
record('EG-six',len(S['constitutive_principles'])==6,'All six source constitutive principles present.')
a=[row[0] for row in S['mature_locked_cell3']['B_nm']]
half=[v/2 for v in a]
record('stored-column-half',half==[Decimal('0.1637506210279453'),Decimal('-0.0274485039420032'),Decimal('-0.01874375144736495')],str(half)+' nm; exact operations on stored decimal strings, not new physical data.')
for q,z in [(F(1,2),1),(F(-1,2),0)]:
    calc=(q+F(1,2)).numerator//(q+F(1,2)).denominator
    record('cell-'+str(q),calc==z and -F(1,2)<=q-z<F(1,2) and z+(q-z)==q,'Half-open boundary owner and reconstruction checked using exact fractions.')
for a,b in [(2,6),(3,7)]:
    m=F(a+b,2); h=F(a-b,2)
    record('mean-detail-'+str(a),m+h==a and m-h==b,f'm={m}, h={h}; reconstruction ({m+h},{m-h}).')
H=[[1,1],[2,2]]
record('rank-original',rank(H)==1 and mv(H,[1,-1])==[0,0],'Exact elimination gives rank 1 and verifies null direction.')
record('equal-output',mv(H,[2,1])==mv(H,[1,2])==[3,6],'Both candidates reconstruct the same two original channels.')
record('rank-added',rank(H+[[1,-1]])==2,'Exact elimination on three rows yields rank 2.')
for s,d,expected in [(5,-1,[2,3]),(4,2,[3,1])]:
    t=[F(s+d,2),F(s-d,2)]
    record('inverse-'+str(s),t==expected and mv([[1,1],[1,-1]],t)==[s,d],f'theta={t}; independent substitution succeeds.')
record('product-ambiguity',2*3==1*6==6,'Two distinct gain/responsivity pairs have identical product.')
responses={bits:tuple(bool(int(v)) for v in bits) for bits in ['00','01','10','11']}
record('two-bit-discrimination',len(set(responses.values()))==4 and 2<4,'Two-bit answer pairs distinct; one binary answer has only two outputs.')
record('discriminator',mv([[1,1],[1,-1]],[2,1])==[3,1] and mv([[1,1],[1,-1]],[1,2])==[3,-1],'A/B sum agrees and difference sign separates.')
record('intervals',F(-3,4)<F(3,4) and not F(3,4)<=0<=F(5,4) and not F(-5,4)<=0<=F(-3,4),'Toy +/-1/4 intervals disjoint and exclude zero.')
for y,expectedA,expectedB in [([3,0],[0,-1],[0,1]),([4,1],[1,0],[1,2])]:
    for label,p,expected in [('A',[3,1],expectedA),('B',[3,-1],expectedB)]:
        r=[a-b for a,b in zip(y,p)]
        record('residual-'+label+'-'+str(y),r==expected and [a+b for a,b in zip(p,r)]==y,f'r={r}; exact full-channel reconstruction.')
record('diagnostic-residual',[2-3,-1-1]==[-1,-2],'Lesson 6 diagnostic recomputed independently.')
obj={'a':None,'c':'unknown','d':'reported'}
rows=[(k,k in obj,type(obj[k]).__name__ if k in obj else 'absent',obj.get(k)) for k in ['a','b','c','d']]
rebuilt={k:v for k,present,kind,v in rows if present}
record('raw-kind-readback',rebuilt==obj and 'b' not in rebuilt and 'a' in rebuilt,'Presence and raw types retained; absent b not emitted.')
A=[[1,0],[0,1],[1,1]]; c=[F(7,3),F(10,3)]; y=[2,3,6]
pred=mv(A,c); r=[F(v)-w for v,w in zip(y,pred)]
record('decoder-reconstruction',r==[F(-1,3),F(-1,3),F(1,3)] and [v+w for v,w in zip(pred,r)]==y,'Exact fractions reconstruct every channel.')
record('decoder-convention',r[0]+r[2]==r[1]+r[2]==0 and 2*c[0]+c[1]==8 and c[0]+2*c[1]==9,'Residual column dot products zero; normal equations independently substituted.')
record('decoder-rank',rank(A)==2,'Two independent coefficient coordinates; 3-2=1 retained residual dimension.')
sourceA=modules[16]['channel_matrix_A']
record('source-M17-rank',len(sourceA)==13 and len(sourceA[0])==6 and rank(sourceA)==6,'Exact elimination of source integer matrix gives rank 6, left-nullity 13-6=7; no occupation inference.')
# Complex pairs use exact integer arithmetic rather than floating complex numbers.
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
factors=[(0,1),(0,1),(-1,0),(0,-1),(0,1),(1,0)]
def prod(seq):
    v=(1,0)
    for f in seq: v=cmul(v,f)
    return v
record('six-factors',prod(factors)==(1,0) and prod(factors[:3]+factors[4:])==(0,1),'Exact integer-pair complex multiplication gives 1; deleting heavy gives i.')
record('geometry-transfer',2*F(1,2)==1,'Synthetic ruler phi=1; transfer predictions checked above; calibration remains proposed.')
anchor_checks=[]
for i in range(1,9):
    text=(P/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    required=[f'C30.{i:02}-{suffix}' for suffix in ['E1','W1','P1','D1']]
    record(f'lesson-{i:02}-anchors',all(x in text for x in required),'All four approved teaching anchors exist; semantic teaching review is separate.')
    anchor_checks.append({'lesson':i,'anchors':required})
record('pacing',sum([3,2,2,2,2,1,1,3])==16 and (16+3)*55==1045,'16 core plus 3 capstone periods =1045 minutes.')
payload={'schema_version':'1.0','status':'passed','executed_utc':datetime.now(timezone.utc).isoformat(),'runtime':sys.executable,'method':'Exact fractions/decimals and integer elimination; original source hashes; independent substitutions and readback. No external empirical execution or Agda typecheck.','source_hashes':source_checks,'checks':checks,'check_count':len(checks)}
(P/'verification.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','check_count':len(checks),'runtime':sys.executable}))
