# 5. Sidereal combs and event windows

Essential question: How can event selection remain independent of the signal?

Goals:

- Solve the frozen toy event equation
- Build all windows and masks
- Identify inputs needed for a physical event rule

## Prerequisite bridge

Use [Symmetry, palindromes, and signed comparisons](lesson-04.md): its retained records and operations are the inputs to this lesson.

Pacing: 2 period(s) of 55 minutes. Frozen geometry and event windows / Partial support and invalid normalized windows.

## C28.05-E1 — first principles

An event rule identifies a position or phase before inspecting signal values. Phase locates progress through a repeating cycle; an unwrapped phase may increase past 1. An integer phase k means a whole number of cycles. A comb is a list of these event locations, often drawn as narrow marks. Its purpose is to compare responses at geometrically declared positions without allowing the response to move the marks.

Our synthetic coordinate is distance z(t)=t metres when t is in seconds, with origin z=0 at t=0, normal +z and spacing 2 metres. More explicitly the speed is 1 metre/second. Hence q=z/(2 metres)=t/(2 seconds) cycles. The shorthand q=t/2 assumes the numerical t is in seconds. This is a toy trajectory, not a physical celestial model. Solve q=k: t=2k seconds. In the closed midpoint range [0,4] seconds, k=0,1,2 gives events 0,2,4 seconds.

Freeze a mapping rule: use exact existing integer-second midpoint samples at offsets -1,0,+1 second, do not interpolate, and retain absent support. The offsets describe a three-sample window, not the continuous exposure durations. Exposure intervals remain separate metadata. At center 2, samples are at 1,2,3 seconds, giving raw A=(5,8,1). Side difference 5-1=4 tests same polarity; side sum 5+1=6 tests inverted polarity. The center 8 is also retained: under reversal it contributes same component 8, inverted component 0.

The full windows are center 0: (absent,2,5); center 2: (5,8,1); center 4: (1,3,absent). Their raw support masks are (0,1,1),(1,1,1),(1,1,0), where 1 means an acquired value exists. Row 3's stipulated diagnostic flag travels with both windows that use it. A separate normalized-validity mask is (0,1,0),(0,1,1),(1,1,0). None of the three ratio windows is complete. Do not fill the absent edge with zero or divide by zero to make the windows look alike.

A sidereal event is tied to orientation relative to celestial directions. A real calculation needs an observer site, time scale, astronomical position source (ephemeris), its version, vector origin, orientation frame, crossing equation and calibration interval. A direction alone is not a timestamp. Geometry and fitted response parameters have different roles: a calibration run may estimate response, while a later check run uses frozen parameters. Changing a center after seeing values creates a new exploratory analysis version.

> Claim scope: The event geometry is synthetic and frozen by definition. It is not a measured sidereal law or an astronomical prediction.

## C28.05-W1 — worked example

Use a declared synthetic phase q(t)=t/2 cycles and events q=k, yielding t=0,2,4 s. Freeze integer-second sample offsets (-1,0,1) around each event. At center 2 s, raw A window is (5,8,1); side same-polarity difference 5-1=4 and inverted sum 5+1=6. Retain center 8 and both defects.

## C28.05-P1 — guided practice

**Student task.** Using the common acquisition and frozen offsets (-1,0,1) s, list the windows centered at 0 and 4 s, their raw masks, and their ratio-validity masks. Then build the normalized center-2 window and explain why it is incomplete. Retain reasons for every missing or invalid entry.

### Worked answer

At center 0 s the negative-time sample is absent; at center 4 s the 5 s sample is absent. Keep partial-support windows and masks. The normalized center 2 window includes an invalid ratio at t=1 because Clear=0; report it as incomplete while retaining the complete raw window.

Center 0: raw (absent,2,5), raw mask (0,1,1), ratio (absent,1/5,undefined), ratio mask (0,1,0). Center 4: raw (1,3,absent), raw mask (1,1,0), ratio (1/10,3/10,absent), ratio mask (1,1,0). Center 2 ratio is (undefined,2/5,1/10), mask (0,1,1). Undefined arises from recorded C=0; absent means no acquisition at the requested offset. Row-3 fault travels separately.

## C28.05-D1 — diagnostic checks

1. Solve q=k over midpoint range [0,4].
2. What is the raw center-2 side difference and sum?
3. May the missing sample at -1 second be set to zero?
4. What physical inputs does q=t/2 lack?

## Worked answers

1. t=2k seconds gives 0,2,4 for k=0,1,2.
2. 5-1=4 and 5+1=6; retain the center 8 and flags.
3. No. Preserve a missing-support label and the partial window.
4. A physical site, UTC epoch/time scale, ephemeris/version, orientation and event definition; the toy rule supplies none of them.

Next dependency: [lesson-06](lesson-06.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
