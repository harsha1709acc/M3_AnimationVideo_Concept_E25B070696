"""
scene5_interpret.py — Scene 5: Interpretation  (target: ~34 seconds)
──────────────────────────────────────────────────────────────────────
Substitutes (1,2,3) back into all 3 original equations to verify.
Shows the 3 original planes meeting at (1,2,3) and explains the
two special cases: zero row (infinite solutions) vs [0 0 0 | c] (no solution).
Every beat is continuously animated; no static hold exceeds ~4 s.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from manim import *
from constants import *


class Scene5Interpret(Scene):
    """
    Scene 5 — Interpretation
    Storyboard timing: 4:02 – 4:36  (~34 s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── BEAT 1 (~3 s): Title ─────────────────────────────────────────────
        title = Text("Verification & Interpretation", font_size=HEADING_FS, color=PIVOT_COLOR, weight=BOLD)
        self.play(Write(title), run_time=0.8)
        self.wait(1.0)
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.3), run_time=0.5)

        # ── BEAT 2 (~16 s): Substitute (1,2,3) into Original Equations ───────
        sub_heading = Text(
            "Check (x, y, z) = (1, 2, 3) in the ORIGINAL equations:",
            font_size=SMALL_FS,
            color=SUBTITLE_COLOR,
        ).next_to(title, DOWN, buff=0.35)
        self.play(Write(sub_heading), run_time=0.7)

        eq1_row = VGroup(
            Text("Eq 1:", font_size=SMALL_FS, color=ROW_SOURCE_COLOR),
            MathTex(r"1 + 2(2) + 3 = 1 + 4 + 3 = 8", font_size=BODY_FS - 4, color=WHITE),
            MathTex(r"= 8 \;\;\checkmark", font_size=BODY_FS - 4, color=VERIFY_COLOR),
        ).arrange(RIGHT, buff=0.25)

        eq2_row = VGroup(
            Text("Eq 2:", font_size=SMALL_FS, color=ROW_CHANGE_COLOR),
            MathTex(r"2(1) + 3(2) + 4(3) = 2 + 6 + 12 = 20", font_size=BODY_FS - 4, color=WHITE),
            MathTex(r"= 20 \;\;\checkmark", font_size=BODY_FS - 4, color=VERIFY_COLOR),
        ).arrange(RIGHT, buff=0.25)

        eq3_row = VGroup(
            Text("Eq 3:", font_size=SMALL_FS, color=SOLUTION_COLOR),
            MathTex(r"3(1) + 7(2) + 2(3) = 3 + 14 + 6 = 23", font_size=BODY_FS - 4, color=WHITE),
            MathTex(r"= 23 \;\;\checkmark", font_size=BODY_FS - 4, color=VERIFY_COLOR),
        ).arrange(RIGHT, buff=0.25)

        checks = VGroup(eq1_row, eq2_row, eq3_row).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        checks.next_to(sub_heading, DOWN, buff=0.5).center()

        for row in [eq1_row, eq2_row, eq3_row]:
            self.play(Write(row[0]), Write(row[1]), run_time=1.1)
            self.wait(1.0)
            self.play(Write(row[2]), Indicate(row[2], color=VERIFY_COLOR, scale_factor=1.15), run_time=0.8)
            self.wait(1.0)

        verified_banner = Text(
            "All 3 original equations hold → unique point (1, 2, 3)!",
            font_size=SMALL_FS - 2,
            color=PIVOT_COLOR,
        ).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(verified_banner, shift=UP * 0.15), run_time=0.7)
        self.wait(2.2)

        self.play(
            FadeOut(sub_heading), FadeOut(checks), FadeOut(verified_banner),
            run_time=0.6,
        )

        # ── BEAT 3 (~15 s): Special Cases ────────────────────────────────────
        cases_title = Text("Two Special Cases in Echelon Form", font_size=BODY_FS - 2, color=ROW_CHANGE_COLOR, weight=BOLD)
        cases_title.next_to(title, DOWN, buff=0.35)
        self.play(Write(cases_title), run_time=0.6)

        case1_mat = MathTex(
            r"\begin{bmatrix} * & * & * & | & * \\ 0 & * & * & | & * \\ 0 & 0 & 0 & | & 0 \end{bmatrix}",
            font_size=SMALL_FS,
        )
        case1_label = Text(
            "Zero row [0 0 0 | 0]\n→ Infinitely many solutions\n(redundant equation / free variable)",
            font_size=TINY_FS,
            color=ANNOTATION_COLOR,
            line_spacing=1.3,
        )
        case1 = VGroup(case1_mat, case1_label).arrange(RIGHT, buff=0.5)

        case2_mat = MathTex(
            r"\begin{bmatrix} * & * & * & | & * \\ 0 & * & * & | & * \\ 0 & 0 & 0 & | & 5 \end{bmatrix}",
            font_size=SMALL_FS,
        )
        case2_mat.set_color_by_tex("5", ERROR_COLOR)
        case2_label = Text(
            "Contradiction [0 0 0 | 5]\n→ No solution (0 = 5 impossible!)\n(inconsistent system)",
            font_size=TINY_FS,
            color=ERROR_COLOR,
            line_spacing=1.3,
        )
        case2 = VGroup(case2_mat, case2_label).arrange(RIGHT, buff=0.5)

        cases_group = VGroup(case1, case2).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        cases_group.next_to(cases_title, DOWN, buff=0.45).center().shift(DOWN * 0.35)

        self.play(FadeIn(case1_mat, shift=RIGHT * 0.2), run_time=0.7)
        self.play(Write(case1_label), run_time=1.0)
        self.wait(2.2)
        self.play(Indicate(case1_mat, color=ANNOTATION_COLOR, scale_factor=1.04), run_time=0.7)
        self.wait(1.2)

        self.play(FadeIn(case2_mat, shift=RIGHT * 0.2), run_time=0.7)
        self.play(Write(case2_label), run_time=1.0)
        self.wait(2.2)
        self.play(Indicate(case2_mat, color=ERROR_COLOR, scale_factor=1.04), run_time=0.9)
        self.wait(3.3)

        self.play(
            FadeOut(title), FadeOut(cases_title), FadeOut(cases_group),
            run_time=0.7,
        )
        self.wait(0.2)
