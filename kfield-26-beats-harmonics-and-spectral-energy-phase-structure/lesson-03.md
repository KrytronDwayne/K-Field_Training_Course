# Harmonics and spatial rulers

**Essential question:** How does motion through repeated spatial structure set a signed cycle rate?

**Goals:** Calculate projected spatial phase; calculate integer harmonic rates; preserve the information distinguishing reversed motion.

**Prerequisite bridge.** Lesson 1 counted cycles in time. Imagine parallel ruler marks: crossing one spacing advances one cycle. A vector is an ordered coordinate list. Its dot product multiplies matching entries and adds: (a,b,c)·(u,v,w)=au+bv+cw. This lesson uses constant velocity and needs no calculus.

## C26.03-E1 — Declare the ruler and origin

Let n be a unit normal to parallel planes, d>0 their perpendicular spacing in meters, O an origin in meters and x(t) a position in meters. A unit normal has length one. For n=(1,0,0), the dot product picks out the first coordinate. Define q(t)=n·(x(t)−O)/d in cycles. Subtracting the origin is necessary: phase depends on where the ruler starts.

For constant velocity v in m/s, x(t)=x(0)+vt. Substitution gives q(t)=q(0)+(n·v/d)t. Name the constant signed rate qdot=n·v/d cycles/s. This is a rate obtained by division; derivative notation is not needed. A negative rate means motion backward relative to n. Its repetition frequency is |qdot|.

The kth harmonic has phase 2πkq for a positive integer k. It repeats k cycles per fundamental cycle, so its signed rate is k qdot. All harmonics here use the same trajectory and origin. Harmonic indices are counts, not length units.

An optical wavelength λ is a spatial repeat length of an optical wave. The geometric ruler spacing d and wavelength λ need not be the same. Even the letter q needs a declared role: this lesson's q is cycles; source plane cost qF in Lesson 7 is a different quantity.

## C26.03-W1 — Worked synthetic geometry

Choose n=(1,0,0), O=(0,0,0) m, x(t)=(t,0,0) m with t in seconds, and d=1/2 m. Then q=t/(1/2)=2t cycles. The fundamental frequency is 2 Hz. For k=3, phase=2π·3·2t=12πt, giving cos(12πt) at 6 Hz.

At t=1/24 s the phase is π/2. The quadrature pair (cosine,sine) is (0,1). Reverse velocity: the phase is −12πt, and at that time the pair is (0,−1). Cosine alone is unchanged because it is even in angle; sine records the reversal. Keep both if direction is to remain recoverable.

## C26.03-P1 — Practice and worked answer

For d=1/2 m, n·v=−1 m/s, q(0)=0 and k=2, find rate and the quadrature pair at t=1/16 s. **Answer:** qdot=−2 cycles/s and the harmonic rate is −4 cycles/s. Phase=−8πt=−π/2, so the pair is (0,−1). Positive motion gives (0,1). Retain the orientation of n, origin, spacing and time convention.

## C26.03-D1 — Diagnostic checks and answers

1. What if motion is parallel to the planes? **Answer:** n·v=0, so this phase remains fixed even though tangential position changes. Keep the full trajectory.
2. Double d at fixed v. **Answer:** The signed rate halves, because each cycle takes twice the travel.
3. Are 1,3,9,27 all possible integer indices, and are they every integer index? **Answer:** They are possible indices, but only a subset. Their successive factor 3 defines a ternary ladder.
4. Can changing O be ignored? **Answer:** No. It changes phase by a constant. State the coordinate transformation before comparing.

> **Source scope:** This is synthetic Euclidean geometry, not a new calculation of Cell3 constants. Cell3 uses source-locked ICRS columns [a b c], an intentional negative determinant and affine displacement x−O_K. Its M_cell=BᵀB and inverse R_cell are distinct from G_phase. No matrix inversion is needed here. The ternary source ladder, Fibonacci-cutoff synthesis and proposed difference pathway are distinguished in Lesson 5.

**Next dependency:** [Lesson 4](lesson-04.md) retains both phase coordinates in finite spectral coefficients.
