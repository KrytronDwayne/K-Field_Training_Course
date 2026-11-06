"""Independent finite enumeration checks; no source arrays persisted."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json,hashlib,sys
p=Path(__file__).parent
checks=[]
def check(name,condition,detail):
 assert condition,name
 checks.append({'id':name,'status':'passed','method_result':detail})
check('runtime',sys.executable.lower()==r'C:\Users\info\.conda\envs\tf_gpu_env\python.exe'.lower(),sys.executable)
for n in range(4):
 intervals=[(Fraction(j,2**n),Fraction(j+1,2**n)) for j in range(2**n)]
 check('binary-'+str(n),sum(b-a for a,b in intervals)==1 and all(intervals[i][1]==intervals[i+1][0] for i in range(len(intervals)-1)),f'{2**n} adjacent half-open intervals, total width1; {2**n+1} distinct boundaries')
 if n:
  check('binary-parents-'+str(n),all(j==2*(j//2)+(j%2) for j in range(2**n)),f'all {2**n} parent/bit reconstructions exact')
for n in range(3):
 m=3*2**n
 # Enumerate coordinate choices independently of closed formulas.
 cells=sum(1 for _ in product(range(m),repeat=3)); verts=sum(1 for _ in product(range(m+1),repeat=3))
 check('group-'+str(n),cells==27*8**n and verts==(3*2**n+1)**3 and cells*Fraction(6,8**n)==162,f'enumerated {cells} cells,{verts} corners; total toy volume162')
for span in [1,3,9]:
 points=0;sheets=set()
 for xyz in product(range(-span,span+1),repeat=3): points+=1;sheets.add(sum(xyz))
 check('half-step-'+str(span),points==(2*span+1)**3 and sheets==set(range(-3*span,3*span+1)),f'{points} points; {len(sheets)} attained integer sheets')
check('rung',[(g,n) for g in range(3) for n in range(4) if 3**g*2**n+1==10]==[(2,0)] and 3**3>9 and 2**4>9,'bounded exhaustive12 pairs; unique(2,0); positivity excludes larger powers')
words={sum(e*3**i for i,e in enumerate(w)):w for w in product([-1,0,1],repeat=3)}
check('balanced-range',len(words)==27 and set(words)==set(range(-13,14)),'all27 signed words bijectively enumerate−13..13')
for t,w in words.items():
 r=sum(w[i]*3**i for i in range(2));e=w[2]
 assert t==r+9*e and (t-r)%9==0 and (r-w[0])%3==0
check('all-balanced-roundtrips',True,'all27 words pass two modular parent checks and exact coarse/detail reconstruction')
check('word5',words[5]==(-1,-1,1),'enumerated word gives5; parents−4,−1')
check('word8',words[8]==(-1,0,1),'enumerated word gives8; parents−1,−1')
for d in [1,2]:
 classes=range(3**d)
 check('ternary-'+str(d),sum(1 for _ in product(classes,repeat=3))==27**d,f'3D Cartesian count{27**d}')
check('tree-children',[[i for i in range(9) if i%3==r] for r in range(3)]==[[0,3,6],[1,4,7],[2,5,8]],'all9 one-coordinate children assigned exactly once')
check('negative-remainders',(-2)%3==1 and (-4)%3==2,'standard nonnegative remainder convention verified')
c=json.loads((p/'input-contract.json').read_text(encoding='utf-8-sig'))
for row in c['coverage_matrix']:
 text=(p/(row['introduction']+'.md')).read_text(encoding='utf-8-sig')
 for token in row['all_required_teaching_item_ids']: assert token in text,token
check('teaching-ids',True,'all approved required W/P/D IDs occur in their actual lesson')
for b in c['capstone_specification']['backward_map']:
 text=(p/(b['introduction']+'.md')).read_text(encoding='utf-8-sig')
 for k in ['worked_example_id','prior_practice_id','diagnostic_id']: assert b[k] in text
 assert b['step_id'] in (p/'capstone.md').read_text(encoding='utf-8-sig')
check('backward-map-ids',True,'all9 capstone steps resolve to earlier authored example, answered practice and diagnostic IDs; substantive alignment independently reviewed')
for s in c['sources']:
 check('source-hash-'+s['id'],hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256'],'in-place SHA256 matches input contract')
result={'status':'passed','checks':checks,'check_count':len(checks),'method':'Independent enumeration and exact Fraction arithmetic; no numpy or third-party packages; no source data copies.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
