# Lesson 02 — Side transfers and the A1 pattern

**Essential question:** Why does moving one unit between two sides change their difference by two?

**Goals:** Derive and reverse side coordinates; check integer compatibility; compute the A1 parity class while retaining full information.

**Bridge and pacing:** Lesson 01 distinguished preserving a sum from preserving all quantities. Here the carrier is ordered integer side carries (C_b,C_c). A carry is a signed integer entry retained by the source's recursive description; it need not be positive. Two 55-minute periods, each with 5 minutes retrieval, 20 instruction/example, 15 practice, 15 diagnostic repair. Period A teaches transfers and inversion; period B teaches congruence and reconstruction.

## C13.02-E1 — Sum, difference, and recoverability

Define S=C_b+C_c and A=C_b-C_c. Add these equations to obtain S+A=2C_b. Subtract the second from the first to obtain S-A=2C_c. Thus C_b=(S+A)/2 and C_c=(S-A)/2. This is a change of coordinates, not information removal.

For integer carries both halves must be integers. This happens exactly when S and A are both even or both odd. “Same parity” means this shared remainder upon division by 2. If one is even and the other odd, their sum and difference are odd and division by 2 gives half-integers.

The native transfer is (C_b,C_c) → (C_b+1,C_c-1). Its output sum is C_b+1+C_c-1=S. Its output difference is C_b+1-(C_c-1)=A+2. The reverse transfer changes A by -2. After an integer k of forward transfers (negative k means reverse), the pair is (C_b+k,C_c-k), and A becomes A+2k.

Write Z for all integers. In the difference coordinate, the allowed weight values form P₁=Z and the transfer displacements form Q₁=2Z, the even integers. Here the A1 root steps are +2 and -2. A quotient groups values together when their difference is an allowed displacement. Thus P₁/Q₁ has two classes, even and odd, often written Z₂. Congruence A≡r mod 2 means A-r is divisible by 2. A negative example is -3≡1 mod 2, because -3-1=-4=2(-2).

Retain A=r+2k with r chosen from {0,1}, plus S. For A=-3, r=1 and k=-2. The class r alone cannot recover A. Also, at a fixed S, only the class compatible with that S occurs; the two-class statement concerns P₁ across both parities of S. This prevents counting two parity options on a single fixed-sum line when only one is allowed.

## C13.02-W1 — Transfer an odd difference

Start with (C_b,C_c)=(2,1). Then S=3 and A=1. Forward transfer gives (3,0), so S'=3 and A'=3. The sum stayed fixed; the difference rose by 2. Both differences have remainder 1. Initially A=1+2(0); finally A'=1+2(1). Decoding the final coordinates gives ((3+3)/2,(3-3)/2)=(3,0). Reverse by (-1,+1) to recover (2,1). Its squared norm changes from 5 to 9: the transfer is a symmetry of S, not of that squared norm.

> **Source scope:** S02 /backbone_sequence/5/side_modes and /backbone_sequence/8, plus /proof_nodes/54/formula (KFM-X020), ground these definitions. The finite derivation is checked here. A1 carry parity is not detector antipodal parity. No rounding or half-open cell rule is used in this lesson.

## C13.02-P1 — Transfer and reconstruct a negative example

Starting from (-1,3), calculate S,A, apply one forward transfer, and retain the parity class together with enough information to undo it. Then test the incompatible candidate S=1,A=0.

**Worked practice answer:** Initially S=2, A=-4=0+2(-2). The output is (0,2), with S'=2 and A'=-2=0+2(-1). The class is even at both stages. Store S=2, r=0, k=-2 for the input and the transfer count +1. Decode A=-4, then C_b=(2-4)/2=-1 and C_c=(2+4)/2=3. For S=1,A=0 the inverse gives (1/2,1/2), so this is not an integer carry record.

## Diagnostic checks

1. **C13.02-D1:** What does keeping only A mod 2 lose? Does carry parity determine detector parity?
2. **C13.02-D2:** Decode S=-1,A=3 and apply the reverse transfer.
3. **C13.02-D3:** Write A=-5 as r+2k using r∈{0,1}. Is it in the same class as A=7?
4. **C13.02-D4:** With S=4, can an integer carry pair have A=3? Explain using the inverse formulas.

**Worked answers:** 1. It loses the even displacement 2k; keep k and S or the original pair. Detector parity requires its own rule and carrier. 2. (C_b,C_c)=(1,-2); reverse gives (0,-1), with S=-1,A=1. 3. -5=1+2(-3). The difference 7-(-5)=12 is even, so both are odd. 4. No: (4+3)/2=7/2 and (4-3)/2=1/2 are not integers.

**Next dependency:** [Lesson 03](lesson-03.md) expands the transfer idea to three channels and a plane.
