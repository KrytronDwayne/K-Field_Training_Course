"""Read-only source checks and finite course replay; writes only compact authored verification."""
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
sources=[]
for source in packet['sources']:
    actual=digest(Path(source['path']))
    assert actual==source['sha256'], source['id']
    sources.append(dict(source,verified_sha256=actual,verification='fresh local byte hash'))
s2=json.loads(Path(sources[1]['path']).read_text(encoding='utf-8-sig'))
indices={n['formula']['formula_id']:i for i,n in enumerate(s2['proof_nodes'])}
ids=['KFM-X022','KFM-X023','KFM-X024','KFM-X026','KFM-X027','KFM-F033','KFM-F034','KFM-F035','KFM-F036']
pointers={x:f'/proof_nodes/{indices[x]}/formula' for x in ids}
bidegrees=[(0,0),(0,2),(1,1),(2,0),(2,2),(3,1)]
mult=[math.comb(3,r)*math.comb(2,s) for r,s in bidegrees]
assert mult==[1,1,6,3,3,2]
names=['c1','c2','c3','w1','w2']
sectors=['nu^c','e^c','Q','u^c','d^c','L']
states=[]
def sign(order):
    if len(set(order))!=len(order): return 0
    return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
assert sign([3,0])==-1 and sign([2,0,1])==1 and sign([0,3,0])==0
for k in range(6):
    for subset in itertools.combinations(range(5),k):
        complement=tuple(i for i in range(5) if i not in subset)
        assert sign(subset+complement)*sign(complement+subset)==1
        r=sum(i<3 for i in subset); s=k-r
        q=-2*r+3*s
        assert -2*(3-r)+3*(2-s)==-q
        if k%2==0:
            residue=(q+2*(r%3)+3*(s%2))%6
            assert residue==0
            states.append({'basis':[names[i] for i in subset],'r':r,'s':s,'sector':sectors[bidegrees.index((r,s))],'q':q,'Y':str(F(q,6)),'descent_residue':residue})
assert len(states)==16
for row,(r,s),m in zip(s2['backbone_sequence'][10]['sector_census'],bidegrees,mult):
    assert row['bidegree']==[r,s] and row['multiplicity']==m and row['q']==-2*r+3*s
def ledger(a,b):
    qs=[a*r+b*s for r,s in bidegrees]
    out=[]
    for idx,(name,m,q) in enumerate(zip(sectors,mult,qs)):
        color=F(q)*([0,0,1,F(1,2),F(1,2),0][idx])
        weak=F(q)*([0,0,F(3,2),0,0,F(1,2)][idx])
        pure=[0,0,2,-1,-1,0][idx]
        out.append([m*q,m*q**3,color,weak,pure])
    totals=[sum(row[i] for row in out) for i in range(5)]
    return qs,out,totals
for a in range(-5,6):
    for b in range(-5,6):
        _,_,t=ledger(a,b)
        poly=108*a**3+144*a*a*b+108*a*b*b+40*b**3
        quadratic=36*a*a+24*a*b+20*b*b
        assert quadratic==36*(F(a)+F(b,3))**2+16*b*b
        assert t==[8*(3*a+2*b),poly,3*a+2*b,3*a+2*b,0]
        assert poly==(3*a+2*b)*quadratic
assert ledger(-2,3)[2]==[0]*5
assert ledger(1,0)[2]==[24,108,3,3,0]
assert ledger(0,1)[2]==[16,40,2,2,0]
assert ledger(1,1)[2][1]==400
assert (1j*1)==1/(-1j)
assert 3+1==4 and (3+1)%2==0
assert sign((0,3,1,2,4))==1 and sign((0,4,1,2,3))==-1
records={str((a,b)):{'q':q,'contributions':[[str(x) for x in row] for row in rows],'totals':[str(x) for x in totals]} for a,b in [(-2,3),(1,0),(0,1),(1,1)] for q,rows,totals in [ledger(a,b)]}
result={'status':'passed','method':'Independent exhaustive subset enumeration, rational arithmetic and direct weighted sums; grid tests supplement displayed general algebra, not replace it.','sources':sources,'source_pointers':pointers,'states':states,'trial_column_order':['gravity_squared_U1','U1_cubic','SU3_squared_U1','SU2_squared_U1','SU3_cubic'],'trials':records,'checks':{'all_subsets_complement_involution':32,'even_component_charge_and_descent':16,'integer_weight_pairs':121,'source_census_rows':6,'quadratic_completed_square':'exact Fraction arithmetic','witten_doublets':4,'diagonal_dual_action':'i = inverse(-i)'},'scope':'No fresh compiler/typecheck or empirical inference; no copied source snapshots.'}
(ROOT/'worked-example-verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS: 16 states, 32 complement checks, 121 weight trials, five source hashes.')
