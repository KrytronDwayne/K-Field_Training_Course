# Lesson 4 — The Jack map and its inverse

Essential question: Which three output changes recover three coherent edge-scale changes?

Goals: derive the rows of the fixed-angle map; apply its inverse; check its determinant and ordered units; distinguish scalar coordinates from dynamics.

Bridge: Lesson 3 taught row-by-column multiplication and inversion by equations. Now each entry has a specific source meaning. Use positive edge lengths l_a=|a|, l_b=|b|, l_c=|c| and fixed included angles. Vertical bars mean length here. 'Coherent' means the same three edge changes generate all three face changes.

## C10.04-E1 — Source card and derivation

For two edges, area is base times perpendicular height: A_ab=l_a l_b sin(theta_ab). The sine factor is height divided by the second edge length; it equals 1 for perpendicular edges. This course supplies each angle factor rather than requiring trigonometric calculation. Nondegenerate faces have positive sine factors. The same area rule holds for ac and bc.

With angles fixed, the exact log-area change is the sum of the two exact log-length changes. Its tangent form is

    dln A_ab=x_a+x_b, dln A_ac=x_a+x_c, dln A_bc=x_b+x_c,
    x=(x_a,x_b,x_c)=(dln l_a,dln l_b,dln l_c).

Finite log changes are logs of ratios to the starting quantity; the d symbols here denote their tangents. Both are dimensionless. S02 M05 defines eta=1000 A_bc/A_ab and alpha_inverse=100 A_bc/A_ac. Here alpha_inverse=1/alpha, so alpha=A_ac/(100 A_bc). Constants vanish from changes of logs. Therefore

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
