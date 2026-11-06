# 2. ICRS directions and local orientation

Essential question: How can a sky direction become three components?

Goals

- Convert RA hours and angles to Cartesian components.
- Map a local east/north/up triple into declared common axes.
- Identify zero-vector and polar direction limits.

Prerequisite bridge: Begin with [Lesson 1](lesson-01.md). Use the component transformation from Lesson 1 to connect a sky description with a local triad.


## C24.02-E1 — Directions on a sphere

ICRS names a celestial reference system whose axes serve as our common comparison directions. A direction does not locate an origin or prescribe a terrestrial orientation. In our spherical convention right ascension α is measured around the xy-plane from +x toward +y; declination δ is measured above that plane toward +z. A full turn is 360 degrees or 24 RA hours, so multiply RA hours by 15 degrees/hour. These hours label angle, not elapsed trajectory time.

Draw a circle of radius 1 centered at the origin. At angle θ measured counterclockwise from +x, the point's x-coordinate is cos θ and y-coordinate is sin θ. These definitions also work beyond the first quadrant: signs come from coordinates. A radian measures arc length divided by radius; one full circumference is 2π radii, so radians=degrees×π/180. π is the circle circumference divided by diameter. Use a calculator in the stated angular mode.

| Angle | Radians | cosine | sine |
|---|---|---|---|
|0°|0|1|0|
|30°|π/6|√3/2|1/2|
|45°|π/4|√2/2|√2/2|
|60°|π/3|1/2|√3/2|
|90°|π/2|0|1|
|180°|π|-1|0|

The 30° values come from halving an equilateral triangle: hypotenuse 2, short side 1, remaining side √(4-1)=√3. An isosceles right triangle gives the 45° values. For length r≥0, the height is z=r sin δ and the horizontal radius is r cos δ. Splitting that horizontal radius gives x=r cos δ cos α, y=r cos δ sin α. Check length using |p|=√(x²+y²+z²), the three-dimensional Pythagorean rule. A unit direction is p/|p| for nonzero p.

Local east E, north N and up U form another set of axes. If their common-frame vectors are supplied, a local triple (e,n,u) becomes eE+nN+uU. Real E,N,U depend on site and epoch; a named compass direction is not automatically an ICRS axis.

## C24.02-W1 — Legacy C24-FRAME-EX1

Let L be a declared length unit, r=2L, α=6h=90°, δ=30°. Then x=2(√3/2)(0)=0, y=2(√3/2)(1)=√3 and z=2(1/2)=1, all in L. Length √(0+3+1)=2L verifies the conversion. For a synthetic local triad E=(0,1,0), N=(0,0,1), U=(1,0,0), a local east vector (1,0,0) becomes (0,1,0) in common axes.

## C24.02-P1 — Legacy C24-FRAME-P1

Compute r=3L, α=0°, δ=0°: (x,y,z)=(3,0,0)L. Under the same triad, local (0,1,1) becomes N+U=(1,0,1). Its length is √2; dividing gives (1/√2,0,1/√2). It points at α=0°, δ=45°, since its horizontal and vertical components are equal. Keep length √2 separately if normalizing a displacement: multiplying the unit vector by √2 reconstructs it.

> Scope: These conversions are mathematical consequences of stated conventions. The triad is supplied synthetically, not calculated for an actual observing site. At either celestial pole α is nonunique, because the horizontal radius is zero. A zero vector has no direction.

## C24.02-D1 — Diagnostics

1. Convert 6 RA hours to degrees and radians.
2. Find r=2L, α=180°, δ=0° in components.
3. What is the common vector for local (2,-1,0)?
4. Can (0,0,0) be normalized? What happens to α at δ=90°?

Answers: 1. 90°=π/2 rad. 2. (-2,0,0)L. 3. 2E-N=(0,2,-1), retaining the north sign. 4. No, division by zero is undefined; at the pole all RA values describe the same direction. Do not supply invented unique angles.


Next dependency: [lesson-03](lesson-03.md). Carry your signed component ledger forward.
