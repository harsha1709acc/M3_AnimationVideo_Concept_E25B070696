"""
scene4_example.py — Scene 4: Worked Example  (target: ~102 seconds)
─────────────────────────────────────────────────────────────────────
Full step-by-step Gaussian elimination of:
  x + 2y +  z =  8
 2x + 3y + 4z = 20
 3x + 7y + 2z = 23
Then back-substitution to find (x,y,z) = (1,2,3).
Every step is continuously animated; no static hold exceeds ~4 s.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from manim import *
from constants import *
from matrix_helpers import AugmentedMatrixMob, row_op_animation, highlight_pivots


class Scene4Example(Scene):
    """
    Scene 4 — Worked Example
    Storyboard timing: 2:20 – 4:02  (~102 s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── BEAT 1 (~17 s): System -> Augmented Matrix & First Pivot ─────────
        title = Text("Worked Example", font_size=HEADING_FS, color=PIVOT_COLOR, weight=BOLD)
        self.play(Write(title), run_time=0.8)
        self.wait(1.0)
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.3), run_time=0.6)

        sys_eqs = MathTex(
            r"x + 2y + z &= 8 \\",
            r"2x + 3y + 4z &= 20 \\",
            r"3x + 7y + 2z &= 23",
            font_size=BODY_FS - 2,
        )
        brace = MathTex(r"\left\{", font_size=BODY_FS * 2.1, color=PIVOT_COLOR)
        brace.next_to(sys_eqs, LEFT, buff=0.1)
        sys_group = VGroup(brace, sys_eqs).center().shift(LEFT * 3.1 + DOWN * 0.2)

        self.play(Write(brace), Write(sys_eqs), run_time=1.4)
        self.wait(1.5)

        arrow = Arrow(LEFT * 0.2, RIGHT * 1.1, color=ANNOTATION_COLOR, buff=0).shift(DOWN * 0.2)
        aug_label = Text("augmented\nmatrix", font_size=TINY_FS, color=ANNOTATION_COLOR, line_spacing=1.2)
        aug_label.next_to(arrow, UP, buff=0.15)

        mat_rows_init = [
            ["1",  "2",  "1",  "8"],
            ["2",  "3",  "4",  "20"],
            ["3",  "7",  "2",  "23"],
        ]
        aug = AugmentedMatrixMob(mat_rows_init, font_size=BODY_FS - 2, cell_width=0.9, cell_height=0.75)
        aug.shift(RIGHT * 3.0 + DOWN * 0.2)

        self.play(Create(arrow), Write(aug_label), run_time=0.7)
        self.play(Create(aug), run_time=1.2)
        self.wait(1.8)

        self.play(
            FadeOut(sys_group), FadeOut(arrow), FadeOut(aug_label),
            aug.animate.center().shift(UP * 0.25),
            run_time=0.9,
        )

        step_header = Text("Step 0 — Initial Augmented Matrix", font_size=SMALL_FS, color=SUBTITLE_COLOR)
        step_header.next_to(aug, UP, buff=0.55)
        self.play(FadeIn(step_header, shift=UP * 0.1), run_time=0.6)
        self.wait(1.8)

        # Highlight first pivot
        pivot_box = SurroundingRectangle(aug.entries[0][0], color=PIVOT_COLOR, buff=0.12)
        pivot_note = MathTex(r"\text{Pivot 1} = 1", font_size=SMALL_FS, color=PIVOT_COLOR)
        pivot_note.next_to(aug, LEFT, buff=0.6).align_to(aug.entries[0][0], UP)
        self.play(Create(pivot_box), Write(pivot_note), run_time=0.8)
        self.wait(1.8)
        self.play(FadeOut(pivot_box), FadeOut(pivot_note), run_time=0.5)
        self.play(aug.entries[0][0].animate.set_color(PIVOT_COLOR).scale(1.1), run_time=0.4)

        # ── BEAT 2 (~21 s): Step 1  R2 -> R2 - 2*R1 ──────────────────────────
        new_h1 = Text("Step 1: Eliminate below Pivot 1 in Column 1", font_size=SMALL_FS, color=SUBTITLE_COLOR).next_to(aug, UP, buff=0.55)
        self.play(Transform(step_header, new_h1), run_time=0.6)

        target_box1 = SurroundingRectangle(aug.entries[1][0], color=ROW_CHANGE_COLOR, buff=0.1)
        target_lbl1 = Text("Eliminate this 2", font_size=TINY_FS, color=ROW_CHANGE_COLOR).next_to(aug, LEFT, buff=0.5)
        self.play(Create(target_box1), Write(target_lbl1), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(target_box1), FadeOut(target_lbl1), run_time=0.4)

        step1_calc = MathTex(
            r"R_2 \to R_2 - 2R_1 : \quad [2{-}2(1),\;\; 3{-}2(2),\;\; 4{-}2(1),\;\; 20{-}2(8)]",
            font_size=TINY_FS + 2,
            color=ANNOTATION_COLOR,
        ).to_edge(DOWN, buff=0.95)
        step1_res = MathTex(
            r"= [0,\;\; -1,\;\; 2,\;\; 4]",
            font_size=SMALL_FS,
            color=ROW_CHANGE_COLOR,
        ).next_to(step1_calc, DOWN, buff=0.2)

        self.play(Write(step1_calc), run_time=1.8)
        self.wait(2.8)
        self.play(Write(step1_res), run_time=1.1)
        self.wait(2.2)

        row_op_animation(
            self, aug,
            i=1, j=0, k="-2",
            new_row=["0", "-1", "2", "4"],
            annotation_pos=aug.get_top() + UP * 0.25,
        )
        self.play(Indicate(aug.get_row(1), color=ROW_CHANGE_COLOR, scale_factor=1.05), run_time=1.0)
        self.wait(2.2)
        self.play(FadeOut(step1_calc), FadeOut(step1_res), run_time=0.5)

        # ── BEAT 3 (~22 s): Step 2  R3 -> R3 - 3*R1 + Pivot 2 ────────────────
        new_h2 = Text("Step 2: Eliminate the 3 in Row 3, Column 1", font_size=SMALL_FS, color=SUBTITLE_COLOR).next_to(aug, UP, buff=0.55)
        self.play(Transform(step_header, new_h2), run_time=0.6)

        target_box2 = SurroundingRectangle(aug.entries[2][0], color=ROW_CHANGE_COLOR, buff=0.1)
        target_lbl2 = Text("Eliminate this 3", font_size=TINY_FS, color=ROW_CHANGE_COLOR).next_to(aug, LEFT, buff=0.5).shift(DOWN * 0.7)
        self.play(Create(target_box2), Write(target_lbl2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(target_box2), FadeOut(target_lbl2), run_time=0.4)

        step2_calc = MathTex(
            r"R_3 \to R_3 - 3R_1 : \quad [3{-}3(1),\;\; 7{-}3(2),\;\; 2{-}3(1),\;\; 23{-}3(8)]",
            font_size=TINY_FS + 2,
            color=ANNOTATION_COLOR,
        ).to_edge(DOWN, buff=0.95)
        step2_res = MathTex(
            r"= [0,\;\; 1,\;\; -1,\;\; -1]",
            font_size=SMALL_FS,
            color=ROW_CHANGE_COLOR,
        ).next_to(step2_calc, DOWN, buff=0.2)

        self.play(Write(step2_calc), run_time=1.8)
        self.wait(2.8)
        self.play(Write(step2_res), run_time=1.1)
        self.wait(2.2)

        row_op_animation(
            self, aug,
            i=2, j=0, k="-3",
            new_row=["0", "1", "-1", "-1"],
            annotation_pos=aug.get_top() + UP * 0.25,
        )
        self.play(Indicate(aug.get_row(2), color=ROW_CHANGE_COLOR, scale_factor=1.05), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(step2_calc), FadeOut(step2_res), run_time=0.5)

        # Highlight second pivot
        pivot2_box = SurroundingRectangle(aug.entries[1][1], color=PIVOT_COLOR, buff=0.12)
        pivot2_note = MathTex(r"\text{Pivot 2} = -1", font_size=SMALL_FS, color=PIVOT_COLOR)
        pivot2_note.next_to(aug, LEFT, buff=0.55)
        self.play(Create(pivot2_box), Write(pivot2_note), run_time=0.8)
        self.wait(1.8)
        self.play(FadeOut(pivot2_box), FadeOut(pivot2_note), run_time=0.4)
        self.play(aug.entries[1][1].animate.set_color(PIVOT_COLOR).scale(1.1), run_time=0.4)

        # ── BEAT 4 (~20 s): Step 3  R3 -> R3 + R2 & Echelon Form ─────────────
        new_h3 = Text("Step 3: Eliminate below Pivot 2 in Column 2", font_size=SMALL_FS, color=SUBTITLE_COLOR).next_to(aug, UP, buff=0.55)
        self.play(Transform(step_header, new_h3), run_time=0.6)

        step3_calc = MathTex(
            r"R_3 \to R_3 + R_2 : \quad [0{+}0,\;\; 1{+}(-1),\;\; -1{+}2,\;\; -1{+}4]",
            font_size=TINY_FS + 2,
            color=ANNOTATION_COLOR,
        ).to_edge(DOWN, buff=0.95)
        step3_res = MathTex(
            r"= [0,\;\; 0,\;\; 1,\;\; 3]",
            font_size=SMALL_FS,
            color=ROW_CHANGE_COLOR,
        ).next_to(step3_calc, DOWN, buff=0.2)

        self.play(Write(step3_calc), run_time=1.8)
        self.wait(2.8)
        self.play(Write(step3_res), run_time=1.1)
        self.wait(2.2)

        row_op_animation(
            self, aug,
            i=2, j=1, k="+1",
            new_row=["0", "0", "1", "3"],
            annotation_pos=aug.get_top() + UP * 0.25,
        )
        self.play(FadeOut(step3_calc), FadeOut(step3_res), run_time=0.4)

        # Highlight all three pivots and staircase
        echelon_label = Text(
            "Row-Echelon Form achieved! Pivots: 1, -1, 1",
            font_size=SMALL_FS,
            color=VERIFY_COLOR,
        ).to_edge(DOWN, buff=0.85)
        self.play(Write(echelon_label), run_time=0.8)

        highlight_pivots(self, aug, [(0, 0), (1, 1), (2, 2)])

        stair_arrows = VGroup(
            Arrow(aug.entries[0][0].get_center(), aug.entries[1][1].get_center(),
                  color=PIVOT_COLOR, buff=0.25, stroke_width=2.5),
            Arrow(aug.entries[1][1].get_center(), aug.entries[2][2].get_center(),
                  color=PIVOT_COLOR, buff=0.25, stroke_width=2.5),
        )
        self.play(Create(stair_arrows), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(echelon_label), FadeOut(stair_arrows), run_time=0.5)

        # ── BEAT 5 (~24 s): Back-Substitution ────────────────────────────────
        back_sub_title = Text(
            "Back-Substitution (Bottom-Up)",
            font_size=BODY_FS - 2,
            color=ROW_CHANGE_COLOR,
            weight=BOLD,
        ).next_to(aug, UP, buff=0.55)

        self.play(FadeOut(step_header), Write(back_sub_title), run_time=0.7)
        self.play(
            aug.animate.shift(LEFT * 3.2),
            back_sub_title.animate.shift(LEFT * 3.2),
            run_time=0.8,
        )

        # z from row 3
        row3_box = SurroundingRectangle(VGroup(*aug.entries[2]), color=ROW_CHANGE_COLOR, buff=0.1)
        z_eq = MathTex(r"1z = 3 \implies z = 3", font_size=BODY_FS - 2, color=SOLUTION_COLOR).shift(RIGHT * 2.8 + UP * 1.4)
        self.play(Create(row3_box), run_time=0.7)
        self.play(Write(z_eq), run_time=1.4)
        self.play(Indicate(z_eq, color=PIVOT_COLOR, scale_factor=1.06), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(row3_box), run_time=0.4)

        # y from row 2
        row2_box = SurroundingRectangle(VGroup(*aug.entries[1]), color=ROW_CHANGE_COLOR, buff=0.1)
        y_eq1 = MathTex(r"-y + 2(3) = 4", font_size=BODY_FS - 4, color=WHITE).shift(RIGHT * 2.8 + UP * 0.35)
        y_eq2 = MathTex(r"-y = -2 \implies y = 2", font_size=BODY_FS - 4, color=SOLUTION_COLOR).next_to(y_eq1, DOWN, buff=0.22)
        self.play(Create(row2_box), run_time=0.7)
        self.play(Write(y_eq1), run_time=1.2)
        self.wait(1.8)
        self.play(Write(y_eq2), run_time=1.2)
        self.play(Indicate(y_eq2, color=PIVOT_COLOR, scale_factor=1.06), run_time=0.8)
        self.wait(2.2)
        self.play(FadeOut(row2_box), run_time=0.4)

        # x from row 1
        row1_box = SurroundingRectangle(VGroup(*aug.entries[0]), color=ROW_CHANGE_COLOR, buff=0.1)
        x_eq1 = MathTex(r"x + 2(2) + 3 = 8", font_size=BODY_FS - 4, color=WHITE).shift(RIGHT * 2.8 + DOWN * 1.0)
        x_eq2 = MathTex(r"x + 7 = 8 \implies x = 1", font_size=BODY_FS - 4, color=SOLUTION_COLOR).next_to(x_eq1, DOWN, buff=0.22)
        self.play(Create(row1_box), run_time=0.7)
        self.play(Write(x_eq1), run_time=1.2)
        self.wait(1.8)
        self.play(Write(x_eq2), run_time=1.2)
        self.play(Indicate(x_eq2, color=PIVOT_COLOR, scale_factor=1.06), run_time=0.8)
        self.wait(2.2)
        self.play(FadeOut(row1_box), run_time=0.4)

        # Final boxed solution
        sol_text = MathTex(
            r"\boxed{(x,\, y,\, z) = (1,\, 2,\, 3)}",
            font_size=HEADING_FS - 4,
            color=PIVOT_COLOR,
        ).shift(RIGHT * 2.8 + DOWN * 2.55)
        self.play(Write(sol_text), run_time=1.4)
        self.play(Indicate(sol_text, color=SOLUTION_COLOR, scale_factor=1.08), run_time=1.1)
        self.wait(3.8)

        self.play(
            *[FadeOut(m) for m in [
                title, aug, back_sub_title,
                z_eq, y_eq1, y_eq2, x_eq1, x_eq2, sol_text,
            ]],
            run_time=0.8,
        )
        self.wait(0.2)
