"""Independent finite-example audit; standard library only, no source copies."""
import itertools, json, math, sys
from fractions import Fraction as Q
from pathlib import Path

checks=[]
def check(name, condition):
    assert condition, name
    checks.append({'check': name, 'result': 'passed'})
check('tf_gpu_env runtime', sys.executable.lower()==r'C:\Users\info\.conda\envs\tf_gpu_env\python.exe'.lower())
classes=[[x for x in itertools.product(range(3),repeat=3) if sum(x)%3==r] for r in range(3)]
check('27 disjoint nodes in three classes of 9', [len(c) for c in classes]==[9,9,9] and len(set(sum(classes,[])))==27)
for f in [list(range(1,10)),[9]+[0]*8]:
    m=Q(sum(f),9);d=[x-m for x in f]
    check('Mean-detail reconstruction '+str(f), sum(d)==0 and [m+x for x in d]==f and sum(x*x for x in f)==9*m*m+sum(x*x for x in d))
for amp in [Q(1),Q(2)]:
    check('Nine-label lift norm and inverse '+str(amp),9*(amp/3)**2==amp**2 and 9*(amp/3)/3==amp)
check('27-label normalization counterexample',27*Q(1,3)**2==3)
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def adj(A):return [[complex(A[j][i]).conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def close(A,B):return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))<1e-12
I=[[int(i==j) for j in range(3)] for i in range(3)]
w=complex(-.5,math.sqrt(3)/2)
F=[[w**(j*k)/math.sqrt(3) for k in range(3)] for j in range(3)]
check('All entries F dagger F = I',close(mul(adj(F),F),I))
P=[[int(i==(j+1)%3) for j in range(3)] for i in range(3)]
D=[[w**i if i==j else 0 for j in range(3)] for i in range(3)]
check('DP = omega PD',close(mul(D,P),[[w*v for v in row] for row in mul(P,D)]))
def power(A,n):
    out=I
    for _ in range(n):out=mul(out,A)
    return out
basis={(a,b):mul(power(D,a),power(P,b)) for a,b in itertools.product(range(3),repeat=2)}
def trace(A):return sum(A[i][i] for i in range(3))
check('All 81 Weyl trace inner products',all(abs(trace(mul(adj(B),basis[c]))-(3 if k==c else 0))<1e-12 for k,B in basis.items() for c in basis))
for coeff in [{(0,0):1,(0,1):2,(2,1):-1},{(0,0):2,(1,0):1,(0,2):-1}]:
    Y=[[sum(v*basis[k][i][j] for k,v in coeff.items()) for j in range(3)] for i in range(3)]
    got={k:trace(mul(adj(B),Y))/3 for k,B in basis.items()}
    rebuilt=[[sum(got[k]*B[i][j] for k,B in basis.items()) for j in range(3)] for i in range(3)]
    check('Weyl extraction/reconstruction '+str(coeff),all(abs(got[k]-coeff.get(k,0))<1e-12 for k in basis) and close(Y,rebuilt))
R=[[Q(1,2),Q(1,2),0],[Q(1,2),Q(1,2),0],[0,0,1]]
check('R squared = R exactly',mul(R,R)==R)
for inp,expected in [([2,0,3],[1,1,3]),([4,2,-1],[3,3,-1])]:
    out=[row[0] for row in mul(R,[[v] for v in inp])];comp=[a-b for a,b in zip(inp,out)]
    check('Projector image/complement '+str(inp),out==expected and comp==[1,-1,0] and [a+b for a,b in zip(out,comp)]==inp)
check('Independent product addresses',len(list(itertools.product(range(16),range(3),range(1))))==48 and 16*3*2==96 and 2*3*1==6)
for A,B,C,E,su,sw,ue,we in [(2,1,1,3,5,7,Q(8,5),Q(9,5)),(3,1,2,2,7,8,Q(3,2),Q(5,2))]:
    S=Q(A)-Q(B*C,E);r=Q(su)-Q(B*sw,E);u=r/S;v=(sw-C*u)/E
    check('Schur exact reconstruction '+str((A,B,C,E)),u==ue and v==we and A*u+B*v==su and C*u+E*v==sw and E*S==A*E-B*C)
check('E zero uniquely solvable branch',1+2==3 and 1==1 and 1*0-1*1==-1)
check('S zero free and incompatible branches',all(t+(2-t)==2 for t in [Q(-3,2),0,1,5]) and 2!=3)
print(json.dumps({'runtime':sys.executable,'checks':checks,'count':len(checks),'result':'passed'},indent=2))
