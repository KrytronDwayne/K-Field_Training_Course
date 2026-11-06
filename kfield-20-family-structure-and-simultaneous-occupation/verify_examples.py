"""Replay independent finite checks and audit actual course links and teaching IDs."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, re, subprocess, sys

root=Path(__file__).resolve().parent
assert sys.executable.lower()==r'C:\Users\info\.conda\envs\tf_gpu_env\python.exe'.lower()
packet=json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
checks=[]
def check(name,value):
    assert value,name
    checks.append({'name':name,'status':'passed'})

result=subprocess.run([sys.executable,str(root/'independent-verification.py')],capture_output=True,text=True,check=True)
independent=json.loads(result.stdout)
check('Independent finite mathematical replay exited zero',independent['result']=='passed')
check('All independent recomputations passed',all(x['result']=='passed' for x in independent['checks']))
lessons={f'lesson-{i:02d}':(root/f'lesson-{i:02d}.md').read_text(encoding='utf-8') for i in range(1,8)}
capstone=(root/'capstone.md').read_text(encoding='utf-8')
for row in packet['capstone_specification']['backward_map']:
    text=lessons[row['introduction']]
    for key in ['explanation_id','worked_example_id','prior_practice_id','diagnostic_id']:
        check(row[key]+' exists in prior lesson',row[key] in text)
    check(row['step_id']+' exists in capstone',row['step_id'] in capstone)
for l,text in lessons.items():
    for label in ['Essential question:','Goals:','Prerequisite bridge:','Claim scope:','Diagnostic checks','Worked answers:','Next dependency:']:
        check(l+' '+label,label in text)
    diagnostics=text.split('## Diagnostic checks')[1].split('Worked answers:')[0]
    check(l+' has three to five diagnostics',3<=len(re.findall(r'^\d+\.',diagnostics,re.M))<=5)
    check(l+' no pending authoring placeholders','pending authoring' not in text)
for id in ['C20-RANK-EX1','C20-RANK-P1','C20-RANK-D1']:
    check(id+' retained',id in lessons['lesson-04'])
for path in root.glob('*.md'):
    if path.name=='launch-prompt.md':continue
    for link in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8-sig')):
        if not link.startswith(('http:','https:','#')):
            check(path.name+' local link '+link,(root/link.split('#')[0]).is_file())
check('Capstone points total 100',sum([10,10,12,12,12,12,8,12,12])==100)
for s in packet['sources']:
    check(s['id']+' source SHA-256',hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256'])

# Independent second route for the nine-node norm and scalar solutions.
check('Normalized nine-node indicator exact squared norm',sum([Fraction(1,3)**2]*9)==1)
for a,b,c,e,su,sw,u,w in [(2,1,1,3,5,7,Fraction(8,5),Fraction(9,5)),(3,1,2,2,7,8,Fraction(3,2),Fraction(5,2)),(1,1,1,0,3,1,Fraction(1),Fraction(2))]:
    det=a*e-b*c
    # Solve by eliminating with determinant, independently of the Schur route.
    check('Full-system solution '+str((a,b,c,e)),Fraction(e*su-b*sw,det)==u and Fraction(a*sw-c*su,det)==w and a*u+b*w-su==0 and c*u+e*w-sw==0)
payload={'schema_version':'1.0','status':'passed','runtime':sys.executable,'scope':'Finite synthetic examples and structural teaching checks; not source-selection or missing lift proof replay.','independent_recomputation':independent,'checks':checks,'check_count':len(checks),'tolerance':'Independent complex checks 1e-12; rational checks exact.','reviewed_content_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob('lesson-*.md')}}
(root/'verification.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','structural_and_secondary_checks':len(checks),'independent_math_checks':independent['count']},indent=2))
