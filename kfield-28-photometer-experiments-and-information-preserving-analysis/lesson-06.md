# 6. Scale and channel comparisons

Essential question: How can we change scale without losing information?

Goals:

- Reconstruct mean and detail on declared supports
- Compare channel views without removing signed structure
- Explain why phase must be retained

## Prerequisite bridge

Use [Sidereal combs and event windows](lesson-05.md): its retained records and operations are the inputs to this lesson.

Pacing: 2 period(s) of 55 minutes. Full mean/detail reconstruction / Changed support and retained spectral phases.

## C28.06-E1 — first principles

A mean is the sum divided by the number of included entries. It represents a constant component over that declared support. Let m be the mean and d_i=x_i-m the detail at position i. The reconstruction x_i=m+d_i is an exact identity. A negative detail means below the chosen mean, not a negative raw count. Detail is retained information, not waste.

For the full five-row A support, sum=2+5+8+1+3=19 and m=19/5. Subtract 19/5 from each value: d=(-9/5,6/5,21/5,-14/5,-4/5). Their sum is zero because -9+6+21-14-4=0. Reconstruct row 2 as 19/5+21/5=40/5=8. The raw row with failed normalization remains in this raw mean; the view is explicitly all five supplied raw values including the stipulated fault flag.

For support rows 1,2,3 only, the sum is 14 and mean 14/3. Details are (1/3,10/3,-11/3). A changed mean can come from changed support rather than a new physical process. Always report the keys, time range, masks and weighting rule beside a mean.

A scale view groups information over a chosen span. For example, pair values (2,5): their mean is 3.5 and details (-1.5,1.5). The coarser mean plus the two details restores the pair. If you average a window or smooth a sequence, preserve the removed field and the exact boundary rule. At edges our rule is no invented padding. If a partial-support mean is requested, declare its smaller support explicitly.

Frequency coefficients from lesson 4 are another representation. Phase is the position within a cycle, represented by the signs and real/imaginary coordinates of those coefficients. Magnitude measures size while losing that position. For example a=(1,0,0,0) gives F=(1,1,1,1), while b=(0,1,0,0) gives F=(1,-i,-1,i). Both have four magnitudes of 1, yet their nonzero samples occur at different positions. Keeping complex coefficients with the inverse factor recovers the difference.

Across channels, retain each channel's response identity, raw scale, normalized scale, common support and separate masks. Similar-looking curves may invite a proposed relationship, but the transformation record must still distinguish them. Descriptive scores can index interesting windows; they cannot replace the signed fields that produced them.

> Claim scope: Means and transforms are derived representations. Residuals remain primary coordinates; no size-based deletion is authorized.

## C28.06-W1 — worked example

The five raw A values sum 19, so mean 19/5 and detail (-9/5,6/5,21/5,-14/5,-4/5) reconstruct all five entries. Save the mean and full signed detail, including the row with invalid normalization.

## C28.06-P1 — guided practice

**Student task.** For raw window (5,8,1), compute the mean, all three signed details, and each reconstructed value. Compare its support with the full five-row example. State the complex-coefficient and inverse-factor information needed for a four-point DFT replay.

### Worked answer

For window (5,8,1), mean 14/3 and detail (1/3,10/3,-11/3) reconstruct the window. It is a different support from the five-row mean; do not compare the two means as though the input set were identical. A four-sample DFT retains complex phases and the declared inverse factor.

The reconstructed window is (14/3+1/3,14/3+10/3,14/3-11/3)=(5,8,1). Preserve rows 1,2,3 and their flags; full-record support is 0..4. Retain both complex coordinates, ordering, declared signs and inverse factor 1/4 for the four-point DFT.

## C28.06-D1 — diagnostic checks

1. Reconstruct row 3 from full mean/detail.
2. What is the sum of full details?
3. Why is 14/3 different from 19/5?
4. Do equal Fourier magnitudes imply equal sample positions?

## Worked answers

1. 19/5-14/5=1 count.
2. (-9+6+21-14-4)/5=0.
3. It is computed over rows 1,2,3 instead of all five. Its input support differs.
4. No. The two single-pulse examples have equal magnitudes and different complex coefficients; retain phase.

Next dependency: [lesson-07](lesson-07.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
