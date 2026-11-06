from pathlib import Path
import math,json,sys,hashlib
R=Path(__file__).parent
records=[]
def test(name,actual,expected,tol=1e-9):
    if isinstance(actual,(list,tuple)): ok=all(abs(a-b)<=tol for a,b in zip(actual,expected)) and len(actual)==len(expected)
    else: ok=abs(actual-expected)<=tol
    records.append(dict(id=name,actual=actual,expected=expected,absolute_tolerance=tol,passed=ok))
    assert ok,name
def add(*vs):return [sum(xs) for xs in zip(*vs)]
def scale(v,k):return [k*x for x in v]
def turn(v):return [-v[1],v[0],v[2]]
test('L1-W',add(turn([2,1,0]),[5,3,1]),[4,5,1])
test('L1-inverse',[5-3,-(4-5),1-1],[2,1,0])
test('L1-P1',add([1,2,3],scale([2,-1,0],2)),[5,0,3])
test('L1-P2',add([1,2,3],scale([2,-1,0],4)),[9,-2,3])
test('L1-reverse',add([9,-2,3],scale([2,-1,0],-4)),[1,2,3])
test('L1-D2',add(turn([0,2,1]),[5,3,1]),[3,3,2])
test('L1-D4',add([1,2,3],scale([2,-1,0],6)),[13,-4,3])
a,d=math.pi/2,math.pi/6
test('L2-W',[2*math.cos(d)*math.cos(a),2*math.cos(d)*math.sin(a),2*math.sin(d)],[0,math.sqrt(3),1])
test('L2-norm',math.sqrt(3+1),2)
test('L2-local',add([0,0,1],[1,0,0]),[1,0,1])
test('L2-D3',add(scale([0,1,0],2),scale([0,0,1],-1)),[0,2,-1])
terms=[[10,0,0],[0,2,0],[-1,0,0],[0,0,1]]
test('L3-total',add(*terms),[9,2,1])
test('L3-endpoint',add([1,2,3],*[scale(v,2) for v in terms]),[19,6,5])
test('L3-reversed',add([1,2,3],scale([11,2,1],2)),[23,6,5])
test('L7-reconstruction',add([19,6,5],*[scale(v,-2) for v in terms]),[1,2,3])
test('L4-v0',[1-math.sin(0),math.cos(0),0],[1,1,0])
test('L4-cancel',[1-math.sin(math.pi/2),math.cos(math.pi/2),0],[0,0,0])
test('L4-a0',[-math.cos(0),-math.sin(0),0],[-1,0,0])
test('L4-aquarter',[-math.cos(math.pi/2),-math.sin(math.pi/2),0],[0,-1,0])
# Independent central finite difference check of the declared position rule.
def p(t):return [t+math.cos(t),math.sin(t),0]
eps=1e-5
test('L4-independent-finite-difference',scale(add(p(0+eps),scale(p(0-eps),-1)),1/(2*eps)),[1,1,0],1e-8)
test('L4-residual',add([1.2,.9,0],[-1,-1,0]),[.2,-.1,0])
test('L5-node',turn([1,1,0]),[-1,1,0])
test('L5-half',turn(turn([1,1,0])),[-1,-1,0])
test('L5-directed',math.degrees(math.acos(-1)),180)
test('L5-axis',math.degrees(math.acos(abs(-1))),0)
test('L6-A',2*1000,2000); test('L6-B',2*1,2)
src=Path('Z:/Archive_20260911/Pre_Aug14/K-Field_linear_inertia_derivation_1784989727.json')
assert hashlib.sha256(src.read_bytes()).hexdigest()=='4651a532fe43e8091748ef4f7e28bb899e1a2ea798d689ba1724e99530cd55ab'
q=json.loads(src.read_text())['derived_results']['earth_cmb']
test('physical-source-norm',math.sqrt(sum(x*x for x in q['V_E_icrs_m_s'])),q['speed_m_s'],1e-6)
payload=dict(status='passed',python=sys.executable,scope='Synthetic example arithmetic, inverse operations, finite derivative check and read-only physical source norm. No formal compilation or observational replay.',checks=records)
(R/'worked-example-verification.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',checks=len(records),python=sys.executable)))
