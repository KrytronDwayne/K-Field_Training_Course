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
