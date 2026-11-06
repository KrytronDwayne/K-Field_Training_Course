# Plane Crossings, Rulers, and Event Geometry

Student course — seven lessons, eleven core periods. See [course map](course-map.md), [glossary](terminology.md), [capstone and key](capstone.md), [teacher guide](teacher-guide.md) and [source notes](source-notes.md). All teaching below is reproduced verbatim from the audited lesson files.

<!-- BEGIN: lesson-01 -->
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
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — Crossing rates from velocity

**Essential question:** Which part of velocity changes the sheet coordinate?

**Goals:** Derive a fixed-family rate from two positions; preserve sign and dimensions; identify extra inputs when geometry moves.

**Time:** Two 55-minute periods, each retrieval 5, teaching/example 20, practice 15, checks/repair 15. Period 1 covers fixed geometry and P1; period 2 covers changing geometry, P2 and D3–D4.

**Prerequisite bridge:** Lesson 1 gives q=n·(x−o)/d. Velocity is displacement divided by elapsed time, separately for each coordinate. A delta Δ means final minus initial: Δx=x(t_2)−x(t_1), Δt=t_2−t_1>0.

## C25.02-E1 — Derive before naming

Hold n,o,d fixed. Subtract q values; the origin terms cancel, leaving Δq=n·Δx/d. Divide by Δt. For constant velocity v=Δx/Δt:

`signed rate r=Δq/Δt=n·v/d`.

The **projected velocity** n·v has units m/s. Dividing by spacing in metres gives s⁻¹. Positive r increases sheet index; negative r decreases it. Absolute value |r| is unsigned; save r alongside it. A rate of 2 s⁻¹ means two spacings per second, not necessarily two recorded events in every short window. Starting phase and endpoint inclusion matter.

The dot notation q̇ means instantaneous rate. For linear motion it equals r. When motion changes, a finite ratio is an average; q̇ describes the rate approached over shorter intervals at one instant. No limit calculations are required here.

## C25.02-W1 — Worked projection and reversal

For n=(3/5,4/5,0), d=3/5 m, v=(2,0,0) m/s, n·v=6/5 m/s. Therefore r=(6/5)/(3/5)=2 s⁻¹. Independent check: in half a second x advances 1 m; its projection advances 3/5 m, exactly one spacing, giving 1/(1/2 s)=2 s⁻¹.

Reverse v to (−2,0,0) m/s. Projection becomes −6/5 m/s and r=−2 s⁻¹. Both magnitudes are 2 Hz if one cycle denotes a sheet interval, but sheet orders are opposite. Taking absolute value alone loses direction.

## C25.02-P1 — Practice and worked answer

Let n=(0,1,0), d=1 m. Find r for v=(2,0,0) and v=(0,−3,0) m/s. How long does the nonzero constant rate take to traverse one interval?

**Answer:** First dot product is zero; r=0 and motion is parallel to sheets. There is no finite traversal period. A path already on a sheet may remain on it. Second dot product is −3 m/s; r=−3 s⁻¹. Three spacings per second gives a positive interval of 1/3 s, with direction still negative.

## Moving geometry — finite replay first

Take n=(1,0,0), d=1 m, x(t)=((2 m/s)t,0,0), but o(t)=((1 m/s)t,0,0). At 0 s, q=0. At 1 s, x−o=(1,0,0) m, so q=1. The rate is 1 s⁻¹. Using sensor velocity alone gives a wrong result because the sheets move too.

If normal or spacing changes, evaluate their values at both endpoints. For stationary x=(2,0,0) m, o=0, n=(1,0,0), let d rise from 1 m to 2 m over one second. Then q changes from 2 to 1: average rate −1 s⁻¹ despite zero sensor velocity.

**C25.02-P2:** Sensor and origin both move at (2,0,0) m/s. Initially x−o=(3,0,0) m; n=(1,0,0), d=1 m. Find q at 0 and 2 s. **Answer:** Relative position stays 3 m, so both values are 3 and rate is zero. Record persistent occupancy of sheet 3, not an isolated passage.

**Recognition-only full derivative:** For differentiable inputs,

`q̇=[ṅ·(x−o)+n·(v−ȯ)]/d − q ḋ/d`.

Here ṅ is normal rate, ȯ origin velocity, ḋ spacing rate. The terms describe turning sheets, relative translation and changing scale; each has units s⁻¹. This is a product/quotient derivative rule. Its calculus derivation is outside the assessed core; endpoint replay is required and taught above. Fixed-family rate cannot be applied to changing geometry without checking the extra terms.

> **Claim scope:** These are synthetic kinematics. T10 distinguishes directional crossing rate and magnitude-based beat frequency under its own contract. A geometric rate alone does not establish detector response. T45 preserves separate display scales and specified motion inputs; camera movement does not supply missing physical velocities.

## Diagnostics

1. **C25.02-D1:** Why is zero rate not a zero-second period?
2. **C25.02-D2:** Projected velocity is −4 m/s and d=2 m. Give signed/unsigned rates.
3. **C25.02-D3:** Which input changes in the moving-origin example, and what rate results?
4. **C25.02-D4:** Can n·v/d alone capture changing spacing for a stationary point?

**Worked answers:** (1) Traversal time requires dividing by a nonzero rate; zero has no finite traversal period. (2) −2 s⁻¹ and 2 s⁻¹, decreasing sheet index. (3) Origin moves at 1 m/s and sensor at 2 m/s; relative projection gives 1 s⁻¹. (4) No: q changed from 2 to 1 while v=0. Use the full definition and spacing history.

**Next dependency:** [Lesson 3](lesson-03.md) converts constant rates into time scales.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — Spatial spacing and a temporal signal

**Essential question:** When does equally spaced geometry give equally spaced event times?

**Goals:** Compute a traversal period; convert cycles to radians; preserve a changing-rate path instead of replacing it with one average.

**Time:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

**Prerequisite bridge:** Lesson 2 gives r=n·v/d. Time to travel a distance at constant speed is distance divided by speed. Here use perpendicular spacing and |n·v|, not full speed along the path.

## C25.03-E1 — Period and phase

For a fixed family and constant nonzero projected velocity,

`T=d/|n·v|=1/|r|`.

Metres divided by metres per second gives seconds. T separates successive passage times; initial q determines the wait to the first event. Unsigned frequency f=1/T is measured in hertz (Hz), cycles per second. Spatial frequency 1/d instead counts intervals per metre.

One full turn is 2π radians; π is the circle constant and radians measure angle. A half turn is π, a quarter turn π/2. When one sheet interval is one cycle, **unwrapped phase** is φ=2πq radians. Unwrapped means retaining accumulated turns, including negative values, instead of resetting after each turn. For q=rt+q_0, φ=2πrt+2πq_0; signed angular rate is 2πr rad/s.

## C25.03-W1 — Worked event sequence

With d=3/5 m and projected velocity 6/5 m/s, T=(3/5)/(6/5)=1/2 s. Start q(0)=0. Then q=2t for t in seconds. Solving q=k gives:

| Sheet k | Time (s) | Phase (rad) |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 1/2 | 2π |
| 2 | 1 | 4π |
| 3 | 3/2 | 6π |

Reversing the path gives q=−2t. Times remain 0,1/2,1,3/2 s, indices become 0,−1,−2,−3 and phase becomes 0,−2π,−4π,−6π. A positive period cannot replace the signed sequence. The endpoint at 0 is classified as a passage using the declared linear extension around 0, not two observations inside this interval.

## C25.03-P1 — Practice and worked answer

Keep projected velocity 6/5 m/s but declare a separate family with d=6/5 m. Find T,f. For the original q=2t, find φ and its value at 1/4 s.

**Answer:** T=(6/5)/(6/5)=1 s, f=1 Hz. Doubling spacing halves rate. Keep a new family ID, preserving the original ledger. Original φ=4πt rad for t in seconds; φ(1/4)=π rad.

## Changing-rate bridge without calculus

For piecewise constant rates, accumulate each signed change Δq=rΔt. Start q=0. Let r=1 s⁻¹ on [0,1] s and 3 s⁻¹ on [1,2] s, maintaining continuity. Then q(1)=1 and q(2)=1+3=4. Events k=0,1,2,3,4 occur at 0,1,4/3,5/3,2 s. Average rate is 4/2=2 s⁻¹, but a constant-rate replacement puts k=1 at 1/2 s, wrongly moving the event.

**C25.03-P2:** Start q=0 with r=2 s⁻¹ for one second then −2 s⁻¹ for one second. Find q at 0,1,2 s. **Answer:** 0,2,0. Average is zero because signed changes cancel; motion and sheet encounters still occurred. Keep both segments and the reversal. Accumulating rates over arbitrarily short intervals is called integration; no integral calculation is required here.

> **Claim scope:** Tables are synthetic derived geometry. A periodic phase can be an input to a response model. A measured signal additionally needs a response law and observations. Preserve any observed response as model plus residual, with original values recoverable.

## Diagnostics

1. **C25.03-D1:** Give units of 1/d, r and angular rate. Does zero instantaneous rate rule out a contact?
2. **C25.03-D2:** If q(0)=1/4 and r=2 s⁻¹, when is sheet 1 reached?
3. **C25.03-D3:** Convert q=−3/4 to radians.
4. **C25.03-D4:** Why does an average rate fail to place every variable-rate event?

**Worked answers:** (1) m⁻¹, s⁻¹, rad/s. No; a path can touch and reverse, as Lesson 5 shows. (2) 1/4+2t=1 gives 3/8 s. (3) −3π/2 rad. (4) It retains total signed change but loses its timing; the worked example's event at 1 s would move to 1/2 s.

**Next dependency:** [Lesson 4](lesson-04.md) examines each ruler's physical meaning.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 4 — Optical, oscillator, and crystal rulers

**Essential question:** When can we compare two rates without treating their physical sources as identical?

**Goals:** Classify length and time rulers; calculate a comparison with supplied speed; separate a numerical difference from an observed detector beat.

**Time:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

**Prerequisite bridge:** Lesson 3 converts a length spacing and projected velocity into a passage frequency. A ruler's unit is necessary information, but it does not completely describe what is being counted.

## C25.04-E1 — Attach a meaning to each number

T10 names three ruler semantics: optical wavelength, oscillator period and matter crystal spacing. A wavelength is the distance between repeating wave phases at a specified time and in a specified medium/frame. An oscillator period is the time for a repeating process to complete a cycle. Crystal spacing is a distance between declared material planes. The word “ruler” allows a calculation to use one of these spacings; it does not make the physical objects interchangeable.

| Input | Unit | Meaning | Additional input for a rate or length |
|---|---|---|---|
| Optical wavelength λ | m | Repeating optical phase spacing | Relative phase motion and geometry for actual encounters |
| Oscillator period P | s | Time per cycle | f_osc=1/P; length also needs a declared speed |
| Crystal spacing d_crystal | m | Material plane separation | Sensor/material relative projected velocity |

If a wave propagates at speed u and has period P, it travels uP in one cycle. Thus its wavelength is λ=uP under that wave's propagation model. Sensor velocity is not automatically u. If a ruler is deliberately treated as a fixed reference grid, r=n·v/d applies; if its actual phase sheets move, Lesson 2 requires their motion too.

To compare two nonnegative frequencies on one time convention, we may define a **difference frequency** f_diff=|f_1−f_2|. Subtract first, then take absolute value. This arithmetic does not supply the interaction or detection law needed for a physical beat. A baseband signal is a lower-frequency detector output; an exposure average alone specifies no frequency-conversion mechanism. THz means 10¹² Hz, a unit scale, not a detector transfer rule.

## C25.04-W1 — Worked synthetic comparison

Declare a fixed reference-grid model with projected velocity +2 m/s. An illustrative optical-length ruler λ=0.5 m gives r_opt=2/0.5=+4 s⁻¹. A separate crystal-spacing ruler d_crystal=0.25 m gives r_crystal=2/0.25=+8 s⁻¹. These are intentionally large teaching spacings, not claims about a real optical or crystal experiment. An independent oscillator with P=0.5 s has f_osc=2 Hz.

Under the declared comparison f_diff=||r_opt|−f_osc|, the difference is |4−2|=2 Hz. It is a derived comparison index, not an established optical detector beat. The rate 4 used the reference-grid assumption, not an unstated light propagation speed.

## C25.04-P1 — Practice and worked answer

An oscillator period is 1/4 s. A separate hypothetical propagation model expressly supplies u=3 m/s. Compute frequency and wavelength. Reverse the sensor in W1; report what reverses and what remains positive.

**Answer:** f_osc=1/(1/4)=4 Hz. λ=uP=3×1/4=3/4 m. The speed belongs to this hypothetical propagation model, not to ordinary light or to the sensor. W1 passage rates become −4 and −8 s⁻¹; their magnitudes stay 4 and 8. The P=1/4 s oscillator frequency remains +4 Hz. The W1 oscillator with P=1/2 s is a different input and remains +2 Hz. Keep the two oscillator IDs.

> **Claim scope:** T10's ruler categories and its directional/magnitude distinction are source facts. All numbers above are synthetic. T10 reports a physical Earth/CMB speed of 369812.50200040644 m/s in ICRS; that source value is not used as a propagation speed, phase-transformed velocity or universal speed in these exercises. A proposed detector mechanism must declare its own transfer inputs.

## Diagnostics

1. **C25.04-D1:** Two rates are both 4 Hz. Does this identify their mechanisms?
2. **C25.04-D2:** A period of 2 s is given without speed. Can you assign a wavelength?
3. **C25.04-D3:** Compare rates 7 Hz and 3 Hz under the defined difference rule.
4. **C25.04-D4:** Why is “average a THz input, therefore obtain this baseband beat” incomplete?

**Worked answers:** (1) No: equal values and units do not identify their physical roles. Retain labels, speeds and clocks. (2) Frequency is 1/2 Hz; wavelength is unresolved without speed/propagation model. (3) |7−3|=4 Hz, retaining both original rates. (4) It omits the detector response, interaction and exposure-transfer model. Preserve that missing-input status rather than inventing a conversion.

**Next dependency:** [Lesson 5](lesson-05.md) locates events from a declared signed path and tests what endpoint samples can establish.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — Events and interpolation

**Essential question:** What does a pair of signed samples actually tell us about the events between them?

**Goals:** Locate a zero on a linear segment; distinguish transverse passage, contact and discontinuity; preserve brackets, multiple roots and gaps.

**Time:** Three 55-minute periods, each retrieval 5, teaching/example 20, practice 15, checks/repair 15. Period 1: linear interpolation and P1a. Period 2: multiple roots and contacts, P1b and P2. Period 3: discontinuities, gaps, uncertainty, P1c and diagnostics.

**Prerequisite bridge:** From Lesson 1, an event on sheet k satisfies s_k=0. We now call the selected sheet's signed distance s(t) to keep notation short. A **root** is a time where that value equals zero. A **bracket** [a,b] records both endpoint times, values and the rule trusted between them.

## C25.05-E1 — Continuity is part of the input

A continuous path changes without a jump. If s(a)<0 and s(b)>0, continuity guarantees at least one root between a and b: the value cannot get from negative to positive while skipping zero. This statement guarantees existence, not uniqueness. It needs continuity on the whole interval. A straight line with nonzero slope is a special case that crosses zero exactly once.

For a declared linear segment, change per second is (s_b−s_a)/(b−a). At time t the distance is s_a+(s_b−s_a)(t−a)/(b−a). Set that expression to zero and solve:

`t*=a − s_a(b−a)/(s_b−s_a)`.

The numerator has units m·s and denominator m, giving seconds. If endpoint values are equal, this division fails: equal nonzero values define a constant nonzero linear segment with no root; two zero values define continuous occupancy under the linear rule. Neither case is an isolated crossing.

## C25.05-W1 — Worked brackets and hidden roots

Let a=0 s, b=2 s, s_a=−2/5 m, s_b=6/5 m, and explicitly assume a linear segment. Difference is 8/5 m. Thus t*=0−(−2/5)(2)/(8/5)=1/2 s. Recheck using slope (8/5)/2=4/5 m/s: −2/5+(4/5)(1/2)=0 m. Save the original [0,2] s bracket and both endpoints alongside the exact model root.

Now use a different path s(t)=(1 m)(τ−1)(τ−2), where τ=t/(1 s) is numerical time in seconds. Multiplication gives zero whenever either factor is zero, so roots are 1 and 2 s. At 0 and 3 s, s=2 m in both cases. Equal endpoint signs did not imply absence. At 1/2 s s=3/4 m; at 3/2 s s=−1/4 m; at 5/2 s s=3/4 m. Hence the first passage is positive-to-negative and the second negative-to-positive.

## C25.05-P1 — Three practice cases

**a.** A linear path has s(1 s)=−1 m and s(3 s)=3 m. Locate the root and verify it.

**b.** For s(t)=(1 m)(τ−1)², classify the zero at 1 s using nearby values.

**c.** Let s=−1 m for t<1 s and +1 m for t≥1 s. Do opposite signs at 0 and 2 s guarantee a zero?

**Worked answers:** (a) t*=1−(−1)(2)/4=3/2 s. Slope is 2 m/s; s(3/2)=−1+2(1/2)=0 m. (b) Squaring gives nonnegative values, with s=0 only at 1 s. Both 1/2 and 3/2 s give 1/4 m. This is a tangent contact: it touches and returns to the same side. Its instantaneous rate is zero; no calculus is needed to classify the equal-side pattern. (c) No: the path jumps and never takes the value zero. Save a discontinuity row, not an interpolated passage.

## Refinement, uncertainty and unresolved intervals

When a continuous path is known but not linear, halve a sign-changing bracket and evaluate the midpoint. Keep a smaller sign-changing bracket while preserving all earlier evaluations. This procedure is called bisection. A midpoint zero is an exact evaluated root; otherwise a finite bracket locates a root without pretending to know the exact time. It does not prove no other roots exist.

**C25.05-P2:** Let s(t)=(1 m)(τ²−2). Starting with [1,2] s, evaluate 1.5 s, then 1.25 s. **Answer:** Endpoint values are −1 and +2 m. At 1.5 s the value is +0.25 m, giving [1,1.5] s. At 1.25 s it is −0.4375 m, giving [1.25,1.5] s. All five values remain available. This is localization, not a claim of a measured timing uncertainty. A continuous increasing positive-time square has just one root here, but the generic sign-change rule alone does not give uniqueness.

If values inside (1,2) s are unavailable, retain a gap row with all known endpoints and any independent continuity information. Without a path model, do not draw a line through the missing interval and report its root as exact. If continuity is independently assured and opposite endpoints are known, existence is justified but root count and times remain unresolved. If continuity is unknown, even existence is unresolved. A failed midpoint evaluation leaves the previous bracket valid under its previous assumptions; store the failed attempt.

For measurement uncertainty, retain original values and their supplied bounds separately. A bound spanning zero cannot certify the sample's sign. For example a reported −0.02 m with bound ±0.05 m permits [−0.07,0.03] m. Do not choose the preferred sign. If no bounds were supplied, write “not supplied”; synthetic exact arithmetic is not evidence of zero instrument uncertainty.

> **Claim scope:** Existence follows mathematically from continuity and signs. Linear interpolation is exact within a stated linear model; for samples of an unspecified curve it is only a model estimate. Contacts, failed refinements, endpoint roots, jumps and gaps are information, not disposable exceptions.

## Diagnostics

1. **C25.05-D1:** Known endpoint values straddle an unknown gap. What must the ledger retain?
2. **C25.05-D2:** Does a continuous sign change prove exactly one root?
3. **C25.05-D3:** A root lies at a shared endpoint of two adjacent brackets. Count it once or twice?
4. **C25.05-D4:** Is a tangent contact a negative-to-positive passage?
5. **C25.05-D5:** What is lost by replacing the original bracket with only its refined midpoint?

**Worked answers:** (1) Both values/times, gap, geometry, continuity status and unresolved timing/count; existence only if continuity is known. (2) No; there may be multiple roots. (3) One event ID for that same family/sheet/time, retaining both supporting brackets. Different families retain distinct rows even at the same time. (4) No; the square example is positive on both sides, with zero at contact. (5) Original sample evidence, sign checks and localization bounds. Retain every refinement and failure with provenance.

**Next dependency:** [Lesson 6](lesson-06.md) applies event equations to angles and separates celestial meridians from spatial sheets.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — Meridian events versus spatial-sheet passages

**Essential question:** How can two events share a time but answer different geometric questions?

**Goals:** Solve simple meridian and quadrature equations; unwrap an angular coordinate; label celestial-direction and spatial events separately.

**Time:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

**Prerequisite bridge:** Lesson 3 taught full turn 2π, half turn π and quarter turn π/2. Lesson 5 taught that an event needs a declared equation. We now use angular equations as well as s_k=0. No actual sky ephemeris calculation is required.

## C25.06-E1 — State the equation first

The local meridian is the sky's north–south reference great circle through the observer's zenith and celestial poles. Right ascension RA labels a celestial direction around the equatorial coordinate system. Local sidereal time LST labels the right ascension on the upper meridian. For this course's convention, the **hour angle** is H=LST−RA, increasing toward the west. Express both inputs in the same angular unit before subtraction.

Angles differing by a whole number of turns describe the same wrapped direction. The notation “mod 2π” means “up to adding whole turns.” With integer j:

| Event type | Equation for unwrapped H |
|---|---|
| Upper meridian passage | H=2πj |
| Lower meridian passage | H=(2j+1)π |
| Positive quadrature | H=π/2+2πj |
| Negative quadrature | H=−π/2+2πj |

Here quadrature means hour-angle quadrature relative to the meridian; it does not assert an object's angular separation from the Sun. Upper/lower labels distinguish two halves of the meridian circle, not necessarily visible versus hidden objects.

A spatial sheet passage instead satisfies q(t)=k using position, origin, normal and spacing. A celestial **direction-plane event** may be defined by n·u(t)=0, where u is the dimensionless unit sightline and the plane passes through the direction-space origin. This asks whether a sightline lies in a plane, not whether the sensor occupies a physical sheet. An offset sheet, a direction-plane crossing and a meridian passage have different inputs. Record the event type even if their times coincide.

## C25.06-W1 — Worked synthetic clocks

On 0≤t≤2 h, let H(t)=(π/2 rad/h)t for a fictional object Star S. It reaches H=0 at 0 h (upper), π/2 at 1 h (positive quadrature), and π at 2 h (lower). A separate spatial path q(t)=(t/(1 h))−1/2 reaches sheet k=0 at 1/2 h. At that time H=π/4, none of the tabulated meridian/quadrature values. Thus the sheet event does not imply a meridian event.

The spatial q can be realized by n=(1,0,0), o=0, d=1 m, x=((t/(1 h)−1/2) m,0,0). This complete input card prevents confusing angular and spatial coordinates.

## C25.06-P1 — Practice and worked answer

Use fictional Star R, H(t)=π(t/(1 h)−1) rad on [0,2] h. A separate spatial path has q(t)=2t/(1 h), realized by n=(1,0,0), o=0, d=1 m, x=((2 m/h)t,0,0). Find upper/lower passages and the k=1 sheet event. Add both quadratures.

**Answer:** Upper: H=0 gives t=1 h. Lower: H=−π at 0 h and +π at 2 h; they are distinct endpoint events with different unwrapped branches. Negative quadrature is at 1/2 h; positive quadrature at 3/2 h. The sheet k=1 also occurs at 1/2 h. Keep two rows at that time: Star R negative quadrature and spatial-family k=1. Coincidence does not identify their equations.

## Unwrapping preserves the turn count

RA and LST are often expressed in angular hours, where 24 angular hours equal 2π radians; these are not elapsed civil hours. A displayed angle changing from 23.9 angular hours to 0.1 may be a small forward step through the display boundary. If continuous forward motion less than half a turn is independently known, unwrap the second value as 24.1, giving change +0.2 rather than −23.8. Save the displayed pair and the added turn count +1. Across a long gap the number of turns may be ambiguous; record that ambiguity instead of assuming the shortest change. Compute event equations on the unwrapped H track. A display wrap alone is not a physical transit.

> **Claim scope:** These are definitions and synthetic clocks, not an actual UTC event prediction. T45's source-reported 97-state sidereal display has its own specified replay; our examples do not reproduce it. Source display chambers have independent scales, and the Galactic Center is a visual gauge. No Solar or Galactic short-window time law is supplied by these examples.

## Diagnostics

1. **C25.06-D1:** Does a jump from 24 to 0 angular hours by itself demonstrate a physical transit?
2. **C25.06-D2:** Is H=3π upper or lower meridian?
3. **C25.06-D3:** In P1, what two events occur at 1/2 h?
4. **C25.06-D4:** Can n·u=0 substitute for n·(x−o)=kd?

**Worked answers:** (1) No; preserve unwrapping, time convention and event equation. (2) Lower: 3π=(2×1+1)π. (3) Negative quadrature of Star R and k=1 spatial-sheet passage. (4) No: u is a unit direction; x−o is a length displacement. They answer different questions and require separate fields.

**Next dependency:** [Lesson 7](lesson-07.md) combines typed event rows while keeping every sign, bracket and unresolved branch.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 7 — A signed crossing ledger

**Essential question:** What must an event record retain so another person can reproduce it without guessing?

**Goals:** Assemble multiple-family event rows; distinguish orientation, direction and polarity; reconstruct endpoint distances while preserving residuals and unresolved intervals.

**Time:** Two 55-minute periods, each retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Period 1 builds W1 and the reversed-family practice. Period 2 reconstructs brackets and adds contact, gap and residual rows.

**Prerequisite bridge:** Lessons 1–3 connect a full path to q, signed rate and period. Lesson 4 keeps ruler roles distinct. Lessons 5–6 distinguish event types and their existence conditions. A **ledger** is a collection of records that preserve these inputs with each derived event.

## C25.07-E1 — A record, not just a time

Use an immutable input card to avoid repeating a long path in every row. A card ID refers to the exact path, geometry, clock and evidence class. Changing any input creates a new card. Every event row needs:

| Field | What it retains |
|---|---|
| Event ID and type | Stable identity; sheet passage, contact, angular event, occupancy, gap or failure |
| Family, sheet k and input-card ID | Normal, origin, positive spacing, full path and units by reference |
| Time and epoch/clock | Numerical time plus the named start or absolute time convention |
| Bracket and signed endpoint values | Support before refinement; both adjacent brackets if applicable |
| Continuity/model rule | Linear, specified nonlinear, discontinuous or unknown |
| Direction | + for increasing q through the sheet, − for decreasing; contact/unknown separately |
| Orientation and polarity | Actual oriented normal and a separately declared polarity convention |
| Uncertainty and gaps | Model localization interval, supplied measurement bounds, unresolved inputs |
| Provenance and residual information | Source/card pointer, retained components and reconstruction rule |

For this course only, each family is assigned a **polarity label** p of +1 or −1 independently of its travel direction. It is a declared tag, not detector parity, chirality or an inferred physical charge. Never infer it from time order. If the normal reverses while origin and spacing remain fixed, q and k must both change sign to describe the same physical sheet; its direction reverses in the new coordinate convention. Retain both orientations, not an unsigned normal alone.

## C25.07-W1 — Worked two-family ledger

**Input card SYN-FWD:** Fixed perpendicular Cartesian axes; synthetic elapsed seconds from epoch E0 (not an actual UTC date); x(t)=((2 m/s)t,0,0), defined linearly beyond both ends of reporting interval [0,3/2] s. Family A has n=(3/5,4/5,0), o=0 m, d=3/5 m, p=+1. Family B has n=(1,0,0), o=0 m, d=2 m, p=−1. The family name B here is a label, not the Cell3 basis matrix B. Both paths are exact synthetic models; measurement bounds are not applicable, not measured zero.

Projection gives q_A=2t and q_B=t for numerical seconds. Retain both families at coincident times. All rows below have direction + and transverse passage under the declared extension. The bracket column uses evaluated model points, not fabricated observations. Distances refer to that row's sheet.

| ID | Family:k | Time s | Bracket s | Endpoint s_k values m | p |
|---|---|---:|---|---|---:|
| F-A0 | A:0 | 0 | [0,1/2] | [0,3/5] | +1 |
| F-A1 | A:1 | 1/2 | [0,1] | [−3/5,3/5] | +1 |
| F-A2 | A:2 | 1 | [1/2,3/2] | [−3/5,3/5] | +1 |
| F-A3 | A:3 | 3/2 | [1,3/2] | [−3/5,0] | +1 |
| F-B0 | B:0 | 0 | [0,1] | [0,2] | −1 |
| F-B1 | B:1 | 1 | [1/2,3/2] | [−1,1] | −1 |

Time roots are exact within SYN-FWD, so localization intervals are singleton sets {t}; retain the broader supporting brackets anyway. Boundary rows explicitly rely on the model extension for two-sided passage. Without that extension label them endpoint occupancy with only one-sided evidence. F-A2 and F-B1 both occur at 1 s, but belong to different sheet families. They are neither duplicate entries nor two independent observations: they are derived events on one synthetic trajectory.

Reconstruct F-A2 at its endpoints: s_2=(3/5)(2t−2). At 1/2 s this is −3/5 m; at 3/2 s it is +3/5 m. Reconstruct F-B1 using s_1=2(t−1), obtaining −1 and +1 m. Replaying q does not recover movement parallel to sheets; SYN-FWD preserves all original path components.

## C25.07-P1 — Practice and worked answer

Create SYN-REV by replacing x with ((−2 m/s)t,0,0), preserving geometry, polarity and extension. Report every A event on [0,3/2] s and all B events. Add separate input cards for Lesson 5's tangent s=(1 m)(t/(1 s)−1)² and a gap with known s(1 s)=−1 m, s(2 s)=+1 m, no values inside and unknown continuity. Use n=(1,0,0), o=0, d=1 m, k=0 and x=(s,0,0) for both separate cases; declare p=+1. The tangent is defined on [0,2] s. The gap card supplies no interpolating path.

**Worked answer:** q_A=−2t, q_B=−t. A indices are 0,−1,−2,−3 at 0,1/2,1,3/2 s, all direction −. B indices 0,−1 occur at 0,1 s, also direction −. Their polarities remain A:+1, B:−1. Use the same brackets as W1; the endpoint-distance pairs are the negatives of W1's corresponding pairs, because both q and k negate. For example A:−2 gives s_(−2)=(3/5)(−2t+2), hence +3/5 and −3/5 m on [1/2,3/2]. B:−1 gives s=2(−t+1), hence +1 and −1 m there.

Add T-0: tangent contact at 1 s, bracket [0,2] s with distances [1,1] m, direction “contact; no sign reversal,” localization {1 s}, exact quadratic model, p=+1. Add G-0: unresolved interval (1,2) s with endpoints [−1,+1] m, unknown continuity, time/count/direction unknown, p=+1. The gap is a row, not evidence of absence or a fabricated t=1.5 s passage.

## Residual reconstruction and uncertainty

If an observed signed coordinate y and model m are available, define residual e=y−m and preserve y=m+e. For a small synthetic illustration at times [0,1,2] s, let y=[0,11/10,19/10] m and m=[0,1,2] m. Then e=[0,1/10,−1/10] m. Addition reconstructs every y, including the negative residual. Averaging e to zero would lose its ordered structure. These are illustrative sample values, not source data or instrument evidence.

**C25.07-P2:** Reconstruct y at 2 s; then suppose its supplied bound is ±1/20 m. What is retained? **Answer:** 2+(−1/10)=19/10 m. Keep y, m, e, timestamp and bound; the allowed y interval is [37/20,39/20] m. The residual describes a difference; the bound describes supplied uncertainty. Neither substitutes for the other. For a real archive, reference original records in place rather than duplicating raw data.

> **Claim scope:** A signed ledger preserves derived structure and its provenance. It supplies no force or measured energy claim. Mechanisms remain separate hypotheses. Source-reported empirical rows must keep their own identifiers, uncertainties and dependencies; a new teaching ledger is not a replacement for them.

## Diagnostics

1. **C25.07-D1:** Can polarity be recovered by sorting event times?
2. **C25.07-D2:** Should F-A2 and F-B1 be merged because their times match?
3. **C25.07-D3:** What does an unknown gap permit you to say about its event time?
4. **C25.07-D4:** For y=9/10 m and model m=1 m, give the residual and reconstruction.
5. **C25.07-D5:** What changes when the normal is reversed but the same physical sheet is described?

**Worked answers:** (1) No: p is a separately declared convention. (2) No: retain both family IDs and shared-trajectory dependence. (3) Timing and count remain unresolved without sufficient path/continuity information. (4) e=−1/10 m and 1−1/10=9/10 m. (5) n,q,k and coordinate direction negate; d stays positive. Keep the orientation revision and separately specified polarity; do not silently identify the two signed ledgers.

**Next dependency:** [Capstone](capstone.md) assembles and audits a complete synthetic ledger using these same operations.
<!-- END: lesson-07 -->
