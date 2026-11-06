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
