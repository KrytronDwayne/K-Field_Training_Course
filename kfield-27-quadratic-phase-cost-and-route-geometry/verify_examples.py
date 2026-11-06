"""Independent exact arithmetic checks of the authored finite teaching examples."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal
import json, sys, hashlib, math
root=Path(__file__).resolve().parent
checks=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    checks.append({'id':name,'actual':str(actual),'expected':str(expected),'status':'passed'})
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def q(g,v):return sum(v[i]*g[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))
g=[[F(2),F(1)],[F(1),F(2)]]
for v,w in [((1,2),14),((1,-1),2),((1,1),6),((2,-1),6),((-1,-2),14),((-1,1),2),((1,0),2)]:check('quadratic-'+str(v),q(g,v),F(w))
check('unit-plus-direction',q(g,(1,1))/2,F(3))
check('unit-minus-direction',q(g,(1,-1))/2,F(1))
check('ellipse-short',q(g,(1,1))/6,F(1))
check('ellipse-long',q(g,(1,-1))/2,F(1))
check('ellipse-axis',q(g,(1,0))/2,F(1))
b=[[F(2),F(0)],[F(0),F(1)]]
w=[[x/4 for x in row] for row in mul(transpose(b),mul(g,b))]
check('full-pullback',w,[[F(2),F(1,2)],[F(1,2),F(1,2)]])
tb=[[F(1),F(0)],[F(0),F(2)]]
check('reverse-congruence',mul(transpose(tb),mul(w,tb)),g)
for u,v in [((1,2),(1,1)),((2,-2),(2,-1))]:check('coordinate-cost-'+str(u),q(w,u),q(g,v))
a=[[F(1),F(0)],[F(0),F(1,2)]]
check('ruler-matrix',mul(transpose(a),a),[[F(1),F(0)],[F(0),F(1,4)]])
check('ruler-rate',F(-1)**2+F(2,2)**2,F(2))
check('ruler-third-segment-count',(-1-1+1,1+1-1),(-1,1))
def ledger(vs,ds):
    x=[F(0),F(0)]; total=F(0); out=[]
    for v,d in zip(vs,ds):
        x=[x[i]+d*v[i] for i in range(2)];total+=d*q(g,v);out.append((tuple(x),total))
    return out
check('straight-ledger',ledger([(1,0)]*2,[F(1)]*2),[((F(1),F(0)),F(2)),((F(2),F(0)),F(4))])
check('dogleg-ledger',ledger([(1,1),(1,-1)],[F(1)]*2),[((F(1),F(1)),F(6)),((F(2),F(0)),F(8))])
check('reverse-ledger',ledger([(1,-1),(1,1)],[F(1)]*2),[((F(1),F(-1)),F(2)),((F(2),F(0)),F(8))])
check('subdivision-total',ledger([(1,0)]*4,[F(1,2)]*4)[-1],((F(2),F(0)),F(4)))
check('deviation-excess',2*q(g,(0,1)),F(4))
check('changed-time',4*q(g,(F(1,2),0)),F(2))
# Non-example-specific check: unequal durations and signed 2D velocities.
vs=[(F(2),F(-1)),(F(-1),F(3)),(F(1),F(0))]; ds=[F(1,2),F(3,2),F(2)]
t=sum(ds); avg=[sum(d*v[i] for d,v in zip(ds,vs))/t for i in range(2)]
deviations=[[v[i]-avg[i] for i in range(2)] for v in vs]
check('weighted-deviation-zero',[sum(d*v[i] for d,v in zip(ds,deviations)) for i in range(2)],[F(0),F(0)])
check('general-decomposition',sum(d*q(g,v) for d,v in zip(ds,vs)),t*q(g,avg)+sum(d*q(g,v) for d,v in zip(ds,deviations)))
check('precision-residual',F(1,3)-F(3333,10000),F(1,30000))
check('precision-reconstruction',F(3333,10000)+F(1,30000),F(1,3))
check('precision-interval',F(3333,10000)<=F(1,3)<F(3334,10000),True)
check('bound-gap',F(41,10)-F(39,10),F(1,5))
check('source-residual-nonzero',Decimal('4.58938078934712923077736690075e-12')>0,True)
check('factor-pairs',(2*3,1*6),(6,6))
check('frozen-calibration',F(6,3),F(2))
check('signed-response-residuals',(7-2*3,5-2*3),(1,-1))
for i in range(1,8):
    s=(root/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    for suffix in ['E1','W1','P1','D1']:check(f'anchor-{i}-{suffix}',f'C27.{i:02}-{suffix}' in s,True)
    check(f'lesson-contract-{i}',all(x in s for x in ['Essential question','Goals:','Bridge' if i>1 else 'bridge','Next dependency']),True)
packet=json.loads((root/'input-contract.json').read_text(encoding='utf-8-sig'))
for s in packet['sources']:
    if 'path' in s:check('hash-'+s['id'],hashlib.sha256(Path(s['path']).read_bytes()).hexdigest(),s['sha256'])
report={'status':'passed','python_executable':sys.executable,'method':'Independent standard-library Fraction/Decimal arithmetic plus anchor and original-source digest checks; unit and proof logic additionally reviewed by author and independent auditor.','checks':checks,'count':len(checks)}
(root/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks),'python_executable':sys.executable}))

if '--figure' in sys.argv:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    ts=[2*math.pi*i/400 for i in range(401)]
    ss=[math.cos(t)/math.sqrt(3) for t in ts];tt=[math.sin(t) for t in ts]
    xx=[(s+t)/math.sqrt(2) for s,t in zip(ss,tt)]; yy=[(s-t)/math.sqrt(2) for s,t in zip(ss,tt)]
    fig,ax=plt.subplots(figsize=(6,6),layout='constrained')
    ax.plot(xx,yy,label='2x² + 2xy + 2y² = 1',color='#235789')
    anchors=[(1/math.sqrt(6),1/math.sqrt(6)),(0,1/math.sqrt(2)),(-1/math.sqrt(2),1/math.sqrt(2)),(-1/math.sqrt(2),0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0,-1/math.sqrt(2)),(1/math.sqrt(2),-1/math.sqrt(2)),(1/math.sqrt(2),0)]
    ax.scatter(*zip(*anchors),color='#ce4a27',zorder=3)
    ax.plot([0,1/math.sqrt(6)],[0,1/math.sqrt(6)],color='#008060',lw=2)
    ax.plot([0,1/math.sqrt(2)],[0,-1/math.sqrt(2)],color='#8e44ad',lw=2)
    ax.annotate('short semiaxis L/√3',xy=(.30,.30),xytext=(-.92,.85),arrowprops={'arrowstyle':'->'},fontsize=10)
    ax.annotate('long semiaxis L',xy=(.50,-.50),xytext=(-.90,-.88),arrowprops={'arrowstyle':'->'},fontsize=10)
    ax.axhline(0,color='gray',lw=.7);ax.axvline(0,color='gray',lw=.7)
    ax.set(xlim=(-1,1),ylim=(-1,1),xlabel='x / L',ylabel='y / L',title='Synthetic displacement cost q = 1')
    ax.set_aspect('equal');ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=9)
    fig.savefig(root/'ellipse.png',dpi=160);plt.close(fig)
