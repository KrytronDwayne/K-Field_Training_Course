"""Authoring/recovery helper. All writes remain beside this script."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
def write(name,text): (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8')
def dump(name,obj): write(name,json.dumps(obj,indent=2,ensure_ascii=False))
def digest(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
LESSONS={}
LESSONS['lesson-01']=r'''
# Lesson 1 — Logarithms as ratio coordinates

Essential question: How can multiplication become addition without losing the original areas?

Goals: convert positive ratios to logarithms; reconstruct areas from logs and a reference; distinguish physical scaling from changing the reference.

Bridge: You already multiply fractions, use powers, and solve equations. A face is the parallelogram spanned by two edges. Its area scales by the product of their length factors when their included angle stays fixed. Doubling both edges therefore multiplies area by four. We use signed numbers to record decreases as well as increases.

## C10.01-E1 — A coordinate for multiplication

The exponential function exp(x), also written e^x, extends powers of the positive number e (approximately 2.71828) to real exponents. It satisfies exp(x+y)=exp(x)exp(y), exp(0)=1, and always has positive output. The natural logarithm ln is its inverse: ln(r) is the unique exponent whose exponential is r. Thus exp(ln r)=r for r>0 and ln(exp x)=x. A negative log means a positive ratio below one; it does not mean a negative area.

We can work exactly without a calculator. Write L=ln 2. Then exp(L)=2, exp(2L)=4, ln(1)=0, and ln(1/2)=-L. Since multiplication of exponentials adds exponents, ln(rs)=ln r+ln s. Division subtracts: ln(r/s)=ln r-ln s. These rules require positive r,s. We do not use ln(r+s)=ln r+ln s: for r=s=1 the left side is L and the right side is zero.

An area has units. First choose ONE positive reference area A0 in the same units as all three faces. For example A0=1 LU², where LU means a declared laboratory length unit in our synthetic examples. Define the ordered triple

    y=(ln(A_ab/A0), ln(A_ac/A0), ln(A_bc/A0)).

The subscripts name faces, and the order is always [ab,ac,bc]. Each quotient and each log is dimensionless. A triple is simply three ordered numbers; its first entry is not interchangeable with its third. Inversion is component by component: A_ab=A0 exp(y_ab), and similarly for ac and bc. Store A0 with y.

If all edge lengths are multiplied by a positive factor rho at fixed angles, all areas multiply by rho². Thus every y entry increases by 2 ln rho. If instead the physical areas stay fixed and A0 changes to k A0, every y entry decreases by ln k. These operations can look similar in coordinates, but their physical records differ.

## C10.01-W1 — Worked synthetic example

Let A/A0=(1,4,8). The logs are y=(0,2L,3L), since 4=2² and 8=2³. Double all edges: rho=2, so the new area ratios are (4,16,32). Adding 2L to every old entry gives (2,4,5)L, agreeing with those powers of two. Reconstruct the original third face: A_bc=A0 exp(3L)=8A0. Both the old and new triples remain available.

## C10.01-P1 — Practice before checking the answer

Use A/A0=(2,4,16). Find y, halve every edge, find the new areas and logs, then reconstruct all original ratios. Also change only the reference to 4A0 and explain what changed physically.

Answer: y=(1,2,4)L. Halving edges multiplies areas by 1/4, giving (1/2,1,4)A0 and logs (-1,0,2)L. Applying exp to the original entries gives (2,4,16). Changing only the reference to 4A0 gives the same numerical log triple (-1,0,2)L, but the physical areas remain (2,4,16)A0 because the reconstruction reference is now 4A0. Record which operation occurred.

> Claim scope: The log laws are mathematical identities. All numerical areas here are synthetic. S02#/backbone_sequence/6 uses dimensional-log shorthand; the common A0 makes its intended ratio coordinates explicit, following SA-10. No measurement or force law is inferred.

## Diagnostic checks — C10.01-D1

1. Can a zero area be represented by a finite real log? What about a negative area?
2. What is ln(8/4), and why?
3. If A0 is replaced by 4A0, what happens to y_ac-y_ab?
4. A report stores y but omits A0. What can and cannot be recovered?

Worked answers: (1) Neither is in the positive domain; exp never gives zero or a negative value. (2) ln 2=L, also 3L-2L=L. (3) Each entry loses 2L, so their difference is unchanged. (4) Ratios between faces follow from exp(y_i-y_j). Absolute dimensional areas require the reference.

Next: [Lesson 2](lesson-02.md) separates the common shift from differences. Pacing: 55 minutes = 5 retrieval + 20 teaching/example + 15 practice + 15 diagnostics/repair.
'''
LESSONS['lesson-02']=r'''
# Lesson 2 — One scale coordinate and two shape coordinates

Essential question: Which parts of three area logs change under a common scaling?

Goals: calculate mean and zero-sum shape; compute normalized projection coefficients; reconstruct all three logs and areas; state the limits of area shape.

Bridge: Lesson 1 made each face area a dimensionless log. Common scaling adds the same number to all entries. We now separate that shared part without discarding it.

## C10.02-E1 — Mean, projection, reconstruction

For y=(y_ab,y_ac,y_bc), define m=(y_ab+y_ac+y_bc)/3 and z=y-m(1,1,1). Subtract m from each entry. The three entries of z add to zero, so only two are free: knowing z_ab and z_ac fixes z_bc=-z_ab-z_ac. Keep m as a primary coordinate. Reconstruction is y=m(1,1,1)+z. The word reduction means separating coordinates here, not deleting m.

We also use the exact normalized source coordinates. The dot product of (p,q,r) and (h,j,k) is ph+qj+rk. The squared length of a triple is its dot product with itself. Dividing a vector by the positive square root of its squared length gives length one: (1,1,1)/sqrt(3) has squared length 3/3=1. Square roots need not be decimals; sqrt(2)sqrt(2)=2.

Define

    e_s=(1,1,1)/sqrt(3),
    e_u=(-1,1,0)/sqrt(2),
    e_v=(-1,-1,2)/sqrt(6).

Their squared lengths are 3/3, 2/2, and 6/6. Each pair has dot product zero: the numerators are -1+1+0=0, -1-1+2=0, and 1-1+0=0. This is what orthonormal means: perpendicular unit vectors. A projection coefficient is a dot product with a unit vector. Set s=y dot e_s, u=y dot e_u, v=y dot e_v. Then

    s=(y_ab+y_ac+y_bc)/sqrt(3)=sqrt(3)m,
    u=(-y_ab+y_ac)/sqrt(2),
    v=(-y_ab-y_ac+2y_bc)/sqrt(6),
    y=s e_s+u e_u+v e_v.

Why does this recover y? Taking a dot product of the last expression with e_u returns u: its other two terms vanish. The three displayed independent directions cover triples, and direct substitution gives each original entry. In particular

    y_ab=s/sqrt(3)-u/sqrt(2)-v/sqrt(6),
    y_ac=s/sqrt(3)+u/sqrt(2)-v/sqrt(6),
    y_bc=s/sqrt(3)+2v/sqrt(6).

The source writes mean removal as P_H=I-(1/3)11^T. Here I leaves a triple unchanged; 1=(1,1,1)^T is a column; superscript T turns a column into a row. Multiplying 11^T by y gives the sum of y in each entry. Thus P_H y=z. You can always use subtraction instead of matrix notation.

Adding c to every entry changes m by c and s by sqrt(3)c; it leaves u,v unchanged. The pair (u,v) describes three positive face areas modulo a common area factor. It is called the area-shape fiber (source label A2). It does not encode all possible changes of edge angles. Keep the actual basis or angle information when those are needed.

## C10.02-W1 — Worked synthetic example

For y=(0,2,3)L, m=5L/3 and z=(-5,1,4)L/3. Projection gives s=5L/sqrt(3), u=2L/sqrt(2)=sqrt(2)L, and v=4L/sqrt(6). Reconstruct y_ab: (5/3-1-4/6)L=0; y_ac=(5/3+1-4/6)L=2L; y_bc=(5/3+8/6)L=3L. The sum of z is (-5+1+4)L/3=0. Doubling edges adds 2L to y, so s gains 2sqrt(3)L; u,v do not change.

## C10.02-P1 — Practice

Project y=(1,2,4)L into both representations. Rebuild each log and the areas. Verify e_u dot e_v and both unit lengths. Describe halving all edges.

Answer: m=7L/3, z=(-4,-1,5)L/3, s=7L/sqrt(3), u=L/sqrt(2), v=5L/sqrt(6). The reconstructed coefficients are 7/3-1/2-5/6=1; 7/3+1/2-5/6=2; 7/3+10/6=4. Thus areas are (2,4,16)A0. The dot product is (1-1)/sqrt(12)=0; norms squared are 2/2 and 6/6. Halving edges subtracts 2L from m and 2sqrt(3)L from s, leaving z,u,v fixed.

> Claim scope: S02#/backbone_sequence/6 supplies these directions and the common-scaling argument. The completeness claim here concerns area ratios. Recovering edge ratios additionally uses fixed nondegenerate angles, taught in Lesson 5.

## Diagnostic checks — C10.02-D1

1. Is s=m? 2. If z=(2,-5,w), find w. 3. Can u,v alone recover dimensional areas? 4. Do these two numbers describe arbitrary shear of a cell?

Worked answers: (1) s=sqrt(3)m, so generally no. (2) 2-5+w=0 gives w=3. (3) No: s or m and A0 must also be retained. (4) No: changing included angles adds geometry beyond the three area logs modulo scale.

Next: [Lesson 3](lesson-03.md) treats ordered coefficient maps. Two 55-minute periods: first mean/removal, second normalized projections; each uses 5 retrieval + 20 teaching + 15 practice + 15 checks.
'''
LESSONS['lesson-03']=r'''
# Lesson 3 — Linear response and small changes

Essential question: When does reversing a coefficient map differ from reversing a finite physical change?

Goals: apply and invert a two-variable matrix; identify a tangent coefficient; calculate and preserve a finite remainder.

Bridge: A dot product multiplies corresponding entries and adds. A matrix is a rectangular table whose rows do that calculation to an input column. We will start with two inputs before the three-input Jack map.

## C10.03-E1 — Exact linear maps and local predictions

Let H have rows (1,1) and (1,-1). Applied to input (p,q), its output is (h,k)=(p+q,p-q). Add the two output equations: h+k=2p. Subtract them: h-k=2q. Hence p=(h+k)/2, q=(h-k)/2; the inverse table is H/2. An inverse is a rule that restores every permitted input, not just a remembered example. Substitution gives ((p+q)+(p-q))/2=p and ((p+q)-(p-q))/2=q.

This linear map is exact for any real p,q. A *Jacobian* is a table of such response coefficients at a stated starting point for a possibly nonlinear map. To understand 'local', use a dimensionless change parameter t, initially zero. If f(t)=f(0)+ct+R(t), and R(t)/t approaches zero as nonzero t approaches zero, c is the derivative or tangent coefficient at zero. The predicted change is ct. This definition compares the remainder with the change parameter; it does not authorize throwing R away. Here our polynomial examples let us check it by division.

For example, (1+t)(1+2t)=1+3t+2t². The change from its initial value 1 is 3t+2t². Its tangent part is 3t because (2t²)/t=2t approaches zero. At any specified nonzero t, retain the exact remainder 2t². The exact output is recovered as baseline + tangent prediction + remainder. This is a finite synthetic product model, not a measured cell response.

For a positive length l(t)=l0(1+ct), the exact log change is ln(l(t)/l0)=ln(1+ct). Its tangent is ct at t=0 (the local log rule ln(1+h)/h approaches 1). This is a supplied elementary log property; a general calculus proof is not needed for the computations. The symbol dln l denotes this first-order change, not the exact percentage or the finite log. Keep ln(1+ct)-ct when comparing them. For a log-defined path l(t)=l0 exp(ct), the log change is exactly ct, a different path that must be declared.

## C10.03-W1 — Worked synthetic examples

Input (2t,t) goes through H to (3t,t). Applying H/2 returns ((3t+t)/2,(3t-t)/2)=(2t,t). This reversal has zero residual for every t.

Separately, at t=1/10 the product (1+t)(1+2t)=1.1 times 1.2=1.32. Change=0.32, tangent=0.30, remainder=0.02. Reconstruct 1+0.30+0.02=1.32. Halving t to 0.05 gives remainder 2(0.05)²=0.005; it becomes smaller but remains part of the record.

## C10.03-P1 — Practice

Apply H to (t,-2t) and invert. For the separate square model (1+t)², find exact change, tangent, remainder at t=0.1, and the exact log change. Find the log remainder for a single 10% increase and retain its sign.

Answer: H(t,-2t)=(-t,3t); inverse gives ((-t+3t)/2,(-t-3t)/2)=(t,-2t). Expansion gives 1+2t+t²: change 0.21, tangent 0.20, remainder 0.01. The exact square log change is 2ln(1.1), approximately 0.19062036, not 0.20. For a single increase it is ln(1.1), approximately 0.09531018; subtracting 0.1 gives approximately -0.00468982. These decimals are calculator approximations; the exact logarithmic expressions retain all information.

> Claim scope: H and the product/square are declared classroom models. They explain what 'tangent' means before the source map. A small finite remainder is preserved, not erased by a tolerance or a label.

## Diagnostic checks — C10.03-D1

1. Is ln(1.1)=0.1? 2. If H has input (3,2), recover it from its output. 3. In the product example, what is R(t)/t? 4. Does zero linear inverse residual imply zero nonlinear remainder?

Worked answers: (1) No; the retained difference is ln(1.1)-0.1. (2) Output (5,1); ((5+1)/2,(5-1)/2)=(3,2). (3) 2t for t nonzero; it approaches zero. (4) No. The inverse tests a coefficient map, while the remainder tests a finite approximation; they answer different questions.

Next: [Lesson 4](lesson-04.md) names the source inputs and outputs before using a Jacobian. Two periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks: first exact two-variable maps, then local versus finite changes.
'''
LESSONS['lesson-04']=r'''
# Lesson 4 — The Jack map and its inverse

Essential question: Which three output changes recover three coherent edge-scale changes?

Goals: derive the rows of the fixed-angle map; apply its inverse; check its determinant and ordered units; distinguish scalar coordinates from dynamics.

Bridge: Lesson 3 taught row-by-column multiplication and inversion by equations. Now each entry has a specific source meaning. Use positive edge lengths l_a=|a|, l_b=|b|, l_c=|c| and fixed included angles. Vertical bars mean length here. 'Coherent' means the same three edge changes generate all three face changes.

## C10.04-E1 — Source card and derivation

For two edges, area is base times perpendicular height: A_ab=l_a l_b sin(theta_ab). The sine factor is height divided by the second edge length; it equals 1 for perpendicular edges. This course supplies each angle factor rather than requiring trigonometric calculation. Nondegenerate faces have positive sine factors. The same area rule holds for ac and bc.

With angles fixed, the exact log-area change is the sum of the two exact log-length changes. Its tangent form is

    dln A_ab=x_a+x_b, dln A_ac=x_a+x_c, dln A_bc=x_b+x_c,
    x=(x_a,x_b,x_c)=(dln l_a,dln l_b,dln l_c).

All log changes mean logs of ratios to the same starting quantity; they are dimensionless. S02 M05 defines eta=1000 A_bc/A_ab and alpha_inverse=100 A_bc/A_ac. Here alpha_inverse=1/alpha, so alpha=A_ac/(100 A_bc). Constants vanish from changes of logs. Therefore

    dE=dln eta=dln A_bc-dln A_ab=-x_a+x_c,
    dA=dln alpha=dln A_ac-dln A_bc=x_a-x_b.

Important local notation: dA is the output dln alpha, NOT an area change. The third output dG=dln Gamma2 is the source-named scalar coordinate. The explicitly identified M19 gravity_scalar_lift branch supplies

    dG=9 dln A_ab+8 dln A_ac-11 dln A_bc
      =9(x_a+x_b)+8(x_a+x_c)-11(x_b+x_c)
      =17x_a-2x_b-3x_c.

Thus the Jack matrix is

    J = [ -1   0   1 ]       output order [dE,dA,dG]
        [  1  -1   0 ]       input order  [x_a,x_b,x_c]
        [ 17  -2  -3 ],      output = J input.

Every coefficient is dimensionless. Read one row at a time; do not swap eta and alpha. The M19 branch supplies this scalar relation only. Its name does not supply an equation of motion or a measured force.

Solve rather than memorize. First x_c=dE+x_a and x_b=x_a-dA. Substitute in the third equation: dG=17x_a-2(x_a-dA)-3(dE+x_a)=12x_a+2dA-3dE. Hence

    x_a=(dG-2dA+3dE)/12,
    x_b=(dG-14dA+3dE)/12,
    x_c=(dG-2dA+15dE)/12.

The nonzero coefficient 12 allows division and makes the solution unique. For a 3 by 3 matrix with rows (a,b,c),(d,e,f),(g,h,i), its determinant is a(ei-fh)-b(di-fg)+c(dh-eg). This scalar tests whether a square coefficient map has an inverse. Here it gives (-1)(3)-0+1(-2+17)=-3+15=12, not zero. This is the number twelve, not twelve factorial. Direct substitution of the inverse into each original equation verifies both directions; the determinant is an additional check.

## C10.04-W1 — Worked source-matrix, synthetic input

Let x=(1,2,3)t, a tangent vector with dimensionless parameter t. Jx gives (-1+3,1-2,17-4-9)t=(2,-1,4)t. Invert using (dE,dA,dG)=(2,-1,4)t: x_a=(4+2+6)t/12=t; x_b=(4+14+6)t/12=2t; x_c=(4+2+30)t/12=3t. The inverse residual, recovered minus supplied input, is (0,0,0).

## C10.04-P1 — Practice

Apply J to (2,-1,1)t. Recover the input from the output. Independently form the three area tangent changes and use 9,8,-11 to check the scalar output. Recompute the determinant using the displayed rule.

Answer: outputs are (-2+1,2+1,34+2-3)t=(-1,3,33)t. Inverse numerators are 33-6-3=24; 33-42-3=-12; 33-6-15=12. Dividing by 12 recovers (2,-1,1)t. Areas give (1,3,0)t, and 9(1)+8(3)-11(0)=33. Determinant: -3+15=12.

> Claim scope: S02#/backbone_sequence/6 gives J and its inverse; /backbone_sequence/4 defines eta and alpha; /backbone_sequence/18/branches/gravity_scalar_lift gives the scalar row. These are source formulas with fresh finite algebra checks. J reconstructs coherent fixed-angle tangent edge changes. If an angle varies, dln sin(theta) adds another term to the corresponding area change. J alone then cannot reconstruct arbitrary shear. No general finite Gamma2 response or force law is being asserted.

## Diagnostic checks — C10.04-D1

1. What does dA mean, and what would dln alpha_inverse equal? 2. Why can the equations be uniquely inverted? 3. What is missing if theta_ab changes? 4. Does a scalar named Gamma2 establish a force?

Worked answers: (1) dln alpha; dln alpha_inverse=-dA. (2) Elimination leaves 12x_a, and 12 is nonzero; x_b,x_c then follow. (3) dln sin(theta_ab), which must be retained as additional information. (4) No; the supplied relation defines scalar response, without force dynamics.

Next: [Lesson 5](lesson-05.md) places these outputs in a typed record. Two periods: source rows, then inverse and scope; each 5 retrieval + 20 teaching + 15 practice + 15 checks.
'''
LESSONS['lesson-05']=r'''
# Lesson 5 — The typed Devon object

Essential question: How can a reduced record preserve geometry, scale, shape, scalar response, and branch information?

Goals: compute a diagonal metric/cofactor/reciprocal example; decode admissible branch modes; recover positive edge scale from an area anchor; label each component and inverse.

Bridge: Lessons 2 and 4 separated shape/scale and reconstructed tangent changes. Neither result says that geometry and integer branch records become the same kind of object. A typed record tells us what each number belongs to, its units, order, domain, source, and reconstruction rule.

## C10.05-E1 — A record with distinct components

The source Devon object includes the direct metric, cofactors, reciprocal metric, common scale, A2 area-shape fiber, scalar lift, branch modes, and invertible maps. We compute small diagonal examples; recognition of the broader object does not require university matrix theory.

Let B=[a b c] be a table whose columns are three edge vectors. In Cell3 those columns use ICRS coordinates and intentional negative determinant. Our positive diagonal B below is explicitly a different synthetic box, not the locked Cell3 basis. A diagonal table diag(p,q,r) has p,q,r on its diagonal and zero elsewhere. A transpose B^T exchanges rows and columns. The metric M_cell=B^T B stores edge dot products: entry ij is edge i dot edge j. For a diagonal B, M_cell=diag(p²,q²,r²). It measures squared lengths and angles; its entries have units LU².

For a diagonal metric diag(m1,m2,m3), its determinant is m1 m2 m3 and its cofactor matrix is diag(m2 m3,m1 m3,m1 m2). A cofactor is the signed determinant after deleting one row and one column; in this diagonal case the remaining two diagonal numbers multiply, and off-diagonal cofactors vanish. Units are LU⁴. These metric cofactors are distinct from cofactors of B itself. The reciprocal metric is R_cell=M_cell^-1=diag(1/m1,1/m2,1/m3), units LU^-2. Multiplying corresponding diagonal entries verifies M_cell R_cell=I. Equivalently divide each metric cofactor by det(M_cell), with units LU⁶, to get the reciprocal metric. We never rename this G_phase, the distinct phase metric.

The source M06 branch card defines S=C_b+C_c and A_branch=C_b-C_c. Its symbol is A in the source; here A_branch avoids collision with areas and dA. Adding and subtracting yields C_b=(S+A_branch)/2 and C_c=(S-A_branch)/2. For integer C_b,C_c, S and A_branch must both be even or both odd. This is an admissibility condition: S=3,A_branch=0 would yield halves and is not an integer branch pair. These are carry-side coordinates, not the shape projections u,v or detector parity. We decode supplied pairs; we do not generate a carry history or introduce a new nearest-integer tie convention.

| Component | Type/units | Retained information and return map |
|---|---|---|
| B and geometry | Ordered basis, LU; frame/orientation declared | Keep basis/orientation because metric alone loses absolute orientation |
| M_cell, cof(M_cell), R_cell | Matrices; LU², LU⁴, LU^-2 | B^T B; diagonal cofactors; reciprocal entries |
| m or s; A0 | Dimensionless common log coordinate; area | y=m1+z and areas=A0 exp(y) |
| u,v or z | Dimensionless area shape | y=s e_s+u e_u+v e_v with s retained |
| dG=dln Gamma2 | Dimensionless scalar tangent | Fixed-angle J inverse, with named branch and baseline context |
| S,A_branch | Integer branch coordinates, same parity | (S+A_branch)/2,(S-A_branch)/2 |

## C10.05-W1 — Worked synthetic ledger

For B=diag(1,2,3) LU, M_cell=diag(1,4,9) LU². Its determinant is 36 LU⁶, cofactors diag(36,9,4) LU⁴, reciprocal diag(1,1/4,1/9) LU^-2. The product diagonal is (1,1,1). Its orthogonal face areas are (2,3,6) LU²; with A0=1 LU² retain y=(ln2,ln3,ln6), m=(ln2+ln3+ln6)/3, u=(ln3-ln2)/sqrt2, v=(2ln6-ln2-ln3)/sqrt6. These need not be decimalized. A separate supplied synthetic branch pair S=2,A_branch=-2 gives C_b=0,C_c=2. Retain both records with their different labels. The tangent scalar relation may be stored as a map with no supplied dG value; do not manufacture a measurement.

## C10.05-P1 — Practice

For the separate synthetic B=diag(2,2,2) LU, calculate the three matrices with units and check the inverse. Decode S=4,A_branch=2. Classify m,u,v,dG and the branch pair; explain why B must be retained if orientation is needed.

Answer: M_cell=4I LU², determinant 64 LU⁶, cofactors 16I LU⁴, R_cell=I/4 LU^-2. Their product is I. C_b=(4+2)/2=3, C_c=(4-2)/2=1; recombination gives (4,2). Each area is 4 LU², so for A0=1 LU², m=ln4=2L and u=v=0. dG is a scalar tangent, not one of these shape entries. Rotating every basis edge together preserves all dot products, so M_cell does not recover the original frame orientation; keep B and its frame.

## C10.05-E2 — An area anchor fixes the remaining scale

At fixed known nondegenerate angles, divide A_bc by A_ab: l_b cancels, leaving (l_c/l_a)sin(theta_bc)/sin(theta_ab). Similarly A_bc/A_ac gives l_b/l_a times its angle factors. Thus, using the source ratios,

    k_c=l_c/l_a=(eta/1000) sin(theta_ab)/sin(theta_bc),
    k_b=l_b/l_a=(alpha_inverse/100) sin(theta_ac)/sin(theta_bc).

These ratios fix lengths only up to a common positive length t: (l_a,l_b,l_c)=t(1,k_b,k_c). In this section t is a LENGTH, unlike Lesson 3's dimensionless change parameter. Use the dimensional anchor A_ab=t² k_b sin(theta_ab). Divide by its positive dimensionless factor, then take the positive square root:

    t=sqrt(A_ab/[k_b sin(theta_ab)]).

Recompute all three areas to check compatibility with the supplied angles and ratios. The anchor determines size, not orientation or handedness.

## C10.05-W2 — Worked synthetic anchor

Orthogonal areas (6,8,12) LU² have sine factors all 1. eta=1000(12/6)=2000; alpha_inverse=100(12/8)=150. Therefore k_c=2, k_b=3/2. The anchor gives t=sqrt(6/(3/2))=sqrt4=2 LU. Lengths are (2,3,4) LU. Reconstructed areas are 2 times 3=6, 2 times 4=8, 3 times 4=12 LU².

## C10.05-P2 — Practice

Repeat with orthogonal areas (9,18,18) LU²; find both ratios, t and all lengths. State what remains undetermined if the anchor is omitted.

Answer: eta=2000, alpha_inverse=100, k_c=2, k_b=1. t=sqrt9=3 LU; lengths (3,3,6) LU. Products give (9,18,18) LU². Without the anchor, any positive t gives the same ratios; no absolute length is determined.

> Claim scope: The Devon list is S02#/backbone_sequence/6/devon_dimension; branch maps are /backbone_sequence/5/side_modes; area anchoring is /scale_uniqueness_theorem. Synthetic orthogonal boxes are not the mature locked Cell3. Neither a metric nor the anchor recovers its handed basis. The scalar lift remains separately sourced to M19 gravity_scalar_lift and is not a demonstrated force law.

## Diagnostic checks

1. **C10.05-D1:** Why is an unlabeled tuple of metric entries, u,v and branch modes insufficient?
2. **C10.05-D2:** What fails if angles or the dimensional anchor are omitted?
3. Is S=3,A_branch=2 an admissible integer pair?
4. What units does cof(M_cell)/det(M_cell) have?
5. Is a positive diagonal basis the locked Cell3 basis?

Worked answers: (1) It loses carrier, units, order and inverse metadata. (2) Without angles the length-ratio equations do not close; without anchor the positive length t is free. (3) No, because (3+2)/2=2.5 and (3-2)/2=0.5 are not integers. (4) LU⁴/LU⁶=LU^-2. (5) No; it is a declared synthetic comparison, while Cell3 preserves its source basis and negative determinant.

Next: [Lesson 6](lesson-06.md) tests the entire record. Pacing revised to THREE 55-minute periods: typed geometry, branch decoding, then anchor reconstruction. Each: 5 retrieval + 20 teaching/example + 15 practice + 15 checks. The extra period protects first-principles instruction without reducing coverage.
'''
LESSONS['lesson-06']=r'''
# Lesson 6 — Limits and reconstruction tests

Essential question: What must a reversible change report retain and check?

Goals: distinguish inverse residual from approximation remainder; reconstruct areas from retained coordinates; audit domain, units and provenance.

Bridge: Lessons 1–5 supplied every operation. We now combine them without introducing a new model. Keep unrelated synthetic examples in separately labeled records; do not imply that a branch pair, a square model and an area triple were measured together.

## C10.06-E1 — Two different checks

An inverse residual is recovered input minus supplied input for a declared map. For the Jack coefficient map it is J^-1(Jx)-x, an ordered triple. Algebra makes it exactly zero in the domain. An approximation remainder is exact finite output change minus tangent prediction. In the product model it is 2t²; the square model has t². A zero inverse residual does not force either remainder to vanish. Preserve signs, coordinates and the starting value in both records.

Use this report procedure. First name the record, input order, units, references and source pointer. Next state the domain: positive areas, fixed angles when needed, an admissible integer branch pair, and whether a map is exact or tangent. Calculate transformed coordinates. Preserve the common scale, geometry and all residual information. Finally reconstruct the input and compare component by component. If a residual is nonzero, locate the missing term, approximation or transcription error. A single magnitude or score cannot replace its signed entries.

For log areas, both y=m1+z and y=s e_s+u e_u+v e_v must agree. Then A_i=A0 exp(y_i) restores dimensional areas. If changing the reference, retain the new A0. If changing angles, retain those changes and do not apply J as if they vanished. A scalar baseline or finite response law cannot be recovered from a tangent table alone.

## C10.06-W1 — Worked report audit

Record PRODUCT is the classroom function (1+t)(1+2t) at dimensionless t=0.1. It starts at 1, ends at 1.32, and has change 0.32=0.30+0.02. Save the positive remainder 0.02.

Record JACK uses S02#/backbone_sequence/6, with the M19 gravity_scalar_lift branch named. The synthetic tangent input (1,2,3)t gives (2,-1,4)t and returns to (1,2,3)t. Its inverse residual is (0,0,0). This says nothing about the product's finite remainder.

Record AREAS has A0=1 LU², m=5L/3, z=(-5,1,4)L/3. Addition recovers (0,2,3)L. Exponentiation gives (1,4,8) LU², so the reconstruction residual against those supplied areas is (0,0,0) LU². Keep the original area order, reference and any geometry record; the reduced shape alone could not have restored them.

## C10.06-P1 — Practice

Prepare separate SQUARE, JACK, AREAS and GEOMETRY/BRANCH records using prior practice data: t=0.1 in (1+t)²; Jack input (2,-1,1)t; area logs (1,2,4)L with A0=1 LU²; diagonal basis (2,2,2) LU and branch (4,2). Include inverse and approximation checks. Add the independent anchor record (9,18,18) LU² with perpendicular angles. Explain why the area triples in the different records need not coincide.

Answer: SQUARE gives baseline 1, output 1.21, change 0.21=0.20+0.01. JACK gives (-1,3,33)t and inverse (2,-1,1)t, zero inverse residual. AREAS gives m=7L/3, z=(-4,-1,5)L/3, reconstructing (1,2,4)L and (2,4,16) LU². GEOMETRY gives M_cell=4I LU², cofactors=16I LU⁴, R_cell=I/4 LU^-2; the product is I. BRANCH gives (C_b,C_c)=(3,1), returning to (4,2). ANCHOR yields eta=2000, alpha_inverse=100, t=3 LU and lengths (3,3,6) LU, restoring (9,18,18) LU². These are explicitly separate classroom records; merging them as one box would introduce contradictory geometry.

> Claim scope: Fresh checks verify the displayed finite algebra. S03#/findings/1 reports wider serialization/DAG incompleteness including M07; this course does not certify its global repair. The verified arithmetic, the archived formula statement and an unestablished physical mechanism remain different evidence layers. No empirical datasets are supplied or claimed here.

## Diagnostic checks — C10.06-D1

1. Is the square remainder 0.01 evidence that the Jack inverse failed?
2. What information is lost if a report keeps only u,v?
3. If included angles vary, can zero residual under the old J certify the geometry?
4. What must accompany a dimensional area reconstruction?

Worked answers: (1) No; they concern different maps and checks. (2) Common scale and absolute area reconstruction are lost unless m or s and A0 are retained. (3) No; omitted angle-change terms lie outside that map's stated input domain. (4) Positive A0 with units, the ordered log coordinates or their complete reversible decomposition, and the declared operation/reference history; geometry additionally needs its own basis or angle record.

Next: [Capstone](capstone.md) constructs a reversible report using these same operations. Pacing: 55 minutes = 5 retrieval + 20 worked synthesis + 15 practice + 15 checks/repair.
'''
for name,content in LESSONS.items(): write(name+'.md',content)
