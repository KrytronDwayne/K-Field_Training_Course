import json, math, itertools, hashlib, sys
from pathlib import Path
from collections import Counter
from fractions import Fraction

root=Path(__file__).parent
packet=json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
sources=[]
for src in packet['sources']:
    p=Path(src['path']); h=hashlib.sha256(p.read_bytes()).hexdigest()
    assert h==src['sha256'],src['id']
    sources.append({'id':src['id'],'sha256':h,'matches':True})
s=json.loads(Path(packet['sources'][1]['path']).read_text(encoding='utf-8-sig'))
r=math.sqrt(2)
u=[(.5,r/2,.5),(1/r,0,-1/r),(.5,-r/2,.5)]
l=[r,0,-r]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
A=lambda x:(x[1],x[0]+x[2],x[1])
assert all(abs(x-y)<1e-12 for v,e in zip(u,l) for x,y in zip(A(v),[e*t for t in v]))
assert all(abs(dot(a,b)-(i==j))<1e-12 for i,a in enumerate(u) for j,b in enumerate(u))
nodes=list(itertools.product(range(3),repeat=3))
def neighbors(n):
    for k in range(3):
        for d in (-1,1):
            nn=list(n); nn[k]+=d
            if 0<=nn[k]<3: yield tuple(nn)
modes=[]; maxerr=0
for inds in itertools.product(range(3),repeat=3):
    v={n:math.prod(u[inds[k]][n[k]] for k in range(3)) for n in nodes}
    eigen=sum(l[i] for i in inds)
    maxerr=max(maxerr,max(abs(sum(v[m] for m in neighbors(n))-eigen*v[n]) for n in nodes))
    modes.append(list(v.values()))
assert maxerr<1e-12
assert all(abs(dot(a,b)-(i==j))<1e-12 for i,a in enumerate(modes) for j,b in enumerate(modes))
counts=Counter(sum(t) for t in itertools.product((-1,0,1),repeat=3))
assert [counts[i] for i in range(-3,4)]==[1,3,6,7,6,3,1]
degrees=Counter(len(list(neighbors(n))) for n in nodes)
assert degrees=={3:8,4:12,5:6,6:1}
for f in [(1,2,3),(2,0,0)]:
    cs=[dot(v,f) for v in u]
    rec=[sum(cs[j]*u[j][i] for j in range(3)) for i in range(3)]
    assert max(abs(a-b) for a,b in zip(rec,f))<1e-12
chi=Counter((-1)**sum(t) for t in itertools.product((-1,0,1),repeat=3))
assert chi=={1:13,-1:14}
M=[[Fraction(x) for x in row] for row in s['backbone_sequence'][16]['channel_matrix_A']]
rank=0
for j in range(6):
    pivot=next((i for i in range(rank,len(M)) if M[i][j]),None)
    if pivot is None: continue
    M[rank],M[pivot]=M[pivot],M[rank]
    z=M[rank][j]; M[rank]=[x/z for x in M[rank]]
    for i in range(len(M)):
        if i!=rank:
            z=M[i][j]; M[i]=[a-z*b for a,b in zip(M[i],M[rank])]
    rank+=1
assert rank==6
anchors=[]
for i in range(1,8):
    text=(root/f'lesson-{i:02}.md').read_text(encoding='utf-8-sig')
    ids=[f'C12.{i:02}-{suffix}' for suffix in ('E1','W1','P1','D1')]
    assert all(x in text for x in ids)
    anchors+=ids
out={'runtime':sys.executable,'verified_source_hashes':sources,'all_28_required_anchors_present':True,'path_eigenpairs_and_orthonormality':True,'all_27_product_eigenpairs_and_729_dots_checked':True,'maximum_numeric_eigenpair_error':maxerr,'numeric_tolerance':1e-12,'multiplicities':[counts[i] for i in range(-3,4)],'degree_histogram':dict(degrees),'chi_counts':dict(chi),'M17_exact_rational_rank':rank,'reconstruction_examples':[(1,2,3),(2,0,0)]}
(root/'independent-computation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
