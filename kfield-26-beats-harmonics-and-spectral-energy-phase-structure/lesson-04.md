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
