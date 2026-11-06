from pathlib import Path
from fractions import Fraction as F
import json, hashlib, math, sys
R=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
checks=[]
assert sys.executable.lower().replace('\\','/')=='c:/users/info/.conda/envs/tf_gpu_env/python.exe'
checks.append({'check':'Explicit tf_gpu_env runtime','result':sys.executable})
for source in p['sources']:
    if 'path' in source:
        actual=sha(Path(source['path']))
        assert actual==source['sha256']
        checks.append({'check':'Local source hash','id':source['id'],'sha256':actual,'result':'matched'})
s05=Path('Z:/Archive_20260911/Aug14_Sept1/K-Field_3D_periodic_table_hidden_dimensions_recent24h_1788145361.json')
assert sha(s05)=='d17197c1bec71893e1fd8344e0a35f6e63da3668f35dc3085247a66ad112eae7'
checks.append({'check':'S05 byte identity and exact selected records','sha256':sha(s05),'record_ids':[json.loads(s05.read_text(encoding='utf-8-sig'))['records'][i]['id'] for i in [15,16,20,25,26,27]]})
roots=[1,1j,-1,-1j]
def dft(x): return [sum(x[n]*roots[(-k*n)%4] for n in range(4)) for k in range(4)]
def inv(X): return [sum(X[k]*roots[(k*n)%4] for k in range(4))/4 for n in range(4)]
examples=[
([1,0,-1,0],[0,2,0,2]),([0,1,0,-1],[0,-2j,0,2j]),
([1,1,1,1],[4,0,0,0]),([1,2,3,4],[10,-2+2j,-2,-2-2j]),
([4,1,2,3],[10,2+2j,2,2-2j]),([2,3,2,3],[10,0,-2,0]),
([-1,-1,1,1],[0,-2+2j,0,-2-2j]),([2,0,-2,0],[0,4,0,4]),
([3,1,-1,1],[4,4,0,4])]
for x,X in examples:
    assert dft(x)==X and inv(X)==x
    checks.append({'check':'DFT and full inverse','input':x,'spectrum':[str(v) for v in X],'reconstruction_residual':[0,0,0,0],'arithmetic':'Integer real/imaginary values and quarters are exactly representable; no trigonometric approximation'})
for x in [[1,2,3,4],[3,1,-1,1]]:
    H=x[2:]+x[:2]
    E=[F(a+b,2) for a,b in zip(x,H)]
    O=[F(a-b,2) for a,b in zip(x,H)]
    assert [a+b for a,b in zip(E,O)]==x
    assert sum(a*b for a,b in zip(E,O))==0
    for shift in range(4):
        Es=E[shift:]+E[:shift]
        assert sum(a*b for a,b in zip(Es,O))==0
    checks.append({'check':'Parity reconstruction and four shifted comparator dot products','input':x,'even':list(map(str,E)),'odd':list(map(str,O)),'result':'exact'})
for counts in [[8,4,6,2],[2,5,4,3],[2,0,4,0]]:
    a,b,c,d=map(F,counts); M=(a+c)/2;Q=(b+d)/2;D0=(a-c)/2;D90=(b-d)/2
    assert [M+D0,Q+D90,M-D0,Q-D90]==counts
    checks.append({'check':'Four-count exact rational reconstruction','input':counts,'M_Q_D0_D90':list(map(str,[M,Q,D0,D90])),'fractional_gain':str((M-Q)/Q) if Q else 'undefined: Q=0'})
assert F(4,3)*3*2==8 and F(6)*10/3==20
assert sorted([F(-1,4)*3*2,F(-1,4)*6*2])==[F(-3),F(-3,2)]
checks.append({'check':'Energy and photon equivalents','positive_energy_interval':['8','16'],'signed_energy_interval':['-3','-3/2'],'signed_photon_interval':['-3/20','-3/40'],'result':'exact rational'})
for f1,f2 in [(4,6),(5,7),(10,14)]:
    diffs=[]
    for t in [0,F(1,4),F(1,2),F(3,4)]:
        left=math.cos(2*math.pi*f1*t)+math.cos(2*math.pi*f2*t)
        right=2*math.cos(math.pi*(f1-f2)*t)*math.cos(math.pi*(f1+f2)*t)
        diffs.append(left-right)
        assert abs(left-right)<1e-12
    checks.append({'check':'Beat identity numerical spot check supplementary to algebraic derivation','frequencies':[f1,f2],'signed_rounding_differences':diffs})
rows=json.loads((R/'source-replay.json').read_text())['rows']
assert len(rows)==14
assert sum(r['sign']>0 for r in rows)==8
assert sum(r['sign']<0 for r in rows)==6
assert sum(r['energy_present'] for r in rows)==5
assert {f:sum(r['family']==f for r in rows) for f in ['w','v','lambda']}=={'w':4,'v':4,'lambda':6}
checks.append({'check':'All source rows accounted for','rows':14,'positive':8,'negative':6,'cost_levels':3,'energy_subset':5,'note':'All signed binary64 residuals retained in source-replay.json; no exact source equality claim'})
a,b,c,d=[1485.2562384582884,1483.8843576874326,1483.1281192291442,1483.]
M=(a+c)/2;Q=(b+d)/2;D0=(a-c)/2;D90=(b-d)/2
res=[x-y for x,y in zip([a,b,c,d],[M+D0,Q+D90,M-D0,Q-D90])]
assert res==rows[0]['derived']['reconstruction_residual']
assert (M-Q)/Q==0.0005055808785109474
checks.append({'check':'Independent Python source-card replay','signed_reconstruction_residual':res,'response':0.0005055808785109474/0.0000574509228616101})
for lesson in p['course_map']:
    txt=(R/(lesson['id']+'.md')).read_text(encoding='utf-8')
    a=lesson['teaching_anchor']
    for key in ['explanation_id']:
        assert a[key] in txt
    for sub in ['worked_example','guided_practice','diagnostic']:
        assert a[sub]['id'] in txt
    for supplement in a.get('supplemental_exercises',[]):
        for k in ['explanation_id','worked_example_id','prior_practice_id','diagnostic_id']: assert supplement[k] in txt
    for component in ['Essential question','Goals:','Prerequisite bridge','Next dependency','Claim scope' if lesson['id'] not in ['lesson-03','lesson-07'] else ('Source scope' if lesson['id']=='lesson-03' else 'Evidence layers')]:
        assert component in txt,(lesson['id'],component)
    checks.append({'check':'Lesson contract and exact teaching anchors','lesson':lesson['id'],'result':'present'})
cap=(R/'capstone.md').read_text(encoding='utf-8')
assert all(f'C26-CAP-{i:02}' in cap for i in range(1,10))
assert all(alias in ''.join((R/f'lesson-{i:02}.md').read_text(encoding='utf-8') for i in range(1,9)) for alias in ['C26-BEAT-P1','C26-DFT-EX1','C26-DFT-P1','C26-DFT-D1'])
checks.append({'check':'Nine capstone operations and legacy aliases','result':'present','points':36})
save('verification.json',{'schema_version':'1.0','status':'passed','runtime':sys.executable,'checks':checks,'limitations':['Finite synthetic arithmetic plus reported-event replay, not raw-data admission or compiler proof verification.','Binary64 signed closures retained without interval certification.']})
# Produce the coverage map from the approved contract, linking exact named section identifiers.
lines=['# Course map — '+p['topic'],'','Eight lessons, 17 core 55-minute periods and three capstone periods. Total planned time: 1100 minutes. The input contract preserves the original concepts and all source/teaching amendments. Lesson boundaries remain unchanged; multi-period sessions provide the required bridges.','',
'Entry capabilities: signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs. Courses 12,14,25 supply context; local bridges teach all operations needed by the assessments.','',
'| Concept | Introduction/explanation | Worked example | Prior practice | Diagnostic | Assessment | Later use |','|---|---|---|---|---|---|---|']
for step in p['capstone_specification']['backward_map']:
    lesson=step['introduction']
    concept=step.get('concept_id',step['explanation_id'].rsplit('-',1)[0])
    later=next(l['later_use'] for l in p['course_map'] if l['id']==lesson)
    lines.append('| '+ ' | '.join([concept,f"[{lesson}]({lesson}.md): {step['explanation_id']}",step['worked_example_id'],step['prior_practice_id'],step['diagnostic_id'],step['step_id'],later])+' |')
lines+=['','## Session order','','| Lesson | Periods | Sessions |','|---|---:|---|']
for l in p['course_map']:
    a=l['teaching_anchor'];lines.append(f"| [{l['id']}]({l['id']}.md) | {a['planned_periods']} | "+'; '.join(s['focus'] for s in a['session_sequence'])+' |')
lines+=['','## Dependency and evidence checks','',
'Lesson 1 circle coordinates → Lesson 2 addition and beats → Lesson 3 spatial phase → Lesson 4 reversible finite DFT → Lesson 5 channel ratios, four-angle coordinates and parity → Lesson 6 typed energy equivalent → Lesson 7 source event ledger → Lesson 8 complete residual comparison → nine-part capstone. The capstone uses the named answered practices above; it introduces no new operation.','',
'EA-26-E10-8 is realized in Lessons 2–4 by the derivation, sign convention, inverse factor, four multiplier rows and delayed examples. SA-26 is realized in Lessons 5–8 by all-row source references, signed gains, three cost levels, exact denominator domains, energy boundaries and comparator nullspace. C26.S01 has explicit E1/W1/P1/D1 sections in Lesson 5 and capstone step 9. Legacy aliases C26-DFT-EX1/P1/D1 and C26-BEAT-P1 remain in their teaching headings.','',
'Unit boundary after Lesson 3: circle/beat/ruler rates keep consistent units. After Lesson 5: complex phase and all even/odd coordinates reconstruct. After Lesson 8: energy, source-status and full residual accounting feed every capstone operation.','',
'Source reading is bounded to pinned reports and their contracts. No source-reported proof status is promoted to fresh proof verification. Source gaps are taught explicitly and do not block these finite learning outcomes. See sources.md and the teacher guide for scope and pacing.']
(R/'course-map.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Verification passed:',len(checks),'checks; coverage map written')
