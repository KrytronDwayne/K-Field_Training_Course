"""Exact small-ledger checks; source files are read-only, never copied."""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, sys

P=Path(__file__).parent
contract=json.loads((P/'input-contract.json').read_text(encoding='utf-8-sig'))
def dump(name,x): (P/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def nint(t):
    u=F(t)-F(1,2)
    return -((-u.numerator)//u.denominator)
def row(r,g):
    k=27**g
    q=[nint(k*t) for t in r]
    e=[F(a)-k*t for a,t in zip(q,r)]
    assert all(-F(1,2)<=t<F(1,2) for t in e)
    assert [(a-t)/k for a,t in zip(q,e)]==r
    return q,e
def ledger(r,depth):
    out=[]; cs=[]
    for g in range(depth+1):
        q,e=row(r,g)
        if g:
            c=[a-27*b for a,b in zip(q,oldq)]
            assert c==[nint(-27*t) for t in olde]
            assert e==[27*a+b for a,b in zip(olde,c)]
            s,a=c[1]+c[2],c[1]-c[2]
            assert (s+a)//2==c[1] and (s-a)//2==c[2] and (s-a)%2==0
            assert [(a-b)/27 for a,b in zip(e,c)]==olde
            cs.append(c)
        else: c=None;s=a=None
        out.append(dict(g=g,K=27**g,Q=q,epsilon=list(map(str,e)),C=c,S=s,A=a))
        oldq,olde=q,e
    recovered=[F(out[0]['Q'][i])+sum(F(c[i],27**j) for j,c in enumerate(cs,1))-olde[i]/27**depth for i in range(3)]
    assert recovered==r
    return out

sources=[]; loaded={}
for s in contract['sources']:
    raw=Path(s['path']).read_bytes(); digest=hashlib.sha256(raw).hexdigest()
    assert digest==s['sha256'],s['id']
    loaded[s['id']]=json.loads(raw.decode('utf-8-sig'),parse_float=str)
    sources.append(dict(id=s['id'],path=s['path'],sha256=digest,hash_verified=True))

# Independent nearest-neighbor implementation tests the ceiling implementation.
for den in range(1,31):
    for num in range(-200,201):
        t=F(num,den); lower=t.numerator//t.denominator
        expected=lower if t-lower<=F(1,2) else lower+1
        assert nint(t)==expected
        for m in [-3,0,3]: assert nint(t+m)==nint(t)+m

r=[F(1),F(2,3),F(1,2)];t=[F(1),F(1,3),F(1,4)]
synthetic={'R':ledger(r,2),'T':ledger(t,3),
 'R_perturbed':ledger([r[0],r[1]+F(1,1000),r[2]],2),
 'T_perturbed':ledger([t[0],t[1]+F(1,10000),t[2]],3)}
assert [x['Q'] for x in synthetic['R']]==[[1,1,0],[27,18,13],[729,486,364]]
assert [x['Q'] for x in synthetic['T']]==[[1,0,0],[27,9,7],[729,243,182],[19683,6561,4921]]
for name,depth in [('R',2),('T',3)]:
    first=next(g for g,(a,b) in enumerate(zip(synthetic[name],synthetic[name+'_perturbed'])) if a['Q']!=b['Q'])
    assert first==depth

m06=loaded['S02']['backbone_sequence'][5]
active=[F(x) for x in m06['active_ray']]
active_rows=ledger(active,8)
reported=m06['locked_replay']
active_discrepancies=[dict(g=a['g'],fresh=a['Q'],reported=b['Q']) for a,b in zip(active_rows,reported) if a['Q']!=b['Q']]
rays=loaded['S01']['backbone_sequence'][4]['projective_rays']
hist={name:ledger([F(x) for x in ray],8) for name,ray in rays.items()}
differences=[]
for a,b in zip(hist['master_geometry'],hist['locked_mass_bridge']):
    differences.append(dict(g=a['g'],Q_master_minus_locked=[x-y for x,y in zip(a['Q'],b['Q'])],epsilon_master_minus_locked=[str(F(x)-F(y)) for x,y in zip(a['epsilon'],b['epsilon'])]))
assert all(d['Q_master_minus_locked']==[0,0,0] for d in differences[:8])
assert differences[8]['Q_master_minus_locked']==[0,8,7]
dump('worked-example-verification.json',dict(status='passed',runtime=sys.executable,arithmetic='fractions.Fraction; finite decimal tokens parsed as exact rational values',source_hashes=sources,synthetic=synthetic,active_source=dict(pointer='S02#/backbone_sequence/5/active_ray',rows=active_rows,reported_Q_discrepancies=active_discrepancies),historical=dict(pointer='S01#/backbone_sequence/4/projective_rays',rows=hist,differences=differences),checks=['12030 signed rational rounding cases against independent nearest-neighbor rule','integer translation for shifts -3,0,3 in every rounding case','every row residual interval and exact reconstruction','every carry by integer and residual routes','side-mode inverse and parity','backward residual recovery','finite carry-sum decoder','synthetic first split generations','historical equality g0..7 and difference (0,8,7) at g8']))
print(json.dumps(dict(status='passed',active_discrepancies=active_discrepancies,historical_g8=differences[8]['Q_master_minus_locked'])))
