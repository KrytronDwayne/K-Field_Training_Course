# Beats, Harmonics, and Spectral Energy–Phase Structure

Complete student course. Eight lessons; 17 core periods of 55 minutes. Use [the capstone](capstone.md), [glossary](terminology.md), [course map](course-map.md), [teacher guide](teacher-guide.md) and [source notes](sources.md) alongside these lessons.

<!-- BEGIN: lesson-01 -->
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
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
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
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
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
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Spectral coefficients retain phase

**Essential question:** How can four coefficients retain all four samples, including timing and polarity?

**Goals:** Use powers of i to calculate a four-point transform; reconstruct all samples; distinguish spectra with equal magnitudes but different phase.

**Prerequisite bridge.** Sine and cosine are paired circle coordinates. A complex number a+bi packages two real coordinates (a,b); i is defined by i²=−1. Add matching coordinates. Multiply by distributing products and replacing i² by −1: (a+bi)(c+di)=(ac−bd)+(ad+bc)i. Multiplication by i turns (a,b) into (−b,a), a quarter turn.

## C26.04-E1 — Four roots and two conventions

The powers repeat: i⁰=1, i¹=i, i²=−1, i³=−i, i⁴=1. Negative powers run backward: i⁻¹=−i. A complex number's magnitude is √(a²+b²); its phase is its direction from the positive real axis. The conjugate of a+bi is a−bi, a reflection across that axis. Thus 2 and −2i both have magnitude 2 but phases 0 and −π/2.

The notation exp(iθ), also written e^(iθ), is shorthand here for cos θ+i sin θ. The addition rules from Lesson 2 show that multiplying these expressions adds their angles. No infinite-series definition of the exponential is needed for our finite calculations.

Let x₀,x₁,x₂,x₃ be samples at times 0,Δt,2Δt,3Δt, periodically continued for this exercise. Our forward discrete Fourier transform (DFT) is

X_k=Σ from n=0 to 3 of x_n exp(−2πikn/4), for k=0,1,2,3.

The Σ sign means add the four listed terms. The inverse has the opposite sign and a factor 1/4:

x_n=(1/4)Σ from k=0 to 3 of X_k exp(+2πikn/4).

Instead of memorizing these compact forms, use the table. Each row gives four multipliers; multiply them by the four input entries and add. Inverse rows act on X, not on x, and divide their sum by four.

| row index | forward multipliers | inverse multipliers |
|---:|---|---|
| 0 | 1,1,1,1 | 1,1,1,1 |
| 1 | 1,−i,−1,i | 1,i,−1,−i |
| 2 | 1,−1,1,−1 | 1,−1,1,−1 |
| 3 | 1,i,−1,−i | 1,−i,−1,i |

Why the inverse works: a full four-term sum of any nonconstant root pattern is zero, while summing four ones gives 4. When the forward expression is inserted into the inverse, the desired sample gets weight 4/4=1 and each other sample gets weight 0. Nothing is discarded.

For Δt=1/4 s, the four bins represent 0,1,2 and −1 Hz. Generally use k/(4Δt), with bin 3 also represented as −1/(4Δt). They give the same sampled complex values. Bin 0 is DC; bin 2 is the Nyquist bin, alternating sign each sample. For real samples bins 1 and 3 are conjugates. Four samples cannot distinguish frequencies separated by the sample rate 1/Δt: this is aliasing, not evidence that the continuous signals are identical.

## C26.04-W1 — Worked example (legacy C26-DFT-EX1)

Take x=(1,0,−1,0) counts at Δt=1/4 s. Forward rows yield:
X₀=1+0−1+0=0;
X₁=1+0+1+0=2;
X₂=1−0−1−0=0;
X₃=1+0+1+0=2.
Thus X=(0,2,0,2) counts under this unnormalized convention.

All inverse rows give
x₀=(0+2+0+2)/4=1,
x₁=(0+2i−0−2i)/4=0,
x₂=(0−2+0−2)/4=−1,
x₃=(0−2i−0+2i)/4=0.

Delay by one sample, wrapping the last entry to the start: y_n=x_(n−1 mod 4), where “mod 4” means wrap indices into 0,1,2,3. Then y=(0,1,0,−1). Forward rows give Y=(0,−2i,0,2i). Its inverse is
y₀=(−2i+2i)/4=0;
y₁=(i(−2i)−i(2i))/4=(2+2)/4=1;
y₂=(2i−2i)/4=0;
y₃=((−i)(−2i)+i(2i))/4=(−2−2)/4=−1.
The magnitudes of X and Y match, but the samples differ.

## C26.04-P1 — Practice (legacy C26-DFT-P1)

Transform and reconstruct (1,1,1,1), then (1,2,3,4), in counts with Δt=1/4 s. **Worked answers:** Constant input gives (4,0,0,0), whose inverse is 4/4=1 at every entry. For the second input, row sums are 10, 1−2i−3+4i=−2+2i, 1−2+3−4=−2, and −2−2i. Inverse row numerators are 4,8,12,16, hence samples 1,2,3,4. For example row 1 is 10+i(−2+2i)+2−i(−2−2i)=8.

A one-sample delay (4,1,2,3) has coefficients (10,2+2i,2,2−2i). Each old coefficient is multiplied by exp(−2πik/4), namely 1,−i,−1,i. Check the inverse numerators 16,4,8,12.

## C26.04-D1 — Diagnostic checks (legacy C26-DFT-D1)

1. What happens if the inverse omits 1/4? **Answer:** Every reconstructed sample is four times too large.
2. Can magnitudes distinguish x and y in W1? **Answer:** No: both give (0,2,0,2) as magnitudes. Retain complex phases.
3. Can bin 0 be discarded as uninteresting? **Answer:** It stores the baseline; removing it without keeping it elsewhere breaks reconstruction.
4. Does a four-point bin identify a unique continuous frequency? **Answer:** No. Frequencies differing by 1/Δt alias. Keep sampling metadata and any independent frequency constraints.

> **Claim scope:** The exact finite transform is a reversible mathematical representation of the declared samples. It does not resolve the source's high native harmonics or establish an optical detection mechanism.

**Next dependency:** [Lesson 5](lesson-05.md) compares channels and identifies what an even comparator cannot see.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Cross-channel phase and wavelength

**Essential question:** How can a comparison preserve phase while revealing its own blind spots?

**Goals:** Form a defined complex reference ratio; reconstruct four-angle counts; keep undefined ratios and intermediates; demonstrate the even comparator's odd-mode nullspace.

**Prerequisite bridge.** Lesson 4 supplies complex coefficients. We now compare two coefficients at the same frequency and with the same time convention. A ratio needs a nonzero denominator. For division by a+bi, multiply numerator and denominator by a−bi; the denominator becomes a²+b². This allows a ratio without losing the imaginary coordinate.

## C26.05-E1 — References and four-angle coordinates

Let R be a reference-channel coefficient and Z a comparison-channel coefficient at the same bin. Z/R is defined only if R≠0. Its magnitude gives an amplitude ratio; its angle gives the comparison phase relative to R. For R=2 counts and Z=−2i counts, Z/R=−i: equal amplitudes with a −π/2 phase offset. Reversing comparison polarity changes Z to 2i and ratio to i. Record channel wavelength, polarity, gain scale, time origin, sample spacing and DFT convention. An optical wavelength label does not by itself fix the phase of the recorded modulation.

For four values in angle order α,α+90°,α+180°,α+270°, write C₀,C₉₀,C₁₈₀,C₂₇₀. T35 defines a quadrature baseline Q and count contrast; we add two half-differences so the transform stays reversible:

M=(C₀+C₁₈₀)/2; Q=(C₉₀+C₂₇₀)/2;
D₀=(C₀−C₁₈₀)/2; D₉₀=(C₉₀−C₂₇₀)/2.

Reconstruct with (M+D₀,Q+D₉₀,M−D₀,Q−D₉₀). A pair mean alone would discard its half-difference.

Define contrast_counts=M−Q, and fractional_gain g=(M−Q)/Q for Q≠0. T35 calls contrast_counts G; the spectral JSON's formula labels fractional gain G. We use typed names to avoid that collision. Neither is G_phase, a matrix used later. Q here is a count baseline, not a geometric distance Q from other courses.

The source kinematic ratio is ρ=|v·n|/(c sin θ), with n a unit normal, v a velocity, c a speed in the same units, and θ the source's angle from the plane. Absolute bars give the nonnegative numerator but the signed v·n is retained separately. Then P=g/ρ. Domains: c≠0 and sin θ≠0 for ρ; Q≠0 for g; ρ≠0 and defined g for P. Undefined is not zero.

## C26.05-W1 — Worked synthetic reconstruction

Counts (8,4,6,2) give M=7,Q=3,D₀=1,D₉₀=1 counts. Contrast=4 counts and g=4/3. Use synthetic |v·n|=3 speed units, c=10 in the same units and sin θ=3/5. These toy speed units are not physical light-speed values. Then ρ=3/(10·3/5)=1/2 and P=(4/3)/(1/2)=8/3, both dimensionless. Reconstruct (7+1,3+1,7−1,3−1)=(8,4,6,2).

## C26.05-P1 — Practice and worked answer

Use counts (2,5,4,3) and the same synthetic ρ. **Answer:** M=3,Q=4,D₀=−1,D₉₀=1, contrast=−1 count, g=−1/4, P=−1/2. Reconstruction is (3−1,4+1,3+1,4−1). Also compute the ratio for R=2,Z=−2i, then reversed Z, then R=0. Answers are −i, i, and undefined; in the last case keep both original coefficients.

Practice retaining failures: A uses counts (2,0,4,0) and the W1 motion; Q=0, M=3,D₀=−1,D₉₀=0, contrast=3, ρ=1/2, while g and P are undefined. B uses W1 counts but v·n=0, c=10,sin θ=3/5; g=4/3 and ρ=0, but P is undefined. C uses W1 counts and |v·n|=3,c=10,sin θ=0; g=4/3 while ρ and P are undefined. In B and C retain M=7,Q=3,D₀=D₉₀=1 and every count.

## C26.S01-E1 — What an even comparator misses

For four periodic entries define the half-turn Hx by (Hx)_n=x_(n+2 mod 4). Doing it twice returns x. Define E x=(x+Hx)/2 and O x=(x−Hx)/2. E keeps the part unchanged by a half-turn; O keeps the part reversed by it. Adding the definitions proves E x+O x=x. Applying E to O gives zero: the odd part and its half-turned negative cancel. “Nullspace” means the set of inputs a comparison sends to zero, not absent information in the input.

For a continuous angle φ, the kth complex harmonic is exp(ikφ). A half-turn multiplies it by exp(ikπ)=(−1)^k. E therefore multiplies it by (1+(−1)^k)/2: one for even k, zero for odd k. An even comparator cannot interrogate the odd modes. This is detector-comparator parity, not A1 carry parity, chirality or projective sign.

## C26.S01-W1 — Worked comparator

For x=(1,2,3,4), Hx=(3,4,1,2), E x=(2,3,2,3) and O x=(−1,−1,1,1). Their dot product is −2−3+2+3=0. Every circular shift of an even comparator still has form (a,b,a,b), whose dot product with (u,v,−u,−v) is au+bv−au−bv=0. Thus every shift comparison is blind to O x. Save both parts. Their DFTs are (10,0,−2,0) and (0,−2+2i,0,−2−2i), respectively.

## C26.S01-P1 — Practice and source classification

For x=(3,1,−1,1), Hx=(−1,1,3,1), hence E x=(1,1,1,1), O x=(2,0,−2,0); their sum is x. Their spectra (4,0,0,0) and (0,4,0,4) occupy even and odd bins.

S05 /records/16 (R017) states the even synthetic comparator's structural zeros. /records/20 (R021) applies that blind spot to native odd indices 1,3,9,27. /records/25 (R026) proposes a cutoff/dimension synthesis; /records/26 (R027) compares ternary 27 with proposed cutoff 25, difference 2. /records/27 (R028) retains the difference pathway, not a closed identity. The ternary ladder 1,3,9,27 and Fibonacci-derived cutoff ladder 1,3,5,9,15,25,41 share some indices but are not the same construction. Our toy proves the comparator property, not those empirical or mechanism claims.

## C26.05-D1 and C26.S01-D1 — Diagnostic checks and answers

1. Why save D₀ and D₉₀? **Answer:** Means alone cannot recover all four counts; adding and subtracting half-differences can.
2. Which failure prevents g, and which prevents P only? **Answer:** Q=0 prevents g; ρ=0 with defined g prevents P. sin θ=0 prevents ρ first. Keep each input row.
3. Does E x=0 imply x=0? **Answer:** No. An odd x can be nonzero and invisible to E.
4. Can four samples resolve native indices 25 and 27? **Answer:** No. Bins alias modulo 4; 25 maps to 1 and 27 to 3, also shared by many other indices.
5. What evidence does S05 /records/15 provide? **Answer:** An archive-stated report of odd rotational AC fractions about 0.504–0.536 across nine channels. It is not a fresh measurement replay by this toy; retain its source class.

> **Claim scope:** All count exercises above are synthetic. Source branch statements retain their archive_stated or synthesis classes. Exact source pointers and hashes are in [sources](sources.md). Unexplained odd information remains a primary comparison channel.

**Next dependency:** [Lesson 6](lesson-06.md) calculates an input-equivalent model energy without confusing it with transfer.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Photon-equivalent model energy

**Essential question:** What does an energy equivalent calculate, and what inputs would identify physical transfer?

**Goals:** Calculate an input-equivalent energy interval with units; calculate a photon equivalent; explain transfer ambiguity and retain signed extensions.

**Prerequisite bridge.** Lesson 5 gives dimensionless g. Multiplying a dimensionless ratio by a quantity leaves that quantity's units unchanged. Power measures energy per unit time; one watt is one joule per second. Energy equals constant power times elapsed time. An interval [a,b] lists a lower and upper bound, not necessarily a probability statement.

## C26.06-E1 — Follow the types through the calculation

T35 and the energy-work estimators define input-equivalent power as g times the supplied LED band power. If band power is W_band and exposure duration is τ, the model energy is E_eq=g W_band τ. The word band matters: it is the modeled power allocated to a wavelength range, not necessarily total lamp power. For positive g and τ, multiply both power endpoints by gτ to obtain the energy interval. The result inherits the calibration and estimator assumptions of its inputs.

Reference photon energy is E_photon=hc/λ, with Planck constant h in energy·time, speed c in length/time and wavelength λ in length. Units cancel to energy. Then N_eq=E_eq/E_photon is a dimensionless photon equivalent. It can be fractional because it is a ratio, not an observed integer photon count. For real-unit reference calculations the pinned source supplies h=6.62607015×10⁻³⁴ J·s and c=299792458 m/s; 1 nm=10⁻⁹ m. Our main exercise uses explicitly toy constants to keep multiplication hand-checkable.

## C26.06-W1 — Worked synthetic calculation

Take g=4/3, power=3 energy-units/time-unit and τ=2 time-units. Then E_eq=(4/3)·3·2=8 energy-units. With toy h=6 energy-units·time-unit, c=10 length-units/time-unit and λ=3 length-units, E_photon=6·10/3=20 energy-units. The equivalent count is 8/20=2/5.

If power lies in [3,6] with the same units, E_eq lies in [(4/3)·3·2,(4/3)·6·2]=[8,16] energy-units. N_eq lies in [2/5,4/5]. These endpoints express the stated input interval only. They do not automatically include unknown detector calibration or exposure-transfer effects.

## C26.06-P1 — Practice and worked answer

Keep the same toy power interval, duration and photon energy, but use g=−1/4. **Answer:** Multiplying endpoints gives −3/2 and −3 energy-units. A negative multiplier reverses order, so write [−3,−3/2]. The signed equivalent count interval is [−3/20,−3/40]. This is a signed arithmetic extension, not a claim of a negative number of detected photons. Preserve the negative contrast and its reference.

The source's five positive energy rows are a selected subset of its eight positive-gain rows. We do not fill the other source energy fields with this extension; a null source field remains null, not zero.

## Why an equivalent does not identify transfer

A detector output might be represented by a product of an input factor and a responsivity factor. The pairs (2,3) and (1,6) both give scalar output 6. Observing that output cannot distinguish the factors. This small example illustrates the optical-transfer ambiguity described in T50's optical-transfer obstruction; it is not a reproduction of a compiler proof.

To connect an input equivalent to transferred apparatus energy, the source calls for radiometric calibration (counts mapped to a physical radiation quantity), a blank/reference ledger, uncertainty information, and an exposure transfer function. A transfer function states how time-varying input becomes the recorded output. Down-conversion means a process that makes high-frequency structure affect a lower-frequency channel. A long exposure alone is not a specification of that process. T35 retains an explicit down-conversion obligation for its modeled optical-scale carriers.

The source also keeps raw acquisition, LED datasheet, angular interpolation/mechanical uncertainty and independent replay obligations. These are concrete missing links in that source contract, rather than reasons to erase the reported signed responses.

## C26.06-D1 — Diagnostic checks and answers

1. Why does g W_band τ have energy units? **Answer:** g has no units; energy/time multiplied by time gives energy.
2. For the toy W1, what happens if λ doubles? **Answer:** Photon energy halves to 10, so the energy equivalent stays 8 but photon equivalent doubles to 4/5.
3. Can output 6 choose between (2,3) and (1,6)? **Answer:** No. Both products are 6; an independent calibration or other constraining measurement is needed.
4. Does a null energy field mean zero energy? **Answer:** No. It means no value supplied in that field. Keep the row and its other defined quantities.

> **Claim scope:** Input-equivalent energy and photon equivalent are model calculations. Transferred energy and detected photon counts are different measurement claims. The toy constants are not physical constants; the signed extension is not a modification of the source ledger.

**Next dependency:** [Lesson 7](lesson-07.md) reads the signed archive ledger and its repeated plane costs.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Signed event evidence

**Essential question:** How do we keep fourteen responses while recognizing that they use only three cost inputs?

**Goals:** Read a signed event with provenance; distinguish count contrast, fractional response and plane cost; count independent cost levels without deleting response rows.

**Prerequisite bridge.** Lessons 5–6 supplied four-angle reconstruction, g, ρ, P and model energy. We now read reported source records. A JSON pointer such as /events/3 selects the fourth array entry because indices start at zero. A SHA-256 digest identifies file bytes; matching it establishes byte identity, not the truth of a physical claim.

## C26.07-E1 — Read the source card first

The 2026-08-26 bundle contains two works, each represented as JSON, PDF and abstract. These six files are not six independent studies. The computational representations are the two JSON works. T35 assigns the observations the class **reported_exploratory_to_be_verified**. Read [sources](sources.md) for whole-object digests and exact paths. The source entries below retain their original order; adjacent paired rows share an event context.

A matrix is a rectangular table of numbers. Multiplying a matrix by a vector takes a dot product for each row. A superscript T means turn a column into a row. Thus qF=nᵀ G_phase n means first calculate G_phase n, then dot it with n. The source's symmetric phase metric has rows (2.9764106378,1.2431507795,−2.0803600354), (1.2431507795,2.5922286635,−2.3178839937), (−2.0803600354,−2.3178839937,6.7735709133). Its qF values are source phase-cost scalars, not joules or detector counts. Here we read the reported family values rather than claim an independently certified locked-geometry replay.

For intuition only, take synthetic matrix diag(2,3,4), meaning rows (2,0,0),(0,3,0),(0,0,4), and n=(1,0,0). Matrix multiplication gives (2,0,0); dotting with n gives qF=2. Reversing n gives the same cost because both factors change sign. A signed channel contrast need not stay unchanged. Therefore a projective cost and signed gain have different roles even when their numbers happen to match.

The source assigns w cost 1.777875828850227, v cost 5.949871981229392 and lambda cost 5.7964545517567245. There are four w rows, four v rows and six lambda rows. Fourteen response rows therefore use three independent plane-cost levels, not fourteen. “Independent levels” here counts distinct inputs; it does not assert statistical independence among families. Keep every response and any shared calibration/covariance information. Covariance records how coordinates vary together; shared inputs do not become new measurements merely by appearing in more rows.

## All-row reference ledger

Each index below references spectral-work /events/index and energy-work /all_event_channel_modulations/index. Full timestamps, signed velocities, gains, uncertainties and context stay in those immutable objects. The compact verification file retains row-by-row reconstruction and response closure. No raw acquisition is copied.

| Index | Event ID (pair:channel nm:family) | gain sign | source energy |
|---:|---|:---:|---|
| 0 | 415-515:415:w | + | null |
| 1 | 415-515:515:w | + | supplied |
| 2 | 445-555:445:v | + | supplied |
| 3 | 445-555:555:v | − | null |
| 4 | 480-630:480:lambda | − | null |
| 5 | 480-630:630:lambda | + | supplied |
| 6 | 515-680:515:lambda | − | null |
| 7 | 515-680:680:lambda | − | null |
| 8 | 630-910:630:w | + | supplied |
| 9 | 630-910:910:w | + | null |
| 10 | 415-590:415:lambda | − | null |
| 11 | 415-590:590:lambda | + | null |
| 12 | 515-590:515:v | − | null |
| 13 | 515-590:590:v | + | supplied |

The energy source names the lambda family “lambda-sheet”; the join above explicitly maps lambda-sheet to lambda. The table contains eight positive and six negative gains. Exactly five rows have energy intervals. Three positive rows have null energy fields, so “positive” and “energy selected” are not synonyms.

## C26.07-W1 — A negative row remains evidence

Read /events/3, 445-555:555:v. It shares the pair and timestamp 2026-08-25T16:51:46.693615Z with positive /events/2 at 445 nm. Row 3 has g=−0.0003402658026657847 and ρ=0.0006982587209209132. Dividing gives P approximately −0.4873061982197916. Since ρ is positive, the negative sign comes from g and remains in P. Its plane cost is the same v-family cost as its positive partner; its energy field is null. Shared cost does not imply equal or same-sign responses.

## C26.07-P1 — Worked source-card practice

For /events/0, 415-515:415:w, g=0.0005055808785109474 and ρ=0.0000574509228616101. Calculate P and interpret its energy field. **Answer:** P=g/ρ≈8.800222056115778; energy is null, not zero.

The linked energy-work /all_event_channel_modulations/0 reports four counts in angle order:
(1485.2562384582884,1483.8843576874326,1483.1281192291442,1483).
Their means are M≈1484.1921788437162 and Q≈1483.4421788437162, giving contrast 0.75 count. The half-differences are D₀≈1.064059614572102 and D₉₀≈0.4421788437163059. Adding and subtracting these reconstructs the input counts to binary64 rounding. The signed reconstruction residuals input-minus-reconstruction are (0,2.2737367544323206e−13,2.2737367544323206e−13,0) counts in this replay; they are saved, not silently rounded away. Binary64 is finite computer arithmetic and this check is not an exact interval certificate.

## C26.07-D1 — Diagnostic checks and answers

1. Count cost levels and rows. **Answer:** Three levels; fourteen response rows. Keep the within-family differences.
2. Is a negative gain an invalid observation? **Answer:** Not from its sign. It is a signed contrast relative to the quadrature baseline and stays alongside its partner.
3. How many independent studies do the six representations supply? **Answer:** Two works, not six studies. Their representations are linked evidence.
4. Does a sub-degree interpolated match establish sub-degree acquisition precision? **Answer:** No. The source acquisition grid is 4 degrees; interpolation and mechanical uncertainty remain separately required.
5. What provenance conditions remain? **Answer:** The bundle reports a declared energy revision f98c… versus packaged 9120… and a quadratic PDF digest/size mismatch. Preserve both references and conditions; do not silently merge revisions.

> **Evidence layers:** Counts and signed rows are source-reported observations; g and P are derived coordinates; qF is a model cost. A proposed beat pathway is a mechanism hypothesis. The source reports 65,880 processed rows, including 65,845 healthy and 35 diagnostic rows; the latter remain with masks and reasons in any production replay. We have replayed the compact reported-event arithmetic, not recovered raw acquisition, calibrated transfer or freshly compiled source proofs. The physical CMB authority 369812.50200040644 m/s is distinct from the experiment-local velocity.

**Next dependency:** [Lesson 8](lesson-08.md) carries the complete residual into the next comparison.
<!-- END: lesson-07 -->

<!-- BEGIN: lesson-08 -->
# Residual spectra as the next measurement

**Essential question:** How can an incomplete model be useful without erasing what it fails to represent?

**Goals:** Reconstruct a signal from a represented component and residual; transform both with the same convention; design a next comparison that retains domain failures and odd information.

**Prerequisite bridge.** Lesson 5 split a sequence into even and odd components; Lesson 4 reconstructed a DFT. A model need not describe everything. Define residual r=x−m for any declared represented component m. This is a coordinate equality, x=m+r, not a judgment that r is disposable.

## C26.08-E1 — Keep a complete decomposition

Subtract entry by entry at matching times and channels. Keep m, r, their units, their sample order, and the exact rule that constructed m. The DFT is linear: each output is a sum of fixed multipliers times samples. Distributing those multipliers over m+r proves DFT(x)=DFT(m)+DFT(r). Apply the same inverse to both spectra and add to recover x.

An average magnitude or scalar score can summarize a residual but cannot replace it. For example (1,−1) and (−1,1) have equal squared totals yet different timing. A useful next comparison can inspect residual phase, wavelength, orientation, parity or event neighborhood. It must use common coordinates and keep the component removed at each stage. In a second stage write r=m₁+r₁; then x=m+m₁+r₁. Save all three.

An undefined ratio has a different status from a numerical residual. Keep its original row and reason, plus every defined intermediate. Never fill it with zero to make a plot convenient. If a display hides such a point, the report must still contain its row and status.

## C26.08-W1 — Worked exact reconstruction

Use x=(1,2,3,4) counts with Δt=1/4 s and the DFT convention of Lesson 4. Choose m=E x=(2,3,2,3). The residual r=O x=(−1,−1,1,1). Calculate spectra directly:

DFT(m)=(2+3+2+3, 2−3i−2+3i, 2−3+2−3, 2+3i−2−3i)=(10,0,−2,0).

DFT(r)=(−1−1+1+1, −1+i−1+i, −1+1+1−1, −1−i−1−i)=(0,−2+2i,0,−2−2i).

Adding gives (10,−2+2i,−2,−2−2i), the full spectrum. Inverse m has numerators (8,12,8,12); inverse r has (−4,−4,4,4). Dividing by 4 gives the two retained components, whose entrywise sum is (1,2,3,4).

An even-only comparison has no access to the odd residual. That blindness explains a missing comparison response without implying that the measured odd information is zero.

## C26.08-P1 — Practice and worked answer

For x=(3,1,−1,1), form m=E x and r=O x. **Answer:** Hx=(−1,1,3,1), hence m=(1,1,1,1) and r=(2,0,−2,0). Their spectra are (4,0,0,0) and (0,4,0,4). The inverse of the first is all ones; the second gives (8,0,−8,0)/4=(2,0,−2,0). Add to reconstruct x exactly.

For a next comparison, retain the residual coefficients at bins 1 and 3 and compare them with a second channel sampled at the same Δt and origin. If that reference coefficient is zero, record an undefined ratio and both coefficients instead of replacing the ratio by zero. Keep m alongside that comparison.

Append the three failure rows from Lesson 5: A counts (2,0,4,0), Q=0 with defined M=3,D₀=−1,D₉₀=0, contrast=3,ρ=1/2; B counts (8,4,6,2), g=4/3 but ρ=0; C the same counts and g but sin θ=0, so ρ is undefined. In B and C M=7,Q=3,D₀=D₉₀=1. None permits a defined P. Their different reasons remain distinguishable.

## Plan a replayable comparison

Your output packet should contain: the input reference or full small synthetic sequence; timestamps and units; reference-channel definition; model rule and component; full signed residual and its spectrum; inverse convention; reconstruction residual; defined/undefined statuses; and the evidence class. For archive work, retain the immutable references and all source diagnostic masks, rather than making another raw data copy. For a tiny classroom example, save the complete synthetic coordinates.

Compare candidate mechanisms by what retained structures they can jointly explain and what new predictions they make. A proposal that only fits the even component leaves an explicit task: explain or predict the odd component. No scalar fit summary closes that task. The 25/27-to-2 source pathway remains a proposed branch; our four-sample transform aliases high indices and cannot independently test that native pathway.

## C26.08-D1 — Diagnostic checks and answers

1. Why does DFT(m+r)=DFT(m)+DFT(r)? **Answer:** Each row is a fixed weighted sum, and multiplication distributes over addition.
2. A residual score is zero after rounding. Can r be erased? **Answer:** No. Save its actual signed coordinates and precision; a rounded summary is not the residual.
3. How do you reconstruct after modeling r again? **Answer:** If r=m₁+r₁, sum m+m₁+r₁ with the same coordinates.
4. Does the even comparator's nullspace explain away odd observations? **Answer:** It identifies a comparator limitation. Keep the odd observations and test them with a comparison that has odd support.

> **Claim scope:** Exact closure in these finite synthetic examples demonstrates bookkeeping and algebra. Source binary64 closure, physical calibration, and mechanism identification are different checks. Residual information remains a primary measurement coordinate at each step.

**Next dependency:** [Capstone](capstone.md) combines all nine operations in a complete retained-information packet.
<!-- END: lesson-08 -->

