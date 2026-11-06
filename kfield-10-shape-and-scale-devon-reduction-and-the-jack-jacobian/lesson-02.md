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
