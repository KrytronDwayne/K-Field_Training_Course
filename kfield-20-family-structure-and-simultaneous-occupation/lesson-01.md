# Lesson 1 — Residues modulo three

Essential question: How can one rule divide 27 coordinate labels into three equal classes?

Goals: Compute residues, including negative residues; enumerate a class without omissions; distinguish a class count from an occupation claim.

Prerequisite bridge: You already add signed integers and solve an equation such as x+3=5. Here we add one rule: numbers differing by a multiple of three receive the same label. The course follows courses 15 and 18 in the series, but all finite operations needed here are introduced locally.

## C20.01-E1 — A finite coordinate system

The residue of an integer modulo three is the unique member of {0,1,2} left after subtracting a suitable multiple of three. For example, 8=2×3+2 has residue 2. Also −1=(−1)×3+2 has residue 2. The symbol ≡ means “has the same residue as”: −1≡2 modulo 3. Use these representatives even when subtraction gives a negative number.

The source writes F₃ for these three labels with addition and multiplication reduced modulo three. X=F₃³ is the set of ordered triples (x₁,x₂,x₃). The exponent 3 means three coordinate positions here. Each position has three choices, so X contains 3×3×3=27 nodes. A node is a label, not an observed particle or a position in metres.

Define λ(x)=(x₁+x₂+x₃) mod 3. The Greek letter λ is pronounced “lambda.” Define Cᵣ to contain every node whose λ value is r, for r=0,1,2. In source notation Cᵣ=λ⁻¹(r): this means the set of inputs with output r, not division by λ. Each node belongs to exactly one class because each integer sum has exactly one residue.

To build Cᵣ, choose x₁ and x₂ freely, then solve x₃≡r−x₁−x₂. There is exactly one allowed x₃. Thus nine pairs give nine nodes per class. Use the following fixed pair order throughout the course; the table gives x₃, not the full triple.

| (x₁,x₂) | C₀: x₃ | C₁: x₃ | C₂: x₃ |
|---|---:|---:|---:|
| (0,0) | 0 | 1 | 2 |
| (0,1) | 2 | 0 | 1 |
| (0,2) | 1 | 2 | 0 |
| (1,0) | 2 | 0 | 1 |
| (1,1) | 1 | 2 | 0 |
| (1,2) | 0 | 1 | 2 |
| (2,0) | 1 | 2 | 0 |
| (2,1) | 0 | 1 | 2 |
| (2,2) | 2 | 0 | 1 |

## C20.01-W1 — Worked classification

For (2,2,2), the sum is 6=2×3+0, so λ=0. For (0,0,1), λ=1; for (0,0,2), λ=2. To find the C₀ node beginning (1,2), compute x₃≡0−1−2=−3≡0. The node (1,2,0) checks because its sum is 3. The table gives 9+9+9=27 nodes without repetition: different first pairs differ, and different classes have different residues.

## C20.01-P1 — Guided practice, with answers

Find the C₂ node beginning (2,1), then the C₁ node beginning (2,2). Enumerate C₂ using the fixed pair order.

Answers: 2−2−1=−1≡2 gives (2,1,2); 1−2−2=−3≡0 gives (2,2,0). The ordered C₂ list is (0,0,2), (0,1,1), (0,2,0), (1,0,1), (1,1,0), (1,2,2), (2,0,0), (2,1,2), (2,2,1). Its sums are 2,2,2,2,2,5,2,5,5, all residue 2.

> Claim scope: S02#/backbone_sequence/15/definitions supplies X, λ and Cᵣ. Enumeration is freshly checkable finite mathematics. The three classes are the source's family-label construction; counting them alone does not identify which physical carrier is occupied. Family labels are not detector parity, chirality, projective signs, or primitive lifts.

## Diagnostic checks

1. What is −5 modulo 3?
2. Which class contains (2,0,2)?
3. Why are there nine nodes in C₁, rather than three?
4. **C20.01-D1:** Does the existence of three classes itself establish simultaneous physical occupation?

Worked answers: (1) −5=−2×3+1, so 1. (2) The sum is 4, so C₁. (3) There are nine freely chosen first-coordinate pairs and one third coordinate for each. (4) No; the class count specifies the label space. Identifying the occupied carrier needs the source premises examined in lesson 6.

Next dependency: [Lesson 2](lesson-02.md) assigns values to these ordered nodes and retains both averages and detail.
