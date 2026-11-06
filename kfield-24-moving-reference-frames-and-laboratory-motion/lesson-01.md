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
