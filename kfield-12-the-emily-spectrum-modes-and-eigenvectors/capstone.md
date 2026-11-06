# Capstone · Build and test the Emily ledger

Two 55-minute periods. Use exact arithmetic, show node and mode order, and retain residuals. All state values below are synthetic and dimensionless. You may use the lesson definitions and your completed practice. No general spectral theorem or decoder calculation is required.

## Student task

**C12-CAP-01 (8 points).** Use node order (−1,0,1) and A=[[0,1,0],[1,0,1],[0,1,0]]. Compute A(2,−1,0), showing every row. Explain the input-carrier difference between A and the path incidence D.

**C12-CAP-02 (10 points).** For the two-node swap S, verify (1,1) and (1,−1) with eigenvalues 1 and −1. Verify the scaled path mode A(2,0,−2)=0. Explain why zero input is excluded but zero eigenvalue is permitted.

**C12-CAP-03 (18 points).** Starting with A(a,b,c)=λ(a,b,c), separate λ=0 and λ≠0 and derive all possible eigenvalues. Verify all three vectors (1,√2,1),(1,0,−1),(1,−√2,1) row by row. Normalize them, compute all pairwise dot products, and reject (1,1,1).

**C12-CAP-04 (12 points).** On the open product graph with lexicographic addresses (i,j,k) in {−1,0,1}³, construct U(i,j,k)=u−(i)u−(j)u0(k). Find its eigenvalue by adding factor eigenvalues. At (−1,−1,−1), compute its value, each neighbor value, and the neighbor sum. Explain why its norm is 1.

**C12-CAP-05 (18 points).** Derive the two-factor sum counts and use them to build the seven Emily multiplicities. Account for all 27 ordered modes (a complete ledger or exhaustive grouped rule is acceptable). Separately derive the 14-even/13-odd function count, the node-sheet populations for λ_sheet=i+j+k, and the 13-positive/14-negative χ count. Explain what each list counts.

**C12-CAP-06 (20 points).** For f=(2,0,0), calculate its (+,0,−) coefficients and reconstruct all entries. If only the zero-mode term is retained, give the full residual and show reconstruction. Separately calculate parity parts, mean and centered detail. Explain the retained 1+13+13 coordinate count on the Lucas graph. Calculate A_L **1** by node type and test whether removing the mean deletes one Emily eigenmode.

**C12-CAP-07 (14 points).** Let A_X=diag(1,2), B_Y=diag(2,1). Test the swap T(a,b)=(b,a) by calculating both B_Y T and T A_X, and exhibit its inverse. Reject the candidate T=I using one input. A proposal says “seven sheet populations are the seven Emily eigenvalue groups.” Name the missing structures needed for an operator-preserving identification. Explain why 13 antipodal pairs, 13 decoder channels and seven syndrome dimensions remain distinct objects.

## Backward map: every operation was practiced

| Step | Named input → output | Earlier explanation and worked example | Independently answered practice |
|---|---|---|---|
| 01 | Three node entries → three neighbor sums; A,D → typed inputs | C12.01-E1/W1 | C12.01-P1 both vectors and carrier question |
| 02 | S patterns and scaled path pattern → common multiplier checks | C12.02-E1/W1 | C12.02-P1; D1 zero input reasoning |
| 03 | Component equations → three eigenvalues, unit vectors and zero mutual dots | C12.03-E1/W1; C12-EIG-EX1 | C12.03-P1 derivation, normalization and dots; C12-EIG-P1/D1 |
| 04 | Three ordered factors → eigenvalue, corner value and three neighbor values | C12.04-E1/W1 | C12.04-P1 exact requested product and norm |
| 05 | Ordered choices → seven counts; reflection pairs → dimensions; sheets → χ counts | C12.05-E1/W1 | C12.05-P1 enumeration, split and independent counts |
| 06 | f → coefficients, residual, parity, mean/detail; node types → degree vector | C12.06-E1/W1 | C12.06-P1 all representations and degree table |
| 07 | A_X,B_Y,T → route equality or witness of failure; named carriers → missing map contract | C12.07-E1/W1 | C12.07-P1 identity failure, swap recovery and sheet comparison |

## Full answer key and point rubric

**01.** Rows give 0·2+1·(−1)+0·0=−1; 1·2+0·(−1)+1·0=2; 0·2+1·(−1)+0·0=−1, so (−1,2,−1). A takes node values; D takes directed-edge flows and gives node divergence. Award 2 per correct row and 2 for carrier distinction.

**02.** S(1,1)=(1,1)=1(1,1); S(1,−1)=(−1,1)=−1(1,−1). A(2,0,−2)=(0,2−2,0)=0·(2,0,−2). This is nonzero input with zero eigenvalue. Zero input satisfies every multiplier equation and is excluded by definition. Award 2 per swap pair, 3 for scaled path verification, 3 for zero distinction.

**03.** Equations are b=λa, a+c=λb, b=λc. If λ=0, b=0 and c=−a, with a≠0. If λ≠0, a=c and b=λa; a=0 would force zero input, so 2a=λ²a implies λ²=2. Thus λ=±√2. Row outputs of v+,v0,v− are (√2,2,√2),(0,0,0),(−√2,2,−√2), respectively; these equal √2v+,0v0,−√2v−. Norms are 2,√2,2, giving u+=v+/2,u0=v0/√2,u−=v−/2. Mutual dots are (1−2+1)/4=0, (1−1)/(2√2)=0, (1−1)/(2√2)=0. All norms become 1. A(1,1,1)=(1,2,1) demands inconsistent multipliers. Award 5 for the two-case derivation with valid divisions, 6 for three row verifications, 3 for norms/normalization, 3 for mutual dots, 1 for rejection.

**04.** Eigenvalue −√2−√2+0=−2√2. Corner value (1/2)(1/2)(1/√2)=1/(4√2). Neighbors (0,−1,−1),(−1,0,−1),(−1,−1,0) have values −1/4,−1/4,0. Sum −1/2 equals −2√2 times the corner value. Squared norm factors into the three squared norms, 1·1·1=1. Award 3 for ordered product and eigenvalue, 2 for corner, 3 for neighbors, 2 for eigen-equation check, 2 for norm explanation.

**05.** Two-factor sums −2..2 have counts 1,2,3,2,1. Adding adjacent earlier counts for the third choice gives 1,3,6,7,6,3,1 at m=−3..3, with eigenvalues m√2. Exhaustive groups: m=±3 has all equal signs; m=±2 has three placements of 0 among two equal signs; m=±1 has three placements of that sign among two zeros plus three placements of the opposite sign among two same signs; m=0 has 000 plus all six permutations of +0−. Sum 27. Functions have one even and one odd value per antipodal pair, plus an even center: 14 and 13. Node sheets use the same finite sum-counting on addresses, producing the same population list but a different carrier. χ is +1 on even sheet sums (3+7+3=13 nodes) and −1 on odd sheet sums (1+6+6+1=14). Award 3 for two-factor counts, 5 for full spectrum and exhaustive group accounting, 4 for function parity derivation, 3 for node sheets, 3 for χ and carrier distinction.

**06.** Coefficients are (1,√2,1). Contributions are (1/2,√2/2,1/2)+(1,0,−1)+(1/2,−√2/2,1/2)=(2,0,0), so full reconstruction residual is zero. Zero-mode-only retained part (1,0,−1) has residual (1,0,1); their sum is f. Parity e=(1,0,1), o=(1,0,−1), μ=2/3, d=(4/3,−2/3,−2/3). The mean plus detail and even plus odd each recover f. On 27 nodes the mean is one retained even coordinate, leaving 13 even and 13 odd centered coordinates, hence 1+13+13. A_L **1** has 8 entries 3, 12 entries 4, 6 entries 5, 1 entry 6. It is not constant; uniform mean removal does not delete an adjacency eigenmode or define the quotient adjacency. Award 4 for coefficients, 3 for complete reconstruction, 3 for retained residual, 4 for parity/mean/detail, 2 for 1+13+13, 4 for degree calculation and operator conclusion.

**07.** B_Y T(a,b)=(2b,a)=T A_X(a,b), so both matrices are [[0,2],[1,0]]. Swapping twice is the inverse. Identity fails on (1,0): B_Y I gives (2,0), I A_X gives (1,0). A sheet-to-mode identification needs explicit state carriers, both operators, and an invertible map satisfying their route equation. Counts alone provide none of these. Antipodal pairs are pairs of addresses; channels are decoder input coordinates; syndrome dimensions count retained decoder residual degrees of freedom. Their equal or nearby counts do not identify them. Award 5 for swap equality, 2 for inverse, 2 for identity counterexample, 3 for missing contract, 2 for typed counts.

**Evidence and residual accounting.** The ledger, source graph and parity statement refer to S02 /backbone_sequence/7; sheets to /backbone_sequence/2; decoder counts to /backbone_sequence/16. Source status remains distinct from the fresh finite derivations shown here. No measured physical effects or mechanism claims are assessed. All incomplete representations must retain the signed residual or mean needed to reconstruct their original inputs.
