# Lesson 07 — Infinite objects and operator domains

Essential question: Why can an operation work on every finite truncation and still fail on a complete sequence?

Goals: Specify an operator's input space, domain and action; prove convergence with a block bound; test two sequences against an explicit domain; classify source claims by supplied assumptions.

Bridge and pacing: Lesson 04 proved geometric convergence, and Lesson 06 taught dot products, identity operations and reconstruction. Two 55-minute periods, each retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Period 1 develops the sequence space and block proof; period 2 tests domains and source cards. No calculus is needed.

## C22.07-E1 — An input rule includes an allowed set

An operator is a function that acts on objects such as vectors or sequences. Its carrier (ambient space) specifies what kinds of objects are under discussion. Its domain is the subset on which this particular action has an allowed output. Giving an action formula alone does not specify either set.

For this lesson use real sequences x=(x₁,x₂,…) indexed by positive integers. Define ℓ² as those sequences for which Σx_n² is finite. Its norm is ||x||₂=√(Σx_n²); its inner product is ⟨x,y⟩=Σx_n y_n. To justify this infinite inner product, first prove a finite inequality. For lists a₁,…,a_N and b₁,…,b_N, put A=Σa_n², B=Σb_n² and C=Σa_n b_n, where these three sums stop at N. If B=0, every b_n is zero and C=0. If B>0, the sum of squares Σ(a_n−t b_n)²=A−2tC+t²B is nonnegative for every real t. Choose t=C/B to obtain A−C²/B≥0, hence |C|≤√A√B. This is the finite dot-product inequality. Apply it to a_n=|x_n| and b_n=|y_n|: each finite sum Σ|x_n y_n| is at most ||x||₂||y||₂. These nonnegative partial sums increase and stay bounded, so they converge. Thus the signed inner product converges absolutely: the total size of every remaining signed tail is bounded by the corresponding absolute tail, which tends to zero. Merely bounded signed partial sums would not be enough. The temporary finite-sum names A,B,C in this proof are scalars; B here is not the length-valued matrix of Lesson04. Convergence in this norm means the norm of the difference tends to zero. This is stronger than saying every fixed coordinate converges. These are mathematical specifications; no measured sequence is introduced.

We need a convergence test for Σ1/n². Split positive integers into blocks 2^k≤n<2^(k+1), for k=0,1,2,… . The block has 2^k entries, each at most 1/(2^k)². Its sum is therefore at most 2^(−k). Adding the block bounds gives 1+1/2+1/4+…=2 by Lesson 04. Partial sums of 1/n² increase but stay at most 2, so they approach a finite limit. Moreover the sum from n=2^K onward is at most Σ_(k≥K)2^(−k)=2^(1−K), which tends to zero. We do not need the exact sum.

Define D by (Dx)_n=nx_n, with domain Dom(D)={x∈ℓ²: Σn²x_n²<∞}. The domain condition says precisely that the proposed output lies in ℓ². A rule can be meaningful on a proper subset of its carrier. D is unbounded: the sequence with a single 1 in position m has norm 1, while its output has norm m; no fixed constant bounds all output norms by that constant times the input norm. Unbounded does not mean undefined everywhere.

## C22.07-W1 — Finite success and infinite failure

Let x_n=1/n. Its squared sum is Σ1/n², finite by the block proof, so x∈ℓ². But Dx=(1,1,1,…), whose first N squared entries sum to N. Thus Dx∉ℓ² and x∉Dom(D).

Let x^(N) retain the first N entries of x and set all later entries to zero. This is an explicitly labeled truncation accompanied by the exact removed tail rule x_n=1/n for n>N. Every x^(N) belongs to Dom(D), since its weighted squared sum is the finite number N. Also x^(N)→x in ℓ²: its squared error is the tail of Σ1/n², bounded by the block argument. Yet x is outside the domain. Finite membership and input convergence alone cannot pass an operator through a limit. The output norms √N already reveal the failure.

> Claim scope: D is an explicitly authored domain example, not an archival K-Field history operator. S02 M18's convergent renderer supplies neither this D nor a universal claim about other operators. Self-adjointness (equality with the adjoint on the appropriate domain) is an advanced property whose proof is outside this course; it must never be inferred merely from renderer convergence or a label.

## C22.07-P1 — Practice, then check

Test y_n=1/n² for the domain of D and compute Dy. Then inspect this source card: “M18 specifies compatible addresses, a real renderer and a retained-detail filtration; no particular history-operator action or operator domain is stated in that module.” List what would still be needed to apply a proposed history operator H.

Answer: Σy_n²=Σ1/n⁴≤Σ1/n²<∞ because n≥1. The weighted sum Σn²y_n²=Σ1/n² is finite, so y∈Dom(D) and (Dy)_n=1/n∈ℓ². For H one needs the carrier (for example, histories themselves or functions on histories are different choices), domain, action, norm/topology or inner product where relevant, and the convergence mode for any infinite formula. The card does not provide these for H; mark them “not supplied for H,” not “false” or “supplied by D.”

## Diagnostics — C22.07-D1

1. Why is the constant sequence (1,1,…) outside ℓ²?
2. Does y_n=1/n³ belong to Dom(D)?
3. If every finite truncation lies in Dom(D), must the full sequence lie there?
4. What information belongs in a final paired-rendering report?

Worked answers: (1) Its first N squared entries sum to N without a finite bound. (2) Yes: the input square sum 1/n⁶ and weighted square sum 1/n⁴ are each bounded termwise by 1/n². (3) No; x_n=1/n is the worked counterexample. (4) Exact digit rule or unresolved continuation, residue history and depth, signed partial image, declared B and units, tail bound and any known signed tail, retained detail vectors and reconstruction, plus source status and any proposed operator's missing assumptions.

Next dependency: [Capstone](capstone.md) uses these seven taught operations to produce a complete, source-scoped report.
