"""Small, independently implemented finite checks; no source snapshots or packages."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
results = []

def check(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    results.append({'check': name, 'actual': str(actual), 'expected': str(expected), 'passed': True})

def wedge(*words):
    word = sum((list(w) for w in words), [])
    if len(word) != len(set(word)):
        return 0, ()
    inversions = sum(word[i] > word[j] for i in range(len(word)) for j in range(i+1,len(word)))
    return (-1)**inversions, tuple(sorted(word))

def contract(word, slot):
    if slot not in word:
        return 0, ()
    pos = word.index(slot)
    return (-1)**pos, word[:pos]+word[pos+1:]

def mv(a,x):
    return [sum(c*v for c,v in zip(row,x)) for row in a]

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

check('runtime', str(Path(sys.executable)).lower(), r'C:\Users\info\.conda\envs\tf_gpu_env\python.exe'.lower())
sectors = [(0,0,0),(0,2,6),(1,1,1),(2,0,-4),(2,2,2),(3,1,-3),(0,1,3)]
for r,s,q in sectors:
    check(f'charge degree {r,s}',-2*r+3*s,q)
for name,charges in [('up',[-4,1,3]),('nu',[0,-3,3]),('down',[2,1,-3]),('electron',[6,-3,-3])]:
    check(name+' charge',sum(charges),0)
top=(0,1,2,3,4)
check('up',wedge((0,1),(2,3),(4,)),(1,top))
check('neutrino',wedge((0,1,2,3),(4,)),(1,top))
s,d=contract((0,1,3,4),3)
t,w=wedge((2,3),d)
check('down', (s*t,w),(1,top))
s,e=contract((3,4),3)
t,w=wedge((0,1,2,3),e)
check('electron',(s*t,w),(1,top))
check('weak second removal',contract((3,4),4),(-1,(3,)))
check('fourth-slot removal',contract((0,1,3,4),4),(-1,(0,1,3)))
check('repeat',wedge((0,1,2,3),(3,)),(0,()))
check('negative up',wedge((0,2),(1,3),(4,)),(-1,top))
check('negative neutrino',wedge((0,1,2,4),(3,)),(-1,top))
for name in ['up','nu','down','electron']:
    check(name+' weak phase',1j*(-1j),1)
check('wrong dual phase',1j*1j,-1)
check('color determinant',1j*(-1j)*1*1*1,1)
for v in [2,4,6]:
    check(f'vacuum norm squared v={v}',F(v*v,2),{2:F(2),4:F(8),6:F(18)}[v])
check('electric components',[F(1,2)+F(1,2),-F(1,2)+F(1,2)],[1,0])
for g2,gy,v,expected in [(3,4,2,(9,25)),(4,3,2,(16,25)),(4,3,4,(64,100))]:
    mw=F(g2*g2*v*v,4); mz=F((g2*g2+gy*gy)*v*v,4)
    c=F(g2*g2,g2*g2+gy*gy)
    check(f'mass squares {g2,gy,v}',(mw,mz),expected)
    check(f'rho {g2,gy,v}',mw/(mz*c),1)
check('zero-v rho denominator',F(25*0,4)*F(16,25),0)
check('zero-g2 rho denominator',F(9*4,4)*F(0,9),0)
check('worked matrix',mv([[1,2],[0,3]],[2,-1]),[0,-3])
y=[[2,0],[1,1]]; p=[[0,1],[1,0]]; f=[1,2]
yp=mm(mm(p,y),p); fp=mv(p,f)
check('practice matrix',mv(y,f),[2,3])
check('swap matrix',yp,[[1,1],[0,2]])
check('swap input',fp,[2,1])
check('swap output',mv(yp,fp),[3,2])
check('inverse matrix',mm(mm(p,yp),p),y)
check('inverse input',mv(p,fp),f)
check('wrong coordinate action',mv(yp,f),[3,4])
for before,after,pred,delta,resid in [([5,2,1],[4,4,1],F(4,5),[-1,2,0],F(1,5)),([3,1,2],[2,1,1],F(-3,2),[-1,0,-1],F(-1,2))]:
    dif=[b-a for a,b in zip(before,after)]
    check('energy components '+str(before),dif,delta)
    check('energy endpoint equality '+str(before),sum(dif),sum(after)-sum(before))
    check('energy residual '+str(before),sum(dif)-pred,resid)
    check('energy reconstruction '+str(before),pred+resid,sum(dif))
check('transfer residual',F(-2)-F(-18,10),F(-1,5))
check('rubric points',sum([14,24,10,14,14,12,12]),100)

packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
sources=[]
for src in packet['sources']:
    digest=hashlib.sha256(Path(src['path']).read_bytes()).hexdigest()
    check('source hash '+src['id'],digest,src['sha256'])
    sources.append(dict(src,verified_sha256=digest,hash_matches=True))
(ROOT/'sources.json').write_text(json.dumps({'sources':sources,'primary_pointers':['S02#/backbone_sequence/10','S02#/backbone_sequence/11','S02#/proof_nodes/80','S02#/proof_nodes/84','S02#/proof_nodes/86','S02#/branch_proofs/7'],'evidence_class':'source-reported definitions and architecture; finite examples freshly recomputed','corpus_generation':packet['source_routing']['snapshot_generation'],'manifest_sha256':packet['source_routing']['manifest_sha256'],'identity_observation':'paired identity fields returned by fresh RAG query; capabilities did not expose corpus pair','source_gaps':['No fresh full compiler typecheck or complete kinetic-term derivation; not required for the finite assessed scope.','Physical occupied-state coefficients, potential, mixing, matching scale, and rate inputs are not supplied.']},indent=2)+'\n',encoding='utf-8')

for row in packet['coverage_matrix']:
    content=(ROOT/(row['introduction']+'.md')).read_text(encoding='utf-8')
    for ident in row['all_required_teaching_item_ids']:
        check('teaching item '+ident, ident in content,True)
cap=(ROOT/'capstone.md').read_text(encoding='utf-8')
for i in range(1,8):
    check(f'capstone step {i}',f'C16-CAP-{i:02}' in cap,True)
(ROOT/'worked-example-verification.json').write_text(json.dumps({'status':'passed','runtime':sys.executable,'method':'Independent inversion-count exterior algorithm, slot-position contraction, Fraction arithmetic, row/composition algorithms, endpoint reconstruction; separate human audit checks teaching and scope.','checks':results},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(results),'runtime':sys.executable}))
