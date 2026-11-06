# lesson-04: Reconstruction and dimensional meaning

2 sessions of 55 minutes.

**Essential question:** What does a mass renderer add, and what information must remain beside it?

**Goals**

- Reconstruct channels before rendering a scalar.
- Evaluate a supplied dimensionless dot product and restore mass units.
- Identify missing occupied-state and reference-mass inputs.

## Prerequisite bridge

Lesson 3 supplied six coefficients and a complete syndrome. A dot product was taught in lesson 1. A ratio of two quantities with the same unit is dimensionless: 6 mass units divided by 2 mass units is the number 3.

<a id="C21.04-E1"></a>
## Explanation — C21.04-E1

A decoder answers how a channel vector splits under a declared geometry. A renderer answers a different question: what scalar is associated with supplied coordinates? M17 writes m/m_e=c dot b with b=(1,alpha,alpha²,alpha³,a_e,eta). In words, multiply c1 by 1, c2 by alpha, c3 by alpha², c4 by alpha³, c5 by a_e and c6 by eta, then add. Here alpha² means alpha times itself; alpha³ multiplies three copies. The renderer is dimensionless if c and b are dimensionless. Multiply by a supplied reference mass m_e to obtain a dimensional m.

The source stores alpha=0.0072973525643314245 and eta=1836.1526734259999, and describes a_e as an occupied-state coordinate. These are source witnesses with the displayed precision, not new measurements or newly established exact rational constants. A physically occupied coefficient state needs an explicit selection rule or supplied state. Solving the channel equations alone does not supply that rule. If a contributing renderer entry is missing, keep its term symbolic; for example, an absent a_e leaves c5 a_e symbolic when c5 is nonzero. If only the numerical reference mass m_e is absent, compute the dimensionless ratio m/m_e=c dot b from the supplied entries and retain m=(c dot b)m_e symbolically. Only the numerical dimensional mass remains unresolved in that case.

To practice the arithmetic without pretending to fill those gaps, use b_toy=(1,1/10,1/100,1/1000,1/5,2), and define m_ref=2 synthetic mass units. For c=(1,0,0,0,0,1), the ratio is 1+2=3 and mass is 3 times 2=6 mass units. These are separately declared classroom inputs. Retain c, b_toy, m_ref and s; the number 6 cannot reconstruct thirteen channels.

For the practice c=(0,2,0,0,1,0), the ratio is 2/10+1/5=2/5. Multiplying by m_ref gives 4/5 mass units. With s=0, the source channel matrix yields y=(0,2,2,2,0,1,-1,2,3,1,2,3,1). Even a zero syndrome must be saved as thirteen zero entries with its channel order. A negative channel in this synthetic linear system is permitted; it does not assert a negative physical mass.

Different c may give the same scalar dot product. For example in this toy renderer c=(1,0,0,0,0,0) and c=(0,10,0,0,0,0) both give ratio 1, but their channel vectors differ. Scalar rendering therefore does not replace channel decoding or residual preservation.

> Scope: The source renderer and its witness values are S02 /backbone_sequence/16. The toy renderer is synthetic and is never substituted for physical b. Neither an occupied-state rule nor a_e’s missing definition body is manufactured. Binding, coupling interpretation and measured mass require their own typed input records.

<a id="C21.04-W1"></a>
## Worked example — C21.04-W1

Small reconstruction: (7/3,10/3,17/3)+(-1/3,-1/3,1/3)=(2,3,6). For a separately synthetic renderer b_toy=(1,1/10,1/100,1/1000,1/5,2), c=(1,0,0,0,0,1) yields m/m_ref=3. If m_ref=2 mass units, m=6 mass units. Retain c and all syndrome entries.

<a id="C21.04-P1"></a>
## Guided practice — C21.04-P1

Try the operation before reading the solution. With the same b_toy, c=(0,2,0,0,1,0) gives 2/10+1/5=2/5; m=4/5 mass units for m_ref=2. Reconstruct a channel packet from this c and s=0 using the pinned A; do not substitute b_toy for source b.

### Answered practice: reference mass withheld

Use the existing synthetic c=(1,0,0,0,0,1) and b_toy=(1,1/10,1/100,1/1000,1/5,2), but withhold the numerical value of m_ref. Find the ratio and state exactly what remains unresolved.

**Answer:** c dot b_toy=1+2=3, so m/m_ref=3 and m=3*m_ref. The dimensionless ratio is completely computed. The numerical dimensional mass remains unresolved until m_ref is supplied. Keep the coefficient and syndrome records; withholding the reference mass does not erase their known values.

<a id="C21.04-D1"></a>
## Diagnostic checks — C21.04-D1

1. Compute the practice mass and list the required synthetic inputs.
2. Why does a mass ratio have no mass unit?
3. If a_e is missing and c5 is nonzero, what result can be reported?
4. Show why saving just m cannot preserve the syndrome.

## Worked answers

1. The ratio is 2/5 and m=4/5 mass units. Inputs: the six c values, b_toy, m_ref=2 mass units, A and thirteen zero s entries.
2. The numerator and denominator have the same unit, which cancels; restoring mass requires multiplication by a reference mass.
3. Report the symbolic term c5 a_e with the other known terms and mark the occupied-state input unresolved.
4. Changing s while keeping c fixed changes y=Ac+s but leaves c dot b unchanged. Thus many complete channel packets can share one rendered mass.

**Boundary to carry forward:** Neither b nor a solver chooses a physical occupied c. Missing contributing renderer entries leave their terms symbolic. If only m_e is absent, report the computable dimensionless ratio c dot b and retain m=(c dot b)m_e symbolically; the numerical dimensional mass is unresolved. A rounded report 2.33 is not exact 7/3; retain their difference.

**Next dependency:** [lesson-05](lesson-05.md). Use this lesson’s reconstruction and scope checks there.
