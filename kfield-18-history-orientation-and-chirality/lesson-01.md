# Lesson 01 — Address histories as words

**Essential question:** How can an address remember a sequence of choices?

**Goals:** Generate all words through a stated depth; distinguish an empty label from a zero coefficient; apply a prefix and its conditional removal.

**Bridge:** Courses 06, 15 and 17 are the series prerequisites. Here we need only their habits of keeping ordered labels, signed quantities and distinct carriers. This lesson rebuilds the finite notation: a list of labels tells us which slots exist; a list of numbers tells us what occupies each slot. All classroom coefficients are dimensionless synthetic values, not measurements.

**Pacing:** One 55-minute period: retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15 minutes.

## C18.01-E1 — Words and a ledger

Choose the classroom alphabet {a,b}. A word is a finite ordered string of these letters. Order matters: ab and ba are different. Its length is the number of letters. The empty word, Ω, has length zero. It is a legitimate address: the start before any choice. It is not the number zero.

Prefixing puts a letter on the **left**. Thus prefix a changes b into ab, and changes ab into aab. Our convention records the newest choice on the left. If you instead append on the right, you have defined a different operation and must say so.

A tree connects each word w to aw and bw. A depth cutoff d keeps words with length at most d. It does not tell us what to do when an operation leaves the displayed tree. We will specify that rule separately.

For each word w, let e_w mean a ledger with coefficient 1 in slot w and 0 in all other slots. These are unit coordinate vectors. A vector is a list of coefficients in a declared order; for example 2e_Ω−e_a has root coefficient 2 and a coefficient −1. Different unit coordinate vectors are called orthogonal: their dot product is zero. The dot product multiplies matching entries and adds the products. This is a bookkeeping model, with no probability interpretation assigned.

## C18.01-W1 — Build the depth-two tree

Start with Ω. Prefix either letter to obtain a,b. Prefix to both: a→aa,ba and b→ab,bb. Sorting into the fixed classroom order gives

| Length | Labels | Number |
|---|---|---:|
| 0 | Ω | 1 |
| 1 | a, b | 2 |
| 2 | aa, ab, ba, bb | 4 |

The total is 1+2+4=7. None of these labels is omitted, including Ω. Prefix a sends Ω to a and b to ab. Conditional removal of a sends ab back to b. It fails on ba because ba starts with b. In the later linear operator model a failed removal returns the **zero vector**, meaning all coefficients zero; it does not return e_Ω. Removing a from the one-letter word a does return e_Ω.

To see why those differ, e_Ω=(1,0,0,0,0,0,0), whereas the zero vector has seven zeros. A ledger (2,−1,0,3,0,−2,4) preserves the root, the signs and the zero slots.

## C18.01-P1 — Practice before checking

Draw the depth-one tree. Prefix b to Ω, a and b while allowing depth two. Then record 3e_Ω−2e_b in depth-one order. Explain what would happen to ba if a depth-one display were enforced.

**Worked answer:** The depth-one labels are Ω,a,b. Prefix b gives b,ba,bb respectively. The ledger is (3,0,−2). The last two outputs lie outside a depth-one display. A larger display keeps them; a truncating operator would send them to zero and require a separate record of the omitted coefficients for reconstruction. A drawing cutoff alone does not choose between these rules.

> **Claim scope:** This binary toy is an authored finite example. S02#/backbone_sequence/13 defines the source carrier F_hist=l²(B_8*): all finite words over the source eight-letter alphabet, including Ω. The star means all finite word lengths. The symbol l² means coefficient lists whose sum of squared magnitudes is finite. The source alphabet's complete typed replay definition is flagged in S03#/findings/8; we do not identify its letters with physical directions. Seven coordinate slots are not the source infinite carrier.

## Diagnostic checks

1. **C18.01-D1:** What extra rule must accompany a finite cutoff, and how does this tree differ from F_hist?
2. List the words of exactly length three without repeating or losing a branch.
3. Does removing a from a give zero? Does removing a from ba give Ω?
4. In (0,2,−1), has the root label been deleted?

**Worked answers:** (1) State how operations treat terminal words; our seven labels are a finite binary toy, while F_hist includes all finite words over B_8. (2) aaa,aab,aba,abb,baa,bab,bba,bbb; each of four length-two words has two children, so 8. (3) The first returns e_Ω; the second returns the zero vector under conditional removal. (4) No: the first slot remains and has coefficient zero.

**Next dependency:** [Lesson 02](lesson-02.md) converts these label operations into maps and accounts for both endpoints of a finite shift.
