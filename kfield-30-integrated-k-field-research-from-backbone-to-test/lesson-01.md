# Lesson 1 — Rebuilding the complete dependency chain

Essential question: What must be supplied before a geometric construction can support an instrument prediction?

Goals: Draw a directed dependency map; classify premises and outputs; perform a finite coordinate construction; carry source boundaries into a downstream claim.

Prerequisite bridge: A coordinate triple is an ordered list of three numbers. Multiplying a column by a number scales all its entries; adding columns adds matching entries. An arrow A → B means that B uses A. These operations bridge the earlier courses on geometry, evidence, instruments, and closure; this course supplies the small examples needed for its assessments. No calculus or advanced algebra is required.

## C30.01-E1 — A chain has inputs as well as arrows

A dependency map is a recipe with return addresses. A **premise** is accepted at the start of a particular argument. A **derived object** is constructed using those premises. A **domain hypothesis** says where an operation is allowed: division requires a nonzero divisor. A **state coordinate** selects a particular state inside a permitted family. Proving that a family has six coordinates does not choose their six values.

The mature source S02 names M20 the closure theorem. Its `/backbone_sequence/19/requires` lists M01 through M18. Read the full module table in [sources.md](sources.md), which preserves every source-local `requires` entry, including the two non-module premises of M13. The five groups of work are geometry (M01–M03), retained calculus and shape/graphs (M04–M08), internal carriers (M09–M11), interactions/history/action/families (M12–M16), and decoding/continuum (M17–M18). Grouping helps reading but does not replace the individual edges.

S02 `/constitutive_principles` supplies six EG principles: retain the complete state (A1); require a decoder for a lossless transform (A2); define a finite change by subtraction (A3); retain the joint product of finite changes (A4); retain residuals as next-channel information (A5); keep units, scale, and approximation as typed views of a preserved source (A6). They are constitutive premises in this reading. A decoder reverses an encoding: if T encodes and D decodes, D(T(state))=state.

M20 also carries four state-coordinate entries: scale before the locked area anchor, time/action normalization, vacuum magnitude with admitted operator coefficients, and an occupied six-coordinate mass/coupling state. An anchor fixes a scale; a normalization fixes a convention for numerical values. These inputs must travel with any resulting prediction. History operators, finite gauge hypotheses, spin/coframe data, phase metrics and replay matrices need their declared domains and bodies too (S03 AUD-011).

M19 contains separately retained branches, including a gravity scalar lift, reciprocal-plane inversion and exceptional carrier constructions. Equal dimensions do not construct an action relating two objects: an explicit structure-preserving map would be needed. The corrected core chain therefore has no M19 → M20 arrow. S03 AUD-001 corrects the serialized edge ledger; it does not erase M19.

## C30.01-W1 — Read and use the chain

There are 18 core requirements in the M20 list: counting inclusively from 1 to 18 gives 18. The decoder M17 uses M05 and M11; the continuum renderer M18 uses M03 and M04. Both then feed M20. Write `M05,M11 → M17 → M20` and `M03,M04 → M18 → M20`. The complete table in sources.md lets you expand those inputs recursively rather than guessing from module numbers. The internal `requires` graph has 52 edges; its 18 incoming M20 edges are included in that count.

Here is one actual operation from the geometric side of that chain. The source uses x = O_K + Bq. Here x and O_K are physical position and origin, q is a dimensionless address, and B has three length-valued columns a,b,c in the ICRS celestial frame. For synthetic q=(1/2,0,0), x−O_K is half column a. The input column is a=(0.3275012420558906, −0.0548970078840064, −0.0374875028947299) nm, from S02 `/mature_locked_cell3/B_nm/0/0`, `/mature_locked_cell3/B_nm/1/0` and `/mature_locked_cell3/B_nm/2/0`. Divide each entry by 2. With this stored mature column, the result is (0.1637506210279453, −0.0274485039420032, −0.01874375144736495) nm. This is a calculation on stored decimals, not a new spatial measurement.

Cell ownership uses z=floor(q+1/2), applied separately to each component. Floor means the greatest integer no larger than its input. Thus z=(1,0,0) and u=q−z=(−1/2,0,0). Reconstruction gives z+u=q. The half-open interval [−1/2,1/2) includes its left endpoint and excludes its right endpoint. This assigns a shared boundary to exactly one cell. It is distinct from a rounding rule for residual integerization.

## C30.01-P1 — Practice, then check

Draw the M17, M18 and M19 branches, classify EG-A2 and the occupied vector c, and assign q=(−1/2,0,0) to a cell.

Answer: M17 and M18 have the inputs above and feed M20. M19 uses M07,M08,M10,M13,M18 and remains separate. EG-A2 is a constitutive premise; c supplies a state rather than being selected by a dimension count. For q=(−1/2,0,0), z=(0,0,0), u=(−1/2,0,0), and reconstruction is exact.

> Claim scope: The module roles and theorem are source-attributed. Reading their dependencies is not fresh verification of every proof body. The coordinate arithmetic is freshly checkable. The mature B has an intentional negative determinant; no axis is flipped to make it positive. Reciprocal identities use x−O_K, not an unshifted position. Source gaps and historical numerical branches remain in sources.md.

## C30.01-D1 — Diagnostics and worked answers

1. A diagram contains M19 → M20 but omits M01 → M20. What changes? **Answer:** Remove the former from the core graph and restore all M01–M18 incoming edges, following source `requires` and AUD-001.
2. Does knowing six coefficient slots determine six masses? **Answer:** No. The occupied coefficient values are supplied state coordinates; a renderer evaluates them after selection.
3. Why does q=+1/2 move to the next cell? **Answer:** floor(1)=1 and the retained local coordinate is −1/2; the current cell excludes +1/2.
4. What is lost by saying “Cell3 alone proves M20”? **Answer:** The six constitutive premises, domain hypotheses and supplied states disappear. Restore the complete contract before using the closure statement.

Next dependency: [Lesson 2](lesson-02.md) assigns each arrow's evidence a precise scope.
