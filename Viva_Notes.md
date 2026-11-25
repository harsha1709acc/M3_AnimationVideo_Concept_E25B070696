# Viva_Notes.md — Viva Preparation: Math Explanations & Code Walkthrough

Use this document to prepare for questions from your assessor about:
- The mathematics behind Gaussian elimination
- Why the algorithm is correct
- How specific parts of the Manim code work

---

## Part A — Mathematics

### A1. What is a system of linear equations?
A set of *m* equations in *n* unknowns where each unknown appears only to the first power (no x², no x·y terms). In matrix form: **Ax = b**, where **A** is the coefficient matrix, **x** is the unknown vector, and **b** is the right-hand side.

### A2. What is an augmented matrix?
The matrix `[A | b]` formed by appending the column **b** to **A**. It encodes the full information of the system in one object, making row operations easy to apply uniformly.

### A3. What are the three elementary row operations?
| Op | Notation | Effect |
|----|----------|--------|
| Swap | Rᵢ ↔ Rⱼ | Reorders two equations |
| Scale | Rᵢ → k·Rᵢ (k≠0) | Multiplies one equation by a constant |
| Replace | Rᵢ → Rᵢ + k·Rⱼ | Adds a multiple of one equation to another |

### A4. Why do row operations never change the solution set?
Each operation is **reversible**:
- Swap: apply the same swap again.
- Scale: divide by k.
- Replace: apply Rᵢ → Rᵢ − k·Rⱼ.

Because we can always undo every step, the original system and the transformed system have *exactly the same* solutions. Formally: each operation corresponds to multiplying on the left by an *elementary matrix* E with det(E) ≠ 0, so the system **EAx = Eb** is equivalent to **Ax = b**.

### A5. What is a pivot?
The **first non-zero entry** in a row of the matrix (after any zero rows have been pushed down). Pivots are used to eliminate all entries *below* them in the same column.

### A6. What is row-echelon form?
A matrix is in row-echelon form if:
1. All zero rows (if any) are at the bottom.
2. Each pivot is strictly to the **right** of the pivot in the row above it.

This creates the characteristic "staircase" pattern:
```
[■ * * | *]
[0 ■ * | *]
[0 0 ■ | *]
```

### A7. Walk through every arithmetic step of the worked example.
See [`Verification.md`](Verification.md) for the full derivation. Summary:

| Step | Operation | New row |
|------|-----------|---------|
| 1 | R₂ → R₂ − 2R₁ | [0, −1, 2 \| 4] |
| 2 | R₃ → R₃ − 3R₁ | [0, 1, −1 \| −1] |
| 3 | R₃ → R₃ + R₂  | [0, 0, 1 \| 3] |

Back-sub: z = 3, y = 2, x = 1.

### A8. What do the special cases mean?
- **Row of zeros `[0 0 0 | 0]`:** One equation was a linear combination of the others — it gives no new information. The system is *under-determined* → infinitely many solutions.
- **Contradictory row `[0 0 0 | c]` (c ≠ 0):** The equation says 0 = c, which is impossible. The system is *inconsistent* → no solution.

### A9. What is back-substitution and why do we start from the bottom?
Once in echelon form, the last row has only one unknown (z). We solve for z first, substitute it into the row above to get y, and so on up to x. We start from the bottom because the last row is the simplest equation.

### A10. How did you verify the solution?
Two independent methods:
1. **Exact fraction arithmetic** (`fractions.Fraction` in Python) — no rounding possible.
2. **NumPy** `np.linalg.solve` for floating-point cross-check with `np.allclose`.
Both confirmed (x, y, z) = (1, 2, 3).

---

## Part B — Code Walkthrough

### B1. How is the project structured?
One Python file per scene (`scene1_hook.py` … `scene6_summary.py`), each containing one Manim `Scene` class. Shared utilities live in `constants.py` (colours, font sizes) and `matrix_helpers.py` (the `AugmentedMatrixMob` class and `row_op_animation` function).

### B2. What is `AugmentedMatrixMob`?
A custom `VGroup` subclass defined in `matrix_helpers.py`. It:
- Accepts a 2-D list of string entries.
- Places each entry as a `MathTex` on a grid.
- Draws left and right brackets using `Line` objects.
- Draws a coloured vertical separator for the augmented part.
- Provides methods: `highlight_row(r, color)`, `reset_row_color(r)`, `get_cell(r, c)`.

### B3. What does `row_op_animation` do?
A function that animates a single row-replacement operation in four beats:
1. Colour the **source row** green.
2. Colour the **target row** blue and show the annotation label (e.g., `R₂ → R₂ − 2R₁`).
3. Transform the target row's `MathTex` entries to new values using Manim's `Transform`.
4. Reset colours and fade the annotation.

### B4. How is narration synchronised with animation?
The animation is rendered as a silent MP4 (`-an`) using fixed, hand-chosen `run_time` and `self.wait()` values paced at ~130 words per minute. The student records their own voice-over following [`Narration_Script.md`](Narration_Script.md), which lists exact timestamp ranges and visual cues for every paragraph.

### B5. How does `render_all.sh` work end-to-end?
```
verify_math.py        → assert solution (1,2,3) before anything renders
manim scene*.py ...   → Scene1Hook.mp4 … Scene6Summary.mp4 (1080p, 30fps)
ffmpeg concat (-an)   → STUDENTID_Video.mp4 (silent, no audio stream)
storyboard_gen.py     → Storyboard.pdf
ffprobe               → verify duration (4:45–5:15) & streams
```

### B6. Why are colour constants defined in a separate file?
So the entire video can be restyled by editing one file (`constants.py`). Every scene imports the same `PIVOT_COLOR`, `ROW_CHANGE_COLOR`, etc., so the colour coding is guaranteed to be consistent.

### B7. What Manim animation types are used?
| Manim class / method | Used for |
|---------------------|----------|
| `Write` | Text and equation appearances |
| `FadeIn` / `FadeOut` | Scene transitions |
| `Transform` | Morphing matrix entries during row ops |
| `Create` | Drawing lines, arrows, rectangles |
| `AnimationGroup` | Running multiple animations together |
| `Axes` / `plot` | 2D line graphs in Scene 3 |
| `Dot`, `Arrow`, `Line` | Geometric shapes |
| `SurroundingRectangle` | Pivot highlight boxes |
| `MathTex` | LaTeX-rendered mathematics |

### B8. What would you change if you had more time?
- Use Manim's `ThreeDScene` for a true 3D plane visualisation in Scene 3.
- Add interactive highlights where the viewer can pause and replay each step.
- Implement `manim-voiceover` for frame-accurate narration sync.
- Add a subtitle/caption track for accessibility.

---

*Keep this document handy during your viva. Practice explaining Sections A7 and B3 out loud.*
