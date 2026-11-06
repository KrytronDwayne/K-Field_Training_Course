# Oscillations, frequency, and phase

**Essential question:** What information lets us reconstruct an oscillation?

**Goals:** Identify amplitude, baseline, period and phase; calculate signed samples; explain the need for a time reference.

**Prerequisite bridge.** We use signed arithmetic and coordinate graphs. Earlier courses introduce reference choices; here we rebuild the circle operations we need. On a circle of radius one, a point's horizontal coordinate is cosine and its vertical coordinate is sine. These coordinates can be negative.

## C26.01-E1 — A circle becomes a signal

An angle measures a turn from the positive horizontal axis. Positive angles turn counterclockwise. One full turn is 360 degrees or 2π radians; a quarter turn is π/2 radians. A radian measures an arc whose length equals the radius. Convert degrees to radians by multiplying by π/180. The number π is approximately 3.14159.

| Angle | 0 | π/2 | π | 3π/2 | 2π |
|---|---:|---:|---:|---:|---:|
| cosine | 1 | 0 | −1 | 0 | 1 |
| sine | 0 | 1 | 0 | −1 | 0 |

The period T is the time for a full repetition. Frequency f=1/T counts cycles per second, in hertz (Hz). Angular frequency ω=2πf counts radians per second. A frequency of 2 Hz means a period of 1/2 s and angular frequency 4π radians/s.

Write x(t)=A cos(2πft+φ)+b. Time t is in seconds. The phase offset φ is the angle at the chosen time zero. Amplitude A≥0 is the maximum departure from baseline b. The quantities x, A and b have the same units. The argument of cosine is an angle, not counts. The graph lies between b−A and b+A. The varying component x−b is called AC; the constant baseline is DC. To reconstruct x, retain both.

A sine coordinate is in quadrature with cosine: sin θ=cos(θ−π/2), a quarter-turn displacement. Reversing an angle leaves cosine unchanged and changes the sign of sine. Adding π changes the sign of both coordinates. These circle facts will make direction and polarity visible later.

Evaluate a sinusoid by calculating its angle first, reading cosine second, then multiplying by A and adding b. A changed time origin changes the recorded phase offset; compare phases only after declaring that origin.

## C26.01-W1 — Worked synthetic example

Let x(t)=2 cos(πt+π/2)+1 counts, t in seconds. Matching π to 2πf gives f=1/2 Hz, T=2 s, A=2 counts, b=1 count.

| t (s) | angle | cosine | AC (counts) | x (counts) |
|---:|---:|---:|---:|---:|
| 0 | π/2 | 0 | 0 | 1 |
| 1/2 | π | −1 | −2 | −1 |
| 1 | 3π/2 | 0 | 0 | 1 |
| 3/2 | 2π | 1 | 2 | 3 |

For example, at t=1/2, 2(−1)+1=−1. The negative entry is a synthetic signed coordinate. It is not missing data. Save the spacing 1/2 s, order, baseline and every sign. The next sample at t=2 s repeats the first.

## C26.01-P1 — Practice with worked answer

For y(t)=3 cos(2πt) counts, find f,T and samples at 0,1/4,1/2,3/4 s; then add π to the phase. **Answer:** f=1 Hz and T=1 s. Angles 0,π/2,π,3π/2 give (3,0,−3,0) counts. The shifted samples are (−3,0,3,0). Keep t=0 as origin, spacing 1/4 s and baseline zero.

## C26.01-D1 — Diagnostic checks and answers

1. A period is 4 s. Find f and ω. **Answer:** 1/4 Hz and π/2 radians/s.
2. Does amplitude 3 determine x(0)? **Answer:** No: phase and baseline are needed. At baseline zero, phase 0 gives 3 and phase π gives −3.
3. At t=1/2 in W1, what is the AC value? **Answer:** −2 counts; adding baseline 1 reconstructs −1.
4. What does a maximum magnitude omit? **Answer:** Timing, phase, baseline and other samples. Keep them beside the summary.

> **Claim scope:** These are exact calculations from synthetic equations, not measured detector observations. Phase is a cycle coordinate, not force.

**Next dependency:** [Lesson 2](lesson-02.md) adds oscillations with their signs intact.
