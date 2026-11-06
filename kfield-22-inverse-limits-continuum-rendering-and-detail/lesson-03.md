# Lesson 03 — The ternary inverse limit

Essential question: What makes infinitely many finite addresses one object?

Goals: Construct a compatible infinite rule; distinguish a prefix from a complete point; enumerate next-level choices in three coordinates.

Bridge and pacing: Lessons 01–02 supplied residues, reductions and prefix closeness. Two 55-minute periods: each uses retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Period 1 builds scalar rules; period 2 combines triples and studies unresolved continuation.

## C22.03-E1 — Keep the entire ladder

At depth d there are 3^d choices for one residue. For three coordinates there are (3^d)³=27^d addresses. A deeper address reduces to exactly one shallower address, but a shallow address has many extensions. This direction explains the word “inverse”: the linking maps go from finer information back to coarser information.

The inverse limit A∞ is the set of all sequences (a₁,a₂,a₃,…) whose entries belong to their respective A_d and satisfy every reduction equation. A “set” is a collection; an element here is a whole compatible history, not its last finite row. The notation Z₃³ names the same triple ternary-history structure. The subscript 3 names the ternary completion; it is not the three-element set Z/3Z. This definition introduces no calculus.

A complete digit rule constructs an example: for each positive integer j, tell us which digit u_j to use, and apply the prefix rule from Lesson 01. Adding the next term 3^d u_(d+1) cannot change the old residue. Conversely, at each level the three choices −1,0,1 give distinct extensions because their differences are not multiples of 3. This allows the history to be read back one digit at a time. The infinite rule is a compact specification, not a claim that infinitely many entries were physically stored.

## C22.03-W1 — An exact all-positive rule

Set u_j=1 for every j. The first four signed sums are 1, 1+3=4, 1+3+9=13, and 1+3+9+27=40. All lie in their storage ranges. The general expression is t_d=(3^d−1)/2. Check it without infinite sums: it gives t₁=1 and the difference t_(d+1)−t_d=(3^(d+1)−3^d)/2=3^d, exactly the next contribution. Therefore reduction is compatible at every depth, not just the four listed depths.

An explicit triple point uses rules “all +1”, “all 0”, “all −1” for its first, second and third coordinates. At depths 1–4 its nonnegative residue triples are (1,0,2), (4,0,5), (13,0,14), (40,0,41). Preserve the signed third sums −1,−4,−13,−40 alongside them. No physical units attach to these entries.

> Claim scope: S02 /backbone_sequence/17 defines A∞ and its paired real rendering. We have constructed explicit inverse-limit points and explained the notation; we have not assigned any arbitrary operator to them. The ternary depth is distinct from the dyadic refinement in S02 /backbone_sequence/2/recursions/group_dyadic. Counts 27^d here do not license a substitution of dyadic depth.

## C22.03-P1 — Practice, then check

Use all −1 digits to construct four levels and check compatibility. How many next triple addresses extend any fixed depth-d triple?

Answer: signed sums −1,−4,−13,−40 reduce to 2,5,14,41. Check 5 mod3=2, 14 mod9=5, 41 mod27=14. In one coordinate the extensions of residue a can be written a, a+3^d, a+2·3^d in the next storage range. Independently choosing one for each of three coordinates gives 3·3·3=27 extensions. Balanced digit labels may require reduction but describe the same three choices.

## Diagnostics — C22.03-D1

1. What is the fifth all-positive signed sum?
2. How many triple addresses exist at depth 2?
3. Is a four-row table with no continuation rule an exact infinite point?
4. Does verifying four reductions alone establish a proposed rule at every depth?

Worked answers: (1) 40+81=121=(243−1)/2. (2) 9³=729=27². (3) No; it specifies a family of possible extensions. Record “continuation unresolved.” (4) No; use the general difference argument when a rule is supplied. A finite failure disproves compatibility, but finitely many successes alone leave the rest untested.

Next dependency: [Lesson 04](lesson-04.md) renders the digit rule while preserving this exact address ladder.
