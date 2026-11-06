# 4. Symmetry, palindromes, and signed comparisons

Essential question: Which structures can a comparator see, and which does it miss?

Goals:

- Compute reflection and half-turn components separately
- Prove comparator blindness with a dot product
- Calculate and invert a four-point complex spectrum
- Classify the native-ladder and beat claims

## Prerequisite bridge

Use [Normalization with an inverse account](lesson-03.md): its retained records and operations are the inputs to this lesson.

Pacing: 3 period(s) of 55 minutes. Reflection same/inverted operators / Antipodal even/odd operators / C28.S01 nullspace and source ladder.

## C28.04-E1 — first principles

A reflection compares positions equally far from a specified center. For a four-entry list x=(x0,x1,x2,x3), choose the center halfway between indices 1 and 2. Reversal R sends x to (x3,x2,x1,x0). It is an operation on positions, not a change of sign. Applying R twice returns the original list.

Define s=(x+Rx)/2 and a=(x-Rx)/2, adding and subtracting corresponding entries. The same component satisfies Rs=s; the inverted component satisfies Ra=-a. Adding the definitions cancels Rx and returns x=s+a. Same-polarity defect x-Rx equals 2a; inverted defect x+Rx equals 2s. Both defects are lists, not merely scores. An exactly same input has zero same defect; an exactly inverted input has zero inverted defect. Neither condition requires the other.

For x=(1,2,4,3), Rx=(3,4,2,1). The sum is (4,6,6,4), so s=(2,3,3,2); the difference is (-2,-2,2,2), so a=(-1,-1,1,1). Addition gives (1,2,4,3), entry by entry. Keep the nonzero defects (-2,-2,2,2) and (4,6,6,4). The words same and inverted refer only to this operator and center.

A periodic half-turn is different. For four equally spaced positions on a circle, H shifts two places: Hx=(x2,x3,x0,x1). E means the even-part operation Ex=(x+Hx)/2; O means the odd-part operation Ox=(x-Hx)/2. I is the identity operation Ix=x, so E+O=I means their outputs add back to the input. HEx=Ex and HOx=-Ox. Here parity means behavior under H, not chirality or any other source parity.

An even comparator has form c=(p,q,p,q). Every circular shift has that form with some pair of values. Any odd vector has form o=(u,v,-u,-v). Their dot product means multiply matching entries and add: c dot o=pu+qv-pu-qv=0. Thus shifting and comparing this comparator can never recover odd amplitudes. This is comparator blindness, also called a nullspace: inputs mapped to zero by the comparison. Even large odd structure is invisible to it. A weak channel deserves the same decomposition and retention as a strong one.

We also teach a small frequency encoding so that keeping phase has a concrete meaning. A complex number a+bi stores two signed coordinates, with i*i=-1. Addition is coordinatewise; multiplication distributes, replacing i*i by -1. No calculus is needed. For four samples, define the discrete Fourier transform (DFT) by four weighted sums:

F0=x0+x1+x2+x3; F1=x0-i*x1-x2+i*x3; F2=x0-x1+x2-x3; F3=x0+i*x1-x2-i*x3.

The inverse is x0=(F0+F1+F2+F3)/4; x1=(F0+i*F1-F2-i*F3)/4; x2=(F0-F1+F2-F3)/4; x3=(F0-i*F1-F2+i*F3)/4. These declared signs and the factor 1/4 are part of the contract. Frequency index j counts cycles across the four-sample period. Indices differing by 4 give identical weights (aliasing); this grid cannot distinguish native modes 25 and 27 from indices 1 and 3.

For x=(1,2,3,4), Ex=(2,3,2,3), Ox=(-1,-1,1,1). The odd transform is (0,-2+2i,0,-2-2i): for example F1=-1+i-1+i=-2+2i. Inverting gives x0=(-4)/4=-1, x1=(-4)/4=-1, x2=4/4=1, x3=4/4=1 for the odd component. Every shift of Ex has zero dot product with Ox. Retain both complex coefficients and the even component; a zero comparator result cannot replace them.

Source card S05 R017 describes odd-harmonic structural zeros of an antipodally symmetric synthetic comparator. R021 separately synthesizes a native ternary ladder 1,3,9,27 (each is three times its predecessor) and its comparator blindness. R028 retains 25–27→2 as a proposed difference pathway: 27-25=2 is arithmetic; physical coupling is an additional claim. The Fibonacci-cutoff proposal is a separate source branch, not a consequence of our four-point DFT. These archive claims are not fresh native-data replay. See sources.md for exact pointers and limitations.

> Claim scope: Finite identities are freshly checkable algebra. S05 archive statements retain their own evidence classes; native arrays and beat coupling are not newly verified here.

## C28.04-W1 — worked example

For x=(1,2,4,3), reverse Rx=(3,4,2,1), same component s=(2,3,3,2) and inverted component a=(-1,-1,1,1). R s=s, R a=-a and s+a=x. Neither full input passes an exact same or inverted test; retain both nonzero defects.

## C28.04-P1 — guided practice

**Student task.** For x=(3,1,-1,1), reverse it about the center between indices 1 and 2. Compute s, a, both defects and the reconstructed input. For (-2,0,2), reverse about its middle sample and test inversion. Explain what a nonzero center or weak channel changes.

### Worked answer

For x=(3,1,-1,1), reflection components are (2,0,0,2) and (1,1,-1,-1). For a separate midpoint-centered pair (-2,0,2), reversal negates the sequence, so inverted defect is zero. A nonzero center sample would remain a same component.

For the four-entry practice, Rx=(1,-1,1,3), same defect=(2,2,-2,-2), inverted defect=(4,0,0,4); s+a=(3,1,-1,1). For (-2,0,2), Rx=(2,0,-2), s=(0,0,0), a=(-2,0,2). A nonzero center contributes to s. Retain the same fields for a weak channel.

## C28.S01-E1 / C28.S01-W1 — comparator audit

The half-turn, dot-product proof and DFT above are the explanation and worked example for this supplement. For x=(1,2,3,4), retain Ex=(2,3,2,3), Ox=(-1,-1,1,1) and odd spectrum (0,-2+2i,0,-2-2i).

## C28.S01-P1 — guided practice

**Student task.** For x=(3,1,-1,1), compute Hx, Ex, Ox, the odd DFT and its inverse. Prove zero dot product with any even comparator (p,q,p,q). Classify the native ternary ladder, Fibonacci-cutoff proposal and difference pathway from the source card. Explain what four-point aliasing prevents.

### Worked answer

For x=(3,1,-1,1), Hx=(-1,1,3,1). Adding and halving gives Ex=(1,1,1,1); subtracting and halving gives Ox=(2,0,-2,0). Their sum is x. Dot any even comparator (p,q,p,q) with Ox: 2p-2p=0. Its odd spectrum is (0,4,0,4); the inverse gives (2,0,-2,0). S05 R017/R021 address the native odd ladder; R028 separately retains the proposed 25–27→2 pathway.

## C28.S01-D1 — diagnostic

Can the four-point example distinguish native 1 from native 25? Answer: no, their indices differ by 24, a multiple of 4. Report aliasing and retain the native claim separately.


### Source-ladder bridge and practice answer

The source R026 uses dimensions 2,4,6,10,16: halving gives 1,2,3,5,8. Each term after the first two is the sum of its previous two, a Fibonacci-type rule. Continuing gives 13 and 21; doubling gives dimensions 26 and 42. In the source convention cutoff is dimension minus 1, giving proposed 25 and 41. Thus cutoff ladder 1,3,5,9,15,25,41 differs from native ternary ladder 1,3,9,27. Their finite listed intersection is 1,3,9; 27-25=2 motivates the separately proposed difference branch. These are R026/R027 source syntheses, not newly observed continuation. For the four-point practice, inverse of (0,4,0,4) is ((4+4)/4,(4i-4i)/4,(-4-4)/4,(-4i+4i)/4)=(2,0,-2,0). The modulo-4 grid cannot resolve native mode identities.


## C28.04-D1 — diagnostic checks

1. Find both defects for (1,2,4,3).
2. Does H equal R for a four-point list?
3. Can an even comparator detect o=(2,0,-2,0)?
4. What does the four-point DFT establish about native 25 and 27?
5. What must survive if an odd-channel comparison score is zero?

## Worked answers

1. Same=(-2,-2,2,2); inverted=(4,6,6,4). Neither vanishes.
2. No: H sends (1,2,3,4) to (3,4,1,2); R gives (4,3,2,1).
3. No. (p,q,p,q) dot o=2p-2p=0 for every p,q; retain o.
4. It aliases them modulo 4, so cannot resolve them as native harmonics. The proposed 25–27→2 mechanism remains a distinct source claim.
5. The odd component, its two complex coefficients, support and inverse rule; zero may reflect comparator blindness.

Next dependency: [lesson-05](lesson-05.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
