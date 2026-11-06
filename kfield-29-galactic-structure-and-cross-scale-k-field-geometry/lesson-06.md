# Recursive occupancy and retained residuals

Essential question: How can a count summary preserve sparse structure and reconstruction?

Goals: Enumerate the 27 local states and seven sheets; track parent-child counts and identities; compute distinct vector, angular and radial residuals.

Prerequisite bridge. Lessons 03–05 taught addresses, sheets, centers and metric distances. Now counts summarize assignments, while a parallel identity-and-residual ledger keeps the information needed to reconstruct individual observations. Use one period for states and one for multilevel residual accounting.

## C29.06-E1 — Availability is not occupancy

Let each local label i,j,k take -1,0,1. There are three choices independently for each coordinate, so 3·3·3=27 **available** labels. In the half-step window, the position is A(i,j,k)/2, or O_K+B(i,j,k)/2 for Cell3. The sheet label is lambda=i+j+k. Its possible values are -3,-2,-1,0,1,2,3.

**Occupancy** counts how many observed objects are assigned to each state. It needs an assignment rule and actual observations. A geometric count of available states does not determine their observed occupancy. Nor does a list of seven sheet totals uniquely determine the 27 state counts: several states share a sheet. Keep the full state vector or its immutable source reference in addition to the sheet summary.

## C29.06-W1 — Enumerating a complete window

For lambda=-3 there is only (-1,-1,-1). For -2 there are three permutations of (-1,-1,0). For -1 there are three permutations of (-1,0,0) and three of (-1,-1,1), giving six. For 0 there are (0,0,0) and six permutations of (-1,0,1), giving seven. Changing all signs supplies the positive sheets. The complete table is:

| Sheet | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| Available states | 1 | 3 | 6 | 7 | 6 | 3 | 1 |

The sum is 27. By a different classification there is one body center, six face centers, twelve edge centers and eight corners, again totaling 27. Zero nonzero components means body center; one means face center; two means edge center; three means corner. All labels remain available, including unoccupied ones.

For a small synthetic hierarchy, parent P contains objects a,b,c,d. At depth one, P-left has {a}, P-middle has {b,c}, P-right has {d}. Counts (1,2,1) total four. At depth two, divide P-middle into M-left={b}, M-right={c}. Save the path P/Middle/Left for b and P/Middle/Right for c. The middle count reconstructs as 1+1=2, and the parent as 1+(1+1)+1=4. A table of totals alone cannot recover object identity; retaining membership makes the view reversible.

This toy mixed three-child/two-child tree demonstrates accounting, not a source recursion. The Cell3 dyadic spatial refinement and ternary address recursion are separately typed (S02#/backbone_sequence M03). A dyadic split halves each of three directions, producing eight spatial children; three choices per address coordinate produce 27 address children. “Depth two” is ambiguous unless the recursion is named. Do not equate those systems with our toy tree or with detector parity.

## C29.06-P1 — Guided practice and answer

An independent toy parent has objects e,f,g,h and child memberships {},{e,f,g},{h}, giving (0,3,1). It too totals four. Subtract discovery (1,2,1) componentwise to get (-1,1,0). The zero first occupancy and the zero third difference carry different information; both remain in the ledger.

Now let a synthetic observed unit direction be x=(1,0,0) and candidate center c=(4/5,0,0). The **vector residual** r=x-c=(1/5,0,0). Its Euclidean length is 1/5. The **angular miss** is arccos((x·c)/(||x||||c||))=arccos(1)=0°. The **radial mismatch**, defined here as ||c||-1, is -1/5. These are reconstruction-coordinate quantities. Zero angular miss does not mean zero vector residual: x=c+r still needs r. A radial mismatch from the unit shell is not the galaxy's physical radial distance.

At c=0 the vector residual x still exists and radial mismatch is -1, but angular miss is undefined because a zero vector has no direction. Store null with a `zero_center_direction` flag. Do not delete the observation or substitute a zero angle.

> Source scope. G01#/galaxy_cell_geometry gives the same combinatorial sheet populations; /observed_27_node_occupancy reports observational summaries separately. G04 p4 retains vector, Euclidean, angular and radial residual channels. The small memberships above are synthetic, not copied catalog rows. Source rows and unexported state arrays stay in place and are referenced by provenance.

## Diagnostics — C29.06-D1

1. How many labels lie on lambda=0, and why?
2. Does a zero observed count remove a possible state?
3. Which fields reconstruct x from a center assignment?
4. For x=e_x and c=0, list the available residuals and the undefined one.

Worked answers. 1. Seven: the origin plus the six orders of (-1,0,1). 2. No: retain its label and zero count. 3. Keep c or its address+basis+phase, and the full signed r; then x=c+r. Membership and source identity must also survive. 4. r=e_x, length 1, radial mismatch -1; angular miss is null with the zero-center flag.

Next: [lesson 07](lesson-07.md) freezes assignments before comparing independent populations.
