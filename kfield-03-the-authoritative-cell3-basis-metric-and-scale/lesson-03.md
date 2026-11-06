# Lesson 3 — Face areas and signed volume

**Essential question:** How can area and volume record orientation without becoming negative sizes?

**Goals.** Calculate three cross products; distinguish oriented area from area magnitude; evaluate a scalar triple product and its sign; retain face labels and units.

## Bridge

You can add vectors, take dot products, and compute magnitudes. Those tools measured edges. To measure a face, we need an operation whose magnitude is the parallelogram area and whose direction identifies which way the face is oriented.

## Oriented area components

For u=(u_x,u_y,u_z) and v=(v_x,v_y,v_z), define

u×v=(u_y v_z−u_z v_y, u_z v_x−u_x v_z, u_x v_y−u_y v_x).

Each component is a signed two-dimensional area: yz, zx, and xy in that order. In a two-dimensional plane the difference of the two products measures the parallelogram's signed area. Combining the three gives a vector perpendicular to both inputs. You can verify perpendicularity by dotting the displayed vector with u or v: each product cancels with its opposite. Reversing the order negates the vector. The right-hand rule selects its direction: curl from the first arrow toward the second; the thumb gives the normal direction in right-handed external axes.

The magnitude A_uv=||u×v|| is nonnegative and equals ||u||||v||sin(theta_uv), base times perpendicular height. Sine for an acute right-triangle angle is opposite/hypotenuse; for an included angle from 0 to 180 degrees it gives the nonnegative height factor. Parallel edges have zero area. A **normal** is a perpendicular direction; a unit normal is the cross vector divided by its magnitude, when the magnitude is nonzero.

For three columns, det(B)=a·(b×c), a **scalar triple product**. It is signed base area times signed perpendicular height. The unsigned volume is V=|det(B)|. A zero determinant means the edges cannot enclose three-dimensional volume; a nonzero determinant means they are independent. Negative orientation is retained, not converted into a new basis.

## Worked example — Classroom analogue, not Cell3

Use the same a,b,c as Lessons 1–2. Calculate all three labeled face vectors:

- c_ab=a×b=(0·0−0·2, 0·1−1·0, 1·2−0·1)L²=(0,0,2)L².
- c_ac=a×c=(0,3,0)L², because the middle component is 0·0−1·(−3)=3.
- c_bc=b×c=(2·(−3)−0·0, 0·0−1·(−3), 1·0−2·0)L²=(−6,3,0)L².

Their areas in **ab, ac, bc** order are 2L², 3L², sqrt(36+9)L²=3sqrt(5)L². The third area is about 6.7082L², but its exact expression remains 3sqrt(5)L². Do not reorder this list to match a different source field: the locked source also has a normalized area ray in **bc, ac, ab** order.

Now det(B_ex)=a·c_bc=(1,0,0)·(−6,3,0)L³=−6L³. The same result follows from (a×b)·c=(0,0,2)·(0,0,−3)L³. Its absolute value is 6L³. The area of ab is 2L² and the perpendicular height along c is 3L, so ordinary volume is 2·3=6L³. This independent geometric check confirms the magnitude and leaves the negative orientation intact.

The columns of a cofactor table are conventionally b×c, c×a, a×b. Notice that c×a=−c_ac. Thus naming c_ab, c_ac, c_bc as “face cofactors” does not authorize inserting them unchanged into that column order. Explicit cross-product labels prevent a sign error.

> **Claim scope.** The analogue verifies the operations exactly. Actual Cell3's source volume and areas are on the geometry card. Its negative determinant is intentional under fixed ICRS columns. No detector parity, projective identification of n with −n, or physical chirality is inferred from this arithmetic.

## Guided practice and diagnostic checks

1. Find c×a and its magnitude.
2. Check b·(b×c). What does the result say?
3. Exchange a and b. What happens to signed volume and unsigned volume?
4. Replace c by (2,0,0)L. Compute the determinant and explain the geometric failure.

## Worked answers

1. (0,−3,0)L², magnitude 3L²; reversing order changes orientation, not area.
2. (1,2,0)·(−6,3,0)L³=−6+6=0L³. The cross vector is perpendicular to b.
3. Signed volume becomes +6L³; unsigned volume remains 6L³. This is a new ordered basis.
4. b×c=(0,0,−4)L², so a·(b×c)=0L³. All three edges lie in the xy plane and cannot describe arbitrary z displacements.

**Next dependency:** [Lesson 4](lesson-04.md) uses nonzero volume to justify reversing a coordinate map and its metric.
