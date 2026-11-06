# Lesson 06 — Chirality as a graded construction

**Essential question:** How can two independent kinds of labels be correlated without being identified?

**Goals:** Construct projectors from a two-state grading; compute a four-state correlation and its complement; verify an anticommutation example; calculate supplied angular/spin counts with their scope limits.

**Bridge:** Lesson 04 taught projectors and Lesson 05 separated orientation fields. Here we use plus/minus labels in algebra, but declare what each labels. A shared sign is not a shared physical meaning.

**Pacing:** Three 55-minute periods, each retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. A: grading and matrix products. B: paired labels and reconstruction. C: angular/spin counts and source scope.

## C18.06-E1 — A grading splits a carrier

A carrier is the space of states on which maps act. A grading G gives a plus or minus label and obeys G²=I. In our two-coordinate example G=diag(1,−1). Acting twice restores (x,y): G(x,y)=(x,−y), then G²(x,y)=(x,y).

Define P_plus=(I+G)/2 and P_minus=(I−G)/2. Division of a matrix by 2 divides every entry. Thus P_plus=diag(1,0), P_minus=diag(0,1). They select the plus and minus slots. Algebra also verifies this for any G²=I: (I+G)²/4=(I+2G+G²)/4=(I+G)/2, and (I−G)(I+G)/4=(I−G²)/4=0. The two projectors sum to I. For orthogonal projectors, additionally require G†=G; our diagonal G meets it.

A second map X swaps the two slots: X=[[0,1],[1,0]]. Compare GX and XG. Acting on (x,y), GX gives (y,−x), while XG gives (−y,x). Their sum is zero. The relation GX+XG=0 is called anticommutation. It says this X exchanges the two grades. It does not identify G with a spacetime operator.

Now form two **independent** label sets, (L,R) and (even,odd). Their paired carrier has four labels in the fixed order (L,even),(L,odd),(R,even),(R,odd). The tensor symbol ⊗ means pair the factors: a map A⊗B applies A to the first label and B to the second. For these selector maps it simply keeps pairs satisfying both selections. Applying a first-factor selector and a second-factor selector in either order gives the same answer, so they commute.

Set P_L=diag(1,0), P_R=diag(0,1) in the (L,R) factor; P_even=diag(1,0), P_odd=diag(0,1) in the other. Define Π=P_L⊗P_even+P_R⊗P_odd. It keeps the correlated pairs (L,even) and (R,odd). The pairs (L,odd) and (R,even) still exist, in the complement. To align the source convention P_L=(I−γ_5)/2, the toy γ in (L,R) order would be diag(−1,+1). The earlier generic G=diag(+1,−1) had no L/R names attached. Declaring this sign assignment prevents a silent convention swap.

## C18.06-W1 — Select, then retain the complement

The two terms of Π are diag(1,0,0,0) and diag(0,0,0,1), so Π=diag(1,0,0,1). Hence Π²=Π and Π†=Π. On v=(1,2,3,4), Πv=(1,0,0,4). The complement (I−Π)v=(0,2,3,0) is retained. Their sum recovers v; squared norms 17 and 13 sum to the original 30. Orthogonality is visible slot by slot.

Notice that L was not renamed even. There are two L-labeled coordinates, with different second labels. A rule selecting one pair does not eliminate the need for both label sets.

## C18.06-P1 — Independent practice

Apply Π and I−Π to (2,−1,0,3). Reconstruct. Separately compute GX and XG as matrices, verify their sum, and check P_minus² and P_minus P_plus.

**Worked answer:** The two parts are (2,0,0,3) and (0,−1,0,0); their sum is (2,−1,0,3), squared norms 13+1=14. GX=[[0,1],[−1,0]], XG=[[0,−1],[1,0]], so their sum is the zero matrix. P_minus²=diag(0,1) and P_minus P_plus=diag(0,0). Separate-factor selection commutes because each leaves the other label untouched.

## C18.S02-E1 — Supplied representation counts

The angular branch supplies a family of carriers H_ell, with ell=0,1,2,… and dimension 2ell+1. Dimension counts independent coordinate slots. The direct sum through cutoff m means placing these carriers beside one another, so their dimensions add. The sum 1+3+…+(2m+1) equals (m+1)²: starting from 1=1², the next odd number 2m+1 is exactly the difference (m+1)²−m².

Pairing each angular slot with two spin labels doubles the count. The source also supplies a regrouping rule: for ell≥1 the spin-paired block splits into labels j=ell+1/2 and j=ell−1/2, with counts 2j+1 each. At ell=0 only j=1/2 remains. We evaluate this supplied rule; we do not derive the rotation representation theory called the SO(3)/SU(2) tower or Clebsch–Gordan splitting. The two spin labels here are not the L/R chirality labels from the earlier exercise.

The source quantity C₂ has supplied eigenvalue ell(ell+1). In this use an eigenvalue is the factor by which an operator scales vectors in its labeled block. These are dimensionless representation values. No conversion into physical energy is supplied.

## C18.S02-W1 — Cutoff two

At m=2 the counts are 1,3,5. Total 9=(2+1)²; spin pairing gives 18. C₂ values are 0·1=0, 1·2=2 and 2·3=6. For ell=1, j=3/2 has dimension 2(3/2)+1=4 and j=1/2 has dimension 2; 4+2=6 equals twice 3. This is a count check, not an occupation count measured in a material.

## C18.S02-P1 — Cutoff three

Compute the total through m=3, its spin-paired count, C₂ for ell=3, the split at ell=2, and the allowed split at ell=0.

**Worked answer:** Add 7 to 9 to get 16=4²; spin pairing gives 32. C₂=3·4=12. At ell=2, j=5/2 and 3/2 have dimensions 6 and 4, giving 10=2·5. At ell=0, j=1/2 has dimension 2. There is no negative-j summand; do not invent one to extend the formula.

> **Claim scope:** S02 M14 supplies a spacetime Clifford construction and a correlation with exterior parity on a different factor. The toy G and Π verify grading algebra only. S02#/branch_proofs/5 and /proof_nodes/4, /18, /25 supply the angular/spin rules. Their exact representation scope does not supply a physical Cell3 angular Hamiltonian (the operator specifying angular energy), an energy spacing or physical occupation rule. Source-reported algebra, our finite checks and any proposed physical interpretation remain separate.

## Diagnostic checks

1. **C18.06-D1:** Why is our two-by-two grading not a complete physical chirality construction? Why does Π not mean L=even?
2. On (0,5,−2,0), find Π and its complement. Which part contains the entire record?
3. **C18.S02-D1:** Can counts 9 and 18 determine energy levels or physical occupation? What input is missing?
4. Evaluate the angular total and spin total at m=1; explain the ell=0 exception.

**Worked answers:** (1) No spacetime coframe, metric or full Clifford matrices were supplied for G. Π operates on pairs of independently defined labels. (2) Π gives zero; the complement is (0,5,−2,0), which must be retained. (3) No; a physical Hamiltonian and occupation/selection rule are not specified by the count. (4) 1+3=4, spin total 8. At ell=0 only the j=1/2 block of dimension 2 is present.

**Next dependency:** [Lesson 07](lesson-07.md) reads the archived K4 construction with a premise ledger and checks a separate finite CP witness.
