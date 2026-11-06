# Lesson 02 · Eigenvectors as unchanged pattern directions

**Essential question:** When does an operator change a pattern only by one common multiplier?

**Goals:** Verify an eigenpair component by component; explain zero and negative eigenvalues; verify that nonzero scaling preserves an eigenvalue.

**Prerequisite bridge.** Lesson 01 taught row multiplication and neighbor sums. We now compare an output with a scaled copy of its input. Multiplying a vector by a number means multiplying every entry by that same number.

## C12.02-E1 · The common-multiplier test

A nonzero pattern v is an **eigenvector** of an operator A when Av=λv for one number λ, called its **eigenvalue**. The pair (λ,v) is an eigenpair. Equality means equality at every node: the first output equals λ times the first input, the second equals λ times the second, and so on. Do not divide by entries that are zero; compare products directly.

“Unchanged direction” includes three cases. A positive λ scales the pattern without reversing it. A negative λ reverses every sign while scaling. A zero λ sends that entire pattern to zero. The input must still be nonzero. The all-zero vector is excluded because A0=λ0 for every λ; it cannot select a particular multiplier.

Before using the three-node path, try the two-node path. Its adjacency S=[[0,1],[1,0]] simply swaps two entries: S(a,b)=(b,a). We use S to avoid confusing its two-address domain with A's three-address domain.

## C12.02-W1 · Two patterns that keep their direction

S(1,1)=(1,1)=1·(1,1), so (1,(1,1)) is an eigenpair. S(1,−1)=(−1,1)=−1·(1,−1), so (−1,(1,−1)) is another. Both entries have been checked in each case.

Multiply the first input by 3: S(3,3)=(3,3). Multiply the second by 3: S(3,−3)=(−3,3)=−1·(3,−3). The eigenvalues remain 1 and −1, respectively. Why? Each row is a sum of fixed multiples, so A(tv)=t(Av)=tλv=λ(tv). Here t is any nonzero number. Choosing t=0 would produce the excluded zero vector. This distributive rule is called linearity; it also gives A(v+w)=Av+Aw.

We will soon need √2. For a positive number q, √q means the positive number whose square is q. Thus (√2)²=2 exactly; √2 is approximately 1.414, but we keep the exact symbol. The equation x²=2 has two answers, √2 and −√2, even though the symbol √2 itself names the positive one.

## C12.02-P1 · Guided practice and worked answers

Verify S(2,2), S(2,−2), and the path action A(2,0,−2). The swap gives (2,2) and (−2,2), hence eigenvalues 1 and −1. The path rule gives (0,2−2,0)=(0,0,0)=0·(2,0,−2). This third input is a valid nonzero zero-eigenvalue vector. A zero output does not mean there was no input information: the input's amplitude cannot be recovered from this output alone.

Try the path candidate (1,1,1). Its output is (1,2,1); the first component requires λ=1, while the middle requires λ=2. Thus no common λ works. Also check (√2)(√2)=2 and (−√2)²=2; both follow from the square-root definition and signed multiplication.

> **Claim scope.** “Mode” will mean a chosen eigenvector pattern, not a physical oscillation by default. The calculations establish finite operator facts. A mechanism or measured frequency needs additional definitions and evidence. See S02 /backbone_sequence/7/proof/2–4 for the later source spectrum.

## C12.02-D1 · Diagnostic checks

1. Test S(3,−3) and name its eigenvalue.
2. Why is (0,0) not an eigenvector, although S(0,0)=0·(0,0)?
3. Test (1,1,1) for the three-node A. Is a zero eigenvalue forbidden?
4. If Av=λv, does multiplying v by −2 change λ? Explain using row distributivity.

**Worked answers.** 1. S(3,−3)=(−3,3)=−(3,−3), so λ=−1. 2. The eigenvector definition excludes zero; every λ would work for it. 3. It fails because (1,2,1) is not a common multiple. Zero λ is allowed for a nonzero input such as (2,0,−2). 4. A(−2v)=−2Av=λ(−2v); λ stays the same.

**Next dependency:** [Lesson 03](lesson-03.md) finds every eigenvalue of the three-node path and gives its modes unit length.
