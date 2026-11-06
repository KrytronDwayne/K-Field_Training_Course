# Lesson 04 — Roots, weights, and quotient labels

**Essential question:** How can three channel weights belong to one quotient class?

**Goals:** Center channel vectors; derive the three-class test; preserve the full weight while making a quotient view.

**Bridge and pacing:** Lesson 03 built the integer zero-sum lattice Q₂. We now enlarge the allowed points while keeping the same plane. Two 55-minute periods, each with 5 retrieval, 20 explanation/example, 15 practice, 15 diagnostics. Period A teaches centering; period B teaches quotient membership and addition.

## C13.04-E1 — Centering and a larger lattice

The three channel vectors each have sum 1. Subtract the common mean vector h=(1/3,1/3,1/3) to put each in H. Define u_i=e_i-h. Then u₁=(2,-1,-1)/3, u₂=(-1,2,-1)/3, u₃=(-1,-1,2)/3. A fraction outside parentheses divides every entry. Their sum is zero, so u₃=-u₁-u₂. Differences are unchanged by subtracting the same h: u₁-u₂=e₁-e₂=α₁. To recover a channel vector, retain h and add it back. For a general triple v, retain its mean μ=(v₁+v₂+v₃)/3 along with v-μ(1,1,1).

Define the weight lattice P₂ to be all a u₁+b u₂ with integers a,b. In this course “weight” refers to these abstract vectors, not physical mass. Expanding gives

a u₁+b u₂=((2a-b)/3,(-a+2b)/3,-(a+b)/3).

This vector is integral exactly when a+b is divisible by 3. Necessity follows from its last component. For sufficiency, write a+b=3k. Then the first component is a-k, the second b-k, and the third -k, all integers. The sum is already zero. Conversely, any integer zero-sum (x,y,z) is in P₂: choose a=x-z,b=y-z. The displayed formula returns (x,y,z). Therefore Q₂ is exactly the integral part of P₂.

Two weights share a quotient class if their difference lies in Q₂. Their labels are the remainder of a+b after division by 3, chosen from {0,1,2}. Equal remainders make their coefficient-sum difference divisible by 3, precisely the condition just proved. This produces P₂/Q₂ with three classes, called Z₃. Adding weights adds coefficient sums, so class addition is remainder addition modulo 3. For example, 2+2 has remainder 1. Negative sums follow the same rule: -1=2+3(-1).

Keep the coefficients (a,b), not just the class. They reconstruct the vector exactly. Alternatively retain a chosen representative r u₁ and the full root-lattice displacement q=w-r u₁. Here r is the class label. Recording only r loses q; the quotient is a useful view, not a replacement for the original.

## C13.04-W1 — Representatives and channel differences

u₁ and 2u₁ are not integral: their first components are 2/3 and 4/3. But 3u₁=(2,-1,-1) is integral and zero-sum, hence in Q₂. Representatives 0,u₁,2u₁ have labels 0,1,2. Also u₁-u₂=(1,-1,0)=α₁. Thus u₁ and u₂ have the same label despite being different vectors. For u₃=-u₁-u₂ the coefficient sum is -2≡1 mod 3. All three channel weights lie in class 1. Their sum is zero, consistent with 1+1+1≡0.

> **Source scope:** S02 /backbone_sequence/8 and KFM-X021 give the centered weights and quotient. The divisibility proof here supplies an elementary reconstruction. “Three channel weights” and “three quotient classes” count different objects.

## C13.04-P1 — Compute before classifying

Find u₁+u₂ and 2u₁+u₂, their class labels, and u₂-u₁. For each result keep coefficients and identify whether it belongs to Q₂. Give a representative-plus-displacement record for u₁+u₂.

**Worked practice answer:** u₁+u₂=(1,1,-2)/3 has coefficients (1,1), sum 2, label 2, and is not integral. Relative to representative 2u₁, its displacement is u₂-u₁=(-1,1,0)=-α₁. Thus w=2u₁-α₁ reconstructs it. Next, 2u₁+u₂=(1,0,-1)=α₁+α₂ has coefficients (2,1), sum 3, label 0, and lies in Q₂. Finally u₂-u₁ has coefficients (-1,1), sum 0, label 0, and is a root. Adding it to u₁ changes the vector to u₂ without changing label 1.

## Diagnostic checks

1. **C13.04-D1:** Are u₁,u₂,u₃ representatives of three different quotient classes? What does a root step preserve and what does it change?
2. **C13.04-D2:** Find the coordinates and label of -u₁. Is it in Q₂?
3. **C13.04-D3:** For a=4,b=-1, find the vector and class. Reconstruct it from α₁,α₂.
4. **C13.04-D4:** If only class 2 is retained, can you distinguish 2u₁ from u₁+u₂? What extra record suffices?

**Worked answers:** 1. No, all have label 1. A root step changes the weight vector but preserves its class. 2. (-2,1,1)/3, class -1≡2; it is not integral. 3. (3,-2,-1), label 0 because 4-1=3; it equals 3α₁+α₂. 4. No. Keep (a,b), or representative 2u₁ together with displacement 0 or -α₁, respectively.

**Next dependency:** [Lesson 05](lesson-05.md) distinguishes these weights from other objects that also happen to carry three entries.
