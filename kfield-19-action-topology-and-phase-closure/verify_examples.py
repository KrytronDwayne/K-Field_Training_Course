"""Independent, exact finite recomputation; no source data copied."""
from fractions import Fraction as F
from functools import reduce
from operator import mul
from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parent
results=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    results.append({'id':name,'result':'passed','actual':str(actual),'expected':str(expected)})
def action(q,dt=F(1),k=F(2),vpot=F(2)):
    K=[k*(F(b)-F(a))**2/(2*dt) for a,b in zip(q,q[1:])]
    V=[dt*vpot*F(a)**2/2 for a in q[:-1]]
    return K,V,[x-y for x,y in zip(K,V)]
def prod(xs): return reduce(mul,xs,1)
check('runtime',str(Path(sys.executable)).lower(),r'C:\Users\info\.conda\envs\tf_gpu_env\python.exe'.lower())
for name,q,expected in [('W1',(0,1,3),([1,4],[0,1],[1,3])),('P1',(1,2,2),([1,0],[1,4],[0,-4])),('D2',(0,1,1),([1,0],[0,1],[1,-1]))]:
    K,V,a=action(q)
    check('action-'+name,(K,V,a),expected)
    check('independent-total-'+name,sum(a),sum(K)-sum(V))
check('changed-dt',action((0,1,3),F(2)),([F(1,2),2],[0,2],[F(1,2),0]))
a=action((1,2,2))[2]; m=[1,-4]; r=[x-y for x,y in zip(a,m)]
check('component-residual',r,[-1,0])
check('row-reconstruction',[x+y for x,y in zip(m,r)],a)
check('total-reconstruction',sum(m)+sum(r),-4)
g=[-1,1j,1]
for name,u,expect in [('W1',[1j,1,1j],[-1,1j,-1j]),('P1',[1j,-1j,1],[-1,1,-1])]:
    transformed=[g[j]*u[j]/g[(j+1)%3] for j in range(3)]
    check('links-'+name,transformed,expect)
    check('loop-'+name,prod(transformed),prod(u))
    check('inverse-'+name,[transformed[j]*g[(j+1)%3]/g[j] for j in range(3)],u)
w=[1j,1j,-1,-1j,1j,1]; p=[-1,1j,1j,1,-1j,1j]
for name,z,omit in [('W1',w,3),('P1',p,4)]:
    check('six-product-'+name,prod(z),1)
    mutation=z[:omit]+z[omit+1:]
    check('omission-'+name,prod(mutation),1j)
    check('omission-division-'+name,prod(mutation),prod(z)/z[omit])
    check('omission-residual-'+name,prod(mutation)-1,1j-1)
for name,z,index,multiplier,expected in [('W1',w,0,1j,-1j),('P1',p,4,-1,-1)]:
    new=z.copy(); new[index]/=multiplier
    check('rebased-coefficient-'+name,prod(new),expected)
    check('fixed-tau-scalar-'+name,prod(new)*multiplier,prod(z))
    check('rebase-inverse-'+name,new[index]*multiplier,z[index])
def h(d): return F(d[0],3)+F(d[1],4)+F(d[2],72)
for d,expected in [((1,0,48),1),((0,1,54),1),((1,1,30),1),((1,1,-42),0),((1,1,0),F(7,12))]:
    check('dual-'+str(d),h(d),expected)
for name,A3,A2,C,d,expected_n,expected_pair in [('W1',1,0,3,(1,1,30),(2,F(3,4),F(1,24)),4),('P1',0,1,4,(0,1,54),(F(4,3),2,F(1,18)),5)]:
    n=(A3+F(C,3),A2+F(C,4),F(C,72))
    check('charges-'+name,n,expected_n)
    check('direct-pair-'+name,sum(x*y for x,y in zip(d,n)),expected_pair)
    check('expanded-pair-'+name,A3*d[0]+A2*d[1]+C*h(d),expected_pair)
for label,z in [('lesson-sector-b',w[:-1]+[-1]),('capstone-sector-b',p[:-1]+[-1j])]:
    check(label,prod(z),-1)
    check(label+'-residual',prod(z)-1,-2)
for j in range(1,8):
    content=(ROOT/f'lesson-{j:02}.md').read_text(encoding='utf-8')
    for suffix in ['E1','W1','P1','D1']:
        check(f'content-anchor-C19.{j:02}-{suffix}',f'C19.{j:02}-{suffix}' in content,True)
    check(f'lesson-{j:02}-contract',all(x in content for x in ['Essential question','Goals:','Prerequisite bridge','Worked answer','Diagnostics','Claim scope','Next dependency']),True)
    check(f'capstone-step-{j:02}',f'C19-CAP-{j:02}' in (ROOT/'capstone.md').read_text(encoding='utf-8'),True)
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
for source in packet['sources']:
    check('source-hash-'+source['id'],hashlib.sha256(Path(source['path']).read_bytes()).hexdigest(),source['sha256'])
payload={'schema_version':'1.0','status':'passed','runtime':sys.executable,'scope':'Exact finite synthetic arithmetic and content-anchor checks; no physical or global-source replay','check_count':len(results),'checks':results}
(ROOT/'worked-example-verification.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','check_count':len(results),'runtime':sys.executable}))
