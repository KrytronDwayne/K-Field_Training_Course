# Lesson 1 — Complex numbers and phase

Essential question: How can a number record both size and a reversible turn?

Goals: Compute a conjugate and magnitude; multiply complex numbers; rotate by a quarter-turn and reverse the operation.

Prerequisite bridge: You can plot a pair of real coordinates and expand brackets. We package a pair (a,b) as a single number a+bi. No prior complex arithmetic from course-13 is needed. Use two periods: arithmetic, then rotations and recovery.

## C14.01-E1 — Two coordinates in one number

Define i by i²=−1. The complex number z=a+bi has real component a and imaginary component b, both real numbers. The imaginary component of 2−i is −1, not −i. Plot z at (a,b). Add corresponding components. Multiply by expanding brackets and replacing i² by −1. For example, (1+i)(2−i)=2−i+2i−i²=3+i.

The conjugate is z̄=a−bi: reflection across the horizontal axis. Multiplication gives z̄z=(a−bi)(a+bi)=a²+b². This is the squared modulus |z|²; |z|=√(a²+b²) is distance from the origin. A square root here is the nonnegative number with the stated square. Keep squared lengths when comparing sizes.

Multiplying by i gives i(a+bi)=−b+ai. The point (a,b) becomes (−b,a), a counterclockwise quarter-turn. Its squared length stays b²+a². Repeated multiplication cycles through 1,i,−1,−i,1. The inverse turn multiplies by −i because (−i)i=1. Size alone does not determine z: 1 and i have the same modulus but different directions. Keep both coordinates and the rotation used.

A phase is a direction on the complex unit circle. A unit phase u has |u|=1 and ūu=1, so ū reverses multiplication by u. In angle notation u=cos θ+i sin θ, also written e^(iθ). Here this is notation for a unit-circle turn, requiring no calculus. A full turn is 2π radians, or 360°. Combining turns adds angles, so phases multiply. Powers repeat a turn; negative powers reverse it. At z=0 no unique direction exists, although every phase still sends 0 to 0.

## C14.01-W1 / C14-CX-EX1 — Worked example

For z=1+i, the conjugate is 1−i and |z|²=1²+1²=2. Rotate: iz=i+i²=−1+i. Its squared modulus is (−1)²+1²=2. Reverse: (−i)(−1+i)=i−i²=1+i. Both coordinates survive. This is synthetic arithmetic, not a measurement.

## C14.01-P1 / C14-CX-P1 — Answered practice

Rotate 2−i by i, find the new conjugate and modulus, then recover the original. Answer: i(2−i)=1+2i; conjugate 1−2i; squared modulus 1+4=5; modulus √5. Reversal gives (−i)(1+2i)=2−i. Also multiply (2+i)(1−i): 2−2i+i−i²=3−i. The rotated squared modulus 5 equals the original 4+1.

> Claim scope: Complex arithmetic and rotations are mathematical operations with dimensionless coordinates here. A physical interpretation of phase needs a separately supplied model; no force or measured field is inferred.

For a later six-fold example define ζ=(1+i√3)/2. Its conjugate is (1−i√3)/2. Check ζ̄ζ=(1−i√3)(1+i√3)/4=(1−i²·3)/4=(1+3)/4=1. Thus ζ is a unit phase, with real component 1/2 and imaginary component √3/2. This exact calculation uses only (√3)²=3, not rounded coordinates.

## Diagnostics — C14.01-D1

1. For −3+2i, give both components, conjugate, and squared modulus.
2. Rotate 1−2i by i and undo it.
3. Give two different numbers with modulus 1. What information is missing from modulus alone?
4. Compute (1+i)². Does squaring preserve its modulus?

Worked answers: (1) Components −3 and 2; conjugate −3−2i; squared modulus 9+4=13. (2) i+2=2+i, then (−i)(2+i)=1−2i. (3) 1 and i; direction is missing. (4) 1+2i+i²=2i, of modulus 2, whereas |1+i|=√2. Multiplication preserves length when its multiplier has modulus 1, not in general.

Next dependency: [Lesson 2](lesson-02.md) combines complex coordinates and tests changes of the whole tuple.
