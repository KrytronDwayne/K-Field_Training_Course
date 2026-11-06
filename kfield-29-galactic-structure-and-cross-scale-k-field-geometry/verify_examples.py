"""Fresh, small source checks and exact synthetic example verification; no catalog copies."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D
from itertools import product
import json,hashlib,math
ROOT=Path(__file__).resolve().parent
contract=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
checks=[]
def check(label,actual,expected):
    assert actual==expected,(label,actual,expected)
    checks.append({'id':label,'actual':str(actual),'expected':str(expected),'status':'passed'})
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def trans(a):return list(map(list,zip(*a)))
def mul(a,b):return [[dot(r,c) for c in trans(b)] for r in a]
def mv(a,v):return [dot(r,v) for r in a]
def det(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
source_records=[]
for s in contract['sources']:
    p=Path(s['path']); h=hashlib.sha256(p.read_bytes()).hexdigest()
    check('sha256-'+s['id'],h,s['sha256'])
    source_records.append(dict(id=s['id'],path=str(p),sha256=h,evidence_class='archival source',fresh_hash_match=True))
G=json.loads(Path(next(s['path'] for s in contract['sources'] if s['id']=='G01')).read_text())
S=json.loads(Path(next(s['path'] for s in contract['sources'] if s['id']=='S02')).read_text())
ga=G['ordered_direct_basis_A']; gq=G['reciprocal_basis_Q']
closure=mul(trans(gq),ga)
closure_residual=[[closure[i][j]-int(i==j) for j in range(3)] for i in range(3)]
check('galaxy-determinant-positive',det(ga)>0,True)
check('galaxy-reciprocal-closure-within-1e-12',max(abs(x) for r in closure_residual for x in r)<1e-12,True)
sb=S['mature_locked_cell3']['B_nm']
check('mature-determinant-negative',det(sb)<0,True)
sm=mul(trans(sb),sb)
sm_residual=[[sm[i][j]-S['mature_locked_cell3']['direct_metric_nm2'][i][j] for j in range(3)] for i in range(3)]
check('mature-Gram-within-1e-12',max(abs(x) for r in sm_residual for x in r)<1e-12,True)
check('L01-directed-antipodal-dot',dot([1,0,0],[-1,0,0]),-1)
check('L01-perpendicular-dot',dot([1,0,0],[0,1,0]),0)
check('L02-u-domain',dot([1,0,0],[0,0,1]),0)
check('L02-phase-closure-in-pi-units',F(2,3)+F(2,3),F(4,3))
check('L02-F-square',F(3)+2*(-F(1,2))*3,F(0))
check('L02-D-relative',3*(1+F(1,2)),F(9,2))
check('L02-regular-transfer',F(2)/F(1,2),F(4))
check('L02-address',F(2)*F(3,4)-F(1,2),F(1))
phi=[F(1,4),F(1,2)]; k=[1,-1]; kp=[a+b for a,b in zip(k,phi)]
check('L03-identity-center',kp,[F(5,4),-F(1,2)])
check('L03-scaled-center',mv([[2,0],[0,3]],kp),[F(5,2),-F(3,2)])
for t,z in [(F(1,2),1),(-F(1,2),0),(-F(3,2),-1)]:
    check('L03-owner-'+str(t),math.floor(t+F(1,2)),z)
    check('L03-reconstruction-'+str(t),F(z)+(t-z),t)
for diag in [[1,2,3],[2,1,4]]:
    a,b,c=trans([[diag[i] if i==j else 0 for j in range(3)] for i in range(3)])
    ab=[F(x-y,2) for x,y in zip(a,b)]; bc=[F(x-y,2) for x,y in zip(b,c)]; ac=[F(x-y,2) for x,y in zip(a,c)]
    check('L04-root-closure-'+str(diag),[x+y for x,y in zip(ab,bc)],ac)
    check('L04-root-normal-'+str(diag),[dot([F(1,x) for x in diag],r) for r in [ab,bc,ac]],[F(0)]*3)
M=[[2,1],[1,2]]; inv=[[F(2,3),-F(1,3)],[-F(1,3),F(2,3)]]
check('L05-inverse',mul(M,inv),[[1,0],[0,1]])
for q,v in [([1,-1],2),([1,1],6),([2,0],8)]:check('L05-metric-'+str(q),dot(q,mv(M,q)),v)
x=[F(931,1000),F(49,1000)]; b=[F(9,10),F(1,10)]; r=[a-c for a,c in zip(x,b)]
check('L05-skew-zero',dot(x,x),F(869162,1000000))
check('L05-skew-b',dot(r,r),F(3562,1000000))
states=list(product([-1,0,1],repeat=3)); counts=[sum(sum(s)==i for s in states) for i in range(-3,4)]
check('L06-all-sheet-counts',counts,[1,3,6,7,6,3,1])
check('L06-all-nodes',len(states),27)
check('L06-occupancy-differences',[h-d for d,h in zip([1,2,1],[0,3,1])],[-1,1,0])
check('L06-residual',F(1)-F(4,5),F(1,5))
check('L07-population-sum',57076+57305,114381)
check('L07-phase-change',F(1,3)-F(1,4),F(1,12))
check('L07-old-residual',F(3,10)-F(1,4),F(1,20))
check('L07-new-residual',F(3,10)-F(1,3),-F(1,30))
check('L08-scaling-volume',2**3*6,48)
for vals,expected in [([1,1,3,3],-F(1,4)),([3,3,1,1],F(1,4)),([2,2,2,2],F(0))]:
    check('L08-contrast-'+str(vals),F(vals[0]+vals[1]-vals[2]-vals[3],2*sum(vals)),expected)
occ=G['observed_27_node_occupancy']
# Re-read decimal lexemes exactly for subtraction; do not pretend they are exact empirical ratios.
GD=json.loads(Path(next(s['path'] for s in contract['sources'] if s['id']=='G01')).read_text(),parse_float=D)
od=GD['observed_27_node_occupancy']; dv=od['sheet_fractions_discovery']; hv=od['sheet_fractions_holdout']; rv=od['sheet_fractions_rotation_mean']
rows=['# Source comparison ledger','', 'G01#/observed_27_node_occupancy. All seven sheets are retained; these are stored source fractions, not raw catalog copies. Decimal subtraction is performed on stored lexemes. Source identity and exact path are in sources.md.','', '| Sheet | Discovery | Holdout | Rotation mean | Holdout − discovery | Holdout − rotation mean |','|---|---|---|---|---|---|']
for i,d,h,r0 in zip(range(-3,4),dv,hv,rv):rows.append(f'| {i} | {d} | {h} | {r0} | {h-d} | {h-r0} |')
rows+=['','Stored-fraction sum remainders from one:']+[f'- {label}: {sum(v)-1}' for label,v in [('discovery',dv),('holdout',hv),('rotation mean',rv)]]
rows+=['','All 27 available state labels, grouped by sheet (these are combinatorial labels, not observed counts):','']
for i in range(-3,4):rows.append(f'- {i}: '+', '.join(str(s) for s in states if sum(s)==i))
rows+=['','The full empirical 27-state vectors are not supplied in this small G01 summary. The course retains their source reference and does not fabricate their entries or claim to replay the reported correlation. G02 pp17–19 reports the full-state analysis. The source pure-coordinate family result remains separate from the mixed branch-lift occupancy.']
(ROOT/'source-comparison.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
result={'status':'passed','method':'Exact Fraction synthetic checks; Decimal subtraction of source lexemes; binary64 matrix replay with signed residuals retained. Assertions independently implement the taught operations.','checks':checks,'sources':source_records,'galaxy_QtA_minus_I':closure_residual,'galaxy_determinant_recomputed':det(ga),'mature_determinant_recomputed':det(sb),'mature_Gram_minus_stored':sm_residual,'limits':['No catalog, controls, full 27-state correlation or physical-distance replay.','G03 symbolic boundary exercises are not a fresh historical geometry replay.']}
(ROOT/'worked-example-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks),'closure_max':max(abs(x) for row in closure_residual for x in row)}))
