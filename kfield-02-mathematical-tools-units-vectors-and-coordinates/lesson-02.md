# Lesson 02 — Ratios, powers, and scale

**Essential question:** Why does doubling every edge multiply volume by eight?

**Goals:** Calculate a dimensionless scale ratio; derive length, area, and volume scale factors; distinguish changing a physical size from changing its unit.

**Prerequisite bridge.** Lesson 01 taught unit cancellation and powers of ten. Here repeated multiplication explains why the power of a unit matters. A ratio compares two quantities by division; convert them to the same unit before dividing.

## Build the idea

Let s = new length / old length for corresponding edges of two similar shapes. Similar means the shapes have the same angles and all corresponding lengths share one positive scale factor. Equal length units cancel, so s has no unit. For a rectangle with side lengths l and w, area A = lw counts how many unit squares cover it. Scaling both lengths gives A_new = (sl)(sw) = s²A_old. For a rectangular box, V = lwh counts unit cubes; scaling all three lengths gives V_new = s³V_old. The factors are s, s², s³ for length, area, volume.

This reasoning also explains squared and cubed unit conversions. Since 1 cm = 0.01 m, one square centimetre is (0.01 m)(0.01 m) = 0.0001 m². One cubic centimetre is 0.000001 m³. Changing units leaves the object unchanged. Enlarging an object changes its physical lengths. A drawing scale compares the represented length and the drawing length; its direction must be stated.

For s = 1/2, length halves, area becomes one quarter, and volume one eighth. For different horizontal and vertical factors, there is no single uniform s: a rectangle stretched by 2 horizontally and 3 vertically gains an area factor 6. The square rule requires the same factor in both directions. We use positive size ratios here; orientation signs will have a separate role in Lesson 06.

## Fully worked synthetic example

A model box measures 2 cm by 3 cm by 4 cm. A uniformly enlarged version has first edge 6 cm. The corresponding-length ratio is s = 6/2 = 3, so its edges are 6, 9, and 12 cm.

The 2-by-3 face originally has area 6 cm². Its new area is 54 cm², calculated directly as 6 × 9 or as 3² × 6. Original volume is 2 × 3 × 4 = 24 cm³. New volume is 6 × 9 × 12 = 648 cm³, also 3³ × 24. In metres the original volume is 0.02 × 0.03 × 0.04 = 0.000024 m³; multiplying 24 cm³ by 10^-6 m³/cm³ agrees. Each route preserves dimensions.

> **Claim scope:** This is an exact synthetic geometric enlargement. The volume rule alone does not establish a mass, energy, or biological scaling law. Such a law would need its own relationship and inputs. Nothing is rounded in this example.

## Guided practice

A 10 mm square becomes a 5 mm square. First find s = 5/10 = 1/2. Its area changes from 100 mm² to 25 mm², so the area ratio is 1/4. Express 25 mm² in cm²: each millimetre is 0.1 cm, giving 25 × (0.1)² = 0.25 cm². Check with a 0.5 cm side: 0.5² = 0.25.

## Diagnostic checks

1. A cube's edge grows from 2 m to 8 m. Find the length, face-area, and volume ratios.
2. Convert 9 cm² to m² and 9 cm³ to m³.
3. A 3-by-4 cm rectangle is stretched only horizontally by 2. Find the new area and explain why multiplying by 2² would be wrong.
4. On a drawing, 2 cm represents 5 m. State the represented-to-drawn ratio with matching units, and find the represented length of a 6 cm line.

## Worked answers

1. s = 8/2 = 4. The ratios are 4, 16, and 64; cube volumes 512/8 confirm 64.
2. 9 × (0.01)² = 0.0009 m²; 9 × (0.01)³ = 0.000009 m³. The numerical factors differ because the dimensions differ.
3. New dimensions are 6 by 4 cm, area 24 cm² rather than 12 cm². Only one factor of 2 enters the product.
4. 5 m = 500 cm, so represented/drawn = 500/2 = 250. The 6 cm line represents 1500 cm = 15 m.

**Next dependency:** [Lesson 03](lesson-03.md) applies scale factors to directed coordinate differences while separating an object’s location from its displacement.
