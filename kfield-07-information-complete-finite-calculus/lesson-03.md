# Lesson 03 — Coarse and detail coordinates

Essential question: Can averaging be part of a reversible transformation?

Goals: compute a mean and signed half-difference for each fixed pair; reconstruct the original entries; distinguish a compact encoding from an expanded coarse/detail view.

Prerequisite bridge: Lesson 01 recovered a state by adding a retained change. Lesson 02 showed that separating a quantity into parts requires keeping every term. Now use fractions to create two new coordinates for two old ones. Check (2+5)/2=7/2 and (5−2)/2=3/2 before continuing.

## C07.03-E1 — Two coordinates for two entries

For an ordered pair (a,b), define its mean m=(a+b)/2 and signed half-difference d=(b−a)/2. Here d is a pair coordinate; df in Lessons 01–02 is a full edge difference. The decoder is (a,b)=(m−d,m+d), because

    m−d = (a+b−b+a)/2 = a,
    m+d = (a+b+b−a)/2 = b.

Thus retaining both numbers, their order, and the pair membership preserves the original values. A mean alone is many-to-one: (2,4) and (1,5) both have mean 3. Their details are 1 and 2. If (a,b) is reversed, m stays the same and d changes sign. The sign preserves which sample was larger.

For four entries keep fixed blocks {0,1} and {2,3}. Define an operator E, meaning a rule applied to a whole list, which replaces each pair by its repeated mean. Define I to mean the identity rule I(f)=f. Define Q=I−E, so Qf=f−Ef is the detail list. Subtraction is entry by entry. Q here is a detail operator, not any geometric distance or the later integer Q_g. A block's expanded detail is (−d,d). Then f=Ef+Qf at every original sample ID.

The compact encoding stores two means and two half-differences. The expanded view repeats each mean and lists both signed detail entries. They describe the same information, provided the block map is preserved. We retain small expanded examples to make residual accounting visible; real source data need not be duplicated merely to create another view. Exact decoding rules can document the relationship.

## C07.03-W1 — Worked pair transform

Take f=(2,5,4,9) SU. For block {0,1}, m_1=7/2 and d_1=3/2 SU. For {2,3}, m_2=13/2 and d_2=5/2 SU. Thus Ef=(7/2,7/2,13/2,13/2) and Qf=(−3/2,3/2,−5/2,5/2) SU. Decode: 7/2−3/2=2, 7/2+3/2=5, 13/2−5/2=4, 13/2+5/2=9. A zero sum of details within a block does not mean its individual details vanish.

> Claim scope: This is a fully specified synthetic transform. EG-A2 at S02#/constitutive_principles/1 states the decoder premise; our two displayed equalities prove this particular decoder. General operators E in archival formulas need additional properties, taught next. No physical averaging law is inferred.

## C07.03-P1 — Practice

Transform h=(3,7,6,10) SU with the same blocks. Keep compact coordinates and expanded views. Recover the entries, citing EG-A2.

Answer: m=(5,8), d=(2,2) SU; Eh=(5,5,8,8), Qh=(−2,2,−2,2) SU. Decode (5−2,5+2,8−2,8+2)=(3,7,6,10). EG-A2 asks for a decoder; this one is exhibited and checked.

## Diagnostics

1. **C07.03-D1:** Explain why mean 3 cannot distinguish (2,4) from (1,5), and compute both missing coordinates. What changes if the first pair is reversed?
2. **C07.03-D2:** Transform (7,3) SU and decode it. Is a negative d allowed?
3. **C07.03-D3:** A record keeps means (5,8), unsigned detail magnitudes (2,2), and no ordering. Can it determine h uniquely? Give a competing list.

Worked answers: D1: both sums equal 6; d is 1 versus 2. Reversal to (4,2) gives d=−1. D2: m=5,d=−2 SU; (5−(−2),5+(−2))=(7,3); signed details are required. D3: no; (7,3,10,6) has those same means and magnitudes. Keep signs, IDs and block support.

Next dependency: [Lesson 04](lesson-04.md) tests the exact properties of E needed to distribute products across coarse and detail parts.
