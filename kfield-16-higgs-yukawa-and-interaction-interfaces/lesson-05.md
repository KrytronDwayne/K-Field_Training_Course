# Lesson 5 — Yukawa maps and mixing inputs

Essential question: Why does knowing an allowed interaction leave its numerical coefficients undetermined?

Goals: apply a two-by-two coefficient map; distinguish matrix shape from entries; perform a reversible basis swap; track mass normalization and units.

Bridge: lessons 1–2 establish the interaction's type and invariant scalar structure; lesson 4 shows how supplied numbers affect outputs. Two 55-minute periods, each with 5 retrieval, 20 teaching/examples, 15 practice, 15 diagnostics/repair. Period 1 introduces matrix action, period 2 basis changes and reversibility.

## C16.05-E1 — A table of coefficients is a rule

A matrix is a rectangular array of numbers. For a two-component column f=(f1,f2), the matrix A=[[a,b],[c,d]] sends it to (a f1+b f2,c f1+d f2). Each row gives one output; each column records how one input contributes. The notation [[a,b],[c,d]] lists rows. This is a finite linear map: scaling and adding inputs scales and adds outputs. Matrix multiplication means composition: AB acts by B first, then A. You can compute each output directly without memorizing a general multiplication algorithm.

We write Y_Yuk for the supplied Yukawa coefficient matrix, reserving Y_h for hypercharge. A family label distinguishes copies of the matter structure. It is not a weak slot, color slot, handedness, or detector parity. A two-family teaching model illustrates the map; it is not a claim that the source has only two physical families. Compatibility determines which sectors can connect. It does not supply the numerical entries of Y_Yuk or the state f.

Use dimensionless entries and dimensionless f in the exercises. Y_Yuk f is dimensionless. For a declared classroom mass convention, M=(v/√2)Y_Yuk has entries in μ, so Mf has mass units. A matrix's entries and a map output are not automatically particle mass eigenvalues; we do not ask you to diagonalize a physical mass operator.

A basis change relabels the component coordinates. The swap matrix P=[[0,1],[1,0]] sends (x,y) to (y,x); doing it twice restores the original vector, so P⁻¹=P. Transpose, marked T, interchanges rows and columns. Here P^T=P=P⁻¹. If we swap both input and output coordinates, use Y′=P Y_Yuk P^T and f′=Pf. Then Y′f′=P Y_Yuk P^T P f=P Y_Yuk f because P^T P=I. This changes coordinates while preserving the map's meaning. It is a reversible relabeling, not deletion of a component.

## C16.05-W1 — Worked row-by-row action

Choose synthetic Y_Yuk=[[1,2],[0,3]] and f=(2,−1). The first row gives 1×2+2×(−1)=0; the second gives 0×2+3×(−1)=−3. The output is (0,−3). A zero output component is a retained result, not a reason to erase an input. In the separate normalization example v=√2 μ, v/√2=1 μ, so M has the same numerical entries as Y_Yuk, each multiplied by μ. Mf=(0,−3) μ. Preserve Y_Yuk, f, v, units, and output to replay the computation.

## C16.05-P1 — Practice a map and its swap

Use synthetic Y_Yuk=[[2,0],[1,1]] and f=(1,2). Compute the output, swap both coordinate lists, find Y′ and f′, then compute the new output. Show how to recover the original records.

Worked answer: the original output is (2×1+0×2,1×1+1×2)=(2,3). Swapping rows gives P Y_Yuk=[[1,1],[2,0]]. Swapping columns then gives Y′=[[1,1],[0,2]]. The new input is f′=(2,1); the new output is (1×2+1×1,0×2+2×1)=(3,2), exactly P(2,3). Undo with f=Pf′ and Y_Yuk=P Y′ P, recovering all coefficients. This coordinate change introduces no residual. If v=2 μ, M=√2 μ times Y_Yuk and Mf=(2√2,3√2) μ; this optional normalization uses the same rule, not a new physical inference.

> Claim scope: S02 /backbone_sequence/11 lists Yukawa coefficient matrices and mixing coordinates as occupied-state inputs; /proof_nodes/84 preserves that boundary. All matrix numbers, states, and the classroom normalization above are explicitly supplied examples. A simple simultaneous swap teaches consistency; general mixing can involve different basis changes on input and output, and physical mixing parameters require additional specification.

## Diagnostics and worked answers

1. **C16.05-D1:** Can charge cancellation pick a Yukawa matrix or mixing angle? Answer: no. It checks compatibility, not numerical coefficients or relative basis choices.
2. **C16.05-D2:** Keep Y′ from P1 but forget to swap f. What output results? Answer: [[1,1],[0,2]](1,2)=(3,4), not the required (3,2). Mixing coordinate conventions changes the calculation.
3. **C16.05-D3:** Replace W1's matrix by the identity with the same shape. What happens? Answer: the output becomes (2,−1), demonstrating that shape alone does not select the result.
4. **C16.05-D4:** Is replacing (2,3) by its sum 5 reversible? Answer: not from 5 alone; many pairs have that sum. Retain both components or enough additional coordinates to reconstruct them. The swap, by contrast, has an explicit inverse.

Next dependency: [Lesson 6](lesson-06.md) uses the same preservation discipline for signed energy changes.
