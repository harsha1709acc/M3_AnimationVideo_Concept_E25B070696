# Verification.md — Step-by-Step Mathematical Verification

This document independently re-derives every calculation shown in Scene 4 of the animation,
using exact arithmetic (fractions), and then verifies the solution by substitution into the
original system.

---

## The System

$$
\begin{cases}
x + 2y + z = 8 \\
2x + 3y + 4z = 20 \\
3x + 7y + 2z = 23
\end{cases}
$$

---

## Augmented Matrix

$$
[A \mid b] =
\begin{bmatrix}
1 & 2 & 1 & \big| & 8 \\
2 & 3 & 4 & \big| & 20 \\
3 & 7 & 2 & \big| & 23
\end{bmatrix}
$$

The **pivot** in column 1 is the entry **1** in Row 1.

---

## Step 1 — R₂ → R₂ − 2R₁

Eliminate the leading 2 in Row 2 by subtracting **2 × Row 1**:

| Column | Calculation | Result |
|--------|------------|--------|
| c₁ | 2 − 2(1) | **0** |
| c₂ | 3 − 2(2) | **−1** |
| c₃ | 4 − 2(1) | **2** |
| b  | 20 − 2(8) | **4** |

New Row 2: `[0, −1, 2 | 4]` ✓

---

## Step 2 — R₃ → R₃ − 3R₁

Eliminate the leading 3 in Row 3 by subtracting **3 × Row 1**:

| Column | Calculation | Result |
|--------|------------|--------|
| c₁ | 3 − 3(1) | **0** |
| c₂ | 7 − 3(2) | **1** |
| c₃ | 2 − 3(1) | **−1** |
| b  | 23 − 3(8) | **−1** |

New Row 3: `[0, 1, −1 | −1]` ✓

Matrix after Steps 1 & 2:

$$
\begin{bmatrix}
1 & 2 & 1 & \big| & 8 \\
0 & -1 & 2 & \big| & 4 \\
0 & 1 & -1 & \big| & -1
\end{bmatrix}
$$

The **pivot** in column 2 is **−1** in Row 2.

---

## Step 3 — R₃ → R₃ + R₂

Eliminate the 1 in Row 3, column 2, by **adding Row 2**:

| Column | Calculation | Result |
|--------|------------|--------|
| c₁ | 0 + 0 | **0** |
| c₂ | 1 + (−1) | **0** |
| c₃ | −1 + 2 | **1** |
| b  | −1 + 4 | **3** |

New Row 3: `[0, 0, 1 | 3]` ✓

---

## Row-Echelon Form

$$
\begin{bmatrix}
\mathbf{1} & 2 & 1 & \big| & 8 \\
0 & \mathbf{-1} & 2 & \big| & 4 \\
0 & 0 & \mathbf{1} & \big| & 3
\end{bmatrix}
$$

**Pivots** (bold): 1, −1, 1 — staircase structure confirmed ✓

---

## Back-Substitution

**Row 3** → `1·z = 3`

$$z = \frac{3}{1} = \boxed{3}$$

**Row 2** → `-1·y + 2z = 4`

$$-y + 2(3) = 4 \implies -y = 4 - 6 = -2 \implies y = \boxed{2}$$

**Row 1** → `x + 2y + z = 8`

$$x + 2(2) + 3 = 8 \implies x + 7 = 8 \implies x = \boxed{1}$$

---

## Solution

$$\boxed{(x,\, y,\, z) = (1,\, 2,\, 3)}$$

---

## Substitution Check into Original Equations

| Equation | Substitution | Result | Expected | ✓ |
|----------|-------------|--------|----------|---|
| x + 2y + z = 8 | 1 + 2(2) + 3 = 1 + 4 + 3 | **8** | 8 | ✓ |
| 2x + 3y + 4z = 20 | 2(1) + 3(2) + 4(3) = 2 + 6 + 12 | **20** | 20 | ✓ |
| 3x + 7y + 2z = 23 | 3(1) + 7(2) + 2(3) = 3 + 14 + 6 | **23** | 23 | ✓ |

All three original equations are satisfied. The solution **(1, 2, 3)** is verified correct.

---

## Why Row Operations Preserve the Solution

Each elementary row operation falls into one of three types:

1. **Swap R_i ↔ R_j**: The same set of equations, just reordered. Same solution set.
2. **Scale R_i → k·R_i (k ≠ 0)**: Multiplying both sides of an equation by a non-zero constant produces an equivalent equation.
3. **Replace R_i → R_i + k·R_j**: Adding k times Equation j to Equation i. Any (x,y,z) satisfying both original equations also satisfies the new equation. The operation is reversible: R_i → R_i − k·R_j undoes it.

Since every operation is **reversible**, the new system has **exactly the same solution set** as the original. This is the mathematical guarantee that Gaussian Elimination is correct.

---

*Verified independently using `verify_math.py` (NumPy + exact Fraction arithmetic).*
