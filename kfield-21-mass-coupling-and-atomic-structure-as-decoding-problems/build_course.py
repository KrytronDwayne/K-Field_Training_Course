from pathlib import Path
import json, hashlib
ROOT=Path(__file__).parent
P=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text): (ROOT/name).write_text(text.rstrip()+'\n',encoding='utf-8')
def js(name,obj): write(name,json.dumps(obj,indent=2,ensure_ascii=False))
def digest(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
def initialize():
    if (ROOT/'manifest.json').exists(): return
    cps=[]
    for i,l in enumerate(P['course_map']):
        name=l['id']+'.md'; write(name,'# '+l['title']+'\n\nPending authoring.')
        cps.append(dict(id=l['id'],kind='lesson',path=name,status='pending',dependencies=[P['course_map'][i-1]['id']] if i else [],summary=l['title'],sha256=digest(name)))
    write('course-map.md','# Course map\n\nAuthoring in approved order; see input-contract.json.')
    write('terminology.md','# Terminology\n\nPending authored definitions.')
    js('manifest.json',dict(schema_version='1.0',topic=P['topic'],audience=P['audience'],assumptions=P['assumptions'],checkpoints=cps,blockers=[],next_action='Author lesson-01; verify source arithmetic',course_order=[x['id'] for x in cps]))
    js('audit_report.json',dict(status='pending',findings=[],unresolved_counts=dict(critical=0,major=0,minor=0)))
    js('completion_report.json',dict(status='in_progress',topic=P['topic']))
initialize()
V=json.loads((ROOT/'verification.json').read_text())
def vec(a): return '('+', '.join(map(str,a))+')'
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+'\n'.join('| '+' | '.join(map(str,r))+' |' for r in rows)
def anchor(i):return '<a id="'+i+'"></a>\n'
lessons={}
def lesson(n,question,goals,bridge,body,questions,answers):
    l=P['course_map'][n-1]; a=l['teaching_anchor']; ident=l['id'];cid=a['concept_id']
    txt='# '+ident+': '+l['title']+'\n\n'+str(a['planned_periods'])+' sessions of 55 minutes.\n\n'
    txt+='**Essential question:** '+question+'\n\n**Goals**\n\n'+'\n'.join('- '+g for g in goals)+'\n\n'
    txt+='## Prerequisite bridge\n\n'+bridge+'\n\n'+anchor(a['explanation_id'])+'## Explanation — '+a['explanation_id']+'\n\n'+body+'\n\n'
    txt+=anchor(a['worked_example']['id'])+'## Worked example — '+a['worked_example']['id']+'\n\n'+a['worked_example']['task_and_answer']+'\n\n'
    txt+=anchor(a['guided_practice']['id'])+'## Guided practice — '+a['guided_practice']['id']+'\n\nTry the operation before reading the solution. '+a['guided_practice']['task_and_answer']+'\n\n'
    for s in a.get('supplemental_exercises',[]):
        explanation=s['explanation'].replace('Teach signed characters on','Use signed characters on').replace('Explain an intertwiner T by','An intertwiner T obeys')
        txt+=anchor(s['explanation_id'])+'## Supplemental explanation — '+s['explanation_id']+'\n\n'+explanation+'\n\n'
        for key,label,textkey in [('worked_example_id','Worked example','worked_task_and_answer'),('prior_practice_id','Practice with answer','practice_task_and_answer'),('diagnostic_id','Diagnostic boundary','diagnostic_task_and_answer')]:
            txt+=anchor(s[key])+'### '+label+' — '+s[key]+'\n\n'+s[textkey]+'\n\n'
    if n==4: txt+='### Answered practice: reference mass withheld\n\nUse the existing synthetic c=(1,0,0,0,0,1) and b_toy=(1,1/10,1/100,1/1000,1/5,2), but withhold the numerical value of m_ref. Find the ratio and state exactly what remains unresolved.\n\n**Answer:** c dot b_toy=1+2=3, so m/m_ref=3 and m=3*m_ref. The dimensionless ratio is completely computed. The numerical dimensional mass remains unresolved until m_ref is supplied. Keep the coefficient and syndrome records; withholding the reference mass does not erase their known values.\n\n'
    txt+=anchor(a['diagnostic']['id'])+'## Diagnostic checks — '+a['diagnostic']['id']+'\n\n'+'\n'.join(str(i+1)+'. '+q for i,q in enumerate(questions))+'\n\n## Worked answers\n\n'+'\n'.join(str(i+1)+'. '+q for i,q in enumerate(answers))+'\n\n'
    boundary='Neither b nor a solver chooses a physical occupied c. Missing contributing renderer entries leave their terms symbolic. If only m_e is absent, report the computable dimensionless ratio c dot b and retain m=(c dot b)m_e symbolically; the numerical dimensional mass is unresolved. A rounded report 2.33 is not exact 7/3; retain their difference.' if n==4 else a['diagnostic']['task_and_answer']
    txt+='**Boundary to carry forward:** '+boundary+'\n\n'
    txt+='**Next dependency:** ['+l['later_use']+']('+l['later_use']+'.md). Use this lesson’s reconstruction and scope checks there.\n'
    write(ident+'.md',txt);lessons[ident]=txt.rstrip()
    m=json.loads((ROOT/'manifest.json').read_text());cp=next(x for x in m['checkpoints'] if x['id']==ident);cp.update(status='drafted',sha256=digest(ident+'.md'));m['next_action']='Audit '+ident+' and continue dependencies';js('manifest.json',m)

lesson(1,'How can three channels describe two unknowns without throwing away the third reading?',
['Translate channel recipes into equations and an ordered matrix.','Solve two normal equations by elimination.','Reconstruct every input from represented and residual entries.'],
'''You need signed arithmetic, fractions and linear equations. A tuple is an ordered list: (2,3,6) means first channel 2, second 3, third 6. Multiplying a tuple by a number multiplies every entry; adding tuples adds corresponding entries. These are the only operations needed to begin. Earlier courses motivate retained information, but all matrix operations used here are taught locally.''',
'''Imagine two adjustable coordinates, c1 and c2. A channel is a stated recipe for combining them. Our synthetic instrument reports c1, c2, and c1+c2. A linear recipe multiplies each coordinate by a fixed number and adds; there are no products of unknown coordinates. Arrange the recipes as rows:

```text
A_small = [1 0]     c = [c1]       A_small c = (c1,c2,c1+c2)
          [0 1]         [c2]
          [1 1]
```

A matrix is this rectangular table of coefficients. A row times a column means multiply matching entries and add. Its shape is 3 by 2: three output channels and two input coordinates. The system is overdetermined because there are more equations than unknowns. It may be exactly consistent, but it need not be. For y=(2,3,6), the first two equations demand c1=2 and c2=3, whose sum is 5 rather than 6. Keep all three readings.

Declare a decoding convention before solving. In this course the scalar field is the real numbers, written R, and the inner product is Euclidean: u dot v is the sum of pairwise products. For example (1,0,1) dot (2,3,6)=8. We choose the represented vector A_small c so that the residual r=y-A_small c is perpendicular to each column. Perpendicular here means dot product zero. This convention is a reproducible coordinate choice, not a discovery that the residual lacks information.

The transpose A_small^T is obtained by turning columns into rows. Thus A_small^T r=(r1+r3,r2+r3). Set both entries to zero. Substituting r=(2-c1,3-c2,6-c1-c2) gives 8-2c1-c2=0 and 9-c1-2c2=0. These are the normal equations. In compact notation A_small^T A_small c=A_small^T y. Multiplication here has already been defined by sums; it introduces no new physical assumption.

Solve 2c1+c2=8 and c1+2c2=9. Twice the first minus the second gives 3c1=7, so c1=7/3. Then c2=8-14/3=10/3. The represented channels are (7/3,10/3,17/3). Subtract each from y to obtain r=(-1/3,-1/3,1/3). The two perpendicularity checks are -1/3+1/3=0 and -1/3+1/3=0. Reconstruction gives (7/3-1/3,10/3-1/3,17/3+1/3)=(2,3,6).

This construction also minimizes the sum of squared residual entries, but that score is not our saved output. To see the mathematical fact without calculus, change c by h. The new residual is r-A_small h. Its squared length is r dot r minus twice r dot A_small h plus (A_small h) dot (A_small h). The middle term is zero by the perpendicularity condition, and the last term is nonnegative. This explains the convention while leaving the entire signed residual intact.

> Scope: All channel values in these exercises are synthetic and dimensionless. The Euclidean metric is declared. A different weighting would define a different decoder and must be recorded. No physical source coefficient-selection law is being inferred.

For practice y=(1,2,3), compute A_small^T y=(1+3,2+3)=(4,5). Elimination gives c=(1,2). All three residual entries are zero, so explicitly retain (0,0,0), the channel order and the matrix. A missing entry and a known zero are different records.''',
['For y=(1,1,3), write and solve the normal equations; retain r.','Explain why three rows need not provide three independently adjustable coefficients.','Check every reconstruction entry for y=(2,3,6).','What extra information is lost if only the residual squared length is stored?'],
['The equations are 2c1+c2=4 and c1+2c2=4. Subtraction gives c1=c2; hence c=(4/3,4/3), represented=(4/3,4/3,8/3), r=(-1/3,-1/3,1/3).','There are only two column recipes; the third output is their sum. More readings do not create an additional coefficient direction.','7/3-1/3=2; 10/3-1/3=3; 17/3+1/3=6.','Signs and channel positions disappear. For instance r and -r have the same squared length but reconstruct different input vectors.'])

lesson(2,'What does an independent residual coordinate preserve?',
['Count independent column and residual directions.','Recover a full residual vector from its declared coordinate and basis.','Distinguish real-space equality from integer-lattice equality.'],
'''Lesson 1 taught row multiplication, dot products and reconstruction. We now ask how many freely chosen numbers each part needs. Keep A_small and its ordered three channels. All computations still use exact fractions.''',
'''A column direction is independent of others if it cannot be made by combining them. For A_small, a times (1,0,1) plus b times (0,1,1) is zero only if a=0 and b=0, because its first two entries are a and b. The rank is therefore two. A vector space allows any real multiples and sums of its directions. The image of a matrix is the set of outputs it can make; its kernel is the set of inputs it sends to zero.

The residual conditions r1+r3=0 and r2+r3=0 imply r=(-t,-t,t). Choose t=r3 freely and the other entries are fixed. The residual subspace, also called the left-null space of A_small, therefore has one independent coordinate. We may save t together with the basis vector (-1,-1,1), but saving t without that convention is ambiguous. This course saves the full vector as well. Here the word syndrome names retained coordinates outside the represented image, not an error verdict.

The three numbers (c1,c2,t) reconstruct y=(c1-t,c2-t,c1+c2+t). Conversely y3-y1-y2=3t, so t=(y3-y1-y2)/3, c1=y1+t, and c2=y2+t. This gives an independent route to the previous answers. For (2,3,6), t=(6-2-3)/3=1/3. These formulas demonstrate lossless separation, not merely a count of dimensions.

Real numbers and integers support different claims. Write Z for the integers. An integer lattice consists of integer combinations of the declared columns. Take A0=(2,0)^T and L0=(0,1). The first maps a number a to (2a,0); the second maps (x,y) to y. Over R, the image of A0 and kernel of L0 are both the entire horizontal line. Over Z, the image contains only even horizontal coordinates, but the kernel contains (1,0). Their ranks agree and L0 A0=0, yet their integer sets differ.

A lattice is saturated in its real span if every integer point in that span already belongs to the lattice. The even horizontal lattice is not saturated. Replacing A0 by (1,0)^T repairs this example: (n,0)=A0 n for every integer n. In lesson 3 we will prove saturation for the particular source matrix using an integer coefficient extractor. This is stronger evidence than an unsupported appeal to matching rank.

> Scope: S02 /proof_nodes/10 reports an integer exact-sequence statement, while its displayed dimension argument alone establishes the real-space part. S03 /findings/8 flags the missing source L. We keep the reported status, the argument’s scope and the missing object separate; the small counterexample is freshly checked teaching mathematics.

At the first unit boundary, explain the distinction aloud: A_small^T r=0 says two sums cancel. It does not say each of the three entries of r vanishes. A full residual can remain even when the decoder equations are solved exactly.''',
['For y=(1,1,3), find t and reconstruct y.','Why is A_small^T r=0 compatible with a nonzero r?','Show integer image/kernel equality for A0=(1,0)^T and L0=(0,1).','What fails if only rank is supplied for the even-lattice example?'],
['t=(3-1-1)/3=1/3; c1=c2=4/3. Reconstruction is (1,1,8/3+1/3)=(1,1,3).','The constraints concern sums r1+r3 and r2+r3; (-1,-1,1) satisfies them without being zero.','L0(x,y)=0 forces y=0. Every integer (n,0) is obtained by applying A0 to integer n, and every such output is in the kernel.','Rank counts real directions, not missing integer points. (1,0) is a specific missing point demonstrating the failure.'])

ledger=table(['channel i','y_i','(Ac)_i','s_i'],[[i+1,*[V['worked'][k][i] for k in ['y','represented','syndrome']]]for i in range(13)])
matrix='\n'.join(' '.join(row)for row in V['A'])
lesson(3,'How can thirteen readings be retained as six represented and seven residual coordinates?',
['Use the source matrix in its stated order and verify its rank.','Reconstruct a full thirteen-channel ledger.','Distinguish the integer extractor from the missing source syndrome map.','Check a small character table and a specified intertwiner.'],
'''Lesson 2 taught image, kernel, rank, integer lattices and residual bases. This lesson extends the same operations to a larger rectangular table. Work in three sessions: channel decoding; integer extraction; signed characters. Long tables are for careful checking one row at a time, not memorization.''',
'''S02 /backbone_sequence/16 (M17) supplies the following 13 by 6 matrix A. Row i means channel i; column j multiplies coefficient cj. Keep this ordering. Its columns correspond to the renderer order b=(1,alpha,alpha^2,alpha^3,a_e,eta), which lesson 4 interprets. The classroom calculations use dimensionless channels.

```text
'''+matrix+'''
```

For c=e1=(1,0,0,0,0,0), multiplying A by c simply selects column 1: (0,0,0,0,1,1,1,1,1,1,1,1,1). This is the safest first check of the row order.

The Gram matrix is G=A^T A: its entry (j,k) is the dot product of columns j and k. Column 1 has nine ones, so G11=9; columns 1 and 2 overlap in six ones, so G12=6. Carrying out the remaining dot products gives a top-left block [[9,6,6],[6,9,6],[6,6,9]], bottom-right block diag(6,6,6), and zeros between. This G is only a decoder Gram matrix, not M_cell or G_phase.

The first block acts on (a,b,d) by 3(a,b,d)+6(a+b+d)(1,1,1). On the constant direction (1,1,1) it multiplies by 21. On directions whose entries sum to zero it multiplies by 3. A direction scaled without changing direction is called an eigenvector, and the scale is its eigenvalue. Every triple is a constant triple plus a sum-zero triple: subtract its mean (a+b+d)/3 from each entry. Thus no nonzero triple is sent to zero. The last three directions multiply by 6. All six coefficients can therefore be recovered uniquely; rank A=6. Thirteen total channel coordinates minus six independent represented directions leaves seven independent residual directions.

You do not need a general matrix-inverse algorithm to decode this A. First calculate d=A^T y by column dot products. Set S=(d1+d2+d3)/21. Then c1=(d1-6S)/3, c2=(d2-6S)/3, c3=(d3-6S)/3, and cj=dj/6 for j=4,5,6. Why? S=c1+c2+c3 and the first three normal equations read dj=3cj+6S. Summing them gives 21S=d1+d2+d3.

For y=(1,2,...,13), d=(81,72,65,-9,-3,-1); S=218/21. The equations yield c=(131/21,68/21,19/21,-3/2,-1/2,-1/6). Multiply each row and subtract to obtain this complete ledger:

'''+ledger+'''

For example row 3 predicts c2+c3+c6=68/21+19/21-1/6=167/42; adding -41/42 recovers 3. All thirteen rows are retained. The six sums A^T s vanish. The seven-dimensional syndrome is stored here as thirteen entries constrained by those six equations. A specified seven-element basis could compress the entries reversibly; the source’s particular basis is not supplied.

Compact recognition notation: Aplus=(A^T A)^(-1)A^T names the recipe just derived; inverse means the operation undoing a nonsingular matrix. P=A Aplus extracts represented channels and R=I-P extracts the residual; I leaves every vector unchanged. Since Aplus A=I6, applying P twice gives P again, as does applying R twice. Also A^T R=0. The verification file checks these exact identities. R is a 13 by 13 projector and is not the missing 7 by 13 source L.

There is a different, integer extractor for vectors already in the image. If z=Ac, then c1=z5, c2=z2, c3=z1, c4=z8-z5-z2, c5=z6-z5-z1, c6=z3-z2-z1. These six recipes define L_int, a 6 by 13 integer matrix, with L_int A=I6. Recognition-only certificate vocabulary: their selected rows (5,2,1,8,6,3) form a triangular 6 by 6 matrix (entries above its main diagonal are zero). For a triangular matrix the determinant is the product of diagonal entries, here 1. A square submatrix with determinant 1 or -1 is called a unit minor. The explicit integer recipes, rather than determinant vocabulary, are the core proof used next. An integer z in the real image consequently has integer c=L_int z, proving saturation for this A. If an integer rank-seven source L with LA=0 is supplied, real image/kernel equality plus this saturation establishes integral equality. The extractor does not identify that L. Applied to arbitrary y outside the image, it is not the Euclidean decoder; rational c remains possible.

### A finite bridge to signed characters

Use two-bit labels 00,01,10,11. Addition of labels is bitwise addition modulo 2 (1+1 becomes 0). For a row label x and column label k, multiply matching bits, add, and set W[x,k]=(-1) raised to that sum. Even sums give +1; odd sums give -1. A character is a sign recipe respecting addition: the sign for x+x-prime is the product of the two signs. The table is

```text
       00  01  10  11
00      1   1   1   1
01      1  -1   1  -1
10      1   1  -1  -1
11      1  -1  -1   1
```

Each column has squared length 4; two different columns have dot product zero (for columns 01 and 10, the products are 1,-1,-1,1). Hence W^T W=4I and coefficients a=W^T v/4 reconstruct v=Wa. For v=(1,2,3,4), the four sums are 10,-2,-4,0, giving a=(5/2,-1/2,-1,0). The first reconstructed entry is 5/2-1/2-1=1; the others are 2,3,4.

A representation describes how each group operation acts on coordinates. To compare two actions rho and sigma, an intertwiner T must obey T rho(g)=sigma(g) T for every operation g. In the two-action example below it is enough to check the nonidentity involution (an operation whose square is identity). With rho=diag(1,-1), sigma=diag(-1,1), swapping coordinates by T=[[0,1],[1,0]] gives both products [[0,-1],[1,0]]. T is invertible, and 2T also works, so compatibility does not choose a unique map. In contrast rho has a fixed nonzero vector (1,0), whereas -I has none; an invertible intertwiner to -I cannot preserve that action. Their traces, the sums of diagonal entries, are 0 and -2, another obstruction.

> Source boundary: S02 /branch_proofs/11 reports closed exact module compatibility; /proof_nodes/10, /11 and /23 give the active/syndrome and character claims. Conditional arithmetic 3(1,1,1)+2(2,0,-1)=(7,3,1) and 3²+2²=13 is checkable here. The representation-theory interpretation requires the source actions. Source L (7 by 13) and W7 (eight group elements by seven nonconstant characters, ordered source action not loaded) remain VERIFIED_NOT_LOADED under S03 /findings/8. This toy 4 by 4 W and derived L_int do not replace them.''',
['How many independent coefficients and syndrome coordinates occur? Why save thirteen residual entries?','Decode the c0 and s practice packet below; reconstruct its first four entries.','What does L_int prove, and why is it not source L?','For v=(2,0,0,2), compute the four signed coefficients and reconstruct v.','Why do equal-dimensional actions rho=diag(1,-1) and sigma=-I fail to have an invertible intertwiner?'],
['Six and seven. Thirteen entries carry the seven-dimensional residual with six constraints; this representation fixes channel meaning without inventing a basis.','Ac0=(2,-1,1,1,1,4,2,0,3,1,0,3,1). Adding s gives y=(0,-3,2,2,1,4,2,0,3,1,0,3,1). A^T s=0 so the decoder returns c0 and the full s.','L_int A=I6 provides integer recovery on the image and saturation. Its shape is 6 by 13 and product is identity, whereas source L is 7 by 13 with product zero.','W^T v=(4,0,0,4); divide by 4 to get (1,0,0,1). Adding columns 00 and 11 gives (2,0,0,2).','An invertible action-preserving map would send the nonzero fixed vector of rho to a nonzero fixed vector of -I, which has none. Equal dimension alone is insufficient.'])

lesson(4,'What does a mass renderer add, and what information must remain beside it?',
['Reconstruct channels before rendering a scalar.','Evaluate a supplied dimensionless dot product and restore mass units.','Identify missing occupied-state and reference-mass inputs.'],
'''Lesson 3 supplied six coefficients and a complete syndrome. A dot product was taught in lesson 1. A ratio of two quantities with the same unit is dimensionless: 6 mass units divided by 2 mass units is the number 3.''',
'''A decoder answers how a channel vector splits under a declared geometry. A renderer answers a different question: what scalar is associated with supplied coordinates? M17 writes m/m_e=c dot b with b=(1,alpha,alpha²,alpha³,a_e,eta). In words, multiply c1 by 1, c2 by alpha, c3 by alpha², c4 by alpha³, c5 by a_e and c6 by eta, then add. Here alpha² means alpha times itself; alpha³ multiplies three copies. The renderer is dimensionless if c and b are dimensionless. Multiply by a supplied reference mass m_e to obtain a dimensional m.

The source stores alpha=0.0072973525643314245 and eta=1836.1526734259999, and describes a_e as an occupied-state coordinate. These are source witnesses with the displayed precision, not new measurements or newly established exact rational constants. A physically occupied coefficient state needs an explicit selection rule or supplied state. Solving the channel equations alone does not supply that rule. If a contributing renderer entry is missing, keep its term symbolic; for example, an absent a_e leaves c5 a_e symbolic when c5 is nonzero. If only the numerical reference mass m_e is absent, compute the dimensionless ratio m/m_e=c dot b from the supplied entries and retain m=(c dot b)m_e symbolically. Only the numerical dimensional mass remains unresolved in that case.

To practice the arithmetic without pretending to fill those gaps, use b_toy=(1,1/10,1/100,1/1000,1/5,2), and define m_ref=2 synthetic mass units. For c=(1,0,0,0,0,1), the ratio is 1+2=3 and mass is 3 times 2=6 mass units. These are separately declared classroom inputs. Retain c, b_toy, m_ref and s; the number 6 cannot reconstruct thirteen channels.

For the practice c=(0,2,0,0,1,0), the ratio is 2/10+1/5=2/5. Multiplying by m_ref gives 4/5 mass units. With s=0, the source channel matrix yields y=(0,2,2,2,0,1,-1,2,3,1,2,3,1). Even a zero syndrome must be saved as thirteen zero entries with its channel order. A negative channel in this synthetic linear system is permitted; it does not assert a negative physical mass.

Different c may give the same scalar dot product. For example in this toy renderer c=(1,0,0,0,0,0) and c=(0,10,0,0,0,0) both give ratio 1, but their channel vectors differ. Scalar rendering therefore does not replace channel decoding or residual preservation.

> Scope: The source renderer and its witness values are S02 /backbone_sequence/16. The toy renderer is synthetic and is never substituted for physical b. Neither an occupied-state rule nor a_e’s missing definition body is manufactured. Binding, coupling interpretation and measured mass require their own typed input records.''',
['Compute the practice mass and list the required synthetic inputs.','Why does a mass ratio have no mass unit?','If a_e is missing and c5 is nonzero, what result can be reported?','Show why saving just m cannot preserve the syndrome.'],
['The ratio is 2/5 and m=4/5 mass units. Inputs: the six c values, b_toy, m_ref=2 mass units, A and thirteen zero s entries.','The numerator and denominator have the same unit, which cancels; restoring mass requires multiplication by a reference mass.','Report the symbolic term c5 a_e with the other known terms and mark the occupied-state input unresolved.','Changing s while keeping c fixed changes y=Ac+s but leaves c dot b unchanged. Thus many complete channel packets can share one rendered mass.'])

lesson(5,'Which atomic labels must be fixed before two masses can be compared?',
['Compute a nominal composition label and verify allowed endpoint counts.','Test dependent and independent composition-preserving moves.','Balance synthetic constituent and charge ledgers before applying a mass-energy conversion.'],
'''Lessons 1–4 taught linear maps and reconstruction. Composition counting is another linear map, but its inputs have different meanings: atom counts rather than decoder coefficients. Do not identify the two spaces merely because both use tuples.''',
'''An element identifies a nucleus by its proton count. Isotopes of the same element have different neutron counts. A neutral atom has equal numbers of electrons and protons; removing an electron makes its charge one elementary charge more positive. A molecular formula counts constituent atoms. An isomer has the same formula but a different arrangement. These labels answer different questions, so a report keeps them in separate fields.

Declare the order (C,H,N,O), where each letter is the count of carbon, hydrogen, nitrogen or oxygen atoms. S05 R008 defines nominal V=12C+H+14N+16O. For (4,4,0,1), V=12 times 4+4+14 times 0+16=68. The source calls the label nominal Da; here we say nominal units to distinguish the arithmetic from exact isotope masses. It is not a physical geometric volume despite the symbol V. Negative counts cannot describe an endpoint formula, though signed differences between valid formulas can be useful.

A fiber is the set of inputs sharing one output value. Different compositions can lie in the same V-fiber. A move U is an integer difference tuple; V stays fixed precisely when its weighted sum is zero. For U1=(-1,-2,1,0), the weighted sum is -12-2+14=0. For U2=(1,4,0,-1), it is 12+4-16=0. For U3=(0,2,1,-1), it is 2+14-16=0. But U1+U2=U3 entry by entry, so these are only two independent directions. U1 and U2 are independent because the N entry forces the coefficient of U1 to vanish in a zero combination, after which U2’s O entry forces its coefficient to vanish.

The move K=(-4,0,0,3) also preserves V because -48+48=0. It cannot equal aU1+bU2: its N entry would force a=0, its H entry then forces 4b=0, leaving no C change. K adds a third direction. One constraint on four real coordinates leaves three independent directions; integer-lattice basis questions still require more than a rank count. These moves establish independent directions, not automatically a full integer basis.

Starting from (4,4,0,1), U1 gives (3,2,1,1), whose label is 36+2+14+16=68. U2 gives (5,8,0,0), whose label is 60+8=68. K sends (4,0,0,0) to (0,0,0,3); both labels are 48. Attempting K from (1,0,0,0) would give (-3,0,0,3), an invalid endpoint. A nominal count move is not automatically a physically balanced reaction: carbon and oxygen nuclei are different constituent types.

### Before subtracting endpoint masses

For a synthetic assembly A+B → AB, declare conserved labels A and B. Initial inventory is one A label and one B label; final AB contains exactly those same labels. Declare all three objects neutral and in the specified reference state, so total charge is zero on both sides. Declare each listed mass to include the entire object and its electrons and binding state. Isotopic identities are stipulated unchanged constituents, not inferred from nominal integer weights. There is no emitted unlisted object in this classroom ledger.

Use the reference relation Q_release=(m_initial-m_final)c_light². The symbol c_light is the speed entering mass-energy conversion, not the coefficient vector c. Positive Q_release means energy available by this endpoint difference; negative Q_release means required energy input under the convention. For classroom arithmetic stipulate a synthetic conversion of 1 u times c_light²=10 E_unit. This is not the physical numerical conversion for an atomic mass unit; u here is a declared mass unit in the synthetic problem.

With complete-object masses A=2u, B=3u, AB=4.9u, initial mass is 5u. Subtract final mass to retain delta m=0.1u. Multiply by 10 E_unit/u to get Q_release=1 E_unit. Setting AB=5.05u changes delta m to -0.05u and Q_release to -0.5 E_unit. The latter requires input of 0.5 E_unit; do not erase the sign or normalize it away.

If the initial masses include electrons but the final mass describes a bare positive ion, this ledger is incomplete. Specify the removed electron and consistent binding/ionization states before subtracting; a missing mass cannot be guessed. Even equal formulas can represent different binding states or isomers.

> Source scope: S05 /records/7 is archive_stated nominal composition arithmetic. /records/21 reports dependence of three tested moves; /records/22 reports the independent 4C↔3O direction and a mass-step claim of 15.25614129 mDa (one mDa is one thousandth of a dalton). That decimal and its source claim of exactness are attributed synthesis, not a fresh isotope-mass replay: the required isotope constants and full endpoints have not been loaded. We freshly verify nominal invariance and independence only. R032’s three rank-three structures do not supply a canonical connecting map.''',
['Calculate V for (3,2,1,1), and compare it with (4,4,0,1).','Show U3=U1+U2 and explain why K supplies another direction.','Apply K to (1,0,0,0). Is this a valid composition endpoint?','For the neutral synthetic A+B → AB, calculate Q if final mass is 5.05u.','What must be repaired if a final positive ion is compared with initial neutral masses?'],
['36+2+14+16=68, equal to 48+4+16=68. The formulas differ despite their common label.','The sum is (0,2,1,-1). If K=aU1+bU2, N forces a=0 and H forces b=0, contradicting K≠0.','The result (-3,0,0,3) has a negative C count and is invalid, though K remains a formal kernel direction.','5-5.05=-0.05u; multiplying by the declared 10 E_unit/u gives -0.5 E_unit. Input 0.5 E_unit is needed.','Include removed electrons and consistent charge, isotope and binding/reference states for all whole objects; until supplied, mark the endpoint incomplete rather than compute an unsupported difference.'])

lesson(6,'How can an atomic application be source-traced while its missing coordinates remain explicit?',
['Classify each source card as synthesis, mechanism or unresolved record.','Build a periodic-coordinate ledger without inventing values.','Compute an energy difference and distinguish it from a rate or power.'],
'''Lesson 5 separated formula, isotope, charge, arrangement and binding state. Lesson 3 showed why equal dimensions do not specify an action-preserving map. We now use both ideas to read an archival application without filling its gaps by analogy.''',
'''A source-traced report records what a document actually supplies and which operation was freshly checked. The source cards below are bounded readings of S05. The exact file path and digest appear in sources.md; record numbers use one-based labels but JSON pointers use zero-based array positions.

| Card | Pointer | Stored class | What the course can carry forward |
| --- | --- | --- | --- |
| R029 | /records/28 | synthesis | A proposed periodic coordinate package: base Cell3 address plus nested coordinate fibers. |
| R030 | /records/29 | synthesis; type mechanism | Nuclear, chemical and orientational relations as distinct types of edges. |
| R031 | /records/30 | archive_stated; type unresolved | Formula and nominal label leave isomers unresolved; preserve graph and binding information. |
| R032 | /records/31 | synthesis; type architecture | Three rank-three structures recur, while a canonical connecting map remains absent. |

A graph is a collection of vertices and edges: objects and their declared connections. An adjacency table records which vertex pairs connect; graph identity includes the labeled vertices and full edge list. A Laplacian is the degree table minus the adjacency table (degree counts the incident edges). Its spectrum is a list of eigenvalues, using the scaling-direction idea from lesson 3. These terms are recognition-only here: no unprovided molecular graph is assigned. A spectrum compresses a graph and need not uniquely identify it, so preserve graph identity alongside any spectral summary. An edge labeled chemical rearrangement is not the same operation as a nuclear change or an orientational coupling.

For a source-traced worked row, start with the synthetic composition (4,4,0,1). We know the counts and derived nominal V=68. R029 requests many more coordinates. A correct report looks like this:

| Field requested by R029 | Present value/status in this classroom packet |
| --- | --- |
| Composition counts, nominal label | (4,4,0,1), V=68; synthetic and freshly computed |
| Base Cell3 address | Not supplied |
| Scale/face sector and isospin lambda | Not supplied; source-local labels |
| Three composition-null coordinates | No basis and origin for this point supplied; invariant moves checked separately |
| Exact isotope mass | Not supplied; nominal weights do not replace it |
| Graph identity and spectrum | Not supplied; formula alone is insufficient |
| Charge/parity | Not supplied for this composition row; do not borrow synthetic A/B charge |
| Binding residual | Not supplied; retain as a required coordinate |
| QPC phase tensor | Not supplied; source-local phase-cost object, recognition only |
| Occupied coefficient selection | Not supplied; R030 edge classes do not select c |

The repeated rank three in R032 is an explanatory target: composition-null directions, a geometric isofacial tangent fiber and the EG three-channel phase transform. We have constructed only the composition arithmetic. A meaningful map would need typed domains, units, bases, actions and a rule taking one object to the other. The rank count alone is insufficient. No Cell3 metric, physical coordinate or phase tensor is introduced numerically in this course; their source-local meanings are not merged with our decoder Gram matrix.

### Energy, rate and power have different input requirements

Retain the complete neutral-object convention of lesson 5 and its synthetic conversion. For AB=4.8u, delta m=2+3-4.8=0.2u, and Q_release=2 E_unit. This is an endpoint difference. It supplies no duration, transition frequency or usable-energy fraction. A rate counts events per time; average power is energy delivered divided by duration. If a separate premise says this 2 E_unit release is delivered over 4 time units and half is recovered, recovered energy is 1 E_unit and mean recovered power is 1/4 E_unit per time unit. The duration and fraction must remain in the ledger.

The reference relation delta E=delta m c_light² concerns differences of rest energies of specified complete objects. It does not turn phase into force or a model energy into measured transferred energy. Our numerical conversion is stipulated, so every constant needed for the calculation is supplied locally; no external mass table is required.

> Claim scope: R029 and R030 are archival synthesis and proposed mechanism. The ledger’s missing fields are unresolved inputs, not zero values. The energy arithmetic is a synthetic application of a declared reference relation. No physical periodic address, nuclear reaction rate, binding force or occupied-state selection is claimed by these exercises.''',
['Which R029 fields are actually known for the composition (4,4,0,1)?','What are the different roles of R030 and R031?','Why does R032 not furnish a canonical map?','Compute Q for AB=4.8u, then compute recovered mean power with fraction 1/2 and duration 4.','Does positive Q alone determine a transition rate?'],
['Only the supplied counts and V=68; none of the other required coordinate values follows just from those counts.','R030 proposes typed binding/transition edges; R031 records unresolved isomer distinction and calls for graph and binding coordinates.','Three spaces of equal rank can have different bases, units and actions. The source explicitly does not supply a canonical connecting map.','Delta m=0.2u, Q=2 E_unit; recovered energy=(1/2)2=1 E_unit; divide by 4 time units for 1/4 E_unit per time unit.','No. A rate requires an additional time-dependent process or supplied event count and duration.'])

traces='\n\n'.join('Step t='+t+'\n\n'+table(['n','c_n','r_n','A_small^T r_n'],[[r['n'],vec(r['c']),vec(r['residual']),vec(r['normal_residual'])] for r in rows])for t,rows in V['traces'].items())
lesson(7,'What can a failed numerical iteration teach us without losing its input?',
['Perform two explicit solver updates and retain the full history.','Explain convergence or divergence using two taught error directions.','Distinguish numerical convergence, channel closure and physical identification.'],
'''Use A_small and synthetic y=(2,3,6) from lesson 1. The exact solution c_star=(7/3,10/3) is already known. A sequence is an ordered list indexed n=0,1,2,...; c_n is simply the coefficient pair after n updates.''',
'''A solver is a rule for producing successive candidates. Declare c_0=(0,0) and a step parameter t. At every stage compute r_n=y-A_small c_n, then the two normal residual sums g_n=A_small^T r_n, then c_(n+1)=c_n+t g_n. Save n, t, c_n, r_n and g_n together. These are different fields: the normal residual is two sums; the channel residual is three entries.

For t=1/4, the initial normal residual is (8,9). Multiply by 1/4 to get c_1=(2,9/4). Its represented channels are (2,9/4,17/4), so r_1=(0,3/4,7/4). Adding first-plus-third and second-plus-third gives g_1=(7/4,5/2). Multiply that by 1/4 and add to c_1: c_2=(2+7/16,9/4+5/8)=(39/16,23/8). Subtract its channels from y to get (-7/16,1/8,11/16).

'''+traces+'''

The t=1 branch is a useful comparison, not a discarded run. It first gives c_1=(8,9), so r_1=(2-8,3-9,6-17)=(-6,-6,-11). Thus g_1=(-17,-17), and c_2=(-9,-8). Reconstruction still works: (-9,-8,-17)+(11,11,23)=(2,3,6). The solver has moved away from its target while the retained packet remains exact.

To explain these branches without calculus, define coefficient error e_n=c_n-c_star. Since the exact solution obeys A_small^T y=G c_star with G=[[2,1],[1,2]], subtraction gives e_(n+1)=(I-tG)e_n. The sum direction (1,1) is multiplied by G by 3; the difference direction (1,-1) by 1. Every error (a,b) equals ((a+b)/2)(1,1)+((a-b)/2)(1,-1). Each update multiplies these two parts by 1-3t and 1-t respectively.

If a multiplier has absolute value less than one, repeated multiplication shrinks that component toward zero. For t=1/4, the multipliers are 1/4 and 3/4, so both shrink. For t=1, they are -2 and 0; the nonzero sum component flips sign and doubles each step. In general both shrink when 0<t<2/3. At the boundary t=2/3, the sum component flips without shrinking; at t=0 it does not move. These conclusions are about this explicit solver and matrix, not about all solvers.

Even as c_n approaches c_star, the channel residual approaches (-1/3,-1/3,1/3), not zero. Numerical convergence is reaching the decoder’s coefficients. Channel closure is whether r itself vanishes. Physical identification is whether the model coordinates and source selection rule describe the measured system. They are three distinct claims.

If columns are dependent, the normal matrix may be singular, meaning it has no unique inverse. For example two identical columns produce the same channels for coefficients (1,0) and (0,1). A solver must preserve the free-coordinate ambiguity, use additional declared constraints if supplied, and check compatibility; it must not invent uniqueness.

> Scope: These finite iteration histories are synthetic computations. Divergence exposes parameter dependence; it is not a reason to delete inputs, negative residuals or the failed branch. A scalar norm may index a history but cannot replace any saved coordinate.''',
['Recompute c_2 and r_2 for t=1/4.','Recompute the t=1 branch through its second update.','At t=2/3, what happens to the sum-direction error?','If g_n=0, must r_n=0 or c_n represent a physical occupied state?'],
['c_2=(39/16,46/16); its third channel is 85/16. Subtract from (32/16,48/16,96/16) to get (-7/16,2/16,11/16).','c_1=(8,9), r_1=(-6,-6,-11), g_1=(-17,-17), c_2=(-9,-8), r_2=(11,11,23).','The multiplier 1-3(2/3)=-1 flips the sign without shrinking a nonzero component.','No. At c_star the two normal sums are zero while r_star=(-1/3,-1/3,1/3). Physical occupied-state selection is a separate, here missing, input.'])

lesson(8,'What must a report contain so another reader can reconstruct every result?',
['Assemble a ledger separating input, definition, derivation and source status.','Retain approximation differences independently of channel residuals.','Reconstruct a report and identify unresolved source obligations.'],
'''The previous lessons provided all required computations. This final lesson introduces no new physical model. It joins the channel, source, composition, endpoint and history ledgers into a report that a classmate can check.''',
'''A reproducible report tells the reader what was supplied, which operation was applied and what remains unresolved. A measured value comes from an actual observation with acquisition provenance. No new empirical measurement is supplied here: y is synthetic. A source coefficient or witness is a number stated by a document and must retain its source and precision. A derived coefficient is the result of a declared calculation. An approximant is a convenient replacement accompanied by its exact difference. A model output is conditional on model inputs and conventions.

For the worked packet, record y=(2,3,6), channel order 1,2,3, the three rows of A_small, field R, Euclidean inner product and dimensionless units. Derived c=(7/3,10/3); represented=(7/3,10/3,17/3); retained r=(-1/3,-1/3,1/3). The normal check is (0,0), but it is not a substitute for r. Reconstruct each entry before making an interpretation.

Suppose you display c1 as 2.33. This is exactly 233/100 as a decimal approximant. The rounding closure is 7/3-233/100=(700-699)/300=1/300. Store that separately. If both coefficients are displayed as (2.33,3.33), the exact-minus-displayed vector is delta c=(1/300,1/300), whose represented-channel difference is A_small delta c=(1/300,1/300,1/150). Then y=A_small c_display+r+A_small delta c. Rounding information and the original syndrome account for different differences.

The source ledger should identify S02 M17’s matrix and stored renderer witnesses, the missing source L and W7, and S05 R029–R032’s application statuses. A source label such as exact_representation_theory remains an attributed status when the action matrices required for fresh replay are absent. The course has independently recomputed the finite examples; it has not loaded every physical definition body.

For the practice packet y=(1,2,3), report c=(1,2), represented=(1,2,3), r=(0,0,0). Add the negative-Q endpoint record from lesson 5 with its neutral complete-object convention, initial 5u, final 5.05u, delta m=-0.05u, stipulated conversion 10 E_unit/u and Q=-0.5 E_unit. Attach the R029 row showing unsupplied atomic coordinates. These separate records do not turn the synthetic channel into an isotope measurement.

> Report scope: Retain observations if any are later supplied, derived transforms, proposed mechanisms, established reference relations and unresolved inputs in separate fields. No outlier deletion, significance-based erasure or replacement of residual fields by scores is part of this course. Preserve source-local definitions and branches rather than harmonizing away their differences.

Before submitting, give a partner only the inputs and rules. Ask them to recompute a row, a signed residual and an endpoint difference. If the result requires guessing a unit, coefficient selection or source status, repair the earliest missing field. A compact report is successful when it is reconstructable, not when it hides the most information.''',
['Classify y=(2,3,6), source alpha, 7/3, 2.33 and the toy rendered mass.','Compute the approximation closure for 7/3 displayed as 2.33.','What is missing from a report containing only c and a residual squared length?','What must remain unresolved in the source-traced atomic row?'],
['Synthetic input; source witness; exact derived coefficient; decimal approximant; conditional synthetic model output. None is a newly measured physical value.','7/3-233/100=1/300; retain it separately from r1=-1/3.','The signed channel residual and its order/basis, plus any omitted input and decoder conventions. A scalar score cannot reconstruct y.','The unsupplied Cell3 address, typed additional fibers, isotope mass, graph data, charge/parity, binding residual, phase tensor and occupied-state rule; source L/W7 replay remains unloaded.'])

mapping=[]
for l in P['course_map']:
    a=l['teaching_anchor'];mapping.append([a['concept_id'],l['id'],a['explanation_id'],a['worked_example']['id'],a['guided_practice']['id'],a['diagnostic']['id'],l['later_use']])
    for s in a.get('supplemental_exercises',[]):mapping.append([s['concept_id'],l['id'],s['explanation_id'],s['worked_example_id'],s['prior_practice_id'],s['diagnostic_id'],{'C21.S01':'C21-CAP-09','C21.S03':'lesson-08; C21-CAP-11'}.get(s['concept_id'],l['later_use'])])
write('course-map.md','# '+P['topic']+' — course map\n\nEight lessons, 17 core periods of 55 minutes, followed by three capstone periods (20 periods total). Lesson boundaries retain the approved map; multi-session lessons separate new operations instead of compressing them into one period. All new matrix, eigenvector, graph-recognition and endpoint operations are bridged locally.\n\n'+table(['Lesson','Sessions','Dependency','Focus'],[[l['id'],l['teaching_anchor']['planned_periods'],'lesson-'+str(i).zfill(2) if i else 'signed arithmetic, fractions, linear equations',l['title']]for i,l in enumerate(P['course_map'])])+'\n\n## Coverage and backward links\n\n'+table(['Concept','Introduction','Explanation','Worked example','Practice','Diagnostic','Later use'],mapping)+'\n\n## Unit boundaries\n\nAfter lesson-02, require reversible three-channel reconstruction and the integer-lattice counterexample. After lesson-04, require exact row decoding, source-L distinction and dimensional rendering. After lesson-06, require composition invariance, endpoint conventions and source cards. After lesson-08, require complete report reconstruction. Each capstone task maps to an earlier answered practice in capstone.md.\n\n## Scope and assumptions\n\n'+ '\n'.join('- '+s for s in P['assumptions'])+'\n- Named earlier courses provide context; local bridges make finite core operations self-contained.\n- General representation theory, physical coefficient selection and unprovided phase tensors are recognition/retrieval boundaries, not assigned computations.\n- Source mathematical M17 requires M05 and M11; this course teaches the finite prerequisites needed for its explicit decoder, without treating compiler module labels as the same module system.\n- No rounding half-tie, Cell3 coordinate ownership, gauge permutation or metric substitution is used in the core arithmetic. Their source conventions remain unchanged in the input contract.\n')

terms=[
('Channel','An ordered linear recipe for coefficients; one row of A.','01'),('Tuple/vector','An ordered list; operations are entrywise unless a dot product is stated.','01'),('Matrix A_small','The 3 by 2 classroom channel table [[1,0],[0,1],[1,1]].','01'),('A','The ordered 13 by 6 M17 matrix; never a chemical label within a matrix equation.','03'),('c, cj','Coefficient vector and its jth entry; dimensionless in exercises.','01'),('y','Full ordered input vector; synthetic throughout the numerical exercises.','01'),('r or s','Full signed channel residual y-Ac; s is used for M17 syndrome.','01,03'),('Transpose A^T','The matrix formed by turning columns into rows.','01'),('Euclidean inner product','Sum of entrywise products; declares the decoder geometry.','01'),('Normal residual','A^T r, a set of column-dot-product constraints; not the full r.','01'),('Rank','Number of independent column directions over the specified scalar field.','02'),('Image / kernel','Outputs a map can produce / inputs it sends to zero.','02'),('R / Z','Real-number field / integers. Bold or contextual R for reals is separate from projector R.','R: 01; Z: 02'),('Syndrome','Residual coordinates retained outside the represented image under a declared decomposition.','02'),('Lattice / saturation','Integer column combinations / containing all integer points of its real span.','02'),('G=A^T A','Decoder Gram matrix only; distinct from all Cell3 and phase metrics.','03'),('Eigenvector / eigenvalue','A direction a linear map only scales / the scale factor.','03'),('Aplus','(A^T A)^(-1)A^T for this full-column-rank Euclidean decoder.','03'),('P / R=I-P','Represented-channel projector / complementary residual projector.','03'),('L_int','Derived 6 by 13 integer extractor with L_int A=I6; not source L.','03'),('Source L','Missing 7 by 13 syndrome matrix with LA=0; VERIFIED_NOT_LOADED.','03'),('W / W7','Explicit toy four-character table / missing ordered source seven-character replay object; do not equate them.','03'),('Representation / intertwiner','Declared group actions / a map respecting those actions; equality of dimensions supplies neither.','03'),('b / b_toy','Source renderer order (1,alpha,alpha²,alpha³,a_e,eta) / separately stipulated toy values.','b: 03 (rendering 04); b_toy: 04'),('m_e / m_ref','Source reference mass / synthetic reference mass. Neither value is inferred from a dimensionless ratio.','04'),('V','Nominal composition label 12C+H+14N+16O, not geometric volume or exact isotope mass.','05'),('C,H,N,O','Ordered nonnegative atom counts for composition endpoints.','05'),('U1,U2,U3,K','Stated signed composition moves; U3=U1+U2, K is independent.','05'),('Fiber','Inputs sharing a specified output; the map and domain must be declared.','05'),('Isotope / isomer','Same element with different neutron count / same molecular formula with different arrangement.','05'),('A+B → AB','Synthetic conserved constituent labels, distinct from matrix A.','05'),('u / E_unit','Stipulated synthetic mass / energy units; 1u c_light²=10 E_unit is a toy conversion.','05'),('Q_release / delta m','Released-energy convention / initial minus final complete-object mass.','05'),('c_light','Speed factor in the declared mass-energy reference relation; distinct from coefficient c.','05'),('Graph / spectrum','Vertices and edges with identity / eigenvalue list that need not uniquely identify the graph.','06'),('QPC phase tensor','Source-local requested coordinate not supplied here; recognition-only.','06'),('t / n / c_star','Solver step parameter / update index / exact decoder coefficient target.','07'),('Approximant / closure','Displayed replacement / exact original-minus-replacement difference.','08'),('M_cell / R_cell / G_phase','Cell3 Gram metric / its inverse / distinct phase metric; no numerical use or substitution in this course.','source contract'),('O_K / B','Declared physical origin / locked ordered source basis, unused in classroom channel arithmetic.','source contract')]
write('terminology.md','# Terminology and notation\n\nSymbols are local to their declared object. In particular c_light is not c, V is not a geometric volume, and the decoder G is not a Cell3 metric.\n\n'+table(['Term','Meaning and scope','First lesson'],terms))

source_rows=[]
for s in V['sources']:source_rows.append([s['id'],s['path'],s['sha256']])
write('sources.md','# Compact source provenance\n\nAll five supplied files were read-only hash-verified against input-contract.json. No bulk source snapshots were written. The exact small M17 matrix is reproduced as the instructional object. Hash verification establishes file identity, not every claim’s truth.\n\n'+table(['ID','Absolute source path','SHA-256'],source_rows)+'''\n\n## Pointers actually used

| Source and pointer | Evidence class / use |
| --- | --- |
| S02 /backbone_sequence/16 | M17 definition and source-reported decoder proof; exact A, ordered b, rank statement, renderer scope and displayed alpha/eta witness values. Matrix identities independently recomputed. Requires M05 and M11. |
| S02 /branch_proofs/11 | BR-11 endpoint reported closed_exact_module_compatibility; no promotion to a freshly replayed physical map. |
| S02 /proof_nodes/10 | KFM-X039 reported exact_integer_linear_algebra; real dimension argument distinguished from integer saturation. |
| S02 /proof_nodes/11 | KFM-X040 reported character orthogonality; exact source W7 ordering not loaded. |
| S02 /proof_nodes/23 | KFM-X041 reported representation compatibility and noncanonical guard. Numeric character arithmetic checked conditionally; actions not replayed. |
| S03 /findings/8 | AUD-009 missing replay objects, including source L and W7; source gate VERIFIED_NOT_LOADED retained. |
| S05 /records/7 | R008 archive_stated nominal composition map. |
| S05 /records/21 | R022 synthesis: three tested moves span rank two. |
| S05 /records/22 | R023 synthesis: independent 4C-to-3O direction and stored 15.25614129 mDa claim. Nominal invariance checked; isotope-mass claim not freshly replayed. |
| S05 /records/28 | R029 synthesis of a periodic-coordinate package. |
| S05 /records/29 | R030 mechanism synthesis of typed binding edges. |
| S05 /records/30 | R031 archive_stated unresolved isomer/graph/binding coordinates. |
| S05 /records/31 | R032 synthesis comparing three rank-three structures with canonical map unresolved. |

S01 and S04 are retained as provenance branches and hash-verified; no lesson silently substitutes their values for the mature S02 M17 definition. The source-local JSON statuses remain attributed. No compiler integration status is inferred from mathematical module numbers.

## Graph capability check and freshness boundary

The read-only krytronx_capabilities call was performed at production start. It returned the finite read-only interface and canonical application digest 88c14424210ac18e902f33f5330a208a1c547a0e1d763a6b941c3e9de7c812ac. That response did not expose a live corpus generation or manifest digest. The packet pins generation/manifest 5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7; live-generation equality is not claimed. Exact grounding here uses the supplied read-only archival paths and verified file digests rather than graph labels.

## Freshly checked and unresolved

verify_examples.py uses standard-library exact rational arithmetic in tf_gpu_env. verification.json stores the 13-entry worked and practice ledgers, Gram matrix, integer extractor, Walsh exercise, full finite iteration traces and source hashes. These are compact teaching computations, not raw experimental data.

Unresolved source obligations: original L and W7 with ordering/actions; full occupied-state selection and a_e definition inputs; physical m_e and endpoint constants if a physical mass calculation is requested; isotope constants and endpoint conventions for R023’s stored mass-step claim; R032’s canonical map. These are explicit boundaries of the completed finite course, not hidden numerical assignments.
''')

tasks=[
('Use A_small and synthetic y=(1,2,3). Write all three channel equations, solve the normal equations, and save the full residual.', 'A_small=[[1,0],[0,1],[1,1]]; c1=1,c2=2,c1+c2=3. Normal equations 2c1+c2=4, c1+2c2=5 give c=(1,2). Ac=(1,2,3), r=(0,0,0), y=Ac+r. All inputs are dimensionless synthetic values.'),
('Use A_small and y=(1,1,3). Separate c and t, reconstruct every channel, and prove integer image/kernel equality for A0=(1,0)^T, L0=(0,1). Contrast the even-column counterexample.', 'c=(4/3,4/3), t=1/3, r=(-1/3,-1/3,1/3), Ac=(4/3,4/3,8/3). Adding gives (1,1,3); A_small^T r=(0,0). Every integer kernel point of L0 is (n,0)=A0 n. Replacing A0 by (2,0)^T misses (1,0), despite the same real rank.'),
('Using the source A printed in lesson-03, form y from c0=(1,-1,2,0,1,0) and s=(-2,-2,1,1,0,0,0,0,0,0,0,0,0). Verify perpendicularity and explain the six-plus-seven count and missing-source boundary.', 'Ac0=(2,-1,1,1,1,4,2,0,3,1,0,3,1); y=(0,-3,2,2,1,4,2,0,3,1,0,3,1). The first coefficient-column dot s is 0; the second is -2+1+1=0; the third is -2+1+1=0; columns 4 and 5 give 0; column 6 gives 1-1=0. Hence the Euclidean decoder returns c0 and this full s. Six represented directions leave seven independent syndrome directions stored in thirteen constrained entries. L_int is not the missing source L or W7.'),
('Use the lesson-04 toy b=(1,1/10,1/100,1/1000,1/5,2), c=(0,2,0,0,1,0), m_ref=2 mass units and s=0. Render mass and reconstruct the source-A channel packet. State the boundary for source b.', 'Ratio=2/10+1/5=2/5; m=(2)(2/5)=4/5 mass units. Ac=(0,2,2,2,0,1,-1,2,3,1,2,3,1); s=(0,0,0,0,0,0,0,0,0,0,0,0,0). This is synthetic; source b still requires its own occupied-state inputs and reference mass. A scalar mass does not preserve arbitrary s.'),
('For complete neutral synthetic objects A=2u, B=3u, AB=5.05u, keep conserved constituent labels A and B and unchanged isotope convention. Use 1u c_light²=10 E_unit. Compute signed Q and separately V for (4,4,0,1). Identify an electron-convention error that would block this subtraction.', 'Initial and final inventories are one A label and one B label; charges are 0+0=0. Complete-object masses include electrons and the declared binding/reference states. Delta m=5-5.05=-0.05u, Q=-0.5 E_unit, requiring input 0.5 E_unit. V=48+4+16=68 nominal units. Comparing a bare final ion with neutral initial masses without accounting for the removed electron makes the endpoint incomplete.'),
('Complete an R029/R030/R031/R032 source row for (4,4,0,1), then repeat the neutral synthetic reaction with AB=4.8u. Identify supplied values, proposed mechanisms and unresolved information.', 'Counts and derived V=68 are supplied; address, scale/face, lambda, chosen composition coordinates, isotope mass, graph identity/spectrum, charge/parity, binding residual, phase tensor and selected physical c are not. R029 is coordinate synthesis; R030 is typed-edge mechanism synthesis; R031 is archive_stated unresolved isomer information; R032 leaves a canonical map among three rank-three structures unresolved. Delta m=0.2u, Q=2 E_unit with the declared conversion. Neither the source synthesis nor this arithmetic supplies a physical coefficient-selection rule.'),
('For A_small and y=(2,3,6), start c0=0 and take t=1 in c_next=c+t A_small^T(y-A_small c). Save two updates, each full residual and normal residual. Explain the failure and reconstruct y at the second step.', 'At n=0, r=(2,3,6), g=(8,9). At n=1, c=(8,9), r=(-6,-6,-11), g=(-17,-17). At n=2, c=(-9,-8), r=(11,11,23), g=(34,34). Reconstruction is (-9,-8,-17)+(11,11,23)=(2,3,6). The nonzero sum-error component has multiplier -2, so it alternates and grows. Retain this failed parameter branch; the exact target still has nonzero channel residual.'),
('Assemble the y=(1,2,3) decoder report, the negative-Q endpoint ledger and source row from tasks 5–6. Separately classify 7/3 displayed as 2.33 and retain its closure.', 'Record synthetic input y, A_small, channel order, R field, Euclidean metric, dimensionless units, exact c=(1,2), Ac=y, full r=(0,0,0), and normal check (0,0). Attach all endpoint inputs from task 5 and source pointers/statuses from task 6. In a separate approximation illustration, 7/3-233/100=1/300. Source alpha is a witness, 7/3 a derived coefficient, 2.33 an approximant, and a rendered toy mass a model output; no new measured value is present.'),
('Use the explicit four-character W in lesson-03 on v=(2,0,0,2). Compute a=W^T v/4 and reconstruct. Verify the swap intertwiner for rho=diag(1,-1), sigma=diag(-1,1), and explain nonuniqueness and the source boundary.', 'W^T v=(4,0,0,4), a=(1,0,0,1), Wa=(2,0,0,2). T=[[0,1],[1,0]] gives T rho=sigma T=[[0,-1],[1,0]], determinant -1; it is invertible. 2T also intertwines, so compatibility does not select a unique T. The toy W does not load source W7, L or their action/order conventions.'),
('Apply U2=(1,4,0,-1) to (4,4,0,1) and K=(-4,0,0,3) to (4,0,0,0). Verify nominal invariance and nonnegative endpoints, U3=U1+U2, and independence of K. State the R023 and R032 boundaries.', 'The first endpoint is (5,8,0,0), V=60+8=68, matching 48+4+16. The second is (0,0,0,3), V=48, matching 12 times 4. All counts are nonnegative. U1=(-1,-2,1,0) plus U2 gives (0,2,1,-1)=U3. In K=aU1+bU2, N forces a=0 and H forces b=0, contradiction. R023’s 15.25614129 mDa is attributed synthesis with isotope replay inputs missing. R032 has no canonical map. These count moves are not asserted physical carbon-to-oxygen reactions.'),
('Repeat the same neutral reaction with AB=5.05u. In a separate positive release example, 2 E_unit is delivered over 4 time units with recovered fraction 1/2. Compute signed Q and recovered mean power, and state which premises are extra.', 'For the negative branch delta m=-0.05u and Q=-0.5 E_unit, requiring input. Separately, recovered energy=(1/2)2=1 E_unit and mean recovered power=1/4 E_unit per time unit. Duration and recovery fraction are extra premises; endpoint mass difference alone supplies neither rate nor recoverable power.')]
cap='# Capstone: a reconstructable decoding report\n\nThree 55-minute sessions, 44 points. Session 1: input ledger, decoder tasks 1–4. Session 2: composition, sources and energy tasks 5–6 and 10–11. Session 3: solver, report and compatibility tasks 7–9; partner reconstruction and repair. Use the printed lessons and source cards. No external measurements, constants or missing source matrices are required. All numerical channel and reaction inputs are synthetic.\n\n## Student tasks\n\n'
for i,(q,ans) in enumerate(tasks):
    b=P['capstone_specification']['backward_map'][i]
    cap+='### '+b['step_id']+' — 4 points\n\n'+q+'\n\nPreparation: ['+b['introduction']+']('+b['introduction']+'.md), '+b['explanation_id']+'; answered practice '+b['prior_practice_id']+'.\n\n'
cap+='## Full answer key\n\n'
for i,(q,ans) in enumerate(tasks): cap+='### C21-CAP-'+str(i+1).zfill(2)+'\n\n'+ans+'\n\n'
cap+='''## Rubric

Each task earns four independent points: one for declared inputs and scope, one for the correct operation, one for complete reconstruction or accurate source classification, and one for retained information and the boundary. Award demonstrated points even when another part is wrong; use the full key above for task-specific evidence. Total: 11 times 4=44.

For tasks 1–4 and 7, the reconstruction point requires every requested component, not a residual score. For tasks 5, 6 and 11, an inconsistent electron/reference convention loses the input point and must be repaired before the energy result is accepted as that endpoint’s answer. For tasks 6 and 10, a source-reported status presented as fresh physical verification loses the classification point. For task 9, equal dimension without the actual product check does not earn the operation point. For task 8, mixing rounding closure with channel residual loses the retained-information point.

Before advancing, repair any missing full residual, invented source coefficient selection, absent endpoint convention or unexplained source promotion, regardless of total score. A student can earn arithmetic credit and still need conceptual repair. Corrections retain the original attempted calculation and identify what changed.
'''
write('capstone.md',cap)

teacher='# Teacher guide\n\nAudience: high-school seniors comfortable with signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs. No calculus, abstract algebra or prior university linear algebra is assumed. The earlier course references are contextual; local finite bridges teach every assessed operation.\n\n## Session plan\n\n'
for l in P['course_map']:
    teacher+='### '+l['id']+' — '+l['title']+'\n\n'
    teacher+='\n'.join('- Session '+str(s['session'])+': '+s['focus']+'.' for s in l['teaching_anchor']['session_sequence'])+'\n\n'
teacher+='''Each period uses 5 minutes for prerequisite retrieval, 20 for explanation and a worked example, 15 for guided practice, and 15 for independent diagnostics and repair. Allow an additional period if learners cannot reconstruct the previous packet; retain all eight conceptual lessons and record the extension in the class pacing log. The approved baseline is 17 core periods plus 3 capstone periods.

## Teaching moves and readiness checks

In lesson 1, have students write the three equations before using the matrix symbol. Check fraction subtraction individually. Ask pairs to reconstruct all three channels, then explain why a scalar residual score is insufficient. In lesson 2, draw a horizontal line and mark integer points; highlight that the even lattice misses odd points. Do not assume students know vector spaces from the word alone.

Lesson 3 is the highest-load block. Session 1 begins with e1 column selection, then two column dot products, then the explicit six-equation decoding recipe. Split the thirteen ledger rows across pairs and require each pair to return both predicted and residual entries. The provided exact ledger is a checking aid, not a memorization target. Session 2 handles integer extraction and saturation using the six explicit recipes. Session 3 teaches the four-label table (two bits per label), one orthogonality check and the concrete swap intertwiner. General S3 representation theory is recognition-only; students are assessed on the small table and explicit action products.

At the lesson-04 boundary, ask whether a mass scalar can reconstruct a changed syndrome. If students say yes, use identical c with two distinct s packets. Keep source b and toy b on separate cards. A missing a_e does not authorize a guessed value. No physical occupied-state coefficient selection is assessed.

Lesson 5 introduces chemistry vocabulary before applying moves. Check each endpoint for nonnegative counts separately from the weighted-sum test. Have students physically cross off matching synthetic A and B labels on each side of the reaction. Charge and whole-object mass state must be stated before subtraction. If neutral and ionic conventions are mixed, preserve the attempted ledger and mark what additional objects/states are needed.

Lesson 6 uses source cards as a reading exercise. A blank field means not supplied, not zero. Students need not construct a phase tensor or compute a graph spectrum: these are requested source coordinates whose absence must be tracked. They must distinguish mechanism synthesis from checked nominal arithmetic. Keep the synthetic reaction labels separate from the CHNO composition row.

Lesson 7 compares step parameters using exact fractions. Each iteration row includes all three residual entries and both normal sums. A divergent branch is valid saved information about the algorithm and parameter. Lesson 8 asks partners to recreate a result from the report alone. Demand separate rounding closure, channel syndrome and source retrieval gaps.

## Common errors and targeted repair

| Observed error | Repair task |
| --- | --- |
| Three channels means three coefficients | Rebuild y=(c1,c2,c1+c2), count free inputs, then derive residual t. |
| Zero normal residual means no residual | Substitute (-1/3,-1/3,1/3) into both dot products and reconstruct y. |
| Rank proves integer equality | Show (1,0) missing from integer multiples of (2,0). |
| L_int is the source L | Compare shapes and products: 6 by 13/identity versus 7 by 13/zero. |
| Equal rank proves physical identity | Ask for an explicit typed map and the actions it preserves. |
| Nominal V is exact mass or isomer identity | Compare two different nonnegative formulas with V=68 and list unresolved isotope/structure fields. |
| Positive Q gives power | Request duration and recoverable fraction, then compute units. |
| Failed solver values should be removed | Reconstruct y from the divergent second iterate and full residual. |

## Assessment and recovery

Use the answered diagnostics after each session sequence. At unit boundaries (02,04,06,08), recompute one previous example without its answer and check terminology and source layers. An incorrect response is retained alongside its correction. Do not grade a missing definition as student failure; reteach the earliest dependency. Capstone operations all have earlier named explanations, worked examples and answered practices in course-map.md. The answer key and 44-point rubric are in capstone.md.

## Reproducibility and authority

Run verify_examples.py with the explicitly selected tf_gpu_env; it reads sources and writes only compact verification.json in this course directory. The validator adapter path is supplied in the production contract. No package installation, physical-data copying or source mutation is needed. Markdown tables and fenced matrices are the delivery format; no paginated artifact is requested. Source paths, hashes and scope are in sources.md. Formal-looking archival statuses remain attributed when replay objects are absent.
'''
write('teacher-guide.md',teacher)
write('course.md','# '+P['topic']+'\n\nStudent course, approved lesson order. Supporting material: [glossary](terminology.md), [capstone](capstone.md), [sources](sources.md), [teacher guide](teacher-guide.md).\n\n'+'\n\n'.join('<!-- BEGIN: '+k+' -->\n'+v+'\n<!-- END: '+k+' -->'for k,v in lessons.items()))
