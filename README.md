# README.md — M3 Gaussian Elimination Animation Video

## Project: Gaussian Elimination — Animation Video
**Course:** Linear Algebra and Calculus (M3), Internal Assessment, Option 1  
**Student:** Harshavardhan Rambha · E25B070696

---

## Learning Objective
> By the end of this video, the viewer will be able to explain how Gaussian elimination turns a 3×3 linear system into echelon form and solves it by back-substitution, and why the row operations never change the solution.

---

## Concept
**Gaussian Elimination** is a systematic algorithm for solving systems of linear equations. It transforms the augmented matrix `[A | b]` into row-echelon form using three elementary row operations (swap, scale, replace), then recovers the solution by back-substitution from the bottom row upward.

**Key idea:** Every elementary row operation is *reversible*, so the solution set is preserved at every step.

**Worked example:**
```
x + 2y +  z =  8
2x + 3y + 4z = 20
3x + 7y + 2z = 23      →  solution: (x, y, z) = (1, 2, 3)
```

---

## File Structure
```
M3_AnimationVideo_GaussianElimination_E25B070696/
│
├── E25B070696_Video.mp4           ← Final rendered video (1920×1080, 30fps, synced voiceover)
├── Narration_Script.md            ← Timestamped narration script (~130 wpm) for student voice-over
├── Storyboard.pdf                 ← 6-scene storyboard table
├── README.md                      ← This file
├── Verification.md                ← Step-by-step math check
├── Viva_Notes.md                  ← Viva preparation notes
├── render_all.sh                  ← Full render, concat & voiceover sync pipeline
│
└── E25B070696_Code/
    ├── requirements.txt           ← Python dependencies
    ├── constants.py               ← Colour constants & shared config
    ├── matrix_helpers.py          ← Reusable matrix & row-op animation helpers
    ├── verify_math.py             ← NumPy/exact-fraction math verification
    ├── storyboard_gen.py          ← fpdf2 PDF storyboard generator
    ├── voiceover.mp3              ← Student-recorded voice-over narration
    ├── scene1_hook.py             ← Scene 1: Hook / Context
    ├── scene2_concepts.py         ← Scene 2: Concept Introduction
    ├── scene3_intuition.py        ← Scene 3: Visual Intuition
    ├── scene4_example.py          ← Scene 4: Worked Example
    ├── scene5_interpret.py        ← Scene 5: Interpretation
    └── scene6_summary.py          ← Scene 6: Summary & Credits
```

---

## Requirements & Installation

### System requirements
- macOS / Linux
- Python 3.9+
- [Homebrew](https://brew.sh) (macOS) for system libraries

### Step 1 — Install system dependencies
```bash
brew install ffmpeg cairo pkg-config
```

> **LaTeX for math rendering:** Manim uses LaTeX for `MathTex` objects.
> Install BasicTeX (lightweight, ~100 MB):
> ```bash
> brew install --cask basictex
> sudo tlmgr update --self
> sudo tlmgr install standalone preview doublestroke relsize rsfs
> ```
> After install, restart your terminal.

### Step 2 — Install Python packages
```bash
cd STUDENTID_Code
pip3 install -r requirements.txt
```

### Step 3 — Verify the mathematics
```bash
python3 STUDENTID_Code/verify_math.py
```
Expected output: `ALL ASSERTIONS PASSED — solution is (1, 2, 3)`

---

## How to Render

### Draft (fast, 720p — for preview)
```bash
chmod +x render_all.sh
./render_all.sh --draft
```

### Final (1080p, 30fps, silent — for submission)
```bash
./render_all.sh
```

The script will:
1. Verify all mathematics with exact fractions & NumPy assertions
2. Render all 6 Manim scenes at 1080p 30fps
3. Concatenate scenes into `STUDENTID_Video.mp4` with `-an` (no audio stream)
4. Generate `Storyboard.pdf`
5. Verify stream info and total duration with `ffprobe` (target 4:45–5:15)

### Render a single scene manually
```bash
cd STUDENTID_Code
manim scene4_example.py Scene4Example -qh --fps 30
```

---

## Colour Coding
| Colour | Role |
|--------|------|
| 🟡 Gold `#FFD700` | Pivot element |
| 🔵 Sky Blue `#4FC3F7` | Row being modified (Rᵢ) |
| 🟢 Green `#81C784` | Row used to eliminate (Rⱼ) |
| 🟠 Coral `#FF8A65` | Augmented separator & annotations |
| 🟣 Lavender `#CE93D8` | Final solution |

---

## Tools Used
| Tool | Purpose |
|------|---------|
| [Manim Community](https://www.manim.community/) ≥ 0.18 | Animation engine |
| [ffmpeg](https://ffmpeg.org/) | Silent video concatenation (`-an`) |
| [fpdf2](https://py-fpdf2.readthedocs.io/) | Storyboard PDF generation |
| NumPy / SymPy / fractions | Mathematical verification |
| Python 3.9 | All scripting |

---

## Credits & Acknowledgements
- **Concept:** Gaussian Elimination — standard linear algebra curriculum
- **References:**
  - Strang, G. (2016). *Introduction to Linear Algebra*, 5th ed. Wellesley-Cambridge.
  - Anton, H. & Rorres, C. *Elementary Linear Algebra*, 11th ed. Wiley.
  - Lay, D. *Linear Algebra and Its Applications*, 5th ed. Pearson.
- **Voice-Over:** Recorded by the student using [`Narration_Script.md`](Narration_Script.md).

---

## AI-Use Disclosure
AI tools (Google Antigravity / Gemini) were used to help write the animation code and the narration script text; the voice-over is recorded by the student, and all mathematics was verified by the student.

---

## Placeholders to Fill In
Before submission, replace every occurrence of:
- `[YOUR NAME]` → your actual name
- `[YOUR STUDENT ID]` → your actual student ID
- Rename the repo folder accordingly

---

## Git Setup (push to public GitHub)
```bash
# 1. Initialise git (if not already done)
cd /path/to/M3_AnimationVideo_GaussianElimination_[STUDENTID]
git init
git add .
git commit -m "Initial commit: Gaussian elimination animation video project"

# 2. Create a public repo on GitHub (via browser or gh CLI)
gh repo create M3_AnimationVideo_GaussianElimination_[STUDENTID] --public

# 3. Push
git remote add origin https://github.com/[YOUR_GITHUB_USERNAME]/M3_AnimationVideo_GaussianElimination_[STUDENTID].git
git branch -M main
git push -u origin main
```
