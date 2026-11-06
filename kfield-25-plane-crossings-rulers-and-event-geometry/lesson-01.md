# Lesson 1 — Signed distance to a plane

**Essential question:** How can one number tell us which side of a sheet a sensor occupies?

**Goals:** Compute a dot product; distinguish signed distance from sheet count; retain the origin, orientation and full path needed for replay.

**Time:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

**Prerequisite bridge:** You can add signed fractions and substitute time into a linear equation. A position is an ordered list of three coordinates. Earlier courses supply coordinate frames; here we review every operation needed. All three coordinates below use perpendicular axes with the same length unit. An oblique cell-coordinate tuple cannot be substituted as if it were a Cartesian position.

## C25.01-E1 — Build the coordinate

Imagine parallel, equally spaced sheets extending in all directions within each sheet. A normal is an arrow perpendicular to a sheet. Orienting the arrow chooses the positive side. A **unit normal** has length one and carries direction, not metres. For n=(n_x,n_y,n_z), squared length is n_x²+n_y²+n_z². To normalize a nonzero arrow, divide each component by the square root of that sum. A zero arrow cannot define a normal.

Choose a fixed origin o, positive spacing d and position x. Subtract positions component by component, then take the **dot product**:

`n·(x−o)=n_x(x_x−o_x)+n_y(x_y−o_y)+n_z(x_z−o_z)`.

This adds displacement components weighted by how much the normal points along each axis. For a unit normal the result is signed perpendicular distance to the sheet through o. Moving within that sheet contributes zero. Negative distance means the opposite side of the chosen normal; ordinary nonnegative distance is its absolute value.

Number sheets by integers k: …,−2,−1,0,1,2,… . Sheet k obeys n·(x−o)=kd. Define:

- `s_k=n·(x−o)−kd`: signed distance to sheet k, in metres here.
- `q=n·(x−o)/d`: dimensionless sheet coordinate, also called phase in cycles.
- `s_k=d(q−k)`: reconstruction from q and sheet index.

An event on sheet k requires q=k. At q=1/2 the sensor is halfway between sheets 0 and 1. No rounding is required. Cell3 half-open cell ownership is a separate operation, not an event definition.

## C25.01-W1 — Worked synthetic path

Use n=(3/5,4/5,0), o=(0,0,0) m, d=3/5 m. Let t be elapsed seconds from a synthetic start and x(t)=((2 m/s)t,0,0). Writing x=(2t,0,0) m is shorthand only when t denotes its numerical value in seconds.

The squared normal length is 9/25+16/25=1. Projection is (3/5)(2 m/s)t=(6/5 m/s)t. Dividing by 3/5 m gives q=(2/s)t. At t=1/4 s, s_0=3/10 m and q=1/2. Distance to sheet 1 is 3/10−3/5=−3/10 m. Solve 2t=1, with t in seconds, to get the sheet-1 event t=1/2 s; substitution gives s_1=0.

> **Claim scope:** This is synthetic Cartesian geometry, not the mature Cell3 basis or measured motion. T10 supplies ruler vocabulary; arithmetic follows from our declarations. Source ICRS columns and handedness remain unchanged. Scalar q cannot reconstruct a whole position, so keep all components of x(t).

## C25.01-P1 — Practice and worked answer

Keep n,o,d but use x(t)=((−2 m/s)t,0,0). Find q and s_(−1) at 1/2 s. In a separately labeled geometry revision, set o=(1,0,0) m; find the shift in q.

**Answer:** Projection at 1/2 s is −3/5 m. Thus q=−1 and s_(−1)=−3/5−(−1)(3/5)=0 m. The new origin subtracts 3/5 m from the projection, shifting q by −1: q_new=−2t−1 for t in seconds. Keep both geometry IDs. This particular full-spacing shift reindexes the same sheet set but changes the sheet called zero.

## Diagnostics

1. **C25.01-D1:** Is q=−2 invalid? What if d=0?
2. **C25.01-D2:** Normalize (3,4,0). Why is its original dot product not distance?
3. **C25.01-D3:** For q=3/2 and d=2 m, find s_1 and s_2.
4. **C25.01-D4:** Can q reveal motion along a sheet?

**Worked answers:** (1) Negative q preserves side and index. Zero d makes division undefined; retain a geometry-failure status. (2) Length √25=5 gives (3/5,4/5,0); the original projection is five times distance. (3) 2(3/2−1)=1 m and 2(3/2−2)=−1 m. (4) No: many positions share a projection. Keep x(t), o, n, d and unprojected components.

**Next dependency:** [Lesson 2](lesson-02.md) compares signed coordinates at two times.
