# Publication appendix — Complete signed numerical residuals

This appendix reproduces the existing course verification record as teaching support for [Lesson 6](lesson-06.md) and the [locked geometry card](geometry-card.md). These are declared numerical witnesses from stored source strings, not measured physical discrepancies or replacement canonical constants.

Input: verification.json. SHA-256: `4099a1d5f2155ee592f2342f373ee44b8320edc372fc1650f35d8afa14ae471f`. Arithmetic: Decimal, 60 significant digits, ROUND_HALF_EVEN; original source decimal lexemes. Matrix indices below are one-based; JSON pointer indices are zero-based. No signed entry or stored zero exponent is removed.

## BTB_minus_M

Field path: `/locked/BTB_minus_M/values`. Units: nm^2. Rows and columns retain the stored order. For BTB_minus_M, MR_minus_I and R_minus_RT the index order is the direct basis a,b,c; for BRBT_minus_I it is external ICRS x,y,z; BTD_minus_I pairs direct a,b,c rows with reciprocal-column 1,2,3.

| Row | Column | Exact signed value |
|---:|---:|---|
| 1 | 1 | 9.30649226836333E-18 |
| 1 | 2 | -1.0154757939229E-19 |
| 1 | 3 | -5.09519014998468E-18 |
| 2 | 1 | -1.0154757939229E-19 |
| 2 | 2 | 1.057181073319941E-17 |
| 2 | 3 | 3.426837967228082E-17 |
| 3 | 1 | -5.09519014998468E-18 |
| 3 | 2 | 3.426837967228082E-17 |
| 3 | 3 | 3.787694119310721E-17 |

Retained descriptive maximum: 3.787694119310721E-17. It does not replace the component field.

## MR_minus_I

Field path: `/locked/MR_minus_I/values`. Units: dimensionless. Rows and columns retain the stored order. For BTB_minus_M, MR_minus_I and R_minus_RT the index order is the direct basis a,b,c; for BRBT_minus_I it is external ICRS x,y,z; BTD_minus_I pairs direct a,b,c rows with reciprocal-column 1,2,3.

| Row | Column | Exact signed value |
|---:|---:|---|
| 1 | 1 | -1.534125197463488547162E-16 |
| 1 | 2 | 5.218432919786523272E-18 |
| 1 | 3 | -4.5553689366627803E-18 |
| 2 | 1 | -2.5021350432778140562E-17 |
| 2 | 2 | -8.22896404263617743512E-17 |
| 2 | 3 | -2.87569369100098266E-17 |
| 3 | 1 | -9.0029078557079269544E-17 |
| 3 | 2 | -5.05013300893256779056E-17 |
| 3 | 3 | -8.21682910752285088E-17 |

Retained descriptive maximum: 1.534125197463488547162E-16. It does not replace the component field.

## BRBT_minus_I

Field path: `/locked/BRBT_minus_I/values`. Units: dimensionless. Rows and columns retain the stored order. For BTB_minus_M, MR_minus_I and R_minus_RT the index order is the direct basis a,b,c; for BRBT_minus_I it is external ICRS x,y,z; BTD_minus_I pairs direct a,b,c rows with reciprocal-column 1,2,3.

| Row | Column | Exact signed value |
|---:|---:|---|
| 1 | 1 | -4.8782447525374342745385434860406928E-17 |
| 1 | 2 | 3.0855687040983062970974986306057088E-17 |
| 1 | 3 | 2.8370079953211376157067944971446632E-17 |
| 2 | 1 | 4.4026074942260924047256685338777288E-17 |
| 2 | 2 | -1.27933821487840002223637245284114336E-16 |
| 2 | 3 | 2.1222898048955172409280955379559068E-17 |
| 3 | 1 | 5.0107189414464437413153178524691132E-17 |
| 3 | 2 | 1.9086792211601854196956631418629368E-17 |
| 3 | 3 | -5.2273783301254831122066910179664458E-17 |

Retained descriptive maximum: 1.27933821487840002223637245284114336E-16. It does not replace the component field.

## BTD_minus_I

Field path: `/locked/BTD_minus_I/values`. Units: dimensionless. Rows and columns retain the stored order. For BTB_minus_M, MR_minus_I and R_minus_RT the index order is the direct basis a,b,c; for BRBT_minus_I it is external ICRS x,y,z; BTD_minus_I pairs direct a,b,c rows with reciprocal-column 1,2,3.

| Row | Column | Exact signed value |
|---:|---:|---|
| 1 | 1 | 3.6663842409835958E-17 |
| 1 | 2 | 8.759625123209188E-18 |
| 1 | 3 | -5.11516360354655E-18 |
| 2 | 1 | -3.580990292436548E-18 |
| 2 | 2 | 1.45238410899853532E-16 |
| 2 | 3 | 4.032097223369717E-17 |
| 3 | 1 | -9.608419268059783E-18 |
| 3 | 2 | 1.54182146686478486E-16 |
| 3 | 3 | -1.1059284009791404E-16 |

Retained descriptive maximum: 1.54182146686478486E-16. It does not replace the component field.

## R_minus_RT

Field path: `/locked/R_minus_RT/values`. Units: nm^-2. Rows and columns retain the stored order. For BTB_minus_M, MR_minus_I and R_minus_RT the index order is the direct basis a,b,c; for BRBT_minus_I it is external ICRS x,y,z; BTD_minus_I pairs direct a,b,c rows with reciprocal-column 1,2,3.

| Row | Column | Exact signed value |
|---:|---:|---|
| 1 | 1 | 0E-14 |
| 1 | 2 | -5.0E-18 |
| 1 | 3 | 1E-16 |
| 2 | 1 | 5.0E-18 |
| 2 | 2 | 0E-15 |
| 2 | 3 | 0E-16 |
| 3 | 1 | -1E-16 |
| 3 | 2 | 0E-16 |
| 3 | 3 | 0E-16 |

Retained descriptive maximum: 1E-16. It does not replace the component field.

## Scalar and face records

All paths are within `/locked/`. Face arrays retain ab, ac, bc order.

### determinant_recomputed

-0.117914891911744626838502803509518931924895262922

### determinant_minus_source

2.3161497196490481068075104737078E-17

### determinant_units

nm^3

### areas_recomputed

- Entry 0: 0.194869165460484129246116221095176469021942244501339451774823
- Entry 1: 0.261106235790205305694137408886183450213165586271636992193759
- Entry 2: 0.357809539128561557875583822049302411590256785788469168187098

### areas_minus_source

- Entry 0: -7.53883778904823530978057755498660548225177E-19
- Entry 1: 5.694137408886183450213165586271636992193759E-18
- Entry 2: 5.7875583822049302411590256785788469168187098E-17

### area_order

- Entry 0: ab
- Entry 1: ac
- Entry 2: bc

### area_units

nm^2

### source_reported_closure_scalar

2.8939781400741195E-16

### source_reported_closure_status

Reported scalar; source arithmetic not freshly reproduced; not substituted for any new residual matrix

## Reconstruction and provenance

- B^T B = M_stored + BTB_minus_M
- M_stored R_stored = I + MR_minus_I
- B R_stored B^T = I + BRBT_minus_I
- B^T D_stored = I + BTD_minus_I
- det_recomputed = det_source + determinant_minus_source
- areas_recomputed = areas_source + areas_minus_source

R_minus_RT retains the stored inverse-metric antisymmetry directly. See [sources.md](sources.md) for exact archival paths, fingerprints and active-branch pointers. This appendix transcribes the completed verification record; it does not claim a fresh archive calculation.
