# Narration_Script.md — Student Voice-Over Recording Script

**Target Video:** `STUDENTID_Video.mp4` (`4:51`, 1920×1080, 30 fps, silent)  
**Speaking Pace:** ~130 words per minute (natural, unhurried teaching pace)  
**How to Use:** Keep this script open next to your video player. Bracketed cues like `[R2 -> R2 - 2R1 appears]` tell you what appears on screen; `[PAUSE 2s]` tells you when to leave room for the animation.

---

## Scene 1 — Hook / Context (`0:00 – 0:37`)

**`0:00 – 0:08`**  
`[Title card: Gaussian Elimination, Name & Student ID]`  
Welcome! In this video, we are going to explore Gaussian Elimination — a clean, step-by-step method for solving systems of linear equations. `[PAUSE 1.5s]`

**`0:08 – 0:17`**  
`[Central question appears in box]`  
Here is the big question: how do we solve three equations in three unknowns systematically, the exact way a computer does? `[PAUSE 2s]`

**`0:17 – 0:28`**  
`[Three equations appear one by one]`  
Look at this three-by-three system: x plus 2y plus z equals 8; 2x plus 3y plus 4z equals 20; and 3x plus 7y plus 2z equals 23. All three unknowns are tangled together. `[PAUSE 1s]`

**`0:28 – 0:37`**  
`[Staircase blocks & target answer appear]`  
Our plan is to reshape this system into a neat staircase, and then read off the answer from the bottom up: x equals 1, y equals 2, and z equals 3. `[PAUSE 1s]`

---

## Scene 2 — Concept Introduction (`0:37 – 1:19`)

**`0:37 – 0:45`**  
`[Key Definitions: Linear System]`  
First, let us define our terms. In a linear system, every unknown appears only to the first power — no squares, and no products like x times y. `[PAUSE 1s]`

**`0:45 – 0:55`**  
`[Augmented Matrix [A | b] built, braces for A and b]`  
We pack all coefficients into matrix A, and the right-hand constants into vector b. Placing them side by side gives the augmented matrix, written A bar b. `[PAUSE 1s]`

**`0:55 – 1:07`**  
`[Op 1: Swap, Op 2: Scale, Op 3: Replace appear]`  
Gaussian elimination uses three elementary row operations: swap two rows, scale a row by a non-zero number, or replace row i with row i plus a multiple of row j. `[PAUSE 1s]`

**`1:07 – 1:13`**  
`[Pivot & Row-Echelon Form definitions]`  
A pivot is the first non-zero entry in a row. In row-echelon form, each pivot steps strictly to the right of the one above it.

**`1:13 – 1:19`**  
`[Learning Objective box]`  
By the end of this video, you will be able to explain how Gaussian elimination reaches echelon form, solves by back-substitution, and why row operations never change the solution.

---

## Scene 3 — Visual Intuition (`1:19 – 2:12`)

**`1:19 – 1:30`**  
`[Title, then 2D axes with two lines meeting at (1, 2)]`  
Why are row operations safe? Let us start in two dimensions. Here are two lines, x plus y equals 3 and x minus y equals negative 1, meeting at the solution (1, 2). `[PAUSE 1s]`

**`1:30 – 1:41`**  
`[R2 -> R2 - R1 annotation; blue line rotates to y = 2]`  
Now watch what happens when we replace row 2 with row 2 minus row 1. The blue line rotates to y equals 2, `[dot pulses]` but the intersection point (1, 2) stays completely fixed! `[PAUSE 1s]`

**`1:41 – 1:49`**  
`[Reversibility box appears]`  
Why? Because every row operation is reversible — we can always undo it with row 2 plus row 1, so the solution set never changes. `[PAUSE 1s]`

**`1:49 – 1:58`**  
`[Three 3D planes appear meeting at (1, 2, 3)]`  
In three dimensions, each equation is a plane, and all three planes meet at the single point (1, 2, 3). `[PAUSE 1s]`

**`1:58 – 2:12`**  
`[Plane 2 tilts on R2 -> R2 - 2R1, then Plane 3 tilts on R3 -> R3 - 3R1]`  
When we apply row operations, Plane 2 tilts, and Plane 3 tilts into a flat horizontal plane z equals 3 — `[dot circumscribed]` yet all three planes still intersect at (1, 2, 3). `[PAUSE 1s]`

---

## Scene 4 — Worked Example (`2:12 – 3:54`)

**`2:12 – 2:29`**  
`[System converts to augmented matrix; Pivot 1 = 1 highlighted in gold]`  
Now let us solve our system step by step. We write the three equations as an augmented matrix. In Step 0, our first pivot is the 1 in row 1, column 1, highlighted in gold. `[PAUSE 1.5s]`

**`2:29 – 2:50`**  
`[Target 2 boxed; R2 -> R2 - 2R1 calculation shown; Row 2 updates to [0, -1, 2 | 4]]`  
Step 1: we want to eliminate the 2 below the first pivot. `[R2 -> R2 - 2R1 appears]` We replace row 2 with row 2 minus 2 times row 1. Computing entry by entry: 2 minus 2 is 0; 3 minus 4 is negative 1; 4 minus 2 is 2; and 20 minus 16 is 4. `[Row 2 updates]` Row 2 becomes 0, negative 1, 2, bar 4. `[PAUSE 1.5s]`

**`2:50 – 3:12`**  
`[Target 3 boxed; R3 -> R3 - 3R1 calculation shown; Row 3 updates to [0, 1, -1 | -1]; Pivot 2 = -1]`  
Step 2: eliminate the 3 in row 3, column 1. `[R3 -> R3 - 3R1 appears]` We compute row 3 minus 3 times row 1: 3 minus 3 is 0; 7 minus 6 is 1; 2 minus 3 is negative 1; 23 minus 24 is negative 1. `[Row 3 updates]` Column 1 is now clean, and our second pivot is negative 1 in row 2. `[PAUSE 1s]`

**`3:12 – 3:32`**  
`[R3 -> R3 + R2 calculation shown; Row 3 updates to [0, 0, 1 | 3]; all 3 pivots & staircase]`  
Step 3: eliminate below the second pivot. `[R3 -> R3 + R2 appears]` Since row 3 has 1 and row 2 has negative 1, we simply add row 2 to row 3, giving 0, 0, 1, bar 3. `[Staircase arrows appear]` All three pivots — 1, negative 1, and 1 — form a staircase. We are in row-echelon form! `[PAUSE 1.5s]`

**`3:32 – 3:54`**  
`[Matrix slides left; Back-Substitution: z=3, y=2, x=1, boxed (1,2,3)]`  
Now we back-substitute from the bottom up. `[Row 3 boxed]` Row 3 gives 1z equals 3, so z equals 3. `[Row 2 boxed]` Substituting z equals 3 into row 2 gives negative y plus 6 equals 4, so y equals 2. `[Row 1 boxed]` Finally, row 1 gives x plus 4 plus 3 equals 8, so x equals 1. `[Boxed (1, 2, 3)]` Our solution is (1, 2, 3). `[PAUSE 1s]`

---

## Scene 5 — Interpretation (`3:54 – 4:26`)

**`3:54 – 4:10`**  
`[Substitution checks Eq 1, Eq 2, Eq 3 with green checkmarks]`  
Let us verify (1, 2, 3) in the original equations. Equation 1: 1 plus 4 plus 3 equals 8. Check. Equation 2: 2 plus 6 plus 12 equals 20. Check. Equation 3: 3 plus 14 plus 6 equals 23. Check. `[PAUSE 1.5s]`

**`4:10 – 4:26`**  
`[Two special-case matrices appear]`  
Finally, two special cases in echelon form. If a row of all zeros appears, `[0 0 0 | 0]` there are infinitely many solutions because one equation is redundant. But if you get `[0 0 0 | 5]`, zero cannot equal five — the system is inconsistent and has no solution. `[PAUSE 1s]`

---

## Scene 6 — Summary & Credits (`4:26 – 4:51`)

**`4:26 – 4:39`**  
`[Three Key Takeaways cards appear one by one]`  
To wrap up, remember three things: one, row operations are reversible, so they preserve the solution set; two, eliminate below each pivot to reach echelon form; three, back-substitute from the bottom up. `[PAUSE 1s]`

**`4:39 – 4:51`**  
`[References, then AI Disclosure & Student Name/ID]`  
Our references are Strang, Anton, and Lay. Thank you for watching! `[PAUSE 2s until fade out]`
