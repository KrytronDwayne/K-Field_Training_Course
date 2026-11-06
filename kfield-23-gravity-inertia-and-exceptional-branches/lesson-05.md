# Lesson 05 — An action needs more than a matching dimension

**Essential question:** What must a map preserve before two equal-sized mathematical descriptions represent the same action?

**Goals.** By the end, you can (1) multiply small matrices and verify an involution, (2) test a proposed intertwiner while retaining its complete defect matrix, and (3) specify missing construction inputs for an exceptional-action proposal.

**Prerequisite bridge.** Lesson 04 counted independent cycle coordinates. A dimension tells us how many coordinates we need; it does not tell us what transformations do to those coordinates. We now build and compare transformations on two real-number coordinates. These synthetic examples are dimensionless and are not asserted to be the archived F4 construction.

**Time:** two 55-minute periods. Each uses 5 minutes retrieval, 20 instruction/worked example, 15 practice, and 15 diagnostic checks and repair. Period 1 teaches operators and a successful map. Period 2 teaches failed maps and the missing-action checklist.

## C23.05-E1 — Operators, composition, and a map between actions

A column vector (x,y) records two ordered coordinates. A 2×2 **matrix** is a rule taking one such vector to another. For

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
A\binom{x}{y}=\binom{ax+by}{cx+dy},
\]

the first output is the first row times the input column, added; the second uses the second row. Thus diag(1,−1), meaning a diagonal matrix with those entries and zeros elsewhere, sends (x,y) to (x,−y).

Matrix multiplication represents composition: AB means apply B first, then A. Each entry of AB is the corresponding row of A multiplied against a column of B, then summed. For example,

\[
\begin{pmatrix}1&2\\0&1\end{pmatrix}
\begin{pmatrix}3&0\\4&1\end{pmatrix}
=\begin{pmatrix}1(3)+2(4)&1(0)+2(1)\\0(3)+1(4)&0(0)+1(1)\end{pmatrix}
=\begin{pmatrix}11&2\\4&1\end{pmatrix}.
\]

Matrix addition and subtraction work entry by entry. The **identity** I=diag(1,1) leaves both coordinates unchanged. An **invertible** matrix T can be undone by another matrix T⁻¹; both TT⁻¹ and T⁻¹T equal I. An **involution** is an operation whose square is I: doing it twice restores the input.

For our finite example, a symmetry has two operations: do nothing, or apply g, where applying g twice does nothing. An **action** assigns matrices to these operations while preserving the composition rule. Let ρ(g) and σ(g) be two proposed matrices, each squaring to I. The Greek letters rho and sigma label two descriptions, not residuals in this lesson. A change of coordinates T connects the descriptions if

\[
T\rho(g)=\sigma(g)T.
\]

Such a map is an **intertwiner**. The equation says “act first, then translate” equals “translate first, then act.” When T is invertible it gives an equivalence of the descriptions; a noninvertible intertwiner may lose information and does not establish equivalence. In this two-operation example, checking g and I checks all operations. A more complicated group requires its defining relations, not a single arbitrary test.

To test a proposed T, preserve its full **defect matrix** D=Tρ(g)−σ(g)T. If every entry is zero, this equation holds. If not, D records exactly which coordinates disagree. Never replace D with only a pass/fail label: the equality Tρ=σT+D lets us reconstruct the failed comparison.

## C23.05-W1 — A successful interchange map

Set

\[
\rho=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
\sigma=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\quad
T=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

We omit (g) only to shorten these computations. Applying ρ twice sends (x,y) to (x,−y) to (x,y); σ twice similarly restores both coordinates. Thus ρ²=σ²=I. The map T exchanges the coordinates, so T²=I and T⁻¹=T. It is invertible.

Compute both orders:

\[
T\rho=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\sigma T=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

For instance, the upper-right entry of Tρ is 0(0)+1(−1)=−1; that of σT is (−1)(1)+0(0)=−1. Therefore D is the zero matrix. Independently check on a general vector: Tρ(x,y)=T(x,−y)=(−y,x), while σT(x,y)=σ(y,x)=(−y,x).

Existence does not select a unique map. The matrix 2T also intertwines, since both sides of the equation simply double. Its inverse is T/2. A **canonical** choice means one selected by extra declared rules, such as a normalization and basis convention. Even demanding an invertible map has not picked one unique T.

Now test a different proposed map, T₀=I, on this same worked pair. Its defect is

\[
D_0=I\rho-\sigma I=\rho-\sigma=\operatorname{diag}(2,-2).
\]

The identity map fails although a successful exchange map exists. Failure of one proposed map is not proof that every map fails.

## C23.05-P1 — A genuinely different pair

Keep ρ=diag(1,−1) but replace the second action by σ′=−I=diag(−1,−1). (The prime distinguishes it from the worked σ.) Test the identity as a proposed intertwiner and retain the defect. Then determine whether any invertible intertwiner can exist.

**Worked practice answer.** Both actions still square to I and both use two coordinates. For T₀=I, D′=ρ−σ′=diag(2,0). This is not the worked pair's diag(2,−2): changing the second action changes the second residual entry.

To test every possible map, write T=[[a,b],[c,d]]. Multiplication gives Tρ=[[a,−b],[c,−d]], whereas σ′T=−T=[[-a,−b],[-c,−d]]. Equality forces a=−a and c=−c, hence a=c=0 over the real numbers. The first column is zero, so T sends (1,0) to (0,0) and cannot be undone. No invertible intertwiner exists.

There is also a useful short invariant. The **trace** is the sum of diagonal entries: tr(ρ)=0, tr(σ′)=−2. For two square matrices, tr(AB)=tr(BA): in two dimensions both sums consist of ae+bg+cf+dh, just reordered when A=[[a,b],[c,d]] and B=[[e,f],[g,h]]. If σ′=TρT⁻¹, this rule gives tr(σ′)=tr(T⁻¹Tρ)=tr(ρ). Their different traces therefore rule out equivalence. This proof supplements, rather than replaces, the explicit failed-map record.

## The exceptional-action construction checklist

In S02 `/backbone_sequence/18/branches/exceptional_cycle_bridge/exceptional_action_extension`, identifying the 52-cycle sector with a specific F4 action, selecting E6/E7 real forms, and coupling cohomology classes to physics are extension obligations. To turn an action proposal into a checkable construction, specify the domain (which cycle sector), coefficient field (for example real numbers), ordered basis, operators assigned to generating transformations, their defining relations, and the comparison map with its normalization. The dimension alone supplies none of these operators.

For recognition, a **Lie algebra** is a vector space equipped with a bracket describing how generators combine. In a matrix realization the bracket is the **commutator**, [A,B]=AB−BA. Order matters: matrices generally do not commute. A proposed action R must preserve the bracket:

\[
[R(X),R(Y)]=R([X,Y]).
\]

Here X and Y are generators, R assigns their operators, and [X,Y] on the right is the stipulated source bracket. Its defect is [R(X),R(Y)]−R([X,Y]). Retain this whole matrix for each required generating relation. Without the source bracket and generator assignments, the defect cannot even be computed. Students need to state this missing-input test; they are not required to invent exceptional Lie algebra generators.

For a small illustration only, let X have proposed operator A=[[0,1],[0,0]] and Y have B=[[0,0],[1,0]]. Then AB=diag(1,0), BA=diag(0,1), and [A,B]=diag(1,−1). If a proposed source relation is [X,Y]=Z and the assigned R(Z) is the zero matrix, the relation defect is diag(1,−1). That declared assignment fails this relation, and every entry of the failure remains available for repair. This synthetic example does not construct an exceptional action.

> **Claim scope.** Small matrix identities here are fresh finite checks. Archived exceptional carriers and cohomology counts remain source-attributed statements; a particular cycle action needs its own maps and relations. A missing proof body retains its retrieval status rather than inheriting a proof from a matching dimension. S03 AUD-010 (`/findings/9`) requires constituent boundaries to survive into the branch endpoint, and AUD-001 (`/findings/0`) keeps M19 separate from M20 core closure.

## C23.05-D1 — Diagnostic checks

1. Calculate [[0,1],[1,0]](2,−3). Apply the same matrix again. What does this verify?
2. For the worked ρ and σ, state the full identity-map defect. For the practice ρ and σ′, state it again. Why retain both?
3. Does the successful worked T prove a unique comparison map? Give a second invertible example.
4. A proposed F4 action supplies only a 52-dimensional cycle list. Name the missing inputs needed for an intertwiner or bracket check.
5. In the synthetic bracket example, what must R(Z) be to satisfy the displayed relation, with A and B fixed?

**Worked answers.** (1) The first output is (−3,2); the second is (2,−3). This checks the exchange operation twice on this input, consistent with the general identity T²=I already proved. (2) D₀=diag(2,−2), whereas D′=diag(2,0). They refer to different second actions; retaining the ordered pair and whole defect avoids losing the difference. (3) No. 2T is another invertible intertwiner, with inverse T/2. (4) Supply a field, explicit sector and basis, generator operators for both claimed actions, relations or brackets, and the proposed comparison map with domain, invertibility requirement, and normalization. Real-form choices and physical coupling rules are separate required inputs when claimed. (5) R(Z)=diag(1,−1) makes this one relation defect zero. It does not verify any other relation that may be required.

**Next dependency:** [Lesson 06 — Comparing mechanism classes](lesson-06.md) uses preserved predictions and residuals to compare proposed rules with declared inputs.
