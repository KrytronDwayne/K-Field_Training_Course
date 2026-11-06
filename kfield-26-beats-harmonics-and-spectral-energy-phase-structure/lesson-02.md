# Superposition and beat envelopes

**Essential question:** How can two oscillations create a slower variation in amplitude?

**Goals:** Derive the cosine sum identity; calculate a two-frequency beat; distinguish signed modulation frequency and absolute-envelope peak rate.

**Prerequisite bridge.** Lesson 1 taught the circle coordinates cos a and sin a. Superposition means adding signal values at the same time with common units. Whether a physical apparatus implements that addition is a separate modeling question.

## C26.02-E1 — Derive before substituting

Rotate the horizontal unit arrow through angle b: it becomes (cos b,sin b). Rotate the vertical arrow through b: it becomes (−sin b,cos b), since it is a quarter turn ahead. The point (cos a,sin a) is cos a times the horizontal arrow plus sin a times the vertical arrow. After rotation its horizontal coordinate is cos a cos b−sin a sin b, and its vertical coordinate is sin a cos b+cos a sin b. Its angle is a+b, giving the addition rules:

cos(a+b)=cos a cos b−sin a sin b;

sin(a+b)=sin a cos b+cos a sin b.

Reverse b. Since cos(−b)=cos b and sin(−b)=−sin b, we get cos(a−b)=cos a cos b+sin a sin b. Adding the two cosine equations cancels the sine products:

cos(a+b)+cos(a−b)=2 cos a cos b.

For any angles u,v set a=(u+v)/2 and b=(u−v)/2. Check by adding and subtracting these fractions that a+b=u and a−b=v. Therefore

**cos u+cos v=2 cos((u−v)/2)cos((u+v)/2).**

For two unit amplitudes with zero phase offsets, put u=2πf₁t and v=2πf₂t. For nearby positive frequencies, the factor with average frequency (f₁+f₂)/2 is called the carrier. The signed modulation factor is 2 cos(π(f₁−f₂)t), with frequency |f₁−f₂|/2. Its absolute value is the nonnegative envelope. Taking the absolute value folds negative lobes upward: envelope maxima recur at |f₁−f₂| per second. That peak rate is our beat-frequency convention.

The envelope bounds the signal amplitude. A fast carrier maximum need not coincide with every envelope maximum for arbitrary phases and frequencies. Keep the signed factor, not just that bound: a negative factor reverses carrier polarity.

## C26.02-W1 — Worked synthetic example

s(t)=cos(2π·4t)+cos(2π·6t), each term in counts, becomes 2 cos(2πt)cos(2π·5t) counts. The carrier is 5 Hz; the signed factor is 1 Hz; absolute-envelope peaks recur at 2 Hz.

At t=0, the original is 1+1=2 and the product is 2·1·1=2. At t=1/4 s, the original is cos 2π+cos 3π=0; the product is zero because cos(π/2)=0. The algebra proves equality for all times; these substitutions independently check particular values.

## C26.02-P1 — Practice (legacy C26-BEAT-P1)

Factor cos(2π·5t)+cos(2π·7t), give the three rates and evaluate at t=1/2 s. **Answer:** 2 cos(2πt)cos(12πt), with carrier 6 Hz, signed-factor frequency 1 Hz and envelope peak rate 2 Hz. At t=1/2, cos 5π+cos 7π=−2. The product is 2(−1)(1)=−2. Replacing the signed factor by its absolute value would wrongly yield +2.

## C26.02-D1 — Diagnostic checks and answers

1. For 10 and 14 Hz, find the three rates. **Answer:** Carrier 12 Hz, signed factor 2 Hz, envelope peaks 4 Hz.
2. What if both frequencies and phases are equal? **Answer:** Sum=2 cos(2πft); the factor is constant and there is no distinct peak recurrence. Opposite phases instead cancel, so phases matter.
3. Why do sine products cancel in the derivation? **Answer:** They are the same product with opposite signs after b is reversed.
4. Does a difference of source indices establish a physical coupling? **Answer:** It establishes arithmetic. A coupling proposal must additionally explain how the components and phases produce a response.

> **Claim scope:** This identity is a mathematical implication. It does not supply a detector's physical mixing or exposure-transfer mechanism.

**Next dependency:** [Lesson 3](lesson-03.md) builds frequencies from motion through a ruler.
