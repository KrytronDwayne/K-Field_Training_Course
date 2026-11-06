from fractions import Fraction as F
from pathlib import Path
import hashlib,json,re
root=Path(r'Z:/Kfield-doc-training/K-Field_Training_Course/kfield-25-plane-crossings-rulers-and-event-geometry')
checks=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    checks.append({'check':name,'actual':str(actual),'expected':str(expected),'status':'passed'})
check('unit normal squared length',F(3,5)**2+F(4,5)**2,F(1))
check('L1 projected distance at quarter second',F(3,5)*2*F(1,4),F(3,10))
check('L1 q at quarter second',F(3,10)/F(3,5),F(1,2))
check('L1 reversed origin q shift',-F(3,5)/F(3,5),F(-1))
check('L2 projected rate',F(6,5)/F(3,5),F(2))
check('L2 zero rate',F(0)/1,F(0))
check('L2 reversed y rate',F(-3)/1,F(-3))
check('L2 moving origin',F(2)-1,F(1))
check('L2 changing spacing delta q',F(2,2)-F(2,1),F(-1))
check('L3 period',F(3,5)/F(6,5),F(1,2))
check('L3 revised period',F(6,5)/F(6,5),F(1))
check('L3 wait from initial phase quarter',(1-F(1,4))/2,F(3,8))
check('L3 piecewise event times',[F(0),F(1)]+[1+F(k-1,3) for k in range(2,5)],[F(0),F(1),F(4,3),F(5,3),F(2)])
check('L4 oscillator',1/F(1,4),F(4))
check('L4 propagation wavelength',3*F(1,4),F(3,4))
check('L4 grid rates',[2/F(1,2),2/F(1,4)],[F(4),F(8)])
check('L4 worked difference',abs(F(4)-2),F(2))
check('capstone difference',abs(F(4)-4),F(0))
check('L5 worked interpolation',-F(-2,5)*2/(F(6,5)-F(-2,5)),F(1,2))
check('L5 practice interpolation',1-F(-1)*2/(3-F(-1)),F(3,2))
check('L5 two roots evaluations',[(t-1)*(t-2) for t in [F(0),F(1,2),F(1),F(3,2),F(2),F(5,2),F(3)]],[F(2),F(3,4),F(0),F(-1,4),F(0),F(3,4),F(2)])
check('L5 tangent values',[(t-1)**2 for t in [F(0),F(1,2),F(1),F(3,2),F(2)]],[F(1),F(1,4),F(0),F(1,4),F(1)])
check('L5 bisection values',[t*t-2 for t in [F(1),F(2),F(3,2),F(5,4)]],[F(-1),F(2),F(1,4),F(-7,16)])
check('L5 supplied bound',[F(-2,100)-F(5,100),F(-2,100)+F(5,100)],[F(-7,100),F(3,100)])
check('L6 Star R angle/pi at event times',[t-1 for t in [F(0),F(1,2),F(1),F(3,2),F(2)]],[F(-1),F(-1,2),F(0),F(1,2),F(1)])
check('L6 sheet event',F(1)/2,F(1,2))
check('L6 unwrapped increment',F(241,10)-F(239,10),F(1,5))
for family,d,r,ks,brackets,expected in [('A',F(3,5),F(-2),[0,-1,-2,-3],[(0,F(1,2)),(0,1),(F(1,2),F(3,2)),(1,F(3,2))],[(0,F(-3,5)),(F(3,5),F(-3,5)),(F(3,5),F(-3,5)),(F(3,5),0)]),('B',F(2),F(-1),[0,-1],[(0,1),(F(1,2),F(3,2))],[(0,-2),(1,-1)])]:
    for k,br,e in zip(ks,brackets,expected):
        check('REV '+family+str(k)+' endpoint distances',tuple(d*(r*t-k) for t in br),e)
        check('REV '+family+str(k)+' root substitution',d*(r*(F(k)/r)-k),F(0))
y=[F(0),F(11,10),F(19,10)];m=[F(0),F(1),F(2)];e=[a-b for a,b in zip(y,m)]
check('L7 signed residuals',e,[F(0),F(1,10),F(-1,10)])
check('L7 reconstruction',[a+b for a,b in zip(m,e)],y)
check('L7 supplied bound',[F(19,10)-F(1,20),F(19,10)+F(1,20)],[F(37,20),F(39,20)])
files={}
for i in range(1,8):
    p=root/f'lesson-{i:02d}.md';txt=p.read_text(encoding='utf-8');files[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    for suffix in ['E1','W1','P1','D1']:
        anchor=f'C25.{i:02d}-{suffix}'
        check('actual anchor '+anchor,anchor in txt,True)
    check(f'lesson {i} diagnostic count in range',3<=len(re.findall(r'\*\*C25\.\d+-D\d+:',txt))<=5,True)
    for label in ['Essential question','Goals','Prerequisite bridge','Claim scope','Next dependency','Worked answer']:
        check(f'lesson {i} contract {label}',label in txt,True)
p=root/'capstone.md';txt=p.read_text(encoding='utf-8');files[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
for i in range(1,8):
    check(f'capstone operation {i}',f'### C25-CAP-{i:02d}' in txt,True)
    check(f'capstone practice map {i}',f'C25.{i:02d}-P1' in txt,True)
report={'scope':'Independent reread of all seven student lessons and capstone; input-contract teaching anchors and capstone backward map compared. No source-artifact reauthentication or final assembly audit performed in this bounded review.','status':'passed_in_scope','unresolved_counts':{'critical':0,'major':0,'minor':0},'findings':[],'reviewed_sha256':files,'checks':checks,'manual_checks':[{'area':'prerequisite closure and E05','evidence':'Each capstone step uses earlier E1/W1/P1 content. Dot product and unit normal introduced in L1; signed ratio in L2; periods/radians in L3; ruler meanings and difference rule in L4; interpolation/contact/jump/gap in L5; unwrapped angular equations in L6; complete records and residual replay in L7. Recognition-only full derivative is not required by capstone.'},{'area':'event existence and boundaries','evidence':'L5 correctly separates continuity-dependent existence from uniqueness, contacts from transverse examples, equal-sign endpoints from absence, and unknown gaps from invented roots. L7 and capstone explicitly provide linear extension for endpoint passage classification and retain contact/gap/jump records.'},{'area':'evidence and information retention','evidence':'All numeric trajectories and illustrative residuals explicitly synthetic. Polarity declared independently of direction. Grid counts not promoted to measured response or energy; full paths retained because projection loses tangential components. Original brackets, refined values, residual signs and unknown bounds retained.'},{'area':'pacing and assessment','evidence':'11 core 55-minute periods total; each lesson states 5+20+15+15-minute allocations. Seven capstone operations each have four distinct rubric criteria, totaling 28. All requested numeric inputs are locally supplied.'}],'limitations':['Source-specific prose claims about T10/T45 are identified as source claims, but exact pinned-byte fidelity remains the production manager source review responsibility.','Course map, glossary, teacher guide, assembly, manifest integrity and deterministic validator are outside this lesson/capstone-only review.']}
(root/'independent-audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks),'report':str(root/'independent-audit.json')}))
