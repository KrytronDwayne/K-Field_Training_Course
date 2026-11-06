# Lesson 03 — Geometry and proposed inertial response

Essential question: Which additional inputs turn a direction-dependent motion calculation into a force prediction?

Goals: Compute signed directional velocity and acceleration; retain perpendicular components for reconstruction; identify the law and coefficient needed for a force.

Prerequisite bridge. Lesson 02 defined dot products, vector length and unit normals. Use LU for length, T for time and MU for mass. Velocity v gives change of position per time, in LU/T; acceleration a gives change of velocity per time, in LU/T^2. A negative component means motion or change opposite to the chosen positive axis, not a negative magnitude.

Pacing: one 55-minute period: 5 retrieval, 20 instruction/example, 15 practice, 15 diagnostics and repair.

## C23.03-E1 — Preserve a direction and its complement

For a dimensionless unit normal n, the scalar v_parallel=v dot n tells how much velocity points along that orientation. Multiply it by n to obtain the parallel **vector**. The perpendicular vector is v_perp=v-(v dot n)n. Their sum returns v. The dot product of the perpendicular part with n is zero because n dot n=1. This is a reversible description if both pieces are kept. The same decomposition applies to a.

Reverse the normal by replacing n with -n. The scalar projections change signs because each product changes sign. Their squares stay fixed. The parallel vector does not change: its scalar and its normal both reverse. This distinction matters when comparing signed measurements with orientation-independent costs.

Geometry tells us these projections; it does not supply a mass or a force coefficient. A constitutive equation is an additional response rule connecting specified inputs and outputs. For example, propose F_parallel=mu a_parallel with mu in MU. Then F_parallel has units MU*LU/T^2. This is a conditional model computation. The familiar constant-mass Newtonian relation between net force and acceleration is a reference-theory example of such a rule; this exercise does not derive it from the scalar lift. A full prediction of motion would also need starting position/velocity and the applicable forces or boundary conditions. Nothing in the dimensionless F of Lesson 01 makes it this F_parallel.

## C23.03-W1 — Worked signed projection

Let n=(0,0,1), v=(1,2,3) LU/T, and a=(0,0,-2) LU/T^2. Then v_parallel=1(0)+2(0)+3(1)=3 LU/T and a_parallel=-2 LU/T^2. The retained velocity complement is v_perp=(1,2,0) LU/T; 3n+v_perp=(1,2,3). The acceleration complement is zero. Reversing n gives scalar values -3 and +2, while squared values stay 9 LU^2/T^2 and 4 LU^2/T^4. No coefficient mu was supplied, so there is no numerical force prediction.

## C23.03-P1 — Practice and answer

For n=(3/5,4/5,0), v=(5,0,0) LU/T and a=(0,5,0) LU/T^2, verify the normal, calculate both projections, retain complements, and then use the explicitly proposed mu=2 MU response law above.

Answer: n dot n=9/25+16/25=1. Projections are 3 LU/T and 4 LU/T^2. Parallel velocity is (9/5,12/5,0); subtracting from v leaves (16/5,-12/5,0) LU/T. Parallel acceleration is (12/5,16/5,0), leaving (-12/5,9/5,0) LU/T^2. Adding each pair returns its input. The conditional force scalar is 2*4=8 MU*LU/T^2. Its parallel vector would be (24/5,32/5,0) in those force units. The geometry alone does not determine a perpendicular force.

> Claim scope. These are synthetic kinematic inputs and an explicitly added response law. They illustrate how to keep a mechanism's premises visible alongside M19 scalar and reciprocal branches. No observation of gravitational or inertial response is supplied here. A photon-equivalent model energy would also require its own definition; it is not measured transferred energy. Phase is not force.

## Diagnostics and worked answers

1. **C23.03-D1:** Can the dimensionless G of Lesson 01 be relabeled as a force? Answer: not without a declared conversion with units and a response law. Its scalar identity supplies neither.
2. What goes wrong if n=(0,0,2) is used as a unit normal? Answer: n dot n=4, and v dot n doubles the intended signed projection. Normalize first: n/length(n)=(0,0,1).
3. Does reversing n reverse the parallel velocity vector? Answer: no, (-v_parallel)(-n)=v_parallel n. It reverses the signed scalar label.
4. If a synthetic force reading is 9 rather than the predicted 8, what is retained? Answer: observed 9, predicted 8 and residual +1 MU*LU/T^2, together with n, mu, a and the law. Their sum reconstructs the reading; do not erase the discrepancy or call it a new measured law.

Next dependency: [Lesson 04](lesson-04.md) applies the same discipline—compute what inputs justify, then name the remaining structure—to finite cycle counts.
