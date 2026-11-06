# Lesson 4 — Plane normals and physical spacing

**Essential question:** How does a vector that counts plane levels determine the distance between planes?

**Goals:** Calculate a vector's magnitude and unit direction; derive consecutive-level spacing; explain how scaling or reversing a plane label changes its planes.

**Bridge:** Lesson 3 constructs g_h with g_h dot (x-O)=h dot q. Integer values m define parallel planes. We now need the physical distance between planes labeled m and m+1. All computation still uses the synthetic basis in LU, not the source's nm geometry.

## C04.04-E1 — Length, direction and projection

The magnitude of v=(v1,v2,v3), written |v|, is sqrt(v1²+v2²+v3²). The square root is the nonnegative number whose square is the input. Repeated use of the right-triangle length rule gives this formula for perpendicular physical axes. For nonzero v, divide each component by |v| to obtain a **unit vector**, of magnitude 1. Division changes length without changing direction.

For a nonzero reciprocal vector g, define n=g/|g|. Its components have no units because inverse length cancels inverse length. A displacement parallel to n is t n, where the signed number t has length units. Its projection on n is n dot (t n)=t because n dot n=1. More generally n dot d is the signed component of a displacement d along that direction. To see why this measures perpendicular separation, split d as (n dot d)n plus the remainder d-(n dot d)n. The remainder has dot product zero with n, so it lies along a level plane and adds no perpendicular displacement. For a given normal projection, adding a nonzero perpendicular-to-n remainder only increases the displacement's squared length.

A vector perpendicular to a plane is called a **normal**. Along a plane the level does not change: g dot d=0 for a displacement d within it. Therefore g, and also n, is normal to the level planes. Move by t n from one plane. The change of level is g dot (t n)=t|g|. To increase the level by exactly one, choose **t=1/|g|**. Hence consecutive integer-level spacing is **d_h=1/|g_h|**. Spacing is positive, while n carries orientation. Since |g| has inverse-length units, d_h has length units.

## C04.04-W1 — From counter to ruler

For h=(1,0,0), lesson 3 gives g=(1,-1/2,0) LU^-1. Its magnitude is sqrt(1+1/4)=sqrt(5)/2 LU^-1. Divide componentwise:

```text
n = (2,-1,0)/sqrt(5),       d_h = 2/sqrt(5) LU.
```

Check |n|²=4/5+1/5=1. The displacement to the next level is d_h n=(4/5,-2/5,0) LU. Its level increment is g dot (d_h n)=4/5+1/5=1. This checks the spacing using the original counter rather than merely repeating the magnitude calculation. The origin cancels when comparing two points, but stays explicit in each point's plane equation.

## C04.04-P1 — Two axis-aligned normals

Find g, n and spacing for h=(0,1,0) and h=(0,0,1). Verify that moving by the spacing along n increases the corresponding level by one.

**Worked answer:** The first gives g=(0,1/2,0) LU^-1, |g|=1/2 LU^-1, n=(0,1,0), spacing 2 LU. Its normal step (0,2,0) LU has dot product 1 with g. The second gives g=(0,0,-1/3) LU^-1, n=(0,0,-1), spacing 3 LU. Its step (0,0,-3) LU also raises the level by 1. A negative component in a normal is a direction, not a negative spacing.

> **Claim scope:** These are geometric derivations for nonzero h, with all integer levels m allowed. We do not impose a “primitive integer label” convention that would discard labels with a common factor. Replacing h by 2h inserts additional planes between the old integer levels. This differs from multiplying both sides of one plane equation by 2, which leaves that individual plane unchanged. Canonical Cell3 normal and spacing fields remain the source-reading values from lesson 3, with their separate nm units.

## Diagnostic checks

1. **C04.04-D1:** Replace h=(1,0,0) by (2,0,0). Find g, n and the consecutive-level spacing; explain which new planes appear.
2. Replace h=(1,0,0) by (-1,0,0). What happens to normal, spacing and the unlabeled set of planes?
3. What fails at h=0 in n=g/|g| and d_h=1/|g|?
4. For h=(0,1,0), find the physical plane with m=1. Is it x2=2 LU or x2=1 LU?

**Worked answers:** (1) g=(2,-1,0) LU^-1, |g|=sqrt(5) LU^-1, n=(2,-1,0)/sqrt(5), spacing 1/sqrt(5) LU. Odd new integer levels occur halfway between old planes because the new equation is 2q1=m. (2) g and n reverse, spacing stays 2/sqrt(5) LU; the plane set is the same with m labels reversed. (3) Both divide by zero; no unit direction or finite spacing exists. (4) (x2-(-1))/2=1 in LU components, so x2=1 LU. The origin shift matters.

**Pacing:** 20 minutes explanation/worked example, 15 practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** [Lesson 5](lesson-05.md) explains why lengths and angles must use the physical geometry rather than the appearance of addresses.
