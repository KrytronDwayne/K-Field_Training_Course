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
