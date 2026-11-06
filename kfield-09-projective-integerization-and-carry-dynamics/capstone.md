# Capstone — An exact finite carry ledger

Allow two 55-minute periods. Work with the clearly synthetic normalized ray T=(1,1/3,1/4), coordinate order (a,b,c). All ratios are dimensionless. Produce one labeled ledger plus an audit paragraph. Exact fractions are required; a decimal calculator may check arithmetic but must not choose the tie convention implicitly.

Period 1: retrieve definitions (5 min), declare metadata and build the table (25), derive/check carries and side modes (20), inspect residual signs (5). Period 2: compare rays (15), decode the finite record in both directions (20), interpret the supplied historical card (10), review and correct (10).

## Student task

1. **C09-CAP-01 — Rules to test cases.** Write nint, its tie behavior, and the residual sign. Evaluate ±1/2. Contrast the cell owner at both ties. Inputs: two signed ties; outputs: integer, residual, and owner for each.
2. **C09-CAP-02 — Ray to integer records.** Compute K_g, exact K_g T, and Q_g for g=0,1,2. Label the ray as synthetic and list coordinate order, branch, and precision. Inputs: T and generation range; output: three rows.
3. **C09-CAP-03 — Records to exact recovery.** Compute every epsilon_g and recover all three ray coordinates independently from each row. State the difference between epsilon_g and epsilon_g/K_g. Output: residual column and three recovered triples.
4. **C09-CAP-04 — Rows to reversible side coordinates.** Derive C_g=epsilon_g−27epsilon_(g−1) from the two scaled equations. Compute C_1,C_2 by integer subtraction and residual rounding. Compute S,A and recover both side carries by inverse halves. Explain why (S,A)=(1,0) must be rejected as an integer carry encoding.
5. **C09-CAP-05 — Two rays to a first split.** Compare T with T'=(1,1/3+1/10000,1/4) through g=3. Record the integer and full signed residual triples, naming shared coordinates explicitly if you abbreviate. Identify the first integer difference and the earlier residual difference. Then use the historical card from lesson 05: locked g8 Q=(282429536481,206098790228,153815932939), master g8 Q=(282429536481,206098790236,153815932946), with checked agreement at g0..7. Compute master-minus-locked and explain what was replayed and why neither branch replaces the S02 active ray. No large-number multiplication is required for this source-reading step.
6. **C09-CAP-06 — Finite ledger to original normalized input.** Starting from Q_0, C_1,C_2, and epsilon_2, expand Q_2 and decode T by the finite carry sum. State exactly what is lost by omitting the terminal residual. Starting instead with S,A and epsilon_2, reverse every side transform and every residual update; then check direct rounding of the recovered input. Finish with a metadata checklist and a statement of what the decoder does and does not recover.

## Full answer key

**01.** nint(t)=ceil(t−1/2), lower integer at each half-tie; epsilon=Q−t. At +1/2, Q=0, epsilon=−1/2, owner=floor(1)=1. At −1/2, Q=−1, epsilon=−1/2, owner=floor(0)=0. The residual interval is [−1/2,1/2). Cell ownership uses q−owner; integerization uses Q−q.

**02–03.** Use branch “synthetic T,” exact fractions, slots (a,b,c), K_g=27^g, and the above sign and tie rules.

| g | K | K T | Q | epsilon |
|---|---:|---|---|---|
| 0 | 1 | (1,1/3,1/4) | (1,0,0) | (0,−1/3,−1/4) |
| 1 | 27 | (27,9,27/4) | (27,9,7) | (0,0,1/4) |
| 2 | 729 | (729,243,729/4) | (729,243,182) | (0,0,−1/4) |

At g0 the decoder gives (1−0,0+1/3,0+1/4)=(1,1/3,1/4). At g1 it gives (27/27,9/27,(7−1/4)/27)=(1,1/3,1/4). At g2 it gives (729/729,243/729,(182+1/4)/729)=(1,1/3,1/4). Epsilon is a count-coordinate residual; epsilon/K is the ratio-coordinate difference Q/K−T. Neither is silently erased.

**04.** Subtract 27Q_(g−1)=K_g T+27epsilon_(g−1) from Q_g=K_g T+epsilon_g to cancel the common input. C_1=(27,9,7)−27(1,0,0)=(0,9,7). C_2=(729,243,182)−27(27,9,7)=(0,0,−7). Residual rounding gives nint(0,9,27/4)=(0,9,7) and nint(0,0,−27/4)=(0,0,−7). S_1=16,A_1=2; halves give 9,7. S_2=−7,A_2=7; halves give 0,−7. Opposite parity S=1,A=0 gives half-integers, so it cannot encode integer carries. The a carry remains separately 0.

**05.** The complete comparison is:

| g | Q(T) | epsilon(T) | Q(T') | epsilon(T') |
|---|---|---|---|---|
| 0 | (1,0,0) | (0,−1/3,−1/4) | (1,0,0) | (0,−10003/30000,−1/4) |
| 1 | (27,9,7) | (0,0,1/4) | (27,9,7) | (0,−27/10000,1/4) |
| 2 | (729,243,182) | (0,0,−1/4) | (729,243,182) | (0,−729/10000,−1/4) |
| 3 | (19683,6561,4921) | (0,0,1/4) | (19683,6563,4921) | (0,317/10000,1/4) |

T' has scaled b=6562.9683 at g3, rounded to 6563, so its residual is 0.0317. First integer difference is g3, while residual difference begins at g0 with epsilon'_b−epsilon_b=−1/10000. Historical master-minus-locked g8 is (0,8,7). The report concerns S01's two stored decimal strings under the explicit course rounding contract; it agrees with the source report. Those historical identities and the S02 active input have separate provenance. Equality of some integer rows does not make rays or source branches identical.

**06.** Q_2=729Q_0+27C_1+C_2=(729,243,189−7)=(729,243,182). T=Q_0+C_1/27+C_2/729−epsilon_2/729. Thus a=1, b=9/27=1/3, and c=7/27−7/729+1/2916=729/2916=1/4. Omitting epsilon_2 loses the positive third-coordinate correction 1/2916 and leaves 182/729.

Decode S,A as in 04. Then epsilon_1=(epsilon_2−C_2)/27=(0,0,1/4), and epsilon_0=(epsilon_1−C_1)/27=(0,−1/3,−1/4). Forward Q updates reproduce the table. Direct rounding of K_g T reproduces Q at every row, independently confirming the stored table. Retain input identity/branch, exact input precision, coordinate ordering, generation, scale rule, rounding rule, residual sign, all signed residual coordinates, side-mode definitions, separate C_a, and units. Exact normalized T is recovered; an unrecorded original common magnitude or unsupplied decimal digits are not.

## Rubric — 100 points

| Step | Points | Observable criteria |
|---|---:|---|
| 01 | 15 | rule/sign/interval 5; signed ties 6; ownership contrast 4 |
| 02 | 15 | scales 3; exact scaled inputs 6; integer triples and metadata 6 |
| 03 | 15 | full residuals 6; three exact reconstructions 6; coordinate-unit distinction 3 |
| 04 | 20 | cancellation derivation 6; both carry routes 6; modes/inverses 5; parity rejection 3 |
| 05 | 15 | complete comparison/residuals 8; first split and earlier difference 4; historical scope 3 |
| 06 | 20 | finite formula 5; exact evaluation/terminal correction 5; backward replay 6; metadata/scope 4 |

Award arithmetic follow-through credit when a single error is propagated transparently; still require its correction before certifying mastery of an exact decoder. A high total does not compensate for an unresolved tie-rule, sign, branch, parity, or terminal-residual failure. Return that operation for targeted practice and reassessment. The outcome is a correct, reproducible finite ledger, not a score alone.

Source scope: synthetic assessment with one supplied archival comparison card. No physical measurements, infinite-series proof, gauge transport, or mass identification is being assessed.
