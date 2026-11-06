# Moving Reference Frames and Laboratory Motion

Student course • seven lessons • eleven core periods

Supporting [glossary](terminology.md), [capstone and full answers](capstone.md), [teacher guide](teacher-guide.md), and [source ledger](sources.md).

<!-- BEGIN: lesson-01 -->
# 1. Frames, origins, and epochs

Essential question: What makes a position or velocity unambiguous?

Goals

- Label origin, axes, units and epoch for a vector.
- Apply and reverse a rigid coordinate transformation.
- Advance and reverse a constant-velocity trajectory.

Prerequisite bridge: Begin with signed arithmetic and coordinate graphs. A triple lists three signed distances; we will now attach an origin, axes and time.


## C24.01-E1 — A coordinate is an instruction

A position tells how to travel from an origin to a point. In a frame F, p=(2,1,0) km means travel 2 km along its positive x-axis and 1 km along its positive y-axis. Negative components reverse travel. An epoch is the time at which this description applies. Axes alone do not specify the origin: two rooms can have parallel walls but different corner positions.

A velocity gives signed position change per second in a specified frame. A constant velocity v over an elapsed time Δt gives displacement vΔt. Units explain the rule: (km/s)×s=km. Thus p_next=p_now+vΔt. This is exact for our stipulated constant-velocity examples; changing velocities need a declared update rule.

To describe the same point in another frame, first turn its local offset and then add the local origin's world position o. Write p_world=o+R p_local. R is a three-by-three table, or matrix. Its columns are the local unit axes written in world components. Multiplying R by (u,v,w) means u times column 1 plus v times column 2 plus w times column 3. Equivalently each answer component is the sum of the products across one row. R has no length unit.

For a rotation, its inverse is R^T, the transpose obtained by exchanging rows and columns. This works because the unit axes remain perpendicular and of length one. Undo translation before rotation: p_local=R^T(p_world-o). This inverse rule is for these orthonormal rotations, not every arbitrary table of numbers. If o and R are constant, a velocity transforms as v_world=R v_local; adding a distance o to a velocity would mix units. Moving origins and rotating axes need Lesson 4.

## C24.01-W1 — Turn, translate, reverse

At synthetic epoch t0=2026-11-05T00:00:00Z let local-to-world

```
R = [0 -1 0]       o = (5,3,1) km
    [1  0 0]       p_local = (2,1,0) km
    [0  0 1]
```

Row products give R p_local=(-1,2,0) km. Adding o gives p_world=(4,5,1) km. Subtracting o returns (-1,2,0); the transpose maps (x,y,z) to (y,-x,z), recovering (2,1,0) km. Local velocity (1,0,0) km/s becomes (0,1,0) km/s. Both R and o remain constant throughout the velocity interval for this example.

## C24.01-P1 — Answered practice; legacy C24-TRAJ-D1

Use a separate fixed frame F with p0=(1,2,3) km and v=(2,-1,0) km/s. Compute two updates of Δt=2 s, then reverse them. Each displacement is (4,-2,0) km. Thus p1=(5,0,3) km at t0+2 s and p2=(9,-2,3) km at t0+4 s. Reverse: p2-2vΔt=(9,-2,3)-(8,-4,0)=(1,2,3) km. Retain p0, v and both timestamps; the endpoint alone cannot identify the path. This is the trajectory branch of legacy C24-FRAME-EX1.

> Scope: All numbers here are synthetic definitions, not an ephemeris or measured Solar/Galactic motion. Derived endpoints follow those definitions. No mechanism is inferred.

## C24.01-D1 — Diagnostics

1. Does “ICRS, (1,2,3)” specify a position completely?
2. Transform local (0,2,1) km with the example R and o.
3. Can you add o to (1,0,0) km/s?
4. Where is the practice particle at t0+6 s, and how do you recover p0?

Answers: 1. No: give origin, length unit and epoch as well as axes. 2. R gives (-2,0,1), then o gives (3,3,2) km. 3. No: km and km/s differ; a stationary offset cancels in position differences. 4. (13,-4,3) km; subtract 6(2,-1,0) km to obtain (1,2,3) km. Preserve the negative y motion.


Next dependency: [lesson-02](lesson-02.md). Carry your signed component ledger forward.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
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
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# 3. The nested laboratory motion chain

Essential question: Which motions belong in a laboratory velocity?

Goals

- Name the four relative velocity terms and their shared contract.
- Compute a signed sum and a decomposed displacement.
- Recognize double counting and source-epoch gaps.

Prerequisite bridge: Begin with [Lesson 2](lesson-02.md). Use common-axis components from Lesson 2 to add relative motions.


## C24.03-E1 — A chain of relative motions

Imagine walking inside a moving train: your velocity relative to the track combines your motion relative to the train and the train's motion relative to the track, when both use the same axes and time. Our additive classroom chain extends this idea. Write v_A/B for the velocity of A relative to B. EMB means Earth–Moon barycenter, the shared mass-center reference for Earth and Moon. CMB means cosmic microwave background; the source uses a CMB comparison frame. It is not the Galactic-center drawing gauge.

In common axes, at one epoch, in m/s, use

v_lab/CMB = v_Sun/CMB + v_EMB/Sun + v_Earth/EMB + v_lab/Earth.

Each numerator is the next denominator, so intermediate reference motions are accounted for once. Here Earth means its center for the relative translational term; the laboratory term includes its motion relative to that center. A terrestrial component expressed in Earth-fixed axes must first be rotated into the common axes. The formula is the declared additive kinematic model of this course, not a derivation of relativistic velocity addition.

## C24.03-W1 — Four signed ledgers

At t0 use synthetic constant vectors (10,0,0), (0,2,0), (-1,0,0), (0,0,1) m/s, in chain order. Add coordinate by coordinate: (10+0-1+0,0+2+0+0,0+0+0+1)=(9,2,1) m/s. With x0=(1,2,3)m and two elapsed seconds, keep the four displacements:

|Term|Displacement (m)|
|---|---|
|Sun/CMB|(20,0,0)|
|EMB/Sun|(0,4,0)|
|Earth/EMB|(-2,0,0)|
|lab/Earth|(0,0,2)|

Their sum is (18,4,2)m; x(2)=(19,6,5)m. Subtract each displacement to recover (1,2,3)m. Keeping only the total would conceal the opposing x contributions.

## C24.03-P1 — Change one term

Reverse only Earth/EMB to (+1,0,0)m/s. The new total is (11,2,1)m/s and endpoint (23,6,5)m. Relative to the first endpoint the change is (4,0,0)m, because a change from -1 to +1 is +2m/s for two seconds. Keep both ledgers; do not overwrite the original.

## Source card: physical velocity

T40 admits the physical vector at `/derived_results/earth_cmb/V_E_icrs_m_s` in the linear-inertia source; T10 gives its speed. Its ICRS components are (-359003.19906581304,76679.88603400199,-44701.060100687995)m/s, with speed 369812.50200040644m/s. The inspected authority does not attach an explicit vector epoch. A publication timestamp cannot fill that field. See [sources](sources.md) for its exact path and hash.

> Scope: The four tiny classroom velocities are synthetic and do not estimate that source vector. The source vector is an already composed Earth/CMB object, not an extra independent chain term. G_phase V is a phase-transformed vector and is denied as a physical velocity by T40. An experiment-local 361.838…km/s trajectory mentioned in the blueprint is separately typed; it is not a replacement authority or a fifth term. No real propagation is assigned without its full epoch contract.

## C24.03-D1 — Diagnostics

1. Which term accounts for Earth relative to EMB?
2. Can you add Earth/CMB to Sun/CMB and EMB/Sun to improve the sum?
3. Does zero y in one term allow deletion of that term?
4. Can publication time be used as the missing vector epoch?

Answers: 1. v_Earth/EMB, including its sign. 2. No; Earth/CMB already includes upstream motions, so this double counts. 3. No: other components and the zero itself belong to the ledger. 4. No: record “not specified” and withhold real propagation. Synthetic time is declared separately.


Next dependency: [lesson-04](lesson-04.md). Carry your signed component ledger forward.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# 4. Adding vectors without mixing frames

Essential question: What motion is hidden when coordinates remain fixed?

Goals

- Explain a derivative as a rate approached by shorter intervals.
- Retain origin, turning-axis and local-motion velocity terms.
- Compute cancellation and acceleration in a supplied rotating example.

Prerequisite bridge: Begin with [Lesson 3](lesson-03.md). Use the four-term sum from Lesson 3, but now allow its axes to turn.


## C24.04-E1 — A fixed coordinate can move

A dot over a quantity means its instantaneous rate of change. Start with average velocity [p(t+h)-p(t)]/h for a nonzero time interval h. If shorter intervals approach one value, that limiting value is the derivative, written ṗ or dp/dt. A second derivative is the rate of change of velocity, called acceleration, in m/s². We use smooth prescribed functions here; a finite jump need not have an instantaneous derivative.

We need only a few rules. A constant has derivative zero, t has derivative one, and sums differentiate term by term. For a product f(t)g(t), expand its change as f(t+h)[g(t+h)-g(t)]+[f(t+h)-f(t)]g(t). Divide by h and let h approach zero. Continuity gives (fg)̇=f ġ+ḟ g. The same expansion applies to every entry of a matrix times a vector, without reversing their order.

For sin θ and cos θ with θ in radians, a small turn h changes the unit-circle point approximately by h(-sin θ,cos θ): its motion is tangent, perpendicular to the radius, with distance h per unit turn. Taking the limit gives d(sin θ)/dθ=cos θ and d(cos θ)/dθ=-sin θ. If θ=ωt, multiply these rates by angular speed ω, in rad/s. The argument ωt is an angle; writing cos t below is shorthand for cos[(1rad/s)t], not the cosine of a dimensional time.

Apply the product rule to p_world=o(t)+R(t)p_local(t):

v_world=ȯ+Ṙp_local+R v_local.

The terms mean origin motion, motion from turning axes, and local motion turned into world axes. Differentiate once more:

a_world=ö+R̈p_local+2Ṙv_local+R a_local.

The factor 2 comes from one Ṙv_local in each of the last two differentiated terms. This formula is taught here for interpretation and the supplied simple example; general calculus is not assumed.

A rotation about +z through θ is R=[(cos θ,-sin θ,0);(sin θ,cos θ,0);(0,0,1)], where semicolons separate rows. At θ=90° it is Lesson 1's matrix. For fixed axes Ṙ=0; a translating origin still contributes ȯ. Always convert compatible units and epochs before adding.

## C24.04-W1 — Stationary locally, moving globally

Let elapsed time t be in seconds, ω=1rad/s, origin o(t)=(t,0,0)m with its first component understood as (1m/s)t, and fixed p_local=(1,0,0)m. Then p_world=(t+cos t,sin t,0)m in this shorthand. The local velocity is zero but the world velocity is (1,0,0)+(-sin t,cos t,0)+(0,0,0)=(1-sin t,cos t,0)m/s. At t=0 it is (1,1,0)m/s. The circular piece has radius 1m; its acceleration is (-cos t,-sin t,0)m/s².

## C24.04-P1 — Cancellation retains its causes

At t=π/2 s, sin t=1 and cos t=0. Origin motion (1,0,0)m/s plus rotation motion (-1,0,0)m/s gives zero velocity. The particle has not been stationary for the whole interval. At t=0 acceleration is (-1,0,0)m/s²; only R̈p_local contributes, because ö, v_local and a_local are zero. The factor of ω²=1s⁻² gives the acceleration unit.

For a separate synthetic residual exercise suppose the model velocity is (1,1,0)m/s and a supplied comparison vector is (1.2,0.9,0)m/s. Residual r=comparison-model=(0.2,-0.1,0)m/s. Store model, r and the comparison; model+r exactly reconstructs it. A vanishing total or a small residual never licenses erasing signed components.

> Scope: These are analytic consequences of synthetic functions. They introduce no Solar/Galactic time law. The additive physical motion and a phase-transformed vector remain different types. Unresolved motion is retained as a vector residual, not silently set to zero.

## C24.04-D1 — Diagnostics

1. A point has v_local=0. Must v_world=0?
2. Name the missing term in ȯ+R v_local for turning axes.
3. In the worked example at t=π/2s, is acceleration also zero?
4. Why can a velocity in km/s not be added numerically to one in m/s?

Answers: 1. No; origin and rotation can move it. 2. Ṙp_local, with units (1/s)m=m/s. 3. No: (-cos(π/2),-sin(π/2),0)=(0,-1,0)m/s². 4. Convert first, using 1km/s=1000m/s, or the sum attaches unequal units to the same numbers.


Next dependency: [lesson-05](lesson-05.md). Carry your signed component ledger forward.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# 5. Sidereal rotation and sensor motion

Essential question: What rotates, and what stays fixed, in a comparison?

Goals

- Rotate all carried directions and node offsets consistently.
- Compare directed angles with unoriented axis angles.
- Distinguish finite replay states from reported samples.

Prerequisite bridge: Begin with [Lesson 4](lesson-04.md). Use the rotating-frame example to distinguish carried directions from fixed ones.


## C24.05-E1 — What the animation carries

Sidereal rotation compares Earth orientation with celestial directions. An Earth-carried sensor direction changes against a fixed celestial comparison. A translation moves the origin but does not turn its direction arrows. To move a local assembly, rotate every offset by the same R, then translate their common origin. Rotating only the highlighted arrow while leaving its supporting triad unchanged describes a different assembly.

Let e_x=(1,0,0), e_y=(0,1,0), e_z=(0,0,1). A dot product u·v=u_xv_x+u_yv_y+u_zv_z measures shared direction. For unit vectors it equals cos θ; arccos means the inverse cosine giving an angle from 0° to 180°. Normalize nonzero vectors before using this angle rule. Orthogonal rotations preserve lengths and dot products, so carried shapes keep their internal angles.

A directed vector distinguishes u from -u. An unoriented axis is a line that identifies those two directions. Its comparison angle is arccos(|û·v̂|), from 0° to 90°; hats mean unit vectors and vertical bars mean absolute value. Save the original signed vectors too: this reduction alone cannot reconstruct polarity.

## C24.05-W1 — Quarter-turn

Use Lesson 1's 90° z rotation. It sends carried e_x to e_y, carried e_y to -e_x, and e_z to itself. Offset (1,1,0) becomes (-1,1,0). Its dot product with carried e_x was 1 and remains (-1,1,0)·(0,1,0)=1. Its length stays √2. A separately fixed comparison e_x remains (1,0,0), so its angle to the carried e_x is now 90°.

## C24.05-P1 — Half-turn

A 180° z rotation maps (x,y,z) to (-x,-y,z). Thus carried e_x becomes -e_x and offset (1,1,0) becomes (-1,-1,0). Dot with fixed e_x is -1, so the directed angle is arccos(-1)=180°. The unoriented axis angle is arccos(|-1|)=0°. Retain the sign and state which angle the question asks for.

> Source scope: T45 reports 97 finite replay states that rotate the east/north/up triad, selected Earth-carried K-axis and all 27 Cell3 nodes together. The fixed comparison Cell3 and Galactic-center sightline stay fixed. T50 separately reports 180000 samples, 2000 rotations, ten channels and a 15.0407096514-degree/hour clock. These are source-reported evidence, not observations newly generated by this course. Finite replay is distinct from acquisition metadata. Reported circle actions are not a claim of physical K-field co-rotation. Solar and Galactic short-window time laws are not supplied. The course does not replace the mature Cell3 basis with its simple orthonormal teaching triad.

## C24.05-D1 — Diagnostics

1. Under the quarter-turn, where does local offset (2,0,1) go?
2. Should the fixed comparison arrow rotate too?
3. What information is lost if only the antipodal angle is saved?
4. Are 97 replay states 180000 newly measured samples?

Answers: 1. (0,2,1), before origin translation. 2. No: its defining role is fixed comparison. 3. Directional polarity; retain both original vectors. 4. No: the first is a finite representation, the second is reported acquisition metadata. Their counts describe different objects.


Next dependency: [lesson-06](lesson-06.md). Carry your signed component ledger forward.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# 6. Physical motion versus visual gauge

Essential question: What can a drawing legitimately tell us about motion?

Goals

- Convert drawn lengths using each chamber’s scale.
- State the Galactic-center gauge’s limited role.
- Classify finite alignment and orientation comparisons.

Prerequisite bridge: Begin with [Lesson 5](lesson-05.md). Use the directed and axis angles from Lesson 5, then separate drawing distance from physical distance.


## C24.06-E1 — A map is not a common ruler

A display can keep directions common while rescaling lengths separately. Define a scale by physical distance per drawn centimeter. Chamber A might use 1000km/cm, while chamber B uses 1km/cm. A drawn length d becomes physical distance sd within that chamber. Distances between chambers have no physical interpretation unless a separate mapping is explicitly supplied.

A gauge here means a chosen visual reference: holding the Galactic-center sightline still helps compare other orientations. It does not make the Galactic Center an absolute rest frame. A fixed camera choice supplies no equation for the Sun's or Galaxy's motion during the animation. Drawing scale and a physical trajectory law answer different questions.

## C24.06-W1 — Same picture length, different distance

One centimeter in A represents 1000km; one centimeter in B represents 1km. The equal screen lengths differ in physical length by a factor of 1000. You cannot compute a physical speed by dividing the screen separation between chambers by elapsed seconds. Even within one chamber you need a valid physical time and scale contract.

T45 and T50 report a finite alignment decision for displayed Cell3 a,b,c and indexed (111) against the source-bound Sgr A* sightline. Sgr A* is the source's Galactic-center comparison target. The closest listed candidate is c at 31.6153896617°. The source reports no exact axial alignment for this candidate set. “Finite” means only the listed candidates are covered; it is stronger than an unspecified status, but not a statement about every possible axis. We report the stated formal result without claiming a fresh compiler run.

## C24.06-P1 — Scales and evidence

Compute the physical distance for 2cm in each chamber: A gives 2000km and B gives 2km. If a directed vector reverses, its unoriented axis can stay the same, as Lesson 5 showed. Preserve direction before the absolute-value reduction.

The supplied orientation comparison reports 11.165830° between a model's local high-curvature axis and its absolute principal axis, and 3.749971° to phase row 3. A high-curvature axis labels a direction of strong change in that model; no curvature calculation is required here. “Phase row 3” is a source-local model direction label, not an additional physical velocity. Classify these angles as model-derived local/absolute orientation consistency. They do not state exact Sgr A* alignment or global uniqueness.

> Scope: The angle values and finite decision are source-reported T45/T50 statements. Our arithmetic checks the display example, not the underlying formal proof. A source-independent measurement identifying a physical K-Cell axis and its ICRS direction remains an open alignment task. Do not replace this specific boundary with a universal claim either way.

## C24.06-D1 — Diagnostics

1. What does 0.5cm represent in A and B?
2. Does a still Galactic-center arrow assert absolute rest?
3. Does nonalignment of four candidates decide every possible axis?
4. Do 11.165830° and 3.749971° establish exact Sgr A* alignment?

Answers: 1. 500km and 0.5km. 2. No: it defines a visual gauge. 3. No: retain the finite candidate scope. 4. No: they compare model directions internally. Keep their original labels and values rather than substituting a different target.


Next dependency: [lesson-07](lesson-07.md). Carry your signed component ledger forward.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# 7. A reproducible trajectory contract

Essential question: Could another person reconstruct your trajectory?

Goals

- Write a complete synthetic trajectory input contract.
- Reconstruct an initial point from decomposed displacements.
- Identify missing real-source inputs without inventing them.

Prerequisite bridge: Begin with [Lesson 6](lesson-06.md). Combine all six earlier lessons into a reproducible input record.


## C24.07-E1 — Reproducibility is part of the result

A trajectory is a rule assigning positions to times. To repeat it, a reader needs more than its speed. A contract records what each input means, where it came from, and how to use it. UTC labels civil epochs; an elapsed second is a duration. UTC can contain leap seconds, so a real calculation must state its time conversion. TAI is an atomic time scale, TT a terrestrial time scale and TDB a barycentric dynamical time scale used in ephemeris work. These labels are not interchangeable; this course supplies no conversion constants. A real conversion must name its tables, method and version.

An ephemeris supplies celestial positions or motions as functions of time. Earth orientation parameters (EOP) describe Earth's orientation for converting terrestrial and celestial axes. A site record names latitude, longitude, height and their datum, the reference surface/convention. A geometry digest identifies exact bytes of a geometry definition; SHA-256 is the fingerprint used in our source ledger. A digest identifies a file, not a proof of its physical claims.

Record origin, axes, units, epoch/time scale, site, ephemeris/EOP versions, geometry and rotation conventions, every component velocity, update or interpolation rule, and residual/reconstruction rules. Interpolation means a declared rule for values between supplied times. “Not applicable: synthetic” differs from “unknown: required for a real calculation.”

## C24.07-W1 — A fully specified toy packet

|Field|Value|
|---|---|
|Evidence class|Synthetic definition and derived arithmetic|
|Epoch|2026-11-05T00:00:00Z|
|Duration convention|Elapsed SI seconds, 0≤t≤2s; no leap crossing in this stipulated exercise|
|Frame|F, fixed right-handed orthonormal axes and fixed origin O; no real celestial origin asserted|
|Position and velocity units|m and m/s|
|Initial point|(1,2,3)m|
|Four terms in chain order|(10,0,0);(0,2,0);(-1,0,0);(0,0,1)m/s|
|Rule|Each term constant; x(t)=x0+t(9,2,1)|
|Site; ephemeris; EOP; time conversion|Not applicable: synthetic fixed-frame definition|
|Geometry|The stated F axes; identity orientation; no Cell3 numerical geometry used|
|Residual|No measured comparison supplied; not a claim of zero physical residual|
|Reconstruction|Subtract all four signed displacements from endpoint|

At t=2s this gives (19,6,5)m. The synthetic chain labels demonstrate bookkeeping; they do not turn F into a measured astronomical trajectory.

## C24.07-P1 — Reverse and audit

Reverse the endpoint: (19,6,5)-(20,0,0)-(0,4,0)-(-2,0,0)-(0,0,2)=(1,2,3)m. Subtracting the negative Earth/EMB displacement adds 2m in x.

Now prepare a real-source card from Lesson 3. Preserve ICRS, m/s, the full three-component physical vector, source SHA-256 4651a532fe43e8091748ef4f7e28bb899e1a2ea798d689ba1724e99530cd55ab and pointer `/derived_results/earth_cmb/V_E_icrs_m_s`. Mark vector epoch “not specified in inspected authority.” Site, propagation ephemeris/EOP and the complete transformation chain are not supplied for a new real propagation. Keep that operation pending rather than filling fields from publication time. The source speed remains readable; a new time-resolved laboratory path is not thereby specified.

> Scope: This is a complete synthetic trajectory and an intentionally incomplete real propagation request. A mechanism explaining an observed residual would be a separate proposed mechanism. Our input and residual records remain available whether or not such a mechanism is offered. Source facts, derived calculations, interpretations and unresolved inputs retain distinct labels.

## C24.07-D1 — Diagnostics

1. Why does total speed fail to reproduce a trajectory?
2. What must accompany a normalized direction?
3. How do you reconstruct a comparison vector from a model and residual?
4. Is an absent ephemeris the same in the toy packet and a real propagation request?

Answers: 1. Speed lacks direction, initial position, time and frame. 2. Original magnitude, units and orientation/frame metadata; multiply back to recover the vector. 3. comparison=model+residual, retaining every signed component. 4. No: it is explicitly unnecessary for the synthetic definition but a missing required input for the specified real calculation. Do not relabel missing data as zero.


Next dependency: [capstone](capstone.md). Carry your signed component ledger forward.
<!-- END: lesson-07 -->

