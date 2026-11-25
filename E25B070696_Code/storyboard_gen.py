"""
storyboard_gen.py — Generate Storyboard.pdf with the 6-scene table
───────────────────────────────────────────────────────────────────
Run:  python3 storyboard_gen.py
Output: ../Storyboard.pdf  (repo root)

Requires: fpdf2  (pip install fpdf2)
"""

import os
import sys
from fpdf import FPDF

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT    = os.path.join(REPO_ROOT, "Storyboard.pdf")

# ── Storyboard data ───────────────────────────────────────────────────────────
# Fields: Scene | Purpose | Visual | Narration | Math Plan | Duration
SCENES = [
    {
        "scene":    "1 - Hook / Context",
        "purpose":  "Hook the viewer with an open question. Establish motivation.",
        "visual":   "Title card; 3 equations appear one by one; staircase block hint.",
        "narration":"\"How do we solve 3 equations in 3 unknowns, the way a computer does?\"",
        "math":     "Display the system: x+2y+z=8, 2x+3y+4z=20, 3x+7y+2z=23. No ops yet.",
        "duration": "~0:40",
    },
    {
        "scene":    "2 - Concept Introduction",
        "purpose":  "Define all notation before it is used. State learning objective.",
        "visual":   "General linear system; augmented matrix [A|b] built on screen. "
                    "Three row-op boxes (swap/scale/replace). Learning objective text box.",
        "narration":"Defines: linear system, matrix A, vector b, augmented matrix, "
                    "three row operations, pivot, row-echelon form.",
        "math":     "Ri <-> Rj (swap); Ri -> k*Ri (scale); Ri -> Ri + k*Rj (replace). "
                    "Pivot = first non-zero in a row.",
        "duration": "~0:35",
    },
    {
        "scene":    "3 - Visual Intuition",
        "purpose":  "Build geometric understanding of WHY row ops preserve the solution.",
        "visual":   "2D: two lines at (1,2). Row op rotates one line; intersection fixed. "
                    "3D: parallelogram planes at (1,2,3); one plane rotates; dot stays.",
        "narration":"Explains reversibility: every op can be undone, solution set unchanged.",
        "math":     "2D: x+y=3 and x-y=-1 -> (1,2). R2 -> R2-R1 gives y=2; still (1,2). "
                    "3D: planes for the worked system, intersection (1,2,3).",
        "duration": "~1:00",
    },
    {
        "scene":    "4 - Worked Example",
        "purpose":  "Full step-by-step Gaussian elimination with every number shown.",
        "visual":   "Augmented matrix. Row ops highlighted (blue=target, green=source, "
                    "gold=pivot). Annotation at bottom. Back-sub steps beside matrix.",
        "narration":"Every arithmetic step: R2->R2-2R1, R3->R3-3R1, R3->R3+R2, "
                    "then back-sub for z=3, y=2, x=1.",
        "math":     "R2: [2,3,4,20]-2[1,2,1,8]=[0,-1,2,4]. "
                    "R3: [3,7,2,23]-3[1,2,1,8]=[0,1,-1,-1]. "
                    "R3: [0,1,-1,-1]+[0,-1,2,4]=[0,0,1,3]. z=3,y=2,x=1.",
        "duration": "~1:45",
    },
    {
        "scene":    "5 - Interpretation",
        "purpose":  "Verify the answer; cover special cases (infinite / no solutions).",
        "visual":   "Three check-mark equations (1+4+3=8 etc.). "
                    "Two matrices showing zero-row cases.",
        "narration":"Substitution check. Zero row -> inf solutions; "
                    "[0 0 0|c!=0] -> no solution.",
        "math":     "1(1)+2(2)+1(3)=8; 2(1)+3(2)+4(3)=20; 3(1)+7(2)+2(3)=23. "
                    "Special cases: rank-deficient and inconsistent.",
        "duration": "~0:35",
    },
    {
        "scene":    "6 - Summary & Credits",
        "purpose":  "Reinforce the three takeaways; provide references and AI disclosure.",
        "visual":   "Three numbered takeaway cards. References list. Credits block.",
        "narration":"Row ops preserve solutions. Eliminate below each pivot. "
                    "Back-substitute bottom-up. References, AI disclosure.",
        "math":     "No new mathematics - consolidation only.",
        "duration": "~0:25",
    },
]


class StoryboardPDF(FPDF):
    """Custom FPDF subclass with header and footer."""

    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(30, 30, 80)
        self.cell(0, 10, "M3 Linear Algebra - Gaussian Elimination Animation: Storyboard", align="C")
        self.ln(4)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, "Harshavardhan Rambha  |  E25B070696  |  Internal Assessment", align="C")
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def build_pdf(output_path: str):
    pdf = StoryboardPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()

    # Column widths (landscape A4 = 297mm; margins 10mm each side → 277mm)
    COLS = {
        "Scene":     38,
        "Purpose":   42,
        "Visual":    52,
        "Narration": 52,
        "Math Plan": 60,
        "Duration":  18,
    }
    total_w = sum(COLS.values())   # 262 mm
    margin  = (277 - total_w) / 2 + 10

    # ── Table header ──────────────────────────────────────────────────────────
    pdf.set_x(margin)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(30, 30, 80)
    pdf.set_text_color(255, 255, 255)
    for col, w in COLS.items():
        pdf.cell(w, 8, col, border=1, align="C", fill=True)
    pdf.ln()

    # ── Table rows ────────────────────────────────────────────────────────────
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(20, 20, 20)
    fill_colors = [(245, 247, 255), (255, 255, 255)]

    for i, row in enumerate(SCENES):
        fill = fill_colors[i % 2]
        pdf.set_fill_color(*fill)

        # Calculate row height from MultiCell content
        line_h = 4.5
        values  = [
            row["scene"], row["purpose"], row["visual"],
            row["narration"], row["math"], row["duration"]
        ]
        widths  = list(COLS.values())

        # Find tallest cell to set uniform row height
        max_lines = 1
        for val, w in zip(values, widths):
            chars_per_line = int(w / 2.1)
            lines = sum(
                max(1, (len(para) // chars_per_line) + 1)
                for para in val.split("\n")
            )
            max_lines = max(max_lines, lines)
        row_h = max_lines * line_h + 2

        # Save x position for each cell
        x_start = margin
        y_start = pdf.get_y()
        for val, w in zip(values, widths):
            pdf.set_xy(x_start, y_start)
            pdf.multi_cell(w, line_h, val, border=1, fill=True)
            x_start += w

        # Move to next row
        pdf.set_xy(margin, y_start + row_h)

    pdf.output(output_path)
    print(f"Storyboard PDF written to: {output_path}")


if __name__ == "__main__":
    build_pdf(OUTPUT)
