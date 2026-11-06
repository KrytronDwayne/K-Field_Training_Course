# Sky positions and projective axes

Essential question: What information changes when a sky direction is treated as an axis?

Goals: Convert simple sky angles into vectors; calculate directed and axial separations; identify what each observation supplies.

Prerequisite bridge. You need signed arithmetic, coordinate graphs, and the ability to square and take a positive square root. Earlier courses 04, 06, 10, 22, 24 and 26 supply coordinate and evidence-reading experience. The operations used here are rebuilt locally. A vector is an ordered list of components: (1,0,0) means one step along the first axis and none along the others. Its length is sqrt(x²+y²+z²). A unit vector has length one.

## C29.01-E1 — An arrow and an undirected line

Imagine pointing at a galaxy from the observer. The arrow gives a direction. It does not tell you how far along that arrow the galaxy lies. All positive multiples of the arrow point the same way; dividing by its length places its tip on a sphere of radius one. Keep any supplied distance separately so that this normalization can be reversed. If distance was never supplied, mark it missing rather than inventing it.

The ICRS coordinate convention used by G03 and G04 has x toward right ascension (RA) 0°, declination (Dec) 0°; y toward RA 90°, Dec 0°; and z toward the north celestial pole. RA, denoted alpha, goes around the equator; Dec, denoted delta, measures elevation above it. On a unit circle, cosine is the horizontal coordinate and sine is the vertical coordinate. Thus the horizontal projection has length cos(delta), and the height is sin(delta):

`x = (cos(delta)cos(alpha), cos(delta)sin(alpha), sin(delta))`.

For the core calculations use sin(0°)=0, cos(0°)=1, sin(90°)=1, cos(90°)=0, sin(180°)=0 and cos(180°)=-1. The formula uses angles consistently in degrees here. Later loop phases use radians, where one full turn is 2π radians = 360°.

An **unoriented axis** is the pair {x,-x}: it records a line but not which end is positive. An intrinsic galaxy axis describes the galaxy's orientation; its sky position describes where it appears. One is not supplied by the other. A **projective view** deliberately identifies the two ends for a specified calculation. Store the original arrow or its sign alongside that view.

The dot product multiplies corresponding components and adds: x·y=x₁y₁+x₂y₂+x₃y₃. For unit vectors it equals the cosine of their directed angle. `arccos(t)` means the angle from 0° through 180° whose cosine is t. Directed separation is arccos(x·y); axial separation is arccos(|x·y|). Absolute value removes the sign only in the axial calculation. For dot products 1,0,-1 the directed angles are 0°,90°,180°.

## C29.01-W1 — Worked example

RA 0°, Dec 0° gives (1·1,1·0,0)=(1,0,0)=e_x. RA 180°, Dec 0° gives (-1,0,0)=-e_x. Both have length one. Their dot product is -1, so directed separation is 180°. The absolute dot product is 1, so axial separation is 0°. If only the axis were saved, these two different sky positions could no longer be distinguished.

> Source scope. G04 pp1,3 reports 114,381 unique directed sky positions with no radial distance inferred. Its discovery operators used antipodal completion, while final fitting and assignments used the actual directed vectors. G02 p3 explicitly distinguishes this sky-position pathway from an earlier galaxy-axis pathway. These are source-reported observational and analysis facts; our three-coordinate examples are synthetic teaching examples.

## C29.01-P1 — Guided practice and answer

Compute RA 90°, Dec 0° and compare it with e_x in both views. The vector is (0,1,0)=e_y. Its dot product with e_x is zero, so both angles are 90°. An antipodal discovery view may include -e_y, but the observation record still says e_y. Preserve the object identifier and original direction.

## Diagnostics — C29.01-D1

1. Does (1,0,0) locate a galaxy at a known physical distance?
2. For e_z and -e_z, find directed and axial angles.
3. Can sky position alone identify the galaxy's own unoriented axis?
4. What must be retained when forming a projective discovery view?

Worked answers. 1. No: it specifies an arrow on the unit sphere; a radial-distance field is missing. 2. The dot product is -1, giving 180° directed and 0° axial. 3. No: the intrinsic orientation needs its own observation. 4. Retain the original direction and identity, plus the transformation and its scope; a sign can reconstruct a representative only when the chosen representative is also fixed.

Next: [lesson 02](lesson-02.md) uses the dot product to distinguish a historical response from a reciprocal plane address.
