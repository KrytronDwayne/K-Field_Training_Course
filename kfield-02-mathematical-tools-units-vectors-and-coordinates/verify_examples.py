"""Exact checks of small synthetic teaching examples; no source-data copying."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
checks=[]
def enc(x):
    if isinstance(x,(tuple,list)): return [enc(y) for y in x]
    if isinstance(x,F): return str(x)
    return x
def check(name, actual, expected):
    assert actual==expected, (name, actual, expected)
    checks.append({'id':name,'status':'passed','actual':enc(actual),'expected':enc(expected)})
def v(x,y): return (F(x),F(y))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(s,x): return tuple(s*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(B,x): return tuple(dot(row,x) for row in B)
def det(B): return B[0][0]*B[1][1]-B[0][1]*B[1][0]
def inv(B):
    a,b=B[0]; c,d=B[1]; D=det(B)
    if D==0: raise ValueError('Singular basis')
    return ((F(d)/D,-F(b)/D),(-F(c)/D,F(a)/D))
def project(x,d):
    dd=dot(d,d)
    if dd==0: raise ValueError('Zero direction')
    p=scale(dot(x,d)/dd,d)
    return p,sub(x,p)
def round_tenth(x):
    # Exact ties-away rule; Python round would use a different tie rule.
    t=abs(F(x))*10
    n=(t+F(1,2)).numerator//(t+F(1,2)).denominator
    return F(n,10) if x>=0 else -F(n,10)

check('runtime',sys.executable.lower(),r'c:\users\info\.conda\envs\tf_gpu_env\python.exe')
for name,a,b in [
 ('L01.length',F(36,1000),F('0.036')),('L01.period',F(4,1000),F('0.004')),
 ('L01.frequency',1/F('0.004'),250),('L01.khz',F(250,1000),F('0.25')),
 ('L01.guided_cm',F('7.5')/100,F('.075')),('L01.minutes',2*60,120),
 ('L01.D1m',F('.003')*1000,3),('L01.D1mm',3*1000,3000),
 ('L01.D2',F('.00072')*1000,F('.72')),('L01.D3',1/F('.02'),50),
 ('L01.D4',F(1,2),F('.5')),
 ('L02.area',6*9,3**2*(2*3)),('L02.volume',6*9*12,3**3*(2*3*4)),
 ('L02.m3',F('.02')*F('.03')*F('.04'),F('.000024')),
 ('L02.guided_area',5**2,F(1,4)*10**2),('L02.guided_cm2',25*F('.1')**2,F('.25')),
 ('L02.D1', (4,4**2,4**3),(4,16,64)),('L02.D2area',9*F('.01')**2,F('.0009')),
 ('L02.D2volume',9*F('.01')**3,F('.000009')),('L02.D3',6*4,24),
 ('L02.D4',6*F(500,2)/100,15)]: check(name,a,b)

O=v(10,-2); P=v(13,2); Q=v(16,6); w=v(3,4)
check('L03.position',sub(P,O),w);check('L03.displacement',sub(Q,P),w)
check('L03.reconstructP',add(O,w),P);check('L03.reconstructQ',add(P,w),Q)
check('L03.magnitude_squared',dot(w,w),25)
check('L03.unit_squared',dot(scale(F(1,5),w),scale(F(1,5),w)),1)
check('L03.origin_change',sub(sub(Q,v(11,0)),sub(P,v(11,0))),w)
check('L03.double_length_squared',dot(scale(2,w),scale(2,w)),100)
check('L03.guided',sub(v(2,-2),v(-1,2)),v(3,-4))
check('L03.D1',sub(v(-1,7),v(2,3)),v(-3,4))
check('L03.D2',scale(F(1,6),v(0,-6)),v(0,-1))
check('L03.D3P',sub(v(1,2),v(5,-1)),v(-4,3))
check('L03.D3Q',sub(v(4,6),v(5,-1)),v(-1,7))
check('L03.D4',scale(-2,v(3,4)),v(-6,-8))

for name,x,d,p,r in [
 ('L04.worked',v(4,3),v(2,0),v(4,0),v(0,3)),
 ('L04.guided',v(5,0),v(3,4),v(F(9,5),F(12,5)),v(F(16,5),F(-12,5))),
 ('L04.D2',v(-2,5),v(0,3),v(0,5),v(-2,0)),
 ('L04.D3',v(3,4),v(3,4),v(3,4),v(0,0)),
 ('L04.D4',v(-4,0),v(1,0),v(-4,0),v(0,0)),
 ('Teacher.unit2',v(2,3),v(0,2),v(0,3),v(2,0))]:
    pp,rr=project(x,d)
    check(name+'.projection',pp,p);check(name+'.residual',rr,r)
    check(name+'.reconstruction',add(pp,rr),x);check(name+'.perpendicular',dot(rr,d),0)
check('L04.D1',scale(10,v(F(4,5),F(3,5))),v(8,6))
try: project(v(1,2),v(0,0))
except ValueError: check('zero_direction_rejected',True,True)
else: raise AssertionError('Zero projection was accepted')

B=((2,1),(0,1)); C=((1,2),(2,0))
for name,M,q,x in [
 ('L05.worked',B,v(3,-2),v(4,-2)),('L05.guided',B,v(-1,3),v(1,3)),
 ('L05.D1',B,v(2,1),v(5,1)),('L05.D2',B,v(2,3),v(7,3)),
 ('L05.D3',B,v(F(1,2),2),v(3,2)),('L06.worked',C,v(2,-1),v(0,4)),
 ('L06.D3',C,v(2,2),v(6,4))]:
    check(name+'.forward',mv(M,q),x); check(name+'.inverse',mv(inv(M),x),q)
check('L05.swapped',mv(((1,2),(1,0)),v(-2,3)),v(4,-2))
check('L06.D',det(C),-4);check('L06.D1',det(B),2)
check('L06.D2swapped',det(((2,1),(0,2))),4)
for name,S,q1,q2 in [('L06.singular',((1,2),(2,4)),v(2,0),v(0,1)),('L06.D4',((1,3),(2,6)),v(3,0),v(0,1))]:
    check(name+'.D',det(S),0); check(name+'.collision',mv(S,q1),mv(S,q2))
    try: inv(S)
    except ValueError: check(name+'.rejected',True,True)
    else: raise AssertionError('Singular inverse accepted')

O=v(10,-1); q=v(F(5,4),F(-3,4)); x=mv(C,q); P=add(O,x)
check('L07.worked_x',x,v(F(-1,4),F(5,2)))
check('L07.worked_P',P,v(F(39,4),F(3,2)))
check('L07.worked_reverse',mv(inv(C),sub(P,O)),q)
qh=tuple(round_tenth(z) for z in q);e=sub(q,qh)
check('L07.display',qh,v('1.3','-0.8'));check('L07.residual',e,v('-.05','.05'))
check('L07.Be',mv(C,e),v('.05','-.1'))
check('L07.restore',add(add(O,mv(C,qh)),mv(C,e)),P)
qg=mv(inv(C),sub(v(11,2),O)); qgh=tuple(round_tenth(z) for z in qg)
check('L07.guided_q',qg,v('1.5','-.25'));check('L07.guided_display',qgh,v('1.5','-.3'))
check('L07.guided_residual_image',mv(C,sub(qg,qgh)),v('.1',0))
for t,display,residual in [('2.25','2.3','-.05'),('-2.25','-2.3','.05'),('2.24','2.2','.04')]:
    check('L07.tie_'+t,round_tenth(F(t)),F(display))
    check('L07.e_'+t,F(t)-round_tenth(F(t)),F(residual))
check('L07.D3',mv(inv(C),sub(v(12,3),O)),v(2,0))

B=((2,1),(1,-1));O=v(100,-20);q=v(F(5,4),F(-3,4));x=mv(B,q);P=add(O,x)
check('capstone.origin_m',scale(F(1,100),O),v(1,'-.2'))
check('capstone.period',F(25,1000),F('.025'));check('capstone.frequency',1/F('.025'),40)
check('capstone.x',x,v(F(7,4),2));check('capstone.mag_squared',dot(x,x),F(113,16))
check('capstone.P',P,v('101.75',-18));check('capstone.Pm',scale(F(1,100),P),v('1.0175','-.18'))
check('capstone.D',det(B),-3);check('capstone.Dm',F(det(B),10000),F('-.0003'))
check('capstone.inverse',inv(B),((F(1,3),F(1,3)),(F(1,3),F(-2,3))))
check('capstone.reverse',mv(inv(B),sub(P,O)),q)
check('capstone.forward_restore',add(O,mv(B,mv(inv(B),sub(P,O)))),P)
check('capstone.test2',mv(inv(B),sub(v(103,-20),O)),v(1,1))
p,r=project(x,v(2,0))
check('capstone.projection',p,v(F(7,4),0));check('capstone.residual',r,v(0,2))
check('capstone.project_restore',add(p,r),x);check('capstone.orthogonal',dot(r,v(2,0)),0)
# Exact symbolic ratio checks: squares of 7/sqrt(113), 8/sqrt(113).
check('capstone.trig_unit',F(49,113)+F(64,113),1)
check('capstone.cos_component_squared',F(113,16)*F(49,113),F(49,16))
check('capstone.sin_component_squared',F(113,16)*F(64,113),4)
qh=tuple(round_tenth(z) for z in q);e=sub(q,qh)
check('capstone.qhat',qh,v('1.3','-.8'));check('capstone.e',e,v('-.05','.05'))
check('capstone.Be',mv(B,e),v('-.05','-.1'))
check('capstone.Phat',add(O,mv(B,qh)),v('101.8','-17.9'))
check('capstone.restore',add(add(O,mv(B,qh)),mv(B,e)),P)
check('capstone.coefficients_restore',add(qh,e),q)
check('capstone.rubric_total',sum((8,4,6,8,6,8)),40)
check('teacher.pacing',7*55+2*55,495)
check('teacher.unit1area',F(3,100)**2,F('.0009'))

# Additional exact round-trip tests exercise all signs and both directions.
for M in [((2,1),(0,1)),((1,2),(2,0)),((2,1),(1,-1))]:
    for a in [F(-3,2),F(0),F(5,4)]:
        for b in [F(-3,4),F(0),F(7,3)]:
            x=v(a,b);y=mv(M,x)
            assert mv(inv(M),y)==x
            assert mv(M,mv(inv(M),x))==x
check('property_roundtrips_27_both_directions',True,True)
for i in range(-100,101):
    z=F(i,40);h=round_tenth(z);e=z-h
    assert abs(e)<=F(1,20) and h+e==z
check('rounding_201_exact_values_and_endpoints',True,True)

inputs=[f'lesson-{i:02d}.md' for i in range(1,8)]+['capstone.md','teacher-guide.md']
report={'schema_version':'1.0','status':'passed','runtime':sys.executable,'check_count':len(checks),'checks':checks,'checked_artifact_hashes':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in inputs},'verification_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Small synthetic exact-arithmetic and reconstruction checks plus manual independent audit. No measurement datasets or archival proof validation. Symbolic square-root checks use known positive signs.'}
(ROOT/'worked-example-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} checks, 27 bidirectional matrix cases, 201 exact rounding cases.')
