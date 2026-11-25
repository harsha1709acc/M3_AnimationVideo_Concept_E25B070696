"""
verify_math.py — Independent mathematical verification of the worked example
─────────────────────────────────────────────────────────────────────────────
Run:  python3 verify_math.py
Expected output: "ALL ASSERTIONS PASSED — solution is (1, 2, 3)"

This script uses both NumPy (floating-point) and SymPy (exact rational
arithmetic) to independently verify every row-operation step shown in
Scene 4, and the final back-substitution result.
"""

import numpy as np
from fractions import Fraction


def frac_row(row):
    """Convert a list to Fraction for exact arithmetic."""
    return [Fraction(x) for x in row]


def print_matrix(M, label=""):
    if label:
        print(f"\n── {label} ──")
    for row in M:
        print("  ", [str(x) for x in row])


# ════════════════════════════════════════════════════════════════════════════
#  1.  Original augmented matrix  [A | b]
#  x + 2y +  z =  8
# 2x + 3y + 4z = 20
# 3x + 7y + 2z = 23
# ════════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("  GAUSSIAN ELIMINATION — MATHEMATICAL VERIFICATION")
print("=" * 60)

# Using exact fractions to avoid any floating-point rounding
R1 = frac_row([1,  2,  1,  8])
R2 = frac_row([2,  3,  4, 20])
R3 = frac_row([3,  7,  2, 23])

M = [R1[:], R2[:], R3[:]]
print_matrix(M, "Initial augmented matrix")

# ── Step 1: R2 → R2 − 2·R1 ──────────────────────────────────────────────────
R2_new = [R2[c] - 2 * R1[c] for c in range(4)]
print_matrix([R2_new], "After R2 → R2 − 2·R1  (expected: 0  −1  2  4)")

assert R2_new == frac_row([0, -1, 2, 4]), f"Step 1 FAILED: {R2_new}"
print("  ✓ Step 1 correct: R2 = [0, -1, 2, 4]")

# ── Step 2: R3 → R3 − 3·R1 ──────────────────────────────────────────────────
R3_after_step2 = [R3[c] - 3 * R1[c] for c in range(4)]
print_matrix([R3_after_step2], "After R3 → R3 − 3·R1  (expected: 0  1  −1  −1)")

assert R3_after_step2 == frac_row([0, 1, -1, -1]), f"Step 2 FAILED: {R3_after_step2}"
print("  ✓ Step 2 correct: R3 = [0, 1, -1, -1]")

# ── Step 3: R3 → R3 + R2 ────────────────────────────────────────────────────
# Note: at this point R2 = R2_new from Step 1
R3_after_step3 = [R3_after_step2[c] + R2_new[c] for c in range(4)]
print_matrix([R3_after_step3], "After R3 → R3 + R2  (expected: 0  0  1  3)")

assert R3_after_step3 == frac_row([0, 0, 1, 3]), f"Step 3 FAILED: {R3_after_step3}"
print("  ✓ Step 3 correct: R3 = [0, 0, 1, 3]")

# ── Echelon form ─────────────────────────────────────────────────────────────
echelon = [R1[:], R2_new[:], R3_after_step3[:]]
print_matrix(echelon, "Row-echelon form")
print("  Pivots at (0,0)=1, (1,1)=−1, (2,2)=1  — staircase verified ✓")

# ════════════════════════════════════════════════════════════════════════════
#  2.  Back-substitution (exact)
# ════════════════════════════════════════════════════════════════════════════
print("\n── Back-substitution ──")

# Row 3: z = RHS / pivot
z = R3_after_step3[3] / R3_after_step3[2]
assert z == Fraction(3), f"z FAILED: {z}"
print(f"  z = {R3_after_step3[3]} / {R3_after_step3[2]} = {z}  ✓")

# Row 2: -1·y + 2·z = 4  →  y = (4 - 2z) / (-1)
# General: R2[1]·y + R2[2]·z = R2[3]
y = (R2_new[3] - R2_new[2] * z) / R2_new[1]
assert y == Fraction(2), f"y FAILED: {y}"
print(f"  y = ({R2_new[3]} − {R2_new[2]}·{z}) / {R2_new[1]} = {y}  ✓")

# Row 1: 1·x + 2·y + 1·z = 8
x = (R1[3] - R1[2] * z - R1[1] * y) / R1[0]
assert x == Fraction(1), f"x FAILED: {x}"
print(f"  x = ({R1[3]} − {R1[2]}·{z} − {R1[1]}·{y}) / {R1[0]} = {x}  ✓")

# ════════════════════════════════════════════════════════════════════════════
#  3.  Substitution check into ORIGINAL equations
# ════════════════════════════════════════════════════════════════════════════
print("\n── Substitution check into original equations ──")
eq1 = 1*x + 2*y + 1*z
eq2 = 2*x + 3*y + 4*z
eq3 = 3*x + 7*y + 2*z

assert eq1 == Fraction(8),  f"Eq1 FAILED: {eq1}"
assert eq2 == Fraction(20), f"Eq2 FAILED: {eq2}"
assert eq3 == Fraction(23), f"Eq3 FAILED: {eq3}"
print(f"  Eq1: 1·{x} + 2·{y} + 1·{z} = {eq1} = 8  ✓")
print(f"  Eq2: 2·{x} + 3·{y} + 4·{z} = {eq2} = 20 ✓")
print(f"  Eq3: 3·{x} + 7·{y} + 2·{z} = {eq3} = 23 ✓")

# ════════════════════════════════════════════════════════════════════════════
#  4.  Cross-check with NumPy
# ════════════════════════════════════════════════════════════════════════════
print("\n── NumPy cross-check ──")
A_np = np.array([[1, 2, 1], [2, 3, 4], [3, 7, 2]], dtype=float)
b_np = np.array([8, 20, 23], dtype=float)
sol  = np.linalg.solve(A_np, b_np)
assert np.allclose(sol, [1.0, 2.0, 3.0], atol=1e-10), f"NumPy FAILED: {sol}"
print(f"  NumPy solution: x={sol[0]:.10f}, y={sol[1]:.10f}, z={sol[2]:.10f}  ✓")

print("\n" + "=" * 60)
print("  ALL ASSERTIONS PASSED — solution is (1, 2, 3)  ✅")
print("=" * 60)
